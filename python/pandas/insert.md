Title: Pandas - insert
Date: 2025-12-07 22:50
Modified: 2025-12-07 22:50
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, insert
Author: Mustafa Halil

# `insert()` Metodu

`pandas.DataFrame.insert()` metodu, bir **DataFrame**'e **belirtilen bir konuma yeni bir sütun eklemek** için kullanılır. Bu işlem, orijinal DataFrame üzerinde gerçekleşir (yerinde değişiklik yapar).

## Amacı

- Belirtilen bir dizine (`loc`) yeni bir sütun (`column`) ekler.

- Bu sayede, sütunların sırasını kontrol ederek veri setine yeni veriler dahil etmeye olanak tanır.

## Sözdizimi:

```python
DataFrame.insert(loc, column, value, allow_duplicates=<no_default>)
```

## Parametreler

1. **`loc`** (int):
   
   - Sütunun ekleneceği konumun dizini (indeksi).
   
   - `0 <= loc <= len(columns)` koşulunu sağlamalıdır. Örneğin, 1, ilk sütundan sonra ekleneceği anlamına gelir.

2. **`column`** (str, sayı veya karma nesne):
   
   - Eklenecek yeni sütunun etiketi (adı).

3. **`value`** (Scalar, Series veya dizi benzeri):
   
   - Eklenecek yeni sütunun içeriği.
   
   - Eğer **Series** tipinde bir değer verilirse, mevcut DataFrame'in indeksi ile **hizalanır**.

4. **`allow_duplicates`** (bool, opsiyonel, varsayılan `False`):
   
   - Eğer `False` ise (varsayılan), eklenmek istenen sütun etiketi (`column`) zaten varsa bir `ValueError` hatası verir.
   
   - Eğer `True` olarak ayarlanırsa, aynı isimde birden fazla sütun oluşturulmasına izin verir.

## Basit Kullanım Örneği

Aşağıdaki örnek, `col1` ve `col2` sütunlarına sahip bir DataFrame'e **1** konumuna (yani `col1`'den sonra) `newcol` adında yeni bir sütun eklemeyi göstermektedir:

Orijinal DataFrame;

```python
df = pd.DataFrame({'sütun1': [1, 2], 'cosütun2': [3, 4]})
print("Orijinal DataFrame:")
print(df)
```

Çıktı:

```python
Orijinal DataFrame:
   sütun1  sütun2
0      1        3
1      2        4
```

|     | sütun1 | sütun2 |
| --- | ------ | ------ |
| 0   | 1      | 3      |
| 1   | 2      | 4      |

1. konuma "**yeni_sütun**" sütununu ekleme

```python
df.insert(1, "yeni_sütun", [99, 99])

print("Ekleme sonrası DataFrame:")
print(df)
```

Çıktı:

```python
Ekleme sonrası DataFrame:
   col1  yeni_sütun  col2
0     1          99     3
1     2          99     4
```

|     | sütun1 | yeni_sütun | sütun2 |
| --- | ------ | ---------- | ------ |
| 0   | 1      | 99         | 3      |
| 1   | 2      | 99         | 4      |

### İndeks Hizalama Örneği

Eğer `value` olarak bir **Series** kullanılırsa, pandas DataFrame'in indeksi ile **hizalama** yapar:

df'ye '**sütun0**' sütununu **0. konuma** ekliyoruz.
Series'in indeksi `[1, 2]` olduğu için, **0.** indekse `NaN` (Not a Number) atanır.

```python
df.insert(0, "sütun0", pd.Series([5, 6], index=[1, 2])) 

print("\nSeries ile ekleme sonrası DataFrame:")
print(df)
```

Series ile ekleme sonrası DataFrame:

```python
   sütun0  sütun1  yeni_sütun  sütun2
0     NaN       1          99       3
1     5.0       2          99       4
```

|     | sütun0 | sütun1 | yeni_sütun | sütun2 |
| --- | ------ | ------ | ---------- | ------ |
| 0   | NaN    | 1      | 99         | 3      |
| 1   | 5.0    | 2      | 99         | 4      |

> Not: Bu çıktı, yukarıdaki df.insert(1, "yeni_sütun", ...) işleminden sonraki df üzerinden devam eder.

## Kaynak:

* [pandas.DataFrame.insert &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)
