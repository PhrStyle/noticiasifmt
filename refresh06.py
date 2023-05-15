import os
import instagram
import github
import shutil

github.git_refresh()

#instagram.download_instagram()

os.system("pkill firefox")

os.system("firefox --kiosk localhost:5000")
