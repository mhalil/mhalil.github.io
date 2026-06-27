Title: Pandas - isnull
Date: 2022-07-10 20:40
Modified: 2025-11-15 21:45
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, isnull
Author: Mustafa Halil

# `isnull()` Metodu

Veri çerçevesinde boş, eksik, kayıp veri (excel tablosundaki boş hücre gibi düşünebiliriz) olup olmadığını `isnull()` metodu ile tespit edebiliriz. `isnull` ifadesini, **boş mu?, geçersiz mi?, kayıp/eksik mi?** sorusu olarak düşünebilirsiniz. Bu fonksiyonu çalıştırdığımızda veri çerçevesinin satır ve sütun başlıkları ekrana yazdırılır ancak veri yerine `True` ya da `False` bilgisi görüntülenir.

Öncelikle **Pandas** Kütüphanesini içe aktarıp, kodlama esnasında hızlı olması adına bu kütüphaneye **pd** adını atayalım;

```python
import pandas as pd
```

Basit bir Veri Çerçevesi (Data Frame) oluşturalım ve oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"], 
                    "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
                    "iş-meslek" : ["mühendis", "programcı", "akademisyen","yönetici","amir","mühendis","yönetici","müdür","veteriner","yönetici"]}

veri = pd.DataFrame(sozluk)
print(veri)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | Halil      | 38  | programcı   |
| 2   | Burak      | 41  | akademisyen |
| 3   | Emre       | 23  | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 23  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

# isnull() Fonksiyonunun Kullanımı

**isnull()** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.isnull())
```

|     | isim  | yaş   | iş-meslek |
| --- | ----- | ----- | --------- |
| 0   | False | False | False     |
| 1   | False | False | False     |
| 2   | False | False | False     |
| 3   | False | False | False     |
| 4   | False | False | False     |
| 5   | False | False | False     |
| 6   | False | False | False     |
| 7   | False | False | False     |
| 8   | False | False | False     |
| 9   | False | False | False     |

## any() Fonksiyonu

**isnull()** fonksiyonuna **any()** Fonksiyonunu da eklersek, veri çerçevesi tümüyle görüntülenmez sadece veri çerçevesi başlıkları ve bu başlıklarda (sütunlarda) eksik/kayıp veri bulunup bulunmadığı bilgisi görüntülenir.

```python
print(veri.isnull().any())
```

```python
isim         False
yaş          False
iş-meslek    False
dtype: bool
```

Görüyoruz ki, veri çerçevemizde hiç eksik/kayıp veri bulunmamaktadır.
 Yukarıdaki sözlük yapısında bazı verileri boş bırakarak yeni bir veri çerçevesi oluşturalım ve **isnull()** fonksiyonunu çalıştırıp sonuçları inceleyelim.

```python
sozluk_2 = {"isim" : ["Mustafa", pd.NaT, "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 38, 41, pd.NaT, 37, 52, 30, 23, 40,  pd.NaT],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici"]}
veri_2 = pd.DataFrame(sozluk_2)
print(veri_2)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | NaT        | 38  | programcı   |
| 2   | Burak      | 41  | akademisyen |
| 3   | Emre       | NaT | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 23  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | NaT | yönetici    |

**1** nolu İndeksteki **isim**, **3** nolu ve **9** nolu İndekslerdeki **yaş** bilgilerin boş olduğunu görüyoruz.

```python
print(veri_2.isnull())
```

|     | isim  | yaş   | iş-meslek |
| --- | ----- | ----- | --------- |
| 0   | False | False | False     |
| 1   | True  | False | False     |
| 2   | False | False | False     |
| 3   | False | True  | False     |
| 4   | False | False | False     |
| 5   | False | False | False     |
| 6   | False | False | False     |
| 7   | False | False | False     |
| 8   | False | False | False     |
| 9   | False | True  | False     |

**1** nolu İndeksteki **isim**, **3** nolu ve **9** nolu İndekslerdeki **yaş** bilgileri **eksik** olduğu için bu değerler **True**, diğer hücrelerde ise eksik veri olmadığı için **False** değeri ile gösterilmektedir.  
Sütun bazlı eksik/kayıp veri olup olmadığını incelersek;

```python
print(veri_2.isnull().any())
```

```python
isim          True
yaş           True
iş-meslek    False
dtype: bool
```

Çıktıdan anlıyoruz ki;

- **isim** ve **yaş** sütunlarında Eksik veri bulunuyor
- **iş-meslek** sütununda hiç eksik veri bulunmuyor.

Bir bakşa örneği daha inceleyelim, **IMDB** listemizde eksik veri var mı? varsa hangi sütunda ne kadar eksik veri var?
**Verimiz**;

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

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx")
print(imdb.isnull())
```

|     | Film_Adı | Yıl   | Puan  | Oylayan_Kişi |
| --- | -------- | ----- | ----- | ------------ |
| 0   | False    | False | False | False        |
| 1   | False    | False | False | False        |
| 2   | False    | False | False | False        |
| 3   | False    | False | False | False        |
| 4   | False    | False | False | False        |
| ... | ...      | ...   | ...   | ...          |
| 242 | False    | False | False | False        |
| 243 | False    | False | False | False        |
| 244 | False    | False | False | False        |
| 245 | False    | False | False | False        |
| 246 | False    | False | False | False        |

247 rows × 4 columns

Görüldüğü üzere, bu fonksiyon, veri çerçevesindeki her hücreye, kayıp/eksik veri olup olmadığı verisini yazıyor. **False** Yanlış, yani Eksik/Kayıp veri **YOK**, **True** ise Doğru yan, Eksik/Kayıp veri **VAR** anlamına gelir.

## sum() Fonksiyonu

Yukarıdaki **imdb** tablosuna tek tek bakmak yerine, tüm sütunlardaki eksik/kayıp verileri python'a saydırıp, sonucu görüntüleyebiliriz.
Python'da aşina olduğumuz **sum()** fonksiyonu işimize yarayacaktır.

```python
print(imdb.isnull().sum())
```

```python
Film_Adı        0
Yıl             0
Puan            0
Oylayan_Kişi    0
dtype: int64
```

Gördüğümüz kadarıyla tüm sonuçlar sıfır, yani veri çerçevemizde hiç eksik/kayıp veri bulunmamaktadır.

İçerisinde Kayıp/Eksik veri olan bir **Calc** tablosunu, veri çerçevesine dönüştürerek inceleyelim.

```python
veri = pd.read_excel("Veri_Setleri/eksik_veri.ods")
print(veri)
```

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

`isnull().sum()` metodlarıyla, yeni veri çerçevemizdeki eksik verilerin bilgilerini görelim

```python
print(veri.isnull().sum())
```

```python
Film_Adı        0
Yıl             1
Puan            0
Oylayan_Kişi    2
dtype: int64
```

**Yıl** sütununda 1, **Oylayan_Kişi** sütununda 2 adet eksik veri olduğu görünüyor. 
