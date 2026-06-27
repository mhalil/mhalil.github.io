Title: Pandas 04 - Seçim Yöntemleri
Date: 2022-07-11 00:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Seçim
Author: Mustafa Halil

# Seçim Yöntemleri

Veri Çerçevesi oluştururken ya da oluşturduktan sonra istenilen satır ve sütunların seçilmesi/görüntülenmesi ya da seçilmemesi/görüntülenmemesi konusunu inceleyelim. Veri çerçevesinde işimize yaramayacak verileri devre dışı bırakmak için bu yöntemleri kullanabiliriz.

## Satır ve Sütun Seçimi

### iloc[] Metodu

Veri Çerçevesindeki istenilen satır ve sütunu seçmek/görüntülemek için **iloc[]** metodu kullanılır. **iloc[]** kelimesini unutmamak için **İndex Location** yani, **Konumun İndeks Değeri** gibi düşünebilir, hafızanızda kodlayabilirsiniz. Bir başka ifadeyle, `iloc[]` için, Tamsayı değerine dayalı konum indeksleme metodu diyebiliriz. Esas olarak **iloc[]** metodu, hem satır hem de sütun numarası alarak çalışır.

```
Veri_Cercevesi_Adı.iloc[Satir_Numarası, Sütun_Numarası]
```

`iloc[]` metodunun alabileceği parametreler şunlardır:  

- Bir satır ve sütun dizini, ör. `(0,1)`
- Bir tamsayı, ör. `5`
- Bir tamsayı listesi veya dizisi, ör. `[4, 3, 0]`
- Tamsayılı bir dilim nesnesi, ör. `1:7`
- Bir mantık (boole) dizisi.

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

Verimizi **.iloc[]** metodu ile seçelim.

```python
print(veri.iloc[8,2])
```

```
'veteriner'
```

`iloc[]` metodu, parametre olarak tam sayı alabileceği gibi, sayı listesi de alabilir. Bildiğiniz gibi Python'da liste veri tipleri köşeli parantez `[]` ile ifade ediliyor. O nedenle `iloc[]` metoduna parametre olarak liste veri tipi girileceği zaman içiçe köşeli
 parantezler (hem satıra hemde sütuna ait listeler yazılacağı için) konuyu yeni öğrenenlerde kafa karışıklığına sebep olabilir. Anlatmak istediğimi aşağıdaki koda bakarak rahatlıkla anlayabilirsiniz.

```python
iloc[[satır_listesi], [sütun_listesi]]
```

Yukarıda oluşturduğumuz veri çerçevemizi kullanarak, listelerden müteşekkil bir dilimleme yapalım.

```python
print(veri.iloc[[1,3,5],[0,2]])
```

|     | isim   | iş-meslek |
| --- | ------ | --------- |
| 1   | Halil  | programcı |
| 3   | Emre   | yönetici  |
| 5   | Sertaç | mühendis  |

## Sadece Satırları Listelemek

### Bir Tamsayı ile Satır Seçimi

`iloc[]` metoduna parametre olarak sadece **bir tamsayı değeri** girildiğinde, girilen sayıya (indeks bilgisine) ait **satır** verisi döndürülür. Bu veri, Seri (Series) tipindedir. Hemen aşağıdaki örneğe bakalım.

```python
print(veri.iloc[5])
```

```
isim           Sertaç
yaş                52
iş-meslek    mühendis
Name: 5, dtype: object
```

### Bir Sayı Listesi ile Satır Seçimi

Veri çerçevemizden **belirli bazı satırları** seçmek istersek `iloc[]` metoduna parametre olarak bir **liste** tanımlamalıyız. Bu liste, bir satırdan başlayıp diğer bir satıra kadar olan aralık (dilimleme) olabileceği gibi tek tek te belirtilebilir. 
Şimdi bunları inceleyelim.

Örneğin veri çerçevemizde indeks değeri 3, 5 ve 7 olan satırları seçmek istersek aşağıdaki şekilde kod yazmamız gerekir.

```python
print(veri.iloc[[3,5,7]])
```

|     | isim   | yaş | iş-meslek |
| --- | ------ | --- | --------- |
| 3   | Emre   | 23  | yönetici  |
| 5   | Sertaç | 52  | mühendis  |
| 7   | Murat  | 23  | müdür     |

`print(veri.iloc[[3,5,7]])` koduna dikkat ederseniz `iloc[]` metoduna parametre olarak sadece bir adet köşeli parantez yazıldı, ikinci köşeli parantez yazılmadı. Bu demek oluyor ki, **parametre olarak sadece satır bilgisi** var yani sütunlarda seçme ya da kısıtlamaya işlemi yapılmadı, tüm sütun bilgileri gösterilmeli. Zaten Çıktıya baktığımızda anlattığımız gibi sonuç elde ettiğimizi görüyoruz.

### Dilimleyerek Satır Seçimi

Python'da **listeler** konusunu okuduğunuzda, dilimlemenin nasıl yapıldığını da görmüş olmalısınız. Kısaca bahsedecek olursak, dilimleme için `:` karakteri kullanılır. `:` karakterinin solunda **başlangıç**, sağında **bitiş** değeri yazılır. Elimizde veri çerçevemizin indeks değerleri gibi **0 ile 9** arasında sayılardan oluşan bir liste varsa, bu listeden aralık seçmek yani dilimleme yapmak istersek aşağıdaki kodu yazmalıyız.

`[1:5]`

Bu kodun anlamı, 1. öğeden başlayarak **5. öğeye kadar** (yani 5. öğe dahil **DEĞİL**) dilimleme yap, 1,2,3,4 sonucunu ver.

`[3:]`

Bu kodun anlamı, **3. öğeden başlayarak** listenin sonuna kadar dilimleme yap, 3,4,5,6,7,8,9 sonucunu ver.

`[3:]` koduna dikkat ederseniz, `:`'dan sonra kısıtlama/sınırlama getirilmemiştir, yani liste sona kadar devam eder.

Bir aralık belirterek veri çerçevemizde dilimleme yapalım ve sonucu görelim;

```python
print(veri.iloc[1:5])
```

|     | isim  | yaş | iş-meslek   |
| --- | ----- | --- | ----------- |
| 1   | Halil | 38  | programcı   |
| 2   | Burak | 41  | akademisyen |
| 3   | Emre  | 23  | yönetici    |
| 4   | Ersin | 37  | amir        |

Dilimleme yaparken `iloc[]` metodunun içine ayrıca köşeli parantez **kullanmadığımıza** dikkat edin.

Belirli bir satırdan başlayıp, veri çerçevesinin sonuna kadar giden bir dilimleme yapmak istersek, aşağıda bulunan kod gibi `:`'nin sağına değer yazmamalı, boş bırakmalıyız.

```python
print(veri.iloc[3:])
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

Yukarıdaki anlatımın tersi olan ilk satırdan başlayıp, veri çerçevesinin istenilen satırına kadar giden bir dilimleme yapmak istersek te, aşağıda bulunan kod gibi `:`'nin soluna değer yazmamalı, boş bırakmalıyız.

```python
print(veri.iloc[:4])
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 1   | Halil   | 38  | programcı   |
| 2   | Burak   | 41  | akademisyen |
| 3   | Emre    | 23  | yönetici    |

### Satır ve Sütunları Belirterek Listelemek

Yukarıda yazdığımız `veri.iloc[8,2]` kodu, hem satır hemde sütun belirterek değer elde ettiğimiz bir indeksleme yöntemidir.

### Satır ve Sütunda dilimleme yapmak

Hem satırda hemde sütunda dilimleme yapmak istersek aşağıdaki şekilde kod yazmalıyız;

```python
print(veri.iloc[3:8,:2])
```

|     | isim   | yaş |
| --- | ------ | --- |
| 3   | Emre   | 23  |
| 4   | Ersin  | 37  |
| 5   | Sertaç | 52  |
| 6   | Furkan | 30  |
| 7   | Murat  | 23  |

`veri.iloc[3:8,:2]` kodu ile, 3-8 arası satır, 0-2 arası sütun verileri dilimlenmiş. (**Satırlarda**, 3'ten başlayan 8'de biten bir sınırlama yazılmış, **Sütunlarda** başlangıçta sınır yok yani 0'dan başlıyor, 2. sütuna kadar sınırlama getirilmiş.)

### Satırla aynı uzunluktaki mantık (boole) listesiyle / maskesiyle Satır Seçimi

Python'da Mantık (boolean) işlemleri **0** ya da **1**, **Evet** ya da **Hayır** anlamında, **True** ya da **False** sonucu döndürür. Bu mantı anlamak için, yukarıda oluşturduğumuz 10 satırlık veri çerçevemizi kullanalım. Örneğin **1., 3., 6. ve 9.** indisleri gizlemek isteyelim. O halde görmek istediğimiz satırlar için **True**, gizlemek istediğimiz satırlar için **False** anahtar kelimelerini sırasıyla **liste veri tipi olarak** yazmalı ve `iloc[]` metoduna paramatre olarak eklemeliyiz.

```python
print(veri.iloc[[True, False, True, False, True, True, False, True, True, False]])
```

|     | isim    | yaş | iş-meslek   |
| --- | ------- | --- | ----------- |
| 0   | Mustafa | 25  | mühendis    |
| 2   | Burak   | 41  | akademisyen |
| 4   | Ersin   | 37  | amir        |
| 5   | Sertaç  | 52  | mühendis    |
| 7   | Murat   | 23  | müdür       |
| 8   | Ahmet   | 40  | veteriner   |

## loc[] Metodu

### Etiketlere veya mantık (boole) dizisine göre bir satır ve sütun grubuna erişim

`loc[]` metodu, `iloc[]` metoduna benzer bir metottur ancak `loc[]` metodunda, satır ve sütun seçmek/görüntülemek istediğimiz zaman, satır ve sütunların isimlerini (metinsel / string ifadelerini) yazmalıyız. `loc[]` metodu aslında etiket tabanlıdır, ancak bir mantık (boole) dizisiyle de kullanılabilir. `iloc[]` metodunun alabileceği parametreler şunlardır:

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

```python
'8,9'
```

**Star Wars** isimli satır verisine ulaşmak için `loc[]` metoduna **Star Wars** metinsel (string) ibaresini eklemeliyiz.

```python
print(imdb.loc["Star Wars"])
```

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

### Tek etiket ile Satır Seçimi

`loc[]` metodunda tek etiket kullanıldığında, sonucun satırı bir Seri olarak döndürüldüğünü unutmayın. Örneğe bakalım;

```python
print(df.loc['viper'])
```

```python
max_speed    4
shield       5
Name: viper, dtype: int64
```

### Etiket listesi ile Satır Seçimi

Köşeli parantez `[[]]` kullanımı , sonuc olarak bir Veri Çerçevesi (DataFrame) döndürür. İnceleyelim;

```python
print(df.loc[['viper', 'sidewinder']])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

### Satır ve sütun belirterek Değer Seçimi

Tıpkı `iloc[]` metodunda olduğu gibi `loc[]` metoduna da hem satır hem de sütun değeri girilebilir. Bu durumda MS Excel ve Libre Ofis Calc programında olduğu gibi satır ve sütunların kesişimindeki hücre ya da hücre değer(ler)i, sonuç olarak döndürülür.

Aşağıdaki örnekte, `loc[]` metoduna birer adet satır ve sütun değeri girilecek. Sonucu incelersek sadece bir değer döndürdüğünü göreceksiniz.

```python
print(df.loc['cobra', 'shield'])
```

```python
2
```

### Satır için aralıklı etiket, Sütun için ise tek etiketle dilimleme

Bu kısımda, satır seçiminde bir aralık, sütün seçiminde ise sadece tek bir değer (yani tek sütun) belirterek sonucun nasıl çıkacağını inceleyelim.

Yukarıdaki **Uyarıda** belirtildiği gibi, Pandas'ta dilimleme esnasında hem **başlangıç** hem de **bitiş** değerlerinin seçime dahil edildiğini unutmayın.

```python
print(df.loc['cobra':'viper', 'max_speed'])
```

```python
cobra    1
viper    4
Name: max_speed, dtype: int64
```

### Satır ile aynı uzunlukta Mantık (Boole) listesi ile Seçim

**df** isimli veri çerçevemiz 3 satırdan oluştuğu için, toplam 3 adet **True** ya da **False** anahtar kelimesi kullanarak bir mantık (boole) listesi oluşturacak ve **True** olarak belirttiğimiz satırları göreceğimiz bir sonuç elde edeceğiz.

```python
print(df.loc[[False, False, True]])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

### Hizalanabilir Mantık (boole) Serisi ile Satır Seçimi

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

### Index Fonksiyonu (df.reindex ile aynı davranış)

`Index` metodu, veri çerçevesindeki index isimlerine göre Sıralama ve satır seçimi yapmamızı sağlar. `name` parametresi ise, indeks başlığı olarak kullanacağımız değeri atamamıza yarar. Önce Veri Çerçevemize göz atalım;

```python
print(df)
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| cobra      | 1         | 2      |
| viper      | 4         | 5      |
| sidewinder | 7         | 8      |

**viper ve cobra** satırlarındaki verileri seçmek ve sıralamayı değiştirmek isteyelim. Bu durumda aşağıdaki kodu yazıp çalıştırmamız yeterli olacaktır;

```python
print(df.loc[pd.Index(["viper", "cobra"], name="Baslik")])
```

| Baslik | max_speed | shield |
| ------ | --------- | ------ |
| viper  | 4         | 5      |
| cobra  | 1         | 2      |

## Koşullu Satır Seçimi

Veri çerçevemizde belirttiğimiz koşullara uyan satırları seçmek istersek, bunu Python operatörleri ile rahatlıkla gerçekleştirebiliriz. **shield** sütununda 6'dan büyük değerleri barındıran satırları seçmek istediğimizi varsayalım ve buna uygun kodu yazıp çalıştıralım;

```python
print(df.loc[df['shield'] > 6])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

## Koşullu Sütun seçimi

Veri çerçevemizde belirttiğimiz koşullara uyan sütunları seçmek istersek, benzer kodu kullanabiliriz. Örneğin **shield** sütununda 6'dan büyük değerleri barındıran satırları ve bu satırların sadece **max_speed** sütununu seçmek istediğimizi varsayalım. Bunun için aşağıdaki kodu yazıp çalıştıralım;

```python
print(df.loc[df['shield'] > 6, ['max_speed']])
```

|            | max_speed |
| ---------- | --------- |
| sidewinder | 7         |

### lambda() Fonksiyonu ile Satır Seçimi

`lambda` fonksiyonu ile belirteceğimiz koşulu sağlayan satırı seçmek için aşağıdaki kod mantığını kullanabiliriz. Örneğin **shield** satırında **8**'e eşit değer barındıran satırları seçelim.

```python
print(df.loc[lambda df: df['shield'] == 8])
```

|            | max_speed | shield |
| ---------- | --------- | ------ |
| sidewinder | 7         | 8      |

## Sütun Seçimi

Sadece bir Sütunu seçmek/görüntülemek için veri çerçevesinin adı ile birlikte seçmek/görüntülemek istediğimiz sütunun ismini yazmak yeterlidir. Bu da iki şekilde gerçekleştirilebilir.

1. **VeriCervecesiAdı.SütunAdı**
2. **VeriCervecesiAdı["SütunAdı"]**

Sütun isminde boşluk ya da nokta karakterleri bulunması halinde, ilk (noktalı) seçeneği kullanamayız, o durumda 2. seçeneği (köşeli parantezli) kullanmak gerekir.
Bunları da örneklerle görelim.

```python
print(imdb.Puan)
```

```python
Film_Adı
The Shawshank Redemption     9,2
The Godfather                9,2
The Godfather: Part II         9
Pulp Fiction                 8,9
The Dark Knight              8,9
                            ... 
Mystic River                 7,9
In the Heat of the Night     7,9
Arsenic and Old Lace         7,9
Before Sunrise               7,9
Papillon                     7,9
Name: Puan, Length: 247, dtype: object
```

```python
print(imdb["Puan"])
```

```python
Film_Adı
The Shawshank Redemption     9,2
The Godfather                9,2
The Godfather: Part II         9
Pulp Fiction                 8,9
The Dark Knight              8,9
                            ... 
Mystic River                 7,9
In the Heat of the Night     7,9
Arsenic and Old Lace         7,9
Before Sunrise               7,9
Papillon                     7,9
Name: Puan, Length: 247, dtype: object
```

Birden fazla sütun seçmek istediğimiz durumda, sütun isimlerini liste olarak (bildiğiniz gibi liste veri tipleri köşeli parantez ile temsil edilir) belirtmek/yazmak gerekir.

```python
print(imdb[["Yıl", "Puan"]])
```

| Film_Adı                 | Yıl  | Puan |
| ------------------------ | ---- | ---- |
| The Shawshank Redemption | 1994 | 9,2  |
| The Godfather            | 1972 | 9,2  |
| The Godfather: Part II   | 1974 | 9    |
| Pulp Fiction             | 1994 | 8,9  |
| The Dark Knight          | 2008 | 8,9  |
| ...                      | ...  | ...  |
| Mystic River             | 2003 | 7,9  |
| In the Heat of the Night | 1967 | 7,9  |
| Arsenic and Old Lace     | 1944 | 7,9  |
| Before Sunrise           | 1995 | 7,9  |
| Papillon                 | 1973 | 7,9  |

247 rows × 2 columns

Yukarıda anlatılan `loc` ve `iloc` metodlarını, **Satır**lar da olduğu gibi, **Sütun**larda da kullanabiliriz.

### at[] Metodu

`at[]` metodunu, bir satır/sütun etiket çifti belirterek tek bir değere erişmek için kullanabiliriz. MS Excel ya da Libre Ofis Calc uygulamalarındaki satır ve sütun değerlerinin kesişimindeki hücre değerine ulaşmak ile aynı mantık.

`loc[]` metoduna benzer şekilde kullanılır, her ikisi de etiket tabanlı aramalar sağlar. Bir Veri çerçevesi (DataFrame) veya Seride (Series) **yalnız tek bir değer** almanız veya ayarlamanız gerekiyorsa `at[]` metodunu kullanın.

#### KeyError (AnahtarHatası)

`at[]` metoduna parametre olarak yazılan **etiket**, Veri çerçevesi ya da Seride bulunmuyorsa `KeyError` hatası alınır.

#### ValueError (DeğerHatası)

`at[]` metoduna parametre olarak yazılan satır/sütun etiket çifti bir demet (tuple) veri tipi değilse ya da parametre çiftinden herhangi biri DataFrame için skaler değilse `ValueError` hatası alınır.  
`at[]` metodunun `loc[]` metoduna benzer şekilde kullanıldığını ifade ettik. O nedenle konuyu uzun uzun açıklamaya gerek görmüyorum. Sadece bir kaç örnek kod inceleyerek konuyu kapatacağım.  
Örnek uygulamalar için bir veri çerçevesi oluşturarak devam edelim;

```python
import pandas as pd
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]], 
                  index=[4, 5, 6], columns=['A', 'B', 'C'])
print(df)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 4   | 0   | 2   | 3   |
| 5   | 0   | 4   | 1   |
| 6   | 10  | 20  | 30  |

### Belirtilen satır/sütun çiftinde değer alın

Satır/sütun etiket çifti belirterek tek bir değere erişmek isteyelim.
 Bu işlem, Excel ya da Calc uygulamalarındaki satır ve sütun değerlerinin kesişimindeki hücre değerine ulaşmak ile aynı mantığa sahip.

Veri çerçevemizdeki **4.** indeks ile **B** sütununun kesişim değerini seçelim.

```python
print(df.at[4, 'B'])
```

```python
2
```

### Bir Seri içinden değer elde etmek

Malumunuz, veri çerçevesinden sadece bir satır seçtiğimiz zaman sonuç olarak bir seri elde etmiş oluyoruz, çünkü Seriler tek boyutlu dizilerdir. Bu seri içerisinden bir değer almak istersen aşağıdaki şekilde kod yazmamız yeterli olacaktır.

Örneğin Öncelikle veri çerçevemizdeki **5.** indekse ait satırı seçip ardıdan **B** sütununun değerini alalım;

```python
print(df.loc[5].at['B'])
```

```python
4
```

### iat[] Metodu

`iat[]` metodu, satır/sütun çiftinde tamsayı belirtilerek **tek bir değere** erişim sağlamak için kullanılır. ve `iloc[]` metoduna benzerdir, her iki metot ta tamsayı tabanlı aramalar sağlar. `at[]` metodunda **etiket** kullanırken `iat[]` metodunda **indeks değeri olan tamsayı** kullanılır. `loc[]` ve `iloc[]` metoduna benzer mantık.

Bir Veri çerçevesi (DataFrame) veya Seride (Series) **yalnızca tek bir değer** almanız veya ayarlamanız gerekiyorsa `iat[]` metodunu kullanın.

### IndexError (İndeksHatası)

`iat[]` metoduna parametre olarak yazılan **tamsayı değeri**, Veri çerçevesi ya da Seri sınırlarının dışında bulunuyorsa `IndexError` hatası alınır.

`iat[]` metodunun `iloc[]` metoduna benzer şekilde kullanıldığını ifade ettik. O nedenle konuyu uzun uzun açıklamaya gerek görmüyorum. Sadece bir kaç örnek kod inceleyerek konuyu kapatacağım.  
Örnek uygulamalar için bir veri çerçevesi oluşturarak devam edelim;

```python
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  columns=['A', 'B', 'C'])
print(df)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 0   | 0   | 2   | 3   |
| 1   | 0   | 4   | 1   |
| 2   | 10  | 20  | 30  |

### Belirtilen satır/sütun çiftinde değer alın

Satır/sütun değer çifti belirterek tek bir değere erişmek isteyelim. 
Bu işlem, Excel ya da Calc uygulamalarındaki satır ve sütun değerlerinin kesişimindeki hücre değerine ulaşmak ile aynı mantığa sahip.

Veri çerçevemizde satırın 1 numaralı indeksi ile sütunun 2 numaralı indeksinin kesişim değerini seçelim. (İndeks değeri 0'dan başladığı için **2** nolu indeks **C** sütun etiketine tekabül ediyor.)

```python
print(df.iat[1, 2])
```

```python
1
```

### Bir Seri içinden değer elde etmek

Bir seri içerisinden bir değer almak istersen aşağıdaki şekilde kod yazmamız yeterli olacaktır.

Örneğin Öncelikle veri çerçevemizdeki **0.** indekse ait satırı seçip ardıdan **1.** indekse sahip (B) sütununun değerini alalım;

```python
print(df.loc[0].iat[1])
```

```pyt
2
```

[← Önceki Bölüm](pandas-03-veriyi-kesfet-incele.html) | [Sonraki Bölüm →](pandas-05-eksik-kayip-veri-yontemleri.html)
