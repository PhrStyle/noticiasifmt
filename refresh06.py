import os
import instagram
import github
import shutil

dirgit = "/noticiasifmt/static/github"
for f in os.listdir(dirgit):
    os.remove(os.path.join(dirgit, f))
github.git_refresh()

dirinsta = "/noticiasifmt/static/ifmtcuiabaoficial"
for f in os.listdir(dirinsta):
    os.remove(os.path.join(dirinsta, f))
try:
    instagram.download_instagram()
except:
    print("Limite de usos da api do instagram excedido.")
os.system("xdotool windowactivate $(xdotool search --onlyvisible --class chromium|head -1)")
os.system("xdotool key ctrl+F5")
