from random import randint
import getpass


##################################################################################################################################################
####################################################'''Le Mot Le Plus Long'''#############################################################################
##################################################################################################################################################
def LETTRE():
    print("""---------------------LeMotLePlusLong-------------------
    Regle du Jeu:.
    Les Joueur 1 et Joueur 2 choissient a tour de role:
    - une voyelle ou une consonne avec les touche (c ou v)
    - Puis chacun formera un mot avec les lettre de la liste renvoyé
    - Le Joueur Gagne s'il utilise le plus de lettre que le joueur 2
    --------------------------------------------------------------""")  
    #Les principales Listes
    consonne=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    voyelle=['a','e','i','o','u','y']
    #----------------------------------------------------------------------------------------------------------
    def renvoie(choix):
                '''Renvoie un Tirage de lettre choix dans les liste Voyelle et Consonne
                   parametre:choix ,entré d'une variable type (str)
                   renvoie:lite de 10 letrre'''
                Tirage_Final=[]
               #tant que le tirage n'a pas atteint 10
                for lettre in range(10):
                        n=0
                        #Ajout D'une Boucle While qui tant que le choix n'est pas [c]ou[v] on redemande
                        while choix!='c' and choix!='v':
                            print('erreur vous ne pouvez pas entrez cette lettre')
                            choix=input('faites un choix entre c et v')
                            n+=1
                        if choix=='c':
                                    Tirage_Final+=consonne[randint(0,len(consonne)-1)]                                                           
                                    print(Tirage_Final)
                                    choix=input('faites votre choix entre c et v:')                                                                                      
                                                        
                        elif choix =='v':
                                    Tirage_Final+=voyelle[randint(0,len(voyelle)-1)]
                                    
                                    print(Tirage_Final)
                                    choix=input('faites votre choix entre c et v:')
                                
                               
                     
                return Tirage_Final

    choix=input('faites votre choix entre c et v:')
    #joueur2=input('J2 faites votre choix entre c et v:')
    Tirage=renvoie(choix)
    print("Formez un mot avec les lettre en miniscule",Tirage)
    #
    def copie_lst(lst):
        '''copie de liste
           parametre liste:lst,liste qu'on copie
           renvoie:la copie de la liste'''
        
        copie_lst=[]
        for e in range(len(lst)) :
            copie_lst.append(lst[e])
        return(copie_lst)

    #
    #Modification de la Fonction lettre qui verifie si le mot est dans le dico
    def lettre(joueur,Tirage):
        '''verifie si les lettre du mot sont dans le dico
           parametre joueur,Tirage:Joueur:input type(str),Tirage:liste de lettre type(lst)
           renvoie:True si le mot est dans le dictionnaire fourni False sinon'''
        
        lexique = []
        with open('francais.txt', 'r') as mon_fichier:
            for line in mon_fichier:#pour chaque ligne de mon_fichier
                lexique.extend(line.split())#on l'ajoute a la liste
        #return True si mot dans liste False Sinon
        if joueur in lexique :
                return True	
        else :
                return False	
     

    #
    def verif_lettre_dans_liste(Tirage,joueur):
        '''verifie si les elements du mot sont dans le Tirage
           parametre Tirage,Joueur: Tirage:liste de lettre type(str), joueur:input type(str)
           renvoie:True si les lettre de joueur sont dans la liste False sinon'''
        
        copie_de_lst=copie_lst(lst)#appel de fonction
        for e in range(len(joueur)):
            #si lettre de joueur n'est pas liste return False,True sinon
            if joueur[e] not in copie_de_lst :
                return False
            elif e in Tirage :
                copie_de_lst.pop(copie_de_lst.index(joueur[e]))
        return(True)

    #methode du dico originel qui marchait pas
    #fichier=open('francais.txt','r')
    #dico={}
    #dico[1]={fichier}
    #
    joueur1=getpass.getpass("J1 entrez un mot:")#joueur 1 entre son mot qui est sensé etre caché
    joueur2=getpass.getpass("J2 entrez un mot:")#joueur 2 entre son mot qui est sensé etre caché
    print("Joueur 1 a tapé:",joueur1)
    print("Joueur 2 a tapé:",joueur2)
    #Verifie si les lettre de J1 et J2 sont dans le Tirage
    lettre(joueur1,Tirage)
    lettre(joueur2,Tirage)
    #--------------------------------------------------------------------------------------------------------------
    def Vainqeur(joueur1,joueur2):
        '''Fonction qui definie celui qui a le mot le plus long
           parametre joueur1,joueur2:joueur1,joueur2:input type(str)
           renvoie:Le Gagnant de la partie'''
        #joueur1 gagne la partie car lettre J2=False
        if lettre(joueur1,Tirage)==True and lettre(joueur2,Tirage)==False:
                print('J1 a gagné,les lettres de j2 ne sont pas valide')
                
        #joueur 2 gagne la partie car lettre J1=False
        if lettre(joueur1,Tirage)==False and lettre(joueur2,Tirage)==True:
                print('J2 a gagné,les lettres de j1 ne sont pas valide')
                
        #J1 et J2 ont perdu car leur lettre ne sont pas bon
        if lettre(joueur1,Tirage)==False and lettre(joueur2,Tirage)==False:
                print("J1 et J2 ont perdu,leurs lettres ne sont pas valide")
                
        #J1 et J2 ==True
        if lettre(joueur1,Tirage)==True and lettre(joueur2,Tirage)==True:
                
                # joueur 1 gagne car J1>a J2
                if len(joueur1)>len(joueur2):
                    print('Joueur1 a Gagné la Partie')
                    
                #J2 gagne car J2>J1
                elif len(joueur1)<len(joueur2):
                    print("joueur2 a gagné")
                    
                #personne gagne car egalité
                elif len(joueur1)==len(joueur2):
                    print('égalité')
          
           
        


        
    Vainqeur(joueur1,joueur2)




###############################################################################################################################
######################################################'''CHIFFRE'''##################################################################
###############################################################################################################################
def CHIFFRE():
    print("""----------------LeCompteEstBon------------------------
    Regle du Jeu:
    - le jeu donne un nombre et une liste de chiffre de taille n
    - Les Joueur 1 commence et entre ses operation puis c'est au tour du joueur 2:
    - Le joueur entre ses operation avec les elements de la liste 
    - Le gagnant est celui qui trouve le nombre avec le moins d'opération
    --------------------------------------------------------------""")
    def liste_nbr_utilise(lst):
        '''Fonction qui creer et renvoie une liste aléatoire de taille 5
           Parametre lst:liste aléatoire type(lst)
           Renvoie:liste_nbr_utilise'''
        
        liste_nbr_utilise = []
        for e in range(5):
            x=randint(0,len(lst)-1)
            y=lst[x]
            liste_nbr_utilise.append(y)# selectionne 5 nombre parmi la liste a dispostion 
            lst.pop(x)
        return(liste_nbr_utilise)


    def recup_premier_nombre(chaine):
        '''Fonction qui permet de recuper le premier nombre
           Parametre chaine:input du premier nombre type(str)
           Renvoie:int du Premier Nombre'''
        x=''
        i=0
        while i <=len(chaine)-1:                    # lorsque l'on tape l operation isole puis recupere le premier nombre  
            x=x+str(chaine[i])
            i=i+1
            if chaine[i]=='+' or chaine[i]=='-' or chaine[i]=='/' or chaine[i]=='*' :
                return(int(x))
        


    def recup_second_nombre(chaine):
        '''Fonction qui permet de recuperer le second nombre
           parametre chaine:input de l'operende type(str)
           Renvoie:int du Second nombre'''
        i=0
        while i <=len(chaine)-1: 
            i=i+1
            if chaine[i]=='+' or chaine[i]=='-' or chaine[i]=='/' or chaine[i]=='*' :
                i=i+1
                x=''
                while i<=len(chaine)-1:                      # lorsque l'on tape l operation isole puis recupere le second nombre
                    x=x+str(chaine[i])
                    i=i+1
                return(int(x))

    def recup_signe(chaine):
        '''Fonction qui permet de recuperer le signe
           Parametre chaine:input de l'operande
           Renvoi:renvoi l'operande'''
        i=0
        while i<=len(chaine)-1:
            if chaine[i]=='+' or chaine[i]=='-' or chaine[i]=='/' or chaine[i]=='*' : # lorsque l'on tape l operation isole puis recupere le signe
                return(chaine[i])
            i=i+1

    def utilisation_signe(x1,x2,signe):
        '''Fonction qui complete et forme l'operation
           Parametre (x1,x2,signe):x1:Premier Nombre,x2:Second Nombre,signe:signe de l'operation
           Renvoie:y resultat de l'operation'''
        if signe=='+':
            y= x1 + x2
            return(y)
        if signe=='-':
            y= x1 - x2
            return(y)             # utilise le return des fonctions precedente pour effectuer l'operation 
        if signe=='*':
            y= x1 * x2
            return(y)
        if signe=='/':
            y= x1 / x2
            return(y)




    def copie_lst(lst):
        '''copie de la liste'''
        copie_lst=[]
        for e in range(len(lst)) :         # copie la liste de nombre a disposition pour ne pas la modifier 
            copie_lst.append(lst[e])
        return(copie_lst)


    def decision_du_vainqueur(premier_resulat,deuxieme_resultat,nbr_objctif):
        '''Fonction qui designe le Vainqueur
           Parametre (premier_resultat,deuxieme_resultat_nbr_objctif)
           Renvoie:le gagnant'''
        if premier_resulat >= nbr_objectif :
                decision_du_vainqueur_1 = resultat_de_j1 - nbr_objectif
        else :
                decision_du_vainqueur_1 = nbr_objectif - resultat_de_j1        # decide qui est le vainqueur 
        if deuxieme_resultat >= nbr_objectif :
                decision_du_vainqueur_2 = resultat_de_j2 - nbr_objectif
        else :
                decision_du_vainqueur_2 = nbr_objectif - resultat_de_j2
        if decision_du_vainqueur_1 < decision_du_vainqueur_2 :
                print('joueur 1 a gagné')
        if decision_du_vainqueur_1 > decision_du_vainqueur_2 :
                print('joueur 2 a gagné')
        if decision_du_vainqueur_1 == decision_du_vainqueur_2 :
                print(' il y a egalité j1 et j2 ont gagné')
        


    nbr_objectif=randint(25,500)

    liste_de_nbr_utilisable=[1,2,3,4,5,6,7,8,9,10,25,25,50,75,75,100,100]    

    liste_nbr_utilise=liste_nbr_utilise(liste_de_nbr_utilisable)

    print('joueur 1 vous commencez')

    def le_compte_est_bon(lst):
        '''Fonction qui verifie si le joueur a trouver le bon nombre
           Parametre lst:liste type(lst)
           Renvoi:resultat'''
        copie_de_lst=copie_lst(lst)
        print('tirage courant :' ,copie_de_lst, 'objectif :' ,nbr_objectif)
        operation_joueur=input('entrez votre operation ou [f]ini : ')
        while operation_joueur!='f': 
                premier_nombre = recup_premier_nombre(operation_joueur)
                second_nombre = recup_second_nombre(operation_joueur)                     # supprime les nombres de loperation et ajoute à la liste le resultat de l'operation  
                signe = recup_signe(operation_joueur)
                resultat = utilisation_signe(premier_nombre,second_nombre,signe)
                copie_de_lst.pop(copie_de_lst.index(premier_nombre))
                copie_de_lst.pop(copie_de_lst.index(second_nombre))
                copie_de_lst.append(resultat)
                if resultat == nbr_objectif :
                        print('le compte est bon')
                        return(resultat)
                print('tirage courant :' ,copie_de_lst, 'objectif :' ,nbr_objectif )
                operation_joueur=input('entrez un autrre operation ou [f]ini : ')
                
        return(resultat)


    resultat_de_j1=le_compte_est_bon(liste_nbr_utilise)

    print('joueur 2 cest a vous ')

    resultat_de_j2=le_compte_est_bon(liste_nbr_utilise)

    decision_du_vainqueur(resultat_de_j1,resultat_de_j2,nbr_objectif)

#################################################################
#################Menu############################################
def menu():
        '''simulation du menu du jeu avec 1 pour Lettre , 2 pour Chiffre
           3 Pour Abondonner et 4 pour la difficulté
	   parametre:rien
	   renvoie:L'un des deux programme'''
        
        print('''##################################################################
                 ############### DES CHIFFRES ET DES LETTRES ######################
                               1- Jouer une partie de lettres  
                               2- Jouer une partie de chiffres
                               3-Pour Fuir Le Jeu Abondonner Le Jeu
                               4-Changer La Difficulté[En chantier...:):):)]
               ---------------------------------------------------------------------''')


         
        manche=int(input("Combien de manche voulez vous Faire:"))
     
        #i=0
        for i in range(manche):
            choix = input("Quelle partie voulez-vous lancer ? : ")
            
            if choix == "1" :
                LETTRE()
            elif choix == "2" :
                CHIFFRE()
            elif choix =="3":
                break
            #elif choix=="4"
                #mode=input('Vous Avez le choix entre[F]acile--[M]oyen--[D]ifficile--[E]xtreme')
                #if mode=='F':
                #elif mode=='M':
                #elif mode=='D':
                #elif mode=='E'
           
           
menu()






	
