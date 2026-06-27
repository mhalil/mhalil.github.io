Title: Pandas - to_frame
Date: 2025-12-06 13:04
Modified: 2025-12-06 13:04
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, to_frame
Author: Mustafa Halil

# `.to_frame()` Metodu

`pandas.Series.to_frame()` metodu, Serileri DataFrame'e (Veri çerçevesine) dönüştürür. `to_frame` sözcüğü, **Çerçeveye, Veri çerçevesine** anlamına gelir. Metodun İşlevi, isminden anlaşılıyor. 

## Sözdizimi:

```python
 Series.to_frame(name=<no_default>)
```

## Parametreler:

**name** : nesne, isteğe bağlı

*Yazılan isim, seri isminin yerine geçer (eğer varsa).*

## Döndürdüğü değer:

**DataFrame** : Serinin DataFrame temsili. İşlem sonrası seri dataframe'e döner.

## Örnekler

```python
s = pd.Series(["a", "b", "c"], name="vals")
print(s)
```

Çıktı:

```python
0    a
1    b
2    c
Name: vals, dtype: object
```

Şimdi bu Seriyi, DataFrame'e çevirelim;

```python
s = s.to_frame()
print(s)
```

Çıktı:

```python
  vals
0    a
1    b
2    c
```

Başka bir örnek yapalım. Elimizde aşağıdaki gibi sayılardan oluşan bir tablo olsun.

```python
veri = {"birler" : [1,2,3,4,5],
        "onlar" : [10,20,30,40,50],
        "yuzler" : [100,200,300,400,500]}

df = pd.DataFrame(veri)
print(df)
```

Çıktı:

|     | birler | onlar | yuzler |
| --- | ------ | ----- | ------ |
| 0   | 1      | 10    | 100    |
| 1   | 2      | 20    | 200    |
| 2   | 3      | 30    | 300    |
| 3   | 4      | 40    | 400    |
| 4   | 5      | 50    | 500    |

Şimdi **Sütunların Toplamını** bulup tablonun en alt satırına ekleyelim.

```python
# Sütun toplamlarını bul. 
toplam = df.sum()    # Çıktı bir `Series` objesidir.

# Series objesini "Veri Çerçevesine (DataFrame'e) dönüştür ve transpozunu al
## Birleştirme öncesi veri çerçevelerinin sütun isimleri aynı olmalı. o nedenle veri çerçevesinin transpozunu almalıyız
df_toplam = toplam.to_frame(name="Toplam").transpose()    

# veri çerçevelerini birleştirelim.
df = pd.concat([df, df_toplam])
print(df)
```

Çıktı:

|        | birler | onlar | yuzler |
| ------ | ------ | ----- | ------ |
| 0      | 1      | 10    | 100    |
| 1      | 2      | 20    | 200    |
| 2      | 3      | 30    | 300    |
| 3      | 4      | 40    | 400    |
| 4      | 5      | 50    | 500    |
| Toplam | 15     | 150   | 1500   |

## Kaynak:

* [pandas.Series.to_frame &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_frame.html)
