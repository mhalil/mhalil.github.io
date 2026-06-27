Title: Pandas - len
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:30
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, len
Author: Mustafa Halil

# len() Fonksiyonu

**len()** foknsiyonu, Veri Çerçevesinin kaç satırdan oluştuğunu bildirir.

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

# len() Fonksiyonunun Kullanımı

**len()** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(len(veri))
```

```
10
```

Çıktıdan anladığımız kadarıyla, **veri** isimli veri çerçevesi, 10 satırlık bir yapıdan oluşuyor.
