Title: Pandas - median
Date: 2025-12-03 21:50
Modified: 2025-12-03 22:50
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, median
Author: Mustafa Halil

## `median()` Metodu

`pandas.DataFrame.median()` metodu, bir **DataFrame**'deki (veri çerçevesi) değerlerin, belirtilen eksen (satır veya sütun) üzerindeki **medyanını (ortanca değerini)** döndürmek için kullanılır.

**Medyan**, bir veri kümesindeki değerler küçükten büyüğe sıralandığında tam ortada kalan değerdir.

Bu yöntem genellikle bir **Series** (Seri) veya bir **Scalar** (tek bir sayı) döndürür.

## ⚙️ Parametreler

Yöntemin temel parametreleri şunlardır:

| Parametre      | Varsayılan Değer                                                                                                                                                                                                                                                                                                                    | Açıklama                                                                                                                       |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `axis`         | `0` (index) <br><br> **`0` (index)**: Her **sütunun** medyanını hesaplar ve sonuç olarak bir **Series** döndürür (varsayılan). <br><br> **`1` (columns)**: Her **satırın** medyanını hesaplar ve sonuç olarak bir **Series** döndürür. <br><br> **`None`**: Tüm DataFrame'in tek bir medyanını hesaplar (Sürüm 2.0.0'dan itibaren). | İşlevin uygulanacağı ekseni belirtir.                                                                                          |
| `skipna`       | `True`                                                                                                                                                                                                                                                                                                                              | Hesaplama yapılırken `NA` (boş/null) değerlerinin hariç tutulup tutulmayacağını belirtir. `True` ise hariç tutulur.            |
| `numeric_only` | `False`                                                                                                                                                                                                                                                                                                                             | Hesaplamaya yalnızca **float, integer (tam sayı)** ve **boolean (mantıksal)** sütunların dahil edilip edilmeyeceğini belirtir. |
| `**kwargs`     |                                                                                                                                                                                                                                                                                                                                     | Fonksiyona iletilecek ek anahtar kelime argümanları.                                                                           |

## 📝 Kullanım Örnekleri

### 1. Varsayılan Kullanım (`axis=0`)

Varsayılan olarak `axis=0` kullanılır, yani her sütunun medyanı hesaplanır:

```python
import pandas as pd

df = pd.DataFrame({ 'a': [1, 2, 8, 12], 
                    'b': [10,15, 24, 32], 
                    'c': [33, 50, 80, 100]})
print(df)
```

Veri çerçevemize bakalım, Çıktı:

```python
    a   b    c
0   1  10   33
1   2  15   50
2   8  24   80
3  12  32  100
```

Veri çerçevesinin medyanını bulalım;

```python
median_result = df.median()
print(median_result)
```

Çıktı:

```python
a     5.0 # ortadaki iki değerin ortalaması (2 + 8) / 2
b    19.5 # ortadaki iki değerin ortalaması (15 + 24) / 2
c    65.0 # ortadaki iki değerin ortalaması (50 + 80) / 2
dtype: float64
```

Sütunlarda 4'er veri olduğu için tam ortadaki değer seçilemiyor, bunun yerine tam ortada bulunan sayıların ortalaması alınıyor.

### 2. Satır Bazında Medyan (`axis=1`)

Satırlar arasındaki medyanı hesaplamak için `axis=1` kullanılır:

```python
median_result_axis_1 = df.median(axis=1)
print(median_result_axis_1)
```

Çıktı:

```python
0    10.0 # Ortadaki sayı 10 [1, 10, 23]
1    15.0 # Ortadaki sayı 10 [2, 15, 50]
2    24.0 # Ortadaki sayı 10 [8, 24, 80]
3    32.0 # Ortadaki sayı 10 [12, 32, 100]
dtype: float64
```

Satırlarda 3 adet (tek sayılı) veri olduğu için tam ortadaki sayı, medyan olarak hesaplanıyor. 

Bir de tüm Veri çerçevesinin medyanını bulalım.

```python
median_result_axis_None = df.median(axis=None)
print(median_result_axis_None)
```

Çıktı:

```python
19.5 # (15 + 24) / 2 <- Tablonun tam ortasındaki değerler 15 ve 24'tür.
```

### 3. Sadece Sayısal Sütunları Kullanma (`numeric_only=True`)

DataFrame'de sayısal olmayan (örneğin metin/string) sütunlar varsa, yalnızca sayısal sütunları dahil etmek için `numeric_only=True` ayarlanmalıdır. Aksi takdirde hata oluşabilir:

```python
df = pd.DataFrame({ 'a': [1, 2, 8, 12], 
                    'b': [10,'V', 24, 'N'], 
                    'c': [33, 50, 80, 100]})
print(df)
```

Veri Çerçevemiz:

```python
    a   b    c
0   1  10   33
1   2   V   50
2   8  24   80
3  12   N  100
```

Sadece numerik (sayılardan oluşan) verilerin ortalamasını bulalım;

```python
median_numeric = df.median(numeric_only=True)
print(median_numeric)
```

Çıktı:

```python
a     5.0
c    65.0
dtype: float64
```

Satırların medyanını bulalım;

```python
median_numeric = df.median(axis = 1, numeric_only=True)
print(median_numeric)
```

Çıktı:

```python
0    17.0 # (1 + 33) / 2
1    26.0 # (2 + 50) / 2
2    44.0 # (8 + 80) / 2
3    56.0 # (12 + 100) / 2
dtype: float64
```

**B** Sütunundaki **Tüm Değerler** devre dışı bırakılıp kalan değerlerin ortalaması alınarak medyan hesaplandı.

## Kaynak:

* [pandas.DataFrame.median &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html)
