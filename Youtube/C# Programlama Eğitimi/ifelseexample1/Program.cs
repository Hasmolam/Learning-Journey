using System;

namespace akis_kontrol_semalari
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Senaryo 1 
            // Klavyeden iki ürünün fiyatı girildiğinde toplam fiyat 200 TL'den fazla ise, 2.üründen %25 indirim yaparak ödenecek tutarı gösteren uygulamayı yapalım.
            // Console.Write("1.ürünün fiyatı: ");
            // double urun1 = Convert.ToDouble(Console.ReadLine());
            // Console.Write("2.ürünün fiyatı: ");
            // double urun2 = Convert.ToDouble(Console.ReadLine());
            // double toplam = urun1 + urun2;
            // if (toplam > 200)
            // {
            //     urun2 *= 0.75;
            // }
            // toplam = urun1 + urun2;
            // Console.WriteLine(toplam);
            #endregion
            #region Senaryo 2
            //Belirlenen kullanıcı adı ve şifre doğru girildiğinde  "Giriş Başarılı", yanlış girildiğinde "Girdiğiniz kullanıcı adı veya şifre hatalı" mesajı veren Console uygulamasını yapalım.
            // string kullaniciAdi = "Hasan";
            // string sifre = "12345";
            // Console.Write("Kullanıcı Adı: ");
            // string inputKullaniciAdi = Console.ReadLine();
            // Console.Write("Şifre: ");
            // string inputSifre = Console.ReadLine();

            // if ile yapılmış versiyonu
            // if (kullaniciAdi == inputKullaniciAdi && inputSifre == sifre)
            // {
            //     Console.WriteLine("Giriş Başarılı!");
            // }
            // else
            // {
            //     Console.WriteLine("Girdiğiniz kullanıcı adı veya şifre hatalı");
            // }

            // switch ile yapılmış versiyonu
            // switch (inputKullaniciAdi)
            // {
            //     case "Hasan" when ("12345" == inputSifre):
            //         Console.WriteLine("Giriş Başarılı");
            //         break;
            //     default:
            //         Console.WriteLine("Girdiğiniz kullanıcı adı veya şifre hatalı");
            //         break;
            // }
            #endregion
            #region Senaryo 3
            // Kullanıcıdan alınan iki sayının ve yapılacak işlem türünün (toplama, çıkarma, çarpma, bölme) seçilmesiyle, sonucu hesaplayan programı yazalım.
            // Console.Write("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\nİşlem: ");
            // string islem = Console.ReadLine();
            // Console.Write("Sayı 1: ");
            // double sayi1 = Convert.ToDouble(Console.ReadLine());
            // Console.Write("Sayı 2: ");
            // double sayi2 = Convert.ToDouble(Console.ReadLine());

            // switch (islem)
            // {
            //     case "1":
            //         Console.WriteLine($"Sonuç: {sayi1 + sayi2}");
            //         break;
            //     case "2":
            //         Console.WriteLine($"Sonuç: {sayi1 - sayi2}");
            //         break;
            //     case "3":
            //         Console.WriteLine($"Sonuç: {sayi1 * sayi2}");
            //         break;
            //     case "4":
            //         if (sayi2 != 0)
            //         {
            //             Console.WriteLine($"Sonuç: {sayi1 / sayi2}");
            //         }
            //         else
            //         {
            //             Console.WriteLine("Hiçbir sayı 0'a bölünemez!");
            //         }
            //         break;
            //     default:
            //         Console.WriteLine("Geçersiz İşlem!");
            //         break;
            // }
            #endregion
            #region Senaryo 4
            // Girilen sayının değeri 10 değilse ekrana 'sayı yanlış' yazdıralım.
            // Console.Write("Sayı: ");
            // int sayi = Convert.ToInt32(Console.ReadLine());

            // if
            // if (sayi != 10)
            // {
            //     Console.WriteLine("Sayı yanlış");
            // }

            // ternary
            // Console.WriteLine(sayi != 10 ? "Sayı yanlış" : "");

            // switch expression
            // string sonuc = sayi switch
            // {
            //     10 => "",
            //     _ => "Sayı yanlış"
            // };
            // Console.WriteLine(sonuc);

            // switch
            // switch (sayi)
            // {
            //     case 10:
            //         break;
            //     default:
            //         Console.WriteLine("Sayı yanlış");
            //         break;
            // }

            #endregion
            #region Senaryo 5
            // Girilen bir sayının negatif ya da pozitif olduğunu gösteren uygulamayı yazalım.
            Console.Write("Sayı: ");
            int sayi = Convert.ToInt32(Console.ReadLine());
            string sonuc = (sayi > 0 ? "Pozitif" : (sayi == 0 ? "Nötr" : "Negatif"));
            Console.WriteLine(sonuc);  
            #endregion
        }
    }
}