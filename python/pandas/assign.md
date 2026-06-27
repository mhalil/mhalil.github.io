Title: Pandas - assign Metodu
Date: 2025-11-21 16:50
Modified: 2025-12-04 21:03
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Assign, Metot
Author: Mustafa Halil

# `assign()` Metodu

`assign()` metodu, bir veri tablosu üzerinde çalışırken, tablonun **orijinal halini bozmadan** (değiştirilmezlik ilkesi) **yeni bir sütun eklemek veya mevcut sütunları değiştirmek** istediğinizde kullanılır.

Eğer elinizde bir satış tablosu varsa ve siz bu tabloya "Toplam Gelir" diye bir sütun eklemek istiyorsanız, `assign()` metodu ile bu yeni sütunu hesaplayıp ekleyebilirsiniz. Sonuç olarak, hem eski tablonuz hem de yeni eklenmiş sütuna sahip **yepyeni bir tablonuz** olur.

Pandas `DataFrame assign()` metodu, bir **veri tablosuna (DataFrame) yeni sütunlar eklemenin veya mevcut sütunları değiştirmenin** son derece düzenli ve güvenli bir yoludur.

Bu metodu anlamak için kullanacağımız anahtar kavram, **orijinali değiştirmemesi** ve her zaman **yeni bir DataFrame döndürmesidir**.

## Temel Özellikler:

1. **Yeni DataFrame Döndürür:** Orijinal DataFrame'i değiştirmez; her zaman eklenen veya güncellenen sütunları içeren yeni bir DataFrame nesnesi döndürür. Bu, özellikle veri analizi akışlarında (method chaining/zincirleme) çok kullanışlıdır.

2. **Sütun Ekleme veya Güncelleme:** Yeni bir sütun adı verirseniz ekler; eğer mevcut bir sütun adını kullanırsanız, o sütunun değerlerini günceller.

3. **Çok Yönlülük:** Tek bir sütun veya aynı anda birden fazla sütun ekleyebilir.

## Sözdizimi:

`assign()` metodunun genel kullanım şekli oldukça basittir:

```python
DataFrame.assign(**kwargs)
```

Buradaki `**kwargs`, eklemek istediğiniz `sütun adı = değer` çiftleridir.

## Değerler Ne Olabilir?

`assign()` metoduna atanan değerler üç ana şekilde gelebilir:

| Değer Türü                  | Açıklama                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Sabit Değer (Scalar)**    | Tüm satırlara aynı değeri atamak için kullanılır.                                                                |
| **Dizi Benzeri Nesneler**   | Liste, dizi veya bir Pandas `Series` (sütun uzunluğu DataFrame'in satır sayısıyla aynı olmalı).                  |
| **Fonksiyonlar (Callable)** | `lambda` ifadeleri veya harici fonksiyonlar. Bunlar `DataFrame`'in tamamını girdi olarak alarak hesaplama yapar. |

## Örneklerle assign() Metodu

Şimdi bu metodun farklı kullanım senaryolarını inceleyelim.

**Örnek 1: Sabit Bir Değerle Yeni Sütun Ekleme**

Bu, en basit kullanımdır. DataFrame'deki her satır için aynı değeri taşıyan bir sütun ekleriz.

Diyelim ki, sadece 'A' sütunu olan bir `DataFrame`'imiz var.

```python
import pandas as pd
a = pd.DataFrame({'A': [1, 2, 3]})
print(a)

# Çıktı:
#    A
# 0  1
# 1  2
# 2  3
```

Şimdi `assign()` kullanarak sabit bir liste/dizi değerini 'B' sütunu olarak ekleyelim:

```python
b = a.assign(B = [4, 5, 6])
print(b)

# Çıktı:
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6
```

Bu kod, 'A' sütununa ek olarak değerlerini içeren 'B' sütununu ekler ve yeni `DataFrame` **b**'yi oluşturur. Orijinal `a` DataFrame'i değişmemiştir.

**Sabit (Scalar) Değer Örneği:**

Tüm ürünler için para birimini ('USD') belirten sabit bir sütun eklemek:

```python
# Örnek DataFrame
df = pd.DataFrame({'Ucret': [25.99, 45.50]}) 
print(df) 
# Çıktı:
#    Ucret
# 0  25.99
# 1  45.50

# Sabit değer atama
df_guncellenmis = df.assign(Birim = 'TL', Stok = True) 
print(df_guncellenmis) 
# Çıktı:
#    Ucret   Birim    Stock
# 0  25.99      TL     True
# 1  45.50      TL     True
```

Bu örnekte, `Birim` ve `Stok` sütunları, tüm satırlara sabit değer olarak atanmıştır.

**Örnek 2: Mevcut Sütunlara Dayalı Hesaplama (Lambda Fonksiyonu)**

`assign()` metodunun en güçlü yönlerinden biri, mevcut sütunları kullanarak yeni bir sütun hesaplamasına izin vermesidir. Bunun için genelde **lambda fonksiyonları** kullanılır. Lambda fonksiyonu, DataFrame'in tamamını (genellikle `x` olarak adlandırılır) girdi olarak alır.

**Maaş Zammı Örneği:**

Diyelim ki bir personel tablonuz var ve maaşlara %10 zam yapılmış maaşı hesaplamak istiyorsunuz.

```python
veri = pd.DataFrame({'Personel': ["Ahmet", "Halil", "Ali"],
                'Maas': [100, 120, 150]
                })
print(veri)

# Çıktı:
  # #Personel  Maas
# #0    Ahmet   100
# #1    Halil   120
# #2      Ali   150

yeni_veri = veri.assign(
    Zamlı_Maas = lambda x: x['Maas'] + x['Maas'] * 0.10 # lambda x: x['Maas'] * 1.10 bu kod da aynı sonucu verir.
)
print(yeni_veri)

# #Çıktı:
  # #Personel  Maas  Zamlı_Maas
# #0    Ahmet   100       110.0
# #1    Halil   120       132.0
# #2      Ali   150       165.0
```

Bu kod, **"Zamlı_Maas"** adında yeni bir sütun oluşturur. Bu sütundaki her değer, mevcut "Maas" sütunundaki değerin %10 artırılmasıyla hesaplanır.

**Sütunları Çarpma Örneği:**

'A' ve 'B' sütunlarının çarpımını içeren yeni bir 'C' sütunu ekleyelim:

```python
import pandas as pd

a = pd.DataFrame({'A': [1, 2, 3]})
print(a)

# #Çıktı:
   # #A
# #0  1
# #1  2
# #2  3

b = a.assign(B = [4, 5, 6])
print(b)

# #Çıktı:
   # #A  B
# #0  1  4
# #1  2  5
# #2  3  6

# Yeni sütun 'C', diğer iki sütunun (A ve B) çarpımından oluşur

c = b.assign(C = lambda x: x['A'] * x['B'])
print(c)

# #Çıktı:
   # #A  B   C
# #0  1  4   4
# #1  2  5  10
# #2  3  6  18
```

Bu, `assign()` metodu içinde `lambda` fonksiyonu kullanılarak elde edilir.

**Örnek 3: Aynı Anda Birden Fazla Sütun Ekleme (Çoklu Atama)**

`assign()` metoduna birden fazla anahtar kelime argümanı (`kwargs`) vererek aynı anda çoklu sütun ekleyebilirsiniz.

**Çoklu Hesaplama Örneği (Maaş ve Takım Adı):**

Hem maaşa %40 zam yapmak hem de Departman adına bir sonek (`_Yazılım`) ifadesi eklemek istiyoruz.

```python
veri = pd.DataFrame({'Personel': ["Ahmet", "Halil", "Ali"],
                'Departman': ["Bilgi İşlem","Bilgi İşlem","Bilgi İşlem"], 
                'Maas': [100, 120, 150]
                })
print(veri)

# Çıktı:
  # #Personel    Departman  Maas
# #0    Ahmet  Bilgi İşlem   100
# #1    Halil  Bilgi İşlem   120
# #2      Ali  Bilgi İşlem   150
```

```python
yeni_veri = veri.assign(
    Departman = lambda x: x['Departman'] + '_Yazılım',  # Departman adının sonuna '_Yazılım' ifadesi ekler
    Zamlı_Maas = lambda x: x['Maas'] * 1.40 # Maaşa %40 zam yapar
)
print(yeni_veri)

# #Çıktı
  # #Personel            Departman  Maas  Zamlı_Maas
# #0    Ahmet  Bilgi İşlem_Yazılım   100       140.0
# #1    Halil  Bilgi İşlem_Yazılım   120       168.0
# #2      Ali  Bilgi İşlem_Yazılım   150       210.0
```

Bu kod, tek bir `assign()` çağrısında hem **"Departman"** hem de **"Maas"** olmak üzere iki yeni sütun oluşturur. Yukarıdaki örnekte **Departman** sütunu aslında güncellenerek yeniden oluşturulmuştur.

**Örnek 4: Zincirleme Kullanım (Chaining)**

`assign()` metodu her zaman yeni bir DataFrame döndürdüğü için, birden fazla `assign()` işlemini art arda zincirleme olarak kullanabilirsiniz.

Hatta, zincirleme kullanıldığında, sonraki `assign()` çağrıları önceki `assign()` çağrısında yeni oluşturulan sütunları kullanabilir.

```python
df = pd.DataFrame({'A': range(1, 5), 'B': ['A', 'B', 'C', 'D']})
print(df)

# #Çıktı:
   # #A  B
# #0  1  A
# #1  2  B
# #2  3  C
# #3  4  D
```

Yukarıdaki Tabloya önce `C` Sütunu ekleyelim. `C` Sütununun değeri `A` Sütununun değerinin 2 katı `C = A * 2` olsun. Ardından `D` Sütunu ekleyelim. `D` Sütununun değeri de `A` ve `C` Sütunlarının toplamı `D = A + C` olsun. Tüm isteklerimiz peşpeşe, zincirleme `assing()` fonksiyonu kullanımı ile gerçekleşsin.

```python
df = df.assign(C=lambda x: x['A']*2).assign(D=lambda x: x['A'] + x['C'])
print(df)

# #Çıktı:
   # #A  B  C   D
# #0  1  A  2   3
# #1  2  B  4   6
# #2  3  C  6   9
# #3  4  D  8  12
```

Bu, veri manipülasyonunu daha akıcı ve kompakt hale getirir.

**Örnek 5: Koşullu Sütun Oluşturma**

Belirli bir şarta bağlı olarak değer atayan sütunlar da oluşturabilirsiniz.

```python
print(df)

# #Çıktı:
   # #A  B  C   D
# #0  1  A  2   3
# #1  2  B  4   6
# #2  3  C  6   9
# #3  4  D  8  12
```

Yukarıdaki tabloya yeni bir (`E`) sütun oluşturup, `A` sütunundaki değer 2'den büyükse '`High`', değilse '`Low`' değeri atamaya çalışalım.z

```python
# A sütunundaki değer 2'den büyükse 'High', değilse 'Low' atar
df = df.assign(
    E=lambda x: ['High' if a > 2 else 'Low' for a in x['A']])

print(df)
# Output:
#    A B C D     E
# 0  1 A 2 3   Low
# 1  2 B 4 6   Low
# 2  3 C 6 9  High
# 3  4 D 8 12 High
```

Bu örnek, '**E**' sütununu dinamik olarak, '**A**' sütunundaki değerlere göre "**High**" veya "**Low**" olarak kategorize eder.

## Neden assign() Kullanmalıyız?

`assign()` metodu, `DataFrame`'lere köşeli parantez notasyonuyla (`df['yeni_sutun'] = ...`) sütun eklemekten farklıdır. Köşeli parantez notasyonu orijinal `DataFrame`'i doğrudan değiştirirken, `assign()` metodu orijinal verinizi korur ve her zaman yeni, temiz bir kopya döndürür. Bu, özellikle karmaşık veri akışları oluştururken veya büyük veri setlerinde bellek verimliliği açısından tercih edilir.

**Analoji / Benzeşim:**

`assign()` metodunu, elinizdeki orijinal bir tablonuza (DataFrame) notlar ekleyen bir asistan olarak düşünebilirsiniz. Siz asistana dersiniz ki, "Bana bu tablonun yeni bir kopyasını çıkar ve 'Özet' başlıklı bir sütun ekle." Asistanınız size, orijinal tablonuza dokunmadan, tüm notlarınızı ve yeni 'Özet' sütununu içeren yepyeni bir tablo (yeni DataFrame) sunar. Bu, orijinal verinizin her zaman güvende olduğu anlamına gelir.

## Kaynaklar:

* [pandas.DataFrame.assign &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign)

* [Google NotebookLM](https://notebooklm.google.com)

* [pandas: Add rows/columns to DataFrame with assign(), insert() | note.nkmk.me](https://note.nkmk.me/en/python-pandas-assign-append/)

* [Python:Pandas | DataFrame | .assign() | Codecademy](https://www.codecademy.com/resources/docs/pandas/dataframe/assign)

* [Pandas &#8211; Using DataFrame.assign() method (5 examples) - Sling Academy](https://www.slingacademy.com/article/pandas-using-dataframe-assign-method/)

* [Pandas DataFrame assign() Method - Spark By {Examples}](https://sparkbyexamples.com/pandas/pandas-dataframe-assign-method/)

* [Pandas DataFrame assign() Method - Create new Columns in DataFrame - GeeksforGeeks](https://www.geeksforgeeks.org/pandas/pandas-dataframe-assign/)
