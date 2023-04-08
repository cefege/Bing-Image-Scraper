# We are importing our BingScrapper.py file
from BingScrapper import bingScrapper as bss
import os
import numpy as np
from urllib.parse import unquote
from pathlib import Path
import pandas as pd
import sys
file = sys.argv[1]
path_csv = Path(os.path.abspath(__file__).replace(
    f"{os.path.basename(__file__)}", '') + f"{file}")  # We are setting the path for our csv file
df = pd.read_csv(f"{path_csv}")  # We are reading our csv file dataframe
# we are changing the data type of our supporting columng in our dataframe to string
df = df.astype({"supporting_seed_keywords": str})
lista = []
for c, i in enumerate(df['query'].values):  # for every value in column query
    try:
        # here we can set Y = bss(i,download_images=number of images to be downloaded per query)
        # for example Y = bss(i,5) will download 5 images per every query
        # we are running our script and returning removed duplicates values as a list of strings
        Y = bss(i, 2)
        # make sure that html text is decoded (example %24, %27 ...)
        Y = [unquote(i) for i in Y]
        y1 = int(len(Y))  # storing length of Y before removing duplicates
        # list made for storing all supporting column values so far
        lista.clear()
        # for each value in supporting column
        for i in df.loc[df['project_name'] == df['project_name'].values[c], 'supporting_seed_keywords']:
            i = str(i)  # i will turn it to string
            i.lower()
            i = i.split(',')  # split the string with comma
            lista.extend(i)  # add values to the list
        # we are lowering all letters in our list
        lista = [ittem.lower() for ittem in lista]
        lista = list(set(lista))
        # we are lowering all letters in our results from bing scrapper
        Y = [item.lower() for item in Y]
        # if the value of our result Y list is not in the prior list i will keep it , else i won't
        Y = [item for item in Y if item not in lista]
        y2 = int(len(Y))  # storing length of Y after duplicates removal
        # we  are turning our result list to one string that is split by ,
        Y = ','.join(Y)
        #Y = Y.replace("%24","$").replace("%27","'")
        # print(Y)
        # we are locating our cell in supporting column
        is_it_empty = df.loc[c, 'supporting_seed_keywords']
        if is_it_empty == 'nan':  # if its nan value (empty)
            try:
                # we are appening our string into it
                df.at[c, 'supporting_seed_keywords'] = Y
                print(f'Row {c+2} [{df["query"].values[c]}]  --> done')
                print(f'Duplicate strings removed: {y1-y2}')
            except Exception as e:
                print(e)
                pass
        else:
            # else if it isnt empty we are skipping
            print(f'Row {c+2} [{df["query"].values[c]}] X skipped')
            pass
    except Exception as e:
        print('EXCEPTION!!! ', e)
# we are filling nan values with empty space in our resulting csv
df.fillna('', inplace=True)
df.to_csv(path_csv, index=False)  # we are saving our csv resulting file
#pause = input('')
