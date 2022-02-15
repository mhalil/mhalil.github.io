# Python'a Giriş

Bu bölümün amacı, Python programlama dili hakkında kısaca bilgi vermek ve ardından FreeCAD programı içerisinde Python kodu yazmayı ve/veya yazdığımız kodları çalıştırmayı öğrenmektir.

Bu, Python'a yeni başlayanlar için kısa bir eğitimdir. Python, açık kaynaklı, çok platformlu bir programlama dilidir. Onu diğer programlama dillerinden farklı kılan ve yeni kullanıcılar için çok erişilebilir kılan çeşitli özelliklere sahiptir:

+ Python, İnsanlar tarafından okunabilecek şekilde tasarlanmıştır, bu da öğrenmeyi ve anlamasını nispeten kolaylaştırır.
+ Python Yorumlanır bir dildir, bu, programların çalıştırılmadan önce derlenmesine gerek olmadığı anlamına gelir. Python kodu dilerseniz satır satır dahi olsa anında çalıştırılabilir.
+ Python, bir betik dili olarak diğer programlara gömülebilir. FreeCAD, gömülü bir Python yorumlayıcısına sahiptir. FreeCAD'in parçalarını işlemek için Python kodu yazabilirsiniz. Bu çok güçlüdür, kendi araçlarınızı oluşturabileceğiniz anlamına gelir.
+ Genişletilebilir, yeni modülleri Python kurulumunuza kolayca bağlayabilir ve işlevselliğini artırabilirsiniz. Örneğin, Python'un görüntüleri okumasına ve yazmasına, Twitter ile iletişim kurmasına, işletim sisteminiz tarafından gerçekleştirilecek görevleri zamanlamasına ,... vb. izin veren modüller vardır.

Aşağıdakiler python konusunda temel bir bilgilerdir ve bu eksiksiz bir eğitim değildir. Ancak FreeCAD ve mekanizmaları (yöntemi, tekniği, düzeneği) hakkında daha fazla araştırma yapmak için iyi bir başlangıç noktası sağlayacağını umuyorum. Aşağıdaki kod parçacıklarını bir Python yorumlayıcısına girmenizi şiddetle tavsiye ederiz.

# Yorumlayıcı (İnterpreter)

Genellikle bilgisayar programları yazarken, bir metin düzenleyici veya özel programlama ortamınızı (temelde bazı ek araçlar içeren bir metin düzenleyicidir) açarsınız, programınızı yazarsınız, ardından derler ve çalıştırırsınız. Genellikle giriş sırasında bir veya daha fazla hata yapılır, bu nedenle programınız çalışmaz. Kodların doğru çalışmamasına dair neyin yanlış gittiğini bildiren bir hata mesajı bile alabilirsiniz. Ardından metin düzenleyicinize geri dönün, hataları düzeltin, tekrar çalıştırın, programınız istendiği gibi çalışana kadar tekrarlayın.

Python'da tüm süreç Python yorumlayıcısı içinde şeffaf bir şekilde yapılabilir. Yorumlayıcı, basitçe Python kodunu yazabileceğiniz komut istemine sahip bir Python penceresidir. Python'u bilgisayarınıza yüklediyseniz (Windows veya Mac kullanıyorsanız Python web sitesinden indirin, GNU/Linux kullanıyorsanız paket havuzunuzdan yükleyin), başlat menünüzde bir Python yorumlayıcısı olacaktır. Ancak, daha önce de belirtildiği gibi, FreeCAD ayrıca yerleşik bir Python yorumlayıcısına sahiptir.

![Python_konsolu](img/python_konsolu.png)

FreeCAD içerisinde Python konsolunu Göremiyorsanız, **Görünüm → Paneller → Python konsolu**'na tıklayın. Python konsolu yeniden boyutlandırılabilir ve ayrıca yerinden ayrılabilir / taşınıp hareket ettirilebilir.

**Yorumlayıcı**, öncelikle bilgisayarınızda kurulu olan **Python sürüm bilgisini**, ardından komut istemi olan bir `>>>` sembolünü gösterir. Yorumlayıcı içerisinde kod yazmak basittir: her satır bir talimattır. Enter tuşuna bastığınızda, kod satırınız yürütülür/çalıştırılır. Örneğin, şunu yazmayı deneyin: 

```python
print("merhaba")
```

`print()`, ekrana bir şey yazdıran bir Python komutudur. Enter'a bastığınızda işlem gerçekleştirilir ve `merhaba` mesajı yazdırılır. Bir hata yaparsanız, örneğin şunu yazalım:

```python
print(merhaba)
```

Python bunun hatalı bir kod olduğunu size hemen söyleyecektir. Bu durumda Python `merhaba` ifadesinin ne olduğunu bilmiyor. `" "` (çift tırnak işaretleri) karakterleri, içeriğin bir metin parçası için programlama jargonu olan bir **dize (string)** olduğunu belirtir. Bunlar olmadan `print()` komutu `merhaba`'yı tanımıyor. Yukarı oka basarak son kod satırına geri dönebilir ve kodu düzeltebilirsiniz.

Python yorumlayıcısı ayrıca yerleşik bir yardım sistemine sahiptir. Diyelim ki `print(merhaba)` ile neyin yanlış gittiğini anlamadık ve komut hakkında özel bilgi istiyoruz:
```python
help("print")
```

Bu komutu yazıp çalıştırdığınızda `print()` komutunun yapabileceği her şeyin uzun ve eksiksiz bir açıklamasını alacaksınız (açıklamalar konsol ekranında görüntülenecektir).
Artık Python yorumlayıcısını anladığınıza göre, daha ciddi şeylerle devam edebiliriz.

# Değişkenler

Programlamada sıklıkla bir isim altında bir değer saklamanız gerekir. İşte burada değişkenler devreye girer. Örneğin şunu yazın:

```python
a = "merhaba"
print(a)
```

Muhtemelen burada ne olduğunu anlamışsınızdır, `merhaba` dizesini (string) `a` adı altında kaydettik, `a` değişkenine atadık. Artık `a` bilindiğine göre, onu herhangi bir yerde kullanabiliriz, örneğin `print()` komutunda. Değişken olarak istediğimiz herhangi bir ismi kullanabiliriz, sadece boşluk karakteri veya noktalama işaretleri kullanmamak (değişken adı rakam ile başlayamaz) ve Python anahtar kelimeleri kullanmamak gibi bazı basit kurallara uymamız gerekiyor. Örneğin şunu yazabiliriz:

```python
merhaba = "şahsi selamlama mesajım"
print(merhaba)
```

Artık `merhaba` kelimesi tanımsız değil, bir değişken olarak tanımlanmış durumda. Değişkenler herhangi bir zamanda değiştirilebilir, bu yüzden **değişkenler** olarak adlandırılırlar, içerikleri değişebilir. Örneğin:

```python
degiskenim = "merhaba"
print(degiskenim)
degiskenim = "hoşçakal"
print(degiskenim)
```

Görüldüğü üzere `degiskenim` isimli değişkenin değerini değiştirdik.

```python
degisken1 = "merhaba"
degisken2 = degisken1
print(degisken2)
```

Değişkenlerinize anlamlı isimler vermenizi tavsiye edilir. Bir süre sonra değişkeninizin neyi temsil ettiğini hatırlamayacaksınız. Ancak, örneğin hoşgeldiniz mesajım adını verdiyseniz, amacını kolayca hatırlayacaksınız. 

İsimlendirme çok önemli, `myVariable` ile `myvariable` aynı şey değil. Değişkeni tanımlarken isim olarak `myVariable` belirlemişseniz  `print(myvariable)` komutunu çalıştırmaya çalıştığınızda, değişkenin  tanımlanmadığına dair hata alacaksınız. Python’da Büyük-küçük harf duyarlılığı vardır.

# Sayılar

Tabii ki Python programları sadece metin dizileriyle değil, her türlü veriyle uğraşabilir. Önemli olan bir şey var, Python ne tür verilerle uğraştığını bilmelidir. `Print(merhaba)` örneğimizde `print()` komutunun **"merhaba"** dizgemizi tanıdığını gördük. `" "` karakterlerini kullanarak, aşağıdakilerin bir metin dizesi olduğunu belirttik.

`type()` komutu ile bir değişkenin veri tipini her zaman kontrol edebiliriz:

```python
deger = "merhaba"
type(deger)
```

Bize **myVar**'ın içeriğinin **string** için kısa olan bir `'str'` olduğunu söyleyecektir. Ayrıca tamsayı ve ondalıklı sayılar gibi başka temel veri türlerimiz de vardır:

```python
ilkSayi = 10
ikinciSayi = 20
print(ilkSayi + ikinciSayi)
type(ilkSayi)
```

Python, 10 ve 20'nin tamsayılar olduğunu bilir, bu nedenle `'int'` olarak saklanırlar ve Python tamsayılarla yapabileceği her şeyi onlarla yapabilir. Bunun sonuçlarına bakın:

```python
ilkSayi = “10”
ikinciSayi = “20”
print(ilkSayi + ikinciSayi)
```

Burada Python'u, iki değişkenimizin **sayı değil metin parçaları** olduğunu düşünmeye zorladık. Python iki parça metni birbirine ekleyebilir, ancak bu durumda elbette herhangi bir aritmetik işlem  gerçekleştirmeyecektir, metinler yan yana yazılacaktır. 

```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Tam sayılar ve Ondalıklı sayılar sorunsuz bir şekilde toplanabilir:

```python
toplam = var1 + var2
print(toplam)
print(type(toplam))
```

**var2** bir Ondalıklı Ondalıklı sayı olduğundan, Python otomatik olarak sonucun bir Ondalıklı sayı olması gerektiğine karar verir. Ancak Python'un hangi türü kullanacağını bilmediği durumlar da vardır. Örneğin:

```python
varA = "merhaba 123"
varB = 456
print(varA + varB)
```

Bu kod çalıştırıldığı zaman bir hata ile karşılaşılır, **varA** bir **dizedir (string)** ve **varB** bir **tamsayıdır** ve Python ne yapacağını bilmez. Ancak, Python'u türler arasında dönüşüm yapmaya zorlayabiliriz:

```python
varB = str(varB)
```
Ayrıca bir değişkeni tamsayıya dönüştürmek için `int()` ve `float()` kullanabilir ve istersek float kullanabiliriz:

```python
varA = "123"
print(int(varA))
print(float(varA))
```

`print()` komutunu birkaç şekilde kullandığımızı fark etmiş olmalısınız. Değişkenleri, toplamları, virgülle ayrılmış birkaç şeyi ve hatta başka bir Python komutunun sonucunu yazdırdık. Belki bu iki komutu da görmüşsünüzdür:

```python
type(varA)
print(type(varA))
```

Terminal / konsol içerisinde yazdığınızda, bu iki komut aynı sonucu verecektir. Bunun nedeni, yorumlayıcıda her şeyin otomatik olarak yazdırılmasıdır. Yorumlayıcının dışında çalışan daha karmaşık programlar yazdığımızda, bunlar otomatik olarak yazdırılmayacaktır, bu nedenle `print()` komutunu kullanmamız gerekecek. Bunu akılda tutarak, burada `print()` komutu kullanmayı bırakalım. Bundan sonraki anlatımlarda, kodları terminalde yazdığınızı düşünerek şu şekilde yazacağız:

```python
myVar = "hello friends"
myVar
```
# Listeler

Bir başka kullanışlı veri türü de bir **listedir**. Liste, diğer verilerin bir koleksiyonudur. Bir liste tanımlamak için `[ ]` kullanırız:

```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

Gördüğünüz gibi bir liste, her türlü veriyi (string, intger,...vb) içerebilir. Bir liste ile birçok şey yapılabilir. Örneğin, listedeki öğelerin miktarını hesaplayabiliriz:

```python
len(myOtherList)
```

Veya bir öğeyi alın:

```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

`len()` komutu bir listedeki toplam öğe sayısını döndürürken (değer olarak bize verirken), listedeki ilk öğe her zaman 0 (sıfır) konumundadır, bu nedenle **myOtherList** listemizde "**Bob**" 2. konumda olacaktır. Listeler içerisindeki öğeleri sıralamak, kaldırmak ve eklemek te mümkündür.

Bir metin dizesi (string ifade),  Python'daki bir karakter listesine çok benzerdir. Aşağıdaki kodları çalıştırmayı deneyin:

```python
myvar = "hello"
len(myvar)
myvar[2]
```

Genellikle listelerle yapabileceklerinizi **string**lerle de yapabilirsiniz. Aslında hem `listeler (list)` hem de `dizeler (string)` sıralı yapıdır.

`Dizeler, tamsayılar, ondalıklı sayılar` ve `listeler` dışında, `sözlükler` gibi  yerleşik veri türleri vardır ve hatta `sınıf`larla kendi veri türlerinizi oluşturabilirsiniz.


# Girinti (Indentation)

Liste kullanımının önemli, liste içerisinde gezinip  öğlere sırayla erişmek ve her bir öğe ile bir şeyler yapma yeteneğidir. Örneğin şuna bakın:

```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
	print(dalton + " Dalton")
```

`for in` komutuyla listemizi döngüye soktuk (programlama jargonu) ve her bir öğeyle bir şeyler yaptık. Özel sözdizimine dikkat edin: `for` komutu `:` ile sonlanır, bu işaret (iki nokta üstüste), alt satırda bir kod bloğu olacağını belirtir. Yorumlayıcıda, `:` ile biten komut satırına girdikten hemen sonra komut istemi `...` olarak değişecektir.

Python,  `for` döngüsü içinde, sonraki satırlardan kaçının çalıştırılması gerektiğini nasıl bilecek? Bunun için Python girintiye güvenir. Sonraki satırlar bir boşluk veya birkaç boşluk veya bir sekme veya birkaç sekme ile başlamalıdır. Girinti aynı kaldığı sürece satırlar `for in` bloğunun bir parçası olarak kabul edilecektir. Kod bloğunun bir satırına 2, sonraki satırına 4 boşluk bırakarak  kod yazmaya başlarsanız, bir hata mesajı lırsınız, kodlarınız çalışmaz. Blokta yazacağınız kodlar bittiğinde, girintisiz başka bir satır yazmanız veya `for in` bloğundan geri dönmek için `Enter` tuşuna basmanız yeterlidir.

Girinti ayrıca programın/kodların okunabilirliğine de yardımcı olur. Büyük bir program yazarken büyük girintiler kullanırsanız (örneğin boşluklar yerine sekmeler kullanırsanız), neyin neyin içinde yürütüldüğünü net bir şekilde görebilirsiniz. Diğer komutların da girintili kod blokları kullandığını göreceğiz.

`for in` komutu, birden fazla kez yapılması gereken birçok şey için kullanılabilir. Örneğin, `range()` komutuyla birleştirilebilir:

```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
	print(number)
	total = total + number
print("----")
print(total)
```

Eğer yorumlayıcıda `help(range)` yazarsanız şunu göreceksiniz:

```python
range(...)
	range(stop) -> list of integers
	range(start, stop[, step]) -> list of integers
```

Burada köşeli parantezler isteğe bağlı bir parametreyi belirtir. Ancak hepsinin tamsayı olması bekleniyor. Aşağıda adım (artış miktarı) parametresini `int()` kullanarak bir tamsayı olmaya zorlayacağız:

```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number)):
	print(float(i) / number)
```

Bir başka `range()` örneği:

```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
	print(alldaltons[n], " is Dalton number ", n)
```

`range()` komutu ayrıca 0 (sıfır) ile başlaması (başlangıç ​​numarasını belirtmezseniz) ve son numarasının belirttiğiniz bitiş sayısından bir eksik olması gibi garip bir özelliğe sahiptir. Yani Bitiş değeri işleme dahl edilmez. Bu, elbette, diğer Python komutlarıyla iyi çalışır. Örneğin:

```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```

Girintili blokların bir başka ilginç kullanımı ise `if` komutudur. Bu komut, yalnızca belirli bir koşul karşılandığında bir kod bloğu çalıştırılır, örneğin:

```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```

Elbette bu, her zaman cümleyi yazdıracaktır, ancak ikinci satırı şununla değiştirmeyi deneyin:

```python
if "Lucky" in alldaltons:
```

O zaman hiçbir şey yazdırılmaz. Başka bir ifade de belirtebiliriz:

```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```

# Fonksiyonlar

Çok az [standart Python komutu](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) vardır ve bunların birçoğunu zaten biliyoruz. Ancak Python'da kendi komutlarınızı oluşturabilirsiniz. Aslında, Python kurulumunuza ekleyebileceğiniz ek modüllerin çoğu tam da bunu yapar, kullanabileceğiniz komutlar eklerler. Python'da özel komuta, **fonksiyon** denir ve şu şekilde tanımlanır:

```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```

`def()` komutu yeni bir fonksiyon tanımlar, ona bir isim verirsiniz, bu ismi siz belirlersiniz ve parantez içinde fonksiyonun kullanacağı argümanları tanımlarsınız. Bağımsız değişkenler, işleve iletilecek verilerdir. Örneğin, `len()` komutuna bakın. Sadece `len()` yazarsanız, Python size bir argümana ihtiyacı olduğunu söyleyecektir ki bu çok açık: Bir şeyin uzunluğunu bilmek istiyorsunuz. `len(myList)` yazarsanız, `myList, len()` işlevine ilettiğiniz argümandır. `len()` işlevi, bu argümanla ne yapacağını bilecek şekilde tanımlanır. Aynı şeyi `printsqm` fonksiyonumuzla da yaptık.

`myValue` adı herhangi bir şey olabilir ve yalnızca işlev içinde kullanılacaktır. Bu sadece argümana verdiğiniz bir isimdir, böylece onunla bir şeyler yapabilirsiniz. Argümanları tanımlayarak, fonksiyona kaç tane bekleyeceğini de söylersiniz. Örneğin, bunu yaparsanız:

```python
printsqm(45, 34)
```

bu kodu yzadığınızda bir hata oluşacaktır. Fonksiyonumuz sadece bir argüman alacak şekilde programlandı, ancak iki adet argüman (45 ve 34) aldı. Başka bir örnek deneyelim:

```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Burada iki argüman alan,  argümanları toplayan ve bu değeri **döndüren** (yani değeri, istenildiğinde kullanılabilecek şekilde hafızada tutan) bir fonksiyon yaptık. Bir şeyi **döndürmek** çok yararlıdır, çünkü sonuçla `myTotal` değişkeninde saklamak gibi bir şey yapabiliriz.


# Modüller

Artık Python'un nasıl çalıştığı hakkında iyi bir fikriniz olduğuna göre, bir şeyi daha bilmeniz gerekecek: Dosyalar ve modüllerle nasıl çalışılır.

Şimdiye kadar Python komutlarını yorumlayıcıda satır satır yazdık. Bu yöntem açıkça daha büyük programlar için uygun değildir. Normalde Python programlarının kodu, `.py` uzantılı dosyalarda saklanır. Yalnızca düz metin dosyaları olan ve herhangi bir metin düzenleyici (Linux gedit, emacs, vi ve hatta Windows Not Defteri) bunları oluşturmak ve düzenlemek için kullanılabilir.

Bir Python programını çalıştırmanın birkaç yolu vardır. Windows'ta dosyanıza sağ tıklayın, Python ile açın ve çalıştırın. Ancak bunu Python yorumlayıcısının kendisinden de çalıştırabilirsiniz. Bunun için yorumlayıcı programınızın nerede olduğunu bilmelidir. FreeCAD'de en kolay yol, programınızı FreeCAD'in Python yorumlayıcısının varsayılan olarak bildiği bir klasöre, örneğin **FreeCAD'in kullanıcı Mod** klasörüne yerleştirmektir:

+ Linux'ta genellikle /home/<username>/.FreeCAD/Mod/.
+ Windows'ta %APPDATA%\FreeCAD\Mod\, genellikle C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\.
+ Mac OSX'te genellikle /Users/<username>/Library/Preferences/FreeCAD/Mod/.

Buraya **scripts** adında bir alt klasör ekleyelim ve ardından şöyle bir kod yazalım ve dosyayı kaydedelim:

```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```

Dosyayı **scripts** (komut dosyaları) klasörüne `myTest.py` ismiyle kaydedin ve yorumlayıcı penceresinde şunu yazın:

```python
import myTest
```

`.py` uzantısı olmadan yazıldığına dikkat edin. Bu, dosyanın içeriğini sanki yorumlayıcıda yazmışız gibi satır satır yürütecektir. Toplama (sum) fonksiyonu oluşturulacak ve mesaj yazdırılacaktır. Bizimki gibi işlevler içeren dosyalara **modül** denir.

Yorumlayıcıya bir `sum()` işlevi yazdığımızda, onu şu şekilde çalıştırırız:

```python
sum(14, 45)
```

Ancak `sum()` işlevi içeren bir modülü içe aktardığımızda sözdizimi biraz farklıdır:

```python
myTest.sum(14, 45)
```

Yani modül bir "**container**" olarak içe aktarılır ve tüm işlevleri o konteynerin içindedir. Bu çok kullanışlıdır, çünkü birçok modülü içe aktarabilir ve her şeyi iyi organize edebiliriz. Temel olarak, aralarında bir nokta olan `bir_şey.başka_bir_şey` gördüğünüzde, bu, `başka_bir_şey`'in `bir_şey`'in içinde olduğu anlamına gelir.

Ayrıca `sum()` işlevimizi doğrudan ana yorumlayıcı alanına da aktarabiliriz:

```python
from myTest import *
sum(12, 54)
```

Hemen hemen tüm modüller bunu yapar: yorumlayıcıda veya kendi Python modüllerinizde kullanabileceğiniz işlevleri, yeni veri türlerini ve sınıfları tanımlarlar, çünkü modülünüzdeki diğer modülleri içe aktarmanızı hiçbir şey engelleyemez!

Hangi modüllere sahip olduğumuzu, hangi işlevlerin içinde olduğunu ve bunları nasıl kullanacağımızı (yani ne tür argümanlara ihtiyaç duyduklarını) nasıl bilebiliriz? Python'un bir `help()` işlevi olduğunu gördük. 

```python
help("modules")
```

Yukarıdaki kodu konsolda yazdığımızda, bilgisayarımızda yüklü olan mevcut tüm modüller listelenecektir. Bunlardan herhangi birini içe aktarabilir ve modül içeriklerine `dir()` komutuyla göz atabiliriz:

```python
import math
dir(math)
```

`math` (Matematik) modülünde bulunan tüm işlevlerin yanı sıra `__doc__, __file__, __name__` adlı garip şeyleri göreceğiz. İyi yapılmış bir modüldeki her fonksiyonun nasıl kullanılacağını açıklayan bir `__doc__` vardır. Örneğin `math` (matematik) modülünün içinde bir `sin()` fonksiyonu olduğunu görüyoruz. Nasıl kullanılacağını bilmek ister misiniz?

```python
print(math.sin.__doc__)
```

Belirgin olmayabilir, ancak `doc`un her iki tarafında iki alt çizgi karakteri vardır.

Ve son olarak son bir ipucu: Yeni veya mevcut kod üzerinde çalışırken, FreeCAD makro dosya uzantısı `.FCMacro`'yu kullanmamak, bunun yerine standart `.py` uzantısını kullanmak daha iyidir. Bunun nedeni Python'un `.FCMacro` uzantısını tanımamasıdır. `.py` kullanırsanız, kodunuz daha önce gördüğümüz gibi import ile kolayca yüklenebilir ve ayrıca `importlib.reload()` ile yeniden yüklenebilir:

```python
import importlib
importlib.reload(myTest)
```

Ancak bir alternatif var:

```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```

# FreeCAD ile başlamak

Umarım artık Python'un nasıl çalıştığı hakkında iyi bir fikriniz vardır ve FreeCAD'in neler sunabileceğini keşfetmeye başlayabilirsiniz. FreeCAD'in Python işlevlerinin tümü farklı modüllerde iyi organize edilmiştir. FreeCAD'i başlattığınızda bazıları zaten yüklenir (içe aktarılır). Bunların neler olduğunu görmek için FreeCAD Python konsoolunda şunu yazabilirsiniz:

```python
dir()
```

# Not

+ FreeCAD, orijinal olarak Python 2 ile çalışmak üzere tasarlanmıştı. Python 2, 2020'de ömrünün sonuna ulaştığı için, FreeCAD'in gelecekteki gelişimi yalnızca Python 3 ile yapılacak ve geriye dönük uyumluluk desteklenmeyecektir.
+ Python hakkında çok daha fazla bilgi [Resmi Python eğitiminde](https://docs.python.org/3/tutorial/index.html) , [Resmi Python referansında](https://docs.python.org/3/reference/) ve en kapsamlı Türkçe kaynak olan [İstihza Python 3 Belgelerinde](https://python-istihza.yazbel.com/) bulunabilir.
  
Kaynak: [Discovering Python](https://wiki.freecadweb.org/Introduction_to_Python)