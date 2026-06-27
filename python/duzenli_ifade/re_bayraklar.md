Title: Düzenli İfadeler - bayraklar
Date: 2023-09-02 15:40
Modified: 2025-11-06 23:23
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Metakarakter, Bayraklar, Flags

# Bayraklar (Flags)

Buraya kadar öğrendiğimiz konularda, **re** modülünü kullanırken, eksiklik hissettiğiniz bazı durumlar ile karşılaşmış olabiliriz. Örneğin eşleşme yaparken **küçük-büyük harf duyarlılığı** ya da **çok satırlı bir metin içindeki eşleşmeleri arama** konuları bazen  eksik sonuç elde etmenize sebep olmuş olabilir. Bu bölümde bahsedeceğim bayrak (flag) konusu, bu tür sorunların üstesinden gelmenize yardımcı olacaktır. İlk bayrak ile başlayalım.

## re.IGNORECASE veya re.I

Bildiğiniz gibi, Python’da büyük-küçük harfler önemlidir. Yani eğer **python** kelimesini arıyorsanız, alacağınız çıktılar arasında **Python** olmayacaktır. Çünkü **python** ve **Python** birbirlerinden farklı iki karakter dizisidir. 

### Neden Kullanılır?

`re.IGNORECASE` özelliği, metin maddeleme, metin analizi veya kullanıcı girdileri gibi durumlarda, kullanıcıların büyük harf küçük harf karışımıyla yazdığı verilere karşı daha esnek olmak için kullanılır. Bu özellik, arama işlemleri sırasında harf büyüklüğünün ya da küçüklüğünün önemli olmadığı, gözardı edileceği durumlarda faydalıdır.

Bir kullanıcı tarafından sağlanan veriyle çalışırken veya çok dilli metinlerle uğraşırken `re.IGNORECASE` özelliği, arama işlemlerini daha geniş bir kapsama yaymak ve daha fazla esneklik sağlamak için kullanışlı bir araçtır.

`re.IGNORECASE` veya kısaca `re.I` adlı bayrak, bize **büyük-küçük harfe dikkat etmeden (büyük harf ve küçük harf arasındaki farkı önemsemeden) arama / eşleme yapma** imkanı sağlar. Hemen bir örnek verelim: 

```python
metin = """Programlama dili, programcının bir bilgisayara ne yapmasını
istediğini anlatmasının standartlaştırılmış bir yoludur. Programlama
dilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,
verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin
yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla
programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,
C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama
dilleridir."""

# `re.compile()` ile kullanım örneği
derli = re.compile("programlama", re.IGNORECASE)
print(derli.findall(metin))
```

**Çıktı**:

```python
['Programlama', 'Programlama', 'programlama', 'programlama']
```

Gördüğünüz gibi, metinde geçen hem **programlama** kelimesini hem de **Programlama** kelimesini ayıklayabildik. Bunu yapmamızı sağlayan şey de `re.IGNORECASE` adlı bayrak (flag) oldu. 

Eğer bu seçeneği kullanmasaydık, çıktıda yalnızca **programlama** kelimesini görürdük. Çünkü aradığımız şey aslında **programlama** kelimesi idi. Biz istersek `re.IGNORECASE` yerine kısaca `re.I` ifadesini de kullanabiliriz. Aynı anlama gelecektir.

```python
# Düzenli ifade içinde kullanım
result = re.match(r'python', 'Python is powerful!', re.IGNORECASE)
print(result.group())
```

**Çıktı**:

```python
Python
```

Bir örnek daha verelim.

```python
metin = """Programlama dili, programcının bir bilgisayara ne yapmasını
istediğini anlatmasının standartlaştırılmış bir yoludur. Programlama
dilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,
verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin
yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla
programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,
C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama
dilleridir."""

derli = re.compile(r"\sp\w+", re.IGNORECASE)
print(derli.findall(metin)
```

**Çıktı**:

```python
[' programcının', ' Programlama', ' programcının', '\nprogramlama', ' Pascal', ' Perl', ' Python', ' programlama']
```

Çıktıya bakınca, boşluk `\s` ve `p` harfi (hem küçük hem büyük) ile başlayan tüm kelimelerin eşleştiğini görüyoruz.

Bayraklar, `flags` etiketi ile de kullanılabilir;

```python
derli = re.compile("programlama", flags=re.IGNORECASE)
print(derli.findall(metin))
```

## re.MULTILINE veya re.M

`re.MULTILINE` bayrağı (flag), bir düzenli ifadenin **çok satırlı** bir metin içindeki eşleşmeleri nasıl ele aldığını kontrol etmek için kullanılır. Bu bayrak, bir metin içindeki **her bir satırı ayrı ayrı ele alarak** düzenli ifadenin davranışını etkiler. Özellikle, `^` (başlangıç) ve `$` (bitiş) meta karakterlerinin metnin başı ve sonu yerine her satırın başı ve sonuyla eşleşmesini sağlar.

### Neden Kullanılır?

`re.MULTILINE` bayrağı, çok satırlı metinlerle çalışırken ve her bir satırın başı veya sonu ile eşleşme yapmak istediğinizde kullanılır. Özellikle, metni satırlara bölüp her bir satıra ayrı ayrı düzenli ifadeler uygulamak istediğiniz durumlar için uygundur.

Bu özellik, metin maddeleme, metin analizi veya log dosyaları gibi çok satırlı metinlerle çalışırken kullanışlıdır. `re.MULTILINE` sayesinde, düzenli ifadelerle satırları tek tek ele alabilir ve her bir satır için eşleşmeleri bulabilirsiniz.

### Kullanımı

`re.MULTILINE` bayrağı, `re.compile()` fonksiyonu ile birlikte veya bir düzenli ifade string'i içinde kullanılabilir. İşte kullanım örnekleri:

```python
import re

metin = """Programlama dili, programcının bir bilgisayara ne yapmasını
istediğini anlatmasının standartlaştırılmış bir yoludur. Programlama
dilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,
verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin
yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla
programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,
C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama
dilleridir."""

# `re.compile()` ile kullanım
desen = re.compile(r'^\w+', re.MULTILINE)

sonuc = desen.findall(metin)
print(sonuc)
```

**Çıktı**:

```python
['Programlama', 'istediğini', 'dilleri', 'verinin', 'yapılacağını', 'programlama', 'C', 'dilleridir']
```

Kod, her bir satırın ilk kelimesini döndürdü.

```python
# Düzenli ifade içinde kullanım
sonuc = re.findall(r'^\w+', metin, re.MULTILINE)
print(sonuc)
```

**Çıktı**:

```python
['Programlama', 'istediğini', 'dilleri', 'verinin', 'yapılacağını', 'programlama', 'C', 'dilleridir']
```

Yukarıdaki kod ile aynı sonucu elde ettik.

## re.DOTALL veya re.S

Bildiğiniz gibi, metakarakterler arasında yer alan `.` sembolü herhangi bir karakterin yerini tutuyordu. Bu metakarakter bütün karakterlerin yerini tutmak üzere kullanılabilir. Hatırlarsanız, `.` metakarakterini anlatırken, **bu metakarakterin, yeni satır karakterinin yerini tutmayacağını** söylemiştik.  `re.DOTALL` veya `re.S` **bayrağı**, bir düzenli ifadenin `.` karakterinin metin içinde **yeni satır karakterleriyle de eşleşmesini sağlar**. Bunu bir örnek yardımıyla görelim. Diyelim ki elimizde şöyle bir karakter dizisi var:

```python
metin = """Ben Python,
Monty Python\nNam-ı diğer Süper Python"""
print(metin)
```

    Ben Python,
    Monty Python
    Nam-ı diğer Süper Python

Bu karakter dizisi içinde **Python** kelimesini temel alarak bir arama yapmak istiyorsak eğer, kullanacağımız şu kod istediğimiz şeyi yeterince yerine getiremeyecektir:

```python
derle = re.compile("Python.*")
nesne = derle.search(metin)

if nesne:
    print(nesne.group())
```

    Python,

Bunun sebebi, `.` metakarakterinin `\n` (yeni satır) kaçış dizisini dikkate almamasıdır. Bu yüzden **bu kaçış dizisinin ötesine geçip orada arama yapmıyor**. Ama şimdi biz ona bu yeteneği de kazandıracağız:

```python
# `re.compile()` ile kullanım
derle = re.compile("Python.*", re.DOTALL)
nesne = derle.search(metin)

if nesne:
    print(nesne.group())
```

```python
Python,
Monty Python
Nam-ı diğer Süper Python
```

`re.DOTALL` seçeneğini `re.S` şeklinde de kısaltabilirsiniz / kullanabilirsiniz.

```python
import re

metin = """This is a multiline
text with new lines.
"""

# Düzenli ifade içinde kullanım
sonuc = re.match(r'.+', metin, re.S)
print(sonuc.group())  
```

```
This is a multiline
text with new lines.
```

## re.UNICODE veya re.U

`re.UNICODE`, bayrağı (flag), bir düzenli ifadenin **Unicode karakter setini kullanmasını sağlar**. Varsayılan durumda, bazı düzenli ifade karakter sınıfları, yalnızca **ASCII** karakter setini anlar. Ancak, `re.UNICODE` özelliği ile Unicode karakterler de dikkate alınır. Özellikle, çok dilli uygulamalarda veya farklı dil ve alfabeleri içeren metinlerle uğraşırken kullanışlıdır. Bu özellik sayesinde, Unicode karakterler, düzenli ifadelerde doğru şekilde ele alınır ve beklenen eşleşmeleri sağlar.

### Kullanımı

`re.UNICODE` bayrağı, `re.compile()` fonksiyonu ile birlikte veya bir düzenli ifade string'i içinde kullanılabilir. İşte kullanım örnekleri:

```python
import re

# `re.compile()` ile kullanım
pattern = re.compile(r'\w+', re.U)
text = "Yüksek Yapılı Dağlar Çok Haşmetlidir"

result = pattern.findall(text)
print(result)    

# ÇIKTI: ['Yüksek', 'Yapılı', 'Dağlar', 'Çok', 'Haşmetlidir']

# Düzenli ifade içinde kullanım
result = re.findall(r'\w+', text, re.UNICODE)
print(result)  

# ÇIKTI : ['Yüksek', 'Yapılı', 'Dağlar', 'Çok', 'Haşmetlidir']
```

Bu örnekte, `re.UNICODE` bayrağı kullanılarak `\w+` düzenli ifadesi Unicode karakterlerle kelime karakterlerini eşleştirmektedir.

## re.VERBOSE veya re.X

Bu bayrak, desenin mantıksal bölümlerini görsel olarak ayırmanıza ve yorumlar eklemenize olanak tanıyarak daha güzel ve okunabilir düzenli ifadeler yazmanıza olanak tanır. Desen içindeki boşluklar, karakter sınıfında olmadıkları sürece, kaçış karakteri olmayan ters eğik çizgi ile başlamadıkları sürece veya *?, (?: veya (?P<...> gibi belirteçler içinde olmadıkları sürece yok sayılır. Örneğin, (? : ve * ? kullanılamaz. Bir satırda karakter sınıfında olmayan ve öncesinde kaçış karakteri olmayan bir # işareti varsa, en soldaki bu # işaretinden satırın sonuna kadar tüm karakterler yok sayılır.

Bu, ondalık sayıyla eşleşen aşağıdaki iki düzenli ifade nesnesinin işlevsel olarak eşit olduğu anlamına gelir:

```python
b = re.compile(r"\d+\.\d*")
```

Bu ifade aşağıdaki şekilde daha okunaklı yazılabilir.

```python
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
```

Bir başka örnek;

```python
import re

metin = """
Ali: 234,789 TL
Hasan: 345,980 TL
Mahmut: 12,000,000 TL
Semih: 1,655,000 TL
Merve: 345,765,120 TL
"""

desen = r"\b\d{1,3}(,\d{3})*\b"

eslesmeler = re.finditer(desen, metin, flags=re.VERBOSE)

for eslesme in eslesmeler:
    print(eslesme.group())
```

**Çıktı**:

```python
234,789
345,980
12,000,000
1,655,000
345,765,120
```

Normal şartlarda yukarıdaki deseni, daha okunaklı olması için aşağıdaki şekilde yazarsak sorun yaşarız. Çok satırlı desenler kabul edilmez.

```python
desen = r"""
    \b             # kelimenin basinda olsun
    \d{1,3}     # ilk üç rakam
    (,\d{3})*
    \b             # kelimenin sonunda olsun
    """
```

Yukarıdaki desen gayet okunaklı. Deseni bu şekilde kullanabilmek için  `flags=re.VERBOSE` ya da `flags=re.X` bayrağını kullanmak gerekir. Aşağıdaki kodu inceleyebilirsiniz.

```python
import re
metin = """
Ali: 234,789 TL
Hasan: 345,980 TL
Mahmut: 12,000,000 TL
Semih: 1,655,000 TL
Merve: 345,765,120 TL
"""

desen = r"""
    \b             # kelimenin basinda olsun
    \d{1,3}     # ilk üç rakam
    (,\d{3})*
    \b             # kelimenin sonunda olsun
    """

eslesmeler = re.finditer(desen, metin, flags=re.VERBOSE)

for eslesme in eslesmeler:
    print(eslesme.group())
```

**Çıktı**:

```python
234,789
345,980
12,000,000
1,655,000
345,765,120
```

## Bayrakların Birlikte Kullanımı

Bayraklar konusunda anlatılacak bir konu da birden fazla bayrağın aynı desen ile birlikte kullanımı. Örneğin hem **çok satırlı** tarama hem de **büyük-küçük harf duyarlıksız**  eşleşme yapılmak istenirse `re.M` (`re.MULTILINE`) ve `re.I` (`re.IGNORECASE`)  bayraklarını **birlikte** kullanmak gerekir. Bu iki bayrağı birlikte kullanmak için yapılması gereken `|` (pipe) işaretini kullanmaktır.

```python
import re

metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
bir dil denebilir. Ancak Python'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı
olması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi
haline gelmiştir. Ayrıca Google'ın da Python'a özel bir önem ve değer verdiğini, çok iyi derecede Python bilenlere
iş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın yaratıcısı Guido Van Rossum 
Google'de işe başladı...
Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında 
yayınlandı. 2008'de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan 
kodların Python 3.x'te çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, 
dilin son sürümü olan Python 2.7.x Serisi versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi. 
Python 2.x geliştirilme desteğinin sona ermesinin ardından, Python dilinin 3.7.x ve sonraki sürümlerinin 
geliştirilmesi devam etmektedir."""

desen = re.compile(r"^g\w+", flags = re.M | re.I)
sonuc = desen.findall(metin)

print("Sonuc :", sonuc)
```

**Çıktı**:

```python
Sonuc : ['Guido', 'Google', 'geliştirilmesi']
```

`r"^g\w+", flags = re.M | re.I)` deseni, her bir satırın başında, büyük-küçük harfe bakmaksızın **g** harfi ile başlayan kelimeleri aradık ve bulduk.
