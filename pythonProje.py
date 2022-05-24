import Odeme
print("Kütüphane Sistemine hoşgeldiniz!Sistem içeriğini goruntulemek icin kayit olunuz...")

# Kullanıcı Kayıt
class kullanici:
    def __init__(self):
        while True:
            try:
                self.kullaniciAdi=input("kullanici adinizi girin....")
                self.sifre = input("sifrenizi girin...")
            
                if len(self.kullaniciAdi) <=3 :
                    print("kullanici adi 4 haneden az olamaz...Tekrar deneyin")
                    continue
                elif  len(self.sifre)<=4 : 
                    print("Sifre ise 5 haneden az olamaz...Tekrar deneyin") 
                    continue
                else:
                    break
            except Exception:
                raise SystemExit( "beklenmeyen hata...")

kullanici1=kullanici()

# Kullanıcı Giriş
girisHakki = 3

while girisHakki > 0:
    girisHakki -= 1
    girisKullaniciAdi = input("Sistemde kayitli kullanici adinizi girin...")
    girisSifre = input("Sistemde kayitli sifrenizi girin...")

    if girisKullaniciAdi == kullanici1.kullaniciAdi and girisSifre == kullanici1.sifre:
        print("Hoş geldin {} Anasayfaya yönlendiriliyorsun...".format(kullanici1.kullaniciAdi))
        break
    else:
        print("Kullanici adi veya sifre hatalı! Kalan giriş hakkınız {}".format(girisHakki))
        continue

# Şifre Sıfırlama
while girisHakki == 0:
    cevap= int(input("Şifrenizi sıfırlamak istiyorsanız 1e isteniyorsanız 0a basınn : "))

    if cevap == 1:
        yeniSifre= input("Yeni sifrenizi girin... ")
        yeniSifre = kullanici1.sifre.replace(kullanici1.sifre,yeniSifre)

        if yeniSifre == kullanici1.sifre:
            print("Yeni sifreniz eskisiyle aynı olamaz...")
        if len(yeniSifre) <5:
            print("Sifre ise 5 haneden az olamaz...Tekrar deneyin") 
            continue
        else:
            print("Sifreniz basarıyla yenilendi...Ana Menüye yönlendiriliyorsunuz...")
            break
            
    elif cevap == 0:
        raise SystemExit("Hesap ile bağlantınız kesildi.Çıkış yapılıyor....")
    else:
        print("Geçersiz tuşlama.Kontrol ediniz...")
        


edebiyatListesi= {
   
    "Beyaz Zambaklar Ülkesinde" : 30,
    "Martin Eden" : 21,
    "Dönüşüm" : 12,
    "İki Şehrin Hikayesi" : 25

}
edebiyat = list(edebiyatListesi.items())

egitimListesi = {

    "Acil Matematik Soru Bankası" : 28,
    "Apotemi Fasikül Set" : 132,
    "Limit Tyt Turkce" : 35,
    "345 Yayınları Set" : 95 
}

egitim = list(egitimListesi.items())

cocukListesi ={
    "Pofi - Dişlerim Pırıl Pırıl":20,
    "Bebeğimin İlk Sayı Kartları 2 Yaş Ve Üzeri" : 55,
    "Yavru Hayvanlar Dokun Hisset Keşfet" : 82,
    "İlk Sözcükler Kitabım" : 15
}
cocuk = list(cocukListesi.items())

sepetEkle = 0
alinanListesi = []
while True:
    try:
        listeSec = int(input("Hangi kategoriden kitap alacaginizi secin : Edebiyat=0 ; Egitim=1 ; Cocuk=2 " )) #MENÜ SECİMİ

        if listeSec == 0:
            print(edebiyat)
            try:
                kitapNo = int(input("Lütfen almak istediğiniz kitabın numarasını giriniz..."))
                if kitapNo == 0:
                        print("Beyaz Zambaklar Ülkesinde sepete eklendi.")
                        sepetEkle+=30
                        alinanListesi.append(edebiyat[0])
                elif kitapNo == 1:
                        print("Martin Eden sepete eklendi.")
                        sepetEkle+=21
                        alinanListesi.append(edebiyat[1])
                elif kitapNo == 2:
                        print("Dönüşüm sepete eklendi.")
                        sepetEkle+=12
                        alinanListesi.append(edebiyat[2])
                elif kitapNo == 3:
                        print("İki Şehrin Hikayesi sepete eklendi.")
                        sepetEkle+=25
                        alinanListesi.append(edebiyat[3])
                else:
                    print("Böyle bir kitap bulunmamakta")
            except ValueError:
                print("Geçersiz giriş...")
            
            
            
        elif listeSec == 1:
            print(egitim)
            try:
                kitapNo = int(input("Lütfen almak istediğiniz kitabın numarasını giriniz..."))
                if kitapNo == 0:
                        print("Acil Matematik Soru Bankası sepete eklendi.")
                        sepetEkle+=28
                        alinanListesi.append(egitim[0])
                elif kitapNo == 1:
                        print("Apotemi Fasikül Set sepete eklendi.")
                        sepetEkle+=132
                        alinanListesi.append(egitim[1])
                elif kitapNo == 2:
                        print("Limit Tyt Türkçe sepete eklendi.")
                        sepetEkle+=35
                        alinanListesi.append(egitim[2])
                elif kitapNo == 3:
                        print("345 Yayınları Set sepete eklendi.")
                        sepetEkle+=95
                        alinanListesi.append(egitim[2])
                else:
                    print("Böyle bir kitap bulunmamakta")
            except ValueError:
                print("Geçersiz giriş...")
            
    

        elif listeSec == 2:
            print(cocuk)
            try:
                kitapNo = int(input("Lütfen almak istediğiniz kitabın numarasını giriniz..."))
                if kitapNo == 0:
                        print("Pofi - Dişlerim Pırıl Pırıl sepete eklendi.")
                        sepetEkle+=20
                        alinanListesi.append(cocuk[0])
                elif kitapNo == 1:
                        print("Bebeğimin İlk Sayı Kartları 2 Yaş Ve Üzeri sepete eklendi.")
                        sepetEkle+=55
                        alinanListesi.append(cocuk[1])
                elif kitapNo == 2:
                        print("Yavru Hayvanlar Dokun Hisset Keşfet sepete eklendi.")
                        sepetEkle+=82
                        alinanListesi.append(cocuk[2])
                elif kitapNo == 3:
                        print("İlk Sözcükler Kitabım sepete eklendi.")
                        sepetEkle+=15
                        alinanListesi.append(cocuk[3])
                else:
                    print("Böyle bir kitap bulunmamakta")
            except ValueError:
                print("Geçersiz giriş...")
        else:
                print("Böyle bir kategori bulunmamakta")

            
       
        devamSorgu = int(input("Baska kitap eklemek istiyorsanız 1e istemiyorsanız herhangi bir sayıya basın...")) #İŞLEME DEVAM ETMEK İSTENİYOR MU SORGUSU
        if devamSorgu == 1:
            print("Ana menüye yönlendiriliyorsunuz.....")
            continue

        else:
                    
            print("Siparişiniz oluşturuluyor...")
            print("Sipariş tutarınız onaylıyor musunuz ? : {}".format(sepetEkle))
            try:
                onay = int(input("onayliyorsanız 1e onaylamıyorsanız herhangi bir sayıya basın..."))
                if onay == 1:
                            
                        Odeme.odemeYap()
                        print("Toplam tutar  = {}".format(sepetEkle))                       #GUN SONU RAPORU
                        print("Alinan Kitaplar Listesi = {}" .format(alinanListesi))        #GUN SONU RAPORU
                        print("Satin alim yapan kisi : {}".format(girisKullaniciAdi))       
                        break
                else:
                        print("yanlış giriş tekrar deneyin")
                        break
            except ValueError:
                if ValueError != True:
                    raise SystemExit("Geçersiz giriş...İşleminiz iptal edildi...")
    except ValueError:
                print("Geçersiz giriş...") 
