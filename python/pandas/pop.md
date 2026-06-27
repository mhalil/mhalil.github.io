Title: Pandas - pop
Date: 2025-11-29 15:46
Modified: 2025-11-29 16:25
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, pop
Author: Mustafa Halil

# `pop()` Metodu

**`pandas.DataFrame.pop()`** metodu, **Pandas DataFrame'inizdeki belirli bir sütunu** hem DataFrame'den **kaldırır** hem de **kaldırdığı bu sütunu bir Series olarak size geri verir**.

Basitçe anlatmak gerekirse, bir DataFrame'in sütununu yerinden söker, onu bize verir ve **orijinal DataFrame'de artık o sütun olmaz**.

> Pandas'taki **`pop()`** metodu ile doğrudan **satır** silemezsiniz.
> 
> `pop()` metodunun işlevi, bir `DataFrame`'den sadece **sütunları** (column) silmek ve silinen sütunu bir `Series` olarak geri döndürmektir. Satırları hedef almaz.

## Sözdizimi:

```python
DataFrame.pop(sütun_adı)
```

## Detaylı Açıklama

`pandas.DataFrame.pop()` metodunun kullanımı sonucunda;

1. **Sütunu Çıkarır (Pop):** Belirttiğiniz sütun adını (label) alır ve o sütunu DataFrame'den tamamen siler.

2. **Geri Döndürür (Return):** Silinen bu sütunun içeriğini yeni bir **Pandas Series** objesi olarak size geri verir, böylece bu veriyi başka amaçlar için kullanabilirsiniz.

3. **Yerinde Değişiklik Yapar (In-place):** Bu işlem, DataFrame üzerinde doğrudan değişiklik yapar (**in-place**). Yani, işlemi yaptıktan sonra DataFrame'in eski haline dönme şansı yoktur, sütun kalıcı olarak silinir.

## Neden Sadece Tek Bir Sütun?

**`pandas.DataFrame.pop()`** metodu bir seferde **yalnızca tek bir sütun** silebilir (ve geri döndürebilir).

1. **Series Döndürmesi:** `pop()` metodunun temel özelliği, silinen sütunun verilerini bir **Series** objesi olarak geri döndürmesidir. Bir Pandas Series, tek boyutlu bir veri yapısıdır; bu nedenle `pop()` metodunun da tek bir sütun üzerinde çalışması beklenir.

2. **Sözdizimi:** Metodun argümanı, kaldırılacak sütunun etiketini belirten tek bir `item` (etiket) bekler:
   
   ```python
   DataFrame.pop(item)
   ```

Birden fazla sütun etiketi içeren bir liste veya dizi kabul etmez.

### Örnek

Diyelim ki, `df` adında, `isim`, `sınıf` ve `hız` sütunları olan bir DataFrame'iniz var.

```python
import pandas as pd
df = pd.DataFrame([('şahin', 'kuş', 389.0),
                   ('papağan', 'kuş', 24.0),
                   ('aslan', 'memeli', 80.5),
                   ('maymun', 'memeli', np.nan)],
                  columns=('isim', 'sınıf', 'hız'))

print(df)
```

Çıktı:

```python
      isim   sınıf      hız
0    şahin     kuş    389.0
1  papağan     kuş     24.0
2    aslan  memeli     80.5
3   maymun  memeli      NaN
```

|     | isim    | sınıf  | hız   |
| --- | ------- | ------ | ----- |
| 0   | şahin   | kuş    | 389.0 |
| 1   | papağan | kuş    | 24.0  |
| 2   | aslan   | memeli | 80.5  |
| 3   | maymun  | memeli | NaN   |

```python
# 'sınıf' sütununu çıkar ve 'eski_sınıf' değişkenine ata

eski_sınıf = df.pop('sınıf')
print(eski_sınıf)
```

**Sonuçlar:**

1. `eski_sınıf` değişkeni artık yalnızca çıkarılan `sınıf` verilerini içeren bir **Series** olur.

```python
0       kuş
1       kuş
2    memeli
3    memeli
Name: sınıf, dtype: object
```

## Ne Zaman Kullanılır?

- Bir sütunun verisine ihtiyacınız varsa ve aynı zamanda **bu sütunu orijinal veri kümesinden kaldırmak istiyorsanız**.

- Örneğin, bir makine öğrenimi modelinde **hedef değişkeni** (çıktı) veri setinden ayırıp, modeli eğitmek için kullanılan özellikler (girdiler) veri setini temizlemek istediğinizde kullanışlıdır. (`X = df.pop('hedef'); Y = df`)

> **Not:** Sadece bir sütunu silmek istiyor, ancak geri döndürülen veriye ihtiyacınız yoksa, bunun yerine **`df.drop('sütun_adı', axis=1, inplace=True)`** yöntemini kullanabilirsiniz.

## pop() ve drop() Metotları Arasındaki Temel Farklar:

`pandas.DataFrame` üzerinde kullanılan **`pop()`** ve **`drop()`** metotları arasındaki temel fark, **ne yaptıkları** ve **ne döndürdükleri** ile ilgilidir.

İşte bu iki metot arasındaki temel farklar:

| Özellik                       | `DataFrame.pop('sütun_adı')`                                                              | `DataFrame.drop('sütun_adı', axis=1)`                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **İşlev**                     | Sütunu **kaldırır** ve **geri döndürür**.                                                 | Sütunu (veya satırı) **kaldırır** ancak **geri döndürmez**.                                                                               |
| **Geri Dönüş Değeri**         | Kaldırılan sütunu içeren bir **Series** objesi döndürür.                                  | Silme işleminin yapıldığı, ancak sütun/satırın bulunmadığı **yeni bir DataFrame** döndürür.                                               |
| **DataFrame Üzerindeki Etki** | Orijinal DataFrame'de **yerinde değişiklik yapar** (in-place). Kaldırılan sütun kaybolur. | Varsayılan olarak **yerinde değişiklik yapmaz**. Değişiklik için yeni bir DataFrame oluşturur veya `inplace=True` parametresi kullanılır. |
| **Kullanım Amacı**            | Bir sütunu ayırıp, onu kullanmak ve aynı anda orijinal DataFrame'i temizlemek.            | Bir sütunu veya satırı veri kümesinden kalıcı olarak silmek.                                                                              |

### Detaylı Açıklama

### 1. `pop()` Metodu (Yerinden Sökme ve Geri Verme)

**`pop()`** metodu, bir sütunu bir veri listesinden eleman "çekip çıkarmak" gibi çalışır:

- **Sütunu Silerken Geri Verir:** Belirtilen sütunu siler ve bu silinen sütunun verisini bir `Series` olarak size **geri döndürür**.

- **Doğrudan Değişiklik:** Bu metot, **orijinal DataFrame üzerinde doğrudan değişiklik yapar**. Yani `pop()` çağrıldıktan sonra, o sütun orijinal DataFrame'de artık yoktur.

> **Özet:** Bir sütunu ayırıp, kullanmak ve DataFrame'den aynı anda temizlemek için idealdir.

### 2. `drop()` Metodu (Atma ve Yeni Kopyasını Oluşturma)

**`drop()`** metodu, adından da anlaşılacağı gibi, belirtilen satırları veya sütunları "atar":

- **Axis Parametresi Gerekir:** Sütun silmek için mutlaka `axis=1` (sütunları ifade eder) veya satır silmek için `axis=0` (varsayılan) belirtmeniz gerekir.

- **Geri Dönüş:** Silme işleminin uygulandığı, ancak silinen satır/sütunun bulunmadığı **yeni bir DataFrame** döndürür. Silinen veriyi geri döndürmez.

- **İsteğe Bağlı Değişiklik:** Orijinal DataFrame'i değiştirmek için **`inplace=True`** argümanını açıkça belirtmeniz gerekir. Aksi takdirde, orijinal DataFrame değişmez.

> **Özet:** Orijinal DataFrame'inize dokunmadan (veya `inplace=True` ile dokunarak) belirli satırları veya sütunları atmak için standart bir yöntemdir.

## Birden Fazla Sütun Silmek İçin Ne Kullanılır?

Eğer bir DataFrame'den birden fazla sütunu aynı anda silmek istiyorsanız, standart olarak **`drop()`** metodunu kullanmanız gerekir:

```python
# 'Sütun_A' ve 'Sütun_B'yi siler ve yeni bir DataFrame döndürür.
yeni_df = df.drop(columns=['Sütun_A', 'Sütun_B'])
```

### Özet Karşılaştırma

| İşlem                    | Metot        | Girdi Tipi                       | Geri Dönüş Tipi | DataFrame'i Değiştirir mi?        |
| ------------------------ | ------------ | -------------------------------- | --------------- | --------------------------------- |
| Tek Sütun Silme          | **`pop()`**  | Tek bir etiket (string)          | `Series`        | Evet (Her zaman)                  |
| Birden Fazla Sütun Silme | **`drop()`** | Etiket listesi (list of strings) | `DataFrame`     | İsteğe Bağlı (`inplace=True` ile) |

## Kaynaklar:

* [pandas.DataFrame.pop &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pop.html)

* [Google Gemini](https://gemini.google.com)
