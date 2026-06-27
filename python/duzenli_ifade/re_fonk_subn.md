Title: Düzenli İfadeler - subn
Date: 2023-09-01 00:00
Modified: 2025-11-02 13:25
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Subn

# 

# subn() Fonksiyonu

Bu metodu çok kısa bir şekilde anlatıp geçeceğiz. Çünkü bu metot `sub()` metoduyla neredeyse tamamen aynıdır. Tek farkı, `subn()` metodunun bir metin içinde yapılan değişiklik sayısını da göstermesidir. Yani bu metodu kullanarak, kullanıcılarınıza **“toplam şu kadar sayıda değişiklik yapılmıştır”** şeklinde bir bilgi verebilirsiniz. Bu metot çıktı olarak iki öğeli bir demet verir. 

**Birinci öğe değiştirilen metin, ikinci öğe ise yapılan değişiklik sayısıdır**. Yani kullanıcıya değişiklik sayısını göstermek için yapmanız gereken şey, bu demetin ikinci öğesini almaktır. 

```python
import re

txt = "Yaz Yaz Yaz Bir Kenara Yaz"
say = re.subn("Yaz", "Çiz", txt)
print(say)
```

**Çıktı**:

```python
('Çiz Çiz Çiz Bir Kenara Çiz', 4)
```

Sadece** kaç adet değişiklik yapıldığını** görmek istersek kodu şu şekilde kullanabiliriz;

```python
import re

txt = "Yaz Yaz Yaz Bir Kenara Yaz"
say = re.subn("Yaz", "Çiz", txt)
print(say[1])
```

**Çıktı**:

```python
4
```

`sub()` metodunu anlatırken verdiğimiz örnekteki kodların son satırını aşağıdaki gibi değiştirerek metinde toplam kaç adet değişiklik yaptığımızı görebiliriz.

```python
import re

metin = """Karadeniz Ereğlisi denince akla ilk olarak kömür ve demir-çelik
gelir. Kokusu ve tadıyla dünyaya nam salmış meşhur Osmanlı çileği ise ismini
verdiği festival günleri dışında pek hatırlanmaz. Oysa Çin'den Arnavutköy'e
oradan da Ereğli'ye getirilen kralların meyvesi çilek, burada geçirdiği değişim
sonucu tadına doyulmaz bir hal alır. Ereğli'nin havasından mı suyundan mı
bilinmez, kokusu, tadı bambaşka bir hale dönüşür ve meşhur Osmanlı çileği
unvanını hak eder. Bu nazik ve aromalı çilekten yapılan reçel de likör de bir
başka olur. Bu yıl dokuzuncusu düzenlenen Uluslararası Osmanlı Çileği Kültür
Festivali'nde 36 üretici arasında yetiştirdiği çileklerle birinci olan Kocaali
Köyü'nden Güner Özdemir, yılda bir ton ürün alıyor. 60 yaşındaki Özdemir,
çileklerinin sırrını yoğun ilgiye ve içten duyduğu sevgiye bağlıyor: "Erkekler
bahçemize giremez. Koca ayaklarıyla ezerler çileklerimizi" Çileği toplamanın zor
olduğunu söyleyen Ayşe Özhan da çocukluğundan bu yana çilek bahçesinde
çalışıyor. Her sabah 04.00'te kalkan Özhan, çileklerini özenle suluyor. Kasım
başında ektiği çilek fideleri haziran başında meyve veriyor."""


derle = re.compile("çile[kğ]", re.IGNORECASE)

def degistir(nesne):
    a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
    b = nesne.group().split()
    for i in b:
        return a[i]

degisiklik = derle.subn(degistir, metin)
print("Toplam {} değişiklik yapılmıştır.".format(degisiklik[1]))
```

    Toplam 12 değişiklik yapılmıştır.
