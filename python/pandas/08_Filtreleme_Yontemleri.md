Title: Pandas 08 - Veri Filtreleme Yöntemleri
Date: 2022-07-16 00:00 
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre
Author: Mustafa Halil

# Filtreleme Yöntemleri

Pandas kütüphanesi ile en sık yapılan işlemlerden biri de Filtreleme işlemidir. Binlerce, onbinlerce hatta milyonlarca kayıt arasından istediğimize ulaşmak için filreleme komutlarını kullanacağız. Bu bölümdeki anlatılanları da dikkatle okuyup öğrenmenizi tavsiye ederim.

### Karşılaştırma Operatorü Kullanımı

Sütun içerisindeki verilere göre filtreleme uygulamak istersek,  `VeriCervecesiAdı["SütunAdı"] == "Filtre_Kriteri"` yöntemi kullanılabilir.

Pythonda kullanıdığımız **Karşılaştırma operatörlerini (< , > , <=, >=, ==, !=, )** ve **Mantıksal Operatörleri ( (and, ve) & ve (or, Ya da) |** Pandas içerisinde de kullanabiliriz.
Öncelikle veri çerçevemize göz atalım.

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

Örneğin 2010 yılına ait filmleri görmek istersen **Karşılaştırma operatörünü** kullanarak aşağıdaki filtreleme yöntemini kullanabiliriz.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", decimal=",")
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

8,8 ve üzeri Puana sahip filmleri listelemek istersek;

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

Karşılaştırma operatorlerini, Filtreleme işlemini dışında kıyaslama amacıyla da kullanabiliriz. Aşağıdaki kullanımı inceleyelim.

```python
Mantiksal_imdb = imdb["Puan"] > 8
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

Bu durumda, **Puan** sütunundaki değerler, verilen kritere göre (8'den büyük olup olmadığı) sorgulanıyor ve her değer için **True** (Doğru) yani değer 8'den büyük ya da **False** (yanlış) yani değer 8'e eşit ya da küçük sonucu vdöndürüyor.

### between() Fonksiyonu

Bir sayısal aralık belirterek filtreleme yapmak istersek **between()** metodunu kullanabiliriz.
Örneği **1960** ile **1980** yılları arasındaki filmleri filtrelemeye çalışalım.

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

### Mantıksal Operatör Kullanımı

Birden fazla kriter içeren filtreleme işlemi uygulamak istersek, aşağıdaki kodlar ile istediğimiz elde edebiliriz.
İki kriteri bir arada kullanmak istediğimizde **VE (and)** simgesi olan **&**, İki kriterden birini ayrı ayrı seçmek için **YA DA (or)** simgesi olan **|** kullanılır. **and** ve **or** kelimelerini kullanırsanız hata alırsınız.

```python
yıl_2000den_buyuk = imdb["Yıl"] > 2000
Oylayan_Kişi_500000 = imdb["Oylayan_Kişi"] > 500000
print(imdb[yıl_2000den_buyuk & Oylayan_Kişi_500000])
```

|     | Film_Adı                                          | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ---- | ---- | ------------ |
| 4   | The Dark Knight                                   | 2008 | 8.9  | 1045186      |
| 7   | The Lord of the Rings: The Return of the King     | 2003 | 8.8  | 758388       |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001 | 8.8  | 784999       |
| 14  | Inception                                         | 2010 | 8.7  | 844938       |
| 18  | The Lord of the Rings: The Two Towers             | 2002 | 8.7  | 680983       |
| 49  | The Departed                                      | 2006 | 8.4  | 540726       |
| 56  | The Dark Knight Rises                             | 2012 | 8.4  | 672751       |
| 105 | Batman Begins                                     | 2005 | 8.3  | 604923       |
| 107 | Inglourious Basterds                              | 2009 | 8.2  | 505702       |
| 162 | V for Vendetta                                    | 2005 | 8.1  | 507750       |
| 165 | The Avengers                                      | 2012 | 8.1  | 568037       |
| 216 | Pirates of the Caribbean: The Curse of the Bla... | 2003 | 8.0  | 519625       |

```python
yıl_2000den_buyuk = imdb["Yıl"] > 2000
Oylayan_Kişi_500000 = imdb["Oylayan_Kişi"] > 500000
print(imdb[yıl_2000den_buyuk | Oylayan_Kişi_500000])
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| 6   | Schindler's List         | 1993 | 8.9  | 545703       |
| ... | ...                      | ...  | ...  | ...          |
| 231 | Shutter Island           | 2010 | 8.0  | 436151       |
| 233 | Incendies                | 2010 | 8.0  | 36751        |
| 236 | 3 Idiots                 | 2009 | 8.0  | 83178        |
| 237 | The Artist               | 2011 | 8.0  | 132672       |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |

81 rows × 4 columns

Filtreleme esnasında **String** Metotlarını kullanmak için **str** kelimesinden yararlanıyoruz. Diyelim ki içerisinde **star wars** kelime grubu bulunan tüm filmleri filtrelemek istiyoruz. Python küçük harf ve büyük harfe duyarlı olduğu için, **star wars** yazıp aradığımız zaman **Star Wars**, **STAR WARS** ,...vb hiçbir film, filtreye takılmayacak ve yanlış sonuç almış olacağız. Bu durumun önüne geçmek için, öncelikle tüm film isimlerini küçük harfe ya da büyük harfe çevirerek arama/filtreleme yapmamız gerekecektir.
Aşama aşama gidelim.
Tüm film isimlerini küçük harfe çevirelim. Film isimleri indeks olarak ayarlandığı için film isimleri sütununu temsilen, **index** kelimesini kullanmalıyız.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
kucuk_harf = imdb.index.str.lower()
print(kucuk_harf)
```

```python
Index(['the shawshank redemption ', 'the godfather ',
       'the godfather: part ii ', 'pulp fiction', 'the dark knight ',
       '12 angry men ', 'schindler's list ',
       'the lord of the rings: the return of the king ', 'fight club ',
       'star wars: episode v - the empire strikes back ',
       ...
       'the artist ', 'nausicaä of the valley of the wind ',
       'beauty and the beast ', 'three colors: red ', 'bringing up baby ',
       'mystic river ', 'in the heat of the night ', 'arsenic and old lace ',
       'before sunrise ', 'papillon '],
      dtype='object', name='Film_Adı', length=247)
```

Gördüğünüz gibi film isimleri tamamen küçük harfe dönüşmüş oldu. **String** metotlarından biri olan **contains** ile metin içerisinde **içeren** kelime ya da kelimeleri aratabiliyoruz. Şimdi Sıra geldi filtreleme işlemine.

```python
star_wars_icerir = kucuk_harf.str.contains("star wars")
print(imdb[star_wars_icerir])
```

| Film_Adı                                       | Yıl  | Puan | Oylayan_Kişi |
| ---------------------------------------------- | ---- | ---- | ------------ |
| Star Wars: Episode V - The Empire Strikes Back | 1980 | 8,8  | 519895       |
| Star Wars                                      | 1977 | 8,7  | 585132       |
| Star Wars: Episode VI - Return of the Jedi     | 1983 | 8,3  | 410111       |

Biraz karışık gelse de tüm kodları irleştirip aynı sonucu elde edebiliriz.

```python
star_wars_filtrele = imdb.index.str.lower().str.contains("star wars")
print(imdb[star_wars_filtrele])
```

| Film_Adı                                       | Yıl  | Puan | Oylayan_Kişi |
| ---------------------------------------------- | ---- | ---- | ------------ |
| Star Wars: Episode V - The Empire Strikes Back | 1980 | 8,8  | 519895       |
| Star Wars                                      | 1977 | 8,7  | 585132       |
| Star Wars: Episode VI - Return of the Jedi     | 1983 | 8,3  | 410111       |

[← Önceki Bölüm](pandas-07-veri-siralama-yontemleri.html) | [Sonraki Bölüm →](pandas-09-veri-gruplama-yontemleri.html)
