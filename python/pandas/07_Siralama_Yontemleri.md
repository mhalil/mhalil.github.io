Title: Pandas 07 - Veri Sıralama Yöntemleri
Date: 2022-07-15 00:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Sıralama
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

## sort_index() Fonksiyonu

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

### ascending Parametresi

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

### axis Parametresi

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

## sort_values() Fonksiyonu

Veri çerçevesini **sütun(lar)a göre** sıralamak istersek, `sort_values()` fonksiyonunu kullanmalıyız.

### by Parametresi

`sort_values()` fonksiyonu ile sütuna göre sıralama yapmak için `by` parametresi kullanılmalıdır. `by` parametresi, bir veya daha fazla sütunu belirtmek için kullanılabilir. 
Bu durumda sütun isimlerini köşeli parantez içinde yani bir **liste** olarak yazmalıyız. Fonksiyonu, örneklerle inceleyelim.

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

### ascending Parametresi

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

### na_position Parametresi

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

## reindex() Fonksiyonu

`reindex()`, Pandas'ta temel veri sıralama (hizalama) yöntemlerinden biridir. Bir veri çerçevesinin satır ya da sütunlarını yeniden sıralamak için kullanılan en yaygın yöntemdir. Prensip olarak, etiket sıralama mantığına dayanır. Bu işlem, indeks değerlerini ya da sütun isimlerini yeniden sıralamak ve verileri belirli bir eksen (Satır 
ya da sütun) boyunca belirli bir etiket kümesiyle eşleşecek şekilde uyarlamak anlamına gelir. Bu fonksiyon, **hem seçim hem de sıralama** mantığıyla çalışır. Bu yöntemle şunlar sağlanır ;

- Mevcut verileri, Yeni bir etiket kümesiyle eşleştirerek yeniden sıralar
- Etiket kümesinde eşleşen verinin bulunmaması durumunda, etiket konumlarına eksik değer (NA / NaN) işaretçileri ekler
- Belirtilmişse, mantık kullanarak eksik etiketler için verileri 
  doldurur (fill). (zaman serisi verileriyle çalışanlar için oldukça 
  alakalıdır)

**df** veri çerçevemizin ilk 15 verisini inceleyelim.

```python
import pandas as pd
df = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
print(df.head(15))
```

| Film_Adı                                          | Yıl  | Puan | Oylayan_Kişi |
| ------------------------------------------------- | ---- | ---- | ------------ |
| The Shawshank Redemption                          | 1994 | 9,2  | 1071904      |
| The Godfather                                     | 1972 | 9,2  | 751381       |
| The Godfather: Part II                            | 1974 | 9    | 488889       |
| Pulp Fiction                                      | 1994 | 8,9  | 830504       |
| The Dark Knight                                   | 2008 | 8,9  | 1045186      |
| 12 Angry Men                                      | 1957 | 8,9  | 264112       |
| Schindler's List                                  | 1993 | 8,9  | 545703       |
| The Lord of the Rings: The Return of the King     | 2003 | 8,8  | 758388       |
| Fight Club                                        | 1999 | 8,8  | 814389       |
| Star Wars: Episode V - The Empire Strikes Back    | 1980 | 8,8  | 519895       |
| The Lord of the Rings: The Fellowship of the Ring | 2001 | 8,8  | 784999       |
| One Flew Over the Cuckoo's Nest                   | 1975 | 8,7  | 447005       |
| Goodfellas                                        | 1990 | 8,7  | 465445       |
| Seven Samurai                                     | 1954 | 8,7  | 161969       |
| Inception                                         | 2010 | 8,7  | 844938       |

Hem seçim hem de sıralama mantığı ile çalışan bu fonksiyon ile **Fight Club, Pulp Fiction, Inception, The Godfather, The Dark Knight** ve **Seven Samurai** filmlerini, yazdığımız sıra ile **sirala_filtrele** isimli yeni bir Veri Çerçevesine atayalım.

```python
sirala_filtrele = df.reindex(["Fight Club ", "Pulp Fiction", "Inception", "The Godfather ", "The Dark Knight ", "Seven Samurai "])
print(sirala_filtrele)
```

| Film_Adı        | Yıl  | Puan | Oylayan_Kişi |
| --------------- | ---- | ---- | ------------ |
| Fight Club      | 1999 | 8,8  | 814389       |
| Pulp Fiction    | 1994 | 8,9  | 830504       |
| Inception       | 2010 | 8,7  | 844938       |
| The Godfather   | 1972 | 9,2  | 751381       |
| The Dark Knight | 2008 | 8,9  | 1045186      |
| Seven Samurai   | 1954 | 8,7  | 161969       |

**df** veri çerçevemizde bulunmayan (eksik/kayıp veri) bir filmi **sirala_filtrele** veri çerçevemize eklemeye çalışırak ne olacağını görelim.

```python
sirala_filtrele = df.reindex(["Deli Yürek", "Fight Club ", "Pulp Fiction", "Inception", "The Godfather ", "The Dark Knight ", "Seven Samurai "])
print(sirala_filtrele)
```

| Film_Adı        | Yıl    | Puan | Oylayan_Kişi |
| --------------- | ------ | ---- | ------------ |
| Deli Yürek      | NaN    | NaN  | NaN          |
| Fight Club      | 1999.0 | 8,8  | 814389.0     |
| Pulp Fiction    | 1994.0 | 8,9  | 830504.0     |
| Inception       | 2010.0 | 8,7  | 844938.0     |
| The Godfather   | 1972.0 | 9,2  | 751381.0     |
| The Dark Knight | 2008.0 | 8,9  | 1045186.0    |
| Seven Samurai   | 1954.0 | 8,7  | 161969.0     |

Gördüğünüz gibi, **df** veri çerçevemizde **Deli Yürek** isimli bir filmi bulunmadığı için, **sirala_filtrele** veri çerçevemize sadece **Filmin Adı** eklendi, **Yıl, Puan** ve **Oylayan_Kişi** bilgileri yerine **NaN** değeri atandı.

### columns Parametresi

**df** veri çerçevemizin sütun isimleri **Yıl, Puan** ve **Oylayan_Kişi** sırası ile görüntüleniyor. Bu sırayı `reindex()` fonksiyonu yardımı ile değiştirmek istersek, `columns` parametresini kullanabiliriz. **sirala_filtrele** isimli veri çerçevemizin sütunlarını **Puan, Yıl, Oylayan_Kişi** sırasına göre hizalamaya çalışalım.

```python
print(sirala_filtrele.reindex(columns=["Puan", "Yıl", "Oylayan_Kişi"]))
```

| Film_Adı        | Puan | Yıl    | Oylayan_Kişi |
| --------------- | ---- | ------ | ------------ |
| Deli Yürek      | NaN  | NaN    | NaN          |
| Fight Club      | 8,8  | 1999.0 | 814389.0     |
| Pulp Fiction    | 8,9  | 1994.0 | 830504.0     |
| Inception       | 8,7  | 2010.0 | 844938.0     |
| The Godfather   | 9,2  | 1972.0 | 751381.0     |
| The Dark Knight | 8,9  | 2008.0 | 1045186.0    |
| Seven Samurai   | 8,7  | 1954.0 | 161969.0     |

`reindex()` fonksiyonunu, **Dilimleme** ve **Filtreleme** işlemi olarak ta kullanabiliriz. **df** veri çerçevemizdeki **Seven Samurai, Fight Club** ve **Inception** isimli filmlere ait sadece **Yıl** ve **Puan** bilgilerini elde etmek istersek `reindex()` fonksiyonu ile birlikte `index` ve `columns` parametrelerini kullanmalıyız.

```python
print(df.reindex(index=["Seven Samurai ", "Fight Club ", "Inception"], columns=["Yıl", "Puan"]))
```

| Film_Adı      | Yıl  | Puan |
| ------------- | ---- | ---- |
| Seven Samurai | 1954 | 8,7  |
| Fight Club    | 1999 | 8,8  |
| Inception     | 2010 | 8,7  |

### axis parametresi

Veri çerçevenizin indeks değerlerini (satırlar) ya da sütun isimlerini/değerlerini `reindex()` fonksiyonun, `axis` parametresi ile de sıralayabilirsiniz.

İndeks değerleri ve Sütun isimleri **0, 1** ve **2** olan bir veri çerçevesi oluşturup göz atalım.

```python
bir = [1,2,3], [40,50,60], [700,800,900]
sutun = [0,1,2]

df_1 = pd.DataFrame(bir, columns=sutun)
print(df_1)
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   | 1   | 2   | 3   |
| 1   | 40  | 50  | 60  |
| 2   | 700 | 800 | 900 |

#### index Seçeneği

İndeks değerlerini **2, 1** ve **0** olacak şekilde sıralamak için `axis="index"` parametre seçeneğini kullanmalıyız.

```python
print(df_1.reindex([2,1,0], axis="index"))
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 2   | 700 | 800 | 900 |
| 1   | 40  | 50  | 60  |
| 0   | 1   | 2   | 3   |

#### columns Seçeneği

İndeks değerlerini **2, 1** ve **0** olacak şekilde sıralamak için `axis="columns"` parametre seçeneğini kullanmalıyız.

```python
print(df_1.reindex([2,1,0], axis="columns"))
```

|     | 2   | 1   | 0   |
| --- | --- | --- | --- |
| 0   | 3   | 2   | 1   |
| 1   | 60  | 50  | 40  |
| 2   | 900 | 800 | 700 |

### Ek Bilgi :

`reindex()` fonksiyonunu kullanırken, gerçek eksen etiketlerini (indeksleri) içeren `index` nesnelerinin, nesneler arasında paylaşılabileceğine dikkat edin!

Yani bir Seriniz (Series) ve Veri Çerçeveniz (Data Frame) varsa, bunların indeks değerlerini `reindex()` fonksiyonunda parametre olarak kullanabilirsiniz.

```python
iki = ["a","b","c"], ["aa","bb","cc"], ["aaa","bbb","ccc"]
sutun = [1,2,0]

df_2 = pd.DataFrame(iki, index=sutun, columns=sutun)
print(df_2)
```

|     | 1   | 2   | 0   |
| --- | --- | --- | --- |
| 1   | a   | b   | c   |
| 2   | aa  | bb  | cc  |
| 0   | aaa | bbb | ccc |

**df_2** veri çerçevesinde index ve Sütun isimleri **1,2,0** olarak atanmış. **df_1** veri çerçevesinde index ve Sütun isimleri ise **0,1,2** olarak atanmış.

**df_2**'nin indeks değerlerini (satır etiketini) `reindex()` fonksiyonu ile değiştirirken, yeni sıralamayı **df_1**'in indeks değerleri ile belirleyelim/eşleştirelim.

```python
print(df_2.reindex(df_1.index))
```

|     | 1   | 2   | 0   |
| --- | --- | --- | --- |
| 0   | aaa | bbb | ccc |
| 1   | a   | b   | c   |
| 2   | aa  | bb  | cc  |

**df_2**'nin Sütun isimlerini `reindex()` fonksiyonun `columns` parametresi ile değiştirirken, yeni sıralamayı **df_1**'in indeks değerleri ile belirleyelim/eşleştirelim.

```python
print(df_2.reindex(columns=df_1.index))
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 1   | c   | a   | b   |
| 2   | cc  | aa  | bb  |
| 0   | ccc | aaa | bbb |

### Karşılaştırma Operatörü Kullanımı

### is Operatorü

Veri Çerçevelerinin `index` değerleri , liste veri tipi olarak belirtildiği için, listeler arasında karşılaştırma operatörlerini kullanmak ta mümkündür.

Örneğin `df_1.index` değerlerinin `df_2.index` değerlerine eşit olup olmadığını denetleyelim;

```python
print(df_1.index is sirala_filtrele.index)
```

```python
False
```

### > Operatörü

Python'da kullandığımız `<, >, <=, >=, ==`, ...vb operatörleri, Pandas Veri çerçevelerinde de kullanabiliriz.

Örneğin, **df** veri çerçevemizden dilimleme yöntemi ile **sf** isimli bir veri çerçevesi oluşturalım. Ardından **df_1** veri çerçevesinin satır sayısının (`len(df_1.index)`) **sf** veri çerçevesinin satır sayısından (`len(sf.index)`) büyük olup olmadığını denetleyelim;

```python
sf = sirala_filtrele.reindex(columns=["Puan", "Yıl", "Oylayan_Kişi"])
print(sf)
```

| Film_Adı        | Puan | Yıl    | Oylayan_Kişi |
| --------------- | ---- | ------ | ------------ |
| Deli Yürek      | NaN  | NaN    | NaN          |
| Fight Club      | 8,8  | 1999.0 | 814389.0     |
| Pulp Fiction    | 8,9  | 1994.0 | 830504.0     |
| Inception       | 8,7  | 2010.0 | 844938.0     |
| The Godfather   | 9,2  | 1972.0 | 751381.0     |
| The Dark Knight | 8,9  | 2008.0 | 1045186.0    |
| Seven Samurai   | 8,7  | 1954.0 | 161969.0     |

```python
print(len(df_1.index) > len(sf.index))
```

```python
False
```

Benzer şekilde KÜÇÜKTÜR (<) operatörünün çıktısını da aşağıda görebilirsiniz;

```python
print(len(df_1.index) < len(sf.index))
```

```python
True
```

[← Önceki Bölüm](pandas-06-veri-duzenleme-yontemleri.html) | [Sonraki Bölüm →](pandas-08-veri-filtreleme-yontemleri.html)
