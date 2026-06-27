Title: Pandas - Çıkarma Operatörü
Date: 2022-07-28 19:00
Modified: 2025-07-05 16:20
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Operatör, çıkarma
Author: Mustafa Halil

# - (Çıkarma) Operatörü

İki sütun verisini `-` **çıkarma operatörü** ile çıkarabiliriz, farkını alabiliriz.

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

**Yüzler - Onlar** isimli sütun oluşturup, **Yüzler** sütunundaki değerlerden **Onlar** Sütunundaki değerleri çıkarıp yeni sütuna dahil edelim.

```python
basliksiz["Yüzler - Onlar"] = basliksiz["Yüzler"] - basliksiz["Onlar"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Yüzler - Onlar |
| --- | ------ | ----- | ------ | -------------- |
| 0   | 9      | 82    | 246    | 164            |
| 1   | 7      | 78    | 180    | 102            |
| 2   | 8      | 83    | 565    | 482            |
| 3   | 6      | 82    | 486    | 404            |
| 4   | 4      | 37    | 615    | 578            |
| 5   | 2      | 18    | 341    | 323            |
| 6   | 5      | 12    | 539    | 527            |
| 7   | 8      | 59    | 709    | 650            |
| 8   | 1      | 89    | 675    | 586            |
| 9   | 6      | 12    | 965    | 953            |
| 10  | 4      | 24    | 447    | 423            |
| 11  | 6      | 35    | 555    | 520            |
| 12  | 5      | 34    | 117    | 83             |
| 13  | 5      | 21    | 471    | 450            |
| 14  | 7      | 31    | 171    | 140            |
| 15  | 5      | 40    | 491    | 451            |
| 16  | 9      | 55    | 666    | 611            |
| 17  | 8      | 48    | 557    | 509            |
