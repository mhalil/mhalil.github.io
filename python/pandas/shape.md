Title: Pandas - shape
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:32
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, describe, Fonksiyon, shape
Author: Mustafa Halil

# shape Fonksiyonu

**shape** fonksiyonu ile, Veri Çerçevesinin yapısını yani satır ve sütun bilgisini öğrenebiliriz.

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

Çıktı:

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

# shape Fonksiyonunun Kullanımı

**shape** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.shape)
```

Çıktı:

```python
(10, 3)
```

Çıktının **tuple (demet)** yapısı olduğuna dikkat edin. İhtiyacımız olduğunda Demet yapısında, indeks bilgilerine ulaşabiliriz. Örneğin aşağıdaki kod ile `len()` fonksiyonuna eş çıktı elde edebiliriz.

```python
print(veri.shape[0])
```

Çıktı:

```python
10
```

Veri çerçevemizin sütun sayısını öğrenip bir değişkene atayarak kodumuza dahil etmek istersek, aşağıdaki kodunu kullanabiliriz.

```python
sutun_sayısı = veri.shape[1]
```

Şimdi de Sütun sayısını ekrana yazdıralım.

```python
print(sutun_sayısı)
```

Çıktı:

```python
3
```
