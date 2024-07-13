import json
from datetime import datetime, timedelta

class Livre:
    def __init__(self, id, titre, auteur, genre, disponible=True):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.disponible = disponible

    def __str__(self):
        return f"{self.titre} par {self.auteur} - {'Disponible' if self.disponible else 'Emprunté'}"

class Utilisateur:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.nom} ({self.email})"

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []
        self.historique = []
        self.categories = {}
        self.charger_donnees()

    # Gestion des livres
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print("_____________________________________________________________")
        print(f"Livre ajouté : {livre.titre} par {livre.auteur}")
        print("_____________________________________________________________")

    def supprimer_livre(self, livre_id):
        self.livres = [livre for livre in self.livres if livre.id != livre_id]
        print("_____________________________________________________________")
        print(f"Livre avec ID {livre_id} supprimé")
        print("_____________________________________________________________")

    def lister_livres(self):
        if not self.livres:
            print("_____________________________________________________________")
            print("Aucun livre à lister.")
            print("_____________________________________________________________")
        else:
            for livre in self.livres:
                print(livre)

    def modifier_livre(self, livre_id, titre=None, auteur=None, genre=None, disponible=None):
        livre = next((l for l in self.livres if l.id == livre_id), None)
        if livre:
            if titre: livre.titre = titre
            if auteur: livre.auteur = auteur
            if genre: livre.genre = genre
            if disponible is not None: livre.disponible = disponible

    def trier_livres(self, critere):
        self.livres.sort(key=lambda livre: getattr(livre, critere))

    def rechercher_livre(self, titre=None, auteur=None, genre=None, disponible=None):
        resultats = self.livres
        if titre:
            resultats = [livre for livre in resultats if titre.lower() in livre.titre.lower()]
        if auteur:
            resultats = [livre for livre in resultats if auteur.lower() in livre.auteur.lower()]
        if genre:
            resultats = [livre for livre in resultats if genre.lower() in livre.genre.lower()]
        if disponible is not None:
            resultats = [livre for livre in resultats if livre.disponible == disponible]
        for resultat in resultats:
            print(resultat)

    # Gestion des catégories de livres
    def ajouter_categorie(self, categorie):
        self.categories[categorie] = []
        print("_____________________________________________________________")
        print(f"Categorie ajoutée : {categorie}")
        print("_____________________________________________________________")

    def supprimer_categorie(self, categorie):
        if categorie in self.categories:
            del self.categories[categorie]
            print("_____________________________________________________________")
            print(f"Categorie supprimée : {categorie}")
            print("_____________________________________________________________")

    def lister_categories(self):
        for categorie in self.categories:
            print(categorie)

    def ajouter_livre_a_categorie(self, livre_id, categorie):
        livre = next((l for l in self.livres if l.id == livre_id), None)
        if livre and categorie in self.categories:
            self.categories[categorie].append(livre)
            print("_____________________________________________________________")
            print(f"Livre {livre.titre} ajouté à la catégorie {categorie}")
            print("_____________________________________________________________")

    def lister_livres_par_categorie(self, categorie):
        if categorie in self.categories:
            for livre in self.categories[categorie]:
                print(livre)

    # Gestion des utilisateurs
    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)
        print("_____________________________________________________________")
        print(f"Utilisateur ajouté : {utilisateur.nom} ({utilisateur.email})")
        print("_____________________________________________________________")

    def supprimer_utilisateur(self, utilisateur_id):
        self.utilisateurs = [utilisateur for utilisateur in self.utilisateurs if utilisateur.id != utilisateur_id]
        print("_____________________________________________________________")
        print(f"Utilisateur avec ID {utilisateur_id} supprimé")
        print("_____________________________________________________________")

    def lister_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(utilisateur)

    def modifier_utilisateur(self, utilisateur_id, nom=None, email=None):
        utilisateur = next((u for u in self.utilisateurs if u.id == utilisateur_id), None)
        if utilisateur:
            if nom:
                utilisateur.nom = nom
                print("_____________________________________________________________")
                print(f"Nom de l'utilisateur {utilisateur_id} modifié")
                print("_____________________________________________________________")
            if email:
                utilisateur.email = email
                print("_____________________________________________________________")
                print(f"Email de l'utilisateur {utilisateur_id} modifié")
                print("_____________________________________________________________")

    def trier_utilisateurs(self, critere):
        self.utilisateurs.sort(key=lambda utilisateur: getattr(utilisateur, critere))
        print("_____________________________________________________________")
        print(f"Utilisateurs triés par {critere}")
        print("_____________________________________________________________")

    def rechercher_utilisateur(self, nom=None, email=None):
        resultats = self.utilisateurs
        if nom:
            resultats = [utilisateur for utilisateur in resultats if nom.lower() in utilisateur.nom.lower()]
        if email:
            resultats = [utilisateur for utilisateur in resultats if email.lower() in utilisateur.email.lower()]
        for resultat in resultats:
            print(resultat)

    def lister_emprunts_utilisateur(self, utilisateur_id):
        emprunts = [emprunt for emprunt in self.historique if emprunt['utilisateur_id'] == utilisateur_id and 'date_retour' not in emprunt]
        for emprunt in emprunts:
            livre = next((l for l in self.livres if l.id == emprunt['livre_id']), None)
            if livre:
                print(livre)

    def afficher_historique_utilisateur(self, utilisateur_id):
        historique = [emprunt for emprunt in self.historique if emprunt['utilisateur_id'] == utilisateur_id]
        for entree in historique:
            livre = next((l for l in self.livres if l.id == entree['livre_id']), None)
            if livre:
                action = "emprunté" if 'date_retour' not in entree else "retourné"
                date_action = entree['date_emprunt'] if 'date_retour' not in entree else entree['date_retour']
                print(f"{livre.titre} a été {action} le {date_action}")

    # Gestion des emprunts et retours
    def emprunter_livre(self, utilisateur_id, livre_id):
        utilisateur = next((u for u in self.utilisateurs if u.id == utilisateur_id), None)
        livre = next((l for l in self.livres if l.id == livre_id), None)
        if utilisateur and livre and livre.disponible:
            livre.disponible = False
            emprunt = {"utilisateur_id": utilisateur_id, "livre_id": livre_id, "date_emprunt": datetime.now().isoformat()}
            self.historique.append(emprunt)
            print("_____________________________________________________________")
            print(f"{utilisateur.nom} a emprunté {livre.titre}")
            print("_____________________________________________________________")
        else:
            print("Emprunt impossible")

    def retourner_livre(self, utilisateur_id, livre_id):
        utilisateur = next((u for u in self.utilisateurs if u.id == utilisateur_id), None)
        livre = next((l for l in self.livres if l.id == livre_id), None)
        if utilisateur and livre and not livre.disponible:
            livre.disponible = True
            retour = {"utilisateur_id": utilisateur_id, "livre_id": livre_id, "date_retour": datetime.now().isoformat()}
            self.historique.append(retour)
            print("_____________________________________________________________")
            print(f"{utilisateur.nom} a retourné {livre.titre}")
            print("_____________________________________________________________")
        else:
            print("Retour impossible")

    def alertes_retard(self):
        retards = []
        for emprunt in self.historique:
            if 'date_retour' not in emprunt:
                date_emprunt = datetime.fromisoformat(emprunt['date_emprunt'])
                if datetime.now() - date_emprunt > timedelta(days=14):  # Supposons un délai de retour de 14 jours
                    utilisateur = next((u for u in self.utilisateurs if u.id == emprunt['utilisateur_id']), None)
                    livre = next((l for l in self.livres if l.id == emprunt['livre_id']), None)
                    retards.append((utilisateur, livre))
        for utilisateur, livre in retards:
            print("_____________________________________________________________")
            print(f"ALERTE: {utilisateur.nom} est en retard pour le retour de {livre.titre}")
            print("_____________________________________________________________")

    def lister_utilisateurs_en_retard(self):
        retards = set()
        for emprunt in self.historique:
            if 'date_retour' not in emprunt:
                date_emprunt = datetime.fromisoformat(emprunt['date_emprunt'])
                if datetime.now() - date_emprunt > timedelta(days=14):
                    utilisateur = next((u for u in self.utilisateurs if u.id == emprunt['utilisateur_id']), None)
                    if utilisateur:
                        retards.add(utilisateur)
        for utilisateur in retards:
            print("_____________________________________________________________")
            print(f"{utilisateur.nom} est en retard pour le retour d'un livre")
            print("_____________________________________________________________")

    # Gestion des fichiers CSV
    def importer_livres_csv(self, chemin):
        import csv
        with open(chemin, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                livre = Livre(**row)
                self.ajouter_livre(livre)
        print("_____________________________________________________________")
        print("Importation des livres à partir du fichier CSV réussie")
        print("_____________________________________________________________")

    def exporter_livres_csv(self, chemin):
        import csv
        with open(chemin, 'w', newline='') as csvfile:
            fieldnames = ['id', 'titre', 'auteur', 'genre', 'disponible']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for livre in self.livres:
                writer.writerow(livre.__dict__)
        print("_____________________________________________________________")
        print("Exportation des livres vers un fichier CSV réussie")
        print("_____________________________________________________________")

    def importer_utilisateurs_csv(self, chemin):
        import csv
        with open(chemin, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                utilisateur = Utilisateur(**row)
                self.ajouter_utilisateur(utilisateur)
        print("_____________________________________________________________")
        print("Importation des utilisateurs à partir du fichier CSV réussie")
        print("_____________________________________________________________")

    def sauvegarder_donnees(self):
        with open('livres.json', 'w') as livres_file:
            json.dump([livre.__dict__ for livre in self.livres], livres_file)
        with open('utilisateurs.json', 'w') as utilisateurs_file:
            json.dump([utilisateur.__dict__ for utilisateur in self.utilisateurs], utilisateurs_file)
        with open('historique.json', 'w') as historique_file:
            json.dump(self.historique, historique_file)
        print("_____________________________________________________________")
        print("Données sauvegardées avec succès")
        print("_____________________________________________________________")

    def charger_donnees(self):
        try:
            with open('livres.json', 'r') as livres_file:
                self.livres = [Livre(**data) for data in json.load(livres_file)]
        except FileNotFoundError:
            self.livres = []

        try:
            with open('utilisateurs.json', 'r') as utilisateurs_file:
                self.utilisateurs = [Utilisateur(**data) for data in json.load(utilisateurs_file)]
        except FileNotFoundError:
            self.utilisateurs = []

        try:
            with open('historique.json', 'r') as historique_file:
                self.historique = json.load(historique_file)
        except FileNotFoundError:
            self.historique = []
        

print("***MENU BIBLIOTHEQUE***")

def menu():
    print("*******************************************************************************")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Lister les livres")
    print("4. Ajouter un utilisateur")
    print("5. Supprimer un utilisateur")
    print("6. Lister les utilisateurs")
    print("7. Emprunter un livre")
    print("8. Retourner un livre")
    print("9. Sauvegarder les données")
    print("10. Charger les données")
    print("11. Rechercher un livre")
    print("12. Voir les alertes de retard")
    print("13. Modifier les informations d'un utilisateur")
    print("14. Afficher les livres empruntés par un utilisateur")
    print("15. Afficher l'historique d'un utilisateur")
    print("16. Trier les utilisateurs")
    print("17. Recherche avancée d’utilisateurs")
    print("18. Importer des données d'utilisateurs à partir d'un fichier CSV")
    print("19. Afficher les utilisateurs ayant des retards")
    print("0. Quitter")
    print("*******************************************************************************")

def main():
    biblio = Bibliotheque()
    while True:
        menu()
        choix = input("Choisissez une option: ")
        if choix == "1":
            print("_____________________________________________________________")
            id = input("ID du livre: ")
            print("_____________________________________________________________")
            titre = input("Titre du livre: ")
            print("_____________________________________________________________")
            auteur = input("Auteur du livre: ")
            print("_____________________________________________________________")
            genre = input("Genre du livre: ")
            print("_____________________________________________________________")
            livre = Livre(id, titre, auteur, genre)
            biblio.ajouter_livre(livre)
        elif choix == "2":
            id = input("ID du livre à supprimer: ")
            print("_____________________________________________________________")
            biblio.supprimer_livre(id)
        elif choix == "3":
            biblio.lister_livres()
        elif choix == "4":
            id = input("ID de l'utilisateur: ")
            print("_____________________________________________________________")
            nom = input("Nom de l'utilisateur: ")
            print("_____________________________________________________________")
            email = input("Email de l'utilisateur: ")
            print("_____________________________________________________________")
            utilisateur = Utilisateur(id, nom, email)
            biblio.ajouter_utilisateur(utilisateur)
        elif choix == "5":
            id = input("ID de l'utilisateur à supprimer: ")
            print("_____________________________________________________________")
            biblio.supprimer_utilisateur(id)
        elif choix == "6":
            biblio.lister_utilisateurs()
        elif choix == "7":
            utilisateur_id = input("ID de l'utilisateur: ")
            print("_____________________________________________________________")
            livre_id = input("ID du livre à emprunter: ")
            print("_____________________________________________________________")
            biblio.emprunter_livre(utilisateur_id, livre_id)
        elif choix == "8":
            utilisateur_id = input("ID de l'utilisateur: ")
            print("_____________________________________________________________")
            livre_id = input("ID du livre à retourner: ")
            print("_____________________________________________________________")
            biblio.retourner_livre(utilisateur_id, livre_id)
        elif choix == "9":
            biblio.sauvegarder_donnees()
        elif choix == "10":
            biblio.charger_donnees()
        elif choix == "11":
            terme = input("Entrez le titre ou l'auteur du livre à rechercher: ")
            print("_____________________________________________________________")
            biblio.rechercher_livre(titre=terme, auteur=terme)
        elif choix == "12":
            biblio.alertes_retard()
        elif choix == "13":
            id = input("ID de l'utilisateur à modifier: ")
            print("_____________________________________________________________")
            nom = input("Nouveau nom (laisser vide pour ne pas modifier): ")
            print("_____________________________________________________________")
            email = input("Nouvel email (laisser vide pour ne pas modifier): ")
            print("_____________________________________________________________")
            biblio.modifier_utilisateur(id, nom if nom else None, email if email else None)
        elif choix == "14":
            id = input("ID de l'utilisateur: ")
            print("_____________________________________________________________")
            biblio.lister_emprunts_utilisateur(id)
        elif choix == "15":
            id = input("ID de l'utilisateur: ")
            print("_____________________________________________________________")
            biblio.afficher_historique_utilisateur(id)
        elif choix == "16":
            critere = input("Critère de tri (nom, email): ")
            print("_____________________________________________________________")
            biblio.trier_utilisateurs(critere)
        elif choix == "17":
            nom = input("Nom de l'utilisateur (laisser vide pour ignorer): ")
            print("_____________________________________________________________")
            email = input("Email de l'utilisateur (laisser vide pour ignorer): ")
            print("_____________________________________________________________")
            biblio.rechercher_utilisateur(nom if nom else None, email if email else None)
        elif choix == "18":
            chemin = input("Chemin du fichier CSV: ")
            print("_____________________________________________________________")
            biblio.importer_utilisateurs_csv(chemin)
        elif choix == "19":
            biblio.lister_utilisateurs_en_retard()
        elif choix == "0":
            break
        else:
            print("Choix non valide.")

if __name__ == "__main__":
    main()

