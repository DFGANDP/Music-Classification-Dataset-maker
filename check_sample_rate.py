'''

!!!!!!!!!!!!!!!
PRZED UZYCIEM UMIESCIC W DATASET


'''
import os
import wave
import matplotlib.pyplot as plt
from pydub.utils import mediainfo
from pydub import AudioSegment

file_path_1 = "dataset\Russian hardbass mix 4h_sec_6600.0_6900.0.mp3" # 44100
file_path_2 = "1 HOUR  BADASS Music Mix 2021ROCK MIX_sec_1200.0_1500.0.mp3"

def model_1():
    sample_rate_tab = []
    for file_name in os.listdir("dataset/"):
        filepath = "dataset/"+file_name
        with wave.open(filepath, "rb") as wave_file:
            frame_rate = wave_file.getframerate()
        sample_rate_tab.append(frame_rate)

    plt.hist(sample_rate_tab, bins=10, edgecolor='black', log=False)

    plt.xlabel('SAMPLE RATES')
    plt.ylabel('frequency')

    plt.show()


def model_2():
    info=mediainfo(file_path_1)
    for k, v in info.items():
        print(k, v)

def model_3():
    song = AudioSegment.from_mp3(file_path_2)
    print(song.frame_rate)

def model_4():# WYJKONUJE SIE W CHUJ DLUGO
    SR_TAB = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(dir_path):
        print(file[-4:])
        if file[-4:] == ".mp3":
            print("jest")
            song = AudioSegment.from_mp3(file)
            sr = song.frame_rate
            SR_TAB.append(sr)
    plt.hist(SR_TAB, bins=10, edgecolor='black', log=False)
    plt.xlabel('SAMPLE RATES')
    plt.ylabel('frequency')

    plt.show()



if __name__ == '__main__':
    model_2()
