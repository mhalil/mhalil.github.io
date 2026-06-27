Title: Pandas - drop
Date: 2022-07-15 00:00
Modified: 2025-06-22 13:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, drop
Author: Mustafa Halil

# drop() Fonksiyonu

Bu metodun kullanım/yazım şekli aşağıdaki gibidir.

```python
Veri_Çerçevesi_Adı.drop("Satır ya da Sütun Adı", 
                        axis = 0 ya da 1, inplace = True/False)
```

- **Satır ya da Sütun Adı**, adından belli olduğu üzere, silinecek sütunun adıdır. Birden fazla sütun silinmek istenirse, isimler liste şeklinde yani köşeli parantez içinde yazılmalıdır.

## axis Parametresi

Sıfır **(0)** Satırları, Bir **(1)** Sütunları temsil eder. Varsayılan (default) değeri 0'dır. Aynı isme ait satır ve sütun bilgisi olması durumunda, bu parametre satırın mı, sütunun mu silinmesi gerektiği konusunda bize yardımcı olur.

## inplace Parametresi

Gerçekleştirilen silme işleminin veri çerçevesinde kalıcı ya da geçici olmasını ayarladığımız kısımdır. **inplace = True** yazılırsa, yapılan işlem kalıcı hale gelecektir.

Aşağıdaki örneği inceleyelim.

```python
veri = pd.read_csv("Veri_Setleri/nba.csv")
print(veri)
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

NBA oyuncularının bilgilerinin bulunduğu veri çerçevesinden, **Yaş (Age)** bilgisini silmeye çalışalım.

```python
veri.drop("Age", axis = 1, inplace=True)
print(veri)
```

|     | Name          | Team           | Number | Position | Height | Weight | College           | Salary    | Aylık Kazanç  |
| --- | ------------- | -------------- | ------ | -------- | ------ | ------ | ----------------- | --------- | ------------- |
| 0   | Avery Bradley | Boston Celtics | 0.0    | PG       | 6-2    | 180.0  | Texas             | 7730337.0 | 644194.750000 |
| 1   | Jae Crowder   | Boston Celtics | 99.0   | SF       | 6-6    | 235.0  | Marquette         | 6796117.0 | 566343.083333 |
| 2   | John Holland  | Boston Celtics | 30.0   | SG       | 6-5    | 205.0  | Boston University | NaN       | NaN           |
| 3   | R.J. Hunter   | Boston Celtics | 28.0   | SG       | 6-5    | 185.0  | Georgia State     | 1148640.0 | 95720.000000  |
| 4   | Jonas Jerebko | Boston Celtics | 8.0    | PF       | 6-10   | 231.0  | NaN               | 5000000.0 | 416666.666667 |
| ... | ...           | ...            | ...    | ...      | ...    | ...    | ...               | ...       | ...           |
| 453 | Shelvin Mack  | Utah Jazz      | 8.0    | PG       | 6-3    | 203.0  | Butler            | 2433333.0 | 202777.750000 |
| 454 | Raul Neto     | Utah Jazz      | 25.0   | PG       | 6-1    | 179.0  | NaN               | 900000.0  | 75000.000000  |
| 455 | Tibor Pleiss  | Utah Jazz      | 21.0   | C        | 7-3    | 256.0  | NaN               | 2900000.0 | 241666.666667 |
| 456 | Jeff Withey   | Utah Jazz      | 24.0   | C        | 7-0    | 231.0  | Kansas            | 947276.0  | 78939.666667  |
| 457 | NaN           | NaN            | NaN    | NaN      | NaN    | NaN    | NaN               | NaN       | NaN           |

458 rows × 9 columns

Gördüğünüz gibi veri çerçevemizde artık Oyuncuların Yaş bilgilerini barındıran **Age** isimli sütun bulunmuyor, tamemiyle silindi.

Birden fazla satır ya da sütun silmek istediğimiz zaman silinmesini istediğimiz satır ya da sütun isimlerinin (ya da indeks değerlerini) liste olarak yani köşeli parantez içerisinde belirtmemiz gerekir.

```python
veri.drop(["College", "Number"], axis = 1, inplace=True)
print(veri)
```

|     | Name          | Team           | Position | Height | Weight | Salary    | Aylık Kazanç  |
| --- | ------------- | -------------- | -------- | ------ | ------ | --------- | ------------- |
| 0   | Avery Bradley | Boston Celtics | PG       | 6-2    | 180.0  | 7730337.0 | 644194.750000 |
| 1   | Jae Crowder   | Boston Celtics | SF       | 6-6    | 235.0  | 6796117.0 | 566343.083333 |
| 2   | John Holland  | Boston Celtics | SG       | 6-5    | 205.0  | NaN       | NaN           |
| 3   | R.J. Hunter   | Boston Celtics | SG       | 6-5    | 185.0  | 1148640.0 | 95720.000000  |
| 4   | Jonas Jerebko | Boston Celtics | PF       | 6-10   | 231.0  | 5000000.0 | 416666.666667 |
| ... | ...           | ...            | ...      | ...    | ...    | ...       | ...           |
| 453 | Shelvin Mack  | Utah Jazz      | PG       | 6-3    | 203.0  | 2433333.0 | 202777.750000 |
| 454 | Raul Neto     | Utah Jazz      | PG       | 6-1    | 179.0  | 900000.0  | 75000.000000  |
| 455 | Tibor Pleiss  | Utah Jazz      | C        | 7-3    | 256.0  | 2900000.0 | 241666.666667 |
| 456 | Jeff Withey   | Utah Jazz      | C        | 7-0    | 231.0  | 947276.0  | 78939.666667  |
| 457 | NaN           | NaN            | NaN      | NaN    | NaN    | NaN       | NaN           |

458 rows × 7 columns
