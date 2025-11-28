# Python__projet__sauvegarde
#le projet consiste a créé un programme de sauvegarde
#!/usr/bin/env python3 
import platform
import psutil
import os
import wmi

def obtenir_version_bios(): #fonction  pour récupèrer la version du BIOS
    
    if platform.system() == "Windows":
       
            c = wmi.WMI()
            for bios in c.Win32_BIOS():
                return bios.Version
        
    else:
        return "Non disponible sur ce système"

def obtenir_espace_disque_libre(): # fonction pour obtenir l'espace du disque
    
    disque = psutil.disk_usage('/')
    return f"{disque.free / (1024 ** 3):} Go" 

def obtenir_ram_disponible(): # Fonction Pour la memoire ram disponible
   
    ram = psutil.virtual_memory()
    return f"{ram.available / (1024 ** 3):.} Go"

def obtenir_version_os(): # fonction pour la version du système
    
    return platform.version()
# Le menu pour les différents options 
def afficher_menu():
    print('--- PC INFO ---')
    print('1. Version du BIOS')
    print('2. Espace libre sur le disque')
    print('3. RAM disponible')
    print('4. Version du système d\'exploitation')
    print('5. Quitter')
#  la fonction pour enregistrer les informations dans un fichier .txt
def sauvegarder_infos(donnees, nom_fichier):
    dossier = r'C:\PCInfo'
    chemin_fichier = os.path.join(dossier, nom_fichier)
    if not os.path.exists(dossier): # condition pour voir si le dossier n'exite pas  il crée
        os.makedirs(dossier)
    if not nom_fichier.endswith('.txt'):
        print(" Le nom du fichier doit se terminer par .txt")
        return
    with open(chemin_fichier, 'a') as fichier:
        for cle, valeur in donnees.items():
            fichier.write(f"{cle}: {valeur}\n")
    print(f" Les informations ont été enregistrées dans {chemin_fichier}")

def Analyse_Systeme():
    while True:
        afficher_menu()
        choix = input('Choisissez une option : ')
        infos = {}

        if choix == '1':
            infos['Version du BIOS'] = obtenir_version_bios()
            print(f"Version du BIOS: {infos['Version du BIOS']}")
        elif choix == '2':
            infos['Espace libre sur le disque'] = obtenir_espace_disque_libre()
            print(f"Espace libre: {infos['Espace libre sur le disque']}")
        elif choix == '3':
            infos['RAM disponible'] = obtenir_ram_disponible()
            print(f"RAM disponible: {infos['RAM disponible']}")
        elif choix == '4':
            infos['Version du système d\'exploitation'] = obtenir_version_os()
            print(f"Version du système d\'exploitation: {infos['Version du système d\'exploitation']}")
        elif choix == '5':
            break
        else:
            print('Option invalide. Veuillez réessayer.')

        if infos:
           while True:
                nom_fichier = input("Entrez le nom du fichier pour enregistrer les informations (ex: info.txt) : ")
                if nom_fichier.endswith('.txt'):
                    sauvegarder_infos(infos, nom_fichier)
                    break
                else:
                    print(" Le nom du fichier doit se terminer par .txt. Réessayez.")
            

if __name__ == "__main__":
   Analyse_Systeme()
