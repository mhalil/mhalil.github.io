Title: Pandas - isin
Date: 2025-12-06 22:04
Modified: 2025-12-06 22:04
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, isin
Author: Mustafa Halil

# `isin()` Metodu

Bu metodun (`pandas.DataFrame.isin(values)`) temel amacı, bir **DataFrame** içindeki her bir elemanın, sağlanan `values` (değerler) **koleksiyonunda bulunup bulunmadığını kontrol etmektir.**

## Sözdizimi

```python
DataFrame.isin(values)
```

## İşlevi

**DataFrame**'in her bir hücresini alır ve bu değeri, girdi olarak sağlanan `values` içinde arar. Sonuç olarak, orijinal DataFrame ile aynı boyutlara sahip, aranan değerin bulunup bulunmadığına bağlı olarak her hücrede **`True`** veya **`False`** değeri bulunan bir boolean (mantıksal) DataFrame döndürür.

## Parametre

| Parametre    | Tipi                                          | Açıklama                                                                                 |
| ------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **`values`** | `iterable`, `Series`, `DataFrame` veya `dict` | Kontrol edilecek değerleri içerir. Bu parametrenin tipi, eşleşme davranışını değiştirir. |

**`values` parametresinin farklı tiplere göre davranışı:**

1. **Iterable (Liste, Küme vb.)**: DataFrame'deki her bir eleman, iterasyon nesnesindeki herhangi bir değerle eşleşiyorsa sonuç `True` olur.

2. **dict (Sözlük)**: Sözlüğün **anahtarları** DataFrame'deki **sütun isimleri** olmalıdır. Kontrol, yalnızca anahtarla eşleşen sütun için yapılır. Örneğin, `{'sutun_ismi': [deger1, deger2]}` şeklinde bir girdi, yalnızca `sutun_ismi` sütunundaki değerleri `[deger1, deger2]` listesiyle karşılaştırır.

3. **DataFrame veya  Series**: Bu durumda, **hem indeks hem de sütun etiketleri** (etiketler eşleşen bir `Series` için indeks) eşleşmelidir. Bir konumdaki sonuç, ancak ilgili hücrenin değeri *ve* indeksi/sütun etiketi `values` içindeki karşılık gelen konumla eşleşirse `True` olur.

## Dönüş Değeri

- **Tipi**: **`DataFrame`**

- **Açıklaması**: Orijinal DataFrame ile aynı boyutlara ve indekslere sahip, her bir elemanın `values` içinde olup olmadığını belirten boolean (mantıksal) değerler içeren bir DataFrame döndürür.

## Örnek Kullanım

Elimizde aşağıdaki şekilde bir veri çerçevesi var.

```python
import pandas as pd

df = pd.DataFrame({'bacak_sayisi': [2, 4], 
                   'kanat_sayisi': [2, 0]},
                  index=['doğan', 'köpek'])

print(df)
```

Çıktı:

|       | bacak_sayisi | kanat_sayisi |
| ----- | ------------ | ------------ |
| doğan | 2            | 2            |
| köpek | 4            | 0            |

**1. iterable (Liste) ile kontrol:**



DataFrame'deki her değerin `[0, 2]` listesinde olup olmadığını kontrol edelim;

```python
print(df.isin([0, 2]))
```

Çıktı:

|       | bacak_sayisi | kanat_sayisi |
| ----- | ------------ | ------------ |
| doğan | True         | True         |
| köpek | False        | True         |

Veri çerçevesinde sadece `4` değeri `[0, 2]` listesinde olmadığı için bu değere ait çıktı `False` oldu.



* Bunun tam **tersini kontrol etmek** için `~` karakterini kullanmalıyız;

```python
print(~df.isin([0, 2]))
```

|       | bacak_sayisi | kanat_sayisi |
| ----- | ------------ | ------------ |
| doğan | False        | False        |
| köpek | True         | False        |

**2. dict (Sözlük) ile sütuna özel kontrol:**


Yalnızca '**kanat_sayisi**' sütunundaki değerlerin `[0, 3]` listesinde olup olmadığını kontrol edelim;

```python
print(df.isin({'kanat_sayisi': [0, 3]}))
```

Çıktı:

|       | bacak_sayisi | kanat_sayisi |
| ----- | ------------ | ------------ |
| doğan | False        | False        |
| köpek | False        | True         |

**kanat_sayisi** sütunudaki değerlerden sadece `2` değeri `[0, 3]` listesinde yok.

## Kaynak:

* [pandas.DataFrame.isin &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin)
