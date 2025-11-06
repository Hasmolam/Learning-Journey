# C# Programlama Eğitimi — Detaylı İlerleme Kontrol Listesi

Kullanım:
- [ ] — Başlanmadı
- [> ] — Yapılıyor
- [x] — Tamamlandı

Not: Bu dosya ders bazında ayrıntılı kontrol içindir. Üst düzey özet ve oranlar için `README.md` dosyasına bakın.

---

<details>
<summary><strong>İçindekiler</strong> — bölümlere hızlı git</summary>

- [1. Başlarken (35)](#1-başlarken-35)
- [2. Değişken Nedir? (36)](#2-değişken-nedir-36)
- [3. Kod Konsepti Nasıldır? (5)](#3-kod-konsepti-nasıldır-5)
- [4. Tür Dönüşümleri (15)](#4-tür-dönüşümleri-15)
- [5. Operatörler (36)](#5-operatörler-36)
- [6. Akış Kontrol Mekanizmaları (48)](#6-akış-kontrol-mekanizmaları-48)
- [7. Hata Kontrol Mekanizmaları (19)](#7-hata-kontrol-mekanizmaları-19)
- [8. Döngüler (36)](#8-döngüler-36)
- [9. Konseptli Keywordler/Konseptsiz Keywordler? (5)](#9-konseptli-keywordlerkonseptsiz-keywordler-5)
- [10. Yardımcı Manevra Komutları (13)](#10-yardımcı-manevra-komutları-13)
- [11. Ekstra Bilgi (2)](#11-ekstra-bilgi-2)
- [12. Diziler (Arrays) (54)](#12-diziler-arrays-54)
- [13. String Tipi Analizi ve String Fonksiyonları (40)](#13-string-tipi-analizi-ve-string-fonksiyonları-40)
- [14. Dizilerde Verisel Performans (13)](#14-dizilerde-verisel-performans-13)
- [15. Regular Expressions (Düzenli İfadeler) (12)](#15-regular-expressions-düzenli-ifadeler-12)
- [16. Koleksiyon Yapıları (7)](#16-koleksiyon-yapıları-7)
- [17. Foreach İterasyonu (3)](#17-foreach-iterasyonu-3)
- [18. Hazır Sınıflar & Fonksiyonlar (18)](#18-hazır-sınıflar--fonksiyonlar-18)
- [19. Metotlar (Functions) (22)](#19-metotlar-functions-22)

</details>

---

## 1. Başlarken (35)
- [x] 1.1 C# Nedir? — 13 min
- [x] 1.2 ► .NET Framework ve .NET Core Nedir? Farkları Nelerdir? — 08 min
- [x] 1.3 Compiler Nedir? — 04 min
- [x] 1.4 ► .Kodlar Nasıl Compile Edilir? — 04 min
- [x] 1.5 Ortam Tanıtımı – Visual Studio — 07 min
- [x] 1.6 ► Proje ve Solution Kavramları — 03 min
- [x] 1.7 ► Proje Oluşturma, Derleme — 10 min
- [x] 1.8 Ortam Tanıtımı – Visual Studio Code — 03 min
- [x] 1.9 ► Proje Oluşturma, Derleme — 09 min
- [x] 1.10 Dotnet CLI — 05 min
- [x] 1.11 ► Temel Komutlar – help — 02 min
- [x] 1.12 ► Temel Komutlar – new — 03 min
- [x] 1.13 ► Temel Komutlar – restore — 02 min
- [x] 1.14 ► Temel Komutlar – build — 01 min
- [x] 1.15 ► Temel Komutlar – publish — 03 min
- [x] 1.16 ► Temel Komutlar – run — 01 min
- [x] 1.17 ► Paket İle Referans Arasındaki Fark Nedir? — 02 min
- [x] 1.18 ► Proje Modifikasyon Komutları – add package — 01 min
- [x] 1.19 ► Proje Modifikasyon Komutları – add reference — 02 min
- [x] 1.20 ► Proje Modifikasyon Komutları – remove package — 01 min
- [x] 1.21 ► Proje Modifikasyon Komutları – remove reference — 01 min
- [x] 1.22 ► Proje Modifikasyon Komutları – list reference — 01 min
- [x] 1.23 Başlarken Temel İlkeler — 05 min
- [x] 1.24 ► Don’t Repeat Yourself — 09 min
- [x] 1.25 ► Anlamlı İsimlendirme — 04 min
- [x] 1.26 Main Fonksiyonu Nedir? — 10 min
- [x] 1.27 ► dotnet run -value- Yapısı İle Uygulamayı Çalıştırma ve args Parametresine Değer Gönderme — 08 min
- [x] 1.28 ► Top-Level Statements (C# 9.0) — 12 min
- [x] 1.29 Yorum Satırları ve Region — 11 min
- [x] 1.30 Todo Nedir? — 03 min
- [x] 1.31 Debugging Nedir? — 07 min
- [x] 1.32 ► BreakPoint Nedir ve Nasıl Yapılır? — 06 min
- [x] 1.33 ► Watch Penceresi — 03 min
- [x] 1.34 ► Debugsız Uygulamayı Çalıştırma Nasıl Yapılır? — 02 min
- [x] 1.35 Özet — 04 min

## 2. Değişken Nedir? (36)
- [x] 2.1 Değişken Nedir? Bir Programcının Değişkene Neden İhtiyacı Olur? — 08 min
- [x] 2.2 Value Type – Primitive Type – Değer Tipli Değişkenler — 21 min
- [x] 2.3 ► IsPrimitive — 01 min
- [x] 2.4 Değişken Türleri Nelerdir? — 06 min
- [x] 2.5 C# Kuralları — 05 min
- [x] 2.6 Değişken Tanımlama — 06 min
- [x] 2.7 ► RAM’in Yapısı(Stack) — 06 min
- [x] 2.8 ► Değişkenler RAM’de Nasıl Tutulur? — 03 min
- [x] 2.9 ► Değişken Tanımlama Kuralları — 05 min
- [x] 2.10 ►► İsimlendirme Kuralları(Name Convention) (Pascal Case | Camel Case | Snake Case) — 04 min
- [x] 2.11 ►► Değişken İsimlerini @ Operatörüyle Tanımlama — 03 min
- [x] 2.12 Tanımlanmış Değişkene Değer Atama — 19 min
- [x] 2.13 ► Değişkene Değer Atama Kuralları — 23 min
- [x] 2.14 ► (_a, _b) = (a, b) Tuple Türüyle Değer Atama — 07 min
- [x] 2.15 ► Literal Düzenlemeler(C# 7.0) — 01 min
- [x] 2.16 ► Değişken Türüne Uygun Default Değer Atama — 05 min
- [x] 2.17 ► Default Literals — 01 min
- [x] 2.18 Tanımlanmış Değişkenin Değerini Okuma — 05 min
- [x] 2.19 ► Kritik 1 — 04 min
- [x] 2.20 ► Kritik 2 — 01 min
- [x] 2.21 ► Değeri Olmayan Değişkenler! — 03 min
- [x] 2.22 Değişken Davranışları Genel Bakış(ref için farkındalık) — 07 min
- [x] 2.23 Değişkenlerin Faaliyet Alanları (Scope Kavramı) — 09 min
- [x] 2.24 ► Custom Scope Oluşturmak — 03 min
- [x] 2.25 Sabitler(const) — 15 min
- [x] 2.26 Global Değişkenler — 04 min
- [x] 2.27 Değişken Tanımlama Varyasyonları — 02 min
- [x] 2.28 Değişkenler Arası Değer Atama – Deep Copy — 08 min
- [x] 2.29 Değişkenler Arası Değer Atama – Shallow Copy — 05 min
- [x] 2.30 object — 16 min
- [x] 2.31 ► Boxing — 06 min
- [x] 2.32 ► Cast Operatörü — 05 min
- [x] 2.33 ► UnBoxing – Casting — 10 min
- [x] 2.34 var — 12 min
- [x] 2.35 dynamic — 12 min
- [x] 2.36 Özet — 12 min

## 3. Kod Konsepti Nasıldır? (5)
- [x] 3.1 Kod Nasıl Çalışır? — 06 min
- [x] 3.2 Kod Konsepti Nasıldır? — 04 min
- [x] 3.3 ; Operatörü — 04 min
- [x] 3.4 Satır Satır Kod Mantığı Yoktur! — 04 min
- [x] 3.5 Özet — 02 min

## 4. Tür Dönüşümleri (15)
- [x] 4.1 Tür Dönüşümü Nedir? Neden Verilerin Türlerini Değiştirmek/Dönüştürmek İsteriz? — 12 min
- [x] 4.2 Metinsel İfadelerin Diğer İfadelere Dönüştürülmesi | Parse Metodu — 12 min
- [x] 4.3 Metinsel İfadelerin Diğer İfadelere Dönüştürülmesi | Convert Fonksiyonları — 06 min
- [x] 4.4 Diğer İfadelerin Metinsel İfadelere Dönüştürülmesi — 01 min
- [x] 4.5 Sayısal İfadelerin Kendi Aralarında Tür Dönüşümü — 11 min
- [x] 4.6 ► Bilinçsiz Tür Dönüşümü — 05 min
- [x] 4.7 ► Bilinçli Tür Dönüşümü — 07 min
- [x] 4.8 ►► Kritik(Mülakatlar İçin) — 02 min
- [x] 4.9 ►► checked — 04 min
- [x] 4.10 ►► unchecked — 01 min
- [x] 4.11 bool Türünün Sayısal Türe Dönüştürülmesi — 03 min
- [x] 4.12 ► Sayısal Türlerin bool Türüne Dönüştürülmesi — 02 min
- [x] 4.13 char Türünün Sayısal Türe Dönüştürülmesi | ASCII — 05 min
- [x] 4.14 ► Sayısal Türlerin char Türüne Dönüştürülmesi — 02 min
- [x] 4.15 Özet — 04 min

## 5. Operatörler (36)
- [x] 5.1 Operatör Nedir? — 04 min
- [x] 5.2 ► Operatör Okur Yazarlığı — 06 min
- [x] 5.3 Aritmetik Operatörler — 07 min
- [x] 5.4 ► Aritmetik Operatörler Geriye Dönüş Değeri — 07 min
- [x] 5.5 ► (int) * (double) = ? — 03 min
- [x] 5.6 ► (byte) * (int) = ? — 01 min
- [x] 5.7 ► (byte) * (byte) = ? (İstisna! – Mülakat!!!) — 02 min
- [x] 5.8 ► Matematiksel İşlemler(Öncelik Sırası) — 01 min
- [x] 5.9 Karşılaştırma Operatörleri — 02 min
- [x] 5.10 ► Karşılaştırma Operatörleri Geriye Dönüş Değeri — 02 min
- [x] 5.11 Mantıksal Operatörler — 07 min
- [x] 5.12 ► Mantıksal Operatörler Kullanım Mantığı(Solu Sağı bool olmalı) — 05 min
- [x] 5.13 ► Mantıksal Operatörler Geriye Dönüş Değeri — 08 min
- [x] 5.14 Arttırma Azaltma Operatörleri — 16 min
- [x] 5.15 Üzerine Ekleme Yığma Operatörleri — 05 min
- [x] 5.16 Metinsel İfadelerde Kullanılan Operatörler — 05 min
- [x] 5.17 Diğer Operatörler
- [x] 5.18 ► ! Operatörü — 06 min
- [x] 5.19 ► Ternary Operatörü — 13 min
- [x] 5.20 ►► Birden Fazla Condition Uygulamak — 03 min
- [x] 5.21 ►► Örnek 1 — 10 min
- [x] 5.22 ►► Örnek 2 — 05 min
- [x] 5.23 ► Atama(Assign) Operatörü — 02 min
- [x] 5.24 ► .(Member Access – üye Erişim) Operatörü — 04 min
- [x] 5.25 ► Cast Operatörü — 05 min
- [x] 5.26 ► sizeof Operatörü — 01 min
- [x] 5.27 ► typeof Operatörü — 03 min
- [x] 5.28 ► default Operatörü — 03 min
- [x] 5.29 ► is Operatörü — 04 min
- [x] 5.30 ► is null Operatörü — 04 min
- [x] 5.31 ► is not null Operatörü — 01 min
- [x] 5.32 ► as Operatörü — 10 min
- [x] 5.33 ► ?(Nullable) Operatörü — 06 min
- [x] 5.34 ► ??(Null-Coalescing) Operatörü — 03 min
- [x] 5.35 ► ??= Operatörü (Null-Coalescing Assignment) (C# 8.0) — 03 min
- [x] 5.36 Özet — 11 min

## 6. Akış Kontrol Mekanizmaları (48)
- [x] 6.1 Akış Kontrol Mekanizmaları Nedir? — 05 min
- [x] 6.2 Switch Case — 20 min
- [x] 6.3 ► when — 06 min
- [x] 6.4 ► goto — 09 min
- [x] 6.5 ► Switch Expressions (C# 8.0)
- [x] 6.6 ►► Switch Expression — 06 min
- [x] 6.7 ►►► Switch Expression when Şartı Uygulamak — 04 min
- [x] 6.8 ►► Tuple Patterns — 05 min
- [x] 6.9 ►►► Tuple Patterns when Şartı Uygulamak — 02 min
- [x] 6.10 ►► Property Patterns — 02 min
- [x] 6.11 ►►► Property Patterns when Şartı Uygulamak — 01 min
- [x] 6.12 ►► Positional Patterns — 03 min
- [x] 6.13 ►►► Positional Patterns when Şartı Uygulamak — 01 min
- [x] 6.14 if …. else Yapısı
- [x] 6.15 ► if Yapısı — 12 min
- [x] 6.16 ►► Kritik 1 — 03 min
- [x] 6.17 ►► Kritik 2 — 03 min
- [x] 6.18 ► If – Else Yapısı — 06 min
- [x] 6.19 ►► Kritik 1 — 03 min
- [x] 6.20 ►► Kritik 2 — 05 min
- [x] 6.21 ► If – Else If Yapısı — 07 min
- [x] 6.22 ►► Kritik — 08 min
- [x] 6.23 ► If – Else If – Else Yapısı — 02 min
- [x] 6.24 ► Scopesuz If Yapısı — 03 min
- [x] 6.25 ► Örnek Senaryolar
- [x] 6.26 ►► 1. Senaryo — 11 min
- [x] 6.27 ►► 2. Senaryo — 07 min
- [x] 6.28 ►► 3. Senaryo — 08 min
- [x] 6.29 ►► 4. Senaryo — 05 min
- [x] 6.30 ►► 5. Senaryo — 04 min
- [x] 6.31 Pattern Matching (C# 7.0)
- [x] 6.32 ► Type Pattern — 05 min
- [x] 6.33 ►► Kritik — 07 min
- [x] 6.34 ► Constant Pattern — 03 min
- [x] 6.35 ►► Kritik — 05 min
- [x] 6.36 ► Var Pattern — 02 min
- [x] 6.37 ►► Kritik 1 — 01 min
- [x] 6.38 ►► Kritik 2 — 02 min
- [x] 6.39 ►► Kritik 3 — 01 min
- [x] 6.40 ► Recursive Pattern — 05 min
- [x] 6.41 ► Type ve Var Pattern Üzerine Kritik — 01 min
- [x] 6.42 Pattern Matching (C# 9.0) — 01 min
- [x] 6.43 ► Simple Type Patterns — 03 min
- [x] 6.44 ► Relational Patterns — 02 min
- [x] 6.45 ►► Kritik — 01 min
- [x] 6.46 ► Logical Patterns — 01 min
- [x] 6.47 ► Not Patterns — 02 min
- [x] 6.48 Özet — 03 min

## 7. Hata Kontrol Mekanizmaları (19)
- [x] 7.1 Hata Kontrol Mekanizmaları Nedir? Ne Amaçla Kullanılır? — 04 min
- [x] 7.2 Hata Türleri
- [x] 7.3 ► Derleme/Syntax/Sözdizimi Hatası — 05 min
- [x] 7.4 ► Çalışma Zamanı(Run Time) Hatası — 12 min
- [x] 7.5 ► Çalışma Zamanı/Run-Time Hata Durumlarına Örnek Verelim
- [x] 7.6 ►► try – catch Mekanizması Teorik Anlatım — 11 min
- [x] 7.7 ►►► Pratikte try – catch Yapılanması — 10 min
- [x] 7.8 ►►►► Kritik — 07 min
- [x] 7.9 ►►► Hata Parametreleri — 11 min
- [x] 7.10 ►►►► Hata Türleri — 03 min
- [x] 7.11 ►►►► Exception Dışında Farklı Bir Tür İle Hata Yakalama — 08 min
- [x] 7.12 ►►► Birden Çok Catch Durumu — 10 min
- [x] 7.13 ►►► finally Bloğu — 04 min
- [x] 7.14 ►►► when Yapısı Ile Hata Filtreleme(C# 6.0) — 05 min
- [x] 7.15 ► Mantıksal Hatalar — 05 min
- [x] 7.16 ►► Örnek 1 — 01 min
- [x] 7.17 ►► Örnek 2 — 01 min
- [x] 7.18 ►► Örnek 3 — 01 min
- [x] 7.19 Özet — 03 min

## 8. Döngüler (36)
- [x] 8.1 Nedir Bu Döngüler? — 05 min
- [x] 8.2 ‘Hangi Döngü Nerede Kullanılır?’ Yanlış Bir Sorudur! Doğru Soru ‘Hangi Döngü Nereye Yakışır?’ — 05 min
- [x] 8.3 For Döngüsü — 18 min
- [x] 8.4 ► İnceleme 1 — 05 min
- [x] 8.5 ► İnceleme 2 — 05 min
- [x] 8.6 ► İnceleme 3 — 04 min
- [x] 8.7 ► Örnek 1 — 05 min
- [x] 8.8 ► Örnek 2 — 08 min
- [x] 8.9 ► Örnek 3 — 10 min
- [x] 8.10 ► Varyasyonları
- [x] 8.11 ►► 1. Varyasyon — 01 min
- [x] 8.12 ►► 2. Varyasyon — 01 min
- [x] 8.13 ►► 3. Varyasyon — 01 min
- [x] 8.14 ►► 4. Varyasyon — 01 min
- [x] 8.15 ►► 5. Varyasyon — 02 min
- [x] 8.16 ►► 6. Varyasyon — 01 min
- [x] 8.17 ►► 7. Varyasyon — 01 min
- [x] 8.18 ►► 8. Varyasyon — 02 min
- [x] 8.19 While Döngüsü — 03 min
- [x] 8.20 ► For İle Kıyaslama — 04 min
- [x] 8.21 ► İnceleme 1 — 02 min
- [x] 8.22 ► İnceleme 2 — 04 min
- [x] 8.23 ► İnceleme 3 — 04 min
- [x] 8.24 ► İnceleme 4 — 02 min
- [x] 8.25 ► İnceleme 5 — 04 min
- [x] 8.26 Do While Döngüsü — 06 min
- [x] 8.27 ► While İle Kıyaslama — 01 min
- [x] 8.28 Scopesuz Döngüler — 02 min
- [x] 8.29 Sonsuz Döngüler — 02 min
- [x] 8.30 ► For — 04 min
- [x] 8.31 ► While — 04 min
- [x] 8.32 ► Do While — 04 min
- [x] 8.33 İç İçe Döngüler — 03 min
- [x] 8.34 ► For — 07 min
- [x] 8.35 Foreach Bir Döngü mü? — 06 min
- [x] 8.36 Özet — 03 min

## 9. Konseptli Keywordler/Konseptsiz Keywordler? (5)
- [x] 9.1 Gelin Koda Bakış Açımızı Genişletelim — 05 min
- [x] 9.2 Keyword Nedir? Operatörden Farkı Nedir? — 07 min
- [x] 9.3 Konseptli Keywordler(While, If, switch, try catch) — 07 min
- [x] 9.4 Konseptsiz Keywordler(Break, Continue, Return, Goto) — 02 min
- [x] 9.5 Özet — 02 min

## 10. Yardımcı Manevra Komutları (13)
- [x] 10.1 Algoritmada Manevra Yapmamızı Sağlayan Komutlarda Neyin Nesi? — 06 min
- [x] 10.2 break — 13 min
- [x] 10.3 ► Örnek 1 — 05 min
- [x] 10.4 ► Örnek 2 — 03 min
- [x] 10.5 continue — 07 min
- [x] 10.6 ► Örnek 1 — 06 min
- [x] 10.7 ► Örnek 2 — 01 min
- [x] 10.8 return — 07 min
- [x] 10.9 ► Örnek — 03 min
- [x] 10.10 goto — 16 min
- [x] 10.11 Örnek — 03 min
- [x] 10.12 ► Kritik — 02 min
- [x] 10.13 Özet — 02 min

## 11. Ekstra Bilgi (2)
- [x] 11.1 Döngülerde Boş Scope Kullanmak İstemediğimiz Durumlarda ; (Noktalı Virgül) Operatörü İle Temiz Kod Yazımı — 04 min
- [x] 11.2 if Yapısında Boş Scope Kullanmak İstemediğimiz Durumlarda ; (Noktalı Virgül) Operatörü İle Temiz Kod Yazımı — 01 min

## 12. Diziler (Arrays) (54)
- [x] 12.1 Dizi Nedir? — 27 min
- [x] 12.2 Dizi Tanımlama — 24 min
- [x] 12.3 Tanımlanmış Diziye Değer Atama — 14 min
- [x] 12.4 Tanımlanmış Diziden Değer Okuma — 06 min
- [x] 12.5 Tanımlanmış Dizi İçerisinde Döngüyle Dönme — 09 min
- [x] 12.6 ► Kritik 1 — 06 min
- [x] 12.7 Dizilerin Sınırlılıkları ve Koleksiyon Yapılarının Doğuşu — 07 min
- [x] 12.8 Dizi Tanımlama Varyasyonları
- [x] 12.9 ► Varyasyon 1 — 02 min
- [x] 12.10 ► Varyasyon 2 — 02 min
- [x] 12.11 ► Varyasyon 3 — 01 min
- [x] 12.12 ► Varyasyon 4 — 02 min
- [x] 12.13 ► Varyasyon 5 — 03 min
- [x] 12.14 Array Sınıfı — 07 min
- [x] 12.15 ► Bir Dizinin Kendi Türünde Tanımlanmasıyla Array Türünde Tanımlanması Arasındaki Fark Nedir? — 04 min
- [x] 12.16 ► Array Türünden Dizilere Değer Atama/Okuma — 05 min
- [x] 12.17 ► Metotlar
- [x] 12.18 ►► Clear — 04 min
- [x] 12.19 ►► Copy — 07 min
- [x] 12.20 ►► IndexOf — 04 min
- [x] 12.21 ►► Reverse — 03 min
- [x] 12.22 ►► Sort — 02 min
- [x] 12.23 ► Özellikler
- [x] 12.24 ►► IsReadOnly — 03 min
- [x] 12.25 ►► IsFixedSize — 02 min
- [x] 12.26 ►► Length — 01 min
- [x] 12.27 ►► Rank — 02 min
- [x] 12.28 ►► CreateInstance Metodu İle Dizi Tanımlama — 03 min
- [x] 12.29 ►►► Çok Boyutlu Dizi Tanımlama — 02 min
- [x] 12.30 Ranges and Indices (C# 8.0) — 02 min
- [x] 12.31 ► System.Index — 05 min
- [x] 12.32 ►► İnceleme — 03 min
- [x] 12.33 ► System.Range — 06 min
- [x] 12.34 ►► İnceleme 1 — 07 min
- [x] 12.35 ►► İnceleme 2 — 04 min
- [x] 12.36 ► .. Operatörü — 02 min
- [x] 12.37 ►► İnceleme — 03 min
- [x] 12.38 ► ^ Operatörü — 02 min
- [x] 12.39 ►► İnceleme — 03 min
- [x] 12.40 Çok Boyutlu Diziler — 03 min
- [x] 12.41 ► Çok Boyutlu Dizi Tanımlama — 05 min
- [x] 12.42 ► Tanımlanmış Çok Boyutlu Diziye Değer Atama — 08 min
- [x] 12.43 ►► Çok Boyutlu Dizilerde Değer Atama Farklı Varyasyonu — 05 min
- [x] 12.44 ► Çok Boyutlu Dizilerden Değer Okuma — 01 min
- [x] 12.45 ► Dizinin Derecesini Öğrenme(Rank Özelliği) — 01 min
- [x] 12.46 ► Çok Boyutlu Dizilerin Eleman Sayısını Hesaplama — 01 min
- [x] 12.47 ► Çok Boyutlu Dizilerin Belirli Bir Derecesinin Eleman Sayısını Hesaplama — 01 min
- [x] 12.48 ► Çok Boyutlu Dizilerdeki Verileri İç İçe Döngülerle Ekrana Yazdırma — 03 min
- [x] 12.49 Düzensiz Diziler — 03 min
- [x] 12.50 ► Düzensiz Dizi Tanımlama — 05 min
- [x] 12.51 ► Değer Atama/Değer Okuma — 02 min
- [x] 12.52 ► Eleman Sayısını Öğrenme — 04 min
- [x] 12.53 ► Düzensiz Dizilerde İç İçe Döngülerle Çalışma — 03 min
- [x] 12.54 Özet — 05 min

## 13. String Tipi Analizi ve String Fonksiyonları (40)
- [x] 13.1 String Gerçeği — 06 min
- [x] 13.2 ► Null – Empty Durumları, Farkları — 16 min
- [x] 13.3 ► IsNullOrEmpty — 07 min
- [x] 13.4 ► IsNullOrWhiteSpace — 04 min
- [x] 13.5 String RAM(Heap) İlişkisi — 03 min
- [x] 13.6 String char Dizisidir! — 08 min
- [x] 13.7 Döngülerle String Metin İçerisinde Her Bir Karaktere Ulaşma — 05 min
- [x] 13.8 String İfadelerde “+” Operatörü — 05 min
- [x] 13.9 String Formatlandırma — 03 min
- [x] 13.10 ► + Operatörü İle Formatlandırma — 07 min
- [x] 13.11 ► String.Format — 06 min
- [x] 13.12 ► $(String Interpolation) (C# 6.0) — 09 min
- [x] 13.13 Escape(Kaçış) Karakterleri — 12 min
- [x] 13.14 @ (Verbatim Strings) Operatörü — 01 min
- [x] 13.15 ► 1. Kullanım — 02 min
- [x] 13.16 ► 2. Kullanım — 02 min
- [x] 13.17 String Interpolation İle Verbatim Strings Birlikteliği (C# 8.0) — 03 min
- [x] 13.18 String Fonksiyonlar — 02 min
- [x] 13.19 ► Contains — 02 min
- [x] 13.20 ► StartsWith — 01 min
- [x] 13.21 ► EndsWith — 01 min
- [x] 13.22 ► Equals — 01 min
- [x] 13.23 ► Compare — 07 min
- [x] 13.24 ► CompareTo — 02 min
- [x] 13.25 ► IndexOf — 04 min
- [x] 13.26 ► Insert — 04 min
- [x] 13.27 ► Remove — 03 min
- [x] 13.28 ► Replace — 02 min
- [ ] 13.29 ► Split — 04 min
- [ ] 13.30 ► Substring — 05 min
- [ ] 13.31 ► ToLower — 01 min
- [ ] 13.32 ► ToUpper — 01 min
- [ ] 13.33 ► Trim — 05 min
- [ ] 13.34 ► TrimEnd — 01 min
- [ ] 13.35 ► TrimStart — 01 min
- [ ] 13.36 Örnek Çalışmalar
- [ ] 13.37 ► Adımızın İlkten 3. Soyadımızın Sondan 5. Karakterini Getirelim — 07 min
- [ ] 13.38 ► Girilen Metnin İçerisinde Kaç Adet “n” Karakterinin Geçtiğini Hesaplayalım — 04 min
- [ ] 13.39 ► Girilen Metindeki Kelime Sayısını Hesaplayalım — 10 min
- [ ] 13.40 Özet — 05 min

## 14. Dizilerde Verisel Performans (13)
- [ ] 14.1 Dizilerde Verisel Performans Nedir? — 11 min
- [ ] 14.2 ► Pratiksel İnceleme — 06 min
- [ ] 14.3 ArraySegment Türü Nedir? Nasıl Kullanılır?
- [ ] 14.4 ► ArraySegment Nedir? — 04 min
- [ ] 14.5 ► ArraySegment İle Dizinin Belli Bir Alanını Referans Etmek — 09 min
- [ ] 14.6 ► ArraySegment Slicing(Dilimleme) Özelliği — 05 min
- [ ] 14.7 StringSegment Türü Nedir? Nasıl Kullanılır?
- [ ] 14.8 ► StringSegment Nedir? — 04 min
- [ ] 14.9 ► StringSegment İle Dizinin Belli Bir Alanını Referans Etmek — 07 min
- [ ] 14.10 ► StringBuilder Sınıfı — 06 min
- [ ] 14.11 Span, ReadOnlySpan, Memory ve ReadOnlyMemory Türleri Nedir? Nasıl Kullanılır? — 11 min
- [ ] 14.12 ► Pratiksel İnceleme — 07 min
- [ ] 14.13 Özet

## 15. Regular Expressions (Düzenli İfadeler) (12)
- [ ] 15.1 Regular Expressions(Düzenli İfadelerde) Neyin Nesi? — 12 min
- [ ] 15.2 Regular Expressions Operatörleri
- [ ] 15.3 ► ^ Operatörü, Regex Sınıfının Kullanımı — 07 min
- [ ] 15.4 ►  Operatörü — 10 min
- [ ] 15.5 ► + Operatörü — 06 min
- [ ] 15.6 ► | (veya) Operatörü — 02 min
- [ ] 15.7 ► {n} Operatörü — 03 min
- [ ] 15.8 ► ? Operatörü — 02 min
- [ ] 15.9 ► . Operatörü — 02 min
- [ ] 15.10 ► b – B Operatörleri — 04 min
- [ ] 15.11 ► [n] Operatörleri — 04 min
- [ ] 15.12 Match Sınıfı Özellikleri — 03 min

## 16. Koleksiyon Yapıları (7)
- [ ] 16.1 Koleksiyonlar Nelerdir? Diziler Varken Neden Koleksiyon Yapıları İnşa Edilmiştir? — 12 min
- [ ] 16.2 ArrayList Koleksiyonu — 03 min
- [ ] 16.3 ArrayList Koleksiyonu Tanımlama — 04 min
- [ ] 16.4 ArrayList Tanımlanmış Koleksiyona Değer Atama — 03 min
- [ ] 16.5 ArrayList Tanımlanmış Koleksiyondan Değer Okuma — 03 min
- [ ] 16.6 ArrayList Boxing – Unboxing Durumlarından Dolayı Sınırlılıklar — 10 min
- [ ] 16.7 ArrayList Collection Initializers(Koleksiyon İlklendirici) — 05 min

## 17. Foreach İterasyonu (3)
- [ ] 17.1 İterasyon Nedir? — 10 min
- [ ] 17.2 İterasyon ile Döngü Arasındaki Fark Nedir? — 07 min
- [ ] 17.3 Foreach İterasyonu Nasıl Kullanılır? — 07 min

## 18. Hazır Sınıflar & Fonksiyonlar (18)
- [ ] 18.1 C#’da Hazır Sınıflar ve Fonksiyonlar Nedir? — 04 min
- [ ] 18.2 Matematik(Math) Sınıfı – Fonksiyonları
- [ ] 18.3 ► Math Sınıfı – Abs Fonksiyonu — 03 min
- [ ] 18.4 ► Math Sınıfı – Ceiling Fonksiyonu — 02 min
- [ ] 18.5 ► Math Sınıfı – Floor Fonksiyonu — 02 min
- [ ] 18.6 ► Math Sınıfı – Round Fonksiyonu — 02 min
- [ ] 18.7 ► Math Sınıfı – Pow Fonksiyonu — 01 min
- [ ] 18.8 ► Math Sınıfı – Sqrt Fonksiyonu — 01 min
- [ ] 18.9 ► Math Sınıfı – Truncate Fonksiyonu — 01 min
- [ ] 18.10 Tarih(DateTime) Yapısı – Fonksiyonları | Özellikleri
- [ ] 18.11 ► DateTime – Now Özelliği — 01 min
- [ ] 18.12 ► DateTime – Today Özelliği — 01 min
- [ ] 18.13 ► DateTime – Compare Fonksiyonu — 03 min
- [ ] 18.14 ► DateTime – Tarihsel Zamana Saat, Gün, Ay, Yıl Ekleyerek Sonucu Hesaplamak — 03 min
- [ ] 18.15 ► TimeSpan Türü İle İki Tarih Farkının Karşılanması — 03 min
- [ ] 18.16 Random Sınıfı
- [ ] 18.17 ► Random Sınıfı – Next Fonksiyonu — 04 min
- [ ] 18.18 ► Random Sınıfı – NextDouble Fonksiyonu — 01 min

## 19. Metotlar (Functions) (22)
- [ ] 19.1 Metot Nedir? Bir Programcı Gözünden Ne İşe Yarar? — 15 min
- [ ] 19.2 İşlevsel Açıdan Metot Bize Ne Kazandırır? — 13 min
- [ ] 19.3 Metot Anatomisi Nasıldır? Gelin Metot İmzasını İnceleyelim — 19 min
- [ ] 19.4 İşlevine Göre Metot Türleri Nelerdir? — 06 min
- [ ] 19.5 ► Geriye Değer Döndürmeyen Parametre Almayan Metot Türü — 06 min
- [ ] 19.6 ► Geriye Değer Döndürmeyen Parametre Alan Metot Türü — 04 min
- [ ] 19.7 ► Geriye Değer Döndüren Parametre Almayan Metot Türü — 11 min
- [ ] 19.8 ► Geriye Değer Döndüren Parametre Alan Metot Türü — 05 min
- [ ] 19.9 Metodun Geriye Değer Döndürmesi Ne Demektir? — 25 min
- [ ] 19.10 Metotlarda Optional Parameters(İsteğe Bağlı Parametreler) — 16 min
- [ ] 19.11 ► Tanımlandığı Sınıf İçerisindeki Metotlar Tarafından Kullanımı — 11 min
- [ ] 19.12 ► Başka Sınıfta Tanımlanmış Metotların Erişimi – Referans ve Nesne İlişkisine Giriş — 21 min
- [ ] 19.13 ► Başka Sınıfta Tanımlanmış Metotların Erişimi — 11 min
- [ ] 19.14 Non Trailing Named Arguments Özelliği — 05 min
- [ ] 19.15 Metotlarda In Parametreleri (C# – In Keywordü) — 09 min
- [ ] 19.16 Local Functions(Metot İçerisinde Tanımlanabilir Yerel Metotlar) — 23 min
- [ ] 19.17 Static Local Functions(Static Metot İçerisinde Tanımlanabilir Yerel Metotlar) — 08 min
- [ ] 19.18 Metotlarda Overloading(Çoklu Yükleme) — 30 min
- [ ] 19.19 Recursive(Tekrarlamalı/Özyinelemeli) Metotlar — 45 min
- [ ] 19.20 ref Keyword’ü Nedir? Ne Amaçla Kullanılmaktadır? — 33 min
- [ ] 19.21 Ref Returns Özelliği Nedir? Ne Amaçla Kullanılmaktadır? — 16 min
- [ ] 19.22 C#’ta out Keyword’ü Nedir? Ne Amaçla Kullanılmaktadır?
