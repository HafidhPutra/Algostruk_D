##No 1
class MhsTIF(object):
    def __init__(self,nama,nim,kota,uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTIF('Andhika', 85, 'Solo', 35000)
c1 = MhsTIF('Hafidh', 91, 'Salatiga', 30000)
c2 = MhsTIF('Putra', 100, 'Surakarta', 13000)
c3 = MhsTIF('Hesti', 119, 'Solo', 14000)
c4 = MhsTIF('Retno', 74, 'Boyolali', 15000)
c5 = MhsTIF('Sari', 23, 'Boyolali', 16000)
c6 = MhsTIF('Kesya', 113, 'Klaten', 37000)
c7 = MhsTIF('Diwa', 95, 'Wonogiri', 18000)
c8 = MhsTIF('Ariela', 88, 'Karanganyar', 29000)
c9 = MhsTIF('inez', 114, 'Surakart', 20000)
c10 = MhsTIF('Johan', 27, 'Purwodadi', 21000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def temp(a,b,c):
    tmp=a[b]
    a[b]=a[c]
    a[c]=tmp
    
def urutNim(a):
    n = len(a)
    for x in range(n-1):
        for y in range(n-x-1):
            if a[y].nim > a[y+1].nim:
                temp(a,y,y+1)

def cekNim(Daftar):
    for i in Daftar:
        print(i.nama,i.nim,i.kotaTinggal)


##No 2
a = [3, 7, 35, 20, 47, 88, 106, 92, 120, 11]
b = [13, 5, 19, 17, 2, 8, 45, 18, 29, 63, 25, 40]

def Array_1(a,b):
    c = a + b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos >0 and nilai<c[pos - 1]:
            c[pos]= c[pos-1]
            pos -= 1
        c[pos] = nilai
    print(c)

def Array_2(a,b):
    ad0 = len(a)
    ad1 = len(b)
    x= 0
    y=0
    c = []
    while x < ad0 and y < ad1:
        if a[x]<b[y]:
            c.append(a[x])
            x += 1
        else:
            c.append(b[y])
            y += 1
    while x<ad0:
        c.append(a[x])
        x += 1
    while y<ad1:
        c.append(b[y])
        y += 1
    return c

##No 3
def temp(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                temp(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(A, i, n)
        if indexKecil != i:
            temp(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

p = detak();bubbleSort(u_bub);t=detak();print("Bubble    : %g detik"%(t-p));
p = detak();selectionSort(u_sel);t=detak();print("Selection : %g detik"%(t-p));
p = detak();insertionSort(u_ins);t=detak();print("Insertion : %g detik"%(t-p));
