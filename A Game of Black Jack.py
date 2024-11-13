#21 oyunu
import random
import time

Oyuncu=[]
Kupi=[]
kupigizli=[] 
n=0.00
x=0
y=0
z=0

def başlangıç():
  global n
  while True:
   n=float(input("Ne kadar para yatıracaksın:"))
   if n>bank:
      print("Bu kadar çipin yok")
   else:
      break
  a=random.randint(1,11)
  b=random.randint(1,11)
  global x
  x=a+b
  Oyuncu.append(a)
  Oyuncu.append(b)
  c=random.randint(1,11)
  h=random.randint(1,11)
  global y
  y=c
  global z
  z=c+h
  Kupi.append(c)
  kupigizli.append(c)
  kupigizli.append(h)
  
def kartal():
  d=random.randint(1,11)
  global x
  x=x+d
  Oyuncu.append(d)

def kupial():
  global z
  while len(kupigizli)<5 or z<17:
    e=random.randint(1,11)
    z=z+e
    kupigizli.append(e)
    if z>17 or len(kupigizli)==5 :
      break
  

def karhes():
  g=bank-bankilk
  if g>0:
    print(g,"₺"," ","Kardasın")
  elif g==0:
    print("Nötr hiç yoktan iyidir")
  else:
    print(-g,"₺"," ","Zarardasın")





#Başlangıç
bank=float(input("Ne kadar çip istersin:"))
bankilk=bank

while True:
  print("Mevcut paran:",bank)
  if bank==0:
    print("Paran bitti nay nay")
    karhes()
    n=input("Herhangi bir tuşa bas çık")
    break
  başlangıç()
  print("Yatırılan:",n,"kalan para:",(bank-n))
  time.sleep(1)
  print(Kupi," "*3,"Kupiyer kart toplamı:",y,"+x")
  print(Oyuncu," "*3,"Kartlarının toplamı:",x)
  while True:
    if x<21 or len(Oyuncu)<5:
      k=str(input("Kart alıcak mısın yoksa kalıcak mısın ?  (A/K)      :"))
      if k=="a" or k=="A":
        kartal()
        print("")
        print("<----------------------------------------------------->")
        print(Kupi," "*3,"Kupiyer kart toplamı:",y,"+x")
        print(Oyuncu," "*3,"Kartlarının toplamı:",x)
        print("<----------------------------------------------------->")
        print("")
        if x>=21 or len(Oyuncu)==5:
          break
        else:
          continue
      elif k=="k" or k=="K":
         break
      else:
         print("Yaz kardeşim yaz")
    elif x>=21 or len(Oyuncu)==5:
      break

  kupial()
  print(kupigizli," "*3,"Kupiyer kart toplamı:",z)
  print(Oyuncu," "*3,"Kartlarının toplamı:",x)

  
  if x==21 and z!=21:
    bank=bank+(2.5*n)-n
    print(2.5*n,"₺","Kazandın","Total paran:",bank)
    print("1.yol")
  
  elif x>z and x<21:
    bank=bank+n
    print(2*n,"₺","Kazandın","Total paran:",bank)
    print("2.yol")
  
  elif z<x and x<21:
    bank=bank+(n)
    print("3.yol")
    print(2*n,"₺","Kazandın","Total paran:",bank)
  
  elif x<21 and z>21:
    bank=bank+n
    print("4.yol")
    print(2*n,"₺","Kazandın","Total paran:",bank)
  
  elif x>21 and z>21 and x<z:
    bank=bank+n
    print("5.yol")
    print(2*n,"₺","Kazandın","Total paran:",bank)
  
  elif len(Oyuncu)==5 and x<=21:
    bank=bank+n
    print("6.yol")
    print(2*n,"₺","Kazandın","Total paran:",bank)
  
  elif z==21 and x!=21:
    bank=bank-n
    print("7.yol")
    print(n,"₺","Kaybettin","Total paran:",bank)
  
  elif x==z:
    bank=bank-n
    print(n,"₺","Geri döndü","Total paran:",bank)
    print("8.yol")
  elif x>21 and z>21 and z<x:
    bank=bank-n
    print("9.yol")
    print(n,"₺","Kazandın","Total paran:",bank)
  else:
     bank=bank-n
     print(n,"₺","Kaybettin","Total paran:",bank)
     print("10.yol")
    #Burayı daha ayrıntılı hale getirmen lazım
  
  time.sleep(1)
  while True:
    s=str(input("Devam mı Tamam mı ? (D/T) :"))
  
    if s=="T" or s=="t":
      karhes()
      n=input("Herhangi bir tuşa bas çık")
      break
  
    elif s=="d" or s=="D" :
      for i in range(1,len(Oyuncu)+1):
        Oyuncu.pop()  
      for j in Kupi:
        Kupi.pop()
      for k in range(1,len(kupigizli)+1):
        kupigizli.pop()
      break
    else:
      print("Yaz kardeşim yaz")
  if s=="T" or s=="t":
    break 
  