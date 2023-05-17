import os
import instagram
import github
import shutil

github.git_refresh()

try:
    instagram.download_instagram()
except:
    print("Limite de usos da api do instagram excedido.")

os.system("pkill firefox")

os.system("firefox --kiosk localhost:5000")
