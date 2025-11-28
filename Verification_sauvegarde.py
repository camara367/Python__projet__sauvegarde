#!/usr/bin/env python3 
import os
def obtenir_infos_dossier(chemin):  
    if not os.path.exists(chemin):
        return None, None

    taille_totale = 0
    nombre_fichiers = 0

    for dossier_actuel,sous_dossier ,fichiers in os.walk(chemin):
        nombre_fichiers = nombre_fichiers +len(fichiers)
        for fichier in fichiers:
            chemin_fichier = os.path.join(dossier_actuel, fichier)
            taille_totale = taille_totale + os.path.getsize(chemin_fichier)

    return nombre_fichiers, taille_totale

def verifier_dossiers():
    
    while True:
        dossier_utilisateur = input("Entrez le chemin du dossier utilisateur : ")
        dossier_sauvegarde = input("Entrez le chemin du dossier de sauvegarde : ")

        if os.path.exists(dossier_utilisateur) and os.path.exists(dossier_sauvegarde):
            return dossier_utilisateur, dossier_sauvegarde
        else:
            print(" Un des dossiers n'existe pas. Veuillez réessayer.")

def menu_verification():
  
    while True:
        print("\n--- Vérification de Sauvegarde ---")
        dossier_utilisateur, dossier_sauvegarde = verifier_dossiers()

        fichiers_utilisateur, taille_utilisateur = obtenir_infos_dossier(dossier_utilisateur)
        fichiers_sauvegarde, taille_sauvegarde = obtenir_infos_dossier(dossier_sauvegarde)

        print("\n ....Vérification en cours...\n")
        if fichiers_utilisateur == fichiers_sauvegarde and taille_utilisateur == taille_sauvegarde:
            print(" Le Backup est correcte !")
        else:
            print(" Sauvegarde incorrecte. Vérifiez les fichiers.")


        recommencer = input("\nVoulez-vous vérifier un autre dossier ? (O/N) : ") #.lower()
        if recommencer != "o":
            print("\n Merci d'avoir utilisé le programme. À bientôt !")
            break

if __name__ == "__main__":
    menu_verification()
