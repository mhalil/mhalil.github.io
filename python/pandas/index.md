Title: Pandas - index
Date: 2022-07-10 20:40
Modified: 2025-11-29 17:45
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, describe, Fonksiyon, index
Author: Mustafa Halil

# `index` Metodu

**index** metodu, Veri Çerçevesinin indeks bilgisini döndürür.

Öncelikle **Pandas** Kütüphanesini içe aktarıp, kodlama esnasında hızlı olması adına bu kütüphaneye **pd** adını atayalım;

```python
import pandas as pd
```

Basit bir Veri Çerçevesi (Data Frame) oluşturalım ve oluşturduğumuz Veri Çerçevesinin içeriğini görelim;

```python
sozluk = {"isim" : ["Mustafa", "Halil", "Burak", "Emre", "Ersin", "Sertaç", "Furkan","Murat","Ahmet","Abdülkadir"], 
                    "yaş" : [25, 38, 41, 23, 37, 52, 30, 23, 40, 38],
                    "iş-meslek" : ["mühendis", "programcı", "akademisyen","yönetici","amir","mühendis","yönetici","müdür","veteriner","yönetici"]}

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

## `index` Metodunun Kullanımı

**index** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.index)
```

Çıktı:

```python
RangeIndex(start=0, stop=10, step=1)
```

Veri çerçevesi oluşturulurken indeks değerlerinin otomatik olarak belirlenmesi halinde, yukarıdaki şekilde çıktı alırız. Çıktıyı incelersek;

- **start=0** : İlk indeks değerinin 0 olduğu,
- **stop=10** : son indeks değerinin 10 olduğu,
- **step=1** : indeks değerlerinin 1'er 1'er arttığını belirtmektedir.

Veri çerçevesi oluşturulduğunda index değerleri otomatik olarak belirlenir. Bu değeri istersek biz de belirleyebiliriz.

```python
veri.index = range(50, 70, 2)
print(veri)
```

`veri.index = range(50, 70, 2)` ile veri çerçevemizdeki index değerlerini 50'den başlatıp 70'e kadar (70 dahil değil) 2'şer 2'şer artırarak yeniden tanımlıyoruz. Veri çerçevesinde toplamda 10 satır olduğu için yeni atayacağımız indeks sayısı da 10 adet olmalı, aksi halde hata alırız, işlem gerçekleşmez.

**Çıktı**:

```python
          isim  yaş    iş-meslek
50     Mustafa   25     mühendis
52       Halil   38    programcı
54       Burak   41  akademisyen
56        Emre   23     yönetici
58       Ersin   37         amir
60      Sertaç   52     mühendis
62      Furkan   30     yönetici
64       Murat   23        müdür
66       Ahmet   40    veteriner
68  Abdülkadir   38     yönetici
```

Peki indeks değeri sayılardan oluşmazsa, yani indeks bilgisi tarafımızca belirtilen Metinsel verilerden oluşursa **index** fonksiyonu nasıl çıktı verir?.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", index_col="Film_Adı")
print(imdb.head())
```

| Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| ------------------------ | ---- | ---- | ------------ |
| The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| The Godfather            | 1972 | 9,2  | 751381       |
| The Godfather: Part II   | 1974 | 9    | 488889       |
| Pulp Fiction             | 1994 | 8,9  | 830504       |
| The Dark Knight          | 2008 | 8,9  | 1045186      |

```python
print(imdb.index)
```

```python
Index(['The Shawshank Redemption ', 'The Godfather ',
       'The Godfather: Part II ', 'Pulp Fiction', 'The Dark Knight ',
       '12 Angry Men ', 'Schindler's List ',
       'The Lord of the Rings: The Return of the King ', 'Fight Club ',
       'Star Wars: Episode V - The Empire Strikes Back ',
       ...
       'The Artist ', 'Nausicaä of the Valley of the Wind ',
       'Beauty and the Beast ', 'Three Colors: Red ', 'Bringing Up Baby ',
       'Mystic River ', 'In the Heat of the Night ', 'Arsenic and Old Lace ',
       'Before Sunrise ', 'Papillon '],
      dtype='object', name='Film_Adı', length=247)
```

Gördüğünüz gibi, **indeks** bilgisi Metinsel veriler olduğunda, **index** fonksiyonunun çıktısı yukarıda şekilde alınıyor. Çıktıyı incelersek;

- **Index(['The Shawshank Redemption ', 'The Godfather ', 'The Godfather: Part II ', ...]** : İndeks bilgileri liste halinde verilir,
- **type='object'** : İndeks bilgilerinin "Object" yani "Metinsel (String)" veri olduğu,
- **name='Film_Adı'** : İndex adının (başlığının) "Film_Adı" olduğu,
- **length=247** : toplam 247 adet indeks verisi (satır) olduğu ifade etmektedir.

## `name` Parametresi

`name` parametresi, index'in ismini döndürür. Örneğin yukarıdaki Veri çerçevesinin `index` değerinin başığını öğrenmek içi aşağıdaki kodu kullanabiliriz;

```python
print(imdb.index.name)     # index'in ismini (başlığını) döndürür.
```

**Çıktı**:

```python
Film_Adı
```

### `name` Parametresi ile index ve/veya başlığı değiştirmek;

* `df.index = df["sütun adı"]` ile **index başlığı** ve **index değerlerini** değiştirebiliriz;

Elimizde **imdb** isimli aşağıda gösterildiği gibi bir veri çerçevesi olduğunu düşünelim.

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| 1   | The Godfather            | 1972 | 9,2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9    | 488889       |
| 3   | Pulp Fiction             | 1994 | 8,9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8,9  | 1045186      |

**Film_Adı** isimli sütunu, index verisi olarak kullanmak istersek aşağıdaki kodu kullanabiliriz;

```python
imdb.index = imdb["Film_Adı"]
```

Çıktı:

| Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| ------------------------ | ---- | ---- | ------------ |
| The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| The Godfather            | 1972 | 9,2  | 751381       |
| The Godfather: Part II   | 1974 | 9    | 488889       |
| Pulp Fiction             | 1994 | 8,9  | 830504       |
| The Dark Knight          | 2008 | 8,9  | 1045186      |

* Veri çerçevemizin **Index başlığını bir değerle değiştirmek** istediğimiz zaman `name` parametresini aşağıdaki şekilde kullanabiliriz.

```python
imdb.index.name = "Movie Name"
```

**Çıktı:**

| Movie Name               | Yıl  | Puan | Oylayan_Kişi |
| ------------------------ | ---- | ---- | ------------ |
| The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| The Godfather            | 1972 | 9,2  | 751381       |
| The Godfather: Part II   | 1974 | 9    | 488889       |
| Pulp Fiction             | 1994 | 8,9  | 830504       |
| The Dark Knight          | 2008 | 8,9  | 1045186      |
