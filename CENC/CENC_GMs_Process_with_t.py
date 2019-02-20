# -*-coding:utf-8-*-
import os


class GM(object):
    t = []
    ew = []
    ns = []
    ud = []

    def __init__(self):
        pass

    def ew_max(self):
        return max(max(self.ew), abs(min(self.ew)))

    def ns_max(self):
        return max(max(self.ns), abs(min(self.ns)))

    def ud_max(self):
        return max(max(self.ud), abs(min(self.ud)))


gms = []

root = './'
newfilenames = []
for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename[-3:] == 'txt':
            newfilenames.append(filename)
            print(filename)

for i in range(len(newfilenames)):
    gm = GM()
    with open(newfilenames[i], 'r', encoding='utf-8') as f:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()

        t=[]
        ud=[]
        ew=[]
        ns=[]
        temp1=f.readline().strip('\n').split(',')
        baseud=temp1[1]
        baseew=temp1[2]
        basens=temp1[3]
        t.append(float(temp1[0]))
        ud.append(0)
        ew.append(0)
        ns.append(0)

        for line in f.readlines():
            # print(temp)
            temp = line.strip('\n').split(',')
            # print(temp)
            t.append(float(temp[0]))
            ud.append(float(temp[1])-float(baseud))
            ew.append(float(temp[2])-float(baseew))
            ns.append(float(temp[3])-float(basens))
            # gm.ud.append(float(temp[1]))
            # gm.ew.append(float(temp[2]))
            # gm.ns.append(float(temp[3]))
        # print(gm.t)
        gm.t=t
        gm.ud=ud
        gm.ew=ew
        gm.ns=ns
    gms.append(gm)
    del gm
    # print(gms[0].t)
    # print(gms[0].ew)

ewmaxlist = []
nsmaxlist = []
udmaxlist = []
for i in range(len(newfilenames)):
    print(max(gms[i].ew),min(gms[i].ew))
    ewmaxlist.append(max(max(gms[i].ew),abs(min(gms[i].ew))))
    nsmaxlist.append(max(max(gms[i].ns),abs(min(gms[i].ns))))
    udmaxlist.append(max(max(gms[i].ud),abs(min(gms[i].ud))))

# print(ewmaxlist)
ewmax = max(ewmaxlist)
ewmaxindex = ewmaxlist.index(ewmax)
# print(ewmaxindex)
nsmax = max(nsmaxlist)
nsmaxindex = nsmaxlist.index(nsmax)
udmax = max(udmaxlist)
udmaxindex = udmaxlist.index(udmax)

print('ewmax ', ewmax, newfilenames[ewmaxindex])
print('nsmax ', nsmax, newfilenames[nsmaxindex])
print('udmax ', udmax, newfilenames[udmaxindex])


# print(gms[0].t)
for i in range(len(newfilenames)):
    # print(i)
    os.mkdir('./'+newfilenames[i].strip('.txt'))
    with open('./'+newfilenames[i].strip('.txt')+'/EW.txt','w',encoding='utf-8') as few:
        few.write(str(len(gms[i].ew))+'\n')
        for j in range(len(gms[i].ew)):
            # print(j)
            few.write(str(gms[i].t[j]))
            few.write('\t')
            few.write(str(gms[i].ew[j]/100))
            few.write('\n')
    with open('./'+newfilenames[i].strip('.txt')+'/NS.txt','w',encoding='utf-8') as fns:
        fns.write(str(len(gms[i].ns))+'\n')
        for j in range(len(gms[i].ns)):
            fns.write(str(gms[i].t[j]))
            fns.write('\t')
            fns.write(str(gms[i].ns[j]/100))
            fns.write('\n')
    with open('./'+newfilenames[i].strip('.txt')+'/UD.txt','w',encoding='utf-8') as fud:
        fud.write(str(len(gms[i].ud))+'\n')
        for j in range(len(gms[i].ud)):
            fud.write(str(gms[i].t[j]))
            fud.write('\t')
            fud.write(str(gms[i].ud[j]/100))
            fud.write('\n')