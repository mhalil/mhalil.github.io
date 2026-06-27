Title: Pandas - Sütun Filtrele
Date: 2022-07-11 00:00
Modified: 2025-07-05 18:45
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, Koşul, Filtre, Sütun
Author: Mustafa Halil

# Sütun Filtrelemek

Sadece bir Sütunu filtrelemek/görüntülemek için veri çerçevesinin adı ile birlikte filtrelemek/görüntülemek istediğimiz sütunun ismini yazmak yeterlidir. Bu da iki şekilde gerçekleştirilebilir.

1. `VeriCervecesiAdı.SütunAdı`
2. `VeriCervecesiAdı["SütunAdı"]`

Sütun isminde **boşluk** ya da **nokta** karakterleri bulunması halinde, ilk (noktalı) seçeneği KULLANAMAYIZ, o durumda 2. seçeneği  yani **köşeli parantez**li seçeneği kullanmamız gerekir.
Bunları da örneklerle görelim. Elimizde aşağıdaki gibi bir veri çerçevesi olduğunu varsayalım.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
print(imdb)
```

| Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| ------------------------ | ---- | ---- | ------------ |
| The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| The Godfather            | 1972 | 9,2  | 751381       |
| The Godfather: Part II   | 1974 | 9    | 488889       |
| Pulp Fiction             | 1994 | 8,9  | 830504       |
| The Dark Knight          | 2008 | 8,9  | 1045186      |
| ...                      | ...  | ...  | ...          |
| Mystic River             | 2003 | 7,9  | 256159       |
| In the Heat of the Night | 1967 | 7,9  | 37081        |
| Arsenic and Old Lace     | 1944 | 7,9  | 45893        |
| Before Sunrise           | 1995 | 7,9  | 100974       |
| Papillon                 | 1973 | 7,9  | 62517        |

247 rows × 3 columns

Eğer İndex verisi dışında sadece **Puan** isimli sütun verilerini görmek istersek;

```python
print(imdb.Puan)
```

```python
Film_Adı
The Shawshank Redemption     9,2
The Godfather                9,2
The Godfather: Part II         9
Pulp Fiction                 8,9
The Dark Knight              8,9
                            ... 
Mystic River                 7,9
In the Heat of the Night     7,9
Arsenic and Old Lace         7,9
Before Sunrise               7,9
Papillon                     7,9
Name: Puan, Length: 247, dtype: object
```

Aynı sonuca, aşağıdaki kodu yazarak ta ulaşabiliriz;

```python
print(imdb["Puan"])
```

```python
Film_Adı
The Shawshank Redemption     9,2
The Godfather                9,2
The Godfather: Part II         9
Pulp Fiction                 8,9
The Dark Knight              8,9
                            ... 
Mystic River                 7,9
In the Heat of the Night     7,9
Arsenic and Old Lace         7,9
Before Sunrise               7,9
Papillon                     7,9
Name: Puan, Length: 247, dtype: object
```

## Çoklu Sütun Filtrelemek

**Birden fazla sütun filtrelemek** istediğimiz durumda, sütun isimlerini **liste** olarak (bildiğiniz gibi liste veri tipleri köşeli parantez ile temsil edilir) belirtmek/yazmak gerekir.

```python
print(imdb[["Yıl", "Puan"]])
```

| Film_Adı                 | Yıl  | Puan |
| ------------------------ | ---- | ---- |
| The Shawshank Redemption | 1994 | 9,2  |
| The Godfather            | 1972 | 9,2  |
| The Godfather: Part II   | 1974 | 9    |
| Pulp Fiction             | 1994 | 8,9  |
| The Dark Knight          | 2008 | 8,9  |
| ...                      | ...  | ...  |
| Mystic River             | 2003 | 7,9  |
| In the Heat of the Night | 1967 | 7,9  |
| Arsenic and Old Lace     | 1944 | 7,9  |
| Before Sunrise           | 1995 | 7,9  |
| Papillon                 | 1973 | 7,9  |

247 rows × 2 columns

Gördüğünüz gibi artık sadece **Yıl** ve **Puan** Sütunlarına ait verileri filtrelemiş olduk.
