class MhsTIF(object):
    def __init__(self,nama,umur,tinggal,us):
        self.nama = nama
        self.umur = umur
        self.tinggal = tinggal
        self.us = us

c0 = MhsTIF('Andhika', 14, 'Solo', 35000)
c1 = MhsTIF('Hafidh', 34, 'Salatiga', 30000)
c2 = MhsTIF('Putra', 22, 'Surakarta', 13000)
c3 = MhsTIF('Hesti', 19, 'Solo', 14000)
c4 = MhsTIF('Retno', 44, 'Boyolali', 15000)
c5 = MhsTIF('Sari', 23, 'Boyolali', 16000)
c6 = MhsTIF('Kesya', 13, 'Klaten', 37000)
c7 = MhsTIF('Diwa', 15, 'Wonogiri', 18000)
c8 = MhsTIF('Ariela', 8, 'Karanganyar', 29000)
c9 = MhsTIF('inez', 4, 'Surakart', 20000)
c10 = MhsTIF('Johan', 27, 'Purwodadi', 21000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

##Nomer1##
def cari(a):
    x =[]
    for i in range(len(Daftar)):
        if a == Daftar[i].tinggal:
            x.append(i)
    print(x)
#---------------------------------------------------------------------#
##Nomer2##
def uskecil():
    a = Daftar[0].us
    for i in range(len(Daftar)):
        if a> Daftar[i].us:
            a = Daftar[i].us
            
    return a
#---------------------------------------------------------------------#
##Nomer3##
def usterkecil():
    a = Daftar[0].us
    x  =[]
    for i in range(len(Daftar)):
        if a> Daftar[i].us:
            a = Daftar[i].us
    for i in range(len(Daftar)):
        if Daftar[i].us == a:
            x.append(Daftar[i].nama)
    return x
#---------------------------------------------------------------------#
##Nomer4##
def uskurang25k():
    x =[]
    for i in range(len(Daftar)):

        if Daftar[i].us < 250000:
            x.append(Daftar[i].nama)
    return x
def uslebih25k():
    x =[]
    for i in range(len(Daftar)):
        if Daftar[i].us >250000:
            x.append(Daftar[i].nama)
    return x
#---------------------------------------------------------------------#
##Nomer5##
class node(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def cari(self, dicari):
        cur = self
        while cur is not None:
            if cur.next != None:
                if cur.data != dicari:
                    cur = cur.next
                else:
                    print ("Data", dicari, "ada dalam Linked List")
                    break
            elif cur.next == None:
                print ("Data", dicari, "tidak ada dalam Linked List")
                break
##a = node(17)
##menu = a
##a.next = node (19)
##a = a.next
##a.next = node (45)
##a = a.next
##a.next = node (24)
##a = a.next
##menu.cari(17)
##menu.cari(22)
#---------------------------------------------------------------------#
##Nomer6##
z = [6,5,4,9,8,3,2,1,44,12,15]
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    
    x=[]
    while low <=high:
        mid =(high + low)//2
        if kumpulan[mid]==target: 
            return 'target pada indexs ke-'+str(mid)
                    
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid+1
    return False
#---------------------------------------------------------------------#
##Nomer7##
b = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
def binse(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    a = []
    while low <= high:
        if kumpulan [low] == target:
            a.append(low)
            low += 1
        else:
            low += 1
    return a
#---------------------------------------------------------------------#
##Nomer8
##print(
##"""Nomer 8\nada dua pola
##pertama menggunakan konsep Big-O. Dimana yang dipakai
##adalah rumus O(log n) dengan rincian 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
##Di mana log berasal dari pangkat log berbasis 2. Dengan begitu dapat mengetahui jumlah
##maksimal tebakan.
##Untuk pola sendiri:
##        apabila ingin menebak angka 70
##        
##        a = nilai tebakan pertama // 2
##        tebakan selanjutnya = nilai tebakan "lebih dari" + a
##        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
##        tetap nilai lebih dari sebelumnya*
##        a = a // 2
##    Simulasi
##        tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "lebih dari itu"
##        tebakan ke 2: 75 (dari 50 + 25) jawaban = "kurang dari itu"
##        tebakan ke 3: 62 (dari 50 + 12) jawaban = "lebih dari itu"
##        tebakan ke 4: 68 (dari 62 + 6) jawaban = "lebih dari itu"
##        tebakan ke 5: 71 (dari 68 + 3) jawaban = "kurang dari itu"
##        tebakan ke 6: 69 (dari 68 + 1) jawaban = "lebih dari itu"
##        tebakan ke 7: antara 71 dan 69 hanya ada 1 angka = 70!!!
##        
##kedua menggunakan barisan geometri Sn = 2^n
##        barisan yang terjadi adalah : 2, 4, 8, 16, 32, 64
##        Misal angka yang akan diebak adalah 68
##        Tebakan ke-1 : 64 dijawab lebih dari itu
##        Tebakan ke-2 : 96(dari 64 + 32) dijawab "Kurang dari itu"
##        Tebakan ke-3 : 80(dari 64 + 16) dijawab "Kurang dari itu"
##        Tebakan ke-4 : 72(dari 64 + 8) dijawab "Kurang dari itu"
##        Tebakan ke-5 : 68(dari 64 + 4) dijawab "Lebih dari itu"
##        Tebakan ke-6 : 70(dari 68 + 2) dijawab "TEPAT"
##        """)
