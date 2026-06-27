Title: Pandas - add
Date: 2025-11-29 14:16
Modified: 2025-11-29 14:16
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, add
Author: Mustafa Halil

# `add()` Metodu

`pandas.DataFrame.add` metodu, bir DataFrame ile başka bir nesneyi **öğe bazında (element-wise) toplamak** için kullanılan ikili bir operatör sarmalayıcısıdır.

## Sözdizimi:

```python
DataFrame.add(other, axis='columns', level=None, fill_value=None)
```

### Aşama 1: Temel Amaç ve Eşdeğerlik

1. **Basit Toplama:** Bu metodun temel amacı, bir DataFrame'in her bir hücresini (elementini) başka bir değerle (skaler, Seri veya başka bir DataFrame) toplamaktır.

2. **Operatör Eşdeğerliği:** `DataFrame.add` metodu, Python'daki standart **dataframe + other** operatörüne eşdeğerdir.

3. **Esnek Sarmalayıcılar:** Bu metot, `+`, `-`, `*`, `/`, `%` gibi aritmetik operatörler için oluşturulmuş **esnek sarmalayıcılar** (flexible wrappers) grubuna aittir (`sub`, `mul`, `div`, `pow` gibi diğer işlemler de bu gruba dahildir)

### Aşama 2: Esnekliğin Anlamı (Neden `+` yerine `add` kullanılır?)

Standart `+` operatörü ile toplama yapabilirsiniz, ancak `add` gibi esnek sarmalayıcıları kullanmanın en büyük avantajı, eksik veriler (NaN) için bir doldurma değeri (****fill_value****) belirleme desteği sunmasıdır.

1. **Hizalama (Alignment):** İki DataFrame'i veya bir DataFrame ile bir Seriyi topladığınızda, Pandas otomatik olarak **uyumsuz dizinleri birleştirir** (unioned together). Yani, her iki veri yapısında da mevcut olmayan satır veya sütunlar varsa, bunlar sonuç DataFrame'e eklenir.

2. **Eksik Veri Doldurma (fill_value)**: Eğer topladığınız iki girişten birinde veri eksikse (`NaN`), hesaplama yapılmadan önce bu eksik değerlerin yerine bir `fill_value` koyabilirsiniz.

>  **Önemli Not:** Eğer her iki girişin de aynı konumdaki verileri eksikse (`NaN` ise), doldurma değeri uygulansa bile sonuç yine eksik (`NaN`) olacaktır.

### Aşama 3: Parametreler (İşlemi Nasıl Yönlendirirsiniz?)

`add` metodu, toplama işlemini kontrol etmenizi sağlayan birkaç önemli parametre alır:

| Parametre      | Ne Anlama Gelir?                                                                                                                                                             |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **other**      | Toplama işleminin yapılacağı diğer nesnedir. Bu, bir sayı (skaler), dizi, Series, sözlük veya başka bir DataFrame olabilir.                                                  |
| **axis**       | İşlemin hangi eksende eşleşeceğini belirtir. `0` veya `'index'` (satırlar arası eşleştirme) ya da `1` veya `'columns'` ise (sütunlar arası eşleştirme) olarak ayarlanabilir. |
| **fill_value** | Hesaplama öncesinde eksik (`NaN`) değerlerin yerine konulacak değerdir.                                                                                                      |
| **level**      | MultiIndex (Çoklu Dizin) kullanılıyorsa, eşleştirmenin hangi dizin seviyesinde yapılacağını belirtir.                                                                        |

`axis` parametresi için kullanabileceği iki ana değer vardır:

| Değer                        | Anlamı                                   | Eşleştirme Yönü        |
| ---------------------------- | ---------------------------------------- | ---------------------- |
| **0** **veya** **'index'**   | **Dizin (Satırlar)** boyunca karşılaştır | Yatay (Satır İsimleri) |
| **1** **veya** **'columns'** | **Sütunlar** boyunca karşılaştır         | Dikey (Sütun İsimleri) |

> **Önemli Not:** `DataFrame.add` metodunda varsayılan (default) değer **'columns'** (yani 1) olarak ayarlanmıştır.

### Aşama 4: Basit Uygulama Örnekleri

Örnek Veri Çerçevemiz;

```python
import pandas as pd

df = pd.DataFrame({'angles': [0, 3, 4],
                    'degrees': [360, 180, 360]},
                    index=['circle', 'triangle', 'rectangle'])
print(df)
```

**Çıktı**:

```python
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360
```

**1. Skaler Değer ile Matematiksel İşlemler**

**TOPLAMA İŞLEMİ**

Bir DataFrame'e sabit bir değer eklemek istediğinizde, hem toplama  (`+`) operatörü hem de `add` metodunu kullanabilirsiniz ve sonuçlar aynı olacaktır.

**Girdi (Örnek DataFrame** **df**):

* 'angles' (Açılar) sütununda 0, 3, 4 değerleri.

* **İşlem:** `df + 1` veya `df.add(1)`.

* **Sonuç:** DataFrame'deki her bir değer 1 artar (0 olur 1, 360 olur 361 vb.).

**Kod ve Çıktısı:**

```python
print(df.add(1))    # print(df + 1) işlemi ile eşdeğer 
```

Çıktı:

```python
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361
```

**ÇIKARMA İŞLEMİ:**

İlk sütundan (**angles**) **1** değerini, ikinci sütundan (**degrees**) **2** değerini çıkaralım.

```python
df.sub([1, 2], axis='columns')    #  print(df - [1, 2]) işlemi ile eşdeğer
```

Çıktı:

```python
          angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358
```

`axis` parametresi ile eksenlere göre liste ve seriyi çıkaralım;

```python
print(df.sub(pd.Series([1, 3, 5], 
            index=['circle', 'triangle', 'rectangle']), 
            axis='index'))
```

Çıktı:

```python
           angles  degrees
circle         -1      359
triangle        0      177
rectangle      -1      355
```

Görüldüğü gibi, `circle` satırından `1`, `triangle` satırından `3` ve `rectangle` satırından `5` değerleri çıkarıldı.

**BÖLME İŞLEMİ:**

Orjinal Veri çerçevesindeki tüm değerleri 10'a bölelim;

```python
print(df.div(10))    # print(df / 10) işlemi ile eşdeğer
```

Çıktı:

```python
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0
```

**ÇARPMA İŞLEMİ:**

Basit çarpma işlemi yapalım;

```python
print(df.mul(5))    # print(df * 5) ile eşdeğer
```

Çıktı:

```python
           angles  degrees
circle          0     1800
triangle       15      900
rectangle      20     1800
```

Eksenleri (sütunları) bir Sözlük yapısı ile belirtilen değerğerle çarpalım;

```python
print(df.mul({'angles': 0, 'degrees': 2}))
```

Çıktı:

```python
           angles  degrees
circle          0      720
triangle        0      360
rectangle       0      720
```

`angles` sütununu`0` ile `degrees` sütununu `2` değeri ile çarpmış olduk.

Bir de satırlara göre farklı değerlerle çarpma işlemi uygulayalım;

```python
print(df.mul({'circle': 0, 
            'triangle': 2, 
            'rectangle': 3}, 
            axis='index'))
```

Çıktı:

```python
           angles  degrees
circle          0        0
triangle        6      360
rectangle      12     1080
```

`circle` satırı `0` ile, `triangle` satırı `2` ile, `rectangle` satırı da `3` ile çarpıldı.

**2. Uyumsuz Şekillerle Çalışma ve** **`fill_value**` **Kullanımı**

`fill_value` parametresinin kullanımı, `add` metodunun (ve diğer `mul`, `sub` ve `div` gibi esnek sarmalayıcıların) gücünü gösterir. Farklı şekillerdeki iki DataFrame'i çarptığımızı varsayalım. 

• **Senaryo:** iki sütunlu `df` ile sadece tek bir sütunu olan `other` isimli başka bir DataFrame'i çarpmak (`mul`) istiyoruz.

• **Operatör Kullanımı (df other):** Eğer `other`'da olmayan bir sütun varsa (örneğin 'degrees'), bu sütundaki sonuçlar `NaN` (Not a Number - Eksik değer) olarak döner.

• **Esnek Metot Kullanımı (`df.mul(other, fill_value=0)`**): Eğer `fill_value=0` olarak ayarlanırsa, ikinci DataFrame'de (`other`) eksik olan yerler hesaplama yapılmadan önce 0 ile doldurulur. Böylece, normalde `NaN` olacak çarpma sonuçları (çünkü 0 ile çarpılır), 0.0 olarak döner.

> Bu, `add` metodu için de geçerlidir. Eğer toplama işleminde eksik verilerinizi 0 ile doldurursanız, o verilerin kaybolmasını engellemiş olursunuz.

**İKİ FARKLI VERİ ÇERÇEVESİNİ ÇARPALIM:**

Öncelikle `other` adında `angles` adında tek sütundan oluşan bir veri çerçevesi oluşturalım.

```python
other = pd.DataFrame({'angles': [0, 3, 4]},
                     index=['circle', 'triangle', 'rectangle'])

print(other)
```

Çıktı:

```python
           angles
circle          0
triangle        3
rectangle       4
```

Şimdi `df` ile `other` tablolarını çarpalım;

```python
print(df.mul(other))    # print(df * other) ile eşdeğer
```

Çıktı:

```python
           angles  degrees
circle          0      NaN
triangle        9      NaN
rectangle      16      NaN
```

`other` tablomuzda `degrees` sütunu olmadığı için çarpma işlemi sonucundaki `degrees` sütunu değerleri `NaN` olarak karşımıza çıktı.

Bu sorunu çözmek için `fill_value` parametresinden yararlanabiliriz;

```python
print(df.mul(other, fill_value=0))
```

Çıktı:

```python
           angles  degrees
circle          0      0.0
triangle        9      0.0
rectangle      16      0.0
```

**İKİ FARKLI VERİ ÇERÇEVESİNİ TOPLAMAYALIM:**

Önce `df2` isimli `angles` adında tek sütundan oluşan bir veri çerçevesi oluşturalım. Hem `df` hem de `df2` tablomuza bakalım;

```python
df2 = pd.DataFrame({'angles': [50, 60, 70]},
                     index=['circle', 'triangle', 'rectangle'])

print("df:\n", df)
print("df2:\n", df2)
```

Çıktı:

```python
df:
            angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

df2:
            angles
circle         50
triangle       60
rectangle      70
```

Şimdi bu iki tablomuzu `add` metodu ile toplayalım;

```python
print(df.add(df2))
```

Çıktı:

```python
           angles  degrees
circle         50      NaN
triangle       63      NaN
rectangle      74      NaN
```

`df2` tablomuzda `degrees` sütunu olmadığı için toplama işlemi sonucundaki `degrees` sütunu değerleri `NaN` olarak karşımıza çıktı.

Bu sorunu çözmek için yine `fill_value` parametresinden yararlanıyoruz;

```python
print(df.add(df2, fill_value=0))
```

Çıktı:

```python
           angles  degrees
circle         50    360.0
triangle       63    180.0
rectangle      74    360.0
```

`fill_value=0` olarak ayarlandığı için, ikinci DataFrame'de (`df2`) eksik olan yerler hesaplama yapılmadan önce `0` ile dolduruldu. Böylece, normalde `NaN` olacak toplama işlemi sonuçları, (`0` ile toplandığı için) geçerli bir değer olarak döndü.

## Kaynaklar:

* [pandas.DataFrame.add &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add.html)
* [Google NotebookLM](https://notebooklm.google.com)
