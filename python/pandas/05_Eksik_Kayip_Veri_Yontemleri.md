Title: Pandas 05 - Eksik - Kayıp Veri Yöntemleri
Date: 2022-07-12 10:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Eksik, Kayıp, Veri
Author: Mustafa Halil

# Eksik / Kayıp Veri Tespiti ve Düzenleme Yöntemleri

Veri çerçevemizde eksik veri (excel tablosundaki boş hücre gibi düşünebiliriz) olup olmadığını, varsa kaç adet olduğunu tespit edebileceğimiz Pandas yöntemleri mevcuttur. Bunları incelemeye başlayalım.

### isnull() Fonksiyonu

Veri çerçevemizde eksik verileri **isnull()** fonksiyonu ile tespit edebiliriz. **isnull** ifadesini, **boş mu?, geçersiz mi?, kayıp/eksik mi?** sorusu olarak düşünebilirsiniz.
Hemen inceleyelim bakalım, acaba **IMDB** listemizde eksik veri var mı? varsa hangi sütunda ne kadar eksik veri var?

```python
import pandas as pd
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
Tabloya tek tek bakmak yerine, tüm sütunlardaki eksik/kayıp verileri python'a saydırıp, sonucu görüntüleyebiliriz.
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

**isnull().sum()** metodlarıyla, yeni veri çerçevemizdeki eksik verilerin bilgilerini görelim

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

**Yıl** sütununda 1, **Oylayan_Kişi** sütununda 2 adet eksik veri olduğu görünüyor. Eksik veri olan satır ve sütunları silmeye / temizlemeye çalışalım.

### dropna() Fonksiyonu

Veri çerçevelerinde istediğimiz satır ve sütunları **drop()** metodu yardımı ile nasıl silebildiğimizi  [burada](pandas-06-veri-duzenleme-yontemleri.html) anlatıyoruz.

Veri Çerçevelerinde eksik veri bulunan satır ve sütunları otomatik olarak silmek için **dropna()** metodunu kullanabiliriz. Metodun kullanım şekli aşağıdaki gibidir.

```python
VeriÇerçevesi_Adı.dropna(axis = 0 ya da 1, inplace = True ya da False)
```

#### axis Parametresi

Eksenleri tanımlayan parametredir. Sıfır (0) Satırları, Bir (1) Sütunları temsil eder. Varsayılan değer Sıfır(0) yani Satırlardır.

#### inplace Parametresi

Gerçekleştirilen silme işleminin veri çerçevesinde kalıcı ya da geçici olmasını ayarladığımız parametredir. **inplace = True** yazılırsa, yapılan işlem kalıcı hale gelecektir.

```python
print(veri.dropna())
```

|     | Film_Adı                                          | Yıl    | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ------ | ---- | ------------ |
| 0   | The Shawshank Redemption                          | 1994.0 | 9,2  | 1071904.0    |
| 1   | The Godfather                                     | 1972.0 | 9,2  | 751381.0     |
| 2   | The Godfather: Part II                            | 1974.0 | 9    | 488889.0     |
| 3   | Pulp Fiction                                      | 1994.0 | 8,9  | 830504.0     |
| 4   | The Dark Knight                                   | 2008.0 | 8,9  | 1045186.0    |
| 6   | Schindler's List                                  | 1993.0 | 8,9  | 545703.0     |
| 7   | The Lord of the Rings: The Return of the King     | 2003.0 | 8,8  | 758388.0     |
| 8   | Fight Club                                        | 1999.0 | 8,8  | 814389.0     |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980.0 | 8,8  | 519895.0     |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001.0 | 8,8  | 784999.0     |
| 11  | One Flew Over the Cuckoo's Nest                   | 1975.0 | 8,7  | 447005.0     |
| 12  | Goodfellas                                        | 1990.0 | 8,7  | 465445.0     |
| 14  | Inception                                         | 2010.0 | 8,7  | 844938.0     |
| 16  | Forrest Gump                                      | 1994.0 | 8,7  | 711386.0     |
| 17  | The Matrix                                        | 1999.0 | 8,7  | 770559.0     |
| 18  | The Lord of the Rings: The Two Towers             | 2002.0 | 8,7  | 680983.0     |

**dropna()** metodunu parametresiz olarak kullandığımızda ( *veri.dropna()* ), sadece eksik veri tespit edilen **satırlar** silindi. Bir de eksik veri bulunan sütunları silmeye çalışalım.

```python
print(veri.dropna(axis = 1))
```

|     | Film_Adı                                          | Puan |
| --- | ------------------------------------------------- | ---- |
| 0   | The Shawshank Redemption                          | 9,2  |
| 1   | The Godfather                                     | 9,2  |
| 2   | The Godfather: Part II                            | 9    |
| 3   | Pulp Fiction                                      | 8,9  |
| 4   | The Dark Knight                                   | 8,9  |
| 5   | 12 Angry Men                                      | 8,9  |
| 6   | Schindler's List                                  | 8,9  |
| 7   | The Lord of the Rings: The Return of the King     | 8,8  |
| 8   | Fight Club                                        | 8,8  |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 8,8  |
| 10  | The Lord of the Rings: The Fellowship of the R... | 8,8  |
| 11  | One Flew Over the Cuckoo's Nest                   | 8,7  |
| 12  | Goodfellas                                        | 8,7  |
| 13  | Seven Samurai                                     | 8,7  |
| 14  | Inception                                         | 8,7  |
| 15  | Star Wars                                         | 8,7  |
| 16  | Forrest Gump                                      | 8,7  |
| 17  | The Matrix                                        | 8,7  |
| 18  | The Lord of the Rings: The Two Towers             | 8,7  |

#### thresh Parametresi

**dropna()** Metodunun, **thresh** parametresi, veri çerçevesinde en az kaç adet veri varsa satır ya da sütunun silinmemesi gerektiğini belirtir. Bu parametreyi de hem satır hem de sütun için uygulayalım.

```python
print(veri.dropna(thresh=3))
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

**veri.dropna(thresh=3)**: Bu kod,en az 3 sağlam veri barındıran **satırları** silme demek oluyor. Aynı işlemi, **axis** parametresi kullanarak uygulamak istesek kodu şu şekilde yazmamız gerekecekti: ***veri.dropna(axis=0, thresh=3)***

Bir de en az 4 sağlam veri isteyelim bakalım ne sonuç alacağız. Veri çerçevemizde 4 adet sütun bulunduğu için, tümü geçerli, sağlam veri bulunan (dolu) sütunları bulmak istediğimiz anlamına geliyor.

```python
print(veri.dropna(thresh=4))
```

|     | Film_Adı                                          | Yıl    | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ------ | ---- | ------------ |
| 0   | The Shawshank Redemption                          | 1994.0 | 9,2  | 1071904.0    |
| 1   | The Godfather                                     | 1972.0 | 9,2  | 751381.0     |
| 2   | The Godfather: Part II                            | 1974.0 | 9    | 488889.0     |
| 3   | Pulp Fiction                                      | 1994.0 | 8,9  | 830504.0     |
| 4   | The Dark Knight                                   | 2008.0 | 8,9  | 1045186.0    |
| 6   | Schindler's List                                  | 1993.0 | 8,9  | 545703.0     |
| 7   | The Lord of the Rings: The Return of the King     | 2003.0 | 8,8  | 758388.0     |
| 8   | Fight Club                                        | 1999.0 | 8,8  | 814389.0     |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980.0 | 8,8  | 519895.0     |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001.0 | 8,8  | 784999.0     |
| 11  | One Flew Over the Cuckoo's Nest                   | 1975.0 | 8,7  | 447005.0     |
| 12  | Goodfellas                                        | 1990.0 | 8,7  | 465445.0     |
| 14  | Inception                                         | 2010.0 | 8,7  | 844938.0     |
| 16  | Forrest Gump                                      | 1994.0 | 8,7  | 711386.0     |
| 17  | The Matrix                                        | 1999.0 | 8,7  | 770559.0     |
| 18  | The Lord of the Rings: The Two Towers             | 2002.0 | 8,7  | 680983.0     |

Tahmin ettiğiniz gibi, her satırda 4 bilgi bulunan satırlar kaldı, geri kalan **satırlar** silindi.

Bu metodu bir de **sütunlarda** uygulayalım. Veri çerçevemizde 19 satır veri bulunmaktadır. En az 18 adet veri bulunan (yani sütünlarda en fazla 1 adet eksik veriye izin verdiğimiz durumdaki) sütunlar kalsın, geri kalanlar silinsin istersek;

```python
print(veri.dropna(axis=1, thresh=18))
```

|     | Film_Adı                                          | Yıl    | Puan |
| --- | ------------------------------------------------- | ------ | ---- |
| 0   | The Shawshank Redemption                          | 1994.0 | 9,2  |
| 1   | The Godfather                                     | 1972.0 | 9,2  |
| 2   | The Godfather: Part II                            | 1974.0 | 9    |
| 3   | Pulp Fiction                                      | 1994.0 | 8,9  |
| 4   | The Dark Knight                                   | 2008.0 | 8,9  |
| 5   | 12 Angry Men                                      | 1957.0 | 8,9  |
| 6   | Schindler's List                                  | 1993.0 | 8,9  |
| 7   | The Lord of the Rings: The Return of the King     | 2003.0 | 8,8  |
| 8   | Fight Club                                        | 1999.0 | 8,8  |
| 9   | Star Wars: Episode V - The Empire Strikes Back    | 1980.0 | 8,8  |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001.0 | 8,8  |
| 11  | One Flew Over the Cuckoo's Nest                   | 1975.0 | 8,7  |
| 12  | Goodfellas                                        | 1990.0 | 8,7  |
| 13  | Seven Samurai                                     | NaN    | 8,7  |
| 14  | Inception                                         | 2010.0 | 8,7  |
| 15  | Star Wars                                         | 1977.0 | 8,7  |
| 16  | Forrest Gump                                      | 1994.0 | 8,7  |
| 17  | The Matrix                                        | 1999.0 | 8,7  |
| 18  | The Lord of the Rings: The Two Towers             | 2002.0 | 8,7  |

**Oylayan_Kişi** sütununda 2 adet eksik veri bulunduğu için o sütun silindi.

### fillna() Fonksiyonu

Veri Çerçevelerimizde eksik veri bulunması durumunda, her zaman satır ve sütunları silmeye çalışmayız. Bazen eksik verilerin yerine, yeni değer atamamız gerekebilir. Örneğin matematiksel işlemlerde, Pandas ile satır ya da sütunların ortalama değerlerini hesaplatıp, eksik verilerin yerine ( eksik veriyi, Excel programındaki boş hüçreler gibi 
düşünülebilir) yazdırabiliriz/atayabiliriz.

#### value Parametresi

**value** parametresi, Eksik verilerin yerine istersek yazdırmak istediğimiz değerin belirtildiği kısımdır. **value** parametresine sayısal değer yazacağımız zaman doğrudan değerin kendisini, **metinsel (string)** ifadeler de yazacağımız zaman ise **tırnak işareti "** kullanmamız gerektiğini unutmamalıyız. Şimdiki örnekte, Veri çerçevemizdeki eksik verilerin yerine **Mustafa Halil** ismini yazdıracağım.

```python
print(veri.fillna(value="Mustafa Halil"))
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

#### method Parametresi

Veri çerçevesinde değer girilmemiş hücreleri (boşlukları) doldurmak, başka bir ifadeyle, değer atamak için `method` parametresi kullanılabilir.

`method` parametresinin alabileceği değerler;

- backfill
- bfill
- pad
- ffill
- None
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

Şimdi sıra **pad** ve **ffill** seçeneklerinde;

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

[← Önceki Bölüm](pandas-04-secim-yontemleri.html) | [Sonraki Bölüm →](pandas-06-veri-duzenleme-yontemleri.html)
