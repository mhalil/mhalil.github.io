Title: Pandas - pd.Grouper
Date: 2025-11-30 12:55
Modified: 2025-11-30 15:10
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, pandas.Grouper, pd.Grouper
Author: Mustafa Halil

## `pandas.Grouper` Nesnesi

`pandas.Grouper`, özellikle bir DataFrame veya Series üzerinde `.groupby()` metodunu kullanırken, **gruplama talimatlarını detaylı bir şekilde belirtmenize** olanak tanıyan bir nesnedir.

En temel amacı, sütun adı veya index seviyesi gibi standart gruplama anahtarlarının yanı sıra, özellikle **zaman serisi verileri** (datetime-like) üzerinde **yeniden örnekleme (resampling)** tabanlı gruplamalar yapmaktır.

Özetle, `pandas.Grouper`, özellikle karmaşık yeniden örnekleme senaryolarında, aralık sınırlarını, etiketleme noktalarını ve başlangıç zamanlarını (`origin`/`offset`) özelleştirmek istediğinizde standart `groupby()` kullanımının ötesine geçerek size esneklik sağlar.

## Parametreler

| Parametre    | Tip / Seçenekler        | Varsayılan    | Açıklama                                                                                                                                                                            |
| ------------ | ----------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`key`**    | `str`                   | `None`        | Gruplama için kullanılacak **sütun adını** (anahtarını) belirtir.                                                                                                                   |
| **`level`**  | `str` veya `int`        | `None`        | Gruplama için kullanılacak **index seviyesini** (adını/numarasını) belirtir.                                                                                                        |
| **`freq`**   | `str` / Frekans Nesnesi | `None`        | Anahtar bir zaman objesi ise (datetime), veriyi yeniden örneklemek için kullanılacak **zaman aralığını** (örneğin: '`1W`', '`D`', '`M`') belirtir.                                  |
| **`axis`**   | `str` veya `int`        | `0` (Index)   | Gruplamanın yapılacağı ekseni (satırlar için `0/index`, sütunlar için `1/columns`) belirtir.                                                                                        |
| **`sort`**   | `bool`                  | `False`       | Ortaya çıkan etiketlerin (grup anahtarlarının) sıralanıp sıralanmayacağını belirtir.                                                                                                |
| **`closed`** | `{'left', 'right'}`     | `None`        | Sadece `freq` kullanıldığında geçerlidir. Zaman aralıklarının hangi ucunun **kapalı (dahil)** olacağını belirtir.                                                                   |
| **`label`**  | `{'left', 'right'}`     | `None`        | Sadece `freq` kullanıldığında geçerlidir. Ortaya çıkan grupları etiketlemek için aralığın hangi sınırının kullanılacağını belirtir.                                                 |
| **`origin`** | `Timestamp` veya `str`  | `'start_day'` | Sadece `freq` kullanıldığında geçerlidir. Gruplama kutularının hesaplanacağı **sabit başlangıç noktasını** ayarlar (örneğin: `'epoch'`, `'start'`, `'start_day'`).                  |
| **`offset`** | `Timedelta` veya `str`  | `None`        | Sadece `freq` kullanıldığında geçerlidir. `origin`'e eklenecek bir **kaydırma (`offset`)** zaman farkını belirtir. (Kullanımdan kaldırılan `base` argümanının yerine geçer.)        |
| **`dropna`** | `bool`                  | `True`        | `True` ise, grup anahtarlarındaki **`NA` (eksik)** değerler içeren satırlar/sütunlar gruplamadan çıkarılır. `False` ise, `NA` değerler de bir grup anahtarı olarak değerlendirilir. |

## 🛠️ Temel Kullanım ve Parametreler

`pandas.Grouper` nesnesi, Pandas'ta en yaygın `groupby()` metodu kullanımı olan, parantez içine doğrudan bir **sütun adı (string)** vermek yerine, bir sütun adını (string) değil, o sütun üzerinde **nasıl bir gruplama yapılacağına dair bir dizi talimatı** içeren bir nesneyi `groupby()` fonksiyonuna iletmemizi sağlar.

Yani bir sütunu seçerken, aynı anda gruplama mantığına dair ek ayarlar (parametrik kontrol) tanımlamanıza olanak tanır.

### Neden "Daha Fazla Kontrol" Sağlar?

Basit bir string (örneğin; `'Tarih'`) sadece sütunun kendisini seçerken, `pd.Grouper(...)` şunları yapmanızı sağlar:

1. **`key='Tarih'`**: Hangi sütunun seçileceğini belirtir (Tıpkı string gibi).

2. **`freq='W'`**: Gruplamayı **rastgele değerler** yerine, **Haftalık** (Weekly) zaman aralıklarına göre yapılacağını söyler.

3. **`closed='left'`**: Haftalık aralıkların sol sınırının (haftanın başlangıcının) gruplamaya dahil edileceğini söyler.

**Özetle:** String sadece **"neye göre"** gruplanacağını söylerken; `pandas.Grouper`, **"neye göre"** gruplanacağını, **"nasıl"** (haftalık mı, aylık mı) ve **"hangi kurallarla"** (aralıkların başlangıcı nasıl olacak) gruplanacağını bir paket halinde `groupby()`'a iletir. Özellikle zaman serisi verilerinde **Yeniden Örnekleme (Resampling)** yapmak için bu kontrol hayati önem taşır.

### Sütun veya Index Seviyesine Göre Gruplama

Standart bir sütuna göre gruplama yapmak için `key` veya `level` parametrelerini kullanabilirsiniz.

- **`key` (str, varsayılan: `None`):** Gruplama yapılacak sütunun adını belirtir.
  
  - *Örnek:* `df.groupby(pd.Grouper(key="Animal"))`

- **`level` (str veya int, varsayılan: `None`):** Gruplama yapılacak index seviyesini belirtir.

### Zaman Serisi Yeniden Örnekleme (Resampling)

`pandas.Grouper`'ın en önemli özelliği, bir tarih/saat sütununa veya indekse göre zaman periyotlarına dayalı gruplama yapmaktır. Bu, `freq` parametresi ile sağlanır.

- **`freq` (str/frekans nesnesi, varsayılan: `None`):** Eğer gruplama anahtarı (`key` veya `level`) bir zaman objesi ise, gruplamanın yapılacağı zaman aralığını belirtir. (örneğin: '`D`' günlük, '`W`' haftalık, '`M`' aylık, '`1H`' saatlik). Bu parametre kullanıldığında, `Grouper` aslında bir **`TimeGrouper`** davranışı sergiler.

- **`closed` ('`left`' veya '`right`'):** Gruplama aralığının hangi ucunun kapalı (dahil) olacağını belirtir. (Sadece `freq` kullanıldığında geçerlidir.)

- **`label` ('`left`' veya '`right`'):** Gruplama sonucunda etiketleme için aralığın hangi sınırının kullanılacağını belirtir. (Sadece `freq` kullanıldığında geçerlidir.)

- **`origin` (Timestamp veya str):** Gruplama kutularının (bin) ayarlanacağı başlangıç zamanını belirtir (örneğin: '`epoch`' veya '`start_day`').

**`orijin`** parametresinde gruplandırmayı ayarlamak için kullanılacak zaman damgaları; Kaynak zaman dilimi, dizinin zaman dilimi ile eşleşmelidir. Dize ise, aşağıdakilerden biri olmalıdır:

‘`epoch`’: kaynak 1970-01-01'dir.

‘`start`’: kaynak, zaman serisinin ilk değeridir

‘`start_day`’: kaynak, zaman serisinin ilk gününün gece yarısıdır

‘`end`’: kaynak, zaman serisinin son değeridir

‘`end_day`’: kaynak, son günün gece yarısıdır

#### Örnek Kullanım (Zaman Serisi)

Diyelim ki, Elimizdeki veri çerçevesinde **"Publish date"** adında bir tarih sütununuz var.

```python
import pandas as pd

df = pd.DataFrame(
   {
       "Publish date": [
            pd.Timestamp("2000-01-02"),
            pd.Timestamp("2000-01-02"),
            pd.Timestamp("2000-01-09"),
            pd.Timestamp("2000-01-16")
        ],
        "ID": [0, 1, 2, 3],
        "Price": [10, 20, 30, 40]
    }
)
print(df)
```

Çıktı:

```python
  Publish date  ID  Price
0   2000-01-02   0     10
1   2000-01-02   1     20
2   2000-01-09   2     30
3   2000-01-16   3     40
```

 Yukarıdaki tablodaki verileri haftalık (`1W`) bazda gruplayıp ortalama almak istediğimizi düşünelim;

```python
# 'Publish date' sütununa göre haftalık gruplama ve ortalama alma
print(df.groupby(pd.Grouper(key="Publish date", freq="1W")).mean()):
```

Çıktı:

```python
               ID  Price
Publish date            
2000-01-02    0.5   15.0
2000-01-09    2.0   30.0
2000-01-16    3.0   40.0
```

Özellikle zaman serisi verilerinde gruplama aralıklarını (bins) nasıl özelleştirebileceğinizi gösteren aşağıdaki örnekler, `pandas.Grouper`'ın gücünü ortaya koyuyor.

Bu örnekler, genellikle **`freq` (frekans)** parametresi ile birlikte kullanılan **`origin` (başlangıç noktası)** ve **`offset` (kaydırma)** parametrelerinin işlevini açıklamaktadır.

## 🕒 Zaman Aralıklarını Ayarlama (`origin` ve `offset`)

Standart `groupby(freq="...")` işlemi, gruplama aralıklarını varsayılan bir başlangıç noktasına göre oluşturur. Ancak bu örnekler, aralıkların başlangıcını sizin belirlediğiniz bir zaman noktasına göre kaydırmanıza olanak tanır.

Bu örnekler için kullanılan başlangıç veri serisi (`ts`) şöyledir:

```python
import numpy as np
import pandas as pd

start, end = '2000-10-01 23:30:00', '2000-10-02 00:30:00'
rng = pd.date_range(start, end, freq='7min')
ts = pd.Series(np.arange(len(rng)) * 3, index=rng)

print(ts)
```

Verimiz;

```python
2000-10-01 23:30:00     0
2000-10-01 23:37:00     3
2000-10-01 23:44:00     6
2000-10-01 23:51:00     9
2000-10-01 23:58:00    12
2000-10-02 00:05:00    15
2000-10-02 00:12:00    18
2000-10-02 00:19:00    21
2000-10-02 00:26:00    24
Freq: 7min, dtype: int64
```

### 1. Varsayılan Gruplama (Kontrol Örneği)

Sadece `freq='17min'` belirtildiğinde, gruplama aralıkları varsayılan başlangıç noktasına göre hesaplanır.

```python
# Sadece frekans belirtildiğinde (Varsayılan davranış)
print(ts.groupby(pd.Grouper(freq='17min')).sum())
```

Çıktı:

```python
2000-10-01 23:14:00     0
2000-10-01 23:31:00     9
2000-10-01 23:48:00    21
2000-10-02 00:05:00    54
2000-10-02 00:22:00    24
Freq: 17min, dtype: int64
```

### 2. Başlangıç Noktasını Belirleme (`origin`)

`origin` parametresi, zaman aralıklarının oluşturulmaya başlanacağı sabit bir zaman noktasını tanımlamanıza olanak tanır. Aralıklar, bu `origin` noktasından başlayarak `freq` kadar ileri veya geri sayılarak oluşturulur.

#### a. Epoch'a Göre Başlatma

`origin='epoch'`, aralık başlangıcını **1970-01-01 00:00:00**'a göre ayarlar.

```python
# Aralıkları Epoch (1970-01-01) baz alınarak 17 dakikalık periyotlarla oluşturur
print(ts.groupby(pd.Grouper(freq='17min', origin='epoch')).sum())
```

Çıktı:

```python
2000-10-01 23:18:00     0
2000-10-01 23:35:00    18
2000-10-01 23:52:00    27
2000-10-02 00:09:00    39
2000-10-02 00:26:00    24
Freq: 17min, dtype: int64
```

#### b. Özel Bir Tarih/Saate Göre Başlatma

`origin` parametresine istediğiniz bir **Timestamp** değerini dize (string) olarak verebilirsiniz.

```python
# Aralıkları '2000-01-01' zaman noktasından başlatır
print(ts.groupby(pd.Grouper(freq='17min', origin='2000-01-01')).sum())
```

Çıktı:

```python
2000-10-01 23:24:00     3
2000-10-01 23:41:00    15
2000-10-01 23:58:00    45
2000-10-02 00:15:00    45
Freq: 17min, dtype: int64
```

### 3. Başlangıç Değerine Göre Kaydırma (`origin='start'`) ve Eşdeğer `offset`

Veri kümesindeki ilk değerin başlangıç noktası olmasını istiyorsanız `origin='start'` kullanabilirsiniz. Bu, veri kümesi içindeki en erken zaman damgasına göre gruplama aralıklarını hizalar.

```python
# Gruplama aralıklarını zaman serisinin ilk değeri olan '2000-10-01 23:30:00'dan başlatır
print(ts.groupby(pd.Grouper(freq='17min', origin='start')).sum())
```

Çıktı:

```python
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64
```

Bu kullanım, belirli bir zaman farkı (`Timedelta`) ile kaydırma yapan `offset` parametresiyle aynı sonucu verebilir.

```python
# offset='23h30min', aralıkları aynı şekilde kaydırır (origin='start' ile eşdeğer)
print(ts.groupby(pd.Grouper(freq='17min', offset='23h30min')).sum())
```

Çıktı:

```python
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64
```

Bu örnekte `offset` değeri, referans noktası olan gece yarısından itibaren veri serisinin başlangıcına kadar olan farkı temsil ederek, `origin='start'` ile aynı hizalamayı sağlamıştır.

### 4. `offset` ile Özel Kaydırma

`offset` parametresi, kullanımdan kaldırılan (deprecated) `base` argümanının yerini almıştır ve bir **timedelta** (zaman farkı) değeri alarak aralık başlangıçlarını kaydırır.

```python
# Aralık başlangıcını 2 dakika ileri kaydırır
print(ts.groupby(pd.Grouper(freq='17min', offset='2min')).sum())
```

Çıktı:

```python
2000-10-01 23:16:00     0
2000-10-01 23:33:00     9
2000-10-01 23:50:00    36
2000-10-02 00:07:00    39
2000-10-02 00:24:00    24
Freq: 17min, dtype: int64
```

Bu, gruplama aralıklarının standart sıfır noktasından (örneğin gece yarısından) 2 dakika sonra başlamasını sağlar. Böylece, **`base=2`** (deprecated argüman) kullanımına eşdeğer bir sonuç elde edilir.

## Temel Timedelta Parametreleri

| Parametre     | Takma Ad | Türkçe Açıklaması                  |
| ------------- | -------- | ---------------------------------- |
| **`Week`**    | `W`      | **Haftalık** frekans.              |
| `Day`         | `D`      | Bir **mutlak gün** (tam 24 saat).  |
| `Hour`        | `h`      | Bir **saat** (60 dakika).          |
| `Minute`      | `min`    | Bir **dakika** (60 saniye).        |
| `Second`      | `s`      | Bir **saniye**.                    |
| `Millisecond` | `ms`     | Bir **milisaniye** (10−3 saniye).  |
| `Microsecond` | `us`     | Bir **mikrosaniye** (10−6 saniye). |
| `Nanosecond`  | `ns`     | Bir **nanosaniye** (10−9 saniye).  |

## Kaynak:

* [pandas.Grouper &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html)
