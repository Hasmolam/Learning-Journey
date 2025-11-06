using System;

public class Program
{
    public static void Main(string[] args)
    {
        #region Senaryo 1(break)
        //Kullanıcıdan 't' harfi girene kadar alınan sınırsız sayıda sayıyı toplayan ve sonucu ekrana yazdıran uygulamayı yazalım.
        // int toplam = 0;
        // while (true)
        // {
        //     System.Console.Write("Sayı: ");
        //     string sayi = Console.ReadLine();
        //     if (sayi == "t")
        //     {
        //         System.Console.WriteLine(toplam);
        //         break;
        //     }
        //     toplam += Convert.ToInt32(sayi);
        // }
        #endregion
        #region Senaryo 2(break)
        //Kullanıcıdan alınan sonsuz adet sayı değerlerinden 37'in katı girildiğinde sonlanan uygulamayı yazalım.
        // while (true)
        // {
        // System.Console.Write("Sayı: ");
        // int sayi = Convert.ToInt32(Console.ReadLine());
        // if (sayi % 37 == 0)
        // {
        // System.Console.WriteLine("Bu sayı 37'nin katıdır!");
        // break;
        // }
        // }
        #endregion
        #region Senaryo 3(continue)
        //Kullanıcının girdiği sonsuz adet sayıdan pozitif olanları çarpan ve 't'(enter) yapıldığında sonucu ekrana yazdıran kodu yazalım.
        // double product = 1;
        // while (true)
        // {
        //     System.Console.Write("Sayı: ");
        //     string sayi = Console.ReadLine();
        //     if (sayi == "t")
        //     {
        //         Console.WriteLine("Pozitif sayıların çarpımı: " + product);
        //         break;
        //     }
        //     if (Convert.ToInt32(sayi) <= 0)
        //     {
        //         continue;
        //     }
        //     product *= Convert.ToInt32(sayi);
        // }
        #endregion
        #region Senaryo 4(continue)
        //1 ile 1000 arasında 7'in katı olmayan sayıları ekrana yazdıralım
        // for(int i = 1;i <= 1000; i++)
        // {
        //     if (i % 7 == 0)
        //     {
        //         continue;
        //     }
        //     Console.WriteLine(i);
        // }
        #endregion
        #region Senaryo 5(return)
        //Kullanıcı 'c' tuşuna basana kadar sonsuz döngüde dönen uygulamayı yazınız.
        // while (true)
        // {
        //     if (Console.ReadKey().KeyChar == 'c')
        //     {

        //         return;
        //     }
        // }
        #endregion
        #region Senaryo 6(goto)
        //1'den 100'e kadar sayalım
        int i = 1;
    b:
        System.Console.WriteLine(i);
        i++;
        if (i == 101)
        {
            return;
        }
        goto b;
        #endregion
    }
}