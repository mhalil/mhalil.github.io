Title: Düzenli İfadeler - split
Date: 2023-09-01 00:00
Modified: 2025-11-01 14:00
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Split

# split() Fonksiyonu

`split()` metodu, veriyi, eşleşmelerin olduğu noktalardan itibaren böler ve liste haline getirir. Örneğin aşağıdaki kod çalıştırılırsa cümle boşluk (`\s`) karakterlerinden bölünür (yani kelimelere ayrılır):

```python
metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
bir dil denebilir. Ancak Python'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı
olması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi
haline gelmiştir. Ayrıca Google'ın da Python'a özel bir önem ve değer verdiğini, çok iyi derecede Python bilenlere
iş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın yaratıcısı Guido Van Rossum 
Google'de işe başladı..."""

desen = r"Python"
bol = re.split(desen, metin)

print(bol)
```

**Çıktı**:

```
['Guido Van Rossum ', "'ı geliştirmeye 1990 yılında başlamış... Yani aslında ", ' için nispeten yeni\nbir dil denebilir. Ancak ', "'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı\nolması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi\nhaline gelmiştir. Ayrıca Google'ın da ", "'a özel bir önem ve değer verdiğini, çok iyi derecede ", ' bilenlere\niş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce ', "'ın yaratıcısı Guido Van Rossum \nGoogle'de işe başladı..."]
```

Gördüğünüz gibi, metin, **Python** ibaresi gördüğün yerden itibaren parçalara ayrılarak liste oluşturdu. **Python** ibaresi listeye dahil **edilmedi.**

```python
cumle = "python güçlü bir programlama dilidir."
x = re.split("\s", cumle)
print(x)
```

**Çıktı**:

```
['python', 'güçlü', 'bir', 'programlama', 'dilidir.']
```

Bölme sonrası kelime doğrulamak için de aşağıdaki kodlar kullanılabilir. İlk Kelime **python** mu? diye sorgulayalım.

```python
cumle.split()[0] == "python"
```

**Çıktı**:

```
True
```

**String** metotlarından biri olan `startswith` kullanılarak ta ilk kelimenin **python** olup olmadığı şu şekilde de sorgulanabilir.

Eğer düzenli ifadelerden tek beklentiniz bir karakter dizisinin en başındaki veriyle eşleştirme işlemi yapmaksa, `split()` veya `startswith()` metotlarını kullanmak daha mantıklıdır. Çünkü `split()` ve `startswith()` metotları `match()` metodundan çok daha hızlı çalışacaktır.

```python
cumle.startswith("python")
```

**Çıktı**:

```
True
```

İlk Kelime **güçlü** mü? diye sorgulayalım.

```python
cumle.split()[0] == "güçlü"
```

**Çıktı**:

```
False
```

`split()` fonksiyonunun bölümleme sayısını **(maxsplit)** fonksiyonun 3. parametresinde belirtilebilir. 

Aşağıdaki örnekte veri en çok 2 boşluk kadar (3 parça) bölünecektir:

```python
cumle = "python güçlü bir programlama dilidir."
x = re.split("\s", cumle, 2)
print(x)
```

**Çıktı**:

```
['python', 'güçlü', 'bir programlama dilidir.']
```


