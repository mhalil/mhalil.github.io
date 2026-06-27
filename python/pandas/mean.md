Title: Pandas - mean
Date: 2022-07-28 19:00
Modified: 2025-07-05 16:11
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, mean, ortalama, metot
Author: Mustafa Halil

# mean() Metodu

**Her sütun için ortalama** değer hesaplamak için `mean()` metodunu kullanabiliriz.

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

Elimizde, 17 satır ve 3 sütundan oluşan tablomuz var. `mean()`metodunu kullanıp sonuca bakalım.

```python
basliksiz.mean()
```

```python
Birler      5.833333
Onlar      46.666667
Yüzler    488.666667
dtype: float64
```

Gördüğümüz gibi **her sütuna ait** ortalama değerler çıktı olarak sunuldu. **Her satır için** ortalama değer hesaplamak için ise `axis = 1` parametresini ekleyin kodu çalıştırın;

```python
basliksiz.mean(axis = 1)
```

```python
0     112.333333
1      88.333333
2     218.666667
3     191.333333
4     218.666667
5     120.333333
6     185.333333
7     258.666667
8     255.000000
9     327.666667
10    158.333333
11    198.666667
12     52.000000
13    165.666667
14     69.666667
15    178.666667
16    243.333333
17    204.333333
dtype: float64
```
