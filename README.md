# 🚀 Python'a Giriş: Yapay Zeka Destekli İlk Mini Projelerim

Selamlar! Python öğrenme sürecimde temel mantığı (döngüler, if-else yapıları, temel modüller) oturtmak için yapay zeka desteğiyle yazdığım 5 ufak projeyi bu depoda topladım. Yeni başlayanlar için güzel bir pratik arşivi oldu.

## Bu Çalışmanın İçinde Neler Var?

* **1. Sayı Tahmin Oyunu (`sayi_tahmin.py`) — **  
  Bilgisayarın tuttuğu sayıyı yönlendirmelerle bulmaya çalıştığımız klasik oyun. Son güncellemeyle oyuna zorluk seviyeleri (Kolay, Orta, Zor), can hakkı mekaniği ve hatalı girişleri (harf girilmesi vb.) çökmeden yakalayan bir kontrol sistemi ekledim.  
  *(Pratikler: `random` modülü, iç içe `while` döngüleri, `if-elif-else`, `try-except` hata yönetimi)*

* **2. Rastgele Şifre Oluşturucu (`sifre_olusturucu.py`)**  
  İstediğimiz uzunlukta, kırılması zor şifreler (harf, rakam, özel karakter) üreten bir script.  
  *(Pratikler: `string` modülü, `for` döngüsü)*

* **3. To-Do / Yapılacaklar Listesi (`todo_uygulamasi.py`)**  
  Terminal üzerinden çalışan, listeye görev ekleyip görüntüleyebildiğimiz basit bir görev yöneticisi.  
  *(Pratikler: Liste (`list`) yönetimi, `append`, `enumerate`)*

* **4. Taş - Kağıt - Makas (`tas_kagit_makas.py`)**  
  Bildiğimiz klasik oyun. Kullanıcı 'q' tuşuna basıp çıkana kadar bilgisayarla oynamaya devam edebilirsiniz.  
  *(Pratikler: Mantıksal operatörler, `break`/`continue`)*

* **5. Metin Analiz Aracı (`kelime_sayaci.py`)**  
  İçine yapıştırdığınız bir cümlenin kaç kelime ve karakterden (boşluklu/boşluksuz) oluştuğunu sayar.  
  *(Pratikler: `len()`, `split()`, metin parçalama)*

## 🛠️ Nasıl Çalıştırılır?

Bilgisayarınızda Python yüklüyse, terminali (veya komut istemini) açıp dosyaların olduğu klasöre gidin. Ardından çalıştırmak istediğiniz dosyanın adını yazın:

```bash
python sayi_tahmin.py
