import csv
import os
import shutil
from urllib import urlretrieve

DST_PATH = 'E:/ESC-10-masterTheOriginalRepoOGG/ESC-10-NewRepo'
CSV_FILE_NAME  = "esc50.csv"


IS_DATASET_LOCAL = False # False to download the files from the repo directly

if IS_DATASET_LOCAL == False:
    # to get the files directly from the repo uncomment the below line
    SRC_PATH = 'https://raw.githubusercontent.com/karoldvl/ESC-50/master/audio/'
else:
    # if the files are locally stored on your system
    SRC_PATH = 'E:/ESC-50-master/ESC-50/master/audio'



foldername_map = {
'dog' : '001 - Dog bark',
'rain' : '002 - Rain',
'sea_waves' : '003 - Sea waves',
'crying_baby' : '004 - Baby cry',
'clock_tick' : '005 - Clock tick',
'sneezing' : '006 - Person sneeze',
'helicopter' : '007 - Helicopter',
'chainsaw' : '008 - Chainsaw',
'rooster' : '009 - Rooster',
'crackling_fire' : '010 - Fire crackling'}


counter = 0
with open(CSV_FILE_NAME, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    headers = next(csv_reader)
    for row in csv_reader:
        if row[4] == 'True':
            store_path = os.path.join(DST_PATH, foldername_map[row[3]])
            if not os.path.exists(store_path):
                os.makedirs(store_path)

            dst = os.path.join(store_path, row[0])
            src = os.path.join(SRC_PATH, row[0])

            if IS_DATASET_LOCAL == False:
                urlretrieve(SRC_PATH + row[0], dst)
            else:
                shutil.copy2(os.path.join(SRC_PATH, row[0]), dst)

            counter += 1
            print ', '.join(row)

print counter
