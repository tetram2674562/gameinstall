import os
import platform

def installdependancy():
    install = open("install.dat", "r")
    if install==0 :
        os.system(("cmd /c 'mkdir 7zip'"))
        os.system("cmd.exe /c 'curl https://www.7-zip.org/a/7z2107-x64.exe' ")
        os.system("cmd /c 'start 7z2107-x64.exe /D=.\7zip\'")
    


    else:
        menu()
    
    
    return



def menu():
    print ('\x1b[6;31;40m' + ' Bienvenue! ' + '\x1b[0m')
    print ('choisissez une option :')
    print ('1)  installer/mettre à jour un logiciel')
    print ('2)  désinstaller un logiciel')
    print ("3)  à propos de l'auteur")
    print ('4)  installer les dépendances')
    selection=(input(' '))
    if selection=='4' :

        dependency=(input("Pour valider l'installation des dépendances [O/N]"))
        if dependency=='O' :
            print('installation')
            installdependancy()
        
        else:
            print('annulation')


    elif selection=='3' :
        print('uwa')

    elif selection=='2' :
        print('uwo')

    elif selection=='1' :
        print('kyah')

    else:
        print("une erreur c'est produite")
    return

menu()





