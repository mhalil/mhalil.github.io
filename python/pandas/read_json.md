Title: Pandas - read_json
Date: 2022-07-09 20:30
Category: Pandas
Tags: Python, Pandas, DataFrame, Veri Çerçevesi, read_json, Kütüphane, Modül
Author: Mustafa Halil

# read_json() Fonksiyonu Nedir? Nasıl Kullanılır?

**read_json()** fonksiyonu ile **json** uzantılı dosyaları çalışmalarınıza dahil edebilirsiniz.

```python
veri_json = pd.read_json("Veri_Setleri/json_verisi.json")
print(veri_json)
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | 60       | 110   | 130      | 409      |
| 1   | 60       | 117   | 145      | 479      |
| 2   | 60       | 103   | 135      | 340      |
| 3   | 45       | 109   | 175      | 282      |
| 4   | 45       | 117   | 148      | 406      |
| 5   | 60       | 102   | 127      | 300      |

Yerel diskinizde bulunan **json** dosyası dışında, <u>bir web sitesindeki <strong>json</strong> dosyasını da</u> çalışmanıza dahil etmek isterseniz yine **read_json()** fonksiyonunu kullanabilirsiniz.

```python
url = "https://api.exchangerate-api.com/v4/latest/USD"
df = pd.read_json(url)
print(df)
```

|     | provider                         | WARNING_UPGRADE_TO_V6                      | terms                                  | base | date       | time_last_updated | rates  |
| --- | -------------------------------- | ------------------------------------------ | -------------------------------------- | ---- | ---------- | ----------------- | ------ |
| AED | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 3.67   |
| AFN | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 87.53  |
| ALL | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 114.07 |
| AMD | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 409.31 |
| ANG | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 1.79   |
| ... | ...                              | ...                                        | ...                                    | ...  | ...        | ...               | ...    |
| XPF | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 117.34 |
| YER | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 249.15 |
| ZAR | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 16.83  |
| ZMW | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 16.38  |
| ZWL | https://www.exchangerate-api.com | https://www.exchangerate-api.com/docs/free | https://www.exchangerate-api.com/terms | USD  | 2022-07-11 | 1657497602        | 374.49 |

161 rows × 7 columns

