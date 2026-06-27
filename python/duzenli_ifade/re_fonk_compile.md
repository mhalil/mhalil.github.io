Title: Düzenli İfadeler - compile
Date: 2023-09-01 00:00
Modified: 2025-11-06 18:45
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Compile

# compile() Fonksiyonu

## Düzenli İfadelerin Derlenmesi

En başta da söylediğimiz gibi, düzenli ifadeler, karakter dizilerine göre biraz daha yavaş çalışırlar. Ancak düzenli ifadelerin işleyişini hızlandırmanın da bazı yolları vardır. Bu yollardan biri de `compile()` metodunu kullanmaktır. 

Elimizde birden fazla arama yapılacak metin (örneğin metin1, metin2, ...) ve eşleşme için kullanacağımız bir tek desen varsa, findall(), finditer() gibi metotları kullanmak istediğimizde, python her seferinde deseni kendi anlayacağı biçimde derleyip sonra metin içinde arayacaktır. Kaç farklı eşleşme / arama yapılacak yapı (metin) varsa işlem o kadar uzun sürecektir.

**compile** kelimesi İngilizcede **derlemek** anlamına gelir. İşte biz de bu `compile()` metodu yardımıyla **düzenli ifade desenlerimizi/kalıplarımızı kullanmadan önce derleyerek** daha hızlı çalışmalarını sağlayacağız. 

Küçük boyutlu projelerde `compile()` metodu pek hissedilir bir fark yaratmasa da özellikle büyük çaplı programlarda bu metodu kullanmak oldukça faydalı olacaktır.

Basit bir örnekle başlayalım:

```python
import re

liste = ["Python2.7", "Python3.2", "Python3.3", "Python3.4", "Java"]

derli = re.compile(r"[A-Za-z]+[0-9]\.[0-9]")

for eleman in liste:
    nesne = derli.search(eleman)
    if nesne:
        print(nesne.group())
```

**Çıktı**:

```python
Python2.7
Python3.2
Python3.3
Python3.4
```

Burada öncelikle düzenli ifade desenimizi/kalıbımızı derledik. Derleme işlemini nasıl yaptığımıza dikkat edin. 

Derlenecek düzenli ifade desenini `compile()` metodunda parantez içinde belirtiyoruz. 

Daha sonra `search()` metodunu kullanırken ise, `re.search()` demek yerine, `derli.search()` şeklinde bir ifade kullanıyoruz. Ayrıca dikkat ederseniz `derli.search()` kullanımında parantez içinde sadece eşleşecek karakter dizisini `(eleman)` kullandık. 

Eğer derleme işlemi yapmamış olsaydık, hem bu karakter dizisini, hem de düzenli ifade kalıbını yan yana kullanmamız gerekecektir `.search("[A-Za-z]+[0-9].[0-9], eleman)"`. Ama düzenli ifade desenimizi yukarıda derleme işlemi esnasında belirttiğimiz için, bu kalıbı ikinci kez yazmamıza gerek kalmadı. 

Ayrıca burada kullandığımız düzenli ifade desenine de dikkat edin. Nasıl bir şablon oturttuğumuzu anlamaya çalışın. Gördüğünüz gibi, liste öğelerinde bulunan `.` işaretini eşleştirmek için düzenli ifade kalıbı içinde `\.` ifadesini kullandık. Çünkü bildiğiniz gibi, tek başına `.` işaretinin `re` modülü açısından özel bir anlamı var. Dolayısıyla bu özel anlamdan kaçmak için `\` karakterini de kullanmamız gerekiyor.

## Detaylandıralım;

`re.compile()`fonksiyonu, düzenli ifade desenini derler ve bir`re.RegexObject` nesnesi döner. Bu nesne, derlenmiş düzenli ifadeyi temsil eder ve aynı deseni birden çok kez kullanmak için daha verimli bir yol sunar.

İşte `re.compile()` fonksiyonunun temel amacı ve avantajları:

**Performans Artışı:** 

Düzenli ifade desenleri büyük ve karmaşık olabilir. Bu desenleri her seferinde derleyip kullanmak yerine, `re.compile()` ile derlenmiş bir nesne oluşturabilir ve bu nesneyi kullanarak performans avantajı elde edebiliriz. Derleme işlemi, desenin daha hızlı eşleşmesine ve işlenmesine olanak tanır.

Örneğin:

```python
import re

pattern = re.compile(r'\b\w+\b')
result = pattern.findall("Python is powerful")
```

**Tekrar Kullanım Kolaylığı:** 

Derlenmiş bir düzenli ifade nesnesi oluşturduktan sonra, **aynı deseni farklı metinler üzerinde birden çok kez kullanabilirsiniz**. Bu, aynı deseni defalarca yazmak ve kodu çalıştırdıktan sonra her seferinde python tarafından derlemekten daha hızlı, temiz ve okunabilirlik sağlar.

Örneğin:

```python
import re

metin1 = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
bir dil denebilir. Ancak Python'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı
olması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi
haline gelmiştir. Ayrıca Google'ın da Python'a özel bir önem ve değer verdiğini, çok iyi derecede Python bilenlere
iş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın yaratıcısı Guido Van Rossum 
Google'de işe başladı...
Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında 
yayınlandı. 2008'de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan 
kodların Python 3.x'te çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, 
dilin son sürümü olan Python 2.7.x serisi versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi. 
Python 2.x geliştirilme desteğinin sona ermesinin ardından, Python dilinin 3.7.x ve sonraki sürümlerinin 
geliştirilmesi devam etmektedir."""


metin2 = """Python (C, C++, Perl, Ruby ve benzerleri gibi) bir programlama dilidir ve tıpkı öteki programlama dilleri gibi, önünüzde duran kara kutuya, yani bilgisayara hükmetmenizi sağlar.
Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. 
Dediğimiz gibi, Python bir programlama dilidir. Üstelik pek çok dile kıyasla öğrenmesi kolay bir programlama dilidir. Bu yüzden, eğer daha önce hiç programlama deneyiminiz olmamışsa, programlama maceranıza Python’la başlamayı tercih edebilirsiniz.
Eğer daha önce Python programlama dili ile ilgili araştırma yaptıysanız, şu anda piyasada iki farklı Python serisinin olduğu dikkatinizi çekmiş olmalı. 15.12.2023 tarihi itibariyle piyasada olan en yeni Python sürümleri Python 2.7.18 ve Python 3.12.1’dir.
Eğer bir Python sürümü 2 sayısı ile başlıyorsa (mesela 2.7.15), o sürüm Python 2.x serisine aittir. Yok eğer bir Python sürümü 3 sayısı ile başlıyorsa (mesela 3.7.0), o sürüm Python 3.x serisine aittir."""

metin3 = """Programlama dili, programcının bir bilgisayara ne yapmasını
istediğini anlatmasının standartlaştırılmış bir yoludur. Programlama
dilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,
verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin
yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla
programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,
C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama
dilleridir."""

desen = re.compile(r"\ba\w+\b")

sonuc1 = desen.findall(metin1)
sonuc2 = desen.findall(metin2)
sonuc3 = desen.findall(metin3)

print("Sonuc 1:", sonuc1)
print("Sonuc 2:", sonuc2)
print("Sonuc 3:", sonuc3)
```

**Çıktı**:

```python
Sonuc 1: ['aslında', 'ayrı', 'alternatif', 'ardından', 'ardından']
Sonuc 2: ['adlı', 'aldanarak', 'adını', 'aldığını', 'araştırma', 'anda', 'aittir', 'aittir']
Sonuc 3: ['anlatmasının', 'anlatmasını', 'ana']
```

`r"\ba\w+\b"` deseni ile küçük  `a` harfi ile başlayan kelimeleri 3 farklı metinde aratıp ekrana yazdırdık. Deseni bir kez oluşturduk ancak birden fazla metinde kullanabildik.



**Bayrakları Ayarlama:** 

`re.compile()` fonksiyonu, düzenli ifadenin derlenmesi sırasında bayrakları (flags) ayarlamanıza olanak tanır. (Bayraklar konusu [ilgili sayfada]({filename}re_bayraklar.md) detaylı olarak anlatılmaktadır.) Örneğin, `re.IGNORECASE` veya `re.UNICODE` bayraklarını belirleyerek deseni derleyebilirsiniz.

Örneğin:

```python
import re

desen = re.compile(r"\ba\w+\b", re.IGNORECASE) # re.IGNORECASE bayrağı, küçük/büyük harf fark etmeksizin tüm kelimeleri döndürsün anlamına gelir.

sonuc1 = desen.findall(metin1)
sonuc2 = desen.findall(metin2)
sonuc3 = desen.findall(metin3)

print("Sonuc 1:", sonuc1)
print("Sonuc 2:", sonuc2)
print("Sonuc 3:", sonuc3)
```

**Çıktı**:

```python
Sonuc 1: ['aslında', 'Ancak', 'ayrı', 'Ayrıca', 'ABC', 'alternatif', 'ardından', 'ardından']
Sonuc 2: ['adlı', 'aldanarak', 'adını', 'aldığını', 'araştırma', 'anda', 'aittir', 'aittir']
Sonuc 3: ['anlatmasının', 'anlatmasını', 'ana', 'Ada']
```

`r"\ba\w+\b", re.IGNORECASE` deseni ile küçük ya da büyük harf farketmeksizin `a` harfi ile başlayan kelimeleri 3 farklı metinde aratıp ekrana yazdırdık. Deseni bir kez oluşturduk ancak birden fazla metinde kullanabildik.

Bu avantajlar, `re.compile()` fonksiyonunu kullanmanın genellikle tercih edilen bir yöntem haline getirir. Ancak, küçük uygulamalarda veya tek seferlik kullanımlarda `re.compile()` kullanmak zorunlu değildir.
