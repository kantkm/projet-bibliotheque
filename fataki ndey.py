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