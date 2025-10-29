using System;

namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Kullanıcı tarafından girilen sayının aşağıdaki önergelere göre hesabını gerçekleştiren kodu geliştiriniz.

            Console.Write("Lütfen bir sayı giriniz: ");
            int sayi = int.Parse(Console.ReadLine());
            // sayi < 3                    => sayi * 5
            // sayi > 3 && sayi < 9        => sayi * 3
            // sayi >= 9 && sayi % 2 == 0  => sayi * 10
            // sayi % 2 == 1               => sayi
            // hiçbiri değilse             => -1
            int sonuc = sayi < 3 ? sayi * 5 : (sayi > 3 && sayi < 9 ? sayi * 3 : (sayi >= 9 && sayi % 2 == 0 ? sayi * 10 : (sayi % 2 == 1 ? sayi : -1)));
            Console.WriteLine("Sonuç: " + sonuc);
        }
    }
}