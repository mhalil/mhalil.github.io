Title: Pandas - groupby
Date: 2022-07-17 00:00
Modified: 2025-06-29 16:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Grup, groupby, mean, max, min, sort, count, value_counts
Author: Mustafa Halil

# `groupby()` Metodu

Veri Çerçevemizde aynı isme ya da aynı değere sahip birden fazla veri bilgisi olabilir. Verileri gruplayarak, grupların toplam değerleri, ortalama değerleri, grupta kaç adet veri bulunduğu, gruptaki verilerden en küçük ya da en büyük verinin hangisi olduğu gibi pek çok bilgi edinmek için, `groupby()` metodundan yararlanacağız.

`groupby` fonksiyonu incelemek için öncelikle NBA oyuncularının bilgilerinin bulunduğu **.csv** dosyamızı, veri çerçevesine dönüştürüp içeriğine göz atalım.

```python
import pandas as pd
nba = pd.read_csv("Veri_Setleri/nba.csv", decimal=".")
print(nba)
```

|     | Name          | Team           | Number | Position | Age  | Height | Weight | College           | Salary    |
| --- | ------------- | -------------- | ------ | -------- | ---- | ------ | ------ | ----------------- | --------- |
| 0   | Avery Bradley | Boston Celtics | 0.0    | PG       | 25.0 | 6-2    | 180.0  | Texas             | 7730337.0 |
| 1   | Jae Crowder   | Boston Celtics | 99.0   | SF       | 25.0 | 6-6    | 235.0  | Marquette         | 6796117.0 |
| 2   | John Holland  | Boston Celtics | 30.0   | SG       | 27.0 | 6-5    | 205.0  | Boston University | NaN       |
| 3   | R.J. Hunter   | Boston Celtics | 28.0   | SG       | 22.0 | 6-5    | 185.0  | Georgia State     | 1148640.0 |
| 4   | Jonas Jerebko | Boston Celtics | 8.0    | PF       | 29.0 | 6-10   | 231.0  | NaN               | 5000000.0 |
| ... | ...           | ...            | ...    | ...      | ...  | ...    | ...    | ...               | ...       |
| 453 | Shelvin Mack  | Utah Jazz      | 8.0    | PG       | 26.0 | 6-3    | 203.0  | Butler            | 2433333.0 |
| 454 | Raul Neto     | Utah Jazz      | 25.0   | PG       | 24.0 | 6-1    | 179.0  | NaN               | 900000.0  |
| 455 | Tibor Pleiss  | Utah Jazz      | 21.0   | C        | 26.0 | 7-3    | 256.0  | NaN               | 2900000.0 |
| 456 | Jeff Withey   | Utah Jazz      | 24.0   | C        | 26.0 | 7-0    | 231.0  | Kansas            | 947276.0  |
| 457 | NaN           | NaN            | NaN    | NaN      | NaN  | NaN    | NaN    | NaN               | NaN       |

458 rows × 9 columns

Veri çerçevemizi incelediğimizde, **Takım (Team)** ismine göre grulama yapmanın uygun olacağını düşünüyorum. Takıma göre gruplama yaparak, Takımda bulunan Oyuncuların Ortalama, En az ya da En fazla Yaş (Age), Boy uzunluğu (Height), Kilo (Weight) bilgileri ya da Yıllık Kazançlarını (Salary) görebiliriz.

## mean() Metodu

Aşağıdaki örnekte, Takımlara göre tüm sayısal veri barındıran sütunlarının **ortalama** değerlerini göreceğiz. Ortalama değeri bulmak için `mean()` metodunu kullanacağız.

```python
print(nba.groupby("Team").mean())
```

| Team                   | Number    | Age       | Weight     | Salary       |
| ---------------------- | --------- | --------- | ---------- | ------------ |
| Atlanta Hawks          | 19.000000 | 28.200000 | 221.266667 | 4.860197e+06 |
| Boston Celtics         | 31.866667 | 24.733333 | 219.466667 | 4.181505e+06 |
| Brooklyn Nets          | 18.266667 | 25.600000 | 215.600000 | 3.501898e+06 |
| Charlotte Hornets      | 17.133333 | 26.133333 | 220.400000 | 5.222728e+06 |
| Chicago Bulls          | 19.200000 | 27.400000 | 218.933333 | 5.785559e+06 |
| Cleveland Cavaliers    | 14.466667 | 29.533333 | 227.866667 | 7.642049e+06 |
| Dallas Mavericks       | 20.000000 | 29.733333 | 227.000000 | 4.746582e+06 |
| Denver Nuggets         | 15.266667 | 25.733333 | 217.533333 | 4.294424e+06 |
| Detroit Pistons        | 17.266667 | 26.200000 | 222.200000 | 4.477884e+06 |
| Golden State Warriors  | 20.866667 | 27.666667 | 224.600000 | 5.924600e+06 |
| Houston Rockets        | 14.666667 | 26.866667 | 220.333333 | 5.018868e+06 |
| Indiana Pacers         | 18.933333 | 26.400000 | 222.266667 | 4.450122e+06 |
| Los Angeles Clippers   | 19.533333 | 29.466667 | 219.733333 | 6.323643e+06 |
| Los Angeles Lakers     | 16.066667 | 27.533333 | 227.066667 | 4.784695e+06 |
| Memphis Grizzlies      | 15.555556 | 28.388889 | 218.000000 | 5.467920e+06 |
| Miami Heat             | 10.466667 | 28.933333 | 218.400000 | 6.347359e+06 |
| Milwaukee Bucks        | 20.000000 | 24.562500 | 224.062500 | 4.350220e+06 |
| Minnesota Timberwolves | 19.571429 | 26.357143 | 228.642857 | 4.593054e+06 |
| New Orleans Pelicans   | 17.000000 | 26.894737 | 221.000000 | 4.355304e+06 |
| New York Knicks        | 13.250000 | 27.000000 | 223.625000 | 4.581494e+06 |
| Oklahoma City Thunder  | 14.000000 | 27.066667 | 229.400000 | 6.251020e+06 |
| Orlando Magic          | 16.428571 | 25.071429 | 213.357143 | 4.297248e+06 |
| Philadelphia 76ers     | 18.066667 | 24.600000 | 222.133333 | 2.213778e+06 |
| Phoenix Suns           | 15.466667 | 25.866667 | 218.600000 | 4.229676e+06 |
| Portland Trail Blazers | 16.000000 | 25.066667 | 218.600000 | 3.220121e+06 |
| Sacramento Kings       | 16.933333 | 26.800000 | 221.333333 | 4.778911e+06 |
| San Antonio Spurs      | 17.933333 | 31.600000 | 223.933333 | 5.629516e+06 |
| Toronto Raptors        | 22.466667 | 26.133333 | 221.800000 | 4.741174e+06 |
| Utah Jazz              | 17.866667 | 24.466667 | 220.000000 | 4.204006e+06 |
| Washington Wizards     | 17.600000 | 27.866667 | 219.000000 | 5.088576e+06 |

Takımlara göre tüm sütunların ortalama değerleri yerine **sadece Ortalama Yaş** bilgisini görmek isteseydik aşağıdaki kodu çalıştırmamız yeterli olacaktı.

```python
print(nba.groupby("Team").mean()["Age"])
```

```python
Team
Atlanta Hawks             28.200000
Boston Celtics            24.733333
Brooklyn Nets             25.600000
Charlotte Hornets         26.133333
Chicago Bulls             27.400000
Cleveland Cavaliers       29.533333
Dallas Mavericks          29.733333
Denver Nuggets            25.733333
Detroit Pistons           26.200000
Golden State Warriors     27.666667
Houston Rockets           26.866667
Indiana Pacers            26.400000
Los Angeles Clippers      29.466667
Los Angeles Lakers        27.533333
Memphis Grizzlies         28.388889
Miami Heat                28.933333
Milwaukee Bucks           24.562500
Minnesota Timberwolves    26.357143
New Orleans Pelicans      26.894737
New York Knicks           27.000000
Oklahoma City Thunder     27.066667
Orlando Magic             25.071429
Philadelphia 76ers        24.600000
Phoenix Suns              25.866667
Portland Trail Blazers    25.066667
Sacramento Kings          26.800000
San Antonio Spurs         31.600000
Toronto Raptors           26.133333
Utah Jazz                 24.466667
Washington Wizards        27.866667
Name: Age, dtype: float64
```

## max() Metodu

Takımlardaki **en ağır (kilolu) (en büyük)** Oyuncuları listelemek istersek , bu işlemi `max()` metodu ile gerçekleştirebiliriz. Amerika'da, Ülkemizde kullanılan **SI Metrik Ölçü birimi** yerine **İngiliz Ölçü birimi**nden türemiş olan **ABD geleneksel ölçü birimleri** kullanıldığı için, tabloda gördüğünüz **Boy uzunluğu (Height)** ve **Kilo (Weight)** değerleri sizi şaşırtmış olabilir.

```python
nba.dropna(axis=1)
print(nba.groupby("Team")["Weight"].max())
```

```python
Team
Atlanta Hawks             260.0
Boston Celtics            260.0
Brooklyn Nets             275.0
Charlotte Hornets         289.0
Chicago Bulls             275.0
Cleveland Cavaliers       275.0
Dallas Mavericks          275.0
Denver Nuggets            280.0
Detroit Pistons           279.0
Golden State Warriors     273.0
Houston Rockets           265.0
Indiana Pacers            255.0
Los Angeles Clippers      265.0
Los Angeles Lakers        270.0
Memphis Grizzlies         270.0
Miami Heat                265.0
Milwaukee Bucks           265.0
Minnesota Timberwolves    307.0
New Orleans Pelicans      270.0
New York Knicks           278.0
Oklahoma City Thunder     255.0
Orlando Magic             260.0
Philadelphia 76ers        275.0
Phoenix Suns              260.0
Portland Trail Blazers    265.0
Sacramento Kings          270.0
San Antonio Spurs         290.0
Toronto Raptors           255.0
Utah Jazz                 265.0
Washington Wizards        250.0
Name: Weight, dtype: float64
```

## min() Metodu

Takımlardaki **en genç (en küçük)** Oyuncuları listelemek istersek , bu işlemi `min()` metodu ile gerçekleştirebiliriz.

```python
print(nba.groupby("Team")["Age"].min())
```

```python
Team
Atlanta Hawks             22.0
Boston Celtics            20.0
Brooklyn Nets             21.0
Charlotte Hornets         21.0
Chicago Bulls             21.0
Cleveland Cavaliers       24.0
Dallas Mavericks          22.0
Denver Nuggets            20.0
Detroit Pistons           20.0
Golden State Warriors     20.0
Houston Rockets           22.0
Indiana Pacers            20.0
Los Angeles Clippers      23.0
Los Angeles Lakers        20.0
Memphis Grizzlies         21.0
Miami Heat                20.0
Milwaukee Bucks           19.0
Minnesota Timberwolves    20.0
New Orleans Pelicans      23.0
New York Knicks           20.0
Oklahoma City Thunder     21.0
Orlando Magic             20.0
Philadelphia 76ers        20.0
Phoenix Suns              19.0
Portland Trail Blazers    20.0
Sacramento Kings          22.0
San Antonio Spurs         22.0
Toronto Raptors           20.0
Utah Jazz                 20.0
Washington Wizards        20.0
Name: Age, dtype: float64
```

## sort_values() Metodu

Takımlardaki en genç Oyuncuları, Oyuncu yaşına göre **küçükten büyüğe doğru listelemek/sıralamak** istersek , bu işlemi `sort_values()` metodu ile gerçekleştirebiliriz.

```python
print(nba.groupby("Team")["Age"].min().sort_values())
```

```python
Team
Phoenix Suns              19.0
Milwaukee Bucks           19.0
Washington Wizards        20.0
Miami Heat                20.0
Utah Jazz                 20.0
Los Angeles Lakers        20.0
New York Knicks           20.0
Indiana Pacers            20.0
Golden State Warriors     20.0
Detroit Pistons           20.0
Orlando Magic             20.0
Philadelphia 76ers        20.0
Portland Trail Blazers    20.0
Toronto Raptors           20.0
Boston Celtics            20.0
Denver Nuggets            20.0
Minnesota Timberwolves    20.0
Oklahoma City Thunder     21.0
Memphis Grizzlies         21.0
Chicago Bulls             21.0
Charlotte Hornets         21.0
Brooklyn Nets             21.0
Houston Rockets           22.0
Dallas Mavericks          22.0
Sacramento Kings          22.0
San Antonio Spurs         22.0
Atlanta Hawks             22.0
Los Angeles Clippers      23.0
New Orleans Pelicans      23.0
Cleveland Cavaliers       24.0
Name: Age, dtype: float64
```

## count() Metodu

Veri Çerçevemizi **Takım (Team)** ismine göre gruplayarak, hangi sütunda **kaç adet veri olduğunu** bulmak istersek, `count()` metodundan yararlanabiliriz.

```python
print(nba.groupby("Team").count())
```

| Team                   | Name | Number | Position | Age | Height | Weight | College | Salary |
| ---------------------- | ---- | ------ | -------- | --- | ------ | ------ | ------- | ------ |
| Atlanta Hawks          | 15   | 15     | 15       | 15  | 15     | 15     | 11      | 15     |
| Boston Celtics         | 15   | 15     | 15       | 15  | 15     | 15     | 13      | 14     |
| Brooklyn Nets          | 15   | 15     | 15       | 15  | 15     | 15     | 13      | 15     |
| Charlotte Hornets      | 15   | 15     | 15       | 15  | 15     | 15     | 13      | 15     |
| Chicago Bulls          | 15   | 15     | 15       | 15  | 15     | 15     | 12      | 15     |
| Cleveland Cavaliers    | 15   | 15     | 15       | 15  | 15     | 15     | 12      | 14     |
| Dallas Mavericks       | 15   | 15     | 15       | 15  | 15     | 15     | 12      | 15     |
| Denver Nuggets         | 15   | 15     | 15       | 15  | 15     | 15     | 9       | 14     |
| Detroit Pistons        | 15   | 15     | 15       | 15  | 15     | 15     | 15      | 15     |
| Golden State Warriors  | 15   | 15     | 15       | 15  | 15     | 15     | 12      | 15     |
| Houston Rockets        | 15   | 15     | 15       | 15  | 15     | 15     | 11      | 15     |
| Indiana Pacers         | 15   | 15     | 15       | 15  | 15     | 15     | 12      | 15     |
| Los Angeles Clippers   | 15   | 15     | 15       | 15  | 15     | 15     | 14      | 15     |
| Los Angeles Lakers     | 15   | 15     | 15       | 15  | 15     | 15     | 12      | 15     |
| Memphis Grizzlies      | 18   | 18     | 18       | 18  | 18     | 18     | 17      | 14     |
| Miami Heat             | 15   | 15     | 15       | 15  | 15     | 15     | 11      | 13     |
| Milwaukee Bucks        | 16   | 16     | 16       | 16  | 16     | 16     | 14      | 16     |
| Minnesota Timberwolves | 14   | 14     | 14       | 14  | 14     | 14     | 9       | 13     |
| New Orleans Pelicans   | 19   | 19     | 19       | 19  | 19     | 19     | 16      | 19     |
| New York Knicks        | 16   | 16     | 16       | 16  | 16     | 16     | 11      | 16     |
| Oklahoma City Thunder  | 15   | 15     | 15       | 15  | 15     | 15     | 14      | 15     |
| Orlando Magic          | 14   | 14     | 14       | 14  | 14     | 14     | 10      | 14     |
| Philadelphia 76ers     | 15   | 15     | 15       | 15  | 15     | 15     | 15      | 14     |
| Phoenix Suns           | 15   | 15     | 15       | 15  | 15     | 15     | 13      | 15     |
| Portland Trail Blazers | 15   | 15     | 15       | 15  | 15     | 15     | 15      | 15     |
| Sacramento Kings       | 15   | 15     | 15       | 15  | 15     | 15     | 13      | 15     |
| San Antonio Spurs      | 15   | 15     | 15       | 15  | 15     | 15     | 11      | 15     |
| Toronto Raptors        | 15   | 15     | 15       | 15  | 15     | 15     | 10      | 15     |
| Utah Jazz              | 15   | 15     | 15       | 15  | 15     | 15     | 10      | 15     |
| Washington Wizards     | 15   | 15     | 15       | 15  | 15     | 15     | 13      | 15     |

## value_counts() Metodu

Veri Çerçevemizi <u>Takım (Team)</u> ismine göre gruplayarak, <u>Yaş (Age) Sütununda</u> **hangi değerden kaç adet veri olduğunu** bulmak istersek, `value_counts()` metodundan yararlanabiliriz.

```python
print(nba.groupby("Team")["Age"].value_counts())
```

```python
Team                Age 
Atlanta Hawks       24.0    4
                    31.0    3
                    27.0    2
                    35.0    2
                    22.0    1
                           ..
Washington Wizards  26.0    1
                    27.0    1
                    29.0    1
                    32.0    1
                    34.0    1
Name: Age, Length: 288, dtype: int64
```
