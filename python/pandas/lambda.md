Title: Pandas - Lambda
Date: 2022-07-11 00:00
Modified: 2025-07-05 18:35
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, Koşul, Filtre, lambda
Author: Mustafa Halil

# lambda() Fonksiyonu ile Satır Filtrelemek

Veri çerçevemizde belirttiğimiz koşullara uyan satırları filtrelemek istersek, bunu `lambda()` fonksiyonu ile rahatlıkla gerçekleştirebiliriz.
Önce Veri Çerçevemize göz atalım;

```python
print(df)
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| cobra      | 1         | 2      |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

`lambda` fonksiyonu ile belirteceğimiz koşulu sağlayan satırı filtrelemek için aşağıdaki kod mantığını kullanabiliriz. Örneğin **shield** satırında **8**'e eşit değer barındıran satırları seçelim.

```python
print(df.loc[lambda df: df['shield'] == 8])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

> Yukarıda anlatılan `loc` ve `iloc` metodlarını, **Satır**lar da olduğu gibi, **Sütun**larda da kullanabiliriz.
