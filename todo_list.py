def todo_baslat():
    # Görevleri tutacağımız boş listemiz
    gorevler = []
    print("Yapılacaklar Listesi Uygulamasına Hoş Geldiniz!")
    
    while True:
        print("\n" + "="*30)
        print("1. Görev Ekle")
        print("2. Görevleri Görüntüle")
        print("3. Görev Sil")
        print("4. Çıkış")
        print("="*30)
        
        secim = input("Lütfen bir işlem seçin (1/2/3/4): ").strip()
        
        # 1. GÖREV EKLEME
        if secim == '1':
            yeni_gorev = input("Eklenecek görevi yazın: ").strip()
            if yeni_gorev: # Kullanıcı boş enter'a basmadıysa listeye ekle
                gorevler.append(yeni_gorev)
                print(f"✅ '{yeni_gorev}' listeye eklendi!")
            else:
                print("⚠️ Boş bir görev ekleyemezsiniz!")
                
        # 2. GÖREVLERİ GÖRÜNTÜLEME
        elif secim == '2':
            print("\n--- Görevleriniz ---")
            if not gorevler: # Liste boşsa
                print("📝 Listeniz şu an boş. Hadi bir şeyler ekleyelim!")
            else:
                # enumerate, listeyi 1'den başlayarak numaralandırır
                for i, gorev in enumerate(gorevler, 1):
                    print(f"{i}. {gorev}")
                    # YENİ EKLENEN SATIR: Kullanıcı okuyana kadar programı burada bekletir
            input("\nMenüye dönmek için Enter'a basın...")
        # 3. GÖREV SİLME
        elif secim == '3':
            print("\n--- Görev Sil ---")
            if not gorevler:
                print("⚠️ Silinecek görev yok, listeniz zaten boş!")
            else:
                for i, gorev in enumerate(gorevler, 1):
                    print(f"{i}. {gorev}")
                
                try:
                    silinecek_no = int(input("\nSilmek istediğiniz görevin numarasını girin (İptal için 0): "))
                    if silinecek_no == 0:
                        print("İşlem iptal edildi.")
                    elif 1 <= silinecek_no <= len(gorevler):
                        # pop(), verilen indeksteki veriyi listeden atar.
                        # İnsanlar 1,2,3 diye sayar ama Python 0,1,2 diye saydığı için -1 yapıyoruz.
                        silinen = gorevler.pop(silinecek_no - 1)
                        print(f"🗑️ '{silinen}' listeden başarıyla silindi!")
                    else:
                        print("⚠️ Listede böyle bir numara yok!")
                except ValueError:
                    print("⚠️ Lütfen sadece numara girin!")
                    
        # 4. ÇIKIŞ
        elif secim == '4':
            print("👋 Çıkış yapılıyor. İyi günler!")
            break
            
        else:
            print("⚠️ Geçersiz seçim, lütfen menüdeki numaralardan birini girin.")

if __name__ == "__main__":
    todo_baslat()
