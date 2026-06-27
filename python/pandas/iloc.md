Title: Pandas - iloc
Date: 2022-07-11 00:00
Modified: 2025-06-21 18:58
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, Seçim, iloc
Author: Mustafa Halil

# iloc[] Fonksiyonu Nedir? Nasıl Kullanılır?

Veri Çerçevesindeki istenilen satır ve sütunu seçmek/görüntülemek için **iloc[]** metodu kullanılır. **iloc[]** kelimesini unutmamak için **İndex Location** (**Konumun İndeks Değeri**) ya da **İnteger Location (Konumun Tamsayı değeri)** gibi düşünebilir, hafızanızda kodlayabilirsiniz. Bir başka ifadeyle, `iloc[]` için, Tamsayı değerine dayalı konum indeksleme metodu diyebiliriz. Esas olarak **iloc[]** metodu, hem satır hem de sütun numarası alarak çalışır.

```python
Veri_Cercevesi_Adı.iloc[Satir_Numarası, Sütun_Numarası]
```

`iloc[]` metodunun alabileceği parametreler şunlardır:  

- Bir satır ve sütun dizininden oluşan bir demet, ör. `(0,1)`
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

Veri çerçevemizde istediğimiz satır/sütun kesişimindeki değeri **.iloc[]** metodu ile seçelim.

```python
print(veri.iloc[8,2])
```

Çıktı:

```python
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

# Sadece Satırları Listelemek

## Bir Tamsayı ile Satır Seçimi

`iloc[]` metoduna parametre olarak sadece **bir tamsayı değeri** girildiğinde, girilen sayıya (indeks bilgisine) ait **satır** verisi döndürülür. Bu veri, Seri (Series) tipindedir. Hemen aşağıdaki örneğe bakalım.

```python
print(veri.iloc[5])
```

Çıktı:

```python
isim           Sertaç
yaş                52
iş-meslek    mühendis
Name: 5, dtype: object
```

## Bir Sayı Listesi ile Satır Seçimi

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

## Dilimleyerek Satır Seçimi

Python'da **listeler** konusunu okuduğunuzda, dilimlemenin nasıl yapıldığını da görmüş olmalısınız. Kısaca bahsedecek olursak, dilimleme için `:` karakteri kullanılır. 

`:` karakterinin solunda **başlangıç**, sağında **bitiş** değeri yazılır. Elimizde veri çerçevemizin indeks değerleri gibi **0 ile 9** arasında sayılardan oluşan bir liste varsa, bu listeden aralık seçmek yani dilimleme yapmak istersek aşağıdaki kodu yazmalıyız.

`[1:5]`

Yukarıdaki kodun anlamı, 1. öğeden başlayarak **5. öğeye kadar** (yani 5. öğe dahil **DEĞİL**) dilimleme yap, 1,2,3,4 sonucunu ver.

`[3:]`

Yukarıdaki kodun anlamı, **3. öğeden başlayarak** listenin sonuna kadar dilimleme yap, 3,4,5,6,7,8,9 sonucunu ver.

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

## Satır ve Sütunları Belirterek Listelemek

Yukarıda yazdığımız `veri.iloc[8,2]` kodu, hem satır hemde sütun belirterek değer elde ettiğimiz bir indeksleme yöntemidir.

## Satır ve Sütunda dilimleme yapmak

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

`veri.iloc[3:8,:2]` kodu ile, 3 - 8 arası satır, 0 - 2 arası sütun verileri dilimlenmiş. (**Satırlarda**, 3'ten başlayan 8'de biten bir sınırlama yazılmış, **Sütunlarda** başlangıçta sınır yok yani 0'dan başlıyor, 2. sütuna kadar sınırlama getirilmiş.)

## Satırla aynı uzunluktaki mantık (boole) listesiyle / maskesiyle Satır Seçimi

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
