Title: Pandas - mode
Date: 2025-11-30 23:24
Modified: 2025-11-30 23:24
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, mode
Author: Mustafa Halil

# `mode()` Metodu

Sayısal bir veri serisi içindeki **en çok tekrar eden sayı, o serinin modu** olarak adlandırılır.   `pandas.DataFrame.mode()` metodu, bir DataFrame'in **satırları** veya **sütunları** boyunca **en sık tekrar eden** (mod) değerleri bulur. Sonuç olarak, orijinal DataFrame ile **aynı indekslere** ve **aynı sütun isimlerine** sahip **yeni bir DataFrame** döndürür. Bazı serilerde maksimum tekrar sayısına sahip birden fazla seri elemanı olabilir. Bu durumda, serinin birden fazla modu olur.

## Sözdizimi:

```python
 DataFrame.mode(axis=0, numeric_only=False, dropna=True)
```

### Temel Özellikler ve Davranış

- **Veri Tipleri:** Mod, sayısal, kategorik ve metinsel (string) tüm veri tipleri için hesaplanabilir.

- **Birden Fazla Mod:** Bir sütunda **birden fazla** değer aynı en yüksek frekansta görünüyorsa (yani birden fazla mod varsa), fonksiyon bu mod değerlerinin **hepsini** döndürür. Bu nedenle, sonuç DataFrame'i genellikle **orijinal DataFrame'den daha fazla satıra** sahip olabilir.
  
  - Örneğin, bir sütunda `[1, 2, 2, 3, 3, 4]` değerleri varsa, hem **2** hem de **3** moddur. Sonuç DataFrame'inde bu sütun için iki ayrı satırda hem 2 hem de 3 yer alacaktır.

- **`NaN` Değerleri:** Varsayılan olarak, `NaN` (Not a Number - Eksik Değer) değerler hesaplamaya **dahil edilmez**. Mod, yalnızca geçerli (non-NaN) değerler arasında bulunur.

- **Sonuç Tipi:** Her zaman bir **DataFrame** döndürür.

## Parametreler

Fonksiyonun iki ana parametresi vardır:

1. **`axis` (Eksen)**: Modun hangi eksen boyunca hesaplanacağını belirtir.
   
   - `axis=0` (Varsayılan): **Sütunlar boyunca** (yani her bir sütunun modunu) hesaplar. Bu en yaygın kullanımdır.
   
   - `axis=1`: **Satırlar boyunca** (yani her bir satırın modunu) hesaplar. Satırın modunun ne olduğu daha az kullanılır.

2. **`numeric_only` (Yalnızca Sayısal)**: Modun sadece sayısal sütunlar için mi hesaplanacağını belirtir.
   
   - `False` (Varsayılan): Tüm sütunları (sayısal ve sayısal olmayan) dahil eder.
   
   - `True`: Yalnızca sayısal veri tiplerine sahip sütunları dahil eder.

## Örnekler

Bir ankette en çok verilen cevabı veya bir mağazada en çok satılan ürünü bulmak gibi **kategorik veri analizi** yaparken oldukça kullanışlıdır.

```python
import pandas as pd
import numpy as np

# Örnek DataFrame
data = {'A': [1, 2, 2, 3, 4],
        'B': ['elma', 'armut', 'elma', 'muz', 'elma'],
        'C': [5, 6, 6, 7, 7]}
df = pd.DataFrame(data)
print(df)
```

Çıktı:

```python
   A      B  C
0  1   elma  5
1  2  armut  6
2  2   elma  6
3  3    muz  7
4  4   elma  7
```

Her sütunun modunu hesaplayalım; 

```python
# Her sütunun modunu hesapla (axis=0 varsayılan)
sonuc = df.mode()
print(sonuc)
```

```python
     A     B  C
0  2.0  elma  6
1  NaN   NaN  7
```

**Çıktı Analizi:**

- **A Sütunu:** 2 ve 3, aynı sıklıkta (birer kez) tekrar ettiği için **iki mod** olarak döndürüldü.

- **B Sütunu:** "elma" en sık görülen değerdir (**tek mod**).

- **C Sütunu:** 6 ve 7, aynı sıklıkta (ikişer kez) tekrar ettiği için **iki mod** olarak döndürüldü.

- A ve C sütunlarının birden fazla modu olduğu için sonuç DataFrame'i **iki satırdan** oluşur ve ikinci modun olmadığı yerlere `NaN` atılır.

### **`axis`** parametresini somut bir örnekle inceleyelim.

Veri çerçevemiz aşağıdadır;

```python
import pandas as pd
import numpy as np

# Örnek DataFrame oluşturma
data = {
    'Sayı1': [10, 20, 20, 30, 30, 40],
    'Sayı2': [5, 5, 5, 8, 8, 9],
    'Kategori': ['A', 'B', 'A', 'C', 'A', 'B'],
    'Fiyat': [1.5, 1.5, np.nan, 2.0, 2.0, 2.0]
}
df = pd.DataFrame(data)

print("--- Orijinal DataFrame ---")
print(df)
```

Çıktı:

```python
--- Orijinal DataFrame ---
   Sayı1  Sayı2 Kategori  Fiyat
0     10      5        A    1.5
1     20      5        B    1.5
2     20      5        A    NaN
3     30      8        C    2.0
4     30      8        A    2.0
5     40      9        B    2.0
```

#### **`axis=0` Kullanımı (Varsayılan);**

Bu, modun **sütunlar boyunca** (her bir sütunun en sık görülen değeri) hesaplandığı varsayılan davranıştır.

```python
# Varsayılan (axis=0, numeric_only=False)
mod_sutunlar = df.mode()
print("\n--- Sonuç 1: Sütunların Modu (axis=0) ---")
print(mod_sutunlar)
```

Çıktı:

```python
--- Sonuç 1: Sütunların Modu (axis=0) ---
   Sayı1  Sayı2 Kategori  Fiyat
0     20    5.0        A    2.0
1     30    NaN      NaN    NaN
```

💡 **Çıktı Analizi:**

| Sütun        | Değerler                         | Mod Değer(ler)i | Açıklama                                                      |
| ------------ | -------------------------------- | --------------- | ------------------------------------------------------------- |
| **Sayı1**    | 10, **20, 20**, **30, 30**, 40   | 20, 30          | Hem 20 hem de 30 ikişer kez tekrar ediyor (Birden Fazla Mod). |
| **Sayı2**    | **5, 5, 5**, 8, 8, 9             | 5               | 5, üç kez tekrar ederek en sık görülen değerdir (Tek Mod).    |
| **Kategori** | **A**, B, **A**, C, **A**, B     | A               | A, üç kez tekrar ederek en sık görülen değerdir (Tek Mod).    |
| **Fiyat**    | 1.5, 1.5, NaN, **2.0, 2.0, 2.0** | 2.0             | `NaN` hariç, 2.0 üç kez tekrar ediyor.                        |

**Gördüğünüz gibi:** `Sayı1` sütununda iki mod olduğu için sonuç DataFrame'i iki satır döndürmüş, diğer sütunlarda tek mod olduğu için ikinci satırda `NaN` (veya ilgili veri tipinin karşılığı) görünmüştür.

#### `axis=1` **Kullanımı:**

Bu, modun **satırlar boyunca** (her bir satırın en sık görülen değeri) hesaplandığı durumdur. Bu, genellikle bir satırdaki bazı değerlerin (örneğin anket cevapları) tekrar edip etmediğini kontrol etmek için kullanılır.

```python
# Satırların Modu
mod_satirlar = df.mode(axis=1)
print("\n--- Sonuç 3: Satırların Modu (axis=1) ---")
print(mod_satirlar)
```

Çıktı:

```python
--- Sonuç 3: Satırların Modu (axis=1) ---
    0  1  2    3
0  10  5  A  1.5
1  20  5  B  1.5
2  20  5  A  NaN
3  30  8  C  2.0
4  30  8  A  2.0
5  40  9  B  2.0
```

💡 **Çıktı Analizi:**

| Satır İndeksi | Değerler          | Mod Değer(ler)i | Açıklama                                    |
| ------------- | ----------------- | --------------- | ------------------------------------------- |
| **0**         | [10, 5, 'A', 1.5] | NaN             | Tüm değerler farklıdır, mod yoktur.         |
| **1**         | [20, 5, 'B', 1.5] | NaN             | Tüm değerler farklıdır, mod yoktur.         |
| **2**         | [20, 5, 'A', NaN] | NaN             | Tüm geçerli değerler farklıdır, mod yoktur. |
| **3**         | [30, 8, 'C', 2.0] | NaN             | Tüm değerler farklıdır, mod yoktur.         |
| **4**         | [30, 8, 'A', 2.0] | NaN             | Tüm değerler farklıdır, mod yoktur.         |
| **5**         | [40, 9, 'B', 2.0] | NaN             | Tüm değerler farklıdır, mod yoktur.         |

**Not:** Bu örnekte, her satırdaki tüm değerler birbirinden farklı olduğu için (NaN'lar hariç), mod bulunamadı ve sonuç olarak `NaN` döndürüldü.

**Satır Modu için Ek Örnek (Daha Net Olması İçin)**

Eğer DataFrame'i aşağıdaki gibi olsaydı:

```python
df_row_test = pd.DataFrame({'a': [1, 2, 2], 'b': [1, 5, 6], 'c': [1, 5, 2]})
print("\n--- Satır Modu Test DataFrame ---")
print(df_row_test)
```

Çıktı:

```python
--- Satır Modu Test DataFrame ---
   a  b  c
0  1  1  1
1  2  5  5
2  2  6  2
```

Satırların modunu bulalım;

```python
print(df_row_test.mode(axis=1))
```

Çıktı:

```python
   0
0  1
1  5
2  2
```

**Satır Modu Test Çıktı Analizi:**

| Satır İndeksi | Değerler  | Mod Değer(ler)i |
| ------------- | --------- | --------------- |
| **0**         | [1, 1, 1] | 1               |
| **1**         | [2, 5, 5] | 5               |
| **2**         | [2, 6, 2] | 2               |

Bu test örneğinde, **satır 0**'ın modu **1**, **satır 1**'in modu **5** ve **satır 2**'nin modu **2** olacaktır. `axis=1` bu şekilde çalışır.

### **`numeric_only`** parametresini somut bir örnekle inceleyelim.

#### `numeric_only=True` **Kullanımı**

Veri çerçevemiz aşağıdaki gibi olsun;

```python
import pandas as pd
import numpy as np

# Örnek DataFrame oluşturma
data = {
    'Sayı1': [10, 20, 20, 30, 30, 40],
    'Sayı2': [5, 5, 5, 8, 8, 9],
    'Kategori': ['A', 'B', 'A', 'C', 'A', 'B'],
    'Fiyat': [1.5, 1.5, np.nan, 2.0, 2.0, 2.0]
}
df = pd.DataFrame(data)

print("--- Orijinal DataFrame ---")
print(df)
```

Çıktı:

```python
--- Orijinal DataFrame ---
   Sayı1  Sayı2 Kategori  Fiyat
0     10      5        A    1.5
1     20      5        B    1.5
2     20      5        A    NaN
3     30      8        C    2.0
4     30      8        A    2.0
5     40      9        B    2.0
```

Bu parametre `axis=0` (sütun modu) ile birlikte kullanıldığında, sadece **sayısal veri tipine sahip sütunların** modunun hesaplanmasını sağlar.

```python
# Yalnızca Sayısal Sütunların Modu
mod_sayisal = df.mode(numeric_only=True)
print("\n--- Sonuç 2: Sadece Sayısal Sütunların Modu (numeric_only=True) ---")
print(mod_sayisal)
```

Çıktı:

```python
--- Sonuç 2: Sadece Sayısal Sütunların Modu (numeric_only=True) ---
   Sayı1  Sayı2  Fiyat
0     20    5.0    2.0
1     30    NaN    NaN
```

💡 **Çıktı Analizi:**

| Sütun        | Mod Değer(ler)i | Açıklama                                                   |
| ------------ | --------------- | ---------------------------------------------------------- |
| **Kategori** | Yok             | Bu sütun sayısal olmadığı için sonuçtan **çıkarılmıştır**. |
| **Sayı1**    | 20, 30          | Değişmedi (öncekiyle aynı).                                |
| **Sayı2**    | 5               | Değişmedi (öncekiyle aynı).                                |
| **Fiyat**    | 2.0             | Değişmedi (öncekiyle aynı).                                |

**Gördüğünüz gibi:** `Kategori` sütunu, `numeric_only=True` ayarı sayesinde sonuç DataFrame'inde yer almaz.

## Kaynaklar:

* [pandas.DataFrame.mode &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html)
* [Google Gemini](https://gemini.google.com)
