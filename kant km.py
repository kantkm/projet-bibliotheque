
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

