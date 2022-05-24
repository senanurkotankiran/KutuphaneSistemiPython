import sqlite3
def odemeYap():

        satisDosyasi = open("sayisDosyasi.txt", "w")
        print("Odeme bolumune hosgeldiniz!")
        name = input("Isim : ")
        surname = input("Soyisim : ")
        address = input("Adress : ")
        tel = input("Telefon No : ")

    
        try:
            kart = int(input("Kart No :"))
            if len(str(kart))!=16:
                raise SystemExit("kart no 16 haneden oluşmalı....İşleminiz iptal edildi....")
        except ValueError:
            if ValueError != True:
                raise SystemExit("Kart no sayılardan oluşmalıdır...İşleminiz iptal edildi...")
        

        satisDosyasi.write(name)
        satisDosyasi.write("\n")
        satisDosyasi.write(surname)
        satisDosyasi.write("\n")
        satisDosyasi.write(address)
        satisDosyasi.write("\n")
        satisDosyasi.write(tel)
        satisDosyasi.write("\n")
        satisDosyasi.write("Odeme isleminiz tamamlandi. Tesekkur ederiz.")

        veritabani = sqlite3.connect("aliciBilgileri.db")
        baglanti = veritabani.cursor()
        baglanti.execute("CREATE TABLE IF NOT EXISTS aliciBilgileri(Ad,Soyad,Adres,Numara)")
        sorgu = "insert into aliciBilgileri VALUES (?,?,?,?)"
        baglanti.execute(sorgu,(name,surname,address,tel))
        veritabani.commit()
        veritabani.close()

