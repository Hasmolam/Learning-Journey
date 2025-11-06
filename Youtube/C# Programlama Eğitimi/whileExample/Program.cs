using System;
using System.Threading.Tasks;

namespace App
{
    public class Program
    {
        public static async Task Main(String[] args)
        {
            #region Senaryo 1
            //Ekrana 10 kere "Merhaba Dünya" yazdıran bir program yazalım.
            // int i = 0;
            // while (i < 10)
            // {
            //     System.Console.WriteLine("Merhaba Dünya");
            //     i++;
            // }
            #endregion
            #region Senaryo 2
            //Klavyeden girilen sayıdan geriye doğru 0'a kadar sayan bir sayaç hazırlayalım.
            // System.Console.Write("Sayı: ");
            // int i = Convert.ToInt32(Console.ReadLine());
            // while (i >= 0)
            // {
            //     System.Console.WriteLine(i);
            //     i--;
            // }
            #endregion
            #region Senaryo 3
            //0 ile 100 arasındaki tek sayıları toplayarak sonucu ekranda gösteren programı yapalım.
            // int i = 0;
            // int toplam = 0;
            // while (i < 100)
            // {
            //     if (i % 2 == 1)
            //     {
            //         toplam += i;
            //     }
            //     i++;
            // }    
            // System.Console.WriteLine(toplam);
            #endregion
            #region Senaryo 4
            //Klavyeden girilen sayılın faktoriyelini hesaplama
            // System.Console.Write("Sayı: ");
            // int i = Convert.ToInt32(Console.ReadLine());
            // int facto = 1;
            // while (i > 0)
            // {
            //     facto *= i;
            //     i--;
            // }
            // System.Console.WriteLine(facto);
            #endregion
            #region Senaryo 5
            //O anki tarihin saniye değeri 5'in katıysa eğer, tarihi ekranda gösteren uygulamayı yazalım.
            while (true)
            {
                if(DateTime.Now.Second % 5 == 0)
                {
                    System.Console.WriteLine(DateTime.Now.Second);
                    await Task.Delay(1000);
                }
            }
            #endregion
        }
    }
}