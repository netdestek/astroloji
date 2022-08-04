def fok1() :
 try:
  global gun
  gun = int(input("doğum gününü giriniz: "))
  global ay
  ay = int(input("doğum ayını giriniz : "))
  global yil
  yil = int(input("doğum yılını giriniz: "))
 except ValueError:
  print("Enter tuşuna basmadan önce Rakam Girmelisin, Harf Değil!!! \n\n\n")
  fok1()
  exit()
 gun = str(gun)
 ay = str(ay)
 yil = str(yil)
 oglak = "Oglak burcu\narapça karşılığı: Davar-ül kurban\nelementi: Toprak\nyıldızı: Satürn\niteliği: Öncü\nUygun Meslekler: Muhasebeci, yönetici, komisyoncu, ekonomist, mühendis, devlet memuru\ntaş işleme, politika, emlakçılık, mimarlık\n"
 kova = "Kova burcu\narapça karşılığı: damacana\nelementi: Hava\nyıldızı: Satürn\nniteliği: Sabit\nUygun Meslekler: Astrolog, pilot, mucit, makinist, teknoloji uzmanı, bilim-kurgu yazarı, bilgisayar\nbilişim, teknoloji uzmanı, elektrik, elektronik, psikoloji\n"
 balik = "Balik burcu\narapça karşılığı: Mahsulat-ı derya\nelementi: Su\nyıldızı: Jupiter\nniteliği: Değişken\nUygun Meslekler: Aktör, yardım kuruluşu çalışanı, illüzyonist, müzisyen, tasarımcı\nmedyum, ruhsal danışmanlık, dalgıçlık, din görevlisi, mimari, reklam, balıkçılık, fotoğrafçılık, sanat dalları\n"
 koc = "Koç burcu\narapça karşılığı: Davar-ül kurban\nelementi: Ateş\nyıldızı: Mars\nniteliği: Öncü\nUygun meslekler: Doktor, askerlik, polislik, metal işleme, ralli pilotluğu, cerrahlık, politika\npazarlama, gazetecilik, şov dünyası, sinema, mühendislik\n"
 boga = "Boga burcu\narapça karşılığı: Sığır-ül camığ\nelementi toprak\nyıldızı: Venüs\nniteliği: Sabit\nUygun meslekler: Ressamlık, çiftçi, restoran ve otel işletmeciliği, kozmetik, el sanatları\nbankerlik, iç mimari, dekorasyon, kuyumculuk, müzik, mimarlık\n"
 ikizler = "İkizler burcu\narapça karşılığı: Adem-ül çift-i aynen\nelementi: Hava\nyıldızı: Merkür\nniteliği: Değişken\nUygun meslekler: Ticaret, gazetecilik, öğretmenlik, edebiyat, pazarlama, resim\nmüzik, bilim, satış, reklam, tanıtım, psikoloji, politika, danışmanlık, hukuk, matematik\ngözünün gördüğü herşeyi yapabilecek kabiyette!\n"
 yengec = "Yengec burcu\narapça karşılığı: Mahluk-ül derya-ül böcekvari\nelementi: Su\nyıldızı: Ay\nniteliği: Öncü\nUygun meslekler: Psikoloji, hekimlik, müzisyenlik, maliye, armatörlük, bahçeçilik\nbelediyecilik, hastabakıcılık, sosyal yardım görevlisi, aşçılık\n"
 aslan = "Aslan burcu\narapça karşılığı: Malukat-ül vahşi\nelementi: Ateş\nyıldızı: Güneş\nniteliği: Sabit\nUygun meslekler: Yöneticilik, organizatörlük, politika, eğitim- öğretim, iç mimari, kozmetik\naktörlük, sanat yönetmenliği, tiyatro, kuyumculuk, subaylık\n"
 basak = "Basak burcu\narapça karşılığı: Nebatat-ül arpa vü yulaf\nelementi: Toprak\nyıldızı: Merkür\nniteliği: Değişken\nUygun meslekler: Ekonomist, bilgi işlem, analist, muhabirlik, danışmanlık\nmatematik, arşivcilik, pazarlama, mühendislik, öğretmenlik, bakıcılık, tamircilik\n"
 terazi ="Terazi burcu\narapça karşılığı: Endaze-i kantar\nelementi: Hava\nyıldızı: Venüs\nniteliği: Öncü\nUygun meslekler: İç mimari, diplomatlık, elçilik, politika, halkla ilişkiler, danışmanlık\nreklamcılık, ticari temsilcilik, hukuk müşavirliği, sanat, sanat eleştirmenliği, müzik, pazarlamacılık\n"
 akrep ="Akrep burcu\narapça karşılığı: Haşerat-ül zehr-i zıkkım\nelementi: Su\nyıldızı: Mars\nniteliği: Sabit\nUygun meslekler: Dedektiflik, müfettişlik, casusluk, terapist, operatör doktorluk\nyarışçılık, askerlik, pilotluk, politika, görsel sanatlar, hukuk, psikoloji, mühendislik\nBilgisayar Programcısı, bu tipler özgür olmayı seçer!\nÖzellikleri: kendilerine yapılan iyiliği ve kötülüğü asla unutmazlar, duygularına hükmederler\nona geçmişte bir iyilik yaptıysanız\nuçağınız Alp dağlarına düşse dahi sadece oturup bekleyin akrep dostunuz\nsizi kurtarmaya mutlaka gelecektir!\nTürkye AKREP BURCU kuşağındadır. Türkiyenin burcu AKREP BURCUDUR.\n"
 yay   = "Yay burcu\narapça karşılığı: Silah-ül zemberek\nelementi: Ateş\nyıldızı: Jupiter\nniteliği: Değişken\nUygun Meslekler: Akademisyen, gezgin, reklamcı, danışman, din adamı, yayıncı, avukat\ntercüman, eğitim- öğretim, ihracat, alternatif tıp\n"
 yanlis = "henüz doğmadınız"

 d = 0
 e = gun + ay + yil
 for i in e:
    d += int(i)

 toplam = 0
 for rakam in str(int(d)):
    toplam += int(rakam)

 print(gun, ay, yil)
 aa = "11 EN YÜKSEK RUHSAL GÜÇ! "
 ab = "Ruhsal Gücünüz 10 OLAĞANÜSTÜ!"
 ac = "Ruhsal Gücünüz 9 muhteşem"
 ae = "Ruhsal Gücünüz 8 çok iyi"
 af = "Ruhsal Gücünüz 7 gayet iyi"
 ag = "Ruhsal Gücünüz 6 normal"
 ah = "Ruhsal Gücünüz 5 normalin altında"
 aj = "Ruhsal Gücünüz 4 zayıf"
 dd = "Guhsal Gücünüz yok gibi"
 if toplam > 10 : dd = aa
 elif toplam == 10 : dd = ab
 elif toplam == 9 : dd = ac
 elif toplam == 8 : dd = ae
 elif toplam == 7 : dd = af
 elif toplam == 6 : dd = ag
 elif toplam ==5 : dd = ah
 elif toplam == 4 : dd = aj
 elif toplam < 4 : dd = 0

 if int(gun) >= 32 or int(ay) >12 :
    print("kafan karışık sanırım \nyalnış tarih aralığı girdiniz \nTekrar Denemek için Enter'a Çıkmak için Başka Tuşa Basın")

    alfa = input("")
    if alfa == "":
     fok1()
     exit()
    else:
     print("Çıkış Yapılıyor ... ")
 else:
  if dd == 0: print(yanlis)
  else:
    if int(ay) == 1:
     if int(gun) < 22 : print(oglak  + dd ) # oğlak 1 ocak 21 ocak (oğlak 22 aralık 21 ocak)
     else: print(kova + dd) # kova  22 ocak   31 ocak  (kova  22 ocak   19 şubat)
    elif int(ay) == 2:
     if int(gun) < 20: print(kova + dd) # kova  1 şubat   19 şubat  (kova  22 ocak   19 şubat)
     else: print(balik + dd)  # balık 20 şubat  31 şubat (balık 20 şubat  20 mart )
    elif int(ay) == 3:
     if int(gun) < 21:print(balik + dd)  # balık  1 mart 20 mart  (balık 20 şubat  20 mart )
     else: print(koc + dd)  # koç  21 mart 31 mart  (koç   21 mart   20 nisan )
    elif int(ay) == 4:
     if int(gun) < 21:print(koc + dd )  # koç  1 nisan  20 nisan  (koç   21 mart   20 nisan )
     else: print(boga + dd) # boğa  21 nisan 31 nisan    (boğa  21 nisan  21 mayıs)
    elif int(ay) == 5:
     if int(gun) < 22:  print(boga + dd) # boğa  1 mayıs 21 mayıs    (boğa  21 nisan  21 mayıs)
     else: print(ikizler + dd) # ikizler 22 mayıs 31 mayıs    (ikizler 22 mayıs 22 haziran)
    elif int(ay) == 6:
     if int(gun) < 23: print(ikizler + dd) # ikizler 1 haziran 22 haziran    (ikizler 22 mayıs 22 haziran)
     else: print(yengec + dd) # yengeç 23 haziran 31 haziran    (yengeç 23 haziran 22 temmuz)
    elif int(ay) == 7:
     if int(gun) < 23: print(yengec + dd) # yengeç 1 temmuz 22 temmuz    (yengeç 23 haziran 22 temmuz)
     else: print(aslan + dd) # aslan 23 temmuz 31 temmuz    (aslan 23 temmuz 22 ağustos)
    elif int(ay) == 8:
     if int(gun) < 23: print(aslan + dd) # aslan 1 agustos 22 agustos    (aslan 23 temmuz 22 ağustos)
     else: print(basak + dd)  # başak 23 agustos 31 agustos    (başak 23 ağustos 22 eylül
    elif int(ay) == 9:
     if int(gun) < 23: print(basak + dd)  # başak 1 eylül 22 eylül    (başak 23 ağustos 22 eylül
     else:print(terazi + dd)  # terazi 23 eylül 31 eylül    (terazi 23 eylül 22 ekim)
    elif int(ay) == 10:
     if int(gun) < 23: print(terazi + dd) # terazi 1 ekim 22 ekim    (terazi 23 eylül 22 ekim)
     else:print(akrep + dd)  # akrep 23 ekim  31 ekim    (akrep 23 ekim 21 kasım)
    elif int(ay) == 11:
     if int(gun) < 22: print(akrep + dd) # akrep 1 kasım 21 kasım    (akrep 23 ekim 21 kasım)
     else:print(yay + dd)  # yay 22 kasım 31 kasım   (yay 22 kasım 21 aralık)
    elif int(ay) == 12:
     if int(gun) < 22:print(yay + dd)  # yay 1 aralık 21 aralık  (yay 22 kasım 21 aralık)
     else:print(oglak + dd)  # oğlak 22 aralık 31 aralık (oğlak 22 aralık 21 ocak)
     exit()
fok1()
