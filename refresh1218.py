import instagram
import github
import shutil
import os
import noticias

noticias.scraping_noticias()

github.git_refresh()

try:
    instagram.download_instagram()
except:
    print("Limite de usos da api excedido")

os.system("xdotool windowactivate $(xdotool search --onlyvisible --class chromium|head -1)")
os.system("xdotool key CTRL+F5")
