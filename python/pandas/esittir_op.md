Title: Pandas - Eşittir Operatörü
Date: 2022-07-16 00:00 
Modified: 2025-06-26 14:30
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, Eşittir, Operatör
Author: Mustafa Halil

# == (Eşittir) Operatörü

**Eşittir (==)** ya da bir başka deyimle **Eşit midir?** operatörü kullanım mantığı şu şekildedir; Eğer **Eşit ise** `True` değeri döndür.

Örnek Veri çerçevemiz aşağıda görünmektedir.

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

247 rows × 4 columns

Sadece **2010 yılına** ait filmleri görmek istersen **== operatörünü** kullanarak aşağıdaki filtreleme yöntemini kullanabiliriz.

```python
print(imdb[imdb["Yıl"] == 2010])
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 14  | Inception                | 2010 | 8.7  | 844938       |
| 63  | Toy Story 3              | 2010 | 8.4  | 320991       |
| 166 | How to Train Your Dragon | 2010 | 8.1  | 249971       |
| 177 | The King's Speech        | 2010 | 8.1  | 288159       |
| 194 | Black Swan               | 2010 | 8.0  | 373745       |
| 231 | Shutter Island           | 2010 | 8.0  | 436151       |
| 233 | Incendies                | 2010 | 8.0  | 36751        |

Yukarıdaki yazım tarzı kafanızı karıştırdıysa, aşağıdaki (parçalara ayrılmış) yazım tarzı daha anlaşılır gelebilir.
Önce filtreyi tanımlıyor, sonra veri çerçevesine dahil ediyoruz.

```python
filtre_2010 = imdb["Yıl"] == 2010
print(imdb[filtre_2010])
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 14  | Inception                | 2010 | 8.7  | 844938       |
| 63  | Toy Story 3              | 2010 | 8.4  | 320991       |
| 166 | How to Train Your Dragon | 2010 | 8.1  | 249971       |
| 177 | The King's Speech        | 2010 | 8.1  | 288159       |
| 194 | Black Swan               | 2010 | 8.0  | 373745       |
| 231 | Shutter Island           | 2010 | 8.0  | 436151       |
| 233 | Incendies                | 2010 | 8.0  | 36751        |

Başka bir örnek yapalım. Öncelikle varolan tablolarımızda birini içe aktarıp veri çerçevesine dönüştürelim.

```python
json = pd.read_json("Veri_Setleri/json_verisi.json")
json
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | 60       | 110   | 130      | 409      |
| 1   | 60       | 117   | 145      | 479      |
| 2   | 60       | 103   | 135      | 340      |
| 3   | 45       | 109   | 175      | 282      |
| 4   | 45       | 117   | 148      | 406      |
| 5   | 60       | 102   | 127      | 300      |

Veri çerçevemizdeki **her bir değerin 60**'a eşit olup olmadığını sorgulayalım.

```python
print(json == 60)
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | True     | False | False    | False    |
| 1   | True     | False | False    | False    |
| 2   | True     | False | False    | False    |
| 3   | False    | False | False    | False    |
| 4   | False    | False | False    | False    |
| 5   | True     | False | False    | False    |

Veri çerçevemizde **60'a eşit*** kaç adet toplam değer var? Bunu da `sum()` metodu ile hesaplatalım.

```python
(json == 60).sum().sum()
```

```python
4
```
