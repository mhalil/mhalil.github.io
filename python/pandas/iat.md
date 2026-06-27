Title: Pandas - iat
Date: 2022-07-11 00:00
Modified: 2025-06-21 20:06
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, iat
Author: Mustafa Halil

# iat[] Metodu

`iat[]` metodu, satır/sütun çiftinde tamsayı belirtilerek **tek bir değere** erişim sağlamak için kullanılır. ve `iloc[]` metoduna benzerdir, her iki metot ta tamsayı tabanlı aramalar sağlar. `at[]` metodunda **etiket** kullanırken `iat[]` metodunda **indeks değeri olan tamsayı** kullanılır. `loc[]` ve `iloc[]` metoduna benzer mantık.

> Bir Veri çerçevesi (DataFrame) veya Seride (Series) **yalnızca tek bir değer** almanız veya ayarlamanız gerekiyorsa `iat[]` metodunu kullanın.

## IndexError (İndeksHatası)

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

## Belirtilen satır/sütun çiftinde değer alın

Satır/sütun değer çifti belirterek tek bir değere erişmek isteyelim. 
Bu işlem, Excel ya da Calc uygulamalarındaki satır ve sütun değerlerinin kesişimindeki hücre değerine ulaşmak ile aynı mantığa sahip.

Veri çerçevemizde **satırın 1** numaralı indeksi ile **sütunun 2** numaralı indeksinin kesişim değerini seçelim. (İndeks değeri 0'dan başladığı için **2** nolu indeks **C** sütun etiketine tekabül ediyor.)

```python
print(df.iat[1, 2])
```

Çıktı:

```python
1
```

## Bir Seri içinden değer elde etmek

Bir seri içerisinden bir değer almak istersen aşağıdaki şekilde kod yazmamız yeterli olacaktır.

Örneğin Öncelikle veri çerçevemizdeki **0.** indekse ait satırı seçip ardıdan **1.** indekse sahip (B) sütununun değerini alalım;

```python
print(df.loc[0].iat[1])
```

Çıktı:

```pyt
2
```
