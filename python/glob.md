Title: Python - glob
Date: 2024-05-11 18:10
Modified: 2024-05-21 22:05
Category: Cesitli
Tags: Python, glob, Kütüphane, Modül
Author: Mustafa Halil

# `glob()` Modülü / Kütüphanesi

`glob`, Python’da belirli bir dizin (klasör) içindeki dosyaları listelememizi sağlayan standart (gömülü) python kütüphanelerinden / modüllerinden biridir. Modülü kullanmak için `import glob` kodunu çalışmanıza eklemeniz yeterli. 

`glob` kütüphanesi, dosya yolu ve desen yönetimini basitleştirmek için oyunun kurallarını değiştiren güçlü bir araçtır. Joker karakter kalıpları ve özyineleme (recursive) özelliğinden (parametresinden) yararlanarak, dosyaları verimli bir şekilde bulup işleyebilir, zaman ve emekten tasarruf sağlayabiliriz.

Bu modülü kullanırken filtreleme yaparak, sadece istenilen dosyaların listelenmesini de sağlayabiliyoruz. Aşağıda, bu konuyla alakalı örnekler bulunmaktadır.

Bu modül Unix kabuğu tarafından kullanılan kurallara göre belirtilen bir kalıpla / desenle eşleşen tüm yol adlarını bulur, ancak sonuçlar rastgele sırayla döndürülür. Tilde (`~`) işareti genişletmesi yapılmaz, ancak `*, ?` ve `[]` ile ifade edilen karakter aralıkları doğru şekilde eşleştirilir. Bu işlem `os.scandir()` ve `fnmatch.fnmatch()` fonksiyonlarının birlikte kullanılmasıyla gerçekleştirilir, bir alt kabuğun çağrılmasıyla değil.

Nokta (`.`) ile başlayan dosyaların, `fnmatch.fnmatch()` veya `pathlib.Path.glob()`'un aksine, yalnızca nokta ile başlayan kalıplarla eşleştirilebileceğini unutmayın. (Tilde ve kabuk değişkeni genişletmesi için `os.path.expanduser()` ve `os.path.expandvars()` kullanın).

## glob Metodu (glob.glob)

`glob` kütüphanesinin `glob` metodunun kullanımı aşağıdaki şekildedir.

```glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)```

Dosya yolu adı (pathname) mutlak (`/usr/src/Python-1.5/Makefile` gibi) veya göreli (`../../Tools/*/*.gif` gibi) olabilir ve kabuk tarzı joker karakterler içerebilir. Bozuk sembolik bağlantılar sonuçlara dahil edilir (kabukta olduğu gibi). Sonuçların sıralanıp sıralanmayacağı dosya sistemine bağlıdır. Bu fonksiyonun çağrılması sırasında koşulları sağlayan bir dosya kaldırılır veya eklenirse, bu dosya için bir yol adının dahil edilip edilmeyeceği belirtilmez.

Bu kadar teknik anlatım yeterli biraz örnek yapalım.

`/home/mhalil/veriler/` klasörü içerisinde bulunan tüm dosyaları listelemek istediğimizi düşünelim. Bu durumda aşağıdaki kodu çalıştırmamız yeterli olacaktır.

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*")
print(dosyalar)
```

**Çıktı**, `liste` veri tipinde olacaktır;

```python
['/home/mhalil/veriler/Python_ProgramlamaDili.pdf', '/home/mhalil/veriler/360low1.jpg', '/home/mhalil/veriler/Ödeme Durumu.xlsx', '/home/mhalil/veriler/enfuse-handheld-hdri.jpg', '/home/mhalil/veriler/Liste.txt', '/home/mhalil/veriler/İlçe Kodları.xlsx', '/home/mhalil/veriler/artthings-enfuse-handheld.jpg', '/home/mhalil/veriler/MEB Herkes icin Python Programlama Dili.pdf', '/home/mhalil/veriler/13_Panorama_1280x640.jpg', '/home/mhalil/veriler/personel listesi.xlsx', '/home/mhalil/veriler/enfuse-handheld-hapala.jpg', '/home/mhalil/veriler/UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf', '/home/mhalil/veriler/Python for Excel.pdf', '/home/mhalil/veriler/symmetrical_garden_02_2k.hdr', '/home/mhalil/veriler/arakawa-enfuse-handheld.jpg', '/home/mhalil/veriler/Notlar.txt', "/home/mhalil/veriler/Python'da Fonksiyonlar.pdf"]
```

Bu çıktı pek te istediğimiz gibi bir sonuç vermedi. Her dosyayı ayrı bir satırda görmek için `for` döngüsü kullanabiliriz.

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*")

for dosya in dosyalar:
    print(dosya)
```

**Çıktı;**

```python
/home/mhalil/veriler/Python_ProgramlamaDili.pdf
/home/mhalil/veriler/360low1.jpg
/home/mhalil/veriler/Ödeme Durumu.xlsx
/home/mhalil/veriler/enfuse-handheld-hdri.jpg
/home/mhalil/veriler/Liste.txt
/home/mhalil/veriler/İlçe Kodları.xlsx
/home/mhalil/veriler/artthings-enfuse-handheld.jpg
/home/mhalil/veriler/MEB Herkes icin Python Programlama Dili.pdf
/home/mhalil/veriler/13_Panorama_1280x640.jpg
/home/mhalil/veriler/personel listesi.xlsx
/home/mhalil/veriler/enfuse-handheld-hapala.jpg
/home/mhalil/veriler/UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
/home/mhalil/veriler/Python for Excel.pdf
/home/mhalil/veriler/symmetrical_garden_02_2k.hdr
/home/mhalil/veriler/arakawa-enfuse-handheld.jpg
/home/mhalil/veriler/Notlar.txt
/home/mhalil/veriler/Python'da Fonksiyonlar.pdf
```

Eğer dosyayolunu değil sadece dosya adlarını listelemek istersek, Karakter Dizisi Metotlarından olan `split()` ya da `rsplit()` metotlarını kullanabiliriz.

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*")

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1]) # Windows işletim sistemlerinde "/" yerine "\" kullanabilirsiniz.
```

Bu kodun çıktısı aşağıda görüldüğü gibi sadece dosya isimleri olacaktır.

**Çıktı;**

```python
Python_ProgramlamaDili.pdf
360low1.jpg
Ödeme Durumu.xlsx
enfuse-handheld-hdri.jpg
Liste.txt
İlçe Kodları.xlsx
artthings-enfuse-handheld.jpg
MEB Herkes icin Python Programlama Dili.pdf
13_Panorama_1280x640.jpg
personel listesi.xlsx
enfuse-handheld-hapala.jpg
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
Python for Excel.pdf
symmetrical_garden_02_2k.hdr
arakawa-enfuse-handheld.jpg
Notlar.txt
Python'da Fonksiyonlar.pdf
```

Gördüğünüz gibi sonuç alfabetik değil. Eğer dosya isimlerini alfabetik sıralamak istersek, `dosyalar` listesini `sort()` metodu ile alfabetik sıraya dizebiliriz.
Şunu da unutmamak gerekir ki, Büyükharf ve küçükharf ile başlayan kelimeler kendi içleinde alfabetik olarak sıralanır. İsterseniz sıralama işleminden önce dosya isimlerinin tamamını, `lower()` , `upper()` ya da  `title()` fonksiyonları yardımı ile aynı formata getirebilirsiniz. Sıralama işleminde bilmeniz gereken önemli noktalardan biri de, Türkçe karakterler ile başlayan isimlerin, sıralamanınen sonunda yer alacağıdır. Bunun sebebi, `lower()` , `upper()` ya da  `title()` fonksiyonlarının Türkçe karakterleri doğru şekilde tanımıyor olması diye düşünüyorum.

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
13_Panorama_1280x640.jpg
360low1.jpg
Liste.txt
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
personel listesi.xlsx
Python for Excel.pdf
Python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
symmetrical_garden_02_2k.hdr
Ödeme Durumu.xlsx
İlçe Kodları.xlsx
```

### Filtreleme

Sıra geldi filtreleme işlemine. Yani belirli klasör içerisindeki tüm dosyaları değil de sadece belli uzantıya sahip ya da belirli karakter(ler) içeren veyahut belli karakter (harf / sayı) ile başlayan dosyaları listelemek isteyelim. Örneğin `/home/mhalil/veriler/` klasörü içerisinde bulunan `.pdf` uzantılı dosyaları listeleyelim. Bunun için dosya sonuna (`.pdf` ibaresinden önce) `*` özel karakterini eklemeliyiz. Yani `*.pdf` ifadesini kullanmalıyız. Bunun anlamı; dosya adı ne olursa olsun, uzantısı `pdf` olsun yeterli demektir. Bir başka ifadeyle tüm pdf dosyaları demek oluyor.

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*.pdf")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
MEB Herkes icin Python Programlama Dili.pdf
Python for Excel.pdf
Python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
```

Şimdi `P` harfi ile başlayan dosyaları listelemek isteyelim. Bunun için `P*);

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/P*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Python for Excel.pdf
Python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
```

Bu çıkıda bir şeyi fark etmiş olmalısınız. `P` ile başlayan dosya isimleri yazılırken `personel listesi.xlsx` dosyası yazılmadı. Bunun sebebi, `personel listesi.xlsx` dosyasının büyük P ile başlamıyor olması. Yani yazılan karakterler büyük / küçük harfe karşı duyarlı. eğer `P*` yerine `[Pp*]` yazmış olsaydık nasıl bir çıktı elde edrdik, inceleyelim.

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[Pp]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

Çıktı;

```python
Python for Excel.pdf
Python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
personel listesi.xlsx
```

Görüldüğü gibi artık `personel listesi.xlsx` dosyası listeleniyor. 

### Alt Klasörlerdeki Dosyaları Listelemek

Yukarıda kullandığımız kodlar ile sadece belirtilen klasör içerisindeki dosya ve klasöreri listeledik. Gelin şimdi içiçe klasörlerde bulunan dosyaları listeleyelim.

Elimizde aşağıdaki şekilde bir klasör ve dosya yapısı olduğunu düşünelim;

```python
Liste.txt
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
Ödeme Durumu.xlsx
İlçe Kodları.xlsx
Okunacaklar
|-- MEB Herkes icin Python Programlama Dili.pdf
|-- Notlar.txt
|-- Python for Excel.pdf
|-- Python_ProgramlamaDili.pdf
|-- UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
|-- python'da Fonksiyonlar.pdf
Resimler
|-- 13_Panorama_1280x640.jpg
|-- 360low1.jpg
|-- arakawa-enfuse-handheld.jpg
|-- artthings-enfuse-handheld.jpg
|-- enfuse-handheld-hapala.jpg
|-- enfuse-handheld-hdri.jpg
```

`veriler` isimli klasörde 5 dosya ve 2 klasör (Okunacaklar ve Resimler) bulunuyor. Klasörlerin içerisinde de farklı isim ve uzantılara sahip dosyalar mevcut.

Öncelikle yukarıdaki temel kodu kullanarak çıktı alalım.

**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
Okunacaklar
Resimler
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
Ödeme Durumu.xlsx
İlçe Kodları.xlsx
```

Çıktıda, mevcut `/home/mhalil/veriler/` klasöründe bulunan dosya ve klasör isimleri görüyoruz. Alt klasörlere ait dosya isimleri bulunmuyor.

Alt Klasördeki dosyaları görmek için `*/*` ifadesini kullanmalıyız. `*/` ifadesi, tüm klasörleri temsil ediyor. `Okunacaklar/` yazsaydık sadece **Okunacaklar** klasörünü belirtmiş olacaktık.
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*/*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
Python for Excel.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
python'da Fonksiyonlar.pdf
13_Panorama_1280x640.jpg
360low1.jpg
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
```

Çıktıda hem **Okunacaklar** hemde **Resimler** klasörlerinin içerisinde bulunan dosyaları listelemiş olduk. Bu kez de **veriler** klasöründeki dosyaları liste dışı bırakmış olduk.

Mevcut klasör içerisindeki dosyalar ile birlikte tüm alt klasördeki dosyaları listelemek istersek `**/*` ifadesi ile birlikte `recursive = True` parametresini de kullanmak zorundayız. `recursive = True` argümanının eklenmesi, arama terimimizin tam olarak hangi klasörde olacağından emin olmadığımız durumda çok yararlı olabilir. `recursive` parametresinin belirtilmemesi veya `False` olarak ayarlanması durumunda, yalnızca klasörde arama yapılır.

Aşağıdaki kodu ve çıktıyı inceleyin.

**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/**/*", recursive=True)
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
Okunacaklar
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
Python for Excel.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
python'da Fonksiyonlar.pdf
Resimler
13_Panorama_1280x640.jpg
360low1.jpg
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
Ödeme Durumu.xlsx
İlçe Kodları.xlsx
```

Görüldüğü üzere hem mevcut klasördeki hem de alt klasörlerdeki dosya ve klasörler listelenmiş oldu.

Gelin şimdi özel sembolleri inceleyelim.

## iglob Metodu (glob.iglob)

Çok sayıda dizin içerisinde arama yapmak, uzun zaman alabilir ve çok fazla bellek kullanabilir. Bunun için bir çözüm `iglob` kullanmaktır.

`iglob`'un `glob`'dan farkı, "`glob` ile aynı değerleri aynı anda depolamadan veren (`yields`)" bir yineleyici (iterator) döndürmesidir. Bu, `glob`'a kıyasla daha iyi performans / verim sağlar.

Bir dizindeki belirli bir desenle / kalıpla eşleşen tüm dosyaları bulmak için `glob` kullanımını gösterdik. Dosyalar daha sonra daha fazla analiz için kullanılmak üzere tek bir veri çerçevesi halinde birleştirildi.

Ayrıca, verilen bir dizeyi içeren dosyalar için birçok dizini özyinelemeli olarak aramak için `iglob` kullanımını da tartıştık.

`iglob` metodu, bir `generator nesnesi` döndürür. sonuçları ekrana yazdırmak için `next` kullanılabilir.

Kod;

```python
import glob

dosyalar = glob.iglob("/home/mhalil/veriler/**/*.*", recursive=True)

for _ in range(5):
    print(next(dosyalar))
```

Çıktı;

```python
/home/mhalil/veriler/Ödeme Durumu.xlsx
/home/mhalil/veriler/Liste.txt
/home/mhalil/veriler/personel listesi.xlsx
/home/mhalil/veriler/İlçe Kodları.xlsx
/home/mhalil/veriler/symmetrical_garden_02_2k.hdr
```

### Özel Semboller

Eğer **Düzenli İfadeler (Regular Expressions - Regex)** konusuna aşina iseniz, zaten bu konuyu biliyorsunuz diyebiliriz.

glob kütüphanesini kullanarak dosya listelerken bize esneklik katan `*, ?, []` ve `[!]` özel sembollerin / karakterlerinin ne işe yaradığını bir tablo ile açıklayalım.

| Özel Semboller | Anlamı                                                         | Örnek                                                              |
| -------------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| `*`            | Herşeyi (sıfır veya daha çok karakteri) temsil eder            | `*.pdf` : belirtilen dosya yolundaki tüm **PDF** uzantılı dosyalar |
| `?`            | herhangi BİR adet karakteri temsil eder                        | `?????` : 5 karekter uzunluğuna sahip dosyalar                     |
| `[]`           | Köşeli parentez içindeki HERHANGİ bir karekteri BULUNDURAN     | `[RPp]*` : R, P veya p ile başlayan dosyalar                       |
| `[!]`          | Köşeli parentez içindeki HERHANGİ bir karekterle BULUNDURMAYAN | `[!ABC]*` : A, B ve C ile başlamayan dosyalar                      |

Birebir eşleşme için meta karakterleri parantez içine alın. Örneğin, `'[?]'` yazımı, `'?'` karakteriyle eşleşir.

Özel sembolere ait bir kaç örnek kod yazalım.

**NOT: İlk 11 Örnekte dosya ve klasör yapısı aşağıdaki gibidir;**

```python
/home/mhalil/veriler/Python_ProgramlamaDili.pdf
/home/mhalil/veriler/360low1.jpg
/home/mhalil/veriler/Ödeme Durumu.xlsx
/home/mhalil/veriler/enfuse-handheld-hdri.jpg
/home/mhalil/veriler/Liste.txt
/home/mhalil/veriler/İlçe Kodları.xlsx
/home/mhalil/veriler/artthings-enfuse-handheld.jpg
/home/mhalil/veriler/MEB Herkes icin Python Programlama Dili.pdf
/home/mhalil/veriler/13_Panorama_1280x640.jpg
/home/mhalil/veriler/personel listesi.xlsx
/home/mhalil/veriler/enfuse-handheld-hapala.jpg
/home/mhalil/veriler/UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
/home/mhalil/veriler/Python for Excel.pdf
/home/mhalil/veriler/symmetrical_garden_02_2k.hdr
/home/mhalil/veriler/arakawa-enfuse-handheld.jpg
/home/mhalil/veriler/Notlar.txt
/home/mhalil/veriler/Python'da Fonksiyonlar.pdf
```

#### Örnek 1:

İÇİNDE sayı BULUNAN dosyaları listeleyelim. `*[0-9]*`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*[0-9]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
13_Panorama_1280x640.jpg
360low1.jpg
symmetrical_garden_02_2k.hdr
```

#### Örnek 2:

Sayı ile BAŞLAYAN dosya isimlerini listeleyelim. `[0-9]*`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[0-9]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
13_Panorama_1280x640.jpg
360low1.jpg
```

#### Örnek 3:

Büyük harf ile BAŞLAYAN dosyaları listeleyelim. `[A-Z]*`
**Önemli:** `[A-Z]` ifadesi, Türkçe karakterleri kapsamaz. Yani `Ü Ğ İ Ş Ç Ö` harfleri `[A-Z]` ifadesinin içinde yoktur.
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[A-Z]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
Python for Excel.pdf
Python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
```

Çıktıyı incelerseniz, **Ödeme Durumu.xlsx** ve **İlçe Kodları.xlsx** dosya isimlerinin, Büyükharfle başlamış olmasına rağmen çıktıda yer almadığını göreceksiniz. Bunların da görüntülenmesini sağlamak için bu karakterleri köşeli parantez içine eklemeliyiz. Kodumuş aşağıdaki şekilde olmalı: 

`dosyalar = glob.glob("/home/mhalil/veriler/[A-ZÜĞİŞÇÖ]*")`

#### Örnek 4:

Büyük harf ile BAŞLAYAN ancak baş harfi `A` ile `N` harfleri ARASINDA olan dosyaları listeleyelim. `[A-N]*`

**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[A-N]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
```

#### Örnek 5:

Küçük harf ile BAŞLAYAN dosyaları listeleyelim. `[a-z]*`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[a-z]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
```

#### Örnek 6:

Hem Büyük hemde Küçük harf ile BAŞLAYAN (sayı ya da özel simge ile başlamayan) dosyaları listeleyelim. `[A-Za-z]*`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[A-Za-z]*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
Python for Excel.pdf
Python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
```

#### Örnek 7:

 `JPG` uzantılı dosyaları listeleyelim. `*.jpg`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*.jpg")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
13_Panorama_1280x640.jpg
360low1.jpg
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
```

#### Örnek 8:

Sayı ile BAŞLAMAYAN `JPG` dosyaları listeleyelim. `[!0-9]*.jpg`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/[!0-9]*.jpg")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
```

#### Örnek 9:

 İÇİNDE `en` ibaresi bulunan dosyaları listeleyelim. `*en*`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/*en*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
symmetrical_garden_02_2k.hdr
```

#### Örnek 10:

Dosya uzantısı dahil TOPLAM 11 KARAKTER uzunluğundaki dosyaları listeleyelim. `???????????`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/???????????")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
360low1.jpg
```

#### Örnek 11:

Elimizde aşağıdaki gibi dosya isimleri olduğunu düşünelim.

```python
Python for Excel.pdf
python'da Fonksiyonlar.pdf
Python_ProgramlamaDili.pdf
```

Bu dosyaların tümünü `?` özel sembolünü kullanarak tek seferde listelemek için aşağıdaki kodu kullanabiliriz. `?ython*`

**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/?ython*")
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Python for Excel.pdf
Python_ProgramlamaDili.pdf
python'da Fonksiyonlar.pdf
```

Gördüğünüz gibi dosyaların baş harfi ne olursa olsun fark etmiyor, 2. harften itibaren 6. harfe kadar `ython` ibaresinin olması şartı sağlanan dosyalar listeleniyor.

**NOT: Aşağıdaki örneklerde dosya ve klasör yapısı şu şekildedir;**

```python
Liste.txt
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
Ödeme Durumu.xlsx
İlçe Kodları.xlsx
Okunacaklar
|- MEB Herkes icin Python Programlama Dili.pdf
|- Notlar.txt
|- Python for Excel.pdf
|- Python_ProgramlamaDili.pdf
|- UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
|- python'da Fonksiyonlar.pdf
Resimler
|- 13_Panorama_1280x640.jpg
|- 360low1.jpg
|- arakawa-enfuse-handheld.jpg
|- artthings-enfuse-handheld.jpg
|- enfuse-handheld-hapala.jpg
|- enfuse-handheld-hdri.jpg
```

#### Örnek 12:

`/home/mhalil/veriler/` klasörü ve alt klasörlerinde başharfi büyük veya küçük `a` ve `n` ile başlayan dosyaları listeleyelim. `**/[a-nA-N]*", recursive=True`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/**/[a-nA-N]*", recursive=True)
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
```

#### Örnek 13:

`/home/mhalil/veriler/` klasörü ve alt klasörlerinde `txt` uzantılı dosyaları listeleyelim. `**/*.txt", recursive=True`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/**/*.txt", recursive=True)
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
Notlar.txt
```

#### Örnek 14:

`/home/mhalil/veriler/` klasörü ve alt klasörlerinde küçük harfle başlayan dosyaları listeleyelim. `**/[a-z]*", recursive=True`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/**/[a-z]*", recursive=True)
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
python'da Fonksiyonlar.pdf
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
```

#### Örnek 15:

`/home/mhalil/veriler/` klasörü ve alt klasörlerinde içinde sayı bulunan dosyaları listeleyelim. `**/*[0-9]*", recursive=True`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/**/*[0-9]*", recursive=True)
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
13_Panorama_1280x640.jpg
360low1.jpg
symmetrical_garden_02_2k.hdr
```

#### Örnek 16:

`/home/mhalil/veriler/` klasörü ve alt klasörlerinde sadece dosyaları listeleyelim. Klasör isimlerinin (ör. `Okunacaklar` ve `Resimler`) listelenmesini istemeyelim. `**/*.*", recursive=True`
**Kod;**

```python
import glob

dosyalar = glob.glob("/home/mhalil/veriler/**/*.*", recursive=True)
dosyalar.sort()

for dosya in dosyalar:
    print(dosya.rsplit("/",1)[1])
```

**Çıktı;**

```python
Liste.txt
MEB Herkes icin Python Programlama Dili.pdf
Notlar.txt
Python for Excel.pdf
Python_ProgramlamaDili.pdf
UYGULAMALARLA-TEMEL-SEVIYE-PYTHON.pdf
python'da Fonksiyonlar.pdf
13_Panorama_1280x640.jpg
360low1.jpg
arakawa-enfuse-handheld.jpg
artthings-enfuse-handheld.jpg
enfuse-handheld-hapala.jpg
enfuse-handheld-hdri.jpg
personel listesi.xlsx
symmetrical_garden_02_2k.hdr
Ödeme Durumu.xlsx
İlçe Kodları.xlsx
```

### Kaynaklar;

* [Python Glob Modülü Resmi Sayfası](https://docs.python.org/tr/3.11/library/glob.html#module-glob)
* [Bayram Adali - Programcı Kafa](https://bayramadali.wordpress.com/python-glob-modulu/)
* [Python'a Giriş Youtube Kanalı](https://www.youtube.com/watch?v=mxqrzijYF1k)
