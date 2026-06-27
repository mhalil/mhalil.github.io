Title: Pandas - add_prefix
Date: 2025-12-04 17:50
Modified: 2025-12-04 18:03
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, add_prefix
Author: Mustafa Halil

# `add_prefix()` Metodu

`pandas.DataFrame.add_prefix()` metodu, bir **DataFrame**'deki **etiketlerin** (varsayılan olarak **sütun isimlerinin**) önüne belirtilen bir **dizeyi (prefix)** eklemek için kullanılır.

## İşlevi

- **Ne yapar:** DataFrame'deki eksen etiketlerinin (varsayılan olarak sütun isimleri) önüne bir önek (`prefix`) ekler.

- **Döndürdüğü değer:** Önek eklenmiş yeni etiketlere sahip bir **DataFrame** veya **Series** döndürür. **Orijinal DataFrame'i değiştirmez.**

## Parametreler

| Parametre    | Tipi                                                                            | Açıklama                                                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`prefix`** | `str`                                                                           | Her etiketin önüne eklenecek dize (önek).                                                                                                                                                                                      |
| **`axis`**   | `0` veya `index`,<br>`1` veya `columns`,<br>`None}`,<br> **Varsayılan**: `None` | Önekin ekleneceği eksen. <br>Varsayılan olarak (**`axis=1`** veya **`'columns'`** gibi davranır) **sütun** etiketlerine uygulanır. <br>Eğer **`0`** veya **`'index'`** belirtilirse, **satır** etiketlerine (index) uygulanır. |

### Örnek Kullanım (Sütunlara Önek Ekleme)

Bir DataFrame'in sütun isimlerine `Yeni_` önekini ekleyelim:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
print("Orijinal DataFrame:")
print(df)
```

Çıktı:

```python
   A  B  C
0  1  3  5
1  2  4  6
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 0   | 1   | 3   | 5   |
| 1   | 2   | 4   | 6   |

Sütun isimlerine '**Yeni_**' önekini ekleme

```python
df_onekli = df.add_prefix('Yeni_')
print("Önek Eklenmiş DataFrame:")
print(df_onekli)
```

Çıktı:

```python
Önek Eklenmiş DataFrame:
   Yeni_A  Yeni_B  Yeni_C
0       1       3       5
1       2       4       6
```

|     | Yeni_A | Yeni_B | Yeni_C |
| --- | ------ | ------ | ------ |
| 0   | 1      | 3      | 5      |
| 1   | 2      | 4      | 6      |

Aynı DataFrame'in index isimlerine `Yeni_` önekini ekleyelim:

```python
df_indeks_onekli = df.add_prefix('Yeni_', axis="index") # index = 0 ile eş.
print("İndekse Önek Eklenmiş DataFrame:")
print(df_indeks_onekli)
```

Çıktı:

```python
İndekse Önek Eklenmiş DataFrame:
        A  B  C
Yeni_0  1  3  5
Yeni_1  2  4  6
```

|        | A   | B   | C   |
| ------ | --- | --- | --- |
| Yeni_0 | 1   | 3   | 5   |
| Yeni_1 | 2   | 4   | 6   |

Bu metot, özellikle büyük veri kümelerinde farklı kaynaklardan gelen sütunları birleştirmeden önce isim çakışmalarını önlemek veya sütunların kaynağını belirtmek için kullanışlıdır.

## Kaynak:

* [pandas.DataFrame.add_prefix &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add_prefix.html)
