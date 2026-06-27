Title: Pandas - merge
Date: 2022-07-15 00:00
Modified: 2025-06-22 14:05
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Birleştir, merge
Author: Mustafa Halil

# merge() Fonksiyonu

`merge()` fonksiyonu `join()` fonksiyonuna benzer ancak bazı farklı özellikleri vardır. Veri Çerçevesi (DataFrame) veya adlandırılmış Seri nesnelerini (Series) veritabanı stili birleştirme yöntemi ile (SQL’de bulunan inner join, outer join … ‘e benzer) birleştirmek için `merge()` fonksiyonunu kullanılabilir.  
Adlandırılmış Seri nesnesi (Series), adlandırılmış tek bir sütuna sahip Veri çerçevesi (DataFrame) olarak ele alınır.  
`merge()` fonksiyonunun bir çok parametresi vardır. Biz burada temel bir kaç parametreye değineceğiz.

```python
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, 
            left_index=False, right_index=False, sort=False, 
            suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
```

# Parametreler

## on Parametresi

`on` parametresi, Veri Çerçevelerinin hangi sütun baz alınarak birleştirileceğini belirteceğimiz parametredir. Öğrenci isimleri ile Vize ve Final sonuçlarının bulunduğu iki veri çerçevesi oluşturup, parametrelerin kullanımını görelim.

```python
import pandas as pd
vize = pd.DataFrame({"Ogrenci": ["ali", "busra", "ceyhun", "eda", "gamze", "kamil"], 
                     "Sinav Sonucu": [41, 58, 73, 81, 95, 85]})

final = pd.DataFrame({"Ogrenci": ["ali", "busra", "derya", "fatih", "halil"], 
                      "Sinav Sonucu": [60, 68, 74, 90, 95]})
print(vize)
```

|     | Ogrenci | Sinav Sonucu |
| --- | ------- | ------------ |
| 0   | ali     | 41           |
| 1   | busra   | 58           |
| 2   | ceyhun  | 73           |
| 3   | eda     | 81           |
| 4   | gamze   | 95           |
| 5   | kamil   | 85           |

```python
print(final)
```

|     | Ogrenci | Sinav Sonucu |
| --- | ------- | ------------ |
| 0   | ali     | 60           |
| 1   | busra   | 68           |
| 2   | derya   | 74           |
| 3   | fatih   | 90           |
| 4   | halil   | 95           |

Yukarıdaki iki veri çerçevesini, **Ogrenci** isimli sütunu temel alarak birleştirlim. `how` parametresine şuan takılmayın, aşağıda detaylıca anlatılıyor.

```python
tumu = pd.merge(vize, final, on = "Ogrenci", how = "outer")
print(tumu)
```

|     | Ogrenci | Sinav Sonucu_x | Sinav Sonucu_y |
| --- | ------- | -------------- | -------------- |
| 0   | ali     | 41.0           | 60.0           |
| 1   | busra   | 58.0           | 68.0           |
| 2   | ceyhun  | 73.0           | NaN            |
| 3   | eda     | 81.0           | NaN            |
| 4   | gamze   | 95.0           | NaN            |
| 5   | kamil   | 85.0           | NaN            |
| 6   | derya   | NaN            | 74.0           |
| 7   | fatih   | NaN            | 90.0           |
| 8   | halil   | NaN            | 95.0           |

Birleştirme işlemi sonucunda, İki veri çerçevesindeki tüm veriler, yeni veri çerçevesinde birleştirildi. Hem Vize hemde Final veri çerçevelerinde isimleri bulunan öğrencilerin sınav sonuçları yeni veri çerçevesinde eklenmişken, vize ya da final sonucu olmayan öğrenciler için, ilgili sütun değerleri **NaN** (Not a Number) olarak ayarlandı.

## how Parametresi

`how` parametresi, veri çerçevelerini birleştirirken matematikteki Kümeler konusuna benzer seçenekler sunar. `merge()` fonksiyonunda `how` parametresi kullanılmadığı taktirde varsayılan olarak `inner` seçeneği belirtilmiş olur ve birleştirilecek veri çerçevelerinin sadece ortak değerleri alınarak (ortak küme gibi davranarak) birleştirme
 işlemi gerçekleştirilir.

Birleştirme işlemi sonucunda Sütun başlıklarının sonuna varsayılan **_x** ve **_y** sonekleri eklenir.

`how` Parametresi için kullanılabilecek seçenekler:

- `inner` (varsayılan)
- `outer`
- `left`
- `right`
- `cross`

### inner Seçeneği

`inner` seçeneği, sadece iki veri çerçevesinde de bulunan **ortak değerleri** birleştirir. Tek veri çerçevesinde olan değerler silinir. `how = "inner"` ibaresini yazsak ta yazmasak ta aynı sonucu elde ederiz. Aşağıdaki İki kod, aynı sonucu verir, deneyip görelim.

```python
print(pd.merge(vize, final, on = "Ogrenci", how = "inner"))
```

|     | Ogrenci | Sinav Sonucu_x | Sinav Sonucu_y |
| --- | ------- | -------------- | -------------- |
| 0   | ali     | 41             | 60             |
| 1   | busra   | 58             | 68             |

```python
print(pd.merge(vize, final, on = "Ogrenci"))
```

|     | Ogrenci | Sinav Sonucu_x | Sinav Sonucu_y |
| --- | ------- | -------------- | -------------- |
| 0   | ali     | 41             | 60             |
| 1   | busra   | 58             | 68             |

### outer Seçeneği

`outer` seçeneği kullanıldığında, iki veri çerçevesinde bulunan **tüm değerler** birleştirilir. Sol tarafta yazılan veri çerçevesindeki değerler temel alınır. İki veri çerçevesinde bulunan ortak değerler korunur, aksi durumda eksik değerler için **NaN** değeri atanır.

```python
print(pd.merge(vize, final, on = "Ogrenci", how = "outer"))
```

|     | Ogrenci | Sinav Sonucu_x | Sinav Sonucu_y |
| --- | ------- | -------------- | -------------- |
| 0   | ali     | 41.0           | 60.0           |
| 1   | busra   | 58.0           | 68.0           |
| 2   | ceyhun  | 73.0           | NaN            |
| 3   | eda     | 81.0           | NaN            |
| 4   | gamze   | 95.0           | NaN            |
| 5   | kamil   | 85.0           | NaN            |
| 6   | derya   | NaN            | 74.0           |
| 7   | fatih   | NaN            | 90.0           |
| 8   | halil   | NaN            | 95.0           |

### left Seçeneği

`left` seçeneği ile yapılan birleştirme işleminde, **sol tarafta yazılan veri çerçevesinin tüm değerlerini alır ve sağ tarafta yazılan veri çerçevesindeki ortak değerleri** tabloya ekler. Solda yazılan veri çerçevesindeki değerlerin, sağda yazılan veri çerçevesinde karşılığı yoksa, ilgili sütuna **NaN** değeri atanır. Sağ tarafta yazılan veri çerçevesinin, sol tarafta yazılan veri çerçevesinde karşılığı yoksa, bu değerler yok sayılır, 
birleştirme işlemine dahil edilmez.

```python
print(pd.merge(vize, final, on = "Ogrenci", how = "left"))
```

|     | Ogrenci | Sinav Sonucu_x | Sinav Sonucu_y |
| --- | ------- | -------------- | -------------- |
| 0   | ali     | 41             | 60.0           |
| 1   | busra   | 58             | 68.0           |
| 2   | ceyhun  | 73             | NaN            |
| 3   | eda     | 81             | NaN            |
| 4   | gamze   | 95             | NaN            |
| 5   | kamil   | 85             | NaN            |

### right Seçeneği

`right` seçeneği ile yapılan birleştirme işleminde, **sağ tarafta yazılan veri çerçevesinin tüm değerlerini alır ve sol tarafta yazılan veri çerçevesindeki ortak değerleri** tabloya ekler. Sağda yazılan veri çerçevesindeki değerlerin, solda yazılan veri çerçevesinde karşılığı yoksa, ilgili sütuna **NaN** değeri atanır. Sol tarafta yazılan veri çerçevesinin, sağ tarafta yazılan veri çerçevesinde karşılığı yoksa, bu değerler yok sayılır, 
birleştirme işlemine dahil edilmez.

```python
print(pd.merge(vize, final, on = "Ogrenci", how = "right"))
```

|     | Ogrenci | Sinav Sonucu_x | Sinav Sonucu_y |
| --- | ------- | -------------- | -------------- |
| 0   | ali     | 41.0           | 60             |
| 1   | busra   | 58.0           | 68             |
| 2   | derya   | NaN            | 74             |
| 3   | fatih   | NaN            | 90             |
| 4   | halil   | NaN            | 95             |

### cross Seçeneği

`cross` seçeneği sonucunda, kartezyen çarpımı yöntemi ile birleştirme yapılır.

```python
veri1 = pd.DataFrame({'HARF': ['A', 'B', "C"]})
veri2 = pd.DataFrame({'SAYI': [10,20,30]})
print(veri1)
```

|     | HARF |
| --- | ---- |
| 0   | A    |
| 1   | B    |
| 2   | C    |

```python
print(veri2)
```

|     | SAYI |
| --- | ---- |
| 0   | 10   |
| 1   | 20   |
| 2   | 30   |

```python
print(pd.merge(veri1, veri2, how="cross"))
```

|     | HARF | SAYI |
| --- | ---- | ---- |
| 0   | A    | 10   |
| 1   | A    | 20   |
| 2   | A    | 30   |
| 3   | B    | 10   |
| 4   | B    | 20   |
| 5   | B    | 30   |
| 6   | C    | 10   |
| 7   | C    | 20   |
| 8   | C    | 30   |

### left_on Parametresi

Bu parametre opsiyonel yani İsteğe bağlıdır, kullanmak zorunda değilsiniz. Soldaki Veri Çerçevesi üzerinde birleştirmenin hangi düzeyde yapılacağını belirtmek için kullanılır. Sütun başlıklarının sonuna varsayılan **_x** ve **_y** sonekleri eklenir.

`left_on` parametresi, etiket veya liste ya da dizi benzeri veri alır.

### right_on Parametresi

Bu parametre opsiyonel yani İsteğe bağlıdır, kullanmak zorunda değilsiniz. Sağdaki Veri Çerçevesi üzerinde birleştirmenin hangi düzeyde yapılacağını belirtmek için kullanılır. Sütun başlıklarının sonuna varsayılan **_x** ve **_y** sonekleri eklenir.

`right_on` parametresi, etiket veya liste ya da dizi benzeri veri alır.

```python
arastirma1 = pd.DataFrame({'Manav_1': ['elma', 'nar', 'portakal', 'elma'],
                    'fiyat': [1, 2, 3, 4]})

arastirma2 = pd.DataFrame({'Manav_2': ['elma', 'nar', 'portakal', 'elma'],
                    'fiyat': [5, 6, 7, 8]})
print(arastirma1)
```

|     | Manav_1  | fiyat |
| --- | -------- | ----- |
| 0   | elma     | 1     |
| 1   | nar      | 2     |
| 2   | portakal | 3     |
| 3   | elma     | 4     |

```python
print(arastirma2)
```

|     | Manav_2  | fiyat |
| --- | -------- | ----- |
| 0   | elma     | 5     |
| 1   | nar      | 6     |
| 2   | portakal | 7     |
| 3   | elma     | 8     |

```python
print(arastirma1.merge(arastirma2, left_on='Manav_1', right_on='Manav_2'))
```

|     | Manav_1  | fiyat_x | Manav_2  | fiyat_y |
| --- | -------- | ------- | -------- | ------- |
| 0   | elma     | 1       | elma     | 5       |
| 1   | elma     | 1       | elma     | 8       |
| 2   | elma     | 4       | elma     | 5       |
| 3   | elma     | 4       | elma     | 8       |
| 4   | nar      | 2       | nar      | 6       |
| 5   | portakal | 3       | portakal | 7       |

```python
print(arastirma2.merge(arastirma1, right_on='Manav_1', left_on='Manav_2'))
```

|     | Manav_2  | fiyat_x | Manav_1  | fiyat_y |
| --- | -------- | ------- | -------- | ------- |
| 0   | elma     | 5       | elma     | 1       |
| 1   | elma     | 5       | elma     | 4       |
| 2   | elma     | 8       | elma     | 1       |
| 3   | elma     | 8       | elma     | 4       |
| 4   | nar      | 6       | nar      | 2       |
| 5   | portakal | 7       | portakal | 3       |

### suffixes Parametresi

`merge()` fonksiyonu ile birleştirme işlemi sonucunda, sütun başlıklarının sonuna **_x** ve **_y** soneklerinin dahil edildiğini söyledik. Bu değer vaysayılan değerdir. 
Bu değeri değiştirmek ve sütun başlıklarının sonuna, istediğimiz değeri eklemek istersek bu işlemi `suffixes` parametresi ile yapabiliriz.

```python
print(arastirma1.merge(arastirma2, left_on='Manav_1', right_on='Manav_2',
            suffixes=("_bir", "_iki")))
```

|     | Manav_1  | fiyat_bir | Manav_2  | fiyat_iki |
| --- | -------- | --------- | -------- | --------- |
| 0   | elma     | 1         | elma     | 5         |
| 1   | elma     | 1         | elma     | 8         |
| 2   | elma     | 4         | elma     | 5         |
| 3   | elma     | 4         | elma     | 8         |
| 4   | nar      | 2         | nar      | 6         |
| 5   | portakal | 3         | portakal | 7         |
