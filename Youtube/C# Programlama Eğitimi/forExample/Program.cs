using System;

public class ForExample
{
    public static void Main(String[] args)
    {
        #region Senaryo 1
        //Hilmi değerini 10 kere ekrana yazdıralım.
        // for (int i = 0; i < 10; i++)
        // {
        //     System.Console.WriteLine("Hilmi");    
        // }
        #endregion
        #region Senaryo 2
        //1'den 10'a kadar olan sayıları alt alta ekrana yazdıralım.
        // for (int i = 1; i < 11; i++)
        // {
        //     System.Console.WriteLine(i);
        // }
        #endregion
        #region Senaryo 3
        //1 ile 40 arasındaki çift sayıları toplayarak sonucu ekranda gösterelim
        // int sum = 0;
        // for(int i = 1; i <= 40; i++)
        // {
        //     if (i % 2 == 0)
        //     {
        //         sum += i;
        //     }
        // }
        // System.Console.WriteLine(sum);
        #endregion
        #region Senaryo 4
        //Klavyeden girilen sayının faktoriyelini bulan programı yapalım.
        double factorial = 1;
        System.Console.Write("Sayı: ");
        int number = Convert.ToInt32(Console.ReadLine());
        for (int i = number; i > 0; i--)
        {
            factorial *= i;
        }
        System.Console.WriteLine($"Sonuç: {factorial}");
        #endregion
    }
}