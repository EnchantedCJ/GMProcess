# -*- coding:utf-8 -*-
import os, shutil

dim = int(input('Please enter the number of directions (1/2): '))
ifScale = input('Please enter if scale or not (y/n): ')

if os.path.exists('./output'):
    shutil.rmtree('./output')

files = []
for root, dirs, filesWalk in os.walk('./'):
    for file in filesWalk:
        if file.split('.')[1] == 'py':
            continue
        if file.split('.')[1] == 'csv':
            continue
        if file.split('.')[-1] == 'DT2' or file.split('.')[-1] == 'VT2':
            continue
        if file.split('.')[-2][-3:] == '-UP' or file.split('.')[-2][-3:] == 'DWN':
            continue
        files.append(file)

if dim == 1:
    tempFiles = []
    for i in range(len(files)):
        if i % 2 == 1:
            continue
        tempFiles.append(files[i])
    files = tempFiles

print('files', len(files), files)

scales = {}
for file in files:
    scales[file] = 1

if ifScale == 'y':
    with open('./_SearchResults.csv', 'r', encoding='utf-8') as f:
        for i in range(34):
            f.readline()
        while True:
            line = f.readline()
            # print(line)
            if line == '\n':
                break
            temp = line.strip('\n').split(',')
            scaleFactor = float(temp[4])
            name1 = temp[19].strip()
            name2 = temp[20].strip()
            scales[name1] = scaleFactor
            scales[name2] = scaleFactor
print('scales', len(scales), scales)

GMs = []
NPTS = []
DT = []
for i in range(len(files)):
    with open(files[i], 'r', encoding='utf-8') as f:
        print(files[i])
        f.readline()
        f.readline()
        f.readline()
        paraLine = f.readline()
        temp = paraLine.strip('\n').split(', ')
        NPTS.append(int(temp[0].split('=')[1].strip()))
        DT.append(float(temp[1].split('=')[1].strip('SEC').strip()))
        print('NPTS = {p1}, DT = {p2}'.format(p1=NPTS[i], p2=DT[i]))

        GMs.append([])
        for line in f.readlines():
            for data in line.strip().split():
                GMs[i].append(float(data))
                # print(GMs[i])

os.mkdir('./output')

with open('./output/EQ_List.txt', 'w', encoding='utf-8') as f:
    for file in files:
        f.write(file)
        f.write('\n')

for i in range(len(files)):
    with open('./output/' + files[i] + '.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(NPTS[i]) + '\n')
        for step in range(len(GMs[i])):
            fout.write(
                '{time:.3f}\t{acc:.7E}\n'.format(time=step * DT[i],
                                                 acc=GMs[i][step] * 10 * scales[files[i]]))  # g -> m/s2
