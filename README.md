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
