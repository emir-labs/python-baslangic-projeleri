def kelime_ve_harf_say():
    print("Gelişmiş Metin Analiz Aracı'na Hoş Geldiniz!")
    metin = input("Lütfen analiz edilecek metni girin:\n")
    
    # Kullanıcı boş basıp geçerse program çökmesin diye kontrol
    if not metin.strip():
        print("Hiç metin girmediniz!")
        return

    # KULLANICIDAN ARANACAK HARF/İFADE İSTEME (Opsiyonel hale getirildi)
    aranan_ifade = input("\nMetinde aramak istediğiniz bir harf veya kelime girin (Atlamak için Enter'a basın): ").strip()

    # Temel Sayım İşlemleri
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)
    karakter_sayisi = len(metin)
    bosluksuz_karakter = len(metin.replace(" ", ""))
    
    # Özel Harf/Kelime Sayımı (Sadece kullanıcı bir kelime/harf girdiyse çalışır)
    if aranan_ifade:
        # Hem metni hem de aranan harfi küçük harfe çeviriyoruz ki "A" ile "a" ayrımı yapmasın
        aranan_sayisi = metin.lower().count(aranan_ifade.lower())

    # Sonuçları Yazdırma
    print(f"\n--- Temel İstatistikler ---")
    print(f"Toplam Kelime: {kelime_sayisi}")
    print(f"Toplam Karakter (Boşluklar dahil): {karakter_sayisi}")
    print(f"Toplam Karakter (Boşluksuz): {bosluksuz_karakter}")

    # Arama yapıldıysa sonucunu ekrana basıyoruz
    if aranan_ifade:
        print(f"\n--- Özel Arama Sonucu ---")
        print(f"Aradığınız '{aranan_ifade}' metinde toplam {aranan_sayisi} kez kullanılmış.")

if __name__ == "__main__":
    kelime_ve_harf_say()
