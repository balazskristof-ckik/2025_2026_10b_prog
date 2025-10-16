import random


# lebegőpontos - float tört
a = 1.25
b = float(input("Adjon meg egy tizedes törtet: "))

print(b*4)


c = random.randint(100,900)/100
print (c)

#Szövegketezelés
szoveg = input("adjon meg egy szöveget: ")
print(szoveg)
print("Szöveg hossza: ",len(szoveg))
print("első karakter", szoveg[0])
# szöveg karakterekből épül fel
# szöveg = karakter lánc
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)


a = chr(random.randint(97,122))
b = chr(random.randint(97,122))
c = chr(random.randint(97,122))
print(a,b,c)























