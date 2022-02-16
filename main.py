import os




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
            os.system("cmd /c mkdir %APPDATA%\gameinstall")
            os.system("cmd /c mkdir %APPDATA%\gameinstall\dependancy")
            os.system("cmd /c mkdir %APPDATA%\gameinstall\Games")
            os.system("cmd /c curl --url https://mega.nz/MEGAcmdSetup32.exe -O %APPDATA%\gameinstall\dependancy\MEGAcmdSetup32.exe")
            os.system("cmd /c move MEGAcmdSetup32.exe %APPDATA%\gameinstall\dependancy\ ")
            os.system("cmd /c start %APPDATA%\gameinstall\dependancy\MEGAcmdSetup32.exe /S  ")
            os.system("cmd /c del ")
            print('terminer!')
            menu()
              #  est la location de megacmd %USERPROFILE%\AppData\Local\MEGAcmd
        else:
            print('annulation')


    elif selection=='3' :
        print('UwU')

    elif selection=='2' :
        print('UwU')

    elif selection=='1' :
        print('kyah')

    else:
        print("une erreur c'est produite")
    return

menu()






