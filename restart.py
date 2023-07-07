from datetime import date, datetime, time
import os

data = datetime.now()

if data.isoweekday() == 6:
    if data.hour < 12:
        os.system('cec-ctl --tv -d/dev/cec0 --to 0 --image-view-on && echo "$(date): TV LIGADA" >> /home/orangepi/noticiasifmt/updatelogs.txt')
elif data.isoweekday() != 7:
    os.system('cec-ctl --tv -d/dev/cec0 --to 0 --image-view-on && echo "$(date): TV LIGADA" >> /home/orangepi/noticiasifmt/updatelogs.txt')
