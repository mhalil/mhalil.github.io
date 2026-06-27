Title: Pandas - is Operatötü
Date: 2022-07-15 00:00
Modified: 2025-06-26 17:25
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Veri, Sıralama, is, operatör
Author: Mustafa Halil

# is Operatorü

Karşılaştırma operatörlerinden biri olan `is` ile 

Veri Çerçevelerinin `index` değerleri , liste veri tipi olarak belirtildiği için, listeler arasında karşılaştırma operatörlerini kullanmak ta mümkündür.

İndeks değerleri ve Sütun isimleri **0, 1** ve **2** olan df_1 isimli veri çerçevesi oluşturup göz atalım.

```python
bir = [1,2,3], [40,50,60], [700,800,900]
sutun = [0,1,2]

df_1 = pd.DataFrame(bir, columns=sutun)
print(df_1)
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   | 1   | 2   | 3   |
| 1   | 40  | 50  | 60  |
| 2   | 700 | 800 | 900 |

İndeks değerleri ve Sütun isimleri **1, 2** ve **0** olan df_2 isimli veri çerçevesi oluşturup göz atalım.

```python
iki = ["a","b","c"], ["aa","bb","cc"], ["aaa","bbb","ccc"]
sutun = [1,2,0]

df_2 = pd.DataFrame(iki, index=sutun, columns=sutun)
print(df_2)
```

|     | 1   | 2   | 0   |
| --- | --- | --- | --- |
| 1   | a   | b   | c   |
| 2   | aa  | bb  | cc  |
| 0   | aaa | bbb | ccc |

**df_2** veri çerçevesinde index ve Sütun isimleri **1,2,0** olarak atanmış. **df_1** veri çerçevesinde index ve Sütun isimleri ise **0,1,2** olarak atanmış.

Örneğin `df_1.index` değerlerinin `df_2.index` değerlerine eşit olup olmadığını denetleyelim;

```python
print(df_1.index is sirala_filtrele.index)
```

Çıktı:

```python
False
```

Görüldüğü üzere, çıktı **False (Yanlış)** değerini döndürdü. Demek oluyor ki, df_1 ve df_2'nin indeks değerleri aynı değil.

**df_2**'nin indeks değerlerini (satır etiketini) `reindex()` fonksiyonu ile değiştirirken, yeni sıralamayı **df_1**'in indeks değerleri ile belirleyelim/eşleştirelim.

```python
print(df_2.reindex(df_1.index))
```

|     | 1   | 2   | 0   |
| --- | --- | --- | --- |
| 0   | aaa | bbb | ccc |
| 1   | a   | b   | c   |
| 2   | aa  | bb  | cc  |

**df_2**'nin Sütun isimlerini `reindex()` fonksiyonun `columns` parametresi ile değiştirirken, yeni sıralamayı **df_1**'in indeks değerleri ile belirleyelim/eşleştirelim.

```python
print(df_2.reindex(columns=df_1.index))
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 1   | c   | a   | b   |
| 2   | cc  | aa  | bb  |
| 0   | ccc | aaa | bbb |
