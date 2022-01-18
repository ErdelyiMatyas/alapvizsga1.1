'''
Nagyobb szám.
A program kérjen be két számot a felhasználótól, majd írja ki, hogy melyik a nagyobb! 
Vagy irja ki ha egyenlő
--------------
Adj meg egy számot! 1
Adj meg egy másik számot! 17
A nagyobb érték 17
--------------
Adj meg egy számot! 28
Adj meg egy másik számot! -2
A nagyobb érték: 28
---------------
Adj meg egy számot! 999
Adj meg egy másik számot! 999
A két szám egyenlő
------------------
'''


szam1 = int(input("Kérek egy szamot!:"))
szam2 = int(input("Kérek még egy számot':"))

#max(szam,szam1)

if szam1 < szam2:
  print(f"A nagyobb érték {szam2}")
elif szam2 < szam1:
  print(f"A nagyobb érték  {szam1}")
else:
  print("A két szám egyenlő")
