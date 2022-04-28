![GitHub last commit](https://img.shields.io/github/last-commit/DFGANDP/Music-Classification-Dataset-maker)  ![GitHub](https://img.shields.io/github/license/DFGANDP/Music-Classification-Dataset-maker)

![Banner](./Banner.png)

# Description
Tool which helps to make a Dataset from your data!

## Requirements

```bash
1. numpy
2. pandas
3. librosa
4. pydub
5. matplotlib
6. unidecode
```

## PIPELINE

```bash
1. Download albums or long music files from internet
2. Create genres dirs like in data_genres and out files in them
3. Remove special characters
4. Divide albums into 30sec segments
5. Make annotations file
6. Pack all to zip
```


## USAGE

```bash
remove_special_chars.py --> Script to remove special characters
mix_to_segments.py --> Cuts albums into 30sec .mp3 files
make_annotations.py --> Makes annotations
EDA.py --> Shows how balanced is your dataset
check_sample_rate.py --> checks sr
```
