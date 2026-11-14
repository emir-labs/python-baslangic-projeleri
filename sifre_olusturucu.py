import random
import string

def sifre_olustur(uzunluk=12):
    # Tüm harfleri, rakamları ve özel karakterleri tek bir havuzda birleştiriyoruz
    karakterler = string.ascii_letters + string.digits + string.punctuation
    
    # Belirlenen uzunluk kadar rastgele karakter seçip birleştiriyoruz
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

if __name__ == "__main__":
    print("Rastgele Şifre Oluşturucuya Hoş Geldiniz!")
    
    # Kullanıcıdan uzunluk bilgisini alma (Hata yapıp harf girmesine karşı try-except ekleyebiliriz ama şimdilik en sade hali)
    uzunluk_girdisi = input("Şifre uzunluğunu girin (Varsayılan 12 için Enter'a basın): ")
    
    # Kullanıcı boş geçerse 12 karakter yapar, sayı girerse o uzunlukta yapar
    if uzunluk_girdisi:
        uzunluk = int(uzunluk_girdisi)
        yeni_sifre = sifre_olustur(uzunluk)
    else:
        yeni_sifre = sifre_olustur()
        
    print(f"\nOluşturulan Şifreniz: {yeni_sifre}")
