Title: Pandas - read_clipboard
Date: 2022-07-09 20:30
Category: Pandas
Tags: Python, Pandas, DataFrame, Veri Çerçevesi, read_clipboard, Kütüphane, Modül
Author: Mustafa Halil

# read_clipboard() Fonksiyonu Nedir? Nasıl Kullanılır?

**read_clipboard()** fonksiyonu ile panoya kopyaladığımız veriyi (örneğin bir Excel tablosu ya da websitesindeki tabloyu) Veri Çerçevesine dönüştürebiliriz.

```python
pano = pd.read_clipboard()
print(pano)
```

|     | İlçe         | 2020    | 2021    | Fark    | Nüfus art. % | Mah. say. | Alanı km2 | Yoğunluk |
| --- | ------------ | ------- | ------- | ------- | ------------ | --------- | --------- | -------- |
| 0   | Adalar       | 16.033  | 16.372  | 339.000 | 2.11         | 5         | 11        | NaN      |
| 1   | Arnavutköy   | 296.709 | 312.023 | 15.314  | 5.16         | 38        | 453       | NaN      |
| 2   | Ataşehir     | 422.594 | 427.217 | 4.623   | 1.09         | 17        | 25        | NaN      |
| 3   | Avcılar      | 436.897 | 457.981 | 21.084  | 4.82         | 10        | 50        | NaN      |
| 4   | Bağcılar     | 737.206 | 744.351 | 7.145   | 0.96         | 22        | 23        | NaN      |
| 5   | Bahçelievler | 592.371 | 605.300 | 12.929  | 2.18         | 11        | 17        | NaN      |
| 6   | Bakırköy     | 226.229 | 228.759 | 2.530   | 1.11         | 15        | 29        | NaN      |
| 7   | Başakşehir   | 469.924 | 503.243 | 33.319  | 7.09         | 11        | 107       | NaN      |

