Title: Pandas - head
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:20
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, head
Author: Mustafa Halil

# head() Fonksiyonu

**head()** fonksiyonunu, oluşturduğumuz ya da çalışmamıza dahil ettiğimiz (içe aktardığımız) Veri Çerçevelerinin ilk satırlarını görüntüleyerek, içerik hakkında bilgi edinmemizi sağlar. **Head** kelimesi Türkçede **Baş, Kafa** anlamına gelmektedir.

Öncelikle **Pandas** Kütüphanesini içe aktarıp, kodlama esnasında hızlı olması adına bu kütüphaneye **pd** adını atayalım;

```python
import pandas as pd
```

Basit bir Veri Çerçevesi (Data Frame) oluşturalım ve oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", 
                    "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen",
                    "yönetici","amir","mühendis", "yönetici","müdür",
                    "veteriner","yönetici"]}
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

# head() Fonksiyonunun Kullanımı

**head()** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.head())
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 1   | Halil   | 38  | programcı   |
| 2   | Burak   | 41  | akademisyen |
| 3   | Emre    | 23  | yönetici    |
| 4   | Ersin   | 37  | amir        |

**head()** fonksiyonunda parantez içine parametre olarak bir değer yazmazsak, veri çerçevesinin **ilk 5 (satır) değeri** görüntülenir. Değer belirtirsek belirttiğimiz değer kadar satır verisi görüntülenir.

```python
print(veri.head(3))
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 1   | Halil   | 38  | programcı   |
| 2   | Burak   | 41  | akademisyen |

İndex değerinin 2'de bitmesi sizi şaşırtmasın, pekçok programlama dilindi olduğu gibi Python programlama dilinde de, sayma sayıları sıfırdan başlar. Zaten tabloyu incelerseniz, tabloda 3 kullanıcıya ait (3 satır) veri olduğunu görürsünüz.
