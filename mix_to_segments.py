'''
0. adnotacje wymyslic
1. wez nute wczytaj
2. 2 min przerwy
3. 1 min nuty
4. 2 fragmenty po 30 sek
5. zapisz fragmenty jako mp3 (nazwa pliku stara i przedzialy sekundowe dodane do nazwy.mp3)
5. petla punkt 2 --> 4 az do konca
6. jesli nie wychodzi 30 sek na koncu to pomin

'''

import os
from pydub import AudioSegment
import time

data_dir = "data_gatunki/"
out_dir = "dataset/"

# pydub does things in milliseconds


def find_file(data_dir):
    '''
    Iterates over music genres (dirs)
    '''
    for directory in os.listdir(data_dir):
        for file in os.listdir(data_dir+directory):
            #print(data_dir+directory+"/"+file)
            filepath = data_dir+directory+"/"+file
            cut_final(filepath)

def cut_final(filepath):
    '''
    between segments 10 sec of delay
    cut 30 sec segment
    10 sec of delay -> 30 sec of music (save to file) - > 10 sec of delay -> 30 sec of music (save to file) -> n times
    '''
    # Opening file and extracting segment
    song = AudioSegment.from_mp3(filepath)
    slices = song[::30000] # To jest generator a nie lista

    filename = os.path.basename(filepath)
    print(filename)
    slices = list(slices)


    slices = slices[:-1] # cut last beacuse is not 30 sec

    count = 0
    for index, slice in enumerate(slices):
        if len(slice) != 30000:
            pass
        else:
            count += 1
            # print(len(slice))
            if count < 5:
                pass
            elif count > 4 and count < 7:
                if (index) == len(slices):
                    break
                else:
                    if count == 5:
                        start_point = (index)*30000
                        end_point = (index+1)*30000
                        extract = song[start_point:end_point]
                        extract.export(out_dir+filename[:-4]+'_sec_{}_{}.mp3'.format(start_point/100, end_point/100), format="mp3")
                    if count == 6:
                        start_point = (index)*30000+10000
                        end_point = (index+1)*30000+10000
                        extract = song[start_point:end_point]
                        extract.export(out_dir+filename[:-4]+'_sec_{}_{}.mp3'.format(start_point/100, end_point/100), format="mp3")
                        count = 0


if __name__=="__main__":
    start = time.time()
    find_file(data_dir)
    #cut_final(filename)
    end = time.time()
    print("IT TOOK: ")
    print(end - start)


# ffmpeg -i somefile.mp3 -f segment -segment_time 3 -c copy out%03d.mp3
