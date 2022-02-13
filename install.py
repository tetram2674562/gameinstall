import os



print ("Quel logiciel voulez-vous installez?")
print ("1) Terraria")
install = (input("Veuillez écrire le chiffre du logiciel choisi"))
if install== 1 :
    os.system(cmd /c '%USERPROFILE%\AppData\Local\MEGAcmd\MEGAclient.exe --get  ')