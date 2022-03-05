import os

git=(input("Avez-vous déjà lancéce logiciel une fois sur cet ordinateur? [O/N]"))
if git=='O' : 
    
    os.system("cmd /c winget install --id Git.Git -e -source winget")
    os.system("cmd /c %USERPROFILE%\AppData\Local\Program\Git\bin\git.exe clone ")
else :
    os.system("cmd /c %USERPROFILE%\AppData\Local\Program\Git\bin\git.exe clone --git-dir=%APPDATA% https://github.com/tetram2674562/gameinstall.git")
