Title: Pandas - sum operatörü
Date: 2022-07-28 19:00
Modified: 2025-12-04 21:30
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, sum, topla, metot
Author: Mustafa Halil

# `sum()` Metodu

Python'dan **toplam değeri bulmak** için kullanmaya aşina olduğumuz `sum()` fonksiyonu, Pandas içerisinde metot olarak bulunuyor.
Yani Python'da `sum()` fonksiyonuna parametre olarak bir değişken veriyorduk.  (Ör. `sum(liste)`).
Pandasta ise veri çerçevesi adının sonuna metot olarak ekliyoruz.  (Ör. `VeriCercevesi.sum()`)

Örneklerle inceleyelim.

```python
baslik = ["Birler", "Onlar", "Yüzler"]
df = pd.read_excel("Veri_Setleri/basliksiz.ods", 
                            header = None, names = baslik )
print(df)
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

Elimizde, 17 satır ve 3 sütundan oluşan tablomuz var. Bakalım `sum()` metodunu kullanınca nasıl bir sonuç elde edeceğiz.

```python
print(df.sum())
```

```python
Birler 105
Onlar 840
Yüzler 8796
dtype: int64
```

Görüyoruz ki, `sum()` metodu sayesinde **her sütunun toplam değerleri** ekrana yazdırılıyor. Peki Tablodaki tüm değerlerin toplamını bulmak istersek ne yapmalıyız? `sum()` metodu bize 3 sütun başlığı ve 3 değer verdiğine göre, ikinci bir `sum()` metodu (yani `sum()` metodunu peşpeşe iki defa yazmak) bu değerlerin toplamını verir mi dersiniz? Deneyelim.

```python
print(df.sum().sum())
```

```python
9741
```

Tahmin ettiğimiz gibi, iki kez `sum()` metodu kullanmak, tüm veri çerçevesinin toplamını elde etmemizi sağladı.

Peki her sütunun toplamını Veri çerçevesinin son satırına eklemek istersek nasıl bir yol uygulamak gerekir? derseniz, aşağıdaki kodu inceleyin.

```python
toplam = df.sum()

df_toplam = toplam.to_frame().transpose()
df_toplam.index = ["Toplam"]

df = pd.concat([df, df_toplam])
print(df)
```

Çıktı:

```python
        Birler  Onlar  Yüzler
0            9     82     246
1            7     78     180
2            8     83     565
3            6     82     486
4            4     37     615
5            2     18     341
6            5     12     539
7            8     59     709
8            1     89     675
9            6     12     965
10           4     24     447
11           6     35     555
12           5     34     117
13           5     21     471
14           7     31     171
15           5     40     491
16           9     55     666
17           8     48     557
Toplam     105    840    8796
```

|        | Birler | Onlar | Yüzler |
| ------ | ------ | ----- | ------ |
| 0      | 9      | 82    | 246    |
| 1      | 7      | 78    | 180    |
| 2      | 8      | 83    | 565    |
| 3      | 6      | 82    | 486    |
| 4      | 4      | 37    | 615    |
| 5      | 2      | 18    | 341    |
| 6      | 5      | 12    | 539    |
| 7      | 8      | 59    | 709    |
| 8      | 1      | 89    | 675    |
| 9      | 6      | 12    | 965    |
| 10     | 4      | 24    | 447    |
| 11     | 6      | 35    | 555    |
| 12     | 5      | 34    | 117    |
| 13     | 5      | 21    | 471    |
| 14     | 7      | 31    | 171    |
| 15     | 5      | 40    | 491    |
| 16     | 9      | 55    | 666    |
| 17     | 8      | 48    | 557    |
| Toplam | 105    | 840   | 8796   |

Kodu parçalara ayırarak açıklayalım;

* Sütun toplamları;

```python
toplam = df.sum()
print(toplam)
```

Çıktı:

```python
Birler     105
Onlar      840
Yüzler    8796
dtype: int64
```

Çıktı bir `Series` objesidir.

* `Series` objesini **Veri Çerçevesi**ne (**DataFrame**'e) dönüştürmek için `.to_frame()` metodunu kullanıyoruz. 

```python
df_toplam = toplam.to_frame().transpose()
print(df_toplam)
```

Çıktı:

```python
           0
Birler   105
Onlar    840
Yüzler  8796
```

Veri çerçeveleri şuan birleştirilmeye uygun değil. Önce **df_toplam** isimli veri çerçevemizin transpozunu almalıyız ki, birleştirme işlemi öncesi veri çerçevelerinin sütun isimleri aynı olsun.

```python
df_toplam = df_toplam.transpose()
print(df_toplam)
```

Çıktı:

```python
   Birler  Onlar  Yüzler
0     105    840    8796
```

**df_toplam** isimli veri çerçevemizin indek değerini de Toplam diye değiştirelim;

```python
df_toplam.index = ["Toplam"]
print(df_toplam)
```

Çıktı:

```python
        Birler  Onlar  Yüzler
Toplam     105    840    8796
```

Şuan veri çerçevelerini birleştirme için herşey hazır görünüyor.

```python
df = pd.concat([df, df_toplam])
print(df)
```

Çıktı:

```python
        Birler  Onlar  Yüzler
0            9     82     246
1            7     78     180
2            8     83     565
3            6     82     486
4            4     37     615
5            2     18     341
6            5     12     539
7            8     59     709
8            1     89     675
9            6     12     965
10           4     24     447
11           6     35     555
12           5     34     117
13           5     21     471
14           7     31     171
15           5     40     491
16           9     55     666
17           8     48     557
Toplam     105    840    8796
```
