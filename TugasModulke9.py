##Nomor 6
class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranPohon(akar, count=0):
    if akar is None:
        return count

    return ukuranPohon(akar.kiri, ukuranPohon(akar.kanan, count+1))

a = SimpulPohonBiner('Ambarawa')
b = SimpulPohonBiner('Bantul')
c = SimpulPohonBiner('Cimahi')
d = SimpulPohonBiner('Denpasar')
e = SimpulPohonBiner('Enrekang')
f = SimpulPohonBiner('Flores')
g = SimpulPohonBiner('Garut')
h = SimpulPohonBiner('Halmahera Timur')
i = SimpulPohonBiner('Indramayu')
j = SimpulPohonBiner('Jakarta')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h;
g.kanan = i

##Nomor 7
class SimpulPohonBiner():
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar):
    if akar is None:
        return 0
    else:
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan:
            return kiri+1
        else:
            return kanan+1

A = SimpulPohonBiner("Surakarta")
B = SimpulPohonBiner("Cimahi")
C = SimpulPohonBiner("Merauke")
D = SimpulPohonBiner("Salatiga")
E = SimpulPohonBiner("Magelang")
F = SimpulPohonBiner("Purworejo")
G = SimpulPohonBiner("Bogor")
H = SimpulPohonBiner("Klaten")
I = SimpulPohonBiner("Wonogiri")
J = SimpulPohonBiner("Halmahera")

##Nomor 8
def traverse(root):
    lvlist=[]
    current_level = [root]
    lv=0
    while current_level:
        #print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.kiri:
                next_level.append(n.kiri)
                level.append(lv+1)
            if n.kanan:
                next_level.append(n.kanan)
                level.append(lv+1)
            current_level = next_level
            
        lv+=1
        lvlist.append(lv)
    return lvlist
        
def cetakdatadanlevel(root):
    traverse(A)
    print(root.data, ', Level 0')
    for i in range(len(level)):
          print(datalist[i+1], ', Level', level[i])
        

print('Ukuran dari Binary Tree adalah', size(A))
print('')
print('Tinggi maksimal dari Binary Tree adalah', maxDepth(A))
print('')
cetakdatadanlevel(A)
