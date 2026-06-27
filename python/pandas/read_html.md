Title: Pandas - read_html
Date: 2022-07-09 20:30
Category: Pandas
Tags: Python, Pandas, DataFrame, Veri Çerçevesi, read_html, Kütüphane, Modül
Author: Mustafa Halil

# read_html() Fonksiyonu Nedir? Nasıl Kullanılır?

**read_html()** fonksiyonu ile web sitelerinde ya da htm/html uzantılı dosyalardaki tabloları, çalışmalarınıza dahil edebilirsiniz. Öncelikle veri almak istediğimiz sayfanın içerisinde kaç adet tablo olduğunu bulalım.

```python
url_tablo = pd.read_html("https://tr.wikipedia.org/wiki/Van")
print(f"Sayfada bulunan toplam tablo sayısı: {len(url_tablo)}")
```

```python
Sayfada bulunan toplam tablo sayısı: 11
```

## match Parametresi
Hangi tabloyu kullanmak (içe aktarmak) istiyorsak öncelikle o tabloyu, tam olarak belirtmemiz/tanımlamamız gerekiyor. Bunu da **read_html()** fonksiyonunun **match (eşle)** parametresi ile yapmamız gerekir. Benim kullanmak istediğim tablonun içerisinde **Van il nüfus bilgileri** ibaresi bulunduğu için ben bu "<u>kelime grubunu</u>" **match** parametresine dahil ediyorum.

```python
url_tablo = pd.read_html("https://tr.wikipedia.org/wiki/Van", match="Van il nüfus bilgileri")
len(url_tablo)
```

```python
1
```

Bu demek oluyor ki, sayfa içeriğinde, **Van il nüfus bilgileri** ibaresi bulunan **1 adet eşleşmiş tablo** var, artık **url** değişkeni sayfadaki tek tabloyu temsil ediyor ve bu tabloya erişmek için ilk indis olan **0 sıfır**'ı kullanmamız gerekir.

```python
print(url_tablo[0])
```

**Van il nüfus bilgileri**

|     | Yıl      | Toplam    | Sıra | Fark | Şehir - Kır                         |
| --- | -------- | --------- | ---- | ---- | ----------------------------------- |
| 0   | 1965[11] | 266.840   | 48   | NaN  | %23 60.686206.154 %77               |
| 1   | 1970[12] | 325.763   | 43   | %22  | %27 88.227237.536 %73               |
| 2   | 1975[13] | 386.314   | 42   | %19  | %30 115.830270.484 %70              |
| 3   | 1980[14] | 468.646   | 39   | %21  | %33 156.852311.794 %67              |
| 4   | 1985[15] | 547.216   | 35   | %17  | %35 189.269357.947 %65              |
| 5   | 1990[16] | 637.433   | 32   | %16  | %41 258.967378.466 %59              |
| 6   | 2000[17] | 877.524   | 23   | %38  | %51 446.976430.548 %49              |
| 7   | 2007[18] | 979.671   | 19   | %12  | %52 511.678467.993 %48              |
| 8   | 2008[19] | 1.004.369 | 19   | %3   | %51 514.481489.888 %49              |
| 9   | 2009[20] | 1.022.310 | 19   | %2   | %52 527.525494.785 %48              |
| 10  | 2010[21] | 1.035.418 | 19   | %1   | %52 539.619495.799 %48              |
| 11  | 2011[22] | 1.022.532 | 19   | -%1  | %52 526.725495.807 %48              |
| 12  | 2012[23] | 1.051.975 | 19   | %3   | %52 548.717503.258 %48              |
| 13  | 2013[24] | 1.070.113 | 19   | %2   | Şehir ve kır ayrımı kaldırılmıştır. |
| 14  | 2014[25] | 1.085.542 | 19   | %1   | Şehir ve kır ayrımı kaldırılmıştır. |
| 15  | 2015[26] | 1.096.397 | 19   | %1   | Şehir ve kır ayrımı kaldırılmıştır. |
| 16  | 2016[26] | 1.100.190 | 19   | %0   | Şehir ve kır ayrımı kaldırılmıştır. |
| 17  | 2017[26] | 1.106.891 | 19   | %1   | Şehir ve kır ayrımı kaldırılmıştır. |
| 18  | 2018[26] | 1.123.784 | 19   | %2   | Şehir ve kır ayrımı kaldırılmıştır. |
| 19  | 2019[26] | 1.136.757 | 19   | %1   | Şehir ve kır ayrımı kaldırılmıştır. |
| 20  | 2020[26] | 1.149.342 | 19   | %1   | Şehir ve kır ayrımı kaldırılmıştır. |
| 21  | 2021[26] | 1.141.015 | 19   | -%1  | NaN                                 |

**len(url_tablo)** çıktısı **1**'den büyük, yani sayfada aranan kelime ile eşleşen 1'den fazla tablo olsaydı, o durumda **url_tablo[0]** kodundaki indis değerini değiştirerek istediğimiz tabloya erişebilecektik. Örneğin; **url_tablo[3]**  
Aşağıdaki kodu çalıştırırsanız, ilgili sayfada **ilçe** ibaresi geçen 5 adet tablo bulunduğunu göreceksiniz.

```python
url_tablo = pd.read_html("https://tr.wikipedia.org/wiki/Ankara", match="İlçe")
len(url_tablo)
```

Bu tablolardan **üçüncü** tabloya ulaşmak için **print(url_tablo[2])** komutunu çalıştırmanız gerekecektir (indis değeri 0'dan başladığı için 3 yerine 2 yazmalıyız).

