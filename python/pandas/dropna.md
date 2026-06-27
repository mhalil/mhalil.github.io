Title: Pandas - dropna
Date: 2022-07-12 10:00
Modified: 2025-06-22 12:23
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Eksik, Kayıp, Veri, dropna
Author: Mustafa Halil

# dropna() Fonksiyonu

Veri Çerçevelerinde **eksik veri bulunan satır ve sütunları otomatik olarak silmek** için **dropna()** metodunu kullanabiliriz. Metodun kullanım şekli aşağıdaki gibidir.

```python
VeriÇerçevesi_Adı.dropna(axis = 0 ya da 1, inplace = True ya da False)
```

## axis Parametresi

Eksenleri tanımlayan parametredir. 

* Sıfır (0) Satırları, 

* Bir (1) Sütunları 
  
  temsil eder. Varsayılan değer Sıfır(0) yani Satırlardır.

## inplace Parametresi

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

**dropna()** metodunu parametresiz olarak kullandığımızda ( `veri.dropna()`), sadece eksik veri tespit edilen **satırlar** silindi. Bir de eksik veri bulunan sütunları silmeye çalışalım.

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

## thresh Parametresi

**dropna()** Metodunun, **thresh** parametresi, veri çerçevesinde **en az kaç adet veri varsa satır ya da sütunun silinmemesi gerektiğini** belirtir. Bu parametreyi de hem satır hem de sütun için uygulayalım.

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

**veri.dropna(thresh=3)**: Bu kod, en az 3 sağlam veri barındıran **satırları** silme demek oluyor. Aynı işlemi, **axis** parametresi kullanarak uygulamak istesek kodu şu şekilde yazmamız gerekecekti: `veri.dropna(axis=0, thresh=3)`

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
