from datetime import datetime  # Tarih ve saat bilgilerini kullanmak için datetime aracını programa ekler.
ad = input("Adınız nedir? ")  # Kullanıcıdan adını alır.
dogum_yili = int(input("Doğum yılınız nedir? "))  # Doğum yılını alır ve sayıya çevirir.
bu_yil = datetime.now().year  # İçinde bulunduğumuz yılı öğrenir.
if dogum_yili > bu_yil:  # Doğum yılı bu yıldan büyük mü diye kontrol eder.
    print("HATA! Doğum yılınız bu yıldan büyük olamaz.")  # Geçersiz doğum yılı için uyarı gösterir.
else:  # Doğum yılı bu yıldan büyük değilse aşağıdaki işlemleri yapar.
    yas = bu_yil - dogum_yili  # Yaşı hesaplar.
    print(f"Merhaba {ad}, hoş geldin! Yaklaşık {yas} yaşındasın.")  # Kişiye özel mesajı ekrana yazar.