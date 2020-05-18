##--------------------Latihan 10.1--------------------##

#Menjumlahkan bilangan 1 sampai n

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

#Mengukur kinerja, dengan n = 10000

import time

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

for i in range(5):              #Mengulangi 5 kali
    awal = time.time()          #menandai awal kerja
    h = jumlahkan_cara_1(10000) #menjumlahkan 1 sampai s10000
    akhir = time.time()         #menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))

#menaikan n menjadi satu juta

import time

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

for i in range(5):                  #Mengulangi 5 kali
    awal = time.time()              #menandai awal kerja
    h = jumlahkan_cara_1(1000000)   #menjumlahkan 1 sampai s1000000
    akhir = time.time()             #menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))

#mennggunakan algoritma yang lebih baik

import time

def jumlahkan_cara_2(n):
    return (n*(n+1))//2

for i in range(5):              #mwngulangi 5 kali
    awal = time.time()          #menandai awal kerja
    h = jumlahkan_cara_2(10000) #menjumlahkan 1 sampai sepuluh ribu
    akhir = time.time()         #menandai akhir kerja, lalu mencetakn
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))


##--------------------Latihan 10.3--------------------##

#Average Case scenario

import random
import time

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos-1]
            pos = pos -1
        A[pos] = nilai

for i in range(5):
    L = list(range(3000))
    random.shuffle(L)
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Jumlah %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))

#Worst case Scenario

import time

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos-1]
            pos = pos -1
        A[pos] = nilai

for i in range(5):
    L = list(range(3000))
    L = L[::-1]
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Jumlah %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))    


#Best case scenario

import time

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos-1]
            pos = pos -1
        A[pos] = nilai

for i in range(5):
    L = list(range(3000))

    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Jumlah %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))


##--------------------Latihan 10.4--------------------##

#0(log n)

count = 0
i = 32
while i >=1:
    count = count + 1
    i = i//2
print(count)


##--------------------Latihan 10.5.1--------------------##

import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        for j in range (n):
            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        ##print('i = ',i)
        t=timeit.timeit("kalangBersusuh(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

n=1000
LS=ujiKalangBersusuh(n)

plt.plot(LS)
skala=7700000
plt.plot([x*x/skala for x in range (1,n+1)])
plt.show()


























