Title: Düzenli İfadeler - findall
Date: 2023-09-01 00:00
Modified: 2025-11-02 12:15
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Findall

# findall() Fonksiyonu

Bir metin içinde geçen belirli desenlerin tümünü bulmak istiyorsak `findall()` metodunu kullanmalıyız. Bu metot bize bir **liste veri türünde çıktı verir**. Bulunan ya da desen ile eşleşen tüm sonuçlar liste veri tipine eklenmiş olarak çıktı verilir.

```python
metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
bir dil denebilir. Ancak Python'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı
olması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi
haline gelmiştir. Ayrıca Google'ın da Python'a özel bir önem ve değer verdiğini, çok iyi derecede Python bilenlere
iş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın yaratıcısı Guido Van Rossum 
Google'de işe başladı..."""
```

Yukarıdaki **metin** değişkeni içinde geçen bütün **Python** kelimelerini bulmak istersek aşağıdaki kodu çalıştırmalıyız;

```python
print(re.findall("Python", metin))
```

    ['Python', 'Python', 'Python', 'Python', 'Python', 'Python']

Gördüğünüz gibi, metinde geçen bütün “Python” kelimelerini bir çırpıda liste olarak aldık. Tabi bu örnekte kaç adet "Python"" ifadesi olduğunu tespit etmiş olduk. Bunu düzenli ifedaleri kullanmadan da bulabiliriz, neden düzenli ifadeyi kullanayım diye düşünebilirsiniz. 

Konuyu biraz derinleştirip "meta karakterleri" kullanarak (ilerleyen bölümlerde detaylı anlatılıyor) düzenli ifadelerin bize ne kadar esneklik sağladığını görelim.

Diyelim ki, **metin** değişkeninin içinde, **P** harfi ile başlayan tüm kelimeleri `findall() `fonksiyonu yardımıyla bulalım.

```python
print(re.findall(r"P\w+", metin))    # P harfi ile başlayan kelimeleri bul
```

**Çıktı**:

```python
['Python', 'Python', 'Python', 'Python', 'Python', 'Python']
```

Görüldüğü gibi metin içerisinde büyük P harfi ile başlayan sadece Python kelimeleri varmış.

Peki hem küçük hem de büyük P ile başlayan kelimeleri bulmak istersek hangi kodu kullanmalıyız derseniz;

```python
print(re.findall(r"[Pp]\w+", metin))
```

**Çıktı**:

```python
['Python', 'Python', 'peten', 'Python', 'programa', 'pek', 'Python', 'Python', 'Python']
```

Metin içinde sadece büyük harflerle başlayan kelimeleri bulalım;

```python
print(re.findall(r"[A-Z]\w+", metin))
```

**Çıktı**:

```python
['Guido', 'Van', 'Rossum', 'Python', 'Yani', 'Python', 'Ancak', 'Python', 'Ayrıca', 'Google', 'Python', 'Python', 'Mesela', 'Python', 'Guido', 'Van', 'Rossum', 'Google']
```

Metin içindeki sayıları bulalım;

```python
print(re.findall(r"\d+", metin))
```

**Çıktı**:

```python
['1990']
```

Daha fazla örnek vermek mümkün ancak sanıyorum Düzenli ifadelerin gücü ve faydasını anlatmak için bu örnekler yeterli.
