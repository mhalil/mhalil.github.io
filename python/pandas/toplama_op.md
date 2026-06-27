Title: Pandas - Toplama Operatörü
Date: 2022-07-28 19:00
Modified: 2025-07-05 16:15
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Operatör, toplama
Author: Mustafa Halil

# + (Toplama) Operatörü

İki sütun verisini `+` **toplama operatörü** ile toplayabiliriz.

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

**Birler + Onlar** isimli sütun oluşturup, **Birler** ve **Onlar** Sütunlarındaki değerleri toplayıp yeni sütuna dahil edelim.

```python
basliksiz["Birler + Onlar"] = basliksiz["Birler"] + basliksiz["Onlar"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Birler + Onlar |
| --- | ------ | ----- | ------ | -------------- |
| 0   | 9      | 82    | 246    | 91             |
| 1   | 7      | 78    | 180    | 85             |
| 2   | 8      | 83    | 565    | 91             |
| 3   | 6      | 82    | 486    | 88             |
| 4   | 4      | 37    | 615    | 41             |
| 5   | 2      | 18    | 341    | 20             |
| 6   | 5      | 12    | 539    | 17             |
| 7   | 8      | 59    | 709    | 67             |
| 8   | 1      | 89    | 675    | 90             |
| 9   | 6      | 12    | 965    | 18             |
| 10  | 4      | 24    | 447    | 28             |
| 11  | 6      | 35    | 555    | 41             |
| 12  | 5      | 34    | 117    | 39             |
| 13  | 5      | 21    | 471    | 26             |
| 14  | 7      | 31    | 171    | 38             |
| 15  | 5      | 40    | 491    | 45             |
| 16  | 9      | 55    | 666    | 64             |
| 17  | 8      | 48    | 557    | 56             |
