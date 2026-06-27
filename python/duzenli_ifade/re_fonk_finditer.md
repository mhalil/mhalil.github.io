Title: Düzenli İfadeler - finditer
Date: 2023-09-01 00:00
Modified: 2025-11-02 12:40
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Finditer

# finditer() Fonksiyonu

Belirtilen desenlerin tamamını, karakter dizileri içerisinde `finditer()` metodu ile bulabiliriz ancak bu metot, liste döndürmez, **iterable bir nesne döndürür**.  İterable ne demek derseniz, "*bir döngü vasıtası ile üzerinde gezilebilen elemanların oluşturduğu bir nesnedir*" diyebiliriz.

Özellikle Uzun metinlerde aranan desenin bulunması için bu metot kullanılabilir, böylece boşuna tekrar bir liste oluşturmaya gerek kalınmaz. Bulunan değerler **for** döngüsü ile doğrudan işlenebilir (yazdırılabilir, veri tabanına eklenebilir, ...vb)

`finditer()` fonksiyonunu doğrudan ekrana yazdırmak istersek, nasıl bir sonuç elde ederiz, inceleyelim.

```python
metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
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

print(re.finditer("Python", metin))
```

**Çıktı**:

```python
<callable_iterator object at 0x763487fb4a00>
```

Görüldüğü gibi yukarıdaki kod ile metin içinde "Python" ifadesini arattık ancak çıktı, hiç te umduğumuz gibi çıkmadı. Peki Çıktı bize ne söylüyor? Çıktı bir iterable nesne elde ettiğimizi, bu döngüsel nesne ile işlem yapılabileceğini söylemiş oluyor.

## span() Metodu

Örneğin, **metin** değişkeni içerisinde **Python** ifadesinin (deseninin) hangi konumda olduğunu (aranan desenin başlangıç ve bitiş değerlerini) bulmaya çalışalım.

```python
for i in re.finditer("Python", metin):
    print(i.span())
```

**Çıktı**:

```python
(17, 23)
(77, 83)
(128, 134)
(370, 376)
(430, 436)
(522, 528)
(586, 592)
(668, 674)
(733, 739)
(794, 800)
(826, 832)
(885, 891)
(955, 961)
(1046, 1052)
(1106, 1112)
```

## group() Metodu

**metin** içindeki sayısal değerleri bulup ekrana yazdıralım. Bu kez önce deseni bir değişken (**desen**) içerisinde tanımlayalım. Ardından `finditer()` fonksiyonunu başka bir değişkene (**eslesenler**) atayalım, döngüyü bu değişken ile sağlayalım;

```python
desen = r"\d{4}"    # 4 basamaklı sayısal değerleri temsil eder.
eslesenler = re.finditer(desen, metin)

for eslesen in eslesenler:
    print(eslesen.group())
```

**Çıktı**:

```python
1990
1980
2
0
2000
2008
3
0
2
3
2
2
7
1
2020
2
3
7
```

Sadece **yıl bilgisini** bulup yazdıralım;

```python
desen = r"\d{4}"
eslesenler = re.finditer(desen, metin)

for eslesen in eslesenler:
    print(eslesen.group())
```

Çıktı:

```python
1990
1980
2000
2008
2020
```

Sanırım bu bölüm için bu kadar örnek yeterli olacaktır.
