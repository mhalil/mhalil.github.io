Title: Düzenli İfadeler - sub
Date: 2023-09-01 00:00
Modified: 2025-11-02 13:15
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Sub

# sub() Fonksiyonu

Şimdiye kadar hep düzenli ifadeler yoluyla bir karakter dizisini nasıl eşleştireceğimizi inceledik. Ama tabii ki düzenli ifadeler yalnızca bir karakter dizisi **bulmak**la ilgili değildir. Bu araç aynı zamanda bir karakter dizisini **değiştirmeyi** de kapsar. Bu iş için temel olarak iki metot kullanılır. Bunlardan ilki `sub()` metodudur. **Substitute** kelimesi, "yerine koy", "değiştir" anlamına gelir. Bu metot, pek çok uygulamadan bildiğimiz **Bul ve Değiştir** fonksiyonudur aslında. Bu bölümde `sub()` metodunu inceleyeceğiz.

## Metin/Karakter Dizisi Değiştirme İşlemleri

`sub()` metodunun;

- ilk argümanı, değiştirilecek değeri,
- ikinci argümanı, yerine konulacak değeri,
- üçüncü argümanı, hangi yapı/ dizgi/ paragraf içinde değişimin yapılacağını,
- dördüncü argümanı, kaç eşleşmede değişiklik yapılacağını,

tanımlar.

Aşağıdaki örnekte **kavun** kelimesini bulacak ve **karpuz** ile değiştirecektir:

```python
txt = "Bugün kavun yedim."
x = re.sub("kavun", "karpuz", txt)
print(x)
```

**Çıktı**:

```
Bugün karpuz yedim.
```

Yukarıdaki açıklamada `sub()` metodu ile kaç eşleşmede değişiklik yapılacağını, metodun 4. parametresinde (count) belirtebileceğimizden bahsetmiştik. Basit bir örnek yapalım;

```python
txt = "Yaz Yaz Yaz Bir Kenara Yaz"
x = re.sub("Yaz", "Çiz", txt, 2)
print(x)
```

**Çıktı**:

```pyt
Çiz Çiz Yaz Bir Kenara Yaz
```

## sub() ve compile() metotlarının birlikte kullanımı

Aşağıdaki örnekler, düzenli ifadelere aşina olan deneyimli kullanıcıların rahatlıkla anlayabileceği örneklerdir. Düzenli ifadeleri yeni öğrenenler için anlaşılması zor gelebilir. **Compile()** Metodu ve **Bayraklar** konusu ilgili sayfalardan incelenebilir.  

`sub()` metodunu,  `compile()` metodu ile şu şekilde kullanabiliriz:

```python
a = "Kırmızı başlıklı kız, kırmızı elma dolu sepetiyle anneannesinin evine gidiyormuş!"

derle = re.compile("kırmızı", re.IGNORECASE)
print(derle.sub("yeşil", a))
```

**Çıktı**:

```python
yeşil başlıklı kız, yeşil elma dolu sepetiyle anneannesinin evine gidiyormuş!
```

Burada karakter dizimiz içinde geçen bütün **kırmızı** kelimelerini **yeşil** kelimesiyle değiştirdik. Bunu yaparken de `re.IGNORECASE` adlı derleme seçeneğinden yararlandık.

Elbette `sub()` metoduyla daha karmaşık işlemler yapılabilir. Bu noktada şöyle bir hatırlatma yapalım. Bu `sub()` metodu karakter dizilerinin `replace()` metoduna çok benzer. Ama `sub()` metodu hem kendi başına `replace()` metodundan çok daha güçlüdür, hem de beraber kullanılabilecek derleme seçenekleri sayesinde `replace()` metodundan çok daha esnektir. Eğer yapmak istediğiniz iş `replace()` metoduyla halledilebiliyorsa en doğru yol, `replace()` metodunu kullanmaktır.

Şimdi bu `sub()` metodunu kullanarak biraz daha karmaşık bir işlem yapacağız. Aşağıdaki metne bakalım:

```python
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
```

Gelin bu metin içinde geçen **çilek** kelimelerini **erik** kelimesi ile değiştirelim. Ama bunu yaparken, metin içinde **çilek** kelimesinin **Çilek** şeklinde de geçtiğine dikkat edelim. Ayrıca Türkçe kuralları gereği bu **çilek** kelimesinin bazı yerlerde ünsüz yumuşamasına uğrayarak **çileğ-** şekline dönüştüğünü de unutmayalım.

Bu metin içinde geçen **çilek** kelimelerini **erik**'le değiştirmek için birkaç yol kullanabilirsiniz. 

Birinci yolda, her değişiklik için ayrı bir düzenli ifade oluşturulabilir. Ancak bu yolun dezavantajı, metnin de birkaç kez kopyalanmasını gerektirmesidir. Çünkü ilk düzenli ifade oluşturulup buna göre metinde bir değişiklik yapıldıktan sonra, ilk değişiklikleri içeren metnin, farklı bir metin olarak kopyalanması gerekir (metin2 gibi.).

Ardından ikinci değişiklik yapılacağı zaman, bu değişikliğin metin2 üzerinden yapılması gerekir. Aynı şekilde bu metin de, mesela, metin3 şeklinde tekrar kopyalanmalıdır. Bundan sonraki yeni bir değişiklik de bu metin3 üzerinden yapılacaktır. Bu durum bu şekilde uzar gider. 

## Argüman olarak fonksiyon kullanmak

`sub()` metodu, argüman olarak bir **fonksiyon** da alabilir.

Önce basit sonra biraz daha karışık iki örnek yapalım.

1. **Örnek (Basit):**

Elimizdeki metinde bulunan Türkçe karakterleri, başka karakterlerle değiştirelim. Önce bunu gerçekleştirecek bir fonksiyon oluşturalım. Sonra bu fonksiyonu `sub()` fonksiyonuna argüman olarak verelim. Bu örnek için yukarıdaki metni kullanalım.

```python
def degistir_fonk(eslesme):        # Fonksiyon yazıyoruz / oluşturuyoruz.
    turkce_karakter_karsiligi = {
    "ç" : "c",
    "Ç" : "C",
    "ğ" : "g",
    "Ğ" : "G",
    "ı" : "i",
    "İ" : "I",
    "ö" : "o",
    "Ö" : "O",
    "ş" : "s",
    "Ş" : "S",
    "ü" : "u",
    "Ü" : "U"
    }
    return turkce_karakter_karsiligi[eslesme.group()]

desen = r"[çÇğĞıİöÖşŞüÜ]"    # desen tanımlıyoruz.

yeni_metin = re.sub(desen, degistir_fonk, metin)    # fonksiyonu fonksiyona argüman olarak veriyoruz.

print(yeni_metin)    # İşlem sonrası sonucu ekrana yazdırıyoruz.
```

**Çıktı**:

```textile
Karadeniz Ereglisi denince akla ilk olarak komur ve demir-celik
gelir. Kokusu ve tadiyla dunyaya nam salmis meshur Osmanli cilegi ise ismini
verdigi festival gunleri disinda pek hatirlanmaz. Oysa Cin'den Arnavutkoy'e
oradan da Eregli'ye getirilen krallarin meyvesi cilek, burada gecirdigi degisim
sonucu tadina doyulmaz bir hal alir. Eregli'nin havasindan mi suyundan mi
bilinmez, kokusu, tadi bambaska bir hale donusur ve meshur Osmanli cilegi
unvanini hak eder. Bu nazik ve aromali cilekten yapilan recel de likor de bir
baska olur. Bu yil dokuzuncusu duzenlenen Uluslararasi Osmanli Cilegi Kultur
Festivali'nde 36 uretici arasinda yetistirdigi cileklerle birinci olan Kocaali
Koyu'nden Guner Ozdemir, yilda bir ton urun aliyor. 60 yasindaki Ozdemir,
cileklerinin sirrini yogun ilgiye ve icten duydugu sevgiye bagliyor: "Erkekler
bahcemize giremez. Koca ayaklariyla ezerler cileklerimizi" Cilegi toplamanin zor
oldugunu soyleyen Ayse Ozhan da cocuklugundan bu yana cilek bahcesinde
calisiyor. Her sabah 04.00'te kalkan Ozhan, cileklerini ozenle suluyor. Kasim
basinda ektigi cilek fideleri haziran basinda meyve veriyor.
```

Tam istediğimiz gibi, tüm Türkçe karakterler değişmiş.

2. **Örnek (Karışık / Zor):**

Yukarıdaki örnekten devam edersek, metni tekrar tekrar kopyalamak yerine, düzenli ifadeleri kullanarak şöyle bir çözüm de üretebiliriz:

```python
derle = re.compile("çile[kğ]", re.IGNORECASE)

def degistir(nesne):
    a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
    b = nesne.group().split()
    for i in b:
        return a[i]

print(derle.sub(degistir, metin))
```

**Çıktı**:

```textile
Karadeniz Ereğlisi denince akla ilk olarak kömür ve demir-çelik
gelir. Kokusu ve tadıyla dünyaya nam salmış meşhur Osmanlı eriği ise ismini
verdiği festival günleri dışında pek hatırlanmaz. Oysa Çin'den Arnavutköy'e
oradan da Ereğli'ye getirilen kralların meyvesi erik, burada geçirdiği değişim
sonucu tadına doyulmaz bir hal alır. Ereğli'nin havasından mı suyundan mı
bilinmez, kokusu, tadı bambaşka bir hale dönüşür ve meşhur Osmanlı eriği
unvanını hak eder. Bu nazik ve aromalı erikten yapılan reçel de likör de bir
başka olur. Bu yıl dokuzuncusu düzenlenen Uluslararası Osmanlı Eriği Kültür
Festivali'nde 36 üretici arasında yetiştirdiği eriklerle birinci olan Kocaali
Köyü'nden Güner Özdemir, yılda bir ton ürün alıyor. 60 yaşındaki Özdemir,
eriklerinin sırrını yoğun ilgiye ve içten duyduğu sevgiye bağlıyor: "Erkekler
bahçemize giremez. Koca ayaklarıyla ezerler eriklerimizi" Eriği toplamanın zor
olduğunu söyleyen Ayşe Özhan da çocukluğundan bu yana erik bahçesinde
çalışıyor. Her sabah 04.00'te kalkan Özhan, eriklerini özenle suluyor. Kasım
başında ektiği erik fideleri haziran başında meyve veriyor.
```

Gördüğünüz gibi, `sub()` metodu, argüman olarak bir **fonksiyon** da alabiliyor. Yukarıdaki kodlar biraz karışık görünmüş olabilir. Tek tek açıklayalım.

Öncelikle şu satıra bakalım:

```python
derle = re.compile("çile[kğ]", re.IGNORECASE)
```

Burada amacımız, metin içinde geçen **çilek** ve **çileğ** kelimelerini bulmak. Neden **çileğ**? Çünkü **çilek** kelimesi bir sesli harften önce geldiğinde sonundaki **k** harfi **ğ**'ye dönüşüyor. Bu seçenekli yapıyı, daha önceki bölümlerde gördüğümüz `[ ]` köşeli parantez adlı metakarakter yardımıyla oluşturduk. Düzenli ifade kalıbımızın hem büyük harfleri hem de küçük harfleri aynı anda bulması için `re.IGNORECASE` seçeneğinden yararlandık.

Şimdi de şu satırlara bakalım:

```python
def degistir(nesne):
    a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
    b = nesne.group().split()
    for i in b:
        return a[i]
```

Burada, daha sonra `sub()` metodu içinde kullanacağımız fonksiyonu yazıyoruz. Fonksiyonu, `def degistir(nesne)` şeklinde tanımladık. Burada **“nesne”** adlı bir argüman kullanmamızın nedeni, fonksiyon içinde `group()` metodunu kullanacak olmamız. Bu metodu fonksiyon içinde **“nesne”** adlı argümana bağlayacağız. Bu fonksiyon, daha sonra yazacağımız `sub()` metodu tarafından çağrıldığında, yaptığımız arama işlemi sonucunda ortaya çıkan **“eşleşme nesnesi”** fonksiyona atanacaktır (eşleşme nesnesinin ne demek olduğunu ilk bölümlerde anlatıldı). İşte **“nesne”** adlı bir argüman kullanmamızın nedeni de, eşleşme nesnelerinin bir metodu olan `group()` metodunu fonksiyon içinde kullanabilmek.

Bir sonraki satırda bir adet sözlük görüyoruz:

```python
a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
```

Bu sözlüğü oluşturmamızın nedeni, metin içinde geçen bütün **“çilek”** kelimelerini tek bir **“erik”** kelimesiyle değiştiremeyecek olmamız. Çünkü **“çilek”** kelimesi metin içinde pek çok farklı biçimde geçiyor. Başta da dediğimiz gibi, yukarıdaki yol yerine metni birkaç kez kopyalayarak ve her defasında bir değişiklik yaparak da sorunu çözebilirsiniz. (Mesela önce **“çilek”** kelimelerini bulup bunları **“erik”** ile değiştirirsiniz. Daha sonra **“çileğ”** kelimelerini arayıp bunları **“eriğ”** ile değiştirirsiniz, vb…) Ama metni tekrar tekrar oluşturmak pek performanslı bir yöntem olmayacaktır. Bizim şimdi kullandığımız yöntem metin kopyalama zorunluluğunu ortadan kaldırıyor. Bu sözlük içinde **“çilek”** kelimesinin alacağı şekilleri sözlük içinde birer anahtar olarak, **“erik”** kelimesinin alacağı şekilleri ise birer **“değer”** olarak belirliyoruz.

Sonraki satırda iki metot birden var:

```python
b = nesne.group().split()
```

Burada, fonksiyonumuzun argümanı olarak vazife gören eşleşme nesnesine ait metotlardan biri olan `group()` metodunu kullanıyoruz. Böylece `derle = re.compile("çile[kğ]", re.IGNORECASE)` satırı yardımıyla metin içinde bulduğumuz bütün **“çilek”** ve çeşitlerini alıyoruz. Karakter dizilerinin `split()` metodunu kullanmamızın nedeni ise `group()` metodunun verdiği çıktıyı liste haline getirip daha kolay manipüle etmek. Burada `for i in b: print(i)` komutunu verirseniz `group()` metodu yardımıyla ne bulduğumuzu görebilirsiniz:

```python
çileğ
çilek
çileğ
çilek
Çileğ
çilek
çilek
çilek
Çileğ
çilek
çilek
çilek
```

Bu çıktıyı gördükten sonra, kodlarda yapmaya çalıştığımız şey daha anlamlı görünmeye başlamış olmalı. Şimdi sonraki satıra geçiyoruz:

```python
for i in b:
    return a[i]
```

Burada, `group()` metodu yardımıyla bulduğumuz eşleşmeler üzerinde bir `for` döngüsü oluşturduk. 
    Ardından da `return a[i]` komutunu vererek “a” adlı sözlük içinde yer alan öğeleri yazdırıyoruz. Bu arada, buradaki "**i**"nin yukarıda verdiğimiz `group()` çıktılarını temsil ettiğine dikkat edin. `a[i]` gibi bir komut verdiğimizde aslında sırasıyla şu komutları vermiş oluyoruz:  

```python
a["çilek"]
a["çileğ"]
a["çilek"]
a["Çileğ"]
a["çilek"]
a["çilek"]
a["çilek"]
a["Çileğ"]
a["çilek"]
a["çilek"]
```

Bu komutların çıktıları sırasıyla **“erik”, “eriğ”, “erik”, “Eriğ”, “erik”, “erik”, “erik”, “Eriğ”, “erik”, “erik”** olacaktır. İşte bu `return` satırı bir sonraki kod olan `print(derle.sub(degistir,metin))` ifadesinde etkinlik kazanacak. Bu son satırımız sözlük öğelerini tek tek metne uygulayacak ve mesela `a["çilek"]` komutu sayesinde metin içinde **“çilek”** gördüğü yerde **“erik”** kelimesini yapıştıracak ve böylece bize istediğimiz şekilde değiştirilmiş bir metin verecektir.

Bu kodların biraz karışık gibi göründüğünü biliyorum, ama aslında çok basit bir mantığı var: `group()` metodu ile metin içinde aradığımız kelimeleri ayıklıyor. Ardından da **“a”** sözlüğü içinde bunları anahtar olarak kullanarak **“çilek”** ve çeşitleri yerine **“erik”** ve çeşitlerini koyuyor.

### Örnek: Tarihleri Düzenle

Bir tane de tarih verisi ile ilgili kullanım örneği verelim. Verilerimizde farklı tarih formatları bulunuyor. Örneğin, "01/01/2023", "1.5.2021", "12-2-1980", "25/10/18". Bu tarih formatlarını belirli bir formata dönüştürmek için `re.sub()` kullanabiliriz. Aşağıda, bu tarih formatlarını "dd/mm/yyyy" formatına dönüştüren bir örnek var:

```python
import re

tarihler = """
01/01/2023
1.5.2021
12-2-1980
25/10/18
"""

def duzenle(match):
    gun, ay, yil = match.groups()
    return f"{gun.zfill(2)}/{ay.zfill(2)}/{yil.zfill(4)}"

pattern = re.compile(r"(\d{1,2})[\/\.\-](\d{1,2})[\/\.\-](\d{2,4})")
duzenlenmis_tarihler = re.sub(pattern, duzenle, tarihler)

print(duzenlenmis_tarihler)
```

Bu kod, `re.sub()` fonksiyonunu kullanarak tarih formatlarını belirli bir formata dönüştürür. `duzenle` fonksiyonu, her eşleşme için çağrılır ve tarihi "dd/mm/yyyy" formatına dönüştürür.

```python
01/01/2023
01/05/2021
12/02/1980
25/10/2018
```

Bu örnekte `zfill` kullanarak gün, ay ve yılın sırasıyla 2, 2 ve 4 karakterli olmasını sağladık. İhtiyacınıza göre bu düzenlemeleri değiştirebilirsiniz.

### Örnek: Telefon Numaralarını Düzenle

Son olarak ta farklı biçimlerdeki telefon numaralarını düzenlemek için de `re.sub()` fonksiyonunu kullanarak bir örnek yapalım:

```python
import re

numaralar = """
1234567890
533-456-7891
544 456 7892
(216) 456-7893
"""

def duzenle_telefon(match):
    operator, üçhane, dorthane = match.groups()
    return f"({operator}) {üçhane}-{dorthane}"

telefon_pattern = re.compile(r"\(?(?P<operator>\d{3})\)?[ \-]?(?P<üçhane>\d{3})[ \-]?(?P<dorthane>\d{4})")
duzenlenmis_numaralar = re.sub(telefon_pattern, duzenle_telefon, numaralar)

print(duzenlenmis_numaralar)
```

Bu kod, farklı biçimlerdeki telefon numaralarını aynı formata ("(123) 
456-7890") dönüştürür. `duzenle_telefon` fonksiyonu, her eşleşme için çağrılır ve telefon numarasını belirli bir formata dönüştürür.

```python
(123) 456-7890
(533) 456-7891
(544) 456-7892
(216) 456-7893
```

Yukarıda verdiğimiz düzenli ifadeyi böyle ufak bir metinde kullanmak çok anlamlı olmayabilir. Ama çok büyük metinler üzerinde çok çeşitli ve karmaşık değişiklikler yapmak istediğinizde bu kodların işinize yarayabileceğini göreceksiniz.

### sub() Fonksiyonunun, dosya işlemleri ile kullanımı

Elimizde bulunan bir dosya içerisinde değiştirmek istediğimiz deseni tanımlayarak değişiklik yapabiliriz. Örneğin UFO'lar ile alakalı elimizde bir txt dosyası olduğunu düşünelim. Dosyamızın adı **"UFO Nedir.txt"** olsun. Bu dosya içeriği açağıdaki gibidir.

```textile
UFO (İngilizce: "Unidentified Flying Object"/tanımlanamayan uçan nesne);
bilimsel bir açıklaması olmadığı ve genellikle dünya dışı yaşam taşıdığı
iddia edilen gizemli nesne.[1] Türkçede uçan daire kavramı da sıklıkla 
UFO anlamında kullanılır.[2] ufo fenomenleri bazen sadece gözlemcilerin 
iddiasından, bazen de çeşitli kayıt cihazlarıyla elde edilen görüntü 
ve/veya seslerden ibarettir. Ufo'larla ilgili kayıt ve iddiaları inceleyen
kişilere ufolog, bu uğraşa ise ufoloji adı verilir.

Daha öncesinde de uFo gözlemleri yapılmış olmakla birlikte, gözlem 
raporları 1950'li yıllardan itibaren, özellikle ABD’de büyük bir artış 
göstermiştir. Bu yıllardan itibaren günümüze kadar on binlerce ufO iddiası
kaydedilmiştir.[3] 
```

Dosya içerisinde geçen tüm **UFO** kelimelerini (**UFO, ufo, Ufo, uFo, ...vb**) `***` sembolü ile filtreleyerek ayrı bir dosyaya (**filtreli.txt**) kaydetmek isteyelim.

```python
import re

with open("UFO nedir.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

desen = r"\b[uU][fF][oO]\b"
filtreli_icerik = re.sub(desen, "***", icerik)

with open("filtreli.txt", "w", encoding="utf-8") as dosya:
    dosya.write(filtreli_icerik)
```

**filtreli.txt** dosya içeriğine bakacak olursak aşağıdaki çıktı ile karşılaşırız. İstediğimiz gibi Ufo ifadelerinin tüm varyasyonları `***` ile filtrelenmiş.

```textile
*** (İngilizce: "Unidentified Flying Object"/tanımlanamayan uçan nesne);
bilimsel bir açıklaması olmadığı ve genellikle dünya dışı yaşam taşıdığı
iddia edilen gizemli nesne.[1] Türkçede uçan daire kavramı da sıklıkla 
*** anlamında kullanılır.[2] *** fenomenleri bazen sadece gözlemcilerin 
iddiasından, bazen de çeşitli kayıt cihazlarıyla elde edilen görüntü 
ve/veya seslerden ibarettir. ***'larla ilgili kayıt ve iddiaları inceleyen
kişilere ufolog, bu uğraşa ise ufoloji adı verilir.

Daha öncesinde de *** gözlemleri yapılmış olmakla birlikte, gözlem 
raporları 1950'li yıllardan itibaren, özellikle ABD’de büyük bir artış 
göstermiştir. Bu yıllardan itibaren günümüze kadar on binlerce *** iddiası
kaydedilmiştir.[3] 
```
