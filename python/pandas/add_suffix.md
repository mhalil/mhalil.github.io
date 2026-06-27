Title: Pandas - add_suffix
Date: 2025-12-04 20:50
Modified: 2025-12-04 20:50
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, add_suffix
Author: Mustafa Halil

# `add_suffix()` Metodu

Bu metot, bir **DataFrame**'in veya **Series**'in etiketlerine (varsayılan olarak **sütun adlarına**) belirtilen bir dizeyi son ek olarak eklemek için kullanılır.

## Sözdizimi:

```python
DataFrame.add_suffix(suffix, axis=None)
```

## Parametreler

| Parametre    | Tipi                                                                     | Açıklama                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`suffix`** | `str`                                                                    | Her etiketin sonuna eklenecek olan dize.                                                                                                                                   |
| **`axis`**   | `0` ya da `index`, <br>`1` ya da `columns`, <br> `None` (**Varsayılan**) | Son ekin ekleneceği eksen.<br>- Varsayılan (**`None`** veya **`1`**): **Sütun** etiketlerine ekler.<br>- **`0`** veya **`'index'`**: **Satır** etiketlerine (index) ekler. |

**Dönüş Değeri:** Etiketleri güncellenmiş yeni bir `Series` veya `DataFrame` döndürür. **Orijinal DataFrame üzerinde değişiklik yapmaz**.

## 📝 Örnekler

Bu metot en çok, birden fazla DataFrame birleştirilirken (merge/join) hangi verinin hangi kaynaktan geldiğini belirtmek için sütun adlarına topluca son ek eklemek amacıyla kullanılır.

### Sütunlara Son Ek Ekleme (Varsayılan)

Aşağıdaki örnekte, varsayılan davranış olan **sütun etiketlerinin** sonuna `_sütun` dizesi eklenmiştir. Orjinal Veri çerçevemiz;

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]})

print("Orijinal DataFrame:")
print(df)
```

Çıktı:

```python
Orijinal DataFrame:
   A  B
0  1  3
1  2  4
2  3  5
3  4  6
```

|     | A   | B   |
| --- | --- | --- |
| 0   | 1   | 3   |
| 1   | 2   | 4   |
| 2   | 3   | 5   |
| 3   | 4   | 6   |

Aşağıdaki kod ile (`add_suffix()`) sütun isimlerinin sonuna `_sütun` ifadesi ekleniyor.

```python
print("add_suffix('_sütun') sonrası:")
df_sonuc = df.add_suffix('_sütun')
print(df_sonuc)
```

Çıktı:

```python
add_suffix('_sütun') sonrası:
   A_sütun  B_sütun
0        1        3
1        2        4
2        3        5
3        4        6
```

|     | A_Sütun | B_Sütun |
| --- | ------- | ------- |
| 0   | 1       | 3       |
| 1   | 2       | 4       |
| 2   | 3       | 5       |
| 3   | 4       | 6       |

### İndekslere (Satır Etiketlerine) Son Ek Ekleme

`axis=0` parametresi kullanılarak son ek **index etiketlerine** (satır adlarına) de eklenebilir:

```python
print("axis=0 ile indekslere son ek ekleme:")
df_index_sonuc = df.add_suffix('.Satır', axis=0)
print(df_index_sonuc)
```

Çıktı:

```python
axis=0 ile indekslere son ek ekleme:
         A  B
0.Satır  1  3
1.Satır  2  4
2.Satır  3  5
3.Satır  4  6
```

|         | A   | B   |
| ------- | --- | --- |
| 0.Satır | 1   | 3   |
| 1.Satır | 2   | 4   |
| 2.Satır | 3   | 5   |
| 3.Satır | 4   | 6   |

## Kaynak:

* [pandas.DataFrame.add_suffix &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add_suffix.html)
