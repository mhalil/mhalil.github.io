Title: Pandas - Metot ve Operatör Kullanarak Filtreleme
Date: 2022-07-11 00:00
Modified: 2025-07-05 18:25
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, Koşul, Filtre, Metot, Operatör
Author: Mustafa Halil

# Metot ve Operatörün Birlikte Kullanımı ile Filtreleme

Veri çerçevemizde belirttiğimiz koşullara uyan satırları filtrelemek istersek, bunu Python **metot ve operatörlerini birlikte kullanarak** ta gerçekleştirebiliriz.
Önce Veri Çerçevemize göz atalım;

```python
print(df)
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| cobra      | 1         | 2      |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

## loc Metodu ve > Operatörünün Birlikte Kullanımı

**shield** sütununda **6'dan büyük** değerleri barındıran satırları seçmek istediğimizi varsayalım ve buna uygun kodu yazıp çalıştıralım;

```python
print(df.loc[df['shield'] > 6])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

## Koşullu Sütun Filtrelemek

Veri çerçevemizde belirttiğimiz **koşullara uyan belirli sütunu filtrelemek** istersek, benzer kodu kullanabiliriz. Örneğin **shield** sütununda **6'dan büyük** değerleri barındıran satırları ve bu satırların sadece **max_speed** sütununu filtrelemek istediğimizi varsayalım. Bunun için aşağıdaki kodu yazıp çalıştıralım;

```python
print(df.loc[df['shield'] > 6, ['max_speed']])
```

|            | max_speed |
| ---------- | --------- |
| sidewinder | 7         |

> Yukarıda anlatılan `loc` ve `iloc` metodlarını, **Satır**lar da olduğu gibi, **Sütun**larda da kullanabiliriz.
