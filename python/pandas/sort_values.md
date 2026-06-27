Title: Pandas - sort_values
Date: 2022-07-15 00:00
Modified: 2025-06-23 23:27
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Sıralama, sort_values, by, ascending, na_position
Author: Mustafa Halil

# `sort_values()` Metodu

Veri çerçevesini **sütun(lar)daki değerlere göre** sıralamak istersek (sütun başlıklarına göre **değil)**, `sort_values()` metodunu kullanmalıyız. Sütun başlıklarına (isimlerine) göre sıralama yapmak isterseniz, [sort_index() Fonksiyonu]({filename}sort_index.md)nu ya da [reindex() Fonksiyonu]({filename}reindex.md) inceleyebilirsiniz

# Parametreler

## by Parametresi

`sort_values()` fonksiyonu ile sütun değerlerine göre sıralama yapmak için `by` parametresi kullanılmalıdır. `by` parametresi, bir veya daha fazla sütunu belirtmek için kullanılabilir. 
Bu durumda sütun isimlerini köşeli parantez içinde yani bir **liste** olarak yazmalıyız. Fonksiyonu, örneklerle inceleyelim.

```python
import pandas as pd
df = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
print(df.head(10))
```

| Film_Adı                                       | Yıl  | Puan | Oylayan_Kişi |
| ---------------------------------------------- | ---- | ---- | ------------ |
| The Shawshank Redemption                       | 1994 | 9,2  | 1071904      |
| The Godfather                                  | 1972 | 9,2  | 751381       |
| The Godfather: Part II                         | 1974 | 9    | 488889       |
| Pulp Fiction                                   | 1994 | 8,9  | 830504       |
| The Dark Knight                                | 2008 | 8,9  | 1045186      |
| 12 Angry Men                                   | 1957 | 8,9  | 264112       |
| Schindler's List                               | 1993 | 8,9  | 545703       |
| The Lord of the Rings: The Return of the King  | 2003 | 8,8  | 758388       |
| Fight Club                                     | 1999 | 8,8  | 814389       |
| Star Wars: Episode V - The Empire Strikes Back | 1980 | 8,8  | 519895       |

Örneğin yukarıda oluşturduğumuz **df** veri çerçevesini, **Yıla göre sıralamak** istersek aşağıdaki kodu çalıştırmalıyız.

```python
print(df.sort_values(by="Yıl"))
```

| Film_Adı                          | Yıl  | Puan | Oylayan_Kişi |
| --------------------------------- | ---- | ---- | ------------ |
| The Kid                           | 1921 | 8,2  | 35316        |
| The Gold Rush                     | 1925 | 8,2  | 41458        |
| The General                       | 1926 | 8,2  | 34819        |
| Metropolis                        | 1927 | 8,3  | 74994        |
| All Quiet on the Western Front    | 1930 | 8    | 38373        |
| ...                               | ...  | ...  | ...          |
| The Avengers                      | 2012 | 8,1  | 568037       |
| The Hobbit: An Unexpected Journey | 2012 | 8    | 352517       |
| Life of Pi                        | 2012 | 8    | 246325       |
| Rush                              | 2013 | 8    | 28676        |
| Gravity                           | 2013 | 8,5  | 33721        |

247 rows × 3 columns

Sıralama işlemini birden fazla sütuna göre yapmak istersek, sütun isimlerini köşeli parantez içinde yani bir **liste** olarak belirtmemiz gerekir.

```python
print(df.sort_values(by=["Puan", "Yıl"]))
```

| Film_Adı                       | Yıl  | Puan | Oylayan_Kişi |
| ------------------------------ | ---- | ---- | ------------ |
| All Quiet on the Western Front | 1930 | 8    | 38373        |
| Rope                           | 1948 | 8    | 66041        |
| A Streetcar Named Desire       | 1951 | 8    | 60767        |
| Stalag 17                      | 1953 | 8    | 33518        |
| Roman Holiday                  | 1953 | 8    | 63443        |
| ...                            | ...  | ...  | ...          |
| Schindler's List               | 1993 | 8,9  | 545703       |
| Pulp Fiction                   | 1994 | 8,9  | 830504       |
| The Dark Knight                | 2008 | 8,9  | 1045186      |
| The Godfather                  | 1972 | 9,2  | 751381       |
| The Shawshank Redemption       | 1994 | 9,2  | 1071904      |

247 rows × 3 columns

Bu kod ile, öncelikle **Puan** sütununa göre sıralama yapılır, **Puan** sütununda aynı değerler yanyana geldiğinde ise, **Yıl** sütunu baz alınarak sıralama yapılır.

## ascending Parametresi

Yukarıdaki örneklerde göreceğiniz gibi Veri çerçevesi, **Yıl**a göre sıralandığında, varsayılan olarak alfabetik artan (küçükten büyüğe) şeklinde sıralandı. Eğer alfabetik azalan (büyükten küçüğe) şeklinde sıralamak istersek (yani sıralamayı ters çevirmek istersek) `ascending=False` parametresini kullanmalıyız.

```python
print(df.sort_values(by="Yıl", ascending=False))
```

| Film_Adı                       | Yıl  | Puan | Oylayan_Kişi |
| ------------------------------ | ---- | ---- | ------------ |
| Rush                           | 2013 | 8    | 28676        |
| Gravity                        | 2013 | 8,5  | 33721        |
| The Avengers                   | 2012 | 8,1  | 568037       |
| The Dark Knight Rises          | 2012 | 8,4  | 672751       |
| The Hunt                       | 2012 | 8,1  | 39033        |
| ...                            | ...  | ...  | ...          |
| All Quiet on the Western Front | 1930 | 8    | 38373        |
| Metropolis                     | 1927 | 8,3  | 74994        |
| The General                    | 1926 | 8,2  | 34819        |
| The Gold Rush                  | 1925 | 8,2  | 41458        |
| The Kid                        | 1921 | 8,2  | 35316        |

247 rows × 3 columns

## na_position Parametresi

`sort_values()` fonksiyonu, `na_position` parametresi aracılığıyla **NA** (yani kayıp / eksik veri) değerlerini özel işleme tabi tutarak sıralayabilir.

**Numpy** Kütüphanesini kullanarak Rastgele sayılardan müteşekkil örnek bir veri çerçevesi oluşturup içeriğine bakalım.

```python
import numpy as np
df2 = pd.DataFrame(
    {
        "Sütun_1": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "Sütun_2": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "Sütun_3": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
        "Sütun_4": pd.Series(np.random.randn(2), index=["a", "d"]),
    }
)
print(df2)
```

|     | Sütun_1   | Sütun_2  | Sütun_3   | Sütun_4   |
| --- | --------- | -------- | --------- | --------- |
| a   | -1.485741 | 0.063539 | NaN       | -1.125456 |
| b   | -1.675240 | 0.417121 | 0.662779  | NaN       |
| c   | -0.341007 | 0.701759 | -0.998608 | NaN       |
| d   | NaN       | 2.495466 | 0.149067  | 1.512350  |

Görüldüğü üzere, **Sütun_1, Sütun_3** ve **Sütun_4**'te **NaN (Not a Number)** kayıp/eksik veriler bulunmakta.
Örneğin **Sütun_4**'e göre yapılacak sıralama işleminde, **NaN** değerlerini en üste almak isteyelim. Bunun için `na_position` parametresinin `"first"` seçeneğini belirtmemiz gerekir.

```python
print(df2.sort_values(by= "Sütun_4", na_position="first"))
```

|     | Sütun_1   | Sütun_2  | Sütun_3   | Sütun_4   |
| --- | --------- | -------- | --------- | --------- |
| b   | -1.675240 | 0.417121 | 0.662779  | NaN       |
| c   | -0.341007 | 0.701759 | -0.998608 | NaN       |
| a   | -1.485741 | 0.063539 | NaN       | -1.125456 |
| d   | NaN       | 2.495466 | 0.149067  | 1.512350  |

**Sütun_4**'e göre yapılacak sıralama işleminde, **NaN** değerlerini en alta almak istersek, bu defa `na_position` parametresinin `"last"` seçeneğini belirtmemiz gerekir.

```python
print(df2.sort_values(by= "Sütun_4", na_position="last"))
```

|     | Sütun_1   | Sütun_2  | Sütun_3   | Sütun_4   |
| --- | --------- | -------- | --------- | --------- |
| a   | -1.485741 | 0.063539 | NaN       | -1.125456 |
| d   | NaN       | 2.495466 | 0.149067  | 1.512350  |
| b   | -1.675240 | 0.417121 | 0.662779  | NaN       |
| c   | -0.341007 | 0.701759 | -0.998608 | NaN       |
