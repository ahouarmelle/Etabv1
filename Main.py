import fonction
from Personne import *
from Utilisateur import *



eleves = []
professeurs = []


def ajout_elev ():
    try:
        id = int(input("Veuillez entrer votre id : "))
    except:
        print("Vous devez entrer un nombre entier")
        id = int(input("Veuillez entrer votre id : ")) 

    try:
        dateNaissance = input("Veuillez entrer votre date de naissance : ")
    except:
        print("Vous devez entrer un nombre entier")
    
        dateNaissance = input("Veuillez entrer votre date de naissance : ")

    ville= input("Veuillez entrer votre ville : ")
    nom = input("Veuillez entrer votre nom : ")
    prenom = input("Veuilllez entrer vos prénoms : ")
    
    classe = input("Veuillez entrer votre classe : ")

    eleve = Eleve(id,dateNaissance,ville,nom,prenom,classe)
    
    eleves.append(eleve)
    print("Elève ajouter avec success")

def list_elev():
    if not eleves:
        print("Pas d'élève")
        return
    for eleve in eleves:
        print(eleve)


def suppr_elev():
    try:
        choix_id = int(input("Entrer l'id de l'élève à supprimer: "))
    except:
        print("Vous devez entrer un nombre entier")
    
    for eleve in eleves:
        if eleve.id == choix_id :
            eleves.remove(eleve)
            print("Elève supprimé avec success")
            return
    print("Elève inexistant")

def obt_elev_der():
    if eleves:
        dernier = eleves[-1]
        print(f"Le dernier élève saisie est : {dernier}")
    else:
        print("Pas d'élève")

def modif_elev(cho_mod):
    
    if cho_mod == 1:
        try:
            choix_id1 = int(input("Entrer l'id de l'élève à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for eleve in eleves:
            if eleve.id == choix_id1 :
                nom = input("Veuillez entrer un nouveau nom : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mod == 2:
        try:
            choix_id1 = int(input("Entrer l'id de l'élève à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for eleve in eleves:
            if eleve.id == choix_id1 :
                prenom = input("Veuillez entrer un nouveau prénom : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mod == 3:
        try:
            choix_id1 = int(input("Entrer l'id de l'élève à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for eleve in eleves:
            if eleve.id == choix_id1 :
                dateNaissance = input("Veuillez entrer la nouvelle date de naissance : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mod == 4:
        try:
            choix_id1 = int(input("Entrer l'id de l'élève à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for eleve in eleves:
            if eleve.id == choix_id1 :
                ville = input("Veuillez entrer la nouvelle ville : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mod == 5:
            try:
                choix_id1 = int(input("Entrer l'id de l'élève à modification: "))
            except:
                print("Vous devez entrer un nombre entier")
        
            for eleve in eleves:
                if eleve.id == choix_id1 :
                    classe = input("Veuillez entrer la nouvelle classe : ")
                    print("Modification effectuée")
                    return
            print("Elève inexistant")
    
    elif cho_mod == 6:
        fonction.menu()

def men(choix):
    if choix == 1 :
        fonction.men_elev()
        choix1 = int(input("Enter votre choix: "))
        
        choi_elev(choix1)
        
    elif choix ==2 :
        fonction.men_prof()
        choix2 = int(input("Enter votre choix: "))
        choi_prof(choix2)
    elif choix == 3 :
        print("Version suivante")

    elif choix == 0 :
            print("Au revoir")
            

def ajout_prof():
    try:
        id = int(input("Veuillez entrer votre id : "))
    except:
        print("Vous devez entrer un nombre entier")
        id = int(input("Veuillez entrer votre id : "))

    dateNaissance = input("Entrer votre date de naissance: ")
    ville = input("Enter votre ville : ")
    nom = input("   Enter votre nom : ")
    prenom = input("Entrer votre prenom : ")
    try:
        vacant = input("Etes-vous vacant? oui ou non : ").strip().lower()
        if vacant =="oui":
            mo_bool = True
        elif vacant == "non":
            mo_bool = False
    except:
            print("La reponse n'est pas un booleen")
    
    professeur = Professeur(id,dateNaissance,ville,nom,prenom,vacant,)
    
    professeurs.append(professeur)

def list_prof():
    if not professeurs:
        print("Pas de professeur")
        return
    for professeur in professeurs:
        print(professeur)

def suppr_prof():
    choi_prof = int(input("Entrer l'id du professeur"))
    for professeur in professeurs:
        if professeur.id == choi_prof :
            professeurs.remove(professeur)
            print("Professeur supprimé avec success")
            return
    print("Professeur inexistant")

def obt_prof_der():
    if professeurs:
        dernier1 = professeurs[-1]
        print(f"Le dernier professeur saisie est : {dernier1}")
    else:
        print("Pas de professeur")

def modif_prof(cho_mop):
    if cho_mop == 1:
        try:
            choip_id1 = int(input("Entrer l'id du professeur à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for professeur in professeurs:
            if professeur.id == choip_id1 :
                nom = input("Veuillez entrer un nouveau nom : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mop == 2:
        try:
            choip_id1 = int(input("Entrer l'id du professeur à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for professeur in professeurs:
            if professeur.id == choip_id1 :
                prenom = input("Veuillez entrer un nouveau prénom : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mop == 3:
        try:
            choip_id1 = int(input("Entrer l'id du professeur à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for professeur in professeurs:
            if professeur.id == choip_id1 :
                dateNaissance = input("Veuillez entrer la nouvelle date de naissance : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    elif cho_mop == 4:
        try:
            choip_id1 = int(input("Entrer l'id du professeur à modification: "))
        except:
            print("Vous devez entrer un nombre entier")
    
        for professeur in professeurs:
            if professeur.id == choip_id1 :
                ville = input("Veuillez entrer la nouvelle ville : ")
                print("Modification effectuée")
                return
        print("Elève inexistant")

    
    elif cho_mop == 5:
        fonction.menu()





def choi_prof(choix2):
    if choix2 == 1:
        ajout_prof()
    elif choix2 == 2:
        suppr_prof()
    elif choix2 == 3:
        modif_prof()
    elif choix2 == 4:
        list_prof()
    elif choix2 == 5:
        obt_prof_der()
    elif choix2 == 6:
        fonction.menu()
    elif choix2 == 0:
        fonction.connexion()
    



def choi_elev(choix1):
    if choix1 == 1:
        ajout_elev()
    elif choix1 == 2:
        suppr_elev()
    elif choix1 == 3:
        fonction.modifier()
        cho_mod = int(input("Entrer le numero de la modification "))
        modif_elev(cho_mod)

    elif choix1 == 4:
        list_elev()
    elif choix1 == 5:
        obt_elev_der()
    elif choix1 == 6:
        fonction.menu()
    elif choix1 == 0:
        fonction.connexion()
    else:
        print("Choix invalide")

fonction.connexion()
identifiant = input("Entrer un identifiant: ")
mot_de_passe = input("Entrer un mot de passe: ")
def main():
    #utilisateur = Utilisateur("admin","admin") utilisateur.connex()
    if  identifiant == "admin" and mot_de_passe == "admin":
        print("ok")
        while True:
            fonction.menu()
            try:
                choix = int(input("Veuillez choisir l'option: "))

                if choix == 0:
                    print("Fermeture du menu")
                    break

                else:
                    men(choix)
            except ValueError:
                print("Vous devez entrer un nombre entier")
              
    else:
        print("mot de passe erroné")
            


if __name__ == "__main__":
    main()
