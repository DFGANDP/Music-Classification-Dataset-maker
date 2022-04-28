import os

data_path = "data_gatunki/"

count = 0
for dir in os.listdir(data_path):
    for file in os.listdir(data_path+dir):
        count += 1
print(count) 
