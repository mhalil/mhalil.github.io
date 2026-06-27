Title: Pandas - apply
Date: 2022-07-15 00:00
Modified: 2025-11-29 14:20
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, apply
Author: Mustafa Halil

# apply() Metodu

Python programlama dilini öğrenirken karşılaştığımız **fonksiyonlar** konusunu hatırlarsınız. Kullanıcı tarafından yazılan ya da standart python fonksiyonlarını, veri çerçevemize uygulamak istersek, `apply()` metodunu kullanmamız gerekir.

Basit bir Veri Çerçevesi (Data Frame) oluşturalım ve oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", 
                    "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"],
                    "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
                   "iş-meslek" : ["mühendis", "programcı", "akademisyen",
                    "yönetici","amir","mühendis", "yönetici","müdür",
                    "veteriner","yönetici"]}
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

## Kullanıcı Tanımlı Fonksiyon ile Kullanım

Yukarıdaki **iş-meslek** sütunundaki metinlerin büyük harfe dönüştürülmesi örneğini, bir de `apply()` fonksiyonu ile uygulayalım.

```python
def buyuk_harf(x):
    return x.upper()

print(veri["IŞ-MESLEK"].apply(buyuk_harf))
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
Name: IŞ-MESLEK, dtype: object
```

İşlemin kalıcı olmsı için yine atama operatörünü kullanmalıyız.

```python
veri["IŞ-MESLEK"] = veri["IŞ-MESLEK"].apply(buyuk_harf)
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

**apply()** Metodu ile alakalı farklı bir örnek yapalım. **ilceler.txt** isimli dosya içeriğini okuyup bir seriye dönüştürelim.

```python
import pandas as pd

dosya = "ilceler.txt"

seri = pd.Series(ilk_kelime.strip() 
                for ilk_kelime in open(dosya))

print(seri.head())
```

İlk 5 satırın çıktısı:

```python
0    Arnavutköy
1    Bayrampaşa
2      Beşiktaş
3       Beyoğlu
4       Esenler
dtype: object
```

**ilceler.txt** isimli dosya içeriğinde kaç satır veri var, `len()` fonksiyonu ile öğrenelim.

```python
print(len(seri))
```

Çıktı:

```python
39
```

Peki `len()` fonksiyonunu, `apply()` fonksiyonu ile birlikte kullanarak her bir satırdaki string'in uzunluğunu bulmak istersek nasıl kod yazmalıyız derseniz;

```python
print(seri.apply(len))
```

Çıktı:

```python
0     10
1     10
2      8
3      7
4      7
5     10
6      5
7     13
8      9
9      7
10    10
11     5
12     7
13     8
14    12
15     8
16    10
17    10
18    12
19     7
20     8
21     8
22    12
23     7
24    11
25     6
26     8
27     6
28     8
29     7
30     6
31     7
32     6
33    10
34    11
35     4
36     5
37     8
38     7
dtype: int64
```

Yukarıdaki sonuca, aşağıdaki kod ile de ulaşabiliriz.

```python
print(seri.str.len())
```

>  **String metotları, apply()** metodundan daha hızlıdır. İmkan varsa string metotlarını kullanın.

## lambda() Fonksiyonu ile Kullanım

Dosya içeriğindeki her bir satırın ilk karakterini ekrana yazdıralım;

```python
print(seri.apply(lambda x: x[0]))
```

Çıktı:

```python
0     A
1     B
2     B
3     B
4     E
5     E
6     F
7     G
8     K
9     S
10    S
11    Ş
12    A
13    B
14    B
15    B
16    B
17    B
18    B
19    Ç
20    E
21    G
22    K
23    S
24    Z
25    A
26    A
27    B
28    Ç
29    K
30    K
31    M
32    P
33    S
34    S
35    Ş
36    T
37    Ü
38    Ü
dtype: object
```

Aynı sonucu string metotları kullanarak elde edelim;

```python
print(seri.str.get(0))
```

Çıktı:

```python
0     A
1     B
2     B
3     B
4     E
5     E
6     F
7     G
8     K
9     S
10    S
11    Ş
12    A
13    B
14    B
15    B
16    B
17    B
18    B
19    Ç
20    E
21    G
22    K
23    S
24    Z
25    A
26    A
27    B
28    Ç
29    K
30    K
31    M
32    P
33    S
34    S
35    Ş
36    T
37    Ü
38    Ü
dtype: object
```

**lambda() fonksiyonu** ile her satırın ilk üç karakterini yazdıralım.

```python
print(seri.apply(lambda x: x[:3]))
```

Çıktı:

```python
0     Arn
1     Bay
2     Beş
3     Bey
4     Ese
5     Eyü
6     Fat
7     Gaz
8     Kağ
9     Sar
10    Sul
11    Şiş
12    Avc
13    Bağ
14    Bah
15    Bak
16    Baş
17    Bey
18    Büy
19    Çat
20    Ese
21    Gün
22    Küç
23    Sil
24    Zey
25    Ada
26    Ata
27    Bey
28    Çek
29    Kad
30    Kar
31    Mal
32    Pen
33    San
34    Sul
35    Şil
36    Tuz
37    Ümr
38    Üsk
dtype: object
```

**String metotlarında**n biri olan `slice()`'ı kullanarak her satırın ilk üç karakterini yazdıralım.

```python
print(seri.str.slice(0,3))
```

çıktı:

```python
0     Arn
1     Bay
2     Beş
3     Bey
4     Ese
5     Eyü
6     Fat
7     Gaz
8     Kağ
9     Sar
10    Sul
11    Şiş
12    Avc
13    Bağ
14    Bah
15    Bak
16    Baş
17    Bey
18    Büy
19    Çat
20    Ese
21    Gün
22    Küç
23    Sil
24    Zey
25    Ada
26    Ata
27    Bey
28    Çek
29    Kad
30    Kar
31    Mal
32    Pen
33    San
34    Sul
35    Şil
36    Tuz
37    Ümr
38    Üsk
dtype: object
```
