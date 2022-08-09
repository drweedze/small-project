import os

liste_de_course = []

choix_utilisateur = ""

while True:
    print("Choisissez parmi les 5 options suivante :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    choix_utilisateur = input("👉 Votre choix : ")
    
    try:
        choix_utilisateur_int = int(choix_utilisateur)
        
        match choix_utilisateur_int:
            case 1:
                mot_add = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
                liste_de_course.append(mot_add.capitalize())
                os.system('cls')
                os.system('clear')
                print(f"L'élément '{mot_add.capitalize()}' a été ajouté à la liste.")
                print("______________________________________________")
                print()
            case 2:
                mot_remove = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
                liste_de_course.remove(mot_remove.capitalize())
                os.system('cls')
                os.system('clear')
                print(f"L'élément {mot_remove} a été retiré de la liste.")
                print("______________________________________________")
                print()
            case 3:
                os.system('cls')
                os.system('clear')
                print("Voici le contenu de votre liste : ")
                for i, element in enumerate(liste_de_course):
                    print(f"{i+1}. {element}")
                print("______________________________________________")
                print()
            case 4:
                liste_de_course.clear()
                os.system('cls')
                os.system('clear')
                print(f"La liste a été entièrement vidée.")
                print("______________________________________________")
                print()
            case 5:
                os.system('cls')
                os.system('clear')
                break
            case default:
                os.system('cls')
                os.system('clear')
                print("Veuillez taper un nombre entre 1 et 5.")     
                print("______________________________________________")
                print()      
    except:
        os.system('cls')
        os.system('clear')
        print("les caractères ne sont pas autorisés.".capitalize())
        print("______________________________________________")
        print()   

