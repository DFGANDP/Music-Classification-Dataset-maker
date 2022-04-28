import os, glob
import unidecode
import argparse

'''
File for removing special chars from filenames
It is needed because zip dont work well with them
'''



DIRPATH = ""

def removeAccents(input_text):
    '''
    Deletes accents from filenames
    '''

    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'


    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'

    print(len(strange))
    print(len(ascii_replacements))
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)


def find_files(dirpath, subdirs=False):
    '''
    subdirs == True - iterates over genres dirs
    '''
    if subdirs==True:
        targetPattern = "{}\**\*.mp3".format(dirpath)
        pliki = glob.glob(targetPattern)
        #print(pliki[4])
    elif subdirs==False:
        targetPattern = "{}\*.mp3".format(dirpath)
        pliki = glob.glob(targetPattern)
        print(pliki[2])
    return pliki

def remove_underline(filename):
    '''
    Explained
    https://flexiple.com/python-string-contains/
    Removes special chars e.g. star from filenames
    '''
    underlines = []
    for i in range(303,335):
        string = '\\u0{}'.format(i)
        string = string[0:6]
        underlines.append(string)

    # CZARNA GWIAZDA DODAJE RECZNIE
    string = '\\u2605'
    string = string[0:6]
    underlines.append(string)

    new_filename = []
    for i in filename:
        for underline in underlines:
            underline = underline.encode('ASCII').decode('unicode-escape')
            if underline in filename:
                print("TU {}".format(underline))
                #print("jeeest")
                #print(i+"\u0332")
                i = i.replace(underline, "")
                #print(i)
        new_filename.append(i)
    s = ''.join(new_filename)
    #s = unidecode.unidecode(s) # DO USUNIECIA KONCOWEGO NP POGRUBIONYCH LITER POJEBANYCH ITD
    s = s.encode('ascii', 'ignore').decode('ascii')
    return s

def rename_file(filepath_array):
    for filepath in filepath_array:
        filename = os.path.basename(filepath)
        new_filepath = removeAccents(filepath)
        # WYJEBAC UNDERLINE
        new_filepath = remove_underline(new_filepath)
        os.rename(filepath, new_filepath)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath', type=str, default="data_gatunki", help='Directory where you have all files')
    #parser.add_argument('--subdirs', type=bool, default=True, help='If there are subdirs == True')
    args = parser.parse_args()
    return args

def main():
    args = parse_opt()
    pliki = find_files(args.dirpath, subdirs=True)
    rename_file(pliki)

if __name__ == '__main__':
    main()
