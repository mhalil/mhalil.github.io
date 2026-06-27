Title: Pandas - fillna
Date: 2022-07-12 10:00
Modified: 2025-11-15 21:50
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Eksik, Kayıp, Veri, fillna
Author: Mustafa Halil

# fillna() Fonksiyonu

Veri Çerçevelerimizde eksik veri bulunması durumunda, her zaman satır ve sütunları silmeye çalışmayız. Bazen **eksik verilerin yerine, yeni değer atamamız** gerekebilir. Örneğin matematiksel işlemlerde, Pandas ile satır ya da sütunların ortalama değerlerini hesaplatıp, eksik verilerin yerine ( eksik veriyi, Excel programındaki boş hüçreler gibi 
düşünülebilir) yazdırabiliriz/atayabiliriz.

```python
DataFrame.fillna(value=None,
                method=None, 
                axis=None, 
                inplace=False, 
                limit=None, 
                downcast=<no_default>)
```

## value Parametresi

**value** parametresi, Eksik verilerin yerine istersek yazdırmak istediğimiz değerin belirtildiği kısımdır. **value** parametresine sayısal değer yazacağımız zaman doğrudan değerin kendisini, **metinsel (string)** ifadeler de yazacağımız zaman ise **tırnak işareti "** kullanmamız gerektiğini unutmamalıyız. Şimdiki örnekte, Veri çerçevemizdeki eksik verilerin yerine **Mustafa Halil** ismini yazdıracağım.

Eksik (NaN) Veri bulunan tablomuz:

|     | Film_Adı                                          | Yıl    | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ------ | ---- | ------------ |
| 0   | The Shawshank Redemption                          | 1994.0 | 9,2  | 1071904.0    |
| 1   | The Godfather                                     | 1972.0 | 9,2  | 751381.0     |
| 2   | The Godfather: Part II                            | 1974.0 | 9    | 488889.0     |
| 3   | Pulp Fiction                                      | 1994.0 | 8,9  | 830504.0     |
| 4   | The Dark Knight                                   | 2008.0 | 8,9  | 1045186.0    |
| 5   | 12 Angry Men                                      | 1957.0 | 8,9  | NaN          |
| 6   | Schindler's List                                  | 1993.0 | 8,9  | 545703.0     |
| 7   | The Lord of the Rings: The Return of the King     | 2003.0 | 8,8  | 758388.0     |
| 8   | Fight Club                                        | 1999.0 | 8,8  | 814389.0     |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980.0 | 8,8  | 519895.0     |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001.0 | 8,8  | 784999.0     |
| 11  | One Flew Over the Cuckoo's Nest                   | 1975.0 | 8,7  | 447005.0     |
| 12  | Goodfellas                                        | 1990.0 | 8,7  | 465445.0     |
| 13  | Seven Samurai                                     | NaN    | 8,7  | 161969.0     |
| 14  | Inception                                         | 2010.0 | 8,7  | 844938.0     |
| 15  | Star Wars                                         | 1977.0 | 8,7  | NaN          |
| 16  | Forrest Gump                                      | 1994.0 | 8,7  | 711386.0     |
| 17  | The Matrix                                        | 1999.0 | 8,7  | 770559.0     |
| 18  | The Lord of the Rings: The Two Towers             | 2002.0 | 8,7  | 680983.0     |

```python
print(veri.fillna(value = "Mustafa Halil"))
```

|     | Film_Adı                                          | Yıl           | Puan | Oylayan_Kişi  |
| --- | ------------------------------------------------- | ------------- | ---- | ------------- |
| 0   | The Shawshank Redemption                          | 1994.0        | 9,2  | 1071904.0     |
| 1   | The Godfather                                     | 1972.0        | 9,2  | 751381.0      |
| 2   | The Godfather: Part II                            | 1974.0        | 9    | 488889.0      |
| 3   | Pulp Fiction                                      | 1994.0        | 8,9  | 830504.0      |
| 4   | The Dark Knight                                   | 2008.0        | 8,9  | 1045186.0     |
| 5   | 12 Angry Men                                      | 1957.0        | 8,9  | Mustafa Halil |
| 6   | Schindler's List                                  | 1993.0        | 8,9  | 545703.0      |
| 7   | The Lord of the Rings: The Return of the King     | 2003.0        | 8,8  | 758388.0      |
| 8   | Fight Club                                        | 1999.0        | 8,8  | 814389.0      |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980.0        | 8,8  | 519895.0      |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001.0        | 8,8  | 784999.0      |
| 11  | One Flew Over the Cuckoo's Nest                   | 1975.0        | 8,7  | 447005.0      |
| 12  | Goodfellas                                        | 1990.0        | 8,7  | 465445.0      |
| 13  | Seven Samurai                                     | Mustafa Halil | 8,7  | 161969.0      |
| 14  | Inception                                         | 2010.0        | 8,7  | 844938.0      |
| 15  | Star Wars                                         | 1977.0        | 8,7  | Mustafa Halil |
| 16  | Forrest Gump                                      | 1994.0        | 8,7  | 711386.0      |
| 17  | The Matrix                                        | 1999.0        | 8,7  | 770559.0      |
| 18  | The Lord of the Rings: The Two Towers             | 2002.0        | 8,7  | 680983.0      |

Boş hücrelere yani eksik verilerin yerine, **Yıl** sütununun ortalama değerini (1885.0) atamak isteseydik (saçma bir atama işlemi olduğunun farkındayım :) ), aşağıdaki gibi kodlarımızı düzenlememiz gerekecekti.

```python
ortalama = int(veri["Yıl"].sum()/19)
print(veri.fillna(value=ortalama))
```

|     | Film_Adı                                          | Yıl    | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ------ | ---- | ------------ |
| 0   | The Shawshank Redemption                          | 1994.0 | 9,2  | 1071904.0    |
| 1   | The Godfather                                     | 1972.0 | 9,2  | 751381.0     |
| 2   | The Godfather: Part II                            | 1974.0 | 9    | 488889.0     |
| 3   | Pulp Fiction                                      | 1994.0 | 8,9  | 830504.0     |
| 4   | The Dark Knight                                   | 2008.0 | 8,9  | 1045186.0    |
| 5   | 12 Angry Men                                      | 1957.0 | 8,9  | 1885.0       |
| 6   | Schindler's List                                  | 1993.0 | 8,9  | 545703.0     |
| 7   | The Lord of the Rings: The Return of the King     | 2003.0 | 8,8  | 758388.0     |
| 8   | Fight Club                                        | 1999.0 | 8,8  | 814389.0     |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980.0 | 8,8  | 519895.0     |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001.0 | 8,8  | 784999.0     |
| 11  | One Flew Over the Cuckoo's Nest                   | 1975.0 | 8,7  | 447005.0     |
| 12  | Goodfellas                                        | 1990.0 | 8,7  | 465445.0     |
| 13  | Seven Samurai                                     | 1885.0 | 8,7  | 161969.0     |
| 14  | Inception                                         | 2010.0 | 8,7  | 844938.0     |
| 15  | Star Wars                                         | 1977.0 | 8,7  | 1885.0       |
| 16  | Forrest Gump                                      | 1994.0 | 8,7  | 711386.0     |
| 17  | The Matrix                                        | 1999.0 | 8,7  | 770559.0     |
| 18  | The Lord of the Rings: The Two Towers             | 2002.0 | 8,7  | 680983.0     |

## method Parametresi

Veri çerçevesinde değer girilmemiş hücreleri (boşlukları) doldurmak, başka bir ifadeyle, değer atamak için `method` parametresi kullanılabilir.

`method` parametresinin alabileceği değerler;

- **backfill**
- **bfill**
- **pad**
- **ffill**
- **None**
  Varsayılan (öntanımlı) değer None'dır.

Öncelikle Veri çerçevesi oluşturup inceleyelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici"],
                     "kategori" : ["Kategori_1", None, "Kategori_3", "Kategori_4", "Kategori_5", None, None, "Kategori_8", "Kategori_9", None]}
veri = pd.DataFrame(sozluk)
veri
```

|     | isim       | yaş | iş-meslek   | kategori   |
| --- | ---------- | --- | ----------- | ---------- |
| 0   | Mustafa    | 25  | mühendis    | Kategori_1 |
| 1   | Halil      | 38  | programcı   | None       |
| 2   | Burak      | 41  | akademisyen | Kategori_3 |
| 3   | Emre       | 23  | yönetici    | Kategori_4 |
| 4   | Ersin      | 37  | amir        | Kategori_5 |
| 5   | Sertaç     | 52  | mühendis    | None       |
| 6   | Furkan     | 30  | yönetici    | None       |
| 7   | Murat      | 23  | müdür       | Kategori_8 |
| 8   | Ahmet      | 40  | veteriner   | Kategori_9 |
| 9   | Abdülkadir | 38  | yönetici    | None       |

Veri çerçevesini incelediğimzde, Halil, Sertaç, Furkan ve Ahmet'in **kategori** bilgilerinin, geçerli değere sahip olmadığını görüyoruz. Bu değerleri `method` parametresinin seçeneklerini kullanarak doldurmaya çalışalım.

### backfill ve bfill

Öncelikle **backfill** ve **bfill** seçeneklerini inceleyelim.

```python
veri = veri.fillna(method="backfill")
print(veri)
```

|     | isim       | yaş | iş-meslek   | kategori   |
| --- | ---------- | --- | ----------- | ---------- |
| 0   | Mustafa    | 25  | mühendis    | Kategori_1 |
| 1   | Halil      | 38  | programcı   | Kategori_3 |
| 2   | Burak      | 41  | akademisyen | Kategori_3 |
| 3   | Emre       | 23  | yönetici    | Kategori_4 |
| 4   | Ersin      | 37  | amir        | Kategori_5 |
| 5   | Sertaç     | 52  | mühendis    | Kategori_8 |
| 6   | Furkan     | 30  | yönetici    | Kategori_8 |
| 7   | Murat      | 23  | müdür       | Kategori_8 |
| 8   | Ahmet      | 40  | veteriner   | Kategori_9 |
| 9   | Abdülkadir | 38  | yönetici    | None       |

```python
veri = veri.fillna(method="bfill")
print(veri)
```

|     | isim       | yaş | iş-meslek   | kategori   |
| --- | ---------- | --- | ----------- | ---------- |
| 0   | Mustafa    | 25  | mühendis    | Kategori_1 |
| 1   | Halil      | 38  | programcı   | Kategori_3 |
| 2   | Burak      | 41  | akademisyen | Kategori_3 |
| 3   | Emre       | 23  | yönetici    | Kategori_4 |
| 4   | Ersin      | 37  | amir        | Kategori_5 |
| 5   | Sertaç     | 52  | mühendis    | Kategori_8 |
| 6   | Furkan     | 30  | yönetici    | Kategori_8 |
| 7   | Murat      | 23  | müdür       | Kategori_8 |
| 8   | Ahmet      | 40  | veteriner   | Kategori_9 |
| 9   | Abdülkadir | 38  | yönetici    | None       |

Görüldüğü üzere, **backfill** ve **bfill** seçenekleri sayesinde boş (geçersiz değere sahip) hücreler, **kendinden sonraki** (altında bulunan) son geçerli  hücrenin değeri ile dolduruldu.

### pad ve ffill

Şimdi **pad** ve **ffill** seçeneklerini inceleyelim;

```python
veri = veri.fillna(method="pad")
print(veri)
```

|     | isim       | yaş | iş-meslek   | kategori   |
| --- | ---------- | --- | ----------- | ---------- |
| 0   | Mustafa    | 25  | mühendis    | Kategori_1 |
| 1   | Halil      | 38  | programcı   | Kategori_1 |
| 2   | Burak      | 41  | akademisyen | Kategori_3 |
| 3   | Emre       | 23  | yönetici    | Kategori_4 |
| 4   | Ersin      | 37  | amir        | Kategori_5 |
| 5   | Sertaç     | 52  | mühendis    | Kategori_5 |
| 6   | Furkan     | 30  | yönetici    | Kategori_5 |
| 7   | Murat      | 23  | müdür       | Kategori_8 |
| 8   | Ahmet      | 40  | veteriner   | Kategori_9 |
| 9   | Abdülkadir | 38  | yönetici    | Kategori_9 |

```python
veri = veri.fillna(method="ffill")
print(veri)
```

|     | isim       | yaş | iş-meslek   | kategori   |
| --- | ---------- | --- | ----------- | ---------- |
| 0   | Mustafa    | 25  | mühendis    | Kategori_1 |
| 1   | Halil      | 38  | programcı   | Kategori_1 |
| 2   | Burak      | 41  | akademisyen | Kategori_3 |
| 3   | Emre       | 23  | yönetici    | Kategori_4 |
| 4   | Ersin      | 37  | amir        | Kategori_5 |
| 5   | Sertaç     | 52  | mühendis    | Kategori_5 |
| 6   | Furkan     | 30  | yönetici    | Kategori_5 |
| 7   | Murat      | 23  | müdür       | Kategori_8 |
| 8   | Ahmet      | 40  | veteriner   | Kategori_9 |
| 9   | Abdülkadir | 38  | yönetici    | Kategori_9 |

**backfill** ve **bfill** seçeneklerinin tersine **pad** ve **ffill** seçenekleri ile sayesinde ise boş (geçersiz değere sahip) hücreler, **kendinden önceki** (üstünde bulunan) son geçerli  hücrenin değeri ile dolduruldu.
