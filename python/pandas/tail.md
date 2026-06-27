Title: Pandas - tail
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:36
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, tail
Author: Mustafa Halil

# tail() Fonksiyonu

**tail()** fonksiyonu, **head()** fonksiyonuna oldukça benzer bir fonksiyondur. Oluşturduğumuz ya da çalışmamıza dahil ettiğimiz Veri Çerçevelerinin **son satırlarını** görüp içerik hakkında bilgi edinmek istersek **tail()** fonksiyonunu kullanabiliriz. **Tail** kelimesi Türkçede, **kuyruk, son kısım** anlamına gelmektedir.

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

# tail() Fonksiyonunun Kullanımı

**tail()** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.tail())
```

|     | isim       | yaş | iş-meslek |
| --- | ---------- | --- | --------- |
| 5   | Sertaç     | 52  | mühendis  |
| 6   | Furkan     | 30  | yönetici  |
| 7   | Murat      | 23  | müdür     |
| 8   | Ahmet      | 40  | veteriner |
| 9   | Abdülkadir | 38  | yönetici  |

**tail()** fonksiyonunu içine parametre olarak bir değer yazmazsak, veri çerçevesinin **son 5 (satır) değerini** görüntüler. Değer belirtirsek belirttiğimiz değer kadar satır verisi görüntüler.

```python
print(veri.tail(7))
```

|     | isim       | yaş | iş-meslek |
| --- | ---------- | --- | --------- |
| 3   | Emre       | 23  | yönetici  |
| 4   | Ersin      | 37  | amir      |
| 5   | Sertaç     | 52  | mühendis  |
| 6   | Furkan     | 30  | yönetici  |
| 7   | Murat      | 23  | müdür     |
| 8   | Ahmet      | 40  | veteriner |
| 9   | Abdülkadir | 38  | yönetici  |
