Title: Pandas - Eşit Değil Operatörü
Date: 2022-07-16 00:00 
Modified: 2025-07-05 16:55
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, Eşitdeğil, Operatör
Author: Mustafa Halil

# != (Eşit Değil) Operatörü

Örnek Veri çerçevemiz caşağıda görünmektedir.

```python
import pandas as pd
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", decimal=",")
print(imdb)
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9.0  | 488889       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| ... | ...                      | ...  | ...  | ...          |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       |
| 246 | Papillon                 | 1973 | 7.9  | 62517        |

247 rows × 4 columns.

**8.0 puanın dışındaki** filmleri görmek istersen **!= operatörünü** kullanarak aşağıdaki filtreleme yöntemini kullanabiliriz.

```python
print(imdb[imdb["Puan"] != 8.0])
```

tablo

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9.0  | 488889       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| ... | ...                      | ...  | ...  | ...          |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       |
| 246 | Papillon                 | 1973 | 7.9  | 62517        |

190 rows × 4 columns

Yukarıdaki ilk tablomuzun çıktısını incelediğimizde **247** satırlık veri (247 rows) olduğu görülürken, **Puan** değeri **8.0'a eşit olmayan** yani 8.0'dan farklı verileri görmek istediğimizde, çıktıda **190** satırlık veri (190 rows) olduğunu görmekteyiz.

Başka bir örnek yapalım. Öncelikle varolan tablolarımızda birini içe aktarıp veri çerçevesine dönüştürelim.

```python
json = pd.read_json("Veri_Setleri/json_verisi.json")
print(json)
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | 60       | 110   | 130      | 409      |
| 1   | 60       | 117   | 145      | 479      |
| 2   | 60       | 103   | 135      | 340      |
| 3   | 45       | 109   | 175      | 282      |
| 4   | 45       | 117   | 148      | 406      |
| 5   | 60       | 102   | 127      | 300      |

Veri çerçevemizdeki **her bir değerin 170'den farklı yani 170'e eşit olmayan** değer olup olmadığını sorgulayalım.  
Veri çerçevemizde **117**'ye eşit olmayan sayı varsa ilgili değer yerine `True` değerini görüntüler.

```python
print(json != 117)
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | True     | True  | True     | True     |
| 1   | True     | False | True     | True     |
| 2   | True     | True  | True     | True     |
| 3   | True     | True  | True     | True     |
| 4   | True     | False | True     | True     |
| 5   | True     | True  | True     | True     |

Veri çerçevemizde **117**'den farklı kaç sayı var?

```python
print((json != 117).sum().sum())
```

```python
22
```

Peki bunların Sütun dağılımları nasıl? Hangi Sütunda 117'den farklı kaç adet değer var? Bunu nasıl öğrenebiliriz? 

```python
print((json != 117).sum())
```

```python
Duration    6
Pulse       4
Maxpulse    6
Calories    6
dtype: int64
```
