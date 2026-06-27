Title: Pandas - reindex
Date: 2022-07-15 00:00
Modified: 2025-06-23 23:52
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Sıralama, reindex, columns, index, axis
Author: Mustafa Halil

# reindex() Fonksiyonu

`reindex()` fonksiyonu, Pandas'ta temel veri sıralama (hizalama) yöntemlerinden biridir. Bir veri çerçevesinin satır ya da sütunlarını yeniden sıralamak için kullanılan en yaygın yöntemdir. Prensip olarak, etiket sıralama mantığına dayanır. Bu işlem, indeks değerlerini ya da sütun isimlerini yeniden sıralamak ve verileri belirli bir eksen (Satır 
ya da sütun) boyunca belirli bir etiket kümesiyle eşleşecek şekilde uyarlamak anlamına gelir. Bu fonksiyon, **hem seçim hem de sıralama** mantığıyla çalışır. Bu yöntemle şunlar sağlanır ;

- Mevcut verileri, Yeni bir etiket kümesiyle eşleştirerek yeniden sıralar
- Etiket kümesinde eşleşen verinin bulunmaması durumunda, etiket konumlarına eksik değer (NA / NaN) işaretçileri ekler
- Belirtilmişse, mantık kullanarak eksik etiketler için verileri doldurur (fill). (zaman serisi verileriyle çalışanlar için oldukça alakalıdır)

Fonksiyonu ve parametrelerini bir örnekle inceleyelim.  **df** veri çerçevemizin ilk 15 verisine göz atalım.

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
sirala_filtrele = df.reindex(["Deli Yürek", "Fight Club ", "Pulp Fiction",
                              "Inception", "The Godfather ", 
                              "The Dark Knight ", "Seven Samurai "])
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

# Parametreler

## columns Parametresi

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

## index parametresi

`reindex()` fonksiyonunu, **Dilimleme** ve **Filtreleme** işlemi olarak ta kullanabiliriz. **df** veri çerçevemizdeki **Seven Samurai, Fight Club** ve **Inception** isimli filmlere ait sadece **Yıl** ve **Puan** bilgilerini elde etmek istersek `reindex()` fonksiyonu ile birlikte `index` ve `columns` parametrelerini kullanmalıyız.

```python
print(df.reindex(index=["Seven Samurai ", "Fight Club ", "Inception"], 
                 columns=["Yıl", "Puan"]))
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

İndeks değerlerini **2, 1** ve **0** olacak şekilde (büyükten küçüğe doğru) sıralamak için `axis="index"` parametre seçeneğini kullanmalıyız.

```python
print(df_1.reindex([2,1,0], axis="index"))
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 2   | 700 | 800 | 900 |
| 1   | 40  | 50  | 60  |
| 0   | 1   | 2   | 3   |

#### columns Seçeneği

sütun değerlerini **2, 1** ve **0** olacak şekilde (büyükten küçüğe doğru) sıralamak için `axis="columns"` parametre seçeneğini kullanmalıyız.

```python
print(df_1.reindex([2,1,0], axis="columns"))
```

|     | 2   | 1   | 0   |
| --- | --- | --- | --- |
| 0   | 3   | 2   | 1   |
| 1   | 60  | 50  | 40  |
| 2   | 900 | 800 | 700 |

## Ek Bilgi :

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
