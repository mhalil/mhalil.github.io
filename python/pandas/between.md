Title: Pandas - Between
Date: 2022-07-16 00:00 
Modified: 2025-06-26 14:42
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, Between, Fonksiyon
Author: Mustafa Halil

# between() Fonksiyonu

Bir sayısal aralık belirterek filtreleme yapmak istersek `between()` metodunu / fonksiyonunu kullanabiliriz.

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

**1960** ile **1980** yılları arasındaki filmleri filtrelemeye çalışalım.

```python
print(imdb["Yıl"].between(1960,1980))
```

```python
0      False
1       True
2       True
3      False
4      False
       ...  
242    False
243     True
244    False
245    False
246     True
Name: Yıl, Length: 247, dtype: bool
```
