Title: Düzenli İfadeler - match
Date: 2023-09-01 00:00
Modified: 2025-11-01 14:00
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Match

# match() Fonksiyonu

Bir **karakter dizisinin başında** (örneğin bir paragraf başında) belirli bir kelimenin ya da kelime grubunun geçip geçmediğini öğrenmek istiyorsak bu işlemi `match()` metodunu kullanarak yapabiliriz.

**match()** metodunun;

* **ilk argümanı** eşleştirilecek (aranacak) değer, yani **desen**
* **ikinci argümanı** ise, **aramanın yapılacağı karakter dizisi** olmalıdır.

```python
import re

cumle = "python güçlü bir programlama dilidir."

re.match(r"python", cumle)
```

**Çıktı**:

```python
<re.Match object; span=(0, 6), match='python'>
```

Yukarıdaki `r"python"` deseni, yani aranan değer / desen, zaten bulunan değeri ile aynı olduğu için, bu arama/eşleşme yönteminin kullanımı size anlamsız/saçma gelmiş olabilir. 

İlerleyen bölümlerde **Metakarakterler** konusunu anlatılırken çok farklı desenler oluştururarak farklı sonuçlar bulacağız. O bölümde düzenli ifadelerin ne için kullanılabileceğini ve bizlere ne kadar kolaylık sağladığını anlayacaksınız. Aşağıda da metakarakter kullanımına örnek vereceğiz ancak detaylı anlatımı kendi sayfalarında inceleyeceğiz.

Düzenli ifadeler için bir desen tanımlarken, (esasen desen içinde `\` karakteri kullanıldığında) tırnak işaretlerinin öncesinde `r` ifadesini yazmamız istenir. İlerleyen bölümlerde göreceğimiz üzere, **özel metakarakterleri** desen içerisinde yazmamız gerektiğinde `r` ifadesini kullanmadığımızda sorun ile karşılaşırız. Özel metakarakterleri desen içerisinde yazmadığımız zaman da `r` ifadesini kullanmak sorun çıkarmıyor. Üstelik `r` ile tanımlanan ifade, bir değişken mi? yoksa bir düzenli ifade deseni mi? olduğu kodu inceleyenlere yardımcı oluyor.

`match` fonksiyonunu çalıştırdığımızda elde edilen sonuç ile, (nesnesinin dönen değeri ile) bazı işlemler yapılabilir. Bunun için nesnenin yöntemleri kullanılır. Bunlar;

* `span()` Eşleşen değerin başlangıç ve bitiş konumlarını **tuple** olarak verir.
* `string` Eşleşen (Dönen) metinsel dizgi ifadesinin (string)  tamamını yazdırır.
* `group()` Desenle eşleşen grupları yazdırır. (`group(1)`, `group(2)`, ...vb.) 

> **BİLGİ:** `group(0)` ifadesi ile `group()` ifadesi birbirine eşittir. Yani tüm eşleşmeleri yazdırır.

Yukarıdaki çıktıda bulunan **span** parametresi bize, aradığımız **python** karakter dizisinin (yani desenin), **cumle** değişkeninin **0.** ile **6.** karakterleri arasında yer aldığını söylüyor.

## span() metodu

Eşleşmenin **metin içerisinde başladığı ve sona erdiği karakterlerin sayısal değerini** verir (0 değeri 1. karakteri temsil eder):

```python
cumle = "python güçlü bir programlama dilidir."
x = re.match("python", cumle)
x.span()
```

**Çıktı**:

```python
(0, 6)
```

`match()` fonksiyonunun `span()` metodunu kullanarak değerleri doğrudan elde edebiliriz.

```python
cumle[0:6]
```

**Çıktı**:

```python
'python'
```

Farklı tarzda yazmak istersek, şu ifadeyi de kullanabiliriz;

```python
cumle[x.span()[0]:x.span()[1]]
```

**Çıktı**:

```python
'python'
```

Özel karakter kullanılarak arama yapılmak istenirse, aşağıdaki şekilde kod yazılabilir.

Örneğin **y** harfi ile başlayan kelimelerin metindeki konumlarını bulmak için aşağıdaki kodu kullanabiliriz.

```python
txt = "Bu sabah yağmur var İstanbul'da..."
a = re.search(r"\by\w+", txt)
print(a.span())        # **y** harfi ile başlayan kelimelerin konumlarını bul
```

**Çıktı**:

```python
(9, 15)
```

## group() Metodu

`group()` metodu, belirtilen **desen ile eşleşen değeri** döndürür. 

```python
cumle = "python güçlü bir programlama dilidir."
a = re.match("python", cumle)
print(a.group()) 
```

**Çıktı**:

```python
python
```

`x = re.match("python", cumle)` ifadesi ile eşleştirme komutunu bir değişkene (**x**'e) atamıştık. Hatırlarsanız bu fonksiyonu komut satırına yazdığımızda bir eşleşme nesnesi elde ediyorduk. İşte burada değişkene atadığımız şey aslında bu eşleşme nesnesinin kendisi oluyor. Bu durumu şu şekilde teyit edebilirsiniz:

```python
cumle = "python güçlü bir programlama dilidir."
x = re.match("python", cumle)
print(type(x))
```

**Çıktı**:

```python
re.Match
```

Gördüğünüz gibi **x** bir eşleştirme (match) nesnesidir.
**`group()` metodu, düzenli ifadelerin değil, eşleşme nesnelerinin bir metodudur.**

Bu metodu kullandığımızda direkt aranan değer ekrana yazdırılacaktır. Bu aşamada, metodun gereksiz ya da saçma olduğunu düşünüyor olabilirsiniz. [Eşleşme Nesnesi Metotları ve Gruplar]({filename}re_gruplar.md) sayfasında  `group()` metodunun ne işe yaradığını daha detaylı inceleyeceğiz.

```python
cumle = "python güçlü bir programlama dilidir."
x = re.match("python", cumle)
print(x.group())
```

**Çıktı**:

```python
'python'
```

`match()` metodu ile, **cumle** değişkeni içerisinde **Java** kelimesini arayıp, sonucu inceleyelim.

```python
cumle = "python güçlü bir programlama dilidir."
print(re.match("Java", cumle))
```

**Çıktı**:

```python
None
```

Python, **match()** metodu yardımıyla aradığımız şeyi eşleştirdiği (bulduğu) zaman bir eşleşme nesnesi (match object) döndürüyor. Eğer eşleşme yoksa, o zaman da **None** değerini döndürüyor.

```python
cumle = "python güçlü bir programlama dilidir."
print(re.match("güçlü", cumle))
```

**Çıktı**:

```python
None
```

**cumle** değişkeninde **güçlü** ifadesi geçtiği halde `match()` metodu bize bir eşleşme nesnesi döndürmedi. Peki ama neden?

Aslında bu gayet normal. Çünkü `match()` metodu bir karakter dizisinin sadece en başına bakar. 
Yani "**python güçlü bir programlama dilidir.**" ifadesini tutan **cumle** değişkenine `re.match(“güçlü”, cumle)` gibi bir fonksiyon uyguladığımızda, `match()` metodu **cumle** değişkeninin yalnızca en başına bakacak ve **cumle** değişkeninin en başında **güçlü** yerine **python** ifadesini gördüğü için, bize olumsuz yanıt verecektir.

Aslında `match()` metodunun yaptığı bu işi, karakter dizilerinin `split()` metodu yardımıyla da yapabiliriz. İncelemek isterseniz [Split Metodu]({filename}re_fonk_split.md)na ait sayfayı ziyaret edebilirsiniz.
