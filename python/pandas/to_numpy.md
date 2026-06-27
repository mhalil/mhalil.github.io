Title: Pandas - to_numpy
Date: 2025-12-06 23:20
Modified: 2025-12-06 23:20
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, to_numpy
Author: Mustafa Halil

# `to_numpy()` Metodu

**`pandas.DataFrame.to_numpy()`** metodu, bir **pandas DataFrame**'i bir **NumPy dizisine** (`numpy.ndarray`) dönüştürmek için kullanılır.

Bu, bir **DataFrame**'deki verileri, hesaplama ve analiz için yaygın olarak kullanılan temel bir veri yapısı olan **NumPy** formatında elde etmenin tercih edilen yoludur.

## Sözdizimi:

```python
DataFrame.to_numpy(dtype=None, 
                    copy=False, 
                    na_value=<no_default>)
```

## Metodun Kullanımı ve Özeti

Varsayılan olarak, dönen dizinin veri türü (dtype), DataFrame'deki tüm türlerin **ortak NumPy veri türü** olacaktır. Örneğin, DataFrame'de `float16` ve `float32` türleri varsa, sonuç `float32` olacaktır. Farklı veri türlerinin olduğu durumlarda, çıktı dizisi `object` (nesne) veri türüne sahip olabilir.

## Parametreler

| Parametre      | Tür                                        | Açıklama                                                                                                                                                                                                  |
| -------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`dtype`**    | `str` veya `numpy.dtype`, **isteğe bağlı** | `numpy.asarray()`'ye iletilecek veri türü. Belirtilirse, dönen dizinin veri türü bu olacaktır.                                                                                                            |
| **`copy`**     | `bool`, **varsayılan `False`**             | Dönüş değerinin bir kopyasının istenip istenmediğini belirtir. `copy=True`, kesinlikle gerekli olmasa bile bir kopyanın oluşturulmasını sağlar. `copy=False` ise kopyalama yapılmayacağını garanti etmez. |
| **`na_value`** | `Any`, **isteğe bağlı**                    | Eksik değerler (`NaN`, `None`, vb.) için kullanılacak değer. Varsayılan değer, `dtype`'a ve DataFrame sütunlarının veri türlerine bağlıdır.                                                               |

## Dönüş Değeri

- **`numpy.ndarray`**: DataFrame'deki verileri içeren bir **NumPy dizisi**.

## Örnek Kullanım

**1. Basit bir DataFrame'i NumPy dizisine dönüştürme:**

Veri çerçevemiz;

```python
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})
```

|     | A   | B   |
| --- | --- | --- |
| 0   | 1   | 3   |
| 1   | 2   | 4   |

DataFrame'i NumPy dizisine dönüştür;

```python
array = df.to_numpy()
print(array)
```

Çıktı:

```python
[[1 3]
 [2 4]]
```

**2. Farklı veri türlerinin olduğu durumda, en düşük ortak tür kullanılır:**

```python
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.5]})
print(df)
```

Çıktı:

|     | A   | B   |
| --- | --- | --- |
| 0   | 1   | 3.0 |
| 1   | 2   | 4.5 |

A sütununda tamsayı (integer) değerler, B sütununda ise ondalıklı (float) değerler var. Bakalım dönüştürme işlemi sonucu türler nasıl değişecek?

```python
array = df.to_numpy()
print(array)
```

Çıktı:

```python
[[1.  3. ]
 [2.  4.5]]
```

>  **Not**: Tam sayı (int) ve ondalık sayı (float) içerdiği için ortak tür float olmuştur.

Sayısal ve sayısal olmayan türlerin karışımı için, çıktı **dizisi obje / nesne türüne** sahip olacaktır.

```python
df['C'] = pd.date_range('2000', periods=2)
print(df)
```

Çıktı:

|     | A   | B   | C          |
| --- | --- | --- | ---------- |
| 0   | 1   | 3.0 | 2000-01-01 |
| 1   | 2   | 4.5 | 2000-01-02 |

Dönüşümü gerçekleştirelim;

```python
print(df.to_numpy())
```

Çıktı:

```python
array([[1, 3.0, Timestamp('2000-01-01 00:00:00')],
       [2, 4.5, Timestamp('2000-01-02 00:00:00')]], dtype=object)
```

Çıktıda görüldüğü üzere (`dtype=object`) sayısal ve sayısal olmayan (zaman) türlerin karışımı için, çıktı **dizisi obje / nesne türüne** dönüştü.

## Kaynak:

* [pandas.DataFrame.to_numpy &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html)
