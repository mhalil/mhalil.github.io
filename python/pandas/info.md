Title: Pandas - info
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:28
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, info
Author: Mustafa Halil

# info() Fonksiyonu

**info()** fonksiyonu, Veri Çerçevesinin satır ve sütun sayısı, sütun veri tipleri (sayı [int, float], metin [object, string], ...vb) ve doluluk oranı (boş olmayan hücre sayısı [non-null]) hakkında bilgi verir.

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

# info() Fonksiyonunun Kullanımı

**info()** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.info())
```

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   isim       10 non-null     object
 1   yaş        10 non-null     int64 
 2   iş-meslek  10 non-null     object
dtypes: int64(1), object(2)
memory usage: 368.0+ bytes
```

<u>Çıktıyı incelersek;</u>  

**class 'pandas.core.frame.DataFrame** : **veri**'nin Pandas sınıfına ait bir DataFrame yapısı olduğunu,  

**RangeIndex: 10 entries, 0 to 9** : Veri Çerçevesinin 0 ile 9 arasında, toplam 10 satırlık yapı olduğunu,  

**Data columns (total 3 columns)** : Veri Çerçevesinin 3 sütundan oluştuğunu,  

**Column** : Sütun isimlerini,  

**Non-Null Count** : Sütun temelinde Boş olmayan veri sayısını,  

**Dtype** : Veri biçimini tanımlar.  

**int34** ya da int64 **ibaresi**, **tamsayı (integer)** olduğunu, 

**object** ibaresi, verinin **metin (string)** ifadesi olduğunu,  

**dtypes: int64(1), object(2)** : Veri Çerçevesindeki sütunlardan 1'inin tamsayı (**int64(1)**), 2'sinin ise metinsel (string / **object(2)**) veri içerdiğini ifade eder.
