Title: Pandas - columns
Date: 2022-07-10 20:40
Modified: 2025-06-21 14:10
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, columns, Fonksiyon
Author: Mustafa Halil

# columns Fonksiyonu

**columns** fonksiyonu, oluşturulan ya da içe aktarılan Veri Çerçevelerinin **başlık satırını** çıktı olarak verir. **columns** fonksiyonunu kullanırken sonunda <u>parantez işaretleri kullanmadığımıza</u> dikkat edin.

Veri çerçevesine filtreleme işlemi uygulamak istediğimiz zaman, bu fonksiyon çok işimize yarar. Sütun isimlerini hızlı bir şekilde görüntülüyerek filtrelemek ya da seçmek istediğimiz sütun başlıklarını doğru bir şekilde görüntülüyerek (istersek) kopyalayabiliriz.

Öncelikle **Pandas** Kütüphanesini içe aktarıp, kodlama esnasında hızlı olması adına bu kütüphaneye **pd** adını atayalım;

```python
import pandas as pd
```

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

# columns Fonksiyonunun Kullanımı

**columns** fonksiyonu aşağıdaki şekilde kullanılır.

```python
print(veri.columns)
```

Çıktı:

```python
Index(['isim', 'yaş', 'iş-meslek'], dtype='object')
```

Sütun isimlerini değiştirmek istediğimiz zaman da `columns` fonksiyonundan yararlanabiliriz. İstersek harfleri küçük/büyük harfe dönüştürebilir istersek de değiştirebiliriz. Örnek uygulamalar yapalım.

Başlıkları büyük harfe çevirmek için aşağıdaki kodu uygulayabiliriz.

```python
veri.columns = veri.columns.str.upper()
```

`print(veri)` çıktısı:

|     | ISIM       | YAŞ | IŞ-MESLEK   |
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

İşlem sonrası sadece `columns` fonksiyonunun çıktısını inceleyelim.

```python
print(veri.columns)
```

```python
Index(['ISIM', 'YAŞ', 'IŞ-MESLEK'], dtype='object')
```

Şimdi de başlık isimlerini farklı kelimelerle değiştirelim.

```python
veri.columns = ["name", "age", "occupation"]
print(veri)
```

|     | name       | age | occupation  |
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
