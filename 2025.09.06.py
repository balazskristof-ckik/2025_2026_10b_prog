#kérjen be egy egész számot és döntse el, hogy páros vagy páratlen?

szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")

#kérjen be a felhasználótól egy számot és mondja meg hogy 10-zel osztható -e? Ha nem osztható 10-zel írja ki az utolsó számjegyét!
#pl. be: 10 ki: tízzel osztható
#pl. be: 12 ki tízzel nem osztható, utolsó számjegy 2


if (szam % 10 == 0):
    print("osztható")
else:
    print("nem osztható")
    print("az utolsó számjegy: " + str(szam % 10))

    # Kérjen be egy másik számot és írassa ki a két sám reciprokának összegét !

szam2 = int(input("Adjon meg egy másik számot: "))

if(szam != 0):
   if(szam2 != 0):
    rec = 1/szam
    rec2 = 1/szam2
    print(rec+rec2)
   else:
      print("a második számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")    

# Adja meg a két szám összegének gyökét

if(szam != 0):
    if(szam2 != 0):
     gyoka = math.sqrt
     gyoka2 = math.sqrt2
     print(gyoka+gyoka2)
    else:
      print("a második számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")
