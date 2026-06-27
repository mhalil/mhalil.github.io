Title: Düzenli İfadeler - search
Date: 2023-09-01 00:00
Modified: 2025-11-01 14:08
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Search

# search() Fonksiyonu

`search()` metodu ile `match()` metodu arasında çok önemli bir fark vardır. `match()` metodu bir karakter dizisinin (örneğin bir paragrafta) en başına bakıp bir **eşleştirme** işlemi yaparken, `search()` metodu karakter dizisinin genelinde bir **arama** işlemi yapar. Yani biri eşleştirir, öbürü arar.

`search()` metodu, **eşleşmenin gerçekleştiği ilk değeri döndürür**. Aranan değer ya da desen, karakter dizisi içerisinde birden fazla geçse bile, ilk eşleşmede işlem sonlanır.

Örneğin, **güçlü** ifadesini `search()` metodu yardımı ile, **cumle** değişkeni içerisinde **arayalım**.

```python
cumle = "python güçlü bir programlama dilidir."
re.search("güçlü", cumle)
```

```python
<re.Match object; span=(7, 12), match='güçlü'>
```

Gördüğünüz gibi, `search()` metodu **güçlü** kelimesini buldu. Çünkü `search()` metodu, `match()` metodunun aksine, bir karakter dizisinin sadece baş tarafına bakmakla yetinmiyor, karakter dizisinin geneli üzerinde bir arama işlemi gerçekleştiriyor.

Tıpkı `match()` metodunda olduğu gibi, `search()` metodunda da `span()` ve `group()` metotlarından faydalanarak bulunan şeyin hangi aralıkta olduğunu (konumunu) ve bu şeyin ne olduğunu görüntüleyebiliriz:

```python
kardiz = "Python güçlü bir dildir"
nesne = re.search("güçlü", kardiz)
print(nesne.span())
```

**Çıktı**:

```
(7, 12)
```

Eşleşen sonucu görelim:

```python
nesne.group()
```

**Çıktı**:

```
'güçlü'
```

## Start() Medodu

Arama deseni ile eşleşen ifadenin, karakter dizisinin kaçıncı karakterinde **başladığını** görmek için `start()` metodunu kullanabiliriz ;

```python
nesne.start()
```

**Çıktı**:

```
7
```

## End() Medodu

Arama deseni ile eşleşen ifadenin, karakter dizisinin kaçıncı karakterinde **bittiğini** görmek için `end()` metodunu kullanabiliriz ;

```python
nesne.end()
```

**Çıktı**:

```
12
```

Şimdiye kadar hep karakter dizileri üzerinde çalıştık. İsterseniz biraz da listeler üzerinde örnekler verelim.

Şöyle bir listemiz olsun:

```python
liste = ["elma", "armut", "kebap"]
re.search("kebap", liste)
```

```python
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

/tmp/ipykernel_3704/1944706800.py in <module>
      1 liste = ["elma", "armut", "kebap"]
----> 2 re.search("kebap", liste)


/usr/lib/python3.10/re.py in search(pattern, string, flags)
    198     """Scan through string looking for a match to the pattern, returning
    199     a Match object, or None if no match was found."""
--> 200     return _compile(pattern, flags).search(string)
    201 
    202 def sub(pattern, repl, string, count=0, flags=0):


TypeError: expected string or bytes-like object
```

Ne oldu? Hata aldınız, değil mi? Bu normal. Çünkü düzenli ifadeler karakter dizileri üzerinde işler. 
Bunlar doğrudan listeler üzerinde işlem yapamaz. O yüzden bizim Python’a biraz yardımcı olmamız gerekiyor:

```python
liste = ["elma", "armut", "kebap"]
for i in liste:
    nesne = re.search("kebap", i)
    if nesne:
        print(nesne.group())
```

**Çıktı**:

```
kebap
```
