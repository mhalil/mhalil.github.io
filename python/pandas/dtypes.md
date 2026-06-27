Title: Pandas - dtypes
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:15
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, dtypes
Author: Mustafa Halil

# `dtypes` Metodu

`dtypes` metodu, veri çerçevesinin sütunlarına ait veri tiplerini görüntüler. Yani sütunlardaki verilerin, sayısal mı? metin tabanlı mı olduğunu bildirir.

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

# dtypes Fonksiyonunun Kullanımı

**dtypes** fonksiyonu aşağıdaki şekilde kullanılır. **dtypes** fonksiyonunu kullanırken sonunda <u>parantez işaretleri kullanmadığımıza</u> dikkat edin.

```python
print(veri.dtypes)
```

Çıktı:

```python
isim         object
yaş           int64
iş-meslek    object
dtype: object
```

<u>Çıktıyı incelersek;</u>

**yaş** ifadesine karşılık gelen **int64** ibaresi, bu sütundaki verilerin tamamının **tamsayı (integer)** değeri olduğunu,

**isim** ve **iş-meslek** ifadelerine karşılık gelen **object** ibaresi ise, bu sütundaki verilerin **metin (string)** ifadesi olduğunu,

göstermektedir.
