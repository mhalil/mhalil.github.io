Title: Pandas 12 - Operator Kullanımı
Date: 2022-07-28 19:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül
Author: Mustafa Halil

# Operator Kullanımı

## Atama Operatorleri

```python
import pandas as pd
```

# Aritmetik İşlem Operatörleri

## sum() Metodu

Python'dan kullanmaya aşina olduğumuz **sum()** fonksiyonu, Pandas içerisinde metot olarak bulunuyor.
Yani Python'da **sum()** fonksiyonuna parametre olarak değişken veriyorduk. 

(Ör. **sum(liste)**).
Pandasta ise veri çerçevesi adının sonuna metot olarak ekliyoruz. 

(Ör. **VeriCercevesi.sum()**)
Örneklerle inceleyelim.

```python
baslik = ["Birler", "Onlar", "Yüzler"]
basliksiz = pd.read_excel("Veri_Setleri/basliksiz.ods", header = None, names = baslik )
print(basliksiz)
```

|     | Birler | Onlar | Yüzler |
| --- | ------ | ----- | ------ |
| 0   | 9      | 82    | 246    |
| 1   | 7      | 78    | 180    |
| 2   | 8      | 83    | 565    |
| 3   | 6      | 82    | 486    |
| 4   | 4      | 37    | 615    |
| 5   | 2      | 18    | 341    |
| 6   | 5      | 12    | 539    |
| 7   | 8      | 59    | 709    |
| 8   | 1      | 89    | 675    |
| 9   | 6      | 12    | 965    |
| 10  | 4      | 24    | 447    |
| 11  | 6      | 35    | 555    |
| 12  | 5      | 34    | 117    |
| 13  | 5      | 21    | 471    |
| 14  | 7      | 31    | 171    |
| 15  | 5      | 40    | 491    |
| 16  | 9      | 55    | 666    |
| 17  | 8      | 48    | 557    |

Elimizde, 17 satır ve 3 sütundan oluşan tablomuz var. Bakalım **sum()** metodunu kullanınca nasıl bir sonuç elde edeceğiz.

```python
print(basliksiz.sum())
```

```python
Birler 105
Onlar 840
Yüzler 8796
dtype: int64
```

Görüyoruz ki, **sum()** metodu sayesinde her sütunun 
toplam değerleri ekrana yazdırılıyor. Peki Tablodaki tüm değerlerin 
toplamını bulmak istersek ne yapmalıyız? **sum()** metodu bize 3 sütun başlığı ve 3 değer verdiğine göre, ikinci bir **sum()** metodu (yani sum() metodunu peşpeşe iki defa yazmak) bu değerlerin toplamını verir mi dersiniz? Deneyelim.

```python
print(basliksiz.sum().sum())
```

```python
9741
```

Tahmin ettiğimiz gibi, iki kez **sum()** metodu kullanmak, tüm veri çerçevesinin toplamını elde etmemizi sağladı.

## mean() Metodu

**Her sütun için** ortalama değer hesaplamak için `mean()` metodunu kullanabiliriz.

```python
basliksiz.mean()
```

```python
Birler      5.833333
Onlar      46.666667
Yüzler    488.666667
dtype: float64
```

**Her satır için** ortalama değer hesaplamak için ise `axis = 1` parametresini ekleyin kodu çalıştırın;

```python
basliksiz.mean(axis = 1)
```

```python
0     112.333333
1      88.333333
2     218.666667
3     191.333333
4     218.666667
5     120.333333
6     185.333333
7     258.666667
8     255.000000
9     327.666667
10    158.333333
11    198.666667
12     52.000000
13    165.666667
14     69.666667
15    178.666667
16    243.333333
17    204.333333
dtype: float64
```

## Toplama, Çıkarma, Çarpma ve Bölme İşlemleri

Veri çerçevesine yeni sütun ekleme konusunu işlerken buna benzer bir örnek uygulama yapmıştık. Sırayla işlemleri tek tek uygulayıp sonucu görelim.

## Toplama Operatörü

**Birler + Onlar** isimli sütun oluşturup, **Birler** ve **Onlar** Sütunlarındaki değerleri toplayıp yeni sütuna dahil edelim.

```python
basliksiz["Birler + Onlar"] = basliksiz["Birler"] + basliksiz["Onlar"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Birler + Onlar |
| --- | ------ | ----- | ------ | -------------- |
| 0   | 9      | 82    | 246    | 91             |
| 1   | 7      | 78    | 180    | 85             |
| 2   | 8      | 83    | 565    | 91             |
| 3   | 6      | 82    | 486    | 88             |
| 4   | 4      | 37    | 615    | 41             |
| 5   | 2      | 18    | 341    | 20             |
| 6   | 5      | 12    | 539    | 17             |
| 7   | 8      | 59    | 709    | 67             |
| 8   | 1      | 89    | 675    | 90             |
| 9   | 6      | 12    | 965    | 18             |
| 10  | 4      | 24    | 447    | 28             |
| 11  | 6      | 35    | 555    | 41             |
| 12  | 5      | 34    | 117    | 39             |
| 13  | 5      | 21    | 471    | 26             |
| 14  | 7      | 31    | 171    | 38             |
| 15  | 5      | 40    | 491    | 45             |
| 16  | 9      | 55    | 666    | 64             |
| 17  | 8      | 48    | 557    | 56             |

## Çıkarma Operatörü

**Yüzler - Onlar** isimli sütun oluşturup, **Yüzler** sütunundaki değerlerden **Onlar** Sütunundaki değerleri çıkarıp yeni sütuna dahil edelim.

```python
basliksiz["Yüzler - Onlar"] = basliksiz["Yüzler"] - basliksiz["Onlar"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Birler + Onlar | Yüzler - Onlar |
| --- | ------ | ----- | ------ | -------------- | -------------- |
| 0   | 9      | 82    | 246    | 91             | 164            |
| 1   | 7      | 78    | 180    | 85             | 102            |
| 2   | 8      | 83    | 565    | 91             | 482            |
| 3   | 6      | 82    | 486    | 88             | 404            |
| 4   | 4      | 37    | 615    | 41             | 578            |
| 5   | 2      | 18    | 341    | 20             | 323            |
| 6   | 5      | 12    | 539    | 17             | 527            |
| 7   | 8      | 59    | 709    | 67             | 650            |
| 8   | 1      | 89    | 675    | 90             | 586            |
| 9   | 6      | 12    | 965    | 18             | 953            |
| 10  | 4      | 24    | 447    | 28             | 423            |
| 11  | 6      | 35    | 555    | 41             | 520            |
| 12  | 5      | 34    | 117    | 39             | 83             |
| 13  | 5      | 21    | 471    | 26             | 450            |
| 14  | 7      | 31    | 171    | 38             | 140            |
| 15  | 5      | 40    | 491    | 45             | 451            |
| 16  | 9      | 55    | 666    | 64             | 611            |
| 17  | 8      | 48    | 557    | 56             | 509            |

## Çarpma Operatörü

**Yüzler * Birler** isimli sütun oluşturup, **Yüzler** sütunundaki değerleri **Birler** Sütunundaki değerlerle çarpıp yeni sütuna dahil edelim.

```python
basliksiz["Yüzler * Birler"] = basliksiz["Yüzler"] * basliksiz["Birler"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Birler + Onlar | Yüzler - Onlar | Yüzler * Birler |
| --- | ------ | ----- | ------ | -------------- | -------------- | --------------- |
| 0   | 9      | 82    | 246    | 91             | 164            | 2214            |
| 1   | 7      | 78    | 180    | 85             | 102            | 1260            |
| 2   | 8      | 83    | 565    | 91             | 482            | 4520            |
| 3   | 6      | 82    | 486    | 88             | 404            | 2916            |
| 4   | 4      | 37    | 615    | 41             | 578            | 2460            |
| 5   | 2      | 18    | 341    | 20             | 323            | 682             |
| 6   | 5      | 12    | 539    | 17             | 527            | 2695            |
| 7   | 8      | 59    | 709    | 67             | 650            | 5672            |
| 8   | 1      | 89    | 675    | 90             | 586            | 675             |
| 9   | 6      | 12    | 965    | 18             | 953            | 5790            |
| 10  | 4      | 24    | 447    | 28             | 423            | 1788            |
| 11  | 6      | 35    | 555    | 41             | 520            | 3330            |
| 12  | 5      | 34    | 117    | 39             | 83             | 585             |
| 13  | 5      | 21    | 471    | 26             | 450            | 2355            |
| 14  | 7      | 31    | 171    | 38             | 140            | 1197            |
| 15  | 5      | 40    | 491    | 45             | 451            | 2455            |
| 16  | 9      | 55    | 666    | 64             | 611            | 5994            |
| 17  | 8      | 48    | 557    | 56             | 509            | 4456            |

## Bölme Operatörü

**Yüzler / Onlar** isimli sütun oluşturup, **Yüzler** sütunundaki değerleri **Onlar** Sütunundaki değerlere Bölüp yeni sütuna dahil edelim.

```python
basliksiz["Yüzler * Onlar"] = basliksiz["Yüzler"] / basliksiz["Onlar"]
print(basliksiz)
```

|     | Birler | Onlar | Yüzler | Birler + Onlar | Yüzler - Onlar | Yüzler * Birler | Yüzler * Onlar |
| --- | ------ | ----- | ------ | -------------- | -------------- | --------------- | -------------- |
| 0   | 9      | 82    | 246    | 91             | 164            | 2214            | 3.000000       |
| 1   | 7      | 78    | 180    | 85             | 102            | 1260            | 2.307692       |
| 2   | 8      | 83    | 565    | 91             | 482            | 4520            | 6.807229       |
| 3   | 6      | 82    | 486    | 88             | 404            | 2916            | 5.926829       |
| 4   | 4      | 37    | 615    | 41             | 578            | 2460            | 16.621622      |
| 5   | 2      | 18    | 341    | 20             | 323            | 682             | 18.944444      |
| 6   | 5      | 12    | 539    | 17             | 527            | 2695            | 44.916667      |
| 7   | 8      | 59    | 709    | 67             | 650            | 5672            | 12.016949      |
| 8   | 1      | 89    | 675    | 90             | 586            | 675             | 7.584270       |
| 9   | 6      | 12    | 965    | 18             | 953            | 5790            | 80.416667      |
| 10  | 4      | 24    | 447    | 28             | 423            | 1788            | 18.625000      |
| 11  | 6      | 35    | 555    | 41             | 520            | 3330            | 15.857143      |
| 12  | 5      | 34    | 117    | 39             | 83             | 585             | 3.441176       |
| 13  | 5      | 21    | 471    | 26             | 450            | 2355            | 22.428571      |
| 14  | 7      | 31    | 171    | 38             | 140            | 1197            | 5.516129       |
| 15  | 5      | 40    | 491    | 45             | 451            | 2455            | 12.275000      |
| 16  | 9      | 55    | 666    | 64             | 611            | 5994            | 12.109091      |
| 17  | 8      | 48    | 557    | 56             | 509            | 4456            | 11.604167      |

## Mantıksal / Karşılaştırma Operatörleri

Bu konuya da diğer bölümlerde değinmiştik, Konu başlığı bu bölüme ait olduğu için tekrar anlatmakta farar görüyorum.

Mantıksal Operatorler (Boolean), **True (Doğru)** ya da **False (Yanlış)** çıktı verirler. Veri çerçevemizdeki değer ya da metinlerin (string 
ifadelerin) belirlenen değerlere uyup uymadığına dair çıktı almak ya da 
hesap yapmak için kullanılabilir.

**Bu Operatörler;**

- Büyüktür (>),
- Küçüktür (<),
- Eşittir (==),
- Eşit Değildir (!=),
- İçerir (contains),
- İçermez / Değil (not)

örnek olarak verilebilir.

Şimdi bu operatorleri inceleyelim. Öncelikle varolan tablolarımızda birini içe aktarıp veri çerçevesine dönüştürelim.

```python
json = pd.read_json("Veri_Setleri/json_verisi.json")
json
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | 60       | 110   | 130      | 409      |
| 1   | 60       | 117   | 145      | 479      |
| 2   | 60       | 103   | 135      | 340      |
| 3   | 45       | 109   | 175      | 282      |
| 4   | 45       | 117   | 148      | 406      |
| 5   | 60       | 102   | 127      | 300      |

## Büyüktür (>) ve Küçüktür (<) Operatörleri

Veri çerçevemizde 110'dan büyük verileri bulmaya çalışalım. Bu işlemi **büyüktür (>)** operatörü ile yapacağız.

```python
json > 110
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | False    | False | True     | True     |
| 1   | False    | True  | True     | True     |
| 2   | False    | False | True     | True     |
| 3   | False    | False | True     | True     |
| 4   | False    | True  | True     | True     |
| 5   | False    | False | True     | True     |

Gördüğünüz gibi, tablodaki tüm değerler verilen kriter olan 110'dan 
büyük olup olmadığına göre sorgulandı ve cevabı her bir hücreye işlendi.

Sütunlarda, Değeri 110'dan büyük kaçar adet sayı olduğunu bulmak istersek;

```python
(json > 110).sum()
```

```python
Duration 0
Pulse 2
Maxpulse 6
Calories 6
dtype: int64
```

Veri çerçevemizde, 110'dan büyük toplam kaç adet sayı vardır, diye merak edersek;

```python
(json > 110).sum().sum()
```

```python
14
```

**Küçüktür (<)** operatörünün kullanımı da aynıdır.
Veri çerçevemizdeki, **150'den küçük** verileri görelim.

```python
json < 150
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | True     | True  | True     | False    |
| 1   | True     | True  | True     | False    |
| 2   | True     | True  | True     | False    |
| 3   | True     | True  | False    | False    |
| 4   | True     | True  | True     | False    |
| 5   | True     | True  | True     | False    |

## Eşittir (==) ve Eşit Değil (!=) Operatörleri

**Eşittir (==)** ya da bir başka deyimle **Eşit midir?** operatörü :) (Eşitse True değeri döndür demektir)

Veri çerçevemizde **60**'a eşit değerleri bulalım. Bunu **==** operatörü ile tespit edeceğiz.

```python
json == 60
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | True     | False | False    | False    |
| 1   | True     | False | False    | False    |
| 2   | True     | False | False    | False    |
| 3   | False    | False | False    | False    |
| 4   | False    | False | False    | False    |
| 5   | True     | False | False    | False    |

Veri çerçevemizde **60**'a eşit kaç adet toplam değer var?

```python
(json == 60).sum().sum()
```

```python
4
```

Veri çerçevemizde **117**'ye eşit olmayan sayı var mı? Varsa "True" diye göster.

```python
json != 117
```

|     | Duration | Pulse | Maxpulse | Calories |
| --- | -------- | ----- | -------- | -------- |
| 0   | True     | True  | True     | True     |
| 1   | True     | False | True     | True     |
| 2   | True     | True  | True     | True     |
| 3   | True     | True  | True     | True     |
| 4   | True     | False | True     | True     |
| 5   | True     | True  | True     | True     |

Veri çerçevemizde **117**'den farklı kaç sayı var?

Bunların Sütun dağılımları nasıl?

```python
(json != 117).sum().sum()
```

```python
22
```

```python
(json != 117).sum()
```

```python
Duration    6
Pulse       4
Maxpulse    6
Calories    6
dtype: int64
```

## İçerir / İçermez Operatörleri

Bu
 konuyu, Metin bazlı (string ifadeler) veri çerçeveleri ile daha rahat 
anlatabileceğimi düşünüyorum. Hemen yeni bir Veri çerçevesi oluşturalım.

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

**nba** isimli veri çerçevemizde isminin içinde **Jordan** kelimesi bulunan kaç adet oyunucu olduğunu bulmaya çalışalım. Bunu, String Metotlarında **contains()** ile tespit etmeye çalışacağız.

```python
print(nba["Name"].str.contains("Jordan").sum())
```

```python
8
```

İsim-Soyisim içinde **Jordan** kelimesi bulunan oyuncuların hangi sütunda kaç adet verisi bulunuyor?

```python
jordan = nba["Name"].str.contains("Jordan")
print(nba.groupby(jordan).count())
```

| Name  | Name | Team | Number | Position | Age | Height | Weight | College | Salary |
| ----- | ---- | ---- | ------ | -------- | --- | ------ | ------ | ------- | ------ |
| False | 449  | 449  | 449    | 449      | 449 | 449    | 449    | 365     | 439    |
| True  | 8    | 8    | 8      | 8        | 8   | 8      | 8      | 8       | 7      |

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

[← Önceki Bölüm ](pandas-11-melt-fonksiyonunun-kullanimi.html) |
