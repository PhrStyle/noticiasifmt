import os
import instagram
import github
import shutil

github.git_refresh()

try:
    instagram.download_instagram()
except:
    print("Limite de usos da api do instagram excedido.")

os.system("pkill chromium")

os.system("chromium-browser --kiosk 127.0.0.1:5000")
