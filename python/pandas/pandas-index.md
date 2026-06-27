Title: Pandas - pandas-index
Date: 2022-07-11 00:00
Modified: 2025-06-21 20:15
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, Seçim, index, pandas.index
Author: Mustafa Halil

# Index() Fonksiyonu Nedir? Nasıl Kullanılır?

> Index() Fonksiyonu, df.reindex ile aynı davranır.

`Index` metodu, veri çerçevesindeki index isimlerine göre Sıralama ve satır seçimi yapmamızı sağlar. `name` parametresi ise, indeks başlığı olarak kullanacağımız değeri atamamıza yarar. 

Önce Veri Çerçevemize göz atalım;

```python
print(df)
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| cobra      | 1         | 2      |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

**viper ve cobra** satırlarındaki verileri seçmek ve sıralamayı değiştirmek isteyelim. Bu durumda aşağıdaki kodu yazıp çalıştırmamız yeterli olacaktır;

```python
print(df.loc[pd.Index(["viper", "cobra"], name="Baslik")])
```

| Baslik | max_speed | shield |
| ------ | --------- | ------ |
| viper  | 4         | 5      |
| cobra  | 1         | 2      |

> `pd.Index()` fonksiyonunun `loc[]` fonksiyonu içerisine yazıldığına dikkat edin.
