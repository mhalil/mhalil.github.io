Title: Pandas - dataframe
Date: 2022-07-09 20:30
Category: Pandas
Tags: Python, Pandas, DataFrame, Veri Çerçevesi, Oluştur, Kütüphane, Modül
Author: Mustafa Halil

# DataFrame() Fonksiyonu Nedir? Nasıl Kullanılır?

## VeriÇerçevesi (DataFrame) Oluştur

Bu bölümde sıfırdan **Veri Çerçevesi** (**Data Frame**) oluşturmayı öğreneceğiz.

## import Fonksiyonu

Öncelikle **Pandas** Kütüphanesini projemize dahil edip (içe aktarıp), kodlama esnasında hızlı olması adına bu kütüphaneye **pd** adını atayalım;

```python
import pandas as pd
```

## DataFrame() Fonksiyonu

Veri Çerçevesi (Data Frame) Oluşturmak ya da Dönüştürmek için **DataFrame()** fonksiyonunu kullanıyoruz. "Veri Çerçevesi"ne dönüştürmek istediğimiz veriyi, parantez içine, parametre olarak yazmalıyız.

```python
pd.DataFrame(veri)
```

Yukarıdaki kullanımda görülen **veri** parametresi, aşağıdakilerden herhangi biri olabilir.

- Sözlüklerden (Dictionary’lerden), serilerden veya listelerden oluşan bir sözlük (dictionary)
- 2 boyutlu numpy dizisi
- Başka bir DataFrame

örneğin bir **sözlük (dict)** veri yapısı oluşturup bu yapıyı **Veri Çerçevesi**ne (**Data Frame**'e) dönüştürelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
          "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
          "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici"]}
veri = pd.DataFrame(sozluk)
```

Oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
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

Gördüğünüz gibi verimiz, **DataFrame()** fonksiyonu ile,  SQL ya da Excel tablosuna benzer şekilde satır ve sütunlardan oluşan yapıya dönüştürüldü. Artık bu yapıyı yönetmek ve analiz etmek oldukça kolaylaşmış oldu.

Örnek olması açısından, bir de **liste (list)** veri yapısındaki değerlerin **Veri Çerçevesi**ne (**Data Frame**'e) nasıl dönüştürüldüğünü görelim;

```python
veri1 = ["Kerem", 23, "öğrenci"]
df = pd.DataFrame([veri1], columns=["isim", "yaş", "meslek"])
```

`DataFrame()` metodunun içine yazdığımız **liste veri yapısının**, **ayrı bir liste içinde** belirtildiğine dikkat edin. 

Aynı kodu aşağıdaki şekilde yazarak ta aynı sonuca ulaşabiliriz.

```python
df = pd.DataFrame([["Kerem", 23, "öğrenci"]], columns=["isim", "yaş", "meslek"])
```

Oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
print(df)
```

|     | isim  | yaş | iş-meslek |
| --- | ----- | --- | --------- |
| 0   | Kerem | 23  | öğrenci   |

Birden fazla satır kaydı oluşturmak için, aşağıdaki şekilde liste yapısını kullanabilirsiniz;

```python
df = pd.DataFrame([["Kerem", 23, "öğrenci"], ["Safa",18,"öğrenci"]], columns=["isim", "yaş", "meslek"])
print(df)
```

|     | isim  | yaş | iş-meslek |
| --- | ----- | --- | --------- |
| 0   | Kerem | 23  | öğrenci   |
| 1   | Safa  | 18  | öğrenci   |
