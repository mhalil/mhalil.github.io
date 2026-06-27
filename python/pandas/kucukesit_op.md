Title: Pandas - KüçükEşittir Operatörü
Date: 2022-07-16 00:00 
Modified: 2025-06-26 14:35
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, KüçükEşittir, Operatör
Author: Mustafa Halil

# <= (KüçükEşit) Operatörü

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

**8,0 ve küçük Puana** sahip filmleri listelemek istersek;

```python
print(imdb[imdb["Puan"] <= 8.0])
```

| c   | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 182 | Donnie Darko             | 2001 | 8.0  | 398128       |
| 183 | Dog Day Afternoon        | 1975 | 8.0  | 126624       |
| 184 | Amores Perros            | 2000 | 8.0  | 120868       |
| 185 | Howl's Moving Castle     | 2004 | 8.0  | 121059       |
| 186 | Mary and Max             | 2009 | 8.0  | 67759        |
| ... | ...                      | ...  | ...  | ...          |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       |
| 246 | Papillon                 | 1973 | 7.9  | 62517        |

65 rows × 4 columns

**8.0 ve aşağısında Puan alan** toplam **65** adet film varmış. 
