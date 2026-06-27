Title: Pandas - join
Date: 2022-07-15 00:00
Modified: 2025-06-22 14:05
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Birleştir, join
Author: Mustafa Halil

# join() Fonksiyonu

`join()` metodu, Veri çerçevelerini birleştirmek için kullanılan fonksiyonlardan biridir. `join()` fonksiyonunun parametreleri kullanılarak, matematik dersinteki **Kümeler** konusu mantığında birleştirme işlemleri yapılabilir.  
**join()** metodu, parametresiz kullanıldığında varsayılan olarak **left join** (`how = "left"`)
 değerini alır. Sol tarafta yazılan veri çerçevesindeki tüm değerler alınır, bu çerçevedeki indeks değerleri sağ tarafta yazılan veri çerçevesinde varsa, bu değerlere birleştirilir. Soldaki indeks değeri sağdaki veri çerçeveside yoksa o halde ilgili satır ve sütunlara eksik veri mahiyetinde **NaN** (Not a Number) değeri atanır.

Örnek veri çerçevelerimizi oluşturarak konuyu inceleyelim.

```python
veri1 = {'A': ['A1','A2','A3','A4'],'B': ['B1','B2','B3','B4'],'C': ['C1','C2','C3','C4']}
veri2 = {'A': ['A5','A6','A7','A8'],'B': ['B5','B6','B7','B8'],'C': ['C5','C6','C7','C8']}
df1 = pd.DataFrame(veri1, index = [1,2,3,4])
df2 = pd.DataFrame(veri2, index = [5,6,7,8])
print(df1)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | A1  | B1  | C1  |
| 2   | A2  | B2  | C2  |
| 3   | A3  | B3  | C3  |
| 4   | A4  | B4  | C4  |

```python
print(df2)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 5   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 7   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |

```python
veri3 = {'A': ['A5','A6','A7','A8'],'B': ['B5','B6','B7','B8'],'C': ['C5','C6','C7','C8']}
df3 = pd.DataFrame(veri3, index = [1,6,3,8])
print(df3)
```

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | A5  | B5  | C5  |
| 6   | A6  | B6  | C6  |
| 3   | A7  | B7  | C7  |
| 8   | A8  | B8  | C8  |

```python
veri4 = {'Ad': ["mustafa", "halil", "emre", "burak"],
        'yas': [38,42,35,44],
        'meslek': ["yönetici", "mak.müh.", "yönetici", "akademisyen"]}
df4 = pd.DataFrame(veri4)
print(df4)
```

|     | Ad      | yas | meslek      |
| --- | ------- | --- | ----------- |
| 0   | mustafa | 38  | yönetici    |
| 1   | halil   | 42  | mak.müh.    |
| 2   | emre    | 35  | yönetici    |
| 3   | burak   | 44  | akademisyen |

**df1** ile **df4**'ü birleştirelim.

```python
print(df1.join(df4))
```

|     | A   | B   | C   | Ad    | yas  | meslek      |
| --- | --- | --- | --- | ----- | ---- | ----------- |
| 1   | A1  | B1  | C1  | halil | 42.0 | mak.müh.    |
| 2   | A2  | B2  | C2  | emre  | 35.0 | yönetici    |
| 3   | A3  | B3  | C3  | burak | 44.0 | akademisyen |
| 4   | A4  | B4  | C4  | NaN   | NaN  | NaN         |

Sonuca bakarsanız, **df1** veri çerçevesinin temel alındı ve **df4**'teki indeks değerlerine bakılarak, **df1**'in indeks değeri olan sütunlarının veri çerçevesine dahil edildiğini, 
katıldığını görebilirsiniz. Yani ilk veri çerçevesine ilave olarak, **iki veri çerçevesinin ortak indeksleri eklenmiş** diyebiliriz. İşlemin tersini yaparsak, yani df4'ü temel alarak **join** metodunu uygularsak ne olur?

```python
print(df4.join(df1))
```

|     | Ad      | yas | meslek      | A   | B   | C   |
| --- | ------- | --- | ----------- | --- | --- | --- |
| 0   | mustafa | 38  | yönetici    | NaN | NaN | NaN |
| 1   | halil   | 42  | mak.müh.    | A1  | B1  | C1  |
| 2   | emre    | 35  | yönetici    | A2  | B2  | C2  |
| 3   | burak   | 44  | akademisyen | A3  | B3  | C3  |

Bu kez de, tahmin ettiğimiz gibi, **df4** veri çerçevesi temel alındı, ve **df1**'in ortak indeks değerleri dahil edildi, **df4**'ün indeks değeri **df1** de olmadığı durumda, ilgili satıra **NaN** değeri atandı.

# Parametreler

## how parametresi

**join** metodunun **how** parametresi ile, veri çerçevelerinin, sağdaki ya da soldaki veri çerçevesine göre katılma/dahil edilme seçeneğini ayarlayabilir, veri çerçevelerinin 
birleşimini ya da kesişimini de alabiliriz. **how** parametresi, **left, right, inner** ve **outer** değerlerini alır. Varsayılan değer **left**'tir. (**left join**)

Aşağıdaki örneği inceleyerek konuyu daha iyi anlayabilirsiniz.

### how parametresinin seçenekleri

`join()` Fonksiyonunun `how` parametresinin alabileceği seçenekler;  

- `left` (varsayılan)
- `right`
- `outer`
- `inner`

Şimdi bu seçenekleri sıra ile inceleyelim.

![join_merge](../../images/python/pandas/join_merge.png)

### left join

`join()` metodunun, `how` parametresi almadan kullanıldığında varsayılan olarak **left join** (`how = "left"`) değerini aldığından bahsetmiştik. Bu durumda **Sol tarafta yazılan veri çerçevesindeki tüm değerler alınır, bu çerçevedeki indeks değerleri sağ tarafta yazılan veri çerçevesinde varsa, bu değerlere birleştirilir**. Soldaki indeks değeri sağdaki veri çerçeveside yoksa o halde ilgili satır ve sütunlara eksik veri mahiyetinde **NaN** (Not a Number) değeri atanır.  
`how = "left"` kodunu eklesek te eklemesekte aynı sonucu elde ederiz. Ağaşıdaki kodları ayrı ayrı çalıştırıp, göreabilirsiniz.

```python
print(df1.join(df4))
```

```python
print(df1.join(df4, how="left"))
```

|     | A   | B   | C   | Ad    | yas  | meslek      |
| --- | --- | --- | --- | ----- | ---- | ----------- |
| 1   | A1  | B1  | C1  | halil | 42.0 | mak.müh.    |
| 2   | A2  | B2  | C2  | emre  | 35.0 | yönetici    |
| 3   | A3  | B3  | C3  | burak | 44.0 | akademisyen |
| 4   | A4  | B4  | C4  | NaN   | NaN  | NaN         |

### right join

Aynı kodu, **how="right"** parametresi ekleyerek te çalıştırıp sonucu görelim.

```python
print(df1.join(df4, how="right"))
```

|     | A   | B   | C   | Ad      | yas | meslek      |
| --- | --- | --- | --- | ------- | --- | ----------- |
| 0   | NaN | NaN | NaN | mustafa | 38  | yönetici    |
| 1   | A1  | B1  | C1  | halil   | 42  | mak.müh.    |
| 2   | A2  | B2  | C2  | emre    | 35  | yönetici    |
| 3   | A3  | B3  | C3  | burak   | 44  | akademisyen |

**how** parametresi eklenmeyen İlk kodda, indeksler 1'den yani **df1** temel alınarak birleştirme işlemi gerçekleştirilirken, **how="right"** parametresi eklenen ikinci kodda **df2** yani sağdaki veri çerçevesi temel alınarak (indeks değerli 0'dan başlayarak) birleştirme işlemi gerçekleşti.

### inner join

`inner`seçeneği kullanıldığında, **Kesişim kümesi** mantığı ile birleştirme işlemi gerçekleşir. İki veri çerçevesinde ortak indeks değerlerine sahip satırlar alınır, yanyana birleştirilir.

**df1** 1'den 4'e kadar olan indeks değerlerine sahipken, **df4** 0'dan 3'e kadar indeks değerlerine sahip veri çerçeveleridir. Şimdi bu iki veri çerçevesini `how="inner"` parametresi ile birbirine dahil etmek istersen ne olur?

```python
print(df1.join(df4, how="inner"))
```

|     | A   | B   | C   | Ad    | yas | meslek      |
| --- | --- | --- | --- | ----- | --- | ----------- |
| 1   | A1  | B1  | C1  | halil | 42  | mak.müh.    |
| 2   | A2  | B2  | C2  | emre  | 35  | yönetici    |
| 3   | A3  | B3  | C3  | burak | 44  | akademisyen |

İkisinde de ortak olan 1,2 ve 3 nolu indeks değerlerindeki veriler birleştirildi yani her iki veri çerçevesinin **kesişimi** alındı.

### outer join

`outer`seçeneği kullanıldığında, **Birleşik küme** mantığı ile birleştirme işlemi gerçekleşir. Her iki veri çerçevesi tüm içeriği ile alınıp, yanyana birleştirilir.

```python
print(df1.join(df4, how="outer"))
```

|     | A   | B   | C   | Ad      | yas  | meslek      |
| --- | --- | --- | --- | ------- | ---- | ----------- |
| 0   | NaN | NaN | NaN | mustafa | 38.0 | yönetici    |
| 1   | A1  | B1  | C1  | halil   | 42.0 | mak.müh.    |
| 2   | A2  | B2  | C2  | emre    | 35.0 | yönetici    |
| 3   | A3  | B3  | C3  | burak   | 44.0 | akademisyen |
| 4   | A4  | B4  | C4  | NaN     | NaN  | NaN         |

Görüldüğü üzre, önce **df1** veri çerçevesi alındı, daha sonra **df4** veri çerçevesinin içeriği alınarak yanına dahil edildi. Her iki veri çerçevesinde indeks değerleri içermeyen satırlan **NaN** olarak belirlendi.

## sort parametresi

> sort parametresi bool türünde değer alır. Varsayılan değer False'tur  

Veri çerçevesi birleştirme anahtarıyla alfabetik (sözlüksel) olarak sıralanır. Değer **False** ise, birleştirme anahtarının sırası birleştirme türüne (`how` anahtar sözcüğü) bağlıdır.

```python
print(df4.join(df1, sort= True))
```

|     | Ad      | yas | meslek      | A   | B   | C   |
| --- | ------- | --- | ----------- | --- | --- | --- |
| 0   | mustafa | 38  | yönetici    | NaN | NaN | NaN |
| 1   | halil   | 42  | mak.müh.    | A1  | B1  | C1  |
| 2   | emre    | 35  | yönetici    | A2  | B2  | C2  |
| 3   | burak   | 44  | akademisyen | A3  | B3  | C3  |
