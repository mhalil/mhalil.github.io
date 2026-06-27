Title: Pandas - unique ve nunique
Date: 2025-07-06 23:32
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, unique, nunique, Fonksiyon, drop_duplicates, ,value_counts, set
Author: Mustafa Halil

# `unique()` ve `nunique()` Metotları

# `unique()` Metodu

`unique()` Metodu, Veri Çerçevesinden **benzersiz değerler tespit etmek**, kategorik verileri analiz etmek veya **yinelenen verileri tanımlamak** için kullanılır. 

![unique_nunique](../../images/python/pandas/unique_nunique.png)

## `unique()` Metodunun Kullanımı

`unique()` Fonksiyonu bir NumPy dizisi döndürür. Bir sütundaki benzersiz (farklı) değerleri tanımlamak için kullanışlıdır ve bu, kategorik verilerle çalışırken veya benzersiz değerleri algılarken yardımcı olabilir. Benzersiz değerlerin sırası, ilk oluşumlarına göre korunur.

**Sözdizimi**:

```python
Veri_Çerçevesi_Adı["Sütun_Adı"].unique()
```

Konuyu örnek veri çerçevesi oluşturarak inceleyelim.  Veri çerçevemiz aşağıdadır;

```python
import pandas as pd

data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B4'],
    'C': ['C1', 'C2', 'C3', 'C3', 'C3'],
    'D': ['D1', 'D2', 'D2', 'D2', 'D2'],
    'E': ['E1', 'E1', 'E1', 'E1', 'E1']}

df = pd.DataFrame(data)
print("Pandas Veri Çerçevesi:")
print(df)
```

Pandas Veri Çerçevesi:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| 0   | A1  | B1  | C1  | D1  | E1  |
| 1   | A2  | B2  | C2  | D2  | E1  |
| 2   | A3  | B3  | C3  | D2  | E1  |
| 3   | A4  | B4  | C3  | D2  | E1  |
| 4   | A5  | B4  | C3  | D2  | E1  |

`unique()` Fonksiyonunu kullanarak "B" sütunundan benzersiz değerleri alıyor ve ekrana yazdırıyoruz.

```python
benzersiz_degerler = df['B'].unique()

print("B Sütunundaki Benzersiz değerler:")
print(benzersiz_degerler)
```

Çıktı:

```py
B Sütunundaki Benzersiz değerler:
['B1' 'B2' 'B3' 'B4']
```

Bir de "D" Sütunundaki benzersiz değerleri görelim.

```python
benzersiz_degerler = df['D'].unique()

print("D Sütunundaki Benzersiz değerler:")
print(benzersiz_degerler)
```

Çıktı:

```python
D Sütunundaki Benzersiz değerler:
['D1' 'D2']
```

# `nunique()` Metodu

**Benzersiz değerlerin miktarını (kaç adet olduğunu) bulmak** için `nunique()` Metodunu kullanabiliriz. 

**nunique**:  Number of Unique yani Benzersiz Sayısı ifadesini temsil etmektedir.

## `nunique()` Metodunun Kullanımı

**Sözdizimi**:

```python
Veri_Çerçevesi_Adı.nunique(axis=0, dropna=True)

# Aşağıdaki şekilde Sütun ismi belirterek te kullanılabilir;
Veri_Çerçevesi_Adı["Sütun_Adı"].nunique(axis=0, dropna=True)
```

## Parametreler

### axis

`axis` parametresinin alabileceği değer:

* **0**  : Sütun bazında benzersiz değerleri listeler.

* **1** : Satır bazında benzersiz değerleri listeler.

Varsayılan değer **0**'dır. Yani **Sütun bazında** benzersiz değerleri listeler.

### dropna

Bu parametre sayesinde **NaN** (eksik, kayıp, boş, geçersiz) değerlerin sayıma dahil edilip edilmeyeceği belirlenir. `dropna` **bool** yani mantıksal değer alır. Parametrenin alabileceği değer:

* **True**

* **False**

Varsayılan değer **True**'dur.  `True`değeri ile Eksik / Kayıp veri **dikkate alınmaz, yok sayılır**. `False` değeri ise eksik/kayıp veriyi de benzersiz bir veri olarak görür, hesaba dahil eder.

Yukarıdaki veri çerçevesinin her bir sütunundaki benzersiz değerlerin miktarını tespit etmek için `nunique()` Fonksiyonunu kullanalım.

```python
# "A" Sütunundaki benzersiz verileri tespit edelim
benzersiz_degerler_A = df['A'].nunique()
# Print the number of unique values
print("'A' Sütunundaki benzersiz veri sayısı:", benzersiz_degerler_A)

# "B" Sütunundaki benzersiz verileri tespit edelim
benzersiz_degerler_B = df['B'].nunique()
# Print the number of unique values
print("'B' Sütunundaki benzersiz veri sayısı:", benzersiz_degerler_B)

# "C" Sütunundaki benzersiz verileri tespit edelim
benzersiz_degerler_C = df['C'].nunique()
# Print the number of unique values
print("'C' Sütunundaki benzersiz veri sayısı:", benzersiz_degerler_C)

# "D" Sütunundaki benzersiz verileri tespit edelim
benzersiz_degerler_D = df['D'].nunique()
# Print the number of unique values
print("'D' Sütunundaki benzersiz veri sayısı:", benzersiz_degerler_D)

# "E" Sütunundaki benzersiz verileri tespit edelim
benzersiz_degerler_E = df['E'].nunique()
# Print the number of unique values
print("'E' Sütunundaki benzersiz veri sayısı:", benzersiz_degerler_E)
```

Çıktı:

```python
'A' Sütunundaki benzersiz veri sayısı: 5
'B' Sütunundaki benzersiz veri sayısı: 4
'C' Sütunundaki benzersiz veri sayısı: 3
'D' Sütunundaki benzersiz veri sayısı: 2
'E' Sütunundaki benzersiz veri sayısı: 1
```

Kodu daha kısa yazarak ta **tüm sütunlardaki benzersiz değerleri** tek seferde elde edebiliriz;

```python
print(df.nunique())
```

Çıktı:

```python
A    5
B    4
C    3
D    2
E    1
dtype: int64
```

# Parametreler

## `axis` Parametresi

`axis` parametresi ile, **satır** ve **sütunlardaki** benzersiz değerleri tespit edelim.
`axis = 0` ile **sütunlardaki** benzersiz verileri bulalım;

```python
print(df.nunique(axis = 0))    # Bu ifade print(df.nunique()) ile aynıdır.
```

Çıktı:

```python
A    5
B    4
C    3
D    2
E    1
dtype: int64
```

`axis = 1` ile **satırlardaki** benzersiz verileri bulalım;

```python
df.nunique(axis = 1)
```

Çıktı:

```python
0    5
1    5
2    5
3    5
4    5
dtype: int64
```

İndex değerlerini değiştirip satırlardaki benzersiz değerleri tekrar bulmaya çalışalım;

```python
yeni_index = ["satir_1","satir_2","satir_3","satir_4","satir_5"]
df.index = yeni_index
print(df)
```

|         | A   | B   | C   | D   | E   |
| ------- | --- | --- | --- | --- | --- |
| satir_1 | A1  | B1  | C1  | D1  | E1  |
| satir_2 | A2  | B2  | C2  | D2  | E1  |
| satir_3 | A3  | B3  | C3  | D2  | E1  |
| satir_4 | A4  | B4  | C3  | D2  | E1  |
| satir_5 | A5  | B4  | C3  | D2  | E   |

```python
print(df.nunique(axis = 1))
```

Çıktı:

```python
satir_1    5
satir_2    5
satir_3    5
satir_4    5
satir_5    5
dtype: int64
```

## `dropna` Parametresi

Sıra geldi `dropna` Parametresini incelemeye. **B** sütunu ve **satir_4** isimli satırın kesişimindeki değeri `pd.NA` olarak değiştirelim.

```python
df.iloc[3,1] = pd.NA
print(df)
```

|         | A   | B   | C   | D   | E   |
| ------- | --- | --- | --- | --- | --- |
| satir_1 | A1  | B1  | C1  | D1  | E1  |
| satir_2 | A2  | B2  | C2  | D2  | E1  |
| satir_3 | A3  | B3  | C3  | D2  | E1  |
| satir_4 | A4  |     | C3  | D2  | E1  |
| satir_5 | A5  | B4  | C3  | D2  | E1  |

Artık Veri çerçevemizde bir eksik verimiz bulunuyor. `nunique()` fonksiyonunu parametresiz ya da `axis = 0` parametresi ile çalıştırıp sonuca bakalım.

```python
print(df.nunique(axis = 0))    # print(df.nunique()) ile aynıdır.
```

Çıktı:

```python
A    5
B    4
C    3
D    2
E    1
dtype: int64
```

**B** Sütununda **4 adet** benzersiz değer tespit edildi. Şimdi bir de `dropna=True` değeri ile sonucu inceleyelim;

Çıktı:

```python
A    5
B    4
C    3
D    2
E    1
dtype: int64
```

Yukarıdaki ile aynı sonucu elde ettik yani `dropna` parametresi Varsayılan olarak `True` değeri ile Eksik / Kayıp veriyi dikkate almadı.

Peki `dropna` parametresi `False` değeri alırsa, benzersiz değerler hesaplanırken Eksik / Kayıp veriyi dikkate alınacak mı? İnceleyelim.

```python
df.nunique(dropna=False)    # eksik verileri görmezden gelme, say.
```

Çıktı:

```python
A    5
B    5
C    3
D    2
E    1
dtype: int64
```

Çıktıya bakınca görüyoruz ki, eksik / kayıp veri de bir değer olarak kabul edilmiş. **B** sütununda toplam **5 adet** benzersiz değer hesaplanmış.

**E** Sütununa ait **satir_4** isimli satırındaki değeri de silelim.

```python
df.iloc[3,4] = pd.NA
print(df)
```

|         | A   | B    | C   | D   | E    |
| ------- | --- | ---- | --- | --- | ---- |
| satir_1 | A1  | B1   | C1  | D1  | E1   |
| satir_2 | A2  | B2   | C2  | D2  | E1   |
| satir_3 | A3  | B3   | C3  | D2  | E1   |
| satir_4 | A4  | <NA> | C3  | D2  | <NA> |
| satir_5 | A5  | B4   | C3  | D2  | E1   |

E sütununda kaç adet benzersiz değer varmış görelim;

```python
df.E.nunique(dropna=False)
```

Çıktı:

```python
2
```

Peki **satir_4** isimli satırda kaç adet benzersiz veri var dersiniz?

```python
print(df.nunique(axis=1, dropna=True))
```

Çıktı:

```python
satir_1    5
satir_2    5
satir_3    5
satir_4    3
satir_5    5
dtype: int64
```

Sonuç 3 olarak görünüyor. Peki Eksik / kayıp verileri de hesaba dahil edersek sonuç ne olur? görelim;

```python
print(df.nunique(axis=1, dropna=False))
```

Çıktı:

```python
satir_1    5
satir_2    5
satir_3    5
satir_4    4
satir_5    5
dtype: int64
```

Eksik / kayıp verileri de hesaba dahil edince **satir_4** isimli satırda toplam **4 adet** benzersiz değer olduğu tespit edilmiş oldu.

# Ek Bilgi

`unique ()` Fonksiyonuna ek olarak, bir Pandas veri çerçevesinden benzersiz değerleri almanın başka yolları da vardır:

- [drop_duplicates() Fonksiyonu]({filename}drop_duplicates.md)
- [value_counts() Fonksiyonu]({filename}value_counts.md)
- `set()` Fonksiyonu ( aşağıda açıklanıyor )

# `set()` Metodu

Python öğrenirken veri tipleri konusunda karşılaştığımız gömülü fonksiyonlardan biri olan `set()` (küme) fonksiyonunu, Veri çerçevelerindeki benzersiz verileri tespit etmek için kullanabiliriz. 

## `set()` Metodunu Hatırlayalım

`set()` fonksiyonunun görevi farklı veri tiplerini kümeye (küme yapısına) dönüştürmektir. Küme yapısı, matematikte gördüğümüz kümelerde olduğu gibi, bir elemandan **sadece bir tane** barındırmaya izin verir.

Yukarıdaki Veri çerçevesinin '**C**' Sütunundaki benzersiz veri sayısını set() fonksiyonu yardımı ile tespit edelim.

```python
print(set(df["C"]))    # print(set(df.C)) şeklinde de kullanılabilir.
```

Çıktı:

```python
{'C3', 'C2', 'C1'}
```

Görüldüğü üzere çıktı Küme yani set veri tipinde.

**Kümeler** sözlükler gibi **sıralı veri tipi değildir**. Bu yüzden indexleme desteklemez. Kümeler tek başına gereksiz görünse de birden fazla küme olduğu zaman çokça ihtiyacınız olacak ve o zaman kümelerin ne  kadar gerekli olduğunu göreceksiniz.

# Kaynak:

* [Get unique values from a column in Pandas DataFrame - GeeksforGeeks](https://www.geeksforgeeks.org/python/get-unique-values-from-a-column-in-pandas-dataframe/)
