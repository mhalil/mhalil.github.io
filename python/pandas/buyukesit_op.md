Title: Pandas - BüyükEşit Operatörü
Date: 2022-07-16 00:00 
Modified: 2025-06-26 14:35
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, BüyükEşittir, Operatör
Author: Mustafa Halil

# >= (BüyükEşit)Operatörü

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

**8,8 ve üzeri Puana** sahip filmleri listelemek istersek;

```python
filtre_88 = imdb["Puan"] >= 8.8
print(imdb[filtre_88])
```

|     | Film_Adı                                          | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption                          | 1994 | 9.2  | 1071904      |
| 1   | The Godfather                                     | 1972 | 9.2  | 751381       |
| 2   | The Godfather: Part II                            | 1974 | 9.0  | 488889       |
| 3   | Pulp Fiction                                      | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight                                   | 2008 | 8.9  | 1045186      |
| 5   | 12 Angry Men                                      | 1957 | 8.9  | 264112       |
| 6   | Schindler's List                                  | 1993 | 8.9  | 545703       |
| 7   | The Lord of the Rings: The Return of the King     | 2003 | 8.8  | 758388       |
| 8   | Fight Club                                        | 1999 | 8.8  | 814389       |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980 | 8.8  | 519895       |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001 | 8.8  | 784999       |
