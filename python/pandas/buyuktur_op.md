Title: Pandas - Büyüktür Operatörü
Date: 2022-07-16 00:00 
Modified: 2025-11-15 22:30
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, Büyüktür,  Operatör
Author: Mustafa Halil

# > (Büyüktür) Operatörü

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

Karşılaştırma operatorlerini, Filtreleme işlemini dışında kıyaslama amacıyla da kullanabiliriz. Aşağıdaki kullanımı inceleyelim.

```python
Mantiksal_imdb = imdb["Puan"] > 8.8
print(Mantiksal_imdb)
```

```python
0       True
1       True
2       True
3       True
4       True
       ...  
242    False
243    False
244    False
245    False
246    False
Name: Puan, Length: 247, dtype: bool
```

Bu durumda, **Puan** sütunundaki değerler, verilen kritere göre (8'den büyük olup olmadığı) sorgulanıyor ve her değer için **True** (Doğru) yani değer 8'den büyük ya da **False** (yanlış) yani değer 8'e eşit ya da küçük sonucu döndürüyor.

Puan'ı 8'den büyük verileri tablo halinde görmek istersek aşağıdaki kodu kullanabiliriz.

```python
print(imdb[imdb["Puan"] > 8.8])
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9.0  | 488889       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| 5   | 12 Angry Men             | 1957 | 8.9  | 264112       |
| 6   | Schindler's List         | 1993 | 8.9  | 545703       |

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

Veri çerçevemizdeki **her bir değerin 110'dan büyük** olup olmadığını sorgulayalım.  

```python
print(json > 110)
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | False    | False | True     | True     |
| 1   | False    | True  | True     | True     |
| 2   | False    | False | True     | True     |
| 3   | False    | False | True     | True     |
| 4   | False    | True  | True     | True     |
| 5   | False    | False | True     | True     |

Gördüğünüz gibi, tablodaki tüm değerler, verilen kriter olan 110'dan büyük olup olmadığına göre sorgulandı ve cevabı her bir hücreye işlendi.

**Sütunlarda**, Değeri 110'dan büyük kaçar adet sayı olduğunu bulmak istersek `sum()` metodunu kullanmamız gerekir;

```python
print((json > 110).sum())
```

```python
Duration 0
Pulse 2
Maxpulse 6
Calories 6
dtype: int64
```

Veri çerçevemizde, 110'dan büyük **toplam** kaç adet sayı vardır, diye merak edersek;

```python
print((json > 110).sum().sum())
```

```python
14
```
