Title: Pandas - at
Date: 2022-07-11 00:00
Modified: 2025-06-21 20:04
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Fonksiyon, at
Author: Mustafa Halil

# at[] Metodu

`at[]` metodunu, bir satır/sütun etiket çifti belirterek **tek bir değere erişmek** için kullanabiliriz. MS Excel ya da Libre Ofis Calc uygulamalarındaki <u>satır ve sütun değerlerinin kesişimindeki hücre değerine ulaşmak</u> ile aynı mantık.

> `loc[]` metoduna benzer şekilde kullanılır, her ikisi de etiket tabanlı aramalar sağlar. Bir Veri çerçevesi (DataFrame) veya Seride (Series) **yalnız tek bir değer** almanız veya ayarlamanız gerekiyorsa `at[]` metodunu kullanın.

## KeyError (AnahtarHatası)

`at[]` metoduna parametre olarak yazılan **etiket**, Veri çerçevesi ya da Seride bulunmuyorsa `KeyError` hatası alınır.

## ValueError (DeğerHatası)

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

## Belirtilen satır/sütun çiftinde değer alın

Satır/sütun etiket çifti belirterek tek bir değere erişmek isteyelim.
 Bu işlem, Excel ya da Calc uygulamalarındaki satır ve sütun değerlerinin kesişimindeki hücre değerine ulaşmak ile aynı mantığa sahip.

Veri çerçevemizdeki **4.** indeks ile **B** sütununun kesişim değerini seçelim.

```python
print(df.at[4, 'B'])
```

Çıktı:

```python
2
```

## Bir Seri içinden değer elde etmek

Malumunuz, veri çerçevesinden sadece bir satır seçtiğimiz zaman sonuç olarak bir seri elde etmiş oluyoruz, çünkü Seriler tek boyutlu dizilerdir. Bu seri içerisinden bir değer almak istersen aşağıdaki şekilde kod yazmamız yeterli olacaktır.

Örneğin Öncelikle veri çerçevemizdeki **5.** indekse ait satırı seçip ardıdan **B** sütununun değerini alalım;

```python
print(df.loc[5].at['B'])
```

Çıktı:

```python
4
```
