Title: Pandas - drop_duplicates
Date: 2022-07-15 00:00
Modified: 2025-06-22 13:14
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, drop_duplicates
Author: Mustafa Halil

# drop_duplicates() Fonksiyonu

Veri çerçevemizde **çift kayıt varsa**, yani tüm veriler aynı olan birden fazla satır verisi varsa, bunlardan **biri kalacak şekilde diğerlerinin silmek** için `drop_duplicates` fonksiyonunu kullanabiliriz.

Örnek kodları inceleyelim.

```python
import pandas as pd
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir", "Halil", "Ersin"],
                    "yaş" : [25, 42, 43, 23, 37, 52, 30, 38, 40, 38, 42, 37],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici", "programcı", "amir"]}
veri = pd.DataFrame(sozluk)
print(veri)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | Halil      | 42  | programcı   |
| 2   | Burak      | 43  | akademisyen |
| 3   | Emre       | 23  | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 38  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |
| 10  | Halil      | 42  | programcı   |
| 11  | Ersin      | 37  | amir        |

Veri çerçevemizi incelediğimizde 1. ve 10. indeksli satırlardaki ile 4. ve 11. indeksli satırlardaki verilerin aynı olduğunu görüyoruz. Bu fazla verilerden kurtulalım.

```python
print(veri.drop_duplicates())
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | Halil      | 42  | programcı   |
| 2   | Burak      | 43  | akademisyen |
| 3   | Emre       | 23  | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 38  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

# Parametreler

## subset Parametresi

Veri çerçevesinde, tüm satır verisi aynı olmasa da, **sadece belirtilen sütunda aynı değere sahip verilerden birinin kalıp** diğerlerinin silinmesini istersek kullanmamız gereken parametre, **subset**'tir.

**subset** parametresine sütun ismi ya da isimleri yazarken liste veri tipinde giriş yapmak gerekir, yani sütun isimlerini köşeli parantez içerisinde yazmalıyız.

```python
import pandas as pd
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 42, 43, 23, 37, 52, 30, 25, 40, 38],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici"]}
veri = pd.DataFrame(sozluk)
print(veri)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | Halil      | 42  | programcı   |
| 2   | Burak      | 43  | akademisyen |
| 3   | Emre       | 23  | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 25  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

Görüldüğü üzre, veri çerçevemizde birebir aynı satır verileri bulunmuyor ancak aynı meslek grubuna sahip kayıtlar mecvut. Diyelim ki her meslek grubundan bir kişi kalacak, diğer veriler silinecek şekilde bir işlem yapmak istiyoruz. Bu durumda aşağıdaki kdu alıştırmamız gerekir.

```python
print(veri.drop_duplicates(subset=["iş-meslek"]))
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 1   | Halil   | 42  | programcı   |
| 2   | Burak   | 43  | akademisyen |
| 3   | Emre    | 23  | yönetici    |
| 4   | Ersin   | 37  | amir        |
| 7   | Murat   | 25  | müdür       |
| 8   | Ahmet   | 40  | veteriner   |

İndeks verilerine bakarsanız, 5. , 6. ve 9. satırlardaki verilerin silindiğini göreceksiniz. Bunun sebebi, 5. satırda **iş-meslek** sütununda yazan ifadenin, daha üst satırlarda var olması sebebiyle silinmesidir.

## keep Parametresi

Çift olan verilerden İlki mi? sonuncu mu kalacak, hangisinin silineceğine pandas nasıl karar verecek derseniz, onun için de **keep** parametresini kullanmamız gerekecek.

**keep** parametresine **last** değeri atanırsa, bu kez çift verilerden sonuncusu kalacak ve ilk veriler silinecektir.

Örnek kodu inceleyelim.

```python
print(veri.drop_duplicates(subset=["iş-meslek"], keep="last"))
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 1   | Halil      | 42  | programcı   |
| 2   | Burak      | 43  | akademisyen |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 7   | Murat      | 25  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

Görüldüğü gibi, bu kez "iş-meslek" sütununda ilk veriler olan 0. , 3. ve 6. satırlar silindi.
