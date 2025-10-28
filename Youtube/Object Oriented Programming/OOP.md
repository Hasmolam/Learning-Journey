# OOP

- Nesne tabanlı programlama bir programlama dili değil bir yaklaşımdır.(bkz. paradigma)
- Nesneler her şey olabilir. Aklına gelebilecek her şey nesne olabilir.
- Nesneler içerisinde veri tutabilecekleri alanlar barındırırlar. Biz bu alanlara field diyeceğiz.
- Fieldlarda ki değerleri işleyebilmesi için fonksiyonlar mevcuttur.(Metot, property vb.)
- Önce bir nesne modeli oluşturulur. Örneğin araba nesne modeli. Bu nesne modelinden nesneler oluşturulur. Örneğin Mercedes, Audi veya Porche.

# Referans Türlü Değerler

- Öncelikle RAM’in çalışma yapısını anlamamız gerekir. RAM iki bölüme ayrılır: **Stack** ve **Heap**.
- **Stack**: Değer türlü değişkenler ve referanslar burada tutulur.
- **Heap**: Sadece **nesneler (objects)** burada tutulur.
- Kod yazarken Stack’teki değişkenlere isimleri üzerinden erişebiliriz. Örneğin, `a` değişkeni 5 değerini tutuyorsa, `a` diyerek 5’e ulaşabiliriz.
- Peki Heap’teki nesnelere nasıl erişiriz?
    - Geliştiriciler Stack’e **doğrudan erişebilir**, ancak Heap’e doğrudan erişim yoktur.
    - Heap’teki nesnelere doğrudan erişemesek de, **Stack’teki referanslar aracılığıyla** erişebiliriz.
    - Yani Stack’te, Heap’teki nesneleri işaret eden referanslar tanımlarız. Stack’teki bu referansa eriştiğimizde dolaylı olarak Heap’teki nesneye de erişmiş oluruz.
- Nesnelere ve sınıflara referans türlü değerler denmesinin sebebi budur: **Stack’teki referanslar üzerinden Heap’teki nesnelere erişilir.**

# Sınıf (Class)

- OOP’de bir **nesne (object)** oluşturabilmek için önce o nesnenin **modelinin tanımlanması** gerekir.
- Bir nesnenin modelini/tanımını oluşturmak için **class yapısı** kullanılır.
- Class, bir tür **şablon** gibidir; nesneler bu şablona göre üretilir.
- Nesneler (object) bir class’tan türetilmiş **örnekler (instance)** olarak adlandırılır.
- Eğer bir referans değişkeni herhangi bir nesneyi işaret etmiyorsa, o referans **null** değerine sahiptir.

# Class Members

## Field

- Nesne içerisinde veri depoladığımız alanlardır.
- Class içerisindeki değişkenlerdir ve her türden olabilir.
- Field’lar türüne özgü **varsayılan değerler** alırlar.
- Eğer bir değişken **class içinde field olarak tanımlanıyorsa**, default değeri verilir.
- Eğer değişken **metot veya blok içinde tanımlanıyorsa**, default değer verilmez.

---

## Property

- Nesneye **özellik (property)** kazandırır.
- Esasında property, bir **metot** gibi çalışır; programatik/algoritmik kodları içerir.
- Fiziksel olarak metottan farkı: parametre almaz ve **get** ve **set** bloklarını içerir (C#).
- Property’nin değeri çağrıldığında **get** bloğu tetiklenir ve değer döner.
- İşlevsel olarak metottan farkı yoktur, fakat davranışsal olarak nesne üzerinde **okuma ve yazma** işlemlerinde kullanılır.
- Compile neticesinde get ve set blokları **get ve set metotları** olarak çalışır.
- **Amaç:** Field’lara **direkt erişimi engellemek**, kontrollü erişim sağlamak.
- Property yapıları, field’ların dışarıya kontrollü açılmasını ve kontrollü değer alınmasını sağlar.
- Bu işlev, OOP’de **Encapsulation (Kapsülleme/Sarmalama)** olarak adlandırılır:
    - Nesnedeki dataların kontrollü şekilde okunması ve değiştirilmesi.

---

## Property İmzaları

Property oluşturmanın farklı yolları vardır:

- Full Property
- Prop
- Auto Property Initializers
- Ref Readonly Returns
- Computed (Hesaplanmış) Properties
- Expression-Bodied Property (Read Only)
- Init-Only Properties ve Init Accessor

### Full Property

- En temel property yapısıdır.
- **Get** ve **Set** blokları tanımlanmalıdır.
- Property, temsil ettiği field türünden olmalıdır.
- Genellikle property adı, field adıyla aynı, ilk harfi büyük olacak şekilde yazılır (C#).
- Söz dizimi: `[erişim belirleyicisi] [geri dönüş değeri] [property adı] { get {} set {} }`
- **Set** bloğu yoksa: **Read Only**
- **Get** bloğu yoksa: **Write Only**

### Prop

- Field’a müdahale etmeden erişim sağlanmak istendiğinde kullanılır.
- Söz dizimi: `[erişim belirleyicisi] [geri dönüş değeri] [property adı] { get; set; }`
- Compile edildiğinde arka planda kendi field’ını oluşturur, ayrıca field tanımlamaya gerek yoktur.

### Auto Property Initializers (C# 6.0)

- Property’nin ilk değerini nesne oluşturulurken atayabiliriz.
- Read only property’lere hızlı değer atama imkânı sağlar.

### Ref Readonly Returns

- Class içindeki field’ı referansıyla döndürür ve aynı zamanda **read only** yapar.

### Computed (Hesaplanmış) Properties

- İçinde türetilmiş veya hesaplanmış değer taşıyan property’lerdir.

### Expression-Bodied Property

- Lambda Expression kullanarak property tanımlama söz dizimidir.
- Auto Property Initializers’a benzer kısmi bir yapıdır.

### Init-Only Properties (C# 9.0)

- Property yalnızca nesne oluşturulurken atanabilir.
- Run-time’da değişmemesi gereken değerler için güvenlik sağlar.
- Object Initializer desteği vardır; Auto Property Initializers bunu desteklemez.
- Atama sonrası property **read only** olur.

---

## Metot

- Nesne üzerinde field’lar veya dışarıdan gelen parametreler üzerinde işlemler yapan temel programatik yapılardır.

---

## Indexer

- Nesneye **index** ile erişim sağlar.
- Yapısı property ile aynıdır:
    
    `[erişim belirleyicisi] [geri dönüş değeri] this[parametreler] { get; set; }`
    

**Not**: Bir sınıf içerisinde tanımlanmış sınıflar sınıf elemanı değildir. (C#’da)

**Not**: This keyword’ünü kullanmak zorunda değiliz.(C#)

# Nesne Kavramı

## Nesne Nedir? Ne Amaçla Kullanılır?

- **Nesne (Object)**, bir class’ın **örneğine (instance)** verilen addır.
- Nesne, class ile tanımlanmış **özellikleri (field/property) ve davranışları (metot)** taşır.
- Amaç: Program içerisinde **veri ve işlevleri bir arada tutmak** ve OOP prensiplerini (Encapsulation, Abstraction, Inheritance, Polymorphism) uygulamak.
- Nesneler sayesinde aynı class’dan birden fazla bağımsız örnek üretilebilir ve her nesne kendi verisine sahip olur.

---

## new Operatörü ile Nesne Üretimi

- C#’ta nesne üretimi için **`new` operatörü** kullanılır.
- `new` operatörü, **Heap üzerinde nesne için yer ayırır** ve class’ın constructor’ını çalıştırır.
- Örnek:
    
    ```
    Car araba = new Car();
    ```
    
    - `Car` → class adı
    - `araba` → nesne referansı (Stack’te tutulur)
    - `new Car()` → Heap’te yeni nesneyi oluşturur ve referansı Stack’e atar.
- Böylece nesne üzerinden **field ve property’lere erişebilir**, **metotları çağırabiliriz**.

# Referans Nesne İlişkisi

## Referans Nedir?

- RAM’in **Stack** bölgesinde tanımlanan ve **Heap** bölgesindeki nesneleri işaret eden değişkenlerdir.
- Referanslar illa bir nesneyi işaret etmek zorunda değildir.
- Eğer bir referans herhangi bir nesneyi işaretlemiyorsa **null** değerini alır.

---

---

## Stack-Heap İlişkisi

- **Stack**, küçük ve kısa ömürlü veriler için hızlı erişim sağlar; değişkenler ve referanslar burada tutulur.
- **Heap**, nesnelerin tutulduğu ve referanslar aracılığıyla erişildiği bellek bölgesidir.
- Stack’teki referanslar sayesinde Heap’teki nesnelere **dolaylı olarak** erişebiliriz.
- Null olan (yani nesnesi olmayan) referanslar üzerinden herhangi bir member’ı çağırmaya çalıştığımızda **NullReferenceException** hatası oluşur.

---

## Referanssız Nesneler

- Bir nesne oluşturulduğu anda herhangi bir referansla işaretlenmezse Heap’e yerleştirilir, fakat bu nesneye bir daha erişemeyiz. Yani nesne ile aramızdaki tek iletişim oluşturulma anıdır.
- Referanssız nesneler, sistemde gereksiz yer kaplayacağı için bir süre sonra **Garbage Collector (Çöp Toplayıcı)** tarafından temizlenir.
- **Garbage Collector**, Heap’te referanssız nesneleri temizlemekten sorumludur ve bellek yönetimini otomatik olarak sağlar.

---

# Nesne Kopyalama Davranışları

- Nesne ve değer kopyalama **iki temel davranış** üzerinden gerçekleşir: **Shallow Copy** ve **Deep Copy**.

## Shallow Copy

- Var olan bir nesnenin **referansının kopyalanmasıdır**.
- Shallow copy sonucunda **nesne çoğaltılmaz**, sadece **birden fazla referans** tarafından işaretlenmiş olur.
- Yani nesne tek, ama onu işaret eden referans sayısı birden fazla olur.
- **Referans türü değişkenlerde** (class, array vb.) default kopyalama davranışı **shallow copy**’dir.

## Deep Copy

- Var olan bir nesne, **deep copy** ile kopyalandığında, **bellekte yeni bir nesne** oluşturulur.
- Yeni nesne, orijinal nesne ile **aynı özellik ve değerlere** sahiptir, fakat farklı bir nesnedir.
- **Değer türü değişkenlerde** (int, double, bool vb.) default kopyalama davranışı **deep copy**’dir.

# Encapsulation

## Encapsulation Nedir? Bir Veriyi Neden Kapsülleriz?

- **Encapsulation**, nesnelerimizdeki field’ların **kontrollü bir şekilde dışarıya açılması**dır.
- Başka bir deyişle, nesnelerimizi **yanlış veya kontrolsüz kullanım**dan korumak için field’lara doğrudan erişimi engellemektir.
- Field’lara **direkt erişilmesini istemeyiz**, bunun yerine kontrollü erişim sağlarız.

---

## Encapsulation Uygulama

- C#’da Encapsulation iki şekilde uygulanır:
    1. **Metot ile Encapsulation**
        - Field’lara erişim veya değer atama işlemleri metotlar aracılığıyla yapılır.
    2. **Property ile Encapsulation**
        - Field’lar **property’ler üzerinden okunur veya yazılır**, böylece kontrollü erişim sağlanır.