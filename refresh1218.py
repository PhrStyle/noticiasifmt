import instagram
import github
import shutil
import os

github.git_refresh()

#try:
#    instagram.download_instagram()
#except:
#    print("Limite de usos da api do instagram excedido.")

instagram.download_instagram()

os.system("xdotool windowactivate $(xdotool search --onlyvisible --class chromium|head -1)")
os.system("xdotool key ctrl+F5")
