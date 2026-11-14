import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    
    # ANA OYUN DÖNGÜSÜ: Tekrar oynama isteği evet oldukça buralar baştan çalışır.
    while True:
        print("\nZorluk Seviyeleri:")
        print("1 - Kolay (1-50 arası, 10 Can)")
        print("2 - Orta  (1-100 arası, 7 Can)")
        print("3 - Zor   (1-200 arası, 5 Can)\n")

        # Kullanıcıdan geçerli bir zorluk seviyesi alana kadar sor
        while True:
            seviye = input("Bir zorluk seviyesi seçin (1/2/3): ")
            if seviye == '1':
                ust_limit = 50
                can = 10
                break
            elif seviye == '2':
                ust_limit = 100
                can = 7
                break
            elif seviye == '3':
                ust_limit = 200
                can = 5
                break
            else:
                print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.\n")

        rastgele_sayi = random.randint(1, ust_limit)
        print(f"\nBilgisayar 1 ile {ust_limit} arasında bir sayı tuttu.")
        print(f"Toplam {can} hakkın var. Başarılar!\n")

        # Can sıfırdan büyük olduğu sürece tahmin döngüsü devam eder
        while can > 0:
            try:
                tahmin = int(input(f"Tahminin nedir? (Kalan Can: {can}): "))
            except ValueError:
                # Kullanıcı harf girerse programın çökmesini engeller
                print("Lütfen sadece sayı girin!\n")
                continue

            if tahmin < rastgele_sayi:
                print("Daha büyük bir sayı girin.\n")
            elif tahmin > rastgele_sayi:
                print("Daha küçük bir sayı girin.\n")
            else:
                print(f"Harika! Sayıyı doğru bildin: {rastgele_sayi}")
                break # Doğru bilirse tahmin döngüsünden çık
            
            can -= 1 # Yanlış tahminde canı 1 azalt

        # Tahmin döngüsü bittiğinde can sıfırlanmışsa kaybetme mesajı
        if can == 0:
            print(f"Maalesef canın bitti! Tuttuğum sayı: {rastgele_sayi}")
        
        # YENİDEN OYNAMA SORGUSU
        tekrar = input("\nBir daha oynamak ister misin? (e/h): ").lower()
        if tekrar != 'e':
            print("Oynadığın için teşekkürler! Görüşmek üzere.")
            break # Eğer 'e' basılmazsa en dıştaki Ana Oyun Döngüsünü kırar ve biter.

if __name__ == "__main__":
    sayi_tahmin_oyunu()
