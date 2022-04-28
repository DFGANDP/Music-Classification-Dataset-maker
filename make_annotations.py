'''

labele z gtzan
pamietac zeby usunac 544.wav (jazz chyba)

LABELS:
0 : blues
1 : classic
2 : electronic
3 : electronic(vibe)
4 : hip hop
5 : jazz
6 : metal
7 : pop
8 : reggae
9 : rock


OUTPUT:
- filename | label

wziac nazwy z dane_gatunki i przypisac im labele
jesli nazwa pliku jest subsetem string z dataset_filepath przypisac mu wartosc ta wlasnie

Process:
1 struktura danych

'''

import os
import pandas as pd

DIRPATH = "data_gatunki/"

# !! CHANGE TO YOUR LABELS
label_dict = {
    "blues" : 0,
    "classical" : 1,
    "electronic" : 2,
    "electronic(vibe)" : 3,
    "hiphop" : 4,
    "jazz" : 5,
    "metal" : 6,
    "pop" : 7,
    "reggae" : 8,
    "rock" : 9
}



def data_gatunki_to_labels(dirpath):
    full_file_paths = {}
    for genre in os.listdir(dirpath):
        if genre in label_dict.keys():
            # genre idzie do labelu
            label = label_dict[genre]
            for file in os.listdir(dirpath+genre):
                file = file[:-4]
                full_file_paths[file] = label
        else:
            print("{} nie ma w label_dict".format(genre)) # KURWA ZAPOMNIALEM ZAMKNAC NAWIASU I 5 MIN SZUKANIA BLEDU
    return full_file_paths


def przypisz_label_do_pliku(dirpath, full_filenames_dict):
    '''

    '''
    tab_filename = []
    tab_label = []
    for filename in os.listdir(dirpath):
        #iteruj przez klucze slownika
        for k, v in full_filenames_dict.items():
            if k in filename:
                label = v
                tab_filename.append(filename)
                tab_label.append(label)
                #DODAJ DO PANDAS PLIK Z LABELEM
    d = zip(tab_filename, tab_label)
    df = pd.DataFrame(data=d, columns=['filename', 'label'])
    return df

def testuj_substring():
    '''
    Fajnie wytlumaczone
    https://flexiple.com/python-string-contains/
    '''
    subname = "hardbass adidias"
    filename = "hardbass adidias sec_10.0_30.0_.mp3"
    if subname in filename:
        print("jeeest")

def merge_with_gtzan(df):
    '''
    TODO
    *USUNAC Z GTZAN DISCO ORAZ COUNTRY
    *ZAPISAC LABELE JAKO ALBO LICZBY ALBO NAZWY
    '''
    df_gtzan = pd.read_csv("features_30_sec.csv") # GTZAN annotations
    df_gtzan = df_gtzan.drop(554, axis=0, inplace=False)
    # WYBIERZ FILENAME ORAZ LABEL
    dfnew = df_gtzan.filename.to_frame()
    label = df_gtzan.label.to_frame()
    dfnew["label"] = label

    dfnew.columns=['filename','label']

    # USUN DISCO ORAZ COUNTRY
    dfnew = dfnew[dfnew.label != "disco"]
    dfnew = dfnew[dfnew.label != "country"]

    # ZMIEN LABEL NA LICZBY
    dfnew["label"].replace(label_dict, inplace=True) # TU NIE DIZALA

    #print(dfnew)
    #print(dfnew)
    frames = [df, dfnew]
    result = pd.concat(frames)
    # POLACZ JE ZE SOBA JAKO KOLUMNY A POTEM Z df
    return result

def main():
    full_file_paths_dict = data_gatunki_to_labels(DIRPATH)
    df = przypisz_label_do_pliku("dataset", full_file_paths_dict)
    result = merge_with_gtzan(df)
    result.to_csv('CNN_CLASIFIER_annotations.csv', index=False)

main()
