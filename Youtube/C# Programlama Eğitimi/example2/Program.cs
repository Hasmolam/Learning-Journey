using System;
using System.Reflection.Metadata;

namespace App
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Hava durumunu tutan string değişkeninin değerine göre aşağıdaki önergeleri uygulayan programı yazınız.
            // "Yağmurlu" => "Şemsiye almalısın"
            // "Güneşli" => "Bol bol d vitamini alman dileğiyle..."
            // "Kapalı" => "Yağmur yağabilir"
            string havaDurumu = "Kapalı";
            Console.WriteLine(havaDurumu == "Yağmurlu" ? "Şemsiye almalısın": ( havaDurumu == "Güneşli" ? "Bol bol d vitamini alman dileğiyle...": "Yağmur yağabilir"));
        }
    }
}