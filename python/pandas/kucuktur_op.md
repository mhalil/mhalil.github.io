Title: Pandas - Küçüktür Operatörü
Date: 2022-07-16 00:00 
Modified: 2025-06-26 14:39
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, Küçüktür,  Operatör
Author: Mustafa Halil

# < (Küçüktür) Operatörü

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
Mantiksal_imdb = imdb["Puan"] < 8
print(Mantiksal_imdb)
```

```python
0      False
1      False
2      False
3      False
4      False
       ...  
242     True
243     True
244     True
245     True
246     True
Name: Puan, Length: 247, dtype: bool
```

Bu durumda, **Puan** sütunundaki değerler, verilen kritere göre (8'den küçük olup olmadığı) sorgulanıyor ve her değer için **True** (Doğru) yani değer 8'den küçük ya da **False** (yanlış) yani değer 8'e eşit ya da büyük sonucu vdöndürüyor.

Puan'ı 8'den küçük verileri tablo halinde görmek istersek aşağıdaki kodu kullanabiliriz.

```python
print(imdb[imdb["Puan"] < 8])
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 239 | Beauty and the Beast     | 1991 | 7.9  | 189229       |
| 240 | Three Colors: Red        | 1994 | 7.9  | 43438        |
| 241 | Bringing Up Baby         | 1938 | 7.9  | 35695        |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       |
| 246 | Papillon                 | 1973 | 7.9  | 62517        |

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

Veri çerçevemizdeki **her bir değerin 150'den küçük** olup olmadığını sorgulayalım.  

```python
json < 150
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | True     | True  | True     | False    |
| 1   | True     | True  | True     | False    |
| 2   | True     | True  | True     | False    |
| 3   | True     | True  | False    | False    |
| 4   | True     | True  | True     | False    |
| 5   | True     | True  | True     | False    |

Gördüğünüz gibi, tablodaki tüm değerler, verilen kriter olan 150'den küçük olup olmadığına göre sorgulandı ve cevabı her bir hücreye işlendi.
