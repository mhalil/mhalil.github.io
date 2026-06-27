Title: Pandas - concat
Date: 2022-07-15 00:00
Modified: 2025-12-04 15:16
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Bitleştir, concat
Author: Mustafa Halil

# `concat()` Metodu

**Concat** kelimesi Concatenate kelimesinin kısaltamasıdır. **Concatenate** kelimesinin Türkçe karşılığı **Birleştir**'dir.  
`concat()` metodu ile veri çerçeveleri **alt alta ya da yan yana birleştirilebilir**. Varsayılan değer satır bazlı yani alt alta birleştirmedir.

## Sözdizimi:

```python
pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, 
                keys=None, levels=None, names=None, verify_integrity=False,
                sort=False, copy=None)
```

## Parametreler:

| Parametre              | Açıklama                                                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`objs`**             | Birleştirilecek **Series** veya **DataFrame** nesnelerinin bir dizisi (`sequence`) veya eşlemesi (`mapping`). Bir eşleme (örneğin bir sözlük) iletilirse, sıralanmış anahtarlar `keys` argümanı olarak kullanılır. |
| **`axis`**             | Birleştirmenin yapılacağı ekseni belirteceğimiz parametredir. `0`: Satırlar boyunca birleştirme yapılır. (**Varsayılan**)<br>`1`: Sütunlar boyunca birleştirme yapılır.                                            |
| **`join`**             | Diğer eksenlerdeki (birleştirme yapılmayan) indekslerin nasıl ele alınacağını belirtir. Değerler: `{'inner', 'outer'}`. Varsayılan: '`outer`' (tüm indeksleri birleştirir, eşleşmeyen yerlere `NaN` koyar).        |
| **`ignore_index`**     | **bool**, değer alır. **Varsayılan: `False`**. <br>Eğer **`True`** ise, birleştirme ekseni boyunca mevcut indeks değerlerini kullanmaz. Ortaya çıkan eksen 0'dan başlayarak etiketlenir.                           |
| **`keys`**             | **sequence**, **Varsayılan: `None`**. Belirtilirse, en dış düzey olarak bu anahtarları kullanarak hiyerarşik bir indeks (**MultiIndex**) oluşturur.                                                                |
| **`levels`**           | **dizilerin listesi**, **Varsayılan: `None`**. Bir MultiIndex oluşturmak için kullanılacak belirli düzeyleri (benzersiz değerleri) belirtir. Aksi takdirde `keys` argümanından çıkarılır.                          |
| **`names`**            | **liste**, **Varsayılan: `None`**. Sonuçtaki hiyerarşik indeksteki düzeyler için adlar belirtir.                                                                                                                   |
| **`verify_integrity`** | **bool**, **Varsayılan: `False`**. Eğer **`True`** ise, yeni birleştirilmiş eksenin yinelenen değerler içerip içermediğini kontrol eder. Bu, veri birleştirmeye göre oldukça maliyetli olabilir.                   |
| **`sort`**             | **bool**, **Varsayılan: `False`**. Zaten hizalı değilse, birleştirme dışı ekseni sıralar.                                                                                                                          |
| **`copy`**             | **bool**, **Varsayılan: `True`**. Eğer **`False`** ise, veriyi gereksiz yere kopyalamamaya çalışır.                                                                                                                |

### 📝 Özet Bilgi

`pandas.concat` fonksiyonu, temel olarak birden fazla **Series** veya **DataFrame** nesnesini belirli bir eksen boyunca (satır veya sütun) birleştirmek için kullanılır. En yaygın kullanımları şunlardır:

1. **Satır Ekleme (`axis=0`):** Birden çok DataFrame'i alt alta (satırlar boyunca) birleştirir.

2. **Sütun Ekleme (`axis=1`):** Birden çok DataFrame'i yan yana (sütunlar boyunca) birleştirir.

3. **İndeks Yönetimi:** `join` parametresi ile eksik verilerin nasıl ele alınacağını (`inner` veya `outer`), `ignore_index` ile de indekslerin sıfırlanıp sıfırlanmayacağını kontrol edebilirsiniz.

Birleştirme örneklerini öğrenemek için öncelikle 2 sözlük yapısı oluşturup, bunları veri çerçevesine dönüştürelim.

```python
veri1 = {'A': ['A1','A2','A3','A4'],
         'B': ['B1','B2','B3','B4'],
         'C': ['C1','C2','C3','C4']}

veri2 = {'A': ['A5','A6','A7','A8'],
         'B': ['B5','B6','B7','B8'],
         'C': ['C5','C6','C7','C8']}

df1 = pd.DataFrame(veri1, index = [1,2,3,4])
df2 = pd.DataFrame(veri2, index = [5,6,7,8])
print(df1)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | A1  | B1  | C1  |
| 2   | A2  | B2  | C2  |
| 3   | A3  | B3  | C3  |
| 4   | A4  | B4  | C4  |

```python
print(df2)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 5   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 7   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |

Oluşturduğumuz veri çerçevelerini, `concat()` fonksiyonu ile birleştirelim. `concat()` fonksiyonuna en az iki adet veri çevçevesi eklemek gerekir. Malumunuz, Pandas'ta genellikle birden fazla parametre, seçenek ekleneceği zaman, bu değerler köşeli parantez içerisinde yani **liste** veri tipi olarak yazılır.

```python
print(pd.concat([df1, df2]))
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | A1  | B1  | C1  |
| 2   | A2  | B2  | C2  |
| 3   | A3  | B3  | C3  |
| 4   | A4  | B4  | C4  |
| 5   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 7   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |

Gördüğünüz gibi, iki veri çerçevesi altalta birleştirildi.

## Parametreler

### `axis` parametresi

Hatırlarsanız **`drop()`** metodunu anlatırken **`axis`** parametresinden bahsetmiştik. **axis** parametresi, **0 ve 1** değerlerini alır, **0 satırları, 1 ise sütunları** temsil eder demiştik. Aynı parametreyi birleştirme işleminde de kullanabiliriz. eğer **axis** parametresi kullanılmaz ise, varsayılan değer **`axis = 0`** olduğu için yani satırları baz alarak birleştirme yapılır.

Şimdi **`axis=1`** parametresini ekleyerek veri çerçevelerini yanyana birleştirmeyi deneyelim.

```python
print(pd.concat([df1, df2], axis = 1))
```

|     | A   | B   | C   | A   | B   | C   |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | A1  | B1  | C1  | NaN | NaN | NaN |
| 2   | A2  | B2  | C2  | NaN | NaN | NaN |
| 3   | A3  | B3  | C3  | NaN | NaN | NaN |
| 4   | A4  | B4  | C4  | NaN | NaN | NaN |
| 5   | NaN | NaN | NaN | A5  | B5  | C5  |
| 6   | NaN | NaN | NaN | A6  | B6  | C6  |
| 7   | NaN | NaN | NaN | A7  | B7  | C7  |
| 8   | NaN | NaN | NaN | A8  | B8  | C8  |

Bu durumda, 2 veri çerçevesi yanyana birleştirildi ancak veri çerçevelerinde aynı indeks değerleri bulunmadığı için ilgili indeks değerinin karşılığında **`NaN` (Not A Number)** değeri atandı.

 Eğer aşağıdaki gibi bir veri çerçevemiz olsaydı ve bu veri çerçevesini df1 ile yanyana birleştirseydik nasıl bir sonuç elde ederdik dersiniz.

```python
veri3 = {'A': ['A5','A6','A7','A8'],'B': ['B5','B6','B7','B8'],'C': ['C5','C6','C7','C8']}
df3 = pd.DataFrame(veri3, index = [1,6,3,8])
print(df3)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 3   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |

```python
print(pd.concat([df1, df3], axis = 1))
```

|     | A   | B   | C   | A   | B   | C   |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | A1  | B1  | C1  | A5  | B5  | C5  |
| 2   | A2  | B2  | C2  | NaN | NaN | NaN |
| 3   | A3  | B3  | C3  | A7  | B7  | C7  |
| 4   | A4  | B4  | C4  | NaN | NaN | NaN |
| 6   | NaN | NaN | NaN | A6  | B6  | C6  |
| 8   | NaN | NaN | NaN | A8  | B8  | C8  |

df1 ve df3'te ortak indeks değerleri olduğu için 1. ve 3. satırlar tamamen geçerli veri ile doldu.

**`concat`** metodu sadece 2 veri çerçevesini birleştirmiyor. 2'den fazla veri çerçevesini de birleştiriyor. Oluşturduğumuz df1, df2 ve df3 veri çerçevelerini altalta ve yanyana birleştirip sonuçları inceleyelim.

```python
print(pd.concat([df1, df2, df3]))
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | A1  | B1  | C1  |
| 2   | A2  | B2  | C2  |
| 3   | A3  | B3  | C3  |
| 4   | A4  | B4  | C4  |
| 5   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 7   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |
| 1   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 3   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |

```python
print(pd.concat([df1, df2, df3], axis = 1))
```

|     | A   | B   | C   | A   | B   | C   | A   | B   | C   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | A1  | B1  | C1  | NaN | NaN | NaN | A5  | B5  | C5  |
| 2   | A2  | B2  | C2  | NaN | NaN | NaN | NaN | NaN | NaN |
| 3   | A3  | B3  | C3  | NaN | NaN | NaN | A7  | B7  | C7  |
| 4   | A4  | B4  | C4  | NaN | NaN | NaN | NaN | NaN | NaN |
| 5   | NaN | NaN | NaN | A5  | B5  | C5  | NaN | NaN | NaN |
| 6   | NaN | NaN | NaN | A6  | B6  | C6  | A6  | B6  | C6  |
| 7   | NaN | NaN | NaN | A7  | B7  | C7  | NaN | NaN | NaN |
| 8   | NaN | NaN | NaN | A8  | B8  | C8  | A8  | B8  | C8  |

### `ignore_index` Parametresi

Bu parametre, birleştirme işlemi esnasında index değerlerinin orijinal değerlerinin tutulması ya da birleştirilme sonrası yeni index değeri atanması için kullanılır.

Mevcut klasördeki tüm CSV uzantılı dosyaları hem `ignore_index`

 parametresi kullanarak hemde kullanmadan birleştirelim.

```python
import glob
import pandas as pd

dosyalar = glob.glob("*.csv")

Tumu = pd.concat((pd.read_csv(dosya) for dosya in dosyalar))
print(Tumu)
```

Çıktı:

```python
   baslik1   baslik2   baslik3
0      100       200       300
1      400       500       600
2      700       800       900
0       10        20        30
1       40        50        60
2       70        80        90
0        1         2         3
1        4         5         6
2        7         8         9
```

`ignore_index` Parametresi kullanılmadan birleştirme yapıldığında, index değerleri, her dosyada olduğu gibi kalır. 

`ignore_index` Parametresini kullanarak birleştirme işlemi sonucuna bakalım;

```python
import glob
import pandas as pd

dosyalar = glob.glob("*.csv")

Tumu = pd.concat((pd.read_csv(dosya) for dosya in dosyalar), ignore_index=True)
print(Tumu)
```

Çıktı:

```python
   baslik1   baslik2   baslik3
0      100       200       300
1      400       500       600
2      700       800       900
3       10        20        30
4       40        50        60
5       70        80        90
6        1         2         3
7        4         5         6
8        7         8         9
```

Görüldüğü üzere,  koda`ignore_index=True` ifadesi eklendiğinde dosyaların **index** değerleri gözardı edilerek birleştirme işlemi sonrası yeniden oluşturuluyor.

## Kaynaklar:

* [pandas.concat &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

* [Tanıtım | Pandas Dersleri - YouTube](https://www.youtube.com/watch?v=8pn4hSZ-5ds)

* [Temel Bilgiler | Pandas Dersleri - YouTube](https://www.youtube.com/watch?v=SoATtjBv4Iw)
