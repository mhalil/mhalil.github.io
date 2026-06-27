Title: Pandas - Çarpma Operatörü
Date: 2022-07-28 19:00
Modified: 2025-07-05 16:23
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Operatör, çarpma
Author: Mustafa Halil

# * (Çarpma) Operatörü

İki sütun verisini `*` **çarpma operatörü** ile çarpabiliriz.

```python
baslik = ["Birler", "Onlar", "Yüzler"]
basliksiz = pd.read_excel("Veri_Setleri/basliksiz.ods", header = None, names = baslik )
print(basliksiz)
```

|     | Birler | Onlar | Yüzler |
| --- | ------ | ----- | ------ |
| 0   | 9      | 82    | 246    |
| 1   | 7      | 78    | 180    |
| 2   | 8      | 83    | 565    |
| 3   | 6      | 82    | 486    |
| 4   | 4      | 37    | 615    |
| 5   | 2      | 18    | 341    |
| 6   | 5      | 12    | 539    |
| 7   | 8      | 59    | 709    |
| 8   | 1      | 89    | 675    |
| 9   | 6      | 12    | 965    |
| 10  | 4      | 24    | 447    |
| 11  | 6      | 35    | 555    |
| 12  | 5      | 34    | 117    |
| 13  | 5      | 21    | 471    |
| 14  | 7      | 31    | 171    |
| 15  | 5      | 40    | 491    |
| 16  | 9      | 55    | 666    |
| 17  | 8      | 48    | 557    |

Elimizde, 17 satır ve 3 sütundan oluşan tablomuz var.

**Yüzler * Birler** isimli sütun oluşturup, **Yüzler** sütunundaki değerleri **Birler** Sütunundaki değerlerle çarpıp yeni sütuna dahil edelim.

```python
basliksiz["Yüzler * Birler"] = basliksiz["Yüzler"] * basliksiz["Birler"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Yüzler * Birler |
| --- | ------ | ----- | ------ | --------------- |
| 0   | 9      | 82    | 246    | 2214            |
| 1   | 7      | 78    | 180    | 1260            |
| 2   | 8      | 83    | 565    | 4520            |
| 3   | 6      | 82    | 486    | 2916            |
| 4   | 4      | 37    | 615    | 2460            |
| 5   | 2      | 18    | 341    | 682             |
| 6   | 5      | 12    | 539    | 2695            |
| 7   | 8      | 59    | 709    | 5672            |
| 8   | 1      | 89    | 675    | 675             |
| 9   | 6      | 12    | 965    | 5790            |
| 10  | 4      | 24    | 447    | 1788            |
| 11  | 6      | 35    | 555    | 3330            |
| 12  | 5      | 34    | 117    | 585             |
| 13  | 5      | 21    | 471    | 2355            |
| 14  | 7      | 31    | 171    | 1197            |
| 15  | 5      | 40    | 491    | 2455            |
| 16  | 9      | 55    | 666    | 5994            |
| 17  | 8      | 48    | 557    | 4456            |
