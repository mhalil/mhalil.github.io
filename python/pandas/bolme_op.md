Title: Pandas - Bölme Operatörü
Date: 2022-07-28 19:00
Modified: 2025-07-05 16:22
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Operatör, bölme
Author: Mustafa Halil

# / (Bölme) Operatörü

İki sütun verisini `/` **bölme operatörü** ile bölebiliriz.

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

**Yüzler / Onlar** isimli sütun oluşturup, **Yüzler** sütunundaki değerleri **Onlar** Sütunundaki değerlere Bölüp yeni sütuna dahil edelim.

```python
basliksiz["Yüzler / Onlar"] = basliksiz["Yüzler"] / basliksiz["Onlar"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Yüzler / Onlar |
| --- | ------ | ----- | ------ | -------------- |
| 0   | 9      | 82    | 246    | 3.000000       |
| 1   | 7      | 78    | 180    | 2.307692       |
| 2   | 8      | 83    | 565    | 6.807229       |
| 3   | 6      | 82    | 486    | 5.926829       |
| 4   | 4      | 37    | 615    | 16.621622      |
| 5   | 2      | 18    | 341    | 18.944444      |
| 6   | 5      | 12    | 539    | 44.916667      |
| 7   | 8      | 59    | 709    | 12.016949      |
| 8   | 1      | 89    | 675    | 7.584270       |
| 9   | 6      | 12    | 965    | 80.416667      |
| 10  | 4      | 24    | 447    | 18.625000      |
| 11  | 6      | 35    | 555    | 15.857143      |
| 12  | 5      | 34    | 117    | 3.441176       |
| 13  | 5      | 21    | 471    | 22.428571      |
| 14  | 7      | 31    | 171    | 5.516129       |
| 15  | 5      | 40    | 491    | 12.275000      |
| 16  | 9      | 55    | 666    | 12.109091      |
| 17  | 8      | 48    | 557    | 11.604167      |
