Title: Pandas - describe
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:15
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, describe, Fonksiyon
Author: Mustafa Halil

# describe Fonksiyonu

**describe()** fonksiyonu, sayısal veri barındıran sütunlar hakkında detaylı matematiksel bilgiler verir.

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

# describe Fonksiyonunun Kullanımı

**describe()** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.describe())
```

|       | yaş       |
| ----- | --------- |
| count | 10.000000 |
| mean  | 34.700000 |
| std   | 9.333929  |
| min   | 23.000000 |
| 25%   | 26.250000 |
| 50%   | 37.500000 |
| 75%   | 39.500000 |
| max   | 52.000000 |

<u>Çıktıyı incelersek;</u>  

**count :** yaş isimli sütunda **kaç adet veri **olduğunu,  

**mean :** yaş isimli sütudaki** verilerin ortalamasını**,  

**std :** yaş isimli sütudaki **verilerin standart sapmasını**,  

**min:** yaş isimli sütudaki **verilerin en küçük değerini**  

**%25 :** yaş isimli sütundaki verilerin **medyanın alt çeyreğini** (dörttebirliğini),  

**%50 :** yaş isimli sütundaki verilerin **ortanca medyanını,**  

**%75 :** yaş isimli sütundaki verilerin **medyanın üst çeyreğini** (dörttebirliğini),  

**max :** yaş isimli sütudaki **verilerin en büyük değerini**, 

tanımlar.
