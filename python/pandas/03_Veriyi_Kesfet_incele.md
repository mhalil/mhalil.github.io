Title: Pandas 03 -  Veriyi Keşfet - İncele
Date: 2022-07-10 20:40
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül
Author: Mustafa Halil

## Veriyi Keşfet / İncele

Bu bölümde **Veri Çerçevesi** (**Data Frame**) içeriğini görüntülemeye dair komutları öğreneceğiz.

Öncelikle **Pandas** Kütüphanesini içe aktarıp, kodlama esnasında hızlı olması adına bu kütüphaneye **pd** adını atayalım;

```python
import pandas as pd
```

Bu eğitimde, fonksiyon ve metotlar konusunu anlatırken kullanmak üzere, basit bir Veri Çerçevesi (Data Frame) oluşturalım ve oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici"]}
veri = pd.DataFrame(sozluk)
print(veri)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | Halil      | 38  | programcı   |
| 2   | Burak      | 41  | akademisyen |
| 3   | Emre       | 23  | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 23  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

### TEMEL FONKSİYONLAR

### head() Fonksiyonu

Oluşturduğumuz ya da çalışmamıza dahil ettiğimiz (içe aktardığımız) Veri Çerçevelerinin ilk satırlarını görüp, içerik hakkında bilgi edinmek istersek **head()** fonksiyonunu kullanabiliriz. **Head** kelimesi Türkçede **Baş, Kafa** anlamına gelmektedir.

```python
print(veri.head())
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 1   | Halil   | 38  | programcı   |
| 2   | Burak   | 41  | akademisyen |
| 3   | Emre    | 23  | yönetici    |
| 4   | Ersin   | 37  | amir        |

**head()** fonksiyonunda parantez içine parametre olarak bir değer yazmazsak, veri çerçevesinin **ilk 5 (satır) değeri** görüntülenir. Değer belirtirsek belirttiğimiz değer kadar satır verisi görüntülenir.

```python
print(veri.head(3))
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 1   | Halil   | 38  | programcı   |
| 2   | Burak   | 41  | akademisyen |

İndex değerinin 2'de bitmesi sizi şaşırtmasın, pekçok programlama dilindi olduğu gibi Python programlama dilinde de, sayma sayıları sıfırdan başlar. Zaten tabloyu incelerseniz, tabloda 3 kullanıcıya ait (3 satır) veri olduğunu görürsünüz.

### tail() Fonksiyonu

**head()** fonksiyonuna oldukça benzer bir fonksiyondur. Oluşturduğumuz ya da çalışmamıza dahil ettiğimiz Veri Çerçevelerinin **son satırlarını** görüp içerik hakkında bilgi edinmek istersek **tail()** fonksiyonunu kullanabiliriz. **Tail** kelimesi Türkçede, **kuyruk, son kısım** anlamına gelmektedir.

```python
print(veri.tail())
```

|     | isim       | yaş | iş-meslek |
| --- | ---------- | --- | --------- |
| 5   | Sertaç     | 52  | mühendis  |
| 6   | Furkan     | 30  | yönetici  |
| 7   | Murat      | 23  | müdür     |
| 8   | Ahmet      | 40  | veteriner |
| 9   | Abdülkadir | 38  | yönetici  |

**tail()** fonksiyonunu içine parametre olarak bir değer yazmazsak, veri çerçevesinin **son 5 (satır) değerini** görüntüler. Değer belirtirsek belirttiğimiz değer kadar satır verisi görüntüler.

```python
print(veri.tail(7))
```

|     | isim       | yaş | iş-meslek |
| --- | ---------- | --- | --------- |
| 3   | Emre       | 23  | yönetici  |
| 4   | Ersin      | 37  | amir      |
| 5   | Sertaç     | 52  | mühendis  |
| 6   | Furkan     | 30  | yönetici  |
| 7   | Murat      | 23  | müdür     |
| 8   | Ahmet      | 40  | veteriner |
| 9   | Abdülkadir | 38  | yönetici  |

### columns Fonksiyonu

**columns** fonksiyonu, oluşturulan ya da içe aktarılan Veri Çerçevelerinin başlık satırını çıktı olarak verir. **columns** fonksiyonunu kullanırken sonunda <u>parantez işaretleri kullanmadığımıza</u> dikkat edin.

Sütun isimlerini değiştirmek ya da veri çerçevesine filtreleme işlemi uygulamak istediğimiz zaman, bu fonksiyon çok işimize yarar.

```python
print(veri.columns)
```

```python
Index(['isim', 'yaş', 'iş-meslek'], dtype='object')
```

### len() Fonksiyonu

**len()** foknsiyonu, Veri Çerçevesinin kaç satırdan oluştuğunu bildirir.

```python
print(len(veri))
```

```
10
```

Çıktıdan anladığımız kadarıyla, **veri** isimli veri çerçevesi, 10 satırlık bir yapıdan oluşuyor.

### info() Fonksiyonu

**info()** fonksiyonu, Veri Çerçevesinin satır ve sütun sayısı, başlık tipleri (sayı[int, float], metin[object, string], ...vb) ve doluluk oranı (boş olmayan hücre sayısı[non-null]) hakkında bilgi görüntüler.

```python
print(veri.info())
```

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   isim       10 non-null     object
 1   yaş        10 non-null     int64 
 2   iş-meslek  10 non-null     object
dtypes: int64(1), object(2)
memory usage: 368.0+ bytes
```

<u>Çıktıyı incelersek;</u>  
**class 'pandas.core.frame.DataFrame** : **veri**'nin Pandas sınıfına ait bir DataFrame yapısı olduğunu,  
**RangeIndex: 10 entries, 0 to 9** : Veri Çerçevesinin 0 ile 9 arasında, toplam 10 satırlık yapı olduğunu,  
**Data columns (total 3 columns)** : Veri Çerçevesinin 3 sütundan oluştuğunu,  
**Column** : Sütun isimlerini,  
**Non-Null Count** : Boş olmayan veri sayısını,  
**Dtype** : Veri biçimini tanımlar.  
**int34** ya da int64 **ibaresi**, **tamsayı (integer)** olduğunu, **object** ibaresi, verinin **metin (string)** ifadesi olduğunu,  
**dtypes: int64(1), object(2)** : Veri Çerçevesinin 1 adet tamsayı (**int64(1)**), 2 adet metinsel (string / **object(2)**) başlık/sütun içerdiğini temsil eder.

### dtypes Fonksiyonu

**dtypes** fonksiyonu, veri çerçevesinin başlık tiplerini görüntüler. **dtypes** fonksiyonunu kullanırken sonunda <u>parantez işaretleri kullanmadığımıza</u> dikkat edin.

```python
print(veri.dtypes)
```

```python
isim         object
yaş           int64
iş-meslek    object
dtype: object
```

### describe() Fonksiyonu

**describe()** fonksiyonu, sayısal veri barındıran sütunlar hakkında detaylı matematiksel bilgiler verir.

```python
print(veri.describe())
```

|       | yaş       |
| ----- | --------- |
| count | 10.000000 |
| mean  | 34.700000 |
| std   | 9.333929  |
| min   | 23.000000 |
| 25%   | 26.250000 |
| 50%   | 37.500000 |
| 75%   | 39.500000 |
| max   | 52.000000 |

<u>Çıktıyı incelersek;</u>  
**count :** yaş isimli sütunda kaç adet veri olduğunu,  
**mean :** yaş isimli sütudaki verilerin ortalamasını,  
**std :** yaş isimli sütudaki verilerin standart sapmasını,  
**min:** yaş isimli sütudaki verilerin en küçük değerini  
**%25 :** yaş isimli sütundaki verilerin medyanın alt çeyreğini (dörttebirliğini),  
**%50 :** yaş isimli sütundaki verilerin Ortanca medyanını,  
**%75 :** yaş isimli sütundaki verilerin medyanın üst çeyreğini (dörttebirliğini),  
**max :** yaş isimli sütudaki verilerin en büyük değerini, tanımlar

### shape Fonksiyonu

Veri Çerçevesinin yapısını yani satır ve sütun bilgisini öğrenmek için shape fonksiyonunu kullanabiliriz.

```python
print(veri.shape)
```

```python
(10, 3)
```

### index Fonksiyonu

**index** fonksiyonu, Veri Çerçevesinin indeks bilgisini döndürür.

```python
print(veri.index)
```

```python
RangeIndex(start=0, stop=10, step=1)
```

Veri çerçevesi oluşturulurken indeks değerlerinin otomatik olarak belirlenmesi halinde, yukarıdaki şekilde çıktı alırız. Çıktıyı incelersek;

- **start=0** : İlk indeks değerinin 0 olduğu,
- **stop=10** : son indeks değerinin 10 olduğu,
- **step=1** : indeks değerlerinin 1'er 1'er arttığını belirtmektedir.

Peki indeks değeri sayılardan oluşmazsa, yani indeks bilgisi tarafımızca belirtilen Metinsel verilerden oluşursa **index** fonksiyonu nasıl çıktı verir?.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
print(imdb.head())
```

| Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| ------------------------ | ---- | ---- | ------------ |
| The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| The Godfather            | 1972 | 9,2  | 751381       |
| The Godfather: Part II   | 1974 | 9    | 488889       |
| Pulp Fiction             | 1994 | 8,9  | 830504       |
| The Dark Knight          | 2008 | 8,9  | 1045186      |

```python
print(imdb.index)
```

```python
Index(['The Shawshank Redemption ', 'The Godfather ',
       'The Godfather: Part II ', 'Pulp Fiction', 'The Dark Knight ',
       '12 Angry Men ', 'Schindler's List ',
       'The Lord of the Rings: The Return of the King ', 'Fight Club ',
       'Star Wars: Episode V - The Empire Strikes Back ',
       ...
       'The Artist ', 'Nausicaä of the Valley of the Wind ',
       'Beauty and the Beast ', 'Three Colors: Red ', 'Bringing Up Baby ',
       'Mystic River ', 'In the Heat of the Night ', 'Arsenic and Old Lace ',
       'Before Sunrise ', 'Papillon '],
      dtype='object', name='Film_Adı', length=247)
```

Gördüğünüz gibi, **indeks** bilgisi Metinsel veriler olduğunda, **index** fonksiyonunun çıktısı yukarıda şekilde alınıyor. Çıktıyı incelersek;

- **Index(['The Shawshank Redemption ', 'The Godfather ', 'The Godfather: Part II ', ...]** : İndeks bilgileri liste halinde verilir,
- **type='object'** : İndeks bilgilerinin "Object" yani "Metinsel (String)" veri olduğu,
- **name='Film_Adı'** : İndexks başlığının "Film_Adı" olduğu,
- **length=247** : toplam 247 adet indeks verisi (satır) olduğu ifade etmektedir.

### isnull() Fonksiyonu

Veri çerçevesinde boş, kayıp veri olup olmadığını **isnull()** fonksiyonu ile tespit edebiliriz. Bu fonksiyonu çalıştırdığımızda veri çerçevesinin satır ve sütun başlıkları ekrana yazdırılır ancak veri yerine **True** ya da **False** bilgisi görüntülenir.

```python
print(veri.isnull())
```

|     | isim  | yaş   | iş-meslek |
| --- | ----- | ----- | --------- |
| 0   | False | False | False     |
| 1   | False | False | False     |
| 2   | False | False | False     |
| 3   | False | False | False     |
| 4   | False | False | False     |
| 5   | False | False | False     |
| 6   | False | False | False     |
| 7   | False | False | False     |
| 8   | False | False | False     |
| 9   | False | False | False     |

**isnull()** fonksiyonuna **any()** Fonksiyonunu da eklersek, veri çerçevesi tümüyle görüntülenmez sadece veri çerçevesi başlıkları ve bu başlıklarda (sütunlarda) eksik/kayıp veri bulunup bulunmadığı bilgisi görüntülenir.

```python
print(veri.isnull().any())
```

```python
isim         False
yaş          False
iş-meslek    False
dtype: bool
```

Görüyoruz ki, veri çerçevemizde hiç eksik/kayıp veri bulunmamaktadır.
 Yukarıdaki sözlük yapısında bazı verileri boş bırakarak yeni bir veri çerçevesi oluşturalım ve **isnull()** fonksiyonunu çalıştırıp sonuçları inceleyelim.

```python
sozluk_2 = {"isim" : ["Mustafa", pd.NaT, "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 38, 41, pd.NaT, 37, 52, 30, 23, 40,  pd.NaT],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen", "yönetici","amir","mühendis", "yönetici","müdür","veteriner","yönetici"]}
veri_2 = pd.DataFrame(sozluk_2)
print(veri_2)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | NaT        | 38  | programcı   |
| 2   | Burak      | 41  | akademisyen |
| 3   | Emre       | NaT | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 23  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | NaT | yönetici    |

**1** nolu İndeksteki **isim**, **3** nolu ve **9** nolu İndekslerdeki **yaş** bilgilerin boş olduğunu görüyoruz.

```python
print(veri_2.isnull())
```

|     | isim  | yaş   | iş-meslek |
| --- | ----- | ----- | --------- |
| 0   | False | False | False     |
| 1   | True  | False | False     |
| 2   | False | False | False     |
| 3   | False | True  | False     |
| 4   | False | False | False     |
| 5   | False | False | False     |
| 6   | False | False | False     |
| 7   | False | False | False     |
| 8   | False | False | False     |
| 9   | False | True  | False     |

**1** nolu İndeksteki **isim**, **3** nolu ve **9** nolu İndekslerdeki **yaş** bilgileri **eksik** olduğu için bu değerler **True**, diğer hücrelerde ise eksik veri olmadığı için **False** değeri ile gösterilmektedir.  
Sütun bazlı eksik/kayıp veri olup olmadığını incelersek;

```python
print(veri_2.isnull().any())
```

```python
isim          True
yaş           True
iş-meslek    False
dtype: bool
```

Çıktıdan anlıyoruz ki;

- **isim** ve **yaş** sütunlarında Eksik veri bulunuyor
- **iş-meslek** sütununda hiç eksik veri bulunmuyor.

## value_counts() Fonksiyonu

Veri çerçevemizde bir sütunda aynı verinin kaç kez tekrar ettiğini (kaç adet bulunduğunu) öğrenmek için `value_counts()` fonksiyonunu kullanbiliriz.

Örneğin, **veri_2** isimli veri çerçevemizde **iş-meslek** sütununda hangi veri kaç kez tekrar ediliyor, yani veri çerçevemizde kaç adet Mühendis, Programcı, Yönetici,...vb var.

```python
print(veri_2["iş-meslek"].value_counts())
```

```
yönetici       3
mühendis       2
programcı      1
akademisyen    1
amir           1
müdür          1
veteriner      1
Name: iş-meslek, dtype: int64
```

[← Önceki Bölüm](pandas-02-excel-dosyalari-ile-calismak.html) | [Sonraki Bölüm →](pandas-04-secim-yontemleri.html)
