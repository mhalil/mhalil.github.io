Title: Pandas - notna
Date: 2025-11-29 12:12
Modified: 2025-11-29 12:25
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, notna
Author: Mustafa Halil

# `notna()` Metodu

`pandas.notna()` metodu, bir dizi benzeri nesne için **eksik olmayan (geçerli) değerleri tespit etmek** amacıyla kullanılır.

Giriş nesnesinin veya dizisinin `NaN`, `None` veya `NaT` (Zaman Değil) gibi tanınan eksik değerler içerip içermediğini kontrol eder. Kontrol sonucunda, geçerli olması durumunda `True`, eksik olması durumunda ise `False` değerini döndüren bir **boolean** sonuç üretir. 

Metot, skaler girdileri, **NumPy** dizilerini veya **Series**, **DataFrame** ve **Index** gibi daha büyük pandas nesnelerini kabul ederek farklı veri türlerinde çok yönlülüğünü gösterir. 

• Bu metot, bir skalar (tekil) veya dizi benzeri bir nesneyi girdi olarak alır ve değerlerin geçerli olup olmadığını (yani, eksik değer olup olmadığını) belirtir.

• Eksik değerler, sayısal dizilerde `NaN` (Not a Number), nesne dizilerinde `None` veya `NaN`, tarih/saat benzeri dizilerde ise `NaT` (Not a Time) olarak kabul edilir.

## Sözdizimi:

```python
pandas.notna(obj)
```

## Parametreler ve Dönüş Değeri

### Parametre:

* **`obj`**: Eksik olmayan veya boş olmayan değerler için **kontrol edilecek dizi benzeri veya nesne** değeridir.

### Dönüş Değeri:

* Girdi, bir **skalar** ise, skalar bir **boolean** (mantıksal) değer döndürülür.

* Girdi bir **dizi** ise, karşılık gelen her öğenin geçerli olup olmadığını gösteren **boolean'lardan oluşan bir dizi** döndürülür.

### İlgili Metotlar ve Yapılar

Aşağıdaki metotlar ve yapılar `pandas.notna` ile ilişkilidir:

• `pandas.notna`: `isna` metodunun tersidir.

• `Series.notna`: Bir Series içindeki geçerli değerleri tespit eder.

• `DataFrame.notna`: Bir DataFrame içindeki geçerli değerleri tespit eder.

• `Index.notna`: Bir Index içindeki geçerli değerleri tespit eder.

## Örnekler

### 1. Skalar Argümanlar:

Skalar argümanlar (dizeler dahil) skalar bir boolean ile sonuçlanır:

• `pd.notna('dog')`   çıktısı:   `True`

• `pd.notna(pd.NA)`   çıktısı:   `False`

• `pd.notna(np.nan)`   çıktısı:   `False`

### 2. NumPy Dizileri (ndarrays):

NumPy dizileri boolean'lardan oluşan bir `ndarray` ile sonuçlanır. Örneğin;

```python
array = np.array([[ 1, np.nan, 3 ], [ 4, 5, np.nan ]])
print(array)

"""
Çıktı:

[[ 1. nan  3.]
 [ 4.  5. nan]]

"""
```

için, `pd.notna(array)` çıktısı şudur:

```python
# print(pd.notna(array))

array([[ True, False, True], 
       [ True, True, False]])
```

### 3. Indexler:

Indexler için de **boolean**'lardan oluşan bir `ndarray` döndürülür. İçinde `None` değeri bulunan bir `DatetimeIndex` kontrol edildiğinde:

```python
index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", 
                         None, "2017-07-08"])

print(index)

"""
Çıktı:
DatetimeIndex(['2017-07-05', '2017-07-06', 
            'NaT', '2017-07-08'], 
            dtype='datetime64[ns]', 
            freq=None)
"""
```

```python
# Index yapısında None değeri NaT (Not a Time) olarak görünür
print(pd.notna(index))
```

**Çıktı**: 

```python
array([ True, True, False, True]) 
```

### 4. Series ve DataFrame:

Series ve DataFrame için, boolean değerleri içeren aynı tip yapı döndürülür. Örneğin, eksik değer (`None`) içeren bir DataFrame (df) ele alındığında:

```python
df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
print(df)
```

Çıktı:

```python
     0     1    2
0  ant   bee  cat
1  dog  None  fly
```

`pd.notna(df)` çıktısı şudur (`None` değerinin bulunduğu yerde `False` döner):

```python
  0      1     2
0 True True True
1 True False True
```

Aynı şekilde, bu DataFrame'in sadece bir sütunu (df) kontrol edildiğinde de boolean içeren bir Series döndürülür:

```python
pd.notna(df[1])
```

**Çıktı**: 

```python
0 True, 1 False
```

## Kaynak:

* [pandas.notna &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.notna.html#pandas.notna)