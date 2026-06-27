Title: Pandas - loc
Date: 2022-07-11 00:00
Modified: 2025-06-21 19:12
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, Seçim, loc
Author: Mustafa Halil

# loc[] Fonksiyonu Nedir? Nasıl Kullanılır?

> Etiketlere veya mantık (boole) dizisine göre bir satır ve sütun grubuna erişim

`loc[]` metodu, `iloc[]` metoduna benzer bir metottur ancak `loc[]` metodunda, satır ve sütun seçmek/görüntülemek istediğimiz zaman, satır ve sütunların **isimlerini / ifadelerini** (metinsel / string ifadelerini) yazmalıyız. `loc[]` metodu aslında etiket tabanlıdır, ancak bir mantık (boole) dizisiyle de kullanılabilir. `loc[]` metodunun alabileceği parametreler şunlardır:

- Tek bir etiket, ör. `5` veya `'a'`, (`5`'in dizinin bir etiketi olarak yorumlandığını ve **asla** dizin boyunca bir tamsayı konumu olarak yorumlanmadığını unutmayın).
- Bir liste veya etiket dizisi, ör. `['a', 'b', 'c']`
- Etiketleri olan bir dilim nesnesi, ör. `'a':'f'`

##### UYARI:

`loc[]` metodu ile dilimleme işlemi yapılırken `:` karakterinin sağındaki bitiş değeri, standart python dilimleme işlemlerinin aksine, seçime **DAHİL EDİLİR**, unutmayın.

- Dilimlenen eksenle aynı uzunlukta bir mantık (boole) dizisi, ör. `[True, False, True]`
- Hizalanabilir bir mantık (boole) Serisi. Anahtarın dizini, maskelemeden önce hizalanacaktır.
- Hizalanabilir bir İndeks. Döndürülen seçimin Dizini girdi olacaktır.
- Tek argümanlı (çağıran Series veya DataFrame) ve indeksleme için 
  geçerli çıktı döndüren (yukarıdakilerden biri) çağrılabilir bir 
  fonksiyon

Elimizde aşağıdaki gibi bir veri çerçevesi olduğunu varsayalım.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
print(imdb)
```

| Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| ------------------------ | ---- | ---- | ------------ |
| The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| The Godfather            | 1972 | 9,2  | 751381       |
| The Godfather: Part II   | 1974 | 9    | 488889       |
| Pulp Fiction             | 1994 | 8,9  | 830504       |
| The Dark Knight          | 2008 | 8,9  | 1045186      |
| ...                      | ...  | ...  | ...          |
| Mystic River             | 2003 | 7,9  | 256159       |
| In the Heat of the Night | 1967 | 7,9  | 37081        |
| Arsenic and Old Lace     | 1944 | 7,9  | 45893        |
| Before Sunrise           | 1995 | 7,9  | 100974       |
| Papillon                 | 1973 | 7,9  | 62517        |

247 rows × 3 columns

**Pulp Fiction** Filminin **Puan**ını öğrenmek istediğimizi düşünelim. Bu durumda aşağıdaki kodları yazmamız doğru sonucu verecektir.

```python
print(imdb.loc["Pulp Fiction", "Puan"])
```

Çıktı:

```python
'8,9'
```

**Star Wars** isimli satır verisine ulaşmak için `loc[]` metoduna **Star Wars** metinsel (string) ibaresini eklemeliyiz.

```python
print(imdb.loc["Star Wars"])
```

Çıktı:

```python
Yıl               1977
Puan               8,7
Oylayan_Kişi    585132
Name: Star Wars, dtype: object
```

`loc[]` metodunda daha fazla pratik yapmak için **df** isminde bir veri çerçevesi oluşturalım;

```python
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
print(df)
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| cobra      | 1         | 2      |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

## Tek etiket ile Satır Seçimi

`loc[]` metodunda tek etiket kullanıldığında, sonucun satırı bir Seri olarak döndürüldüğünü unutmayın. Örneğe bakalım;

```python
print(df.loc['viper'])
```

Çıktı:

```python
max_speed    4
shield       5
Name: viper, dtype: int64
```

## Etiket listesi ile Satır Seçimi

Köşeli parantez `[[]]` kullanımı , sonuc olarak bir Veri Çerçevesi (DataFrame) döndürür. İnceleyelim;

```python
print(df.loc[['viper', 'sidewinder']])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

## Satır ve sütun belirterek Değer Seçimi

Tıpkı `iloc[]` metodunda olduğu gibi `loc[]` metoduna da hem satır hem de sütun değeri girilebilir. Bu durumda MS Excel ve Libre Ofis Calc programında olduğu gibi satır ve sütunların kesişimindeki hücre ya da hücre değer(ler)i, sonuç olarak döndürülür.

Aşağıdaki örnekte, `loc[]` metoduna birer adet satır ve sütun değeri girilecek. Sonucu incelersek sadece bir değer döndürdüğünü göreceksiniz.

```python
print(df.loc['cobra', 'shield'])
```

Çıktı:

```python
2
```

## Satır için aralıklı etiket, Sütun için ise tek etiketle dilimleme

Bu kısımda, satır seçiminde bir aralık, sütün seçiminde ise sadece tek bir değer (yani tek sütun) belirterek sonucun nasıl çıkacağını inceleyelim.

Yukarıdaki **Uyarıda** belirtildiği gibi, Pandas'ta dilimleme esnasında hem **başlangıç** hem de **bitiş** değerlerinin seçime dahil edildiğini unutmayın.

```python
print(df.loc['cobra':'viper', 'max_speed'])
```

Çıktı:

```python
cobra    1
viper    4
Name: max_speed, dtype: int64
```

## Satır ile aynı uzunlukta Mantık (Boole) listesi ile Seçim

**df** isimli veri çerçevemiz 3 satırdan oluştuğu için, toplam 3 adet **True** ya da **False** anahtar kelimesi kullanarak bir mantık (boole) listesi oluşturacak ve **True** olarak belirttiğimiz satırları göreceğimiz bir sonuç elde edeceğiz.

```python
print(df.loc[[False, False, True]])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

## Hizalanabilir Mantık (boole) Serisi ile Satır Seçimi

Pandas Seriler (Series) veri yapısını kullanarak, oluşturmuş olduğumuz veri çerçevemizde indeks sırasını değiştirerek (hizalayarak) mantıksal (boole) listesi ile belirttiğimiz satırları filtreleyerek satır seçimi yapabiliriz. Anlatım biraz karışık gelmiş olabilir. 

Aşağıdaki örneği incelerken konuyu anlayacağınızı düşünüyorum. Öncelikle **df** isimli veri çerçevemize göz atalım.

```python
print(df)
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| cobra      | 1         | 2      |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

Görüldüğü üzere, satır sırası aşağı doğru, **cobra, viper ve sidewinder** olarak devam ediyor. Yukarıda öğrendiğimiz şekilde sadece, mantık (boole) listesi ile seçim yaparsak yani `df[[False, True, False]]` yazar ve kodu çalıştırısak 0. ve 2. indekste kayıtlı satırları gizle, sadece 1. indekste kayıtlı **viper** satırını göster demiş oluruz. Kodun çıktısını aşağıda görebilirsiniz;

```python
print(df[[False, True, False]])
```

|       | max_speed | shield |
| ----- | --------- | ------ |
| viper | 4         | 5      |

`[False, True, False]` listesini, Pandas Seriler (Series) veri yapısını kullanarak, aynı veri çerçevesine, indeks sırasını değiştirerek (hizalayarak) uygulayıp sonucu görelim.

```python
print(df.loc[pd.Series([False, True, False], index=['viper', 'sidewinder', 'cobra'])])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

`index=['viper', 'sidewinder', 'cobra']` kodu ile indeks sırasını değiştirip ardında 0. ve 2. indekste kayıtlı satırları gizle, sadece 1. indekste kayıtlı satırını göster demiş olduk. Satır sırası değiştiği için 1. indeksteki satır **sidewinder** oldu ve bu satıra ait bilgiler ekrana yazdırıldı.

# 
