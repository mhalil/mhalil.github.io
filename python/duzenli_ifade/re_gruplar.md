Title: Düzenli İfadeler - Gruplar
Date: 2023-12-30 15:06
Modified: 2025-11-08 22:42
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, group, grup, metot

# Gruplama ve Etikeleme

## group() metodu

Bu bölümde doğrudan düzenli ifadelerin değil, ama düzenli ifadeler kullanılarak üretilen eşleşme nesnelerinin bir metodu olan `group()` metodundan bahsedeceğiz. 

Düzenli ifadelerde parantez içine alınan bölümler grup olarak adlandırılır. `group()` metodu, bir eşleşme nesnesi üzerinde çağrıldığında, bu **eşleşmenin içindeki belirli bir grupla eşleşen alt dizeyi döndürür**.  `group()` **metodu**, **bir** `re.Match` **nesnesinin belirli bir grup içindeki eşleşmeyi almak için kullanılır.** `re.findall()` **metodu**, `re.Match` **nesnelerini döndürmez; bu nedenle** `group()` **metodu** `re.findall()` **ile doğrudan kullanılamaz.** Düzenli ifade  içinde parantezle gruplandırılmış alt ifadeler, gruplar oluşturur ve bu gruplara, eşleşen metni belirli bir düzenleme tabi tutarak erişebiliriz. Esasında biz bu metodu önceki bölümlerde de kullanmıştık. Ama burada bu metoda biraz daha ayrıntılı olarak bakacağız.

Daha önceki bölümlerden hatırlayacağınız gibi, bu metot düzenli ifadeleri kullanarak eşleştirdiğimiz karakter dizilerini görme imkanı sağlıyordu. Bu bölümde bu metodu `( )` metakarakteri yardımıyla daha verimli bir şekilde kullanacağız.  İsterseniz ilk olarak şöyle basit bir örnek verelim:

```python
kardiz = "python bir programlama dilidir"
nesne = re.search("(python) (bir) (programlama) (dilidir)", kardiz)

print(nesne.group())
```

    python bir programlama dilidir

Burada düzenli ifade kalıbımızı nasıl grupladığımıza dikkat edin. `print(nesne.group())` komutunu verdiğimizde eşleşen karakter dizileri ekrana döküldü. Şimdi bu grupladığımız bölümlere tek tek erişelim:

```python
nesne.group(0)
```

    'python bir programlama dilidir'

Gördüğünüz gibi, “0” indeksi eşleşen karakter dizisinin tamamını veriyor. Gerisinin nasıl olacağını tahmin edebilirsiniz:

```python
print(nesne.group(1))
print(nesne.group(2))
print(nesne.group(3))
print(nesne.group(4))
```

    python
    bir
    programlama
    dilidir

Düzenli ifadelerde parantez içine alınan bölümler grup olarak adlandırıldığını ifade etmiştik. Örneğin, `(\d+)-(\d+)` deseni, iki sayıyı tire ile ayıran bir grup içerir. Bir eşleşme gerçekleştiğinde, bu gruplara erişmek için `group()` metodu kullanılır.

İşte bir örnek:

```python
import re

text = "2023-02-14"
pattern = re.compile(r'(\d+)-(\d+)-(\d+)')

match = pattern.match(text)

# Tam eşleşen metni alır
full_match = match.group()
print(full_match)  # 2023-02-14

# Grupları alır
group1 = match.group(1)
group2 = match.group(2)
group3 = match.group(3)

print(group1)  # 2023
print(group2)  # 02
print(group3)  # 14
```

Bu örnekte, `(\d+)-(\d+)-(\d+)` deseni ile `2023-02-14` metni eşleştirilir. `group()` metodu, tam eşleşen metni (`2023-02-14`) veya belirli grupları (grup 1, grup 2, grup 3) almak için kullanılır.

Eğer eşleşme gerçekleşmemişse veya belirli bir grup mevcut değilse, `group()` metodu `None` değerini döndürür. Bu nedenle, kullanmadan önce eşleşmenin gerçekleşip gerçekleşmediğini kontrol etmek önemlidir.

```python
if match:
    print(match.group(1))
else:
    print("Eşleşme bulunamadı.")
```

Bu kontrol, eşleşme gerçekleşip gerçekleşmediğini kontrol etmede yardımcı olacaktır.

`group()` metoduna ait benzer bir örnek [**( ) Parantez** ]({filename}re_metakarakterler.md)metakarakter başlığı altında ilgili sayfada detaylı anlatıldı.

Gruplama ile alakalı güzel bir özellik daha göstermek istiyorum. Bu, aynı ifadenin peş peşe (arka arkaya) kullanıldığı durumu tespit etmek için oldukça faydalıdır.

```python
metin = "Seni her gördüğümde gözlerim ışıl ışıl parlıyor, koşa koşa yanına gelmek istiyorum."

desen = r"(\w+\s)\1"
ara = re.findall(desen, metin)


print(ara)
```

**Çıktı**:

```python
['ışıl ', 'koşa ']
```

**metin** değişkeni içindeki cümlede peş peşe tekrar eden kelimelerin **ışıl** ve **koşa** olduğunu kolayca tespit etmiş olduk.

Görüldüğü gibi `(\w+\s)\1` deseninde önce parantez kullanılarak bir grup oluşturuldu. Ardından aynı desenin tekrar kullanılmasını temsil etmek için `\1` ifadesi kullanıldı. Biliyoruz ki parantez kulanılarak gruplama yapıldığında `.group(1)` gibi bir ifade kullanarak ilk eşleşmeyi elde edebiliyorduk. Bu mantığı kullanarak desen içinde bir gruptan bahsetmek istediğimizde `\` ifadesinden sonra kaçıncı gruptan bahsetmek istediğimize dair ilgili sayı değerini kullanmalıyız. 

Bir başka örnek daha yapalım. Bu kez farklı biçimde gösterilen tarih bilgilerini aynı biçime çevirelim.

```python
import re

metin = "Bugün 02.11.2025. 10 gün önceki tarih 23-10-2025 idi."

desen = r"\b(\d{2})[.-](\d{2})[.-](\d{4})\b"
siralama = r"\3/\2/\1"

yeni_metin = re.sub(desen, siralama, metin)

print(yeni_metin)
```

**Çıktı**:

```python
Bugün 2025/11/02. 10 gün önceki tarih 2025/10/23 idi.
```

Gördüğünüz gibi, gün ay ve yıl biçimindeki tarih bilgilerini, yıl, ay ve gün farmatına dönüştürmüş olduk. Bunu, gruplama sırasını ters (`r"\3/\2/\1"`) yazarak sağladık.

## groups() metodu

Bu metot, bize kullanabileceğimiz bütün grupları bir *demet* halinde sunar:

```python
import re
kardiz = "python bir programlama dilidir"
nesne = re.search("(python) (bir) (programlama) (dilidir)", kardiz)

print(nesne.groups())
```

    ('python', 'bir', 'programlama', 'dilidir')

Başka bir örnek;

```python
import re

metin = """
Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
bir dil denebilir. Ancak Python'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı
olması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi
haline gelmiştir. Ayrıca Google'ın da Python'a özel bir önem ve değer verdiğini, çok iyi derecede Python bilenlere
iş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın yaratıcısı Guido Van Rossum 
Google'de işe başladı..."""

bul = re.search(r"([0-9]+)\s+([a-z]+)", metin)

print(bul.groups())
```

**Çıktı**:

```python
('1990', 'y')
```

# Grupları Etiketleme

Gruplama, bu desenler içindeki alt örüntüleri belirlemek ve bu gruplara etiketler eklemek için kullanışlı bir özelliktir. Bu bölüme kadar yaptığımız örneklerde, düzenli ifadeler ile desen oluşturup, oluşturduğumuz gruplara **.group(1), .group(2)**, ...vb şekilde eriştik.  Yani sürekli aşağıdaki şekilde örnekler verdik;

## Gruplama ve Parantez Kullanımı

Gruplama, bir desen içinde belirli bir alt örüntüyü tanımlamak ve bu örüntüyü daha sonra referans almak için kullanılır. Gruplama için parantez `()` kullanılır. Örneğin:

```python
import re
text = "John Doe, Jane Smith"
pattern = re.compile(r'(\w+) (\w+)')

match = pattern.match(text)

if match:
    print("Tam eşleşme:", match.group())
    print("Ad:", match.group(1))
    print("Soyad:", match.group(2))
```

Bu örnekte, `(\w+) (\w+)` deseni içindeki her iki kelimeyi gruplamak için parantez kullanılmıştır. `match.group(1)` ifadesi, desen içindeki ilk parantez içindeki örüntüye eşleşen kısmı döndürür.

```python
Tam eşleşme: John Doe
Ad: John
Soyad: Doe
```

## (?P<...> ile Etiketleme ile Gruplama

Desen içinde gruplama yaparken, gruplara etiket eklemek, grupları daha anlamlı hale getirmek ve daha sonra bu etiketleri kullanmak için faydalıdır. Etiketleme, `?P<etiket>` sözdizimi ile yapılır. `P` harfi `Placeholder`'ın (Yer Tutucu'nun) kısalmasıdır. 

Biliyoruz ki, `?` metakarakteri, **kendisinden önce gelen karakterin SIFIR veya BİR defa** eşleştiği durumlarda kullanılırdı. **Bunun istisnası, `?` karakterinden önce `(` işaretinin gelmesidir.**

Örneğin:

```python
import re
text = "John Doe, Jane Smith"
pattern = re.compile(r'(?P<ad>\w+) (?P<soyad>\w+)')

match = pattern.match(text)

if match:
    print("Tam eşleşme:", match.group())
    print("Ad:", match.group('ad'))
    print("Soyad:", match.group('soyad'))
```

Bu örnekte, `(?P<ad>\w+) (?P<soyad>\w+)` deseni içindeki her iki kelimeyi etiketleme kullanılarak gruplamıştır. `match.group('ad')` ve `match.group('soyad')` ifadeleri, etiketleme sayesinde gruplara erişimi sağlar.

```
Tam eşleşme: John Doe
Ad: John
Soyad: Doe
```

Etiketleme, özellikle karmaşık desenler içinde belirli alt örüntülerin anlamını artırmak ve kodun daha okunabilir olmasını sağlamak için kullanışlıdır.

Bir örnek daha yapalım;

```python
import re
text = """
1234567890
533-456-7891
544 456 7892
(216) 456-7893
"""

pattern = re.compile(r"\(?(\d{3})\)?[ \-]?(\d{3})[ |-]?(\d{4})")
matches = pattern.findall(text)

for match in matches:
    operator, üçhane, dorthane = match
    print(f"Operator: {operator}, Üçhane: {üçhane}, Dorthane: {dorthane}")
```

Çıktı;

```python
Operator: 123, Üçhane: 456, Dorthane: 7890
Operator: 533, Üçhane: 456, Dorthane: 7891
Operator: 544, Üçhane: 456, Dorthane: 7892
Operator: 216, Üçhane: 456, Dorthane: 7893
```

Sadece Operatör numaralarını öğrenmek istersek;

```python
import re
text = """
1234567890
533-456-7891
544 456 7892
(216) 456-7893
"""

pattern = re.compile(r"\(?(\d{3})\)?[ \-]?(\d{3})[ |-]?(\d{4})")
matches = pattern.findall(text)

for match in matches:
    operator, üçhane, dorthane = match
    print(f"Operator: {operator}")
```

Çıktı;

```python
Operator: 123
Operator: 533
Operator: 544
Operator: 216
```

Son Örnek tarihle alakalı olsun;

```python
import re

tarihler = """
30/04/2023
01-03-2021
02.22.2019
11.01.17
"""

pattern = re.compile(r"(?P<gun>\d{2})([\/\-\.])(?P<ay>\d{2})([\/\-\.])(?P<yil>\d{2,4})")
matches = pattern.findall(tarihler)

for match in matches:
    gun, _, ay, _, yil = match
    print(f"Gun: {gun}, Ay: {ay}, Yil: {yil}")
```

Çıktı;

```python
Gun: 30, Ay: 04, Yil: 2023
Gun: 01, Ay: 03, Yil: 2021
Gun: 02, Ay: 22, Yil: 2019
Gun: 11, Ay: 01, Yil: 17
```

## Lookahead (İleriye bak)

**Lookahead**, düzenli ifadelerde kullanılan bir özelliktir ve **bir eşleşmeyi sınırlamak veya filtrelemek için kullanılır**. Lookahead, bir düzenli ifade içinde belirli bir deseni kontrol etmek ve ardından bir eşleşme oluşturmak için kullanılır, ancak bu kontrolün sonucu eşleşme sonucuna dahil edilmez. Lookahead için `?` işareti, ile başlayan düzenli ifadeler kullanılır.

Lookahead iki türde gelir: **pozitif lookahead** ve **negatif lookahead**.

### (?= ...) Pozitif Lookahead

**Bir eşleşme sadece belirli bir desenin arkasında varsa** gerçekleşir. Ancak, bu desen eşleşmenin sonucuna dahil edilmez.

Örneğin:

```python
import re

text = "elma portakal muz çilek"
pattern = re.compile(r'\w+(?=\sportakal)')

result = pattern.findall(text)
print(result)
```

```python
['elma']
```

Bu örnekte, `\w+(?=\sportakal)` deseni, boşluk karakteri (`\s`) ile ayrılmış olarak "**portakal**" kelimesinden önce gelen kelimeyi eşleştirir.

Bir başka örneğe bakalım;

```python
import re
metin = "quantity and qrcode is really useful"
desen = r"q(?=u)[a-zA-Z0-9]+"
print(re.findall(desen, metin))
```

```python
['quantity']
```

Bu desenin açıklaması, **q** ile başlayıp **u** ile devam eden kelime grubunu seç demektir.

Yine aynı metinden yola çıkarak **u** ile devam eden karakterleri, bir başka ifadeyle, **u** harfinden önceki karakteri **seç** demek istersek;

```python
import re
metin = "quantity and qrcode is really useful"
desen = r".(?=u)"
print(re.findall(desen, metin))
```

bu bize **q** , **boşluk** ve **f** karakterlerini seçecektir.

```python
['q', ' ', 'f']
```

Bir örnek daha yapalım;

"**The fat cat ran down the street.**" ifadesinden **at** ile **devam eden karakterleri** seç demek istersek;

```python
import re
metin = "The fat cat ran down the street."
desen = r".(?=at)"
print(re.findall(desen, metin))
```

Çıktı:

```python
['f', 'c']
```

`r".(?=at)"` ifadesi bize **f** ve **c** karakterlerini döndürür. Çünkü cümle içerisinde **at** ile devam eden sadece **fat** ve **cat** kelimeleri vardır.

### (?! ...) Negatif Lookahead

**Bir eşleşme, belirli bir desenin arkasında yoksa** gerçekleşir. Yani **belirlediğimiz desen ile devam etmeyen ifadeleri seç**er. Tarif biraz karışık geldiyse bir de şöyle açıklamaya çalışayım; **Belirlediğimiz desene uyan karakter ya da karakter grubunu filtrele, gizle, gösterme** demek istiyoruz.

Örneğin:

```python
import re

text = "apple orange banana"
pattern = re.compile(r'\w+(?!\sorange)')

result = pattern.findall(text)
print(result)
```

```python
['appl', 'orange', 'banana']
```

Bu örnekte, `\w+(?!\sorange)` deseni, boşluk karakteri (`\s`) ile ayrılmış olarak "**orange**" kelimesinden önce gelmeyen kelimeyi eşleştirir.  Çıktıdaki`appl` kelimesinde `e`harfinin **olmadığına** dikkat edin.

Bir diğer örnek;

"quantity and qrcode is really useful" metninde, **q** ile başlayıp **u** ile devam etmeyen bir ifadeyi seçmek istersek;

```python
import re
metin = "quantity and qrcode is really useful"
desen = r"q(?!u)[a-zA-Z0-9]+"
print(re.findall(desen, metin))
```

Burada **q** ile başlayıp **u** ile devam etmeyen kelime grubunu seçer. [a-zA-Z0-9] ile herhangi bir karakteri gidebildiği karar seçmesini sagladik bu bize **qrcode** kelimesini geri döndürecektir.

```python
['qrcode']
```

Eğer bu ifadeyi **u** yerine **r** ile değiştirirsek yani **q** ile başlayıp **r** ile devam **etmeyen** kelime grubunu seç dersek bu durumda **quantity** seçilecektir;

```python
import re
metin = "quantity and qrcode is really useful"
desen = r"q(?!r)[a-zA-Z0-9]+"
print(re.findall(desen, metin))
```

```python
['quantity']
```

Lookahead, daha karmaşık eşleşme şartlarını ifade etmek ve belirli durumları kontrol etmek için kullanışlıdır. Ancak, düzenli ifadelerin anlaşılması ve kullanılması bazen karmaşık olabilir, bu nedenle dikkatlice kullanılmalıdır.

## Look Behind (geriye bak)

Öncesinde belirlediğimiz karakter ya da karakter gruplarıyla **devam eden** ya da **devam etmeyen** ifadeleri seçmemizi sağlar. **Lookbehind**’ lar bir ifadeden önce başka bir ifade olup olmadığını kontrol etmek için kullanılır. Lookbehind için `?<` işareti ile başlayan düzenli ifadeler kullanılır.

`Lookbehind` (geriye bak) düzenli ifade özelliği, bir eşleşmenin gerçekleşebilmesi için önceki bir desenin arkasında belirli bir desenin bulunmasını kontrol etmeye yarar. `Lookbehind` özelliği, bir eşleşmenin önceki bir deseni içermesi gerektiğinde kullanılır ancak bu deseni eşleşmenin bir parçası olarak almaz.

`Lookbehind` iki türdedir: **pozitif lookbehind** `(?<=...)` ve **negatif lookbehind** `(?<!...)`.

### (?<=...) Pozitif Lookbehind

Bir eşleşme, **belirli bir desenin önceki bir desenin arkasında varsa** gerçekleşir. Yani **eşleşmesi istenilen karakterlerin öncesine** bakılır.

Örneğin:

```python
text = "apple orange banana"
pattern = re.compile(r'(?<=\s).?')

result = pattern.findall(text)
print(result)
```

Bu örnekte, `(?<=\s).?` deseni, öncesinde boşluk karakteri (`\s`) olan karakter(ler)i  eşleştirir.

```python
['o', 'b']
```

Bir başka örneğe bakalım;

"**quantity and qrcode is really unuseful but this is an unethical**" cümlesinde **un** ile başlayan (öncesinde **un** deseni olan) karakterleri seçelim.

```python
import re
metin = "quantity and qrcode is really unuseful but this is an unethical"
desen = r"(?<=un)."
print(re.findall(desen, metin))
```

eşleşme sadece un**u**seful ve un**e**thical kelimelerde gerçekleşecek ve **u** ile **e** karakterlerini verecektir. Çünkü öncesinde **un** karakterleri bulunmaktadır.

```python
['u', 'e']
```

Farklı bir örnek;

"**quantity and qrcode is really unuseful but this is an unethical. The punisher was born in early age. Also the man is really old**" cümlesinde eşleştirmek/bulmak istediğimiz kelimeler **punisher** ve **man** kelimeleri olsaydı. Bunu şu şekilde tespit edebilirdik. İki kelimenin de ortak özelliği öncesinde "**The, the**" ifadelerinin olmasıdır. Yani öncesinde "**The**"" veya "**the**" kelimeleri olan elde etmeliyiz;

```python
import re
metin = "quantity and qrcode is really unuseful but this is an unethical. The punisher was born in early age. Also the man is really old"
desen = r"(?<=[tT]he )[a-zA-Z]+"
print(re.findall(desen, metin))
```

İstediğimizi elde etmek için `(?<=[tT]he )[a-zA-Z]+` ifadesi bizim için yeterli olacaktır. Çünkü **The** ya da **the** bizim seçmek istediğimiz iki farklı kelime olduğu için burada **T** veya **t** opsiyonel olmalıdır. Bu ifade bize şunu **punisher** ve **man** kelimelerini verecektir.

```python
['punisher', 'man']
```

### (?<!...) Negatif Lookbehind

**Pozitif lookbehind**'ın tam tersidir. **Belirtilen ifade ile başlamayan** ifadeleri kontrol etmek için kullanılır.  Yani **öncesinde şu desen olmayan ifadeleri döndür** demek istediğimizde kullanıyoruz.`(?<!ifade)` şeklinde kullanılır. 

Örneğin; **a** harfinden önce **b** harfi **olmayan** bütün ifadeleri yakala demek için `(?<!b)a` ifadesi kullanılır.

Örnek:

```python
import re
text = "banana"
pattern = re.compile(r"(?<!a).?")

result = pattern.findall(text)
print(result)
```

```python
['b', 'a', 'a', 'a']
```

Bu örnekte, `r"(?<!a).?"` deseninde, `(?<!a)` ifadesi ile öncesinde `a` karakteri **olmayan** `.?` karakterleri bulmak istediğimizi ifade etmek istiyoruz.

Bir diğer örneğe bakalım;

```python
import re
text = "pie, apple, orange juice, pie cake, banana split"
pattern = re.compile(r'(?<!\s)pie')

result = pattern.findall(text)
print(result)
```

```python
['pie']
```

Bu örnekte, `(?<!\s)pie` deseni, boşluk karakteri (`\s`) ile ayrılmamış olarak "**pie**" kelimesini eşleştirir. Yani, eğer "**pie**" kelimesi bir boşluk karakteri ile başlamıyorsa, bu kelimeyi eşleştirir. `pie` kelimesi burada `orange juice` içindeki `pie` kelimesine eşleşir, çünkü onun önünde bir boşluk karakteri yok.

Bir örnek daha;

```python
metin = "Pythonscript is fun. Javascript is awesome."
desen = r"(?<!Python)script.+"

eslesme = re.search(desen, metin)
print(eslesme.group())
```

**Çıktı**:

```textile
script is awesome.
```

`Lookbehind` özelliği, belirli bir desenin önceki bir deseni kontrol etmek için kullanılır ve eşleşmenin gerçekleşmesini sınırlar. Ancak, Python'da kullanılan bazı diğer programlama dillerinde olduğu gibi, `Lookbehind` özelliği tamamen genişletilmiş (fixed-width) desenlere izin vermez; yani, lookbehind deseni bir değişken uzunluktaysa hata alabilirsiniz.

# Sonuç

Böylelikle düzenli ifadeler konusunu bitirmiş olduk. Buradaki amacımız, size düzenli ifadeler konusunda genel bir bakış sunabilmekti. Bu yazıları okuduktan sonra kafanızda düzenli ifadelerle ilgili kabataslak da olsa bir resim oluştuysa bu yazılar amacına ulaşmış demektir. Elbette düzenli ifadeler burada anlattıklarımızdan ibaret değildir. Bu konunun üzerine eğildiğinizde aslında düzenli ifadelerin dipsiz bir kuyu gibi olduğunu göreceksiniz.

Esasında en başta da dediğimiz gibi, düzenli ifadeler apayrı bir dil gibidir. Doğrusu şu ki, düzenli ifadeler başlı başına bağımsız bir sistemdir. Hemen hemen bütün programlama dilleri öyle ya da böyle düzenli ifadeleri destekler. Python’da düzenli ifadeleri bünyesine adapte etmiş dillerden biridir. Bizim düzenli ifadeler konusundaki yaklaşımımız, her zaman bunları **“gerektiğinde”** kullanmak olmalıdır. Dediğimiz gibi, eğer yapmak istediğiniz bir işlemi karakter dizilerinin metotları yardımıyla yapabiliyorsanız düzenli ifadelere girişmemek en iyisidir. Çünkü karakter dizisi metotları hem daha hızlıdır hem de anlaması daha kolaydır.
