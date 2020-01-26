from bs4 import BeautifulSoup
import urllib.request
import sys
import math
import os



i = 1
liens = []
listeLiens = []
listeURLPage = []
listeTitrePage = []
nbTourApparitionChoix = 0
nbApparitionChoix = 0
tour = 0
numeroLien = 0
compteurHistorique = 0
lienPage = ''
retour = False
titreJeuPlusTour = '********** Wikigame ********** ' + "tour "
titreDepart = ''
titreActuel = ''
titreCible = ''

temps = ''

class Lien(): 

    def __init__(self, index, nom, url):
        self.index = index
        self.nom = nom
        self.url = url


def ChoixNumero():
    choix = input("\nVotre choix : ")
    
    global nbTourApparitionChoix
    global nbApparitionChoix
    global liens
    global tour
    global lienPage
    global numeroLien
    global retour
    global listeTitrePage
    global titreCible    
    
    retour = False
    
    if choix == '99':
        
        os.system("cls")
        
        print(titreJeuPlusTour + str(tour) + '\n')
        print("Départ : "+titreDepart)
        print("Cible : "+titreCible)
        if tour == 1:
            print("Actuellement : "+titreDepart+'\n')
        else:
            print("Actuellement : "+titreActuel)
            print("\n00 - Retour / "+titreDepart+'\n')
        
        if nbTourApparitionChoix != nbApparitionChoix:
            nbTourApparitionChoix+=1
        else:
            nbTourApparitionChoix = nbApparitionChoix
            
        lastIndex = 20
        k = lastIndex*nbTourApparitionChoix+1 
        newLastIndex = nbTourApparitionChoix*20 + lastIndex
        
        if nbTourApparitionChoix <= nbApparitionChoix:
            for lien in liens:
                if lien.index-1>=k and lien.index-1<=newLastIndex:
                    if lien.index-1 <= 97:
                        variable = lien.nom
                        print(str(lien.index-1)+" - " + variable)
                        k+=1
                    else:
                        variable = lien.nom
                        print(str(lien.index+1)+" - " + variable)
                        k+=1                        
                            
            if nbApparitionChoix != 1 and nbTourApparitionChoix == nbApparitionChoix:
                print("** Fin de la liste des liens **")
                print("\n98 - Voir les liens précédents")                
            else:
                print("\n98 - Voir les liens précédents")
                print("99 - Voir les liens suivants")
    
    elif choix == '98':
        if nbTourApparitionChoix == 0:
            print("Aucun lien précédent à afficher")
        else:        
            os.system("cls")
            
            print(titreJeuPlusTour + str(tour) + '\n')
            print("Départ : "+titreDepart)
            print("Cible : "+titreCible)
            if tour == 1:
                print("Actuellement : "+titreDepart+'\n')
            else:
                print("Actuellement : "+titreActuel)
                print("\n00 - Retour / "+titreDepart+'\n')
                        
            nbTourApparitionChoix-=1
            lastIndex = 20
            k = lastIndex*nbTourApparitionChoix+1
            newLastIndex = nbTourApparitionChoix*20 + lastIndex
            
            for lien in liens:
                if lien.index-1>=k and lien.index-1<=newLastIndex: 
                    if lien.index-1 <= 97:
                        variable = lien.nom
                        print(str(lien.index-1)+" - " + variable)
                        k+=1
                    else:
                        variable = lien.nom
                        print(str(lien.index+1)+" - " + variable)
                        k+=1
            if nbTourApparitionChoix == 0:
                print("\n99 - Voir les liens suivants")                
            else:
                print("\n98 - Voir les liens précédents")
                print("99 - Voir les liens suivants")
            
    elif choix == '00':
        if listeTitrePage[numeroLien] == titreDepart:
            print("Retour impossible")
        else:
            #url = listeURLPage[numeroLien-1]
            listeURLPage.pop() 
            listeTitrePage.pop()     
            liens = listeLiens[numeroLien-1]
            numeroLien -= 1              
            tour += 1
            listeLiens.pop()
            retour = True
            nbTourApparitionChoix = 0            
            extraireLiensWiki() 
    elif len(liens)<=97:
        for lien in liens:            
            if choix == str(lien.index-1):
                lienPage = lien.url
                tour += 1
                numeroLien += 1
                liens = []
                nbTourApparitionChoix = 0
                extraireLiensWiki()        
    elif len(liens)>=98:
        for lien in liens:
            if lien.index-1 <= 97:
                if choix == str(lien.index-1):
                    lienPage = lien.url
                    tour += 1
                    numeroLien += 1
                    liens = []
                    nbTourApparitionChoix = 0
                    extraireLiensWiki() 
            else:
                if choix == str(lien.index+1):
                    lienPage = lien.url
                    tour += 1
                    numeroLien += 1
                    liens = []
                    nbTourApparitionChoix = 0
                    extraireLiensWiki()                    
    if listeTitrePage[numeroLien] != titreCible:                
        ChoixNumero()    
    
def extraireLiensWiki():
    os.system("cls")

    global i 
    global nbApparitionChoix
    global liens
    global tour
    global lienPage
    global listeURLPage
    global retour
    global titreDepart
    global titreActuel
    global titreCible
    global listeTitrePage    
    i = 1  
    
    if retour == True:
        print(titreJeuPlusTour + str(tour)+'\n')        
        print("Départ : "+titreDepart)
        print("Cible : "+titreCible)
        if tour == 1:
            print("Actuellement : "+titreDepart+'\n')
        else:
            print("Actuellement : "+listeTitrePage[numeroLien]+'\n')  
            
        if listeTitrePage[numeroLien] != titreDepart:
            print("\n00 - Retour / "+listeTitrePage[numeroLien-1]+'\n')
        
        for lien in liens:
            if i <=20:
                print(str(liens[i-1].index-1) + " - " +liens[i-1].nom)
                i+=1
            else:
                i+=1
        nbApparitionChoix = int(len(liens)/20)
        
        print("\n99 - Voir la suite")
        
        ChoixNumero()        
    else:
        print(titreJeuPlusTour + str(tour) + '\n')
    
        if tour == 1:
            with urllib.request.urlopen('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard') as response:
                webpage = response.read()
                soup = BeautifulSoup(webpage, 'html.parser')
                listeURLPage.append('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
        else:            
            with urllib.request.urlopen('https://fr.wikipedia.org'+lienPage) as response:
                webpage = response.read()
                soup = BeautifulSoup(webpage, 'html.parser')
                listeURLPage.append('https://fr.wikipedia.org'+lienPage)
    
        if tour == 1:
            with urllib.request.urlopen('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard') as response:
                webpage2 = response.read()
                soup2 = BeautifulSoup(webpage2, 'html.parser') 
                titreCible = soup2.find('h1', {"id" : "firstHeading"}).getText()
        
        if tour == 1:            
            titreDepart = soup.find('h1', {"id" : "firstHeading"}).getText()
            listeTitrePage.append(titreDepart)
        else:
            titreActuel = soup.find('h1', {"id" : "firstHeading"}).getText()
            listeTitrePage.append(titreActuel)
        
        if listeTitrePage[numeroLien] == titreCible:
            os.system("cls")
            print(titreJeuPlusTour + str(tour) + '\n')
            print("GAGNE!!!")
            print("\nVous avez terminé le jeu en "+str(tour)+" tours")
            compteurHistorique = 0
            print("\nHistorique des pages parcourues :\n")
            for titrePage in listeTitrePage:
                compteurHistorique += 1
                print("  " + str(compteurHistorique) + " " + titrePage)    
        else:    
            for bandeau in soup.find_all('div', {"class" : "bandeau-article"}):
                bandeau.decompose()
    
            for indice in soup.find_all('sup', {"class" : "reference"}):
                indice.decompose()
        
            for table in soup.find_all('table', {"class" : "infobox"}):
                table.decompose()
        
            for table in soup.find_all('table', {"class" : "infobox_v2"}):
                table.decompose()        
        
            for table in soup.find_all('table', {"class" : "infobox_v3"}):
                table.decompose()
        
            for editSection in soup.find_all('span', {"class" : "mw-editsection"}):
                editSection.decompose()
        
            for sommaire in soup.find_all('div', {"id" : "toc"}):
                sommaire.decompose()
            
            for sommaire in soup.find_all('div', {"class" : "reference-cadre"}):
                sommaire.decompose()
          
            for sommaire in soup.find_all('div', {"class" : "bandeau-portail"}):
                sommaire.decompose()
            
            for sommaire in soup.find_all('div', {"class" : "navbox-container"}):
                sommaire.decompose()
    
            for image in soup.find_all('a', {"class" : "image"}):
                image.decompose()
        
            for indicateur_langue in soup.find_all('a', {"class" : "extiw"}):
                indicateur_langue.decompose()
        
            for internal in soup.find_all('a', {"class" : "internal"}):
                internal.decompose()
        
            for redirect in soup.find_all('a', {"class" : "mw-redirect"}):
                redirect.decompose()    

            for emptyText in soup.find_all('a'):
                if emptyText.getText() == '':
                    emptyText.decompose()  
            
            print("Départ : "+titreDepart)
            print("Cible : "+titreCible)
            if tour == 1:
                print("Actuellement : "+titreDepart+'\n')
            else:
                print("Actuellement : "+titreActuel)
            
            if listeTitrePage[numeroLien] != titreDepart:
                print("\n00 - Retour / "+listeTitrePage[numeroLien-1]+'\n')
    
            for anchor in soup.find('div', {"class" : "mw-parser-output"}).find_all(['a']): 
                if i <=20:
                    print(str(i) + " - " +anchor.getText())
                    i+=1
                else:
                    i+=1                
                liens.append(Lien(i, anchor.getText(), anchor.get('href')))                
            listeLiens.append(liens) 
            nbApparitionChoix = int(len(liens)/20)
            print("\n99 - Voir les liens suivants")              
            ChoixNumero() 

tour += 1
extraireLiensWiki()
