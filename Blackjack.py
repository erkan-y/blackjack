#Blackjack oyunu son hali
import random   
import os
import time
def devam():
  while True:
    print("devam etmek istiyor musunuz?: ")
    devam= input("yes/no: ")
    if devam.lower() not in("yes","no"):
      print("hatalı giriş yaptınız.")
    elif devam.lower() == "yes":
      os.system('cls')
      print("kartlar karılıyor...")
      time.sleep(2)
      break
      return False
    else:
      return True
def sonuç(toplam_el,toplam_com):      #sonuç çıktıları için fonksiyon
  if toplam_el>21 and toplam_com<21:
      print("kaybettiniz")
  elif toplam_el>21 and toplam_com>21:
      print("berabere")
  elif toplam_el==21:
      print("Blackjack")
  elif toplam_el<21 and toplam_com>21:
      print("kazandınız")
  elif toplam_el < 21 and toplam_el>toplam_com:
      print("kazandınız")
  elif toplam_el<toplam_com:
      print("kaybettiniz")
  elif toplam_el==toplam_com:
      print("berabere")
  elif toplam_el<21 and toplam_com >21:
      print("kazandınız")
def kartçek(el,top):
    kağıt = random.choice(kağıtlar)   #önce kağıt cinsini çekiyoruz
    gelen = random.choice(iskambil[kağıt]) #değerini de seçip variable atıyoruz
    top.append(gelen)  #listelere atıyoruz
    el.append(kağıt+" "+gelen)
    iskambil[kağıt].remove(gelen) #çıkan kağıtları desteden çıkartıyoruz
                                    # ki bir daha gelmesin
def el_hesaplama(el_top):
    toplam_el=0
    for i in range(0,len(el_top)):  #J;Q;K için 10 atıyoruz
      if el_top[i] in(faces):
        el_top[i] = "10"
    el_top.sort()                 #küçükten büyüğe sıraladım, AS sona kaldı varsa
    for i in el_top:
      if i != 'AS':
        toplam_el += int(i)
      if i == 'AS':
        if (toplam_el+11)>21:          #21'den büyükse As 1, değilse 11 değerinde
          i = 1
          toplam_el += i
        else: 
          i = 11
          toplam_el += i
    return toplam_el
print("Blackjack oyununa hoş geldiniz..")
print()
while True:
  kağıtlar = ["karo","kupa","sinek","maça"]
  faces = ["Jack","Queen","King"]
  liste = ["AS","2", "3", "4", "5", "6", "7", "8", "9", "10"]+faces
  iskambil = {"karo":liste.copy(),
              "kupa":liste.copy(),
              "sinek":liste.copy(),
              "maça":liste.copy()}
  el = []     # elimizdeki kağıtları tutacak liste
  el_top = [] # elimizin sayı değerlerini tutacak liste
  com = []    #bilgisayarın elini tutacak liste
  com_top = []  #bilgisayarın sayı değerlerini tutacak liste
  toplam_el, toplam_com = 0,0 #toplamları tutacak variable 
  counter1,counter2=0,0 # while döngüsünde kullanılacak counter
  

  while counter1<2:       #her iki oyuncuya kart çektirdim
    kartçek(el,el_top)
    counter1 +=1
  while counter2<2:
    kartçek(com,com_top)
    counter2 +=1

  print(f"sizin eliniz: {el}")        # elleri hesaplattım
  toplam_el= el_hesaplama(el_top)
  print(f"sizin eliniz: {toplam_el}")
  toplam_com = el_hesaplama(com_top)
  print("bilgisayarın eli: "+ com[0]+" + *-*-*")

  while toplam_el<21:                   #tekrar kart çekmek istediği sürece
    while True:                          #aynı fonksiyonları çağırıyorum
      print("kart çekmek ister misiniz?")
      girdi = input("yes/no?: ")
      if girdi.lower() not in("yes","no"):
        print("sadece yes/no girişi yapın")
      else: 
        break
    if girdi.lower() == "yes":
      kartçek(el,el_top)
      toplam_el = el_hesaplama(el_top)
      print(f"sizin eliniz: {el}")
      print(f"sizin eliniz: {toplam_el}")
    if girdi.lower()=='no':
      break
  while toplam_com<14 or (toplam_com < toplam_el and toplam_com<21):    #bilgisayarın eli 14'den küçükse 
    kartçek(com,com_top)                                               #veya kaybediyorsa kart çekecek
    toplam_com = el_hesaplama(com_top)
  print(f"bilgisayarın eli: {com}")
  print(f"bilgisayarın eli: {toplam_com}")

  sonuç(toplam_el,toplam_com)
  if devam():
    print("yine bekleriz.")
    break
  
