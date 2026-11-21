import random

def tas_kagit_makas():
    secenekler = ['taş', 'kağıt', 'makas']
    print("Taş - Kağıt - Makas Oyununa Hoş Geldiniz! (Çıkmak için 'q' tuşuna basın)")
    
    oynanan_oyun = 0
    kullanici_skor = 0
    bilgisayar_skor = 0
    beraberlik = 0

    while True:
        kullanici_secimi = input("Seçiminiz (taş/kağıt/makas): ").lower()
        
        if kullanici_secimi == 'q':
            # Oyun bittiğinde genel skoru ve kazananı ekrana basıyoruz
            print("\n" + "="*30)
            print("📊 OYUN SONU İSTATİSTİKLERİ")
            print("="*30)
            print(f"Toplam Oynanan Tur: {oynanan_oyun}")
            print(f"Sizin Galibiyetiniz: {kullanici_skor}")
            print(f"Bilgisayarın Galibiyeti: {bilgisayar_skor}")
            print(f"Beraberlik: {beraberlik}")
            print("-" * 30)
            
            # Genel kazanma durumu kontrolü
            if kullanici_skor > bilgisayar_skor:
                print("🏆 GENEL KAZANAN: SİZ OLDUNUZ! Tebrikler!")
            elif bilgisayar_skor > kullanici_skor:
                print("🤖 GENEL KAZANAN: BİLGİSAYAR! Belki bir dahaki sefere.")
            else:
                if oynanan_oyun > 0:
                    print("🤝 GENEL DURUM: BERABERE! Dostluk kazandı.")
                
            print("="*30 + "\n")
            break
        
        if kullanici_secimi not in secenekler:
            print("Geçersiz seçim! Lütfen 'taş', 'kağıt' veya 'makas' yazın.")
            continue

        oynanan_oyun += 1
        bilgisayar_secimi = random.choice(secenekler)
        
        print(f"\n--- {oynanan_oyun}. Tur ---")
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

        if kullanici_secimi == bilgisayar_secimi:
            print("Sonuç: Berabere!\n")
            beraberlik += 1
        elif (kullanici_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
             (kullanici_secimi == 'kağıt' and bilgisayar_secimi == 'taş') or \
             (kullanici_secimi == 'makas' and bilgisayar_secimi == 'kağıt'):
            print("Sonuç: Kazandınız! 🎉\n")
            kullanici_skor += 1
        else:
            print("Sonuç: Kaybettiniz! 😔\n")
            bilgisayar_skor += 1

if __name__ == "__main__":
    tas_kagit_makas()
