Title: Pandas - sort_index
Date: 2022-07-15 00:00
Modified: 2025-06-23 23:11
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Sıralama, sort_index, ascending, axis
Author: Mustafa Halil

# Sıralama Yöntemleri

Oluşturulan Veri Çerçevelerinin, isteğimiz doğrultusunda sıralanması için kullanabileceğimiz yöntemlere, bu bölümde değineceğiz.

Pandas üç tür sıralamayı destekler ;

- İndeks (dizin) etiketlerine göre sıralama,
- Sütun değerlerine göre sıralama
- Her ikisinin birleşimine göre sıralama.

Konuya ait yöntemleri incelemek amacıyla **imdb.xlsx** dosyamızı içe aktararak bir veri çerçevesi oluşturarak işe başlayalım. Oluşturacağımız Veri çerçevesinin indeks değeri olarak **Film Adlarını** belirleyelim.

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

# sort_index() Fonksiyonu

`sort_index()` fonksiyonu (metodu), veri çerçevesini indeks (dizin) değerine göre **Alfabetik** olarak sıralama için kullanılır. **df** veri çerçevemizin indekslerini, **Film adı** olarak atadığımız için, `sort_index()` metodunu kullandığımız zaman, Veri çerçevemizi **Film Adı**na göre sıralamış olacağız.

```python
print(df.sort_index())
```

| Film_Adı                        | Yıl  | Puan | Oylayan_Kişi |
| ------------------------------- | ---- | ---- | ------------ |
| 12 Angry Men                    | 1957 | 8,9  | 264112       |
| 2001: A Space Odyssey           | 1968 | 8,3  | 275055       |
| 3 Idiots                        | 2009 | 8    | 83178        |
| 8½                              | 1963 | 8    | 54451        |
| A Beautiful Mind                | 2001 | 8    | 344294       |
| ...                             | ...  | ...  | ...          |
| Warrior                         | 2011 | 8,1  | 190877       |
| Who's Afraid of Virginia Woolf? | 1966 | 8    | 38192        |
| Wild Strawberries               | 1957 | 8,2  | 41744        |
| Witness for the Prosecution     | 1957 | 8,3  | 36241        |
| Yojimbo                         | 1961 | 8,3  | 49855        |

247 rows × 3 columns

# Parametreler

## ascending Parametresi

Sıralamayı ters çevirmek için `ascending=False` parametresini kullanabiliriz.

```python
print(df.sort_index(ascending=False))
```

| Film_Adı                        | Yıl  | Puan | Oylayan_Kişi |
| ------------------------------- | ---- | ---- | ------------ |
| Yojimbo                         | 1961 | 8,3  | 49855        |
| Witness for the Prosecution     | 1957 | 8,3  | 36241        |
| Wild Strawberries               | 1957 | 8,2  | 41744        |
| Who's Afraid of Virginia Woolf? | 1966 | 8    | 38192        |
| Warrior                         | 2011 | 8,1  | 190877       |
| ...                             | ...  | ...  | ...          |
| A Beautiful Mind                | 2001 | 8    | 344294       |
| 8½                              | 1963 | 8    | 54451        |
| 3 Idiots                        | 2009 | 8    | 83178        |
| 2001: A Space Odyssey           | 1968 | 8,3  | 275055       |
| 12 Angry Men                    | 1957 | 8,9  | 264112       |

247 rows × 3 columns

## axis Parametresi

Sütunlarda sıralama yapmak istersek `axis=1` parametresini kullanmamız gerekir. axis parametresinin varsayılan değeri 0 (sıfır) yani **satırlar**dır.

`df.sort_index(axis=1)` kodunu çalıştırdığımızda, **imdb.xlsx** dosyasını içeriği okunacak, satırlarda bir sıralama yapılmayacak ancak, **sütun isimleri** alfabetik olarak sıralanacaktır. Veri çerçevesi oluşturulurken dosya içeriğindeki **Film_Adı** Sütunu indeks olarak ayarlandığı için, `axis=1` parametresi ile sıralama yapıldığında bu sütun sabit kalacak, diğer sıralı sütun isimleri (**Yıl, Puan, Oylayan_Kişi**) ve sütun değerleri değişecektir (**Oylayan_Kişi, Puan, Yıl** olacak).

```python
print(df.sort_index(axis=1))
```

| Film_Adı                 | Oylayan_Kişi | Puan | Yıl  |
| ------------------------ | ------------ | ---- | ---- |
| The Shawshank Redemption | 1071904      | 9,2  | 1994 |
| The Godfather            | 751381       | 9,2  | 1972 |
| The Godfather: Part II   | 488889       | 9    | 1974 |
| Pulp Fiction             | 830504       | 8,9  | 1994 |
| The Dark Knight          | 1045186      | 8,9  | 2008 |
| ...                      | ...          | ...  | ...  |
| Mystic River             | 256159       | 7,9  | 2003 |
| In the Heat of the Night | 37081        | 7,9  | 1967 |
| Arsenic and Old Lace     | 45893        | 7,9  | 1944 |
| Before Sunrise           | 100974       | 7,9  | 1995 |
| Papillon                 | 62517        | 7,9  | 1973 |

247 rows × 3 columns
