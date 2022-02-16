import os



print ("Quel logiciel voulez-vous installez?")
print ("1) Terraria")
install = (input("Veuillez écrire le chiffre du logiciel choisi"))
if install== 1 :
        url = 'https://mega.nz/file/pSxG1QzC#CdIFLo3IkQRa1WNtt29wXzEMGq48eZglEsNdbAGHYi0'
        exec = 'Terraria.exe'
        dir = '\Terraria'
os.system("cmd /c %USERPROFILE%\AppData\Local\MEGAcmd\MEGAclient.exe get ",url)
os.system("cmd /c mkdir",dir)
os.system("start ",exec," /D=%APPDATA%\gameinstall\Games",dir)


# à faire bah mon gars faut que tu crées une nouvelle branche github et que tu ajoutes unscript qui télécharge et install automatiquement git en protable edition bah voilà mec jpeux plus r pour toi et ajoute ce script sur le github... :)