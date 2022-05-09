# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:42:41 2022

@author: Wojtek



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


"""

import pandas as pd
import matplotlib.pyplot as plt

genre_dict ={
0 : 'blues',
1 : 'classic',
2 : 'electronic',
3 : 'electronic(vibe)',
4 : 'hiphop',
5 : 'jazz',
6 : 'metal',
7 : 'pop',
8 : 'reggae',
9 : 'rock'
    }

def plot_proportions(df_path):
    '''
    Pokazuje ile sampli z kazdego gatunku znajduje sie w bazie danych
    '''
    df = pd.read_csv(df_path)
    dups_labels = df.pivot_table(columns=['label'], aggfunc='size')
    values = (dups_labels.tolist())
    names = list(genre_dict.values())

    plt.bar(names, values, color ='maroon',
        width = 0.4)
    plt.xlabel("GATUNKI")
    plt.ylabel("ILE PLPIKOW")
    plt.title("JAK ZBALANSOWANA JEST BAZA DANCYH")
    plt.show()
plot_proportions("annotations_example/CNN_CLASIFIER_annotations_withgtzan_v2.csv")

