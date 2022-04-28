import librosa
import os
import numpy as np
import matplotlib.pyplot as plt

DIRPATH = "data_gatunki/"

class DatasetEDA():
    '''
    Finds time of each label you have
    '''
    def __init__(self, dirpath):
        self.dirpath = dirpath
        self.dict = {}

    def find_genre_time(self):
        for dir in os.listdir(self.dirpath):
            time_all = 0
            for file in os.listdir(self.dirpath+dir):
                filetime = self.find_file_time(self.dirpath+dir+"/"+file)
                time_all += filetime
            genre = dir
            self.dict[genre] = time_all

    def plot_bars(self):
        plt.bar(range(len(self.dict)), list(self.dict.values()), align='center')
        plt.xticks(range(len(self.dict)), list(self.dict.keys()))
        plt.show()

    def find_file_time(self,filepath):
        filetime = librosa.get_duration(filename=filepath)
        return filetime
        pass

if __name__ == '__main__':
    data = DatasetEDA(DIRPATH)
    data.find_genre_time()
    data.plot_bars()
