from random import choice

import sys

sys.stdout = open("sifreler.txt", "w")

karakterler = ["a","b","c","d","e","f","g","x","q","z",1,2,3,4,5,6,7,8,9,"!","A","B","C","D","Z"]

print("Üretilen Şifre:")

sifreuzunluk = int(input())

sifre = ""

for i in range(sifreuzunluk):

    sifre += str(choice(karakterler))

print(sifre)

sys.stdout.close()
