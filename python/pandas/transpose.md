Title: Pandas - transpose
Date: 2022-07-15 00:00
Modified: 2025-07-05 15:57
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Düzenleme, transpose
Author: Mustafa Halil

# transpose() Fonksiyonu

**Satırların sütuna, sütunların satıra çevrilme işlemini** `transpose()` fonksiyonu yardımıyla gerçekleştirebiliriz. Bu fonksiyon, Excel, LibreOfis,...vb uygulamalarda, "İşlemi tersine çevir" komutu ile aynı sonucu verir. 

Aşağıda bir veri çerçevesi oluşturup, veri çerçevemizin transpozunu alalım.

```python
import pandas as pd
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 42, 43, 23, 37, 52, 30, 38, 40, 38],
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
| 7   | Murat      | 38  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

Veri çerçevemizin transpozunu aşağıdaki şekilde alabiliriz.

```python
print(veri.transpose())
```

|           | 0        | 1         | 2           | 3        | 4     | 5        | 6        | 7     | 8         | 9          |
| --------- | -------- | --------- | ----------- | -------- | ----- | -------- | -------- | ----- | --------- | ---------- |
| isim      | Mustafa  | Halil     | Burak       | Emre     | Ersin | Sertaç   | Furkan   | Murat | Ahmet     | Abdülkadir |
| yaş       | 25       | 42        | 43          | 23       | 37    | 52       | 30       | 38    | 40        | 38         |
| iş-meslek | mühendis | programcı | akademisyen | yönetici | amir  | mühendis | yönetici | müdür | veteriner | yönetici   |
