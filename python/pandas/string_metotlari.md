Title: Pandas - String_Metotlari
Date: 2022-07-15 00:00
Modified: 2025-11-16 15:15
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Düzenleme, String, Metot, upper, lower, capitalize, contains
Author: Mustafa Halil

# String Metotları

Python ile kodlama yaparken, metinsel ifadelerle uğraştığımızda kullandığımız **string metotlarını** hatırlarsınız. Örneğin, Metinlerin tümünü büyük harfe ya da küçük harfe
 çevirmek. Bu tür string metotları Pandas ile kulanmak ve veri çerçevesine uygulamak mümkün. Bunun için `str` ifadesini kullanabiliriz. 

Önce Bir Veri Çerçevesi oluşturalım ve gözatalım.

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

## upper() Metodu

Veri çerçevemizim **sütun başlık**larının **tüm karakterlerini büyük harfe çevirelim**.

```python
veri.columns = veri.columns.str.upper()
print(veri)
```

|     | ISIM       | YAŞ | IŞ-MESLEK   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | mühendis    |
| 1   | Halil      | 38  | programci   |
| 2   | Burak      | 41  | akademisyen |
| 3   | Emre       | 23  | yönetici    |
| 4   | Ersin      | 37  | amir        |
| 5   | Sertaç     | 52  | mühendis    |
| 6   | Furkan     | 30  | yönetici    |
| 7   | Murat      | 23  | müdür       |
| 8   | Ahmet      | 40  | veteriner   |
| 9   | Abdülkadir | 38  | yönetici    |

Şimdi de Veri Çerçevemizin **iş-meslek** sütunundaki tüm metinleri büyük harfe çevirip ekrana yazdıralım.

```python
print(veri["iş-meslek"].str.upper())
```

```python
0       MÜHENDIS
1      PROGRAMCI
2    AKADEMISYEN
3       YÖNETICI
4           AMIR
5       MÜHENDIS
6       YÖNETICI
7          MÜDÜR
8      VETERINER
9       YÖNETICI
Name: iş-meslek, dtype: object
```

Uyguladığımız metot sonrası, veri çerçevemizi tekrar çağırdığımızda, **iş-meslek** sütunundaki metinlerin değişmediğini, eski halinde kaldığını göreceğiz.
 Bunu sebebi, yaptığımız değişikliği bir değişken olarak alıp, **iş-meslek** sütununa atamamaktır. İfade etmeye çalıştığım şeyin, aşağıdaki satırda daha net anlaşılacağını düşünüyorum. Atama işlem sonrası Veri çerçevemizi çağırıp değişikiğin uygulandığını görüyoruz.

```python
veri["iş-meslek"] = veri["iş-meslek"].str.upper()
print(veri)
```

|     | ISIM       | YAŞ | IŞ-MESLEK   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | MÜHENDIS    |
| 1   | Halil      | 38  | PROGRAMCI   |
| 2   | Burak      | 41  | AKADEMISYEN |
| 3   | Emre       | 23  | YÖNETICI    |
| 4   | Ersin      | 37  | AMIR        |
| 5   | Sertaç     | 52  | MÜHENDIS    |
| 6   | Furkan     | 30  | YÖNETICI    |
| 7   | Murat      | 23  | MÜDÜR       |
| 8   | Ahmet      | 40  | VETERINER   |
| 9   | Abdülkadir | 38  | YÖNETICI    |

## lower() Metodu

<u>İlk oluşturulan</u> veri çerçevemizdeki **isim** sütunundaki verilerin **tüm karakterlerini küçük harfe çevirelim**.

```python
veri.isim = veri.isim.str.lower()

print(veri)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | mustafa    | 25  | mühendis    |
| 1   | halil      | 38  | programcı   |
| 2   | burak      | 41  | akademisyen |
| 3   | emre       | 23  | yönetici    |
| 4   | ersin      | 37  | amir        |
| 5   | sertaç     | 52  | mühendis    |
| 6   | furkan     | 30  | yönetici    |
| 7   | murat      | 23  | müdür       |
| 8   | ahmet      | 40  | veteriner   |
| 9   | abdülkadir | 38  | yönetici    |

## capitalize() Metodu

<u>İlk oluşturulan</u> veri çerçevemizdeki **iş-meslek** Sütunundaki verilerin **sadece baş harflerini büyük** yapalım.

```python
veri["iş-meslek"] = veri["iş-meslek"].str.capitalize()
print(veri)
```

|     | isim       | yaş | iş-meslek   |
| --- | ---------- | --- | ----------- |
| 0   | Mustafa    | 25  | Mühendis    |
| 1   | Halil      | 38  | Programci   |
| 2   | Burak      | 41  | Akademisyen |
| 3   | Emre       | 23  | Yönetici    |
| 4   | Ersin      | 37  | Amir        |
| 5   | Sertaç     | 52  | Mühendis    |
| 6   | Furkan     | 30  | Yönetici    |
| 7   | Murat      | 23  | Müdür       |
| 8   | Ahmet      | 40  | Veteriner   |
| 9   | Abdülkadir | 38  | Yönetici    |

## contains() Metodu

**String** metotlarından biri olan **contains** ile metin içerisinde **içeren** kelime ya da kelimeleri aratabiliyoruz. `lower()` metodu ile **isim** sütunundaki  tüm karakterleri küçük harfe çevirelim ve ardından isim içinde **er** ibaresi bulunan tüm verileri filtreleyelim.

```python
veri.isim = veri.isim.str.lower()
iceren = veri.isim.str.contains("er")
print(veri[iceren])
```

|     | isim   | yaş | iş-meslek |
| --- | ------ | --- | --------- |
| 4   | ersin  | 37  | amir      |
| 5   | sertaç | 52  | mühendis  |

Görüldüğü üzere **4. ve 5.** indekslerdeki **ersin** ve **sertaç** ifadelerinin içerisinde **er** ibaresi bulunduğu için filtre işlemi sonucu yukarıdaki çıktıya ulaşıyoruz. 

Benzer sonuca aşağıdaki kod ile de ulaşabiliriz.

```python
iceren = veri.isim.str.lower().str.contains("er")
print(veri[iceren])
```

|     | isim   | yaş | iş-meslek |
| --- | ------ | --- | --------- |
| 4   | Ersin  | 37  | amir      |
| 5   | Sertaç | 52  | mühendis  |

Son iki tabloyu incelerseniz **İsim** sütunundaki verilerin **büyük-küçük harf** değerlerinin farklı olduğunu görebilirsiniz.

Yeni bir veri seti ile bir örnek daha yapalım.

```python
nba = pd.read_csv("Veri_Setleri/nba.csv")
print(nba)
```

|     | Name          | Team           | Number | Position | Age  | Height | Weight | College           | Salary    |
| --- | ------------- | -------------- | ------ | -------- | ---- | ------ | ------ | ----------------- | --------- |
| 0   | Avery Bradley | Boston Celtics | 0.0    | PG       | 25.0 | 6-2    | 180.0  | Texas             | 7730337.0 |
| 1   | Jae Crowder   | Boston Celtics | 99.0   | SF       | 25.0 | 6-6    | 235.0  | Marquette         | 6796117.0 |
| 2   | John Holland  | Boston Celtics | 30.0   | SG       | 27.0 | 6-5    | 205.0  | Boston University | NaN       |
| 3   | R.J. Hunter   | Boston Celtics | 28.0   | SG       | 22.0 | 6-5    | 185.0  | Georgia State     | 1148640.0 |
| 4   | Jonas Jerebko | Boston Celtics | 8.0    | PF       | 29.0 | 6-10   | 231.0  | NaN               | 5000000.0 |
| ... | ...           | ...            | ...    | ...      | ...  | ...    | ...    | ...               | ...       |
| 453 | Shelvin Mack  | Utah Jazz      | 8.0    | PG       | 26.0 | 6-3    | 203.0  | Butler            | 2433333.0 |
| 454 | Raul Neto     | Utah Jazz      | 25.0   | PG       | 24.0 | 6-1    | 179.0  | NaN               | 900000.0  |
| 455 | Tibor Pleiss  | Utah Jazz      | 21.0   | C        | 26.0 | 7-3    | 256.0  | NaN               | 2900000.0 |
| 456 | Jeff Withey   | Utah Jazz      | 24.0   | C        | 26.0 | 7-0    | 231.0  | Kansas            | 947276.0  |
| 457 | NaN           | NaN            | NaN    | NaN      | NaN  | NaN    | NaN    | NaN               | NaN       |

458 rows × 9 columns

**nba** isimli veri çerçevemizde isminin içinde **Jordan** kelimesi bulunan **kaç adet** oyunucu olduğunu bulmaya çalışalım. Bunu, `sum()` metodu ve String Metotlarında `contains()` ile tespit etmeye çalışacağız.

```python
print(nba["Name"].str.contains("Jordan").sum())
```

```python
8
```

İsim-Soyisim içinde **Jordan** kelimesi bulunan oyuncuların **hangi sütunda kaç adet** verisi bulunuyor?

```python
jordan = nba["Name"].str.contains("Jordan")
print(nba.groupby(jordan).count())
```

| Name  | Name | Team | Number | Position | Age | Height | Weight | College | Salary |
| ----- | ---- | ---- | ------ | -------- | --- | ------ | ------ | ------- | ------ |
| False | 449  | 449  | 449    | 449      | 449 | 449    | 449    | 365     | 439    |
| True  | 8    | 8    | 8      | 8        | 8   | 8      | 8      | 8       | 7      |

Eksik ve Kayıp verileri temizlersek;

```python
nba2 = nba.dropna()
print(nba2)
```

|     | Name          | Team           | Number | Position | Age  | Height | Weight | College       | Salary    |
| --- | ------------- | -------------- | ------ | -------- | ---- | ------ | ------ | ------------- | --------- |
| 0   | Avery Bradley | Boston Celtics | 0.0    | PG       | 25.0 | 6-2    | 180.0  | Texas         | 7730337.0 |
| 1   | Jae Crowder   | Boston Celtics | 99.0   | SF       | 25.0 | 6-6    | 235.0  | Marquette     | 6796117.0 |
| 3   | R.J. Hunter   | Boston Celtics | 28.0   | SG       | 22.0 | 6-5    | 185.0  | Georgia State | 1148640.0 |
| 6   | Jordan Mickey | Boston Celtics | 55.0   | PF       | 21.0 | 6-8    | 235.0  | LSU           | 1170960.0 |
| 7   | Kelly Olynyk  | Boston Celtics | 41.0   | C        | 25.0 | 7-0    | 238.0  | Gonzaga       | 2165160.0 |
| ... | ...           | ...            | ...    | ...      | ...  | ...    | ...    | ...           | ...       |
| 449 | Rodney Hood   | Utah Jazz      | 5.0    | SG       | 23.0 | 6-8    | 206.0  | Duke          | 1348440.0 |
| 451 | Chris Johnson | Utah Jazz      | 23.0   | SF       | 26.0 | 6-6    | 206.0  | Dayton        | 981348.0  |
| 452 | Trey Lyles    | Utah Jazz      | 41.0   | PF       | 20.0 | 6-10   | 234.0  | Kentucky      | 2239800.0 |
| 453 | Shelvin Mack  | Utah Jazz      | 8.0    | PG       | 26.0 | 6-3    | 203.0  | Butler        | 2433333.0 |
| 456 | Jeff Withey   | Utah Jazz      | 24.0   | C        | 26.0 | 7-0    | 231.0  | Kansas        | 947276.0  |

364 rows × 9 columns

Veri satır sayımız 458'den 364'e düşmüş oldu.

Şimdi **Name** sütunu içerisinde **Jordon** kelimesi geçen tüm verileri görelim.

```python
isimler = nba2["Name"]
jrd = isimler.str.contains("Jordan")
print(nba2[jrd])
```

|     | Name            | Team                 | Number | Position | Age  | Height | Weight | College   | Salary     |
| --- | --------------- | -------------------- | ------ | -------- | ---- | ------ | ------ | --------- | ---------- |
| 6   | Jordan Mickey   | Boston Celtics       | 55.0   | PF       | 21.0 | 6-8    | 235.0  | LSU       | 1170960.0  |
| 98  | DeAndre Jordan  | Los Angeles Clippers | 6.0    | C        | 27.0 | 6-11   | 265.0  | Texas A&M | 19689000.0 |
| 110 | Jordan Clarkson | Los Angeles Lakers   | 6.0    | PG       | 24.0 | 6-5    | 194.0  | Missouri  | 845059.0   |
| 175 | Jordan McRae    | Cleveland Cavaliers  | 12.0   | SG       | 25.0 | 6-5    | 179.0  | Tennessee | 111196.0   |
| 201 | Jordan Hill     | Indiana Pacers       | 27.0   | C        | 28.0 | 6-10   | 235.0  | Arizona   | 4000000.0  |
| 257 | Jordan Adams    | Memphis Grizzlies    | 3.0    | SG       | 21.0 | 6-5    | 209.0  | UCLA      | 1404600.0  |
| 289 | Jordan Hamilton | New Orleans Pelicans | 25.0   | SG       | 25.0 | 6-7    | 220.0  | Texas     | 1015421.0  |

## get() Metodu

`get()` metodu ile bir string'in istediğimiz karakterini elde edebiliriz.

Örnek verimiz;

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

Şimdi `get()` metodu ile **isim** sütunundaki verilerin ilk karakterlerini ekrana yazdıralım;

```python
print(veri["isim"].str.get(0))
```

Çıktı:

```python
0    M
1    H
2    B
3    E
4    E
5    S
6    F
7    M
8    A
9    A
Name: isim, dtype: object
```

Peki **isim** sütunundaki verilerin son karakterlerini ekrana yazdırmak istersek ne yapmalıyız;

```python
print(veri["isim"].str.get(-1))
```

Çıktı:

```python
0    a
1    l
2    k
3    e
4    n
5    ç
6    n
7    t
8    t
9    r
Name: isim, dtype: object
```

## slice() Metodu

`slice()` metodu ile ile bir string'in istediğimiz karakter aralığını elde edebiliriz.
Verimiz:

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

**isim** sütunundaki verilerin ilk 3 karakterlerini ekrana yazdırmak isteyelim;

```python
print(veri["isim"].str.slice(0,3))
```

Çıktı:

```python
0    Mus
1    Hal
2    Bur
3    Emr
4    Ers
5    Ser
6    Fur
7    Mur
8    Ahm
9    Abd
Name: isim, dtype: object
```

Son 3 karakteri görelim;

```python
print(veri["isim"].str.slice(-3))
```

Çıktı:

```python
0    afa
1    lil
2    rak
3    mre
4    sin
5    taç
6    kan
7    rat
8    met
9    dir
Name: isim, dtype: object
```
