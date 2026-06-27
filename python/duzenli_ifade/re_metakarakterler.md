Title: Düzenli İfadeler - Metakarakterler
Date: 2023-09-02 15:40
Modified: 2025-11-05 19:40
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Metakarakter

# Metakarakterler (Özel Karakterler)

Metakarakterler; kabaca, programlama dilleri için özel anlam ifade eden sembollerdir. Örneğin `\n` bir bakıma bir metakarakterdir, çünkü `\n` sembolü Python programlama dili için özel bir anlam taşır. Python bu sembolü gördüğü yerde yeni bir satıra geçer. Metakarakterler, **Kendisiyle eşleşmeyen karakterler** olarak ifade edilebilir. Örneğin, **a** harfi yalnızca kendisiyle eşleşir. Tıpkı **istihza** kelimesinin yalnızca kendisiyle eşleşeceği gibi. Ancak mesela `\t` ifadesi kendisiyle eşleşmez. Python bu işareti gördüğü yerde sekme (tab) düğmesine basılmış gibi tepki verecektir. İşte düzenli ifadelerde de buna benzer metakarakterlerden yararlanacağız. Düzenli ifadeler içinde de, özel anlam ifade eden pek çok sembol, yani metakarakter vardır. Şimdi bu meta karakterleri ayrı ayrı başlıklar altında inceleyelim.

## [] Köşeli Parantez

İlk inceleyeceğimiz metakarakterlerden biri Köşeli Parantez `[ ]` sembolüdür. 
Python, **köşeli parantez içinde gördüğü bütün karakterleri tek tek liste öğelerine uygular.**

Şimdi aşağıdaki listeden **özcan**, **özhan** ve **özkan** öğelerini bu sembolden yararlanarak nasıl ayıklayacağımızı görelim:

```python
import re

liste = ["özcan", "mehmet", "süleyman", "selim", "kemal", "özkan", "esra", "dündar", "esin", "esma", "özhan", 
         "özlem"]

for i in liste:
    nesne = re.search(r"öz[chk]an", i)
    if nesne:
        print(nesne.group())
```

    özcan
    özkan
    özhan

Yukarıdaki örnekte, bir liste içinde geçen **özcan**, **özhan** ve **özkan** öğelerini ayıklıyoruz. Burada bu üç öğedeki farklı karakterleri (**c**, **h** ve **k**) köşeli parantez içinde nasıl belirttiğimize dikkat edin. 

Python, köşeli parantez içinde gördüğü bütün karakterleri tek tek liste öğelerine uyguluyor. Önce **öz** ile başlayan bütün öğeleri alıyor, ardından **öz** hecesinden sonra **c** harfiyle devam eden ve **an** hecesi ile biten öğeyi buluyor. Böylece **özcan** öğesini bulmuş oldu. 

Aynı işlemi, **öz** hecesinden sonra **h** harfini barındıran ve **an** hecesiyle biten öğeye uyguluyor. Bu şekilde ise **özhan** öğesini bulmuş oldu. 

En son hedef ise **öz** ile başlayıp **k** harfi ile devam eden ve **an** ile biten öğe. Yani listedeki **özkan** öğesi… En nihayetinde de elimizde **özcan**, **özhan** ve **özkan** öğeleri kalmış oluyor.

Yeni bir örnek ile devam edelim.

```python
a = ["23BH56","TY76Z","4Y7UZ","TYUDZ","34534"]
```

Mesela biz bu listedeki öğeler içinde, sayıyla başlayanları ayıklayalım:

```python
for i in a:
    if re.match(r"[0-9]",i):
        print(i)
```

    23BH56
    4Y7UZ
    34534

Burada parantez içinde kullandığımız ifadeye dikkat edin. **0** ile **9** arasındaki bütün öğeleri içeren bir karakter dizisi tanımladık. Yani kısaca, içinde herhangi bir sayı barındıran öğeleri kapsama alanımıza aldık. Burada ayrıca `search()` yerine `match()` metodunu kullandığımıza da dikkat edin. `match()` metodunu kullanmamızın nedeni, bu metodun bir karakter dizisinin sadece en başına bakması. Amacımız sayı ile başlayan bütün öğeleri ayıklamak olduğuna göre, yukarıda yazdığımız kod, liste öğeleri içinde yer alan ve sayı ile başlayan bütün öğeleri ayıklayacaktır.

Şimdi de isterseniz listedeki **TY76Z** öğesini nasıl alabileceğimize bakalım:

```python
for i in a:
    if re.match(r"[A-Z][A-Z][0-9]",i):
        print(i)
```

    TY76Z

Burada dikkat ederseniz düzenli ifademizin başında **A-Z** diye bir şey yazdık. Bu ifade “A” ile “Z” harfleri arasındaki bütün karakterleri temsil ediyor. Biz burada yalnızca büyük harfleri sorguladık. Eğer küçük harfleri sorgulamak isteseydik **A-Z** yerine **a-z** diyecektik. 

Düzenli ifademiz içinde geçen birinci “A-Z” ifadesi aradığımız karakter dizisi olan “TY76Z” içindeki “T” harfini, ikinci “A-Z” ifadesi “Y” harfini, “0-9” ifadesi ise “7” sayısını temsil ediyor. Karakter dizisi içindeki geri kalan harfler ve sayılar otomatik olarak eşleştirilecektir. O yüzden onlar için ayrı bir şey yazmaya gerek yok. Yalnız bu söylediğimiz son şey sizi aldatmasın. Bu “otomatik eşleştirme” işlemi bizim şu anda karşı karşıya olduğumuz karakter dizisi için geçerlidir. Farklı nitelikteki karakter dizilerinin söz konusu olduğu başka durumlarda işler böyle yürümeyebilir. Düzenli ifadeleri başarılı bir şekilde kullanabilmenin ilk şartı, üzerinde işlem yapılacak karakter dizisini tanımaktır. Bizim örneğimizde yukarıdaki gibi bir düzenli ifade kalıbı oluşturmak işimizi görüyor. Ama başka durumlarda, duruma uygun başka kalıplar yazmak gerekebilir/gerekecektir. Dolayısıyla, tek bir düzenli ifade kalıbıyla hayatın geçmeyeceğini unutmamalıyız.

Bu arada, düzenli ifadelerle ilgili daha fazla şey öğrendiğimizde yukarıdaki kodu çok daha sade bir biçimde yazabileceğiz.

## . Nokta

Bu metakarakter, **yeni satır karakteri hariç bütün karakterleri temsil etmek için kullanılır.**  `.` metakarakteri, **sadece tek bir karakterin yerini tutar**. Aşağıdaki örneği inceleyelim:

```python
for i in liste:
    nesne = re.match(r"öz.an",i)
    if nesne:
        print(nesne.group())
```

    özcan
    özkan
    özhan

Gördüğünüz gibi, daha önce `[]` metakarakterini kullanarak yazdığımız bir düzenli ifadeyi bu kez farklı şekilde yazıyoruz. Unutmayın, bir düzenli ifade birkaç farklı şekilde yazılabilir. Biz bunlar içinde en basit ve en anlaşılır olanını seçmeliyiz. Ayrıca yukarıdaki kodu birkaç farklı şekilde de yazabilirsiniz. Mesela şu yazım da bizim durumumuzda geçerli bir seçenek olacaktır:

```python
for i in liste:
    if re.match(r"öz.an",i):
        print(i)
```

    özcan
    özkan
    özhan

Yalnız, unutmamamız gereken şey, bu `.` adlı metakarakterin sadece tek bir karakterin yerini tutuyor olmasıdır. Yani şöyle bir kullanım bize istediğimiz sonucu vermez:

```python
liste = ["ahmet","kemal", "kamil", "mehmet"]

for i in liste:
    if re.match(r".met",i):
        print(i)
```

Bu kodu çalıştırıldığında hiç bir çıktı vermez. Burada `.` sembolü “ah” ve “meh” hecelerinin yerini tutamaz. `.` sembolünün görevi sadece tek bir karakterin yerini tutmaktır (yeni satır karakteri hariç). Ama biraz sonra öğreneceğimiz metakarakter yardımıyla “ah” ve “meh” hecelerinin yerini de tutabileceğiz.

`.` sembolünü kullanarak bir örnek daha yapalım.

```python
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', "1agAY54"]

for i in a:
    if re.match(r".[0-9a-z]", i):
        print(i)
```

    23BH56
    34534
    1agAY54

Burada yaptığımız şey çok basit. Şu özelliklere sahip bir karakter dizisi arıyoruz:

1. Herhangi bir karakter ile başlayacak. Bu karakter sayı, harf veya başka bir karakter olabilir.
2. Ardından bir sayı veya alfabedeki küçük harflerden herhangi birisi gelecek.
3. Bu ölçütleri karşıladıktan sonra, aradığımız karakter dizisi herhangi bir karakter ile devam edebilir.

Yukarıdaki ölçütlere uyan karakter dizilerimiz: “23BH56”, “34534”, “1agAY54”

## * Yıldız

Bu metakarakter, **kendinden önce gelen karakteri SIFIR veya DAHA FAZLA** sayıda eşleştirir. Tanımı biraz karışık olsa da örnek yardımıyla bunu da anlayacağız:

```python
yeniliste = ["st", "sat", "saat", "saaat", "falanca"]

for i in yeniliste:
    if re.match(r"sa*t",i):
        print(i)
```

    st
    sat
    saat
    saaat

Burada `*` sembolü kendinden önce gelen `a` karakterini sıfır veya daha fazla sayıda eşleştiriyor. Yani mesela `st` içinde sıfır adet `a` karakteri var. Dolayısıyla bu karakter yazdığımız düzenli ifadeyle eşleşiyor. `sat` içinde bir adet `a` karakteri var. Dolayısıyla bu da eşleşiyor. `saat` ve `saaat` karakter dizilerinde sırasıyla iki ve üç adet `a` karakteri var. Tabii ki bunlar da yazdığımız düzenli ifadeyle eşleşiyor. Listemizin en son öğesi olan `falanca`da da ilk hecede bir adet `a` karakteri var. Ama bu öğedeki sorun, bunun `s` harfiyle başlamaması. Çünkü biz yazdığımız düzenli ifadede, aradığımız şeyin `s` harfi ile başlamasını, sıfır veya daha fazla sayıda `a` karakteri ile devam etmesini ve ardından da `t` harfinin gelmesini istemiştik. `falanca` öğesi bu koşulları karşılamadığı için süzgecimizin dışında kaldı.

`s` harfinin de sıfır veya daha fazla sayıda eşleşmesini istersek düzenli ifademizi `s*a*t` veya `[sa]*t` biçiminde yazmamız gerekir. Bu iki seçenek içinde `[sa]*t` şeklindeki yazımı tercih etmenizi tavsiye ederim. 

Bir başka örnek inceleyelim:

```python
liste = ["ahmet", "kemal", "kamil", "mehmet"]

for i in liste:
    if re.match(r".*met", i):
        print(i)
```

    ahmet
    mehmet

Gördüğünüz gibi `ahmet` ve `mehmet` öğelerini başarıyla ayıkladık. Bunu yapmamızı sağlayan şey de `*` adlı metakarakter oldu. Burada Python’a şu emri verdik: *Bana kelime başında herhangi bir karakteri (`.` sembolü herhangi bir karakterin yerini tutuyor) sıfır veya daha fazla sayıda içeren ve sonu da `met` ile biten bütün öğeleri ver!*

Kısaca ifade etmek gerekirse, bu komut sayesinde, sonu `met` ile biten her şey (`met` ifadesinin kendisi de dâhil olmak üzere) kapsama alanımıza girecektir.

## + Artı

`+` metakarakteri **kendisinden önce gelen karakteri BİR veya DAHA FAZLA sayıda** tekrar eden karakterleri ayıklar.

```python
liste = ["ahmet", "mehmet", "met", "kezban"]

for i in liste:
    if re.match(r".+met",i):
        print(i)
```

    ahmet
    mehmet

```python
yeniliste = ["st", "sat", "saat", "saaat", "falanca"]

for i in yeniliste:
    if re.match(r"sa+t", i):
        print(i)
```

    sat
    saat
    saaat

```python
a = ["23BH56", "TY76Z", "4Y7UZ", "TYUDZ", "34534"]

for i in a:
    if re.match(r"[A-Z]+[0-9]",i):
        print(i)
```

    TY76Z

## ? Soru İşareti

`?` metakarakteri, **kendisinden önce gelen karakterin SIFIR veya BİR defa** eşleştiği durumları kapsar. Örneğe bakalım:

```python
yeniliste = ["st", "sat", "saat", "saaat", "falanca"]

for i in yeniliste:
    if re.match(r"sa?t",i):
        print(i)
```

    st
    sat

Şimdi bu metakarakteri kullanarak gerçek hayatta karşımıza çıkabilecek bir örnek verelim. Bu metakarakterin tanımına tekrar bakarsak, **olsa da olur olmasa da olur** diyebileceğimiz durumlar için bu metakarakterin rahatlıkla kullanılabileceğini görürüz. 

Şöyle bir örnek verelim: Diyelim ki bir metin üzerinde arama yapacaksınız. Aradığınız kelime `uluslararası`:

```python
metin = """Uluslararası hukuk, uluslar arası ilişkiler altında bir disiplindir. Uluslararası ilişkilerin hukuksal 
boyutunu bilimsel bir disiplin içinde inceler. Devletlerarası hukuk da denir. Ancak uluslar arası ilişkilere yeni
aktörlerin girişi bu dalı sadece devletlerarası olmaktan çıkarmıştır."""
```

Şimdi yapmak istediğimiz şey `uluslararası` kelimesini bulmak. Ama dikkat ederseniz metin içinde `uluslararası` kelimesi aynı zamanda `uluslar arası` şeklinde de geçiyor. Bizim bu iki kullanımı da kapsayacak bir düzenli ifade yazmamız gerekecek.

```python
nesne = re.findall(r"[Uu]luslar ?arası", metin)

for i in nesne:
    print(i)
```

    Uluslararası
    uluslar arası
    Uluslararası
    uluslar arası

Verdiğimiz düzenli ifade kalıbını dikkatlice inceleyin. Bildiğiniz gibi, `?` metakarakteri, kendinden önce gelen karakterin **sıfır veya bir kez** geçtiği durumları arıyor. Burada `?` sembolünü ` ` karakterinden, yani `boşluk` karakterinden sonra kullandık. Dolayısıyla, *boşluk karakterinin sıfır veya bir kez geçtiği durumları* hedefledik. Bu şekilde hem `uluslar arası` hem de `uluslararası` kelimesini ayıklamış olduk. Düzenli ifademizde ayrıca `[Uu]` yazdık, çünkü metnimiz içinde `uluslararası` kelimesinin büyük harfle başladığı yerler de var. Bildiğiniz gibi, `uluslar` ve `Uluslar` kelimeleri asla aynı değildir. Dolayısıyla hem `u` harfini hem de `U` harfini bulmak için, daha önce öğrendiğimiz `[]` metakarakterini kullanıyoruz.

## {} Küme Parantezi

{ } Küme Parantezi metakarakterimiz yardımıyla **bir eşleşmeden kaç adet istediğimizi** belirtebiliyoruz. Yine aynı örnek üzerinden gidelim:

```python
for i in yeniliste:
    if re.match(r"sa{3}t",i):
        print(i)
```

    saaat

Burada `a` karakterinin **3 kez** tekrar etmesini istediğimizi belirttik. Python da bu emrimizi hemen yerine getirdi.

Bu metakarakterin ilginç bir özelliği daha vardır. Küme içinde iki farklı sayı yazarak, **bir karakterin en az ve en çok** kaç kez tekrar etmesini istediğimizi belirtebiliriz. Örneğin:

```python
for i in yeniliste:
    if re.match(r"sa{0,3}t",i):
        print(i)
```

    st
    sat
    saat
    saaat

`sa{0,3}t` ifadesiyle, `a` harfinin en az sıfır kez, en çok da üç kez tekrar etmesini istediğimiz söyledik. Dolayısıyla, “a” harfinin sıfır, bir, iki ve üç kez tekrar ettiği durumlar ayıklanmış oldu. 

## ^ Şapka

`^` sembolünün iki işlevi var. 

**Birinci işlevi :**

**Çok satırlı (örneğin parafraf) yapısında ya da bir karakter dizisinin en başındaki veriyi sorgulamaktır**. `^` Şapka metakarakteri, düzenli ifadenin **metnin herhangi bir satırının başında uyması durumunu kontrol eder.** Bu metakarakter çok satırlı bir metin içinde kullanılıyorsa, her satırın başındaki kelime ile eşleşme olup olmadığını sorgular. Bunun için `re.M` ya da `re.MULTILINE` ifadesini koda eklemek gerekir. Yani aslında `match()` metodunun varsayılan olarak yerine getirdiği işlevi bu metakarakter yardımıyla `search()` metodunda da kullanabiliyoruz. **Sadece kendinden sonra gelen BİR karaktere BAKMIYOR**.

```python
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', '1agAY54']

for i in a:
    nesne = re.search(r"^[A-Z]+[0-9]",i)
    if nesne:
        print(nesne.group())
```

    TY7

Gördüğünüz gibi, `^` (şapka) metakarakteri `search()` metodunun, karakter dizilerinin sadece en başına bakmasını sağladı. O yüzden de bize sadece, `TY7` çıktısını verdi. 

Aynı kodu, şapkasız olarak, şu şekilde kullanırsak:

```python
for i in a:
    nesne = re.search(r"[A-Z]+[0-9]",i)
    if nesne:
        print(nesne.group())
```

    BH5
    TY7
    Y7
    AY5

Gördüğünüz gibi, `^` şapka sembolü olmadığında `search()` metodu karakter dizisinin tamamını tarıyor. Biz yukarıdaki koda bir `^` sembolü ekleyerek, metodumuzun sadece karakter dizisinin en başına bakmasını istedik. 

Burada dikkatimizi çekmesi gereken başka bir nokta da, `search()` metodundaki çıktının **kırpılmış** olması. Dikkat ettiyseniz, `search()` metodu bize öğenin tamamını vermedi. Öğelerin yalnızca `[A-Z]+[0-9]` kalıbına uyan kısımlarını verdi. Çünkü biz ona tersini söylemedik. Eğer öğelerin tamamını istiyorsak bunu açık açık belirtmemiz gerekir:

```python
for i in a:
    nesne = re.search(r"[A-Z]+[0-9].*",i)
    if nesne:
        print(nesne.group())
```

    BH56
    TY76Z
    Y7UZ
    AY54

Veya metodumuzun karakter dizisinin sadece en başına bakmasını istersek:

```python
for i in a:
    nesne = re.search(r"^[A-Z]+[0-9].*",i)
    if nesne:
        print(nesne.group())
```

    TY76Z

Bu kodlarda düzenli ifade kalıbının sonuna `.*` sembolünü eklediğimize dikkat edin. Böylelikle metodumuzun sonu herhangi bir şekilde biten öğeleri bize vermesini sağladık.

Bir örnek daha yapalım. Bu kez elimde bir liste değil, çok satırlı String ifadesi (metin)  olsun.

```python
import re

metin = """
Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
bir dil denebilir. Ancak Python'un çok uzun bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı
olması, ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden ötürü çoğu kimsenin gözdesi
haline gelmiştir. Ayrıca Google'ın da Python'a özel bir önem ve değer verdiğini, çok iyi derecede Python bilenlere
iş olanağı sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın yaratıcısı Guido Van Rossum 
Google'de işe başladı...
Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında 
yayınlandı. 2008'de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan 
kodların Python 3.x'te çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, 
dilin son sürümü olan Python 2.7.x serisi versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi. 
Python 2.x geliştirilme desteğinin sona ermesinin ardından, Python dilinin 3.7.x ve sonraki sürümlerinin 
geliştirilmesi devam etmektedir.
"""

desen = r"^[Gg].+"

sonuc = re.finditer(desen, metin, re.M)
for s in sonuc:
    print(s.group())
```

`re.M` ifadesi ile çoklu satırları tara demiş olduk. `r"^[Gg].+"` ifadesi ile de her satırın başına baş küçük ya da büyük harfle başlıyorsa satırı ekrana yazdır demiş oluyoruz.

Çıktı:

```python
Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani aslında Python için nispeten yeni
Google'de işe başladı...
geliştirilmesi devam etmektedir.
```

**İkinci İşlevi:**

`^` metakarakterinin, karakter dizilerinin en başına demir atmak dışında başka bir görevi daha vardır: **Hariç tut** anlamına gelmektedir.

**Bu görevini sadece `[]` metakarakterinin içinde kullanıldığı zaman yerine getirir.** Bunu bir örnekle görelim. Yukarıdaki listemiz üzerinde öyle bir süzgeç uygulayalım ki, **1agAY54** öğesi çıktılarımız arasında görünmesin. 

Bu öğeyi avlayabilmek için kullanmamız gereken düzenli ifade şöyle olacaktır: `[0-9A-Z][^a-z]+`

```python
for i in a:
    nesne = re.match(r"[0-9A-Z][^a-z]+",i)
    if nesne:
        print(nesne.group())
```

    23BH56
    TY76Z
    4Y7UZ
    TYUDZ
    34534

Burada şu ölçütlere sahip bir öğe arıyoruz:

1. Aradığımız öğe bir sayı veya büyük harf ile başlamalı
2. En baştaki sayı veya büyük harften sonra küçük harf **GELMEMELİ** (Bu ölçütü “^” işareti sağlıyor)
3. Üstelik bu **“küçük harf gelmeme durumu”** bir veya daha fazla sayıda tekrar etmeli. Yani baştaki sayı veya büyük harften sonra kaç tane olursa olsun asla küçük harf gelmemeli (Bu ölçütü de “+” işareti sağlıyor”)

Bu ölçütlere uymayan tek öğe “1agAY54” olacaktır. Dolayısıyla bu öğe çıktıda görünmez.

Burada, `^` işaretinin nasıl kullanıldığına ve küçük harfleri nasıl dışarıda bıraktığına dikkat edin. Unutmayalım, bu `^` işaretinin **hariç** anlamı sadece `[]` metakarakterinin içinde kullanıldığı zaman geçerlidir.

`^` metakarakterinin `findall` fonksiyonu ile çok satırlı / paragraflı metin içinde kullanımına bir örnek verelim.

```python
import re
metin = """Python (C, C++, Perl, Ruby ve benzerleri gibi) bir programlama dilidir ve tıpkı öteki programlama dilleri gibi, önünüzde duran kara kutuya, yani bilgisayara hükmetmenizi sağlar.
Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
Peki neden piyasada iki farklı Python sürümü var ve bu bizim için ne anlama geliyor?
Python programlama dili 1990 yılından bu yana geliştirilen bir dil. Bu süre içinde pek çok Python programı yazıldı ve insanların kullanımına sunuldu. Şu anda piyasada Python’ın 2.x serisinden bir sürümle yazılmış pek çok program bulunuyor. 3.x serisi ise ancak son yıllarda yaygınlık kazanmaya başladı."""

desen = r"^P\w+"
eslesme = re.findall(desen, metin, re.MULTILINE)

for eslesen in eslesme:
    print(eslesen)
```

Yukarıdaki kodu incelersek; desen ile **P** harfi ile başlayan ve devamında harf gruplarının geldiği tüm kelimelerin tespit edilmeye çalışıldığını görüyoruz. `findall` fonksiyonu içerisinde `re.MULTILINE` ifadesi kullanıldığı için tüm paragraflarda eşleşme aranır. `^` metakarakteri ile **tüm paragrafların başlarında** eşleşme olup olmadığı sorgulanır. Kodun çıktısı aşağıdaki gibidir.

```python
Python
Peki
Python
```

## $ Dolar

`$` metakarakteri, **Çok satırlı desenin ya da dizelerin nasıl biteceğini** belirliyor. Bu sembol arama/eşleştirme işleminin karakter dizisinin en sonuna bakmasını sağlıyor. Bu metakarakter çok satırlı bir metin içinde kullanılıyorsa, her satırın sonundaki kelime ile eşleşme olup olmadığı sorgulanır. Bunun için `re.M` ya da `re.MULTILINE` ifadesini koda eklemek gerekir. **Sadece kendinden önceki BİR karaktere BAKMIYOR**. Hatırlarsınız `^` metakarakteri eşleştirme işleminin karakter dizisinin en başından başlamasını sağlıyordu.

```python
liste = ["at", "katkı", "fakat", "atkı", "rahat", "mat", "yat", "sat", "satılık", "katılım"]
```

Diyelim ki yukarıda tanımlı listeden, **at** hecesiyle biten kelimeleri ayıklamak istiyoruz:

```python
for i in liste:
    if re.search(r"at$",i):
        print(i)
```

    at
    fakat
    rahat
    mat
    yat
    sat

Burada `$` metakarakteri sayesinde aradığımız karakter dizisinin nasıl bitmesi gerektiğini belirleyebildik. Eğer biz **at** ile başlayan bütün öğeleri ayıklamak isteseydik ne yapmamız gerektiğini biliyorsunuz:

```python
for i in liste:
    if re.search(r"^at",i):
        print(i)
```

    at
    atkı

Gördüğünüz gibi, `^` işareti bir karakter dizisinin nasıl başlayacağını belirlerken, `$` işareti aynı karakter dizisinin nasıl biteceğini belirliyor. 

Başka bir örnekle devam edelim. Bu defa  **liste** veri tipi yerine **dizgi/dize (string)** veri tipi kullanalım. Elimizde aşağıdaki şekilde bir metin olduğunu düşünerek `$` metakarakterini inceleyelim.

```python
import re

metin = """Python (C, C++, Perl, Ruby ve benzerleri gibi) bir programlama dilidir ve tıpkı öteki programlama dilleri gibi, önünüzde duran kara kutuya, yani bilgisayara hükmetmenizi sağlar.
Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. 
Dediğimiz gibi, Python bir programlama dilidir. Üstelik pek çok dile kıyasla öğrenmesi kolay bir programlama dilidir. Bu yüzden, eğer daha önce hiç programlama deneyiminiz olmamışsa, programlama maceranıza Python’la başlamayı tercih edebilirsiniz.
Eğer daha önce Python programlama dili ile ilgili araştırma yaptıysanız, şu anda piyasada iki farklı Python serisinin olduğu dikkatinizi çekmiş olmalı. 15.12.2023 tarihi itibariyle piyasada olan en yeni Python sürümleri Python 2.7.18 ve Python 3.12.1’dir.
Eğer bir Python sürümü 2 sayısı ile başlıyorsa (mesela 2.7.15), o sürüm Python 2.x serisine aittir. Yok eğer bir Python sürümü 3 sayısı ile başlıyorsa (mesela 3.7.0), o sürüm Python 3.x serisine aittir."""

desen = r"\w+r\.$"
eslesme = re.findall(desen, metin, re.MULTILINE)

for eslesen in eslesme:
    print(eslesen) 
```

Yukarıdaki kodu incelersek; desen ile öncesinde harf gruplarının geldiği sonrasında ise **r.** ile biten tüm kelimelerin tespit edilmeye çalışıldığını görüyoruz. `findall` fonksiyonu içerisinde `re.MULTILINE` ifadesi kullanıldığı için tüm paragraflarda eşleşme aranır. `$` metakarakteri ile **tüm paragrafların sonlarında** eşleşme olup olmadığı sorgulanır. Kodun çıktısı aşağıdaki gibidir.

```python
sağlar.
dir.
aittir.
```

Dikkat edilmesi gereken bir husus ta şudur ki;

* `^` işareti bir karakter dizisinin başına yazılırken
* `$` işareti karakter dizisinin sonuna yazılırken

## \ Ters Bölü

Bu işaret bildiğimiz **kaçış dizisi**dir. Peki burada ne işi var? Şimdiye kadar öğrendiğimiz konulardan gördüğünüz gibi, Python’daki düzenli ifadeler açısından özel anlam taşıyan bir takım semboller/metakarakterler var. Bunlar kendileriyle eşleşmiyorlar. Yani bir karakter dizisi içinde bu sembolleri arıyorsak eğer, bunların taşıdıkları özel anlam yüzünden bu sembolleri ayıklamak hemencecik mümkün olmayacaktır. Yani mesela biz `$` sembolünü arıyor olsak, bunu Python’a nasıl anlatacağız? Çünkü bu sembolü yazdığımız zaman Python bunu farklı algılıyor. Lafı dolandırmadan hemen bir örnek verelim…

Diyelim ki elimizde şöyle bir liste var:

```python
liste = ["10$", "25€", "20$", "10TL", "25£"]
```

Amacımız bu listedeki **dolarlı** değerleri ayıklamaksa ne yapacağız? Şunu deneyelim önce:

```python
for i in liste:
    if re.match(r"[0-9]+$",i):
        print(i)
```

Python `$` işaretinin özel anlamından dolayı, bizim sayıyla biten bir karakter dizisi aradığımızı zannedecek, dolayısıyla da herhangi bir çıktı vermeyecektir. Çünkü listemizde sayıyla biten bir karakter dizisi yok.

Peki biz ne yapacağız? İşte bu noktada `\` metakarakteri devreye girecek. Hemen bakalım:

```python
for i in liste:
    if re.match(r"[0-9]+\$",i):
        print(i)
```

```python
10$
20$
```

Gördüğünüz gibi, “\” sembolünü kullanarak “$” işaretinin özel anlamından kaçtık.

## | Dik Çizgi, Boru (Pipe) Sembolü

Bu metakarakter, birden fazla düzenli ifade kalıbını birlikte eşleştirmemizi sağlar. `|` sembolü, **VEYA** anlamına gelir diyebiliriz. Yani birkaç alternatif modelden **herhangi birini** eşleştirir. Eşleştirme için birden fazla kriter belirlermek için `|` sembölünü kullanabiliriz. Hemen örnek yapalım:

```python
liste = ["at", "katkı", "fakat", "atkı", "rahat", "mat", "yat", "sat", "satılık", "katılım"]

for i in liste:
    if re.search(r"^at|at$",i):
        print(i)
```

    at
    fakat
    atkı
    rahat
    mat
    yat
    sat

Gördüğünüz gibi `|` metakarakterini kullanarak **at** ile başlayan **ve** biten kelimeleri bulduk / ayıkladık. `|` sembolünü kullanmasaydık ve aşağıdaki ifadesiyi yazsaydık **atat** ile başlayan ve biten kelime aramış olurduk ve sonuç bulamazdık.

```python
for i in liste:
    if re.search(r"^atat$",i):
        print(i)
```

Aşağıdaki ifadesiyi yazmış olsaydık ise **at** ile başlayan ve biten kelime aramış olurduk ve sadece **at** sonucunu elde ederdik.

```python
for i in liste:
    if re.search(r"^at$",i):
        print(i)
```

    at

## ( ) Parantez

Bu metakarakter yardımıyla **düzenli ifade kalıplarını gruplayacağız**. Ayrıca gruplandırılmış ifadelerine denk gelen kalıpları saklar ve en fazla 9 kalıp saklayabilir. Bu metakarakter bizim bir karakter dizisinin istediğimiz kısımlarını ayıklamamızda çok büyük kolaylıklar sağlayacak.

```python
x = ["ali", "veli", "deli", "zeki", "abi"]

for i in x:
    if re.search(r"a(b|l)i", i):
        print(i)
```

    ali
    abi

Parantez ile gruplanan desenler, **bir bütünsel yapı olarak** değerlendirilir. Yani `ha+` kodu yazıldığında `h` harfinden sonra `a` harfinden bir veya daha fazla olması anlaşılırken, `(ha)+` kodu ile `ha` ifadesinden bir veya daha fazla olması istenildiği ifade edilmiş olunur. Bir örnek yapalım;

```python
veri = "ali veli hakiki deli zeki abi samimi"

desen = r"\w+(\w{2}){2}"
sonuc = re.finditer(desen, veri)

for i in sonuc:
    print(i.group())
```

    hakiki
    samimi

```python
veri = ['650-654-7544', 'Mustafa Halil', '650524495', '65080976', '08069114', '656037422', '6504476824', '6508000010',
 '6501552207', '(650)605 09 96', '650-537-82-34', '6503320122', '650_919_64', '650-abc-7425', '6509318724', '6502184706',
 '650-xyz-1653', '6501921596']

for i in veri:
    if re.search(r"(\d{3})-([a-z]{3})-(\d{4})", i):
        print(i)
```

    650-abc-7425
    650-xyz-1653

`r"(\d{3})-([a-z]{3})-(\d{4})"` deseni ile 3 adet grup oluşturduk. Bu desenleri açıklayalım;

* `(\d{3})` = **3 adet rakam**, ardından  
* `-` = **Tire işareti** , ardından
* `([a-z]{3})` = **a'dan z'ye kadar 3 adet küçük harf** , ardından
* `-` = **Tire işareti** ve son olarak
* `(\d{4})` = **4 adet rakam**

dan oluşan bir değer arıyorum.

Şimdi grupları açıklamaya çalışayım.

```python
veri = "08069114 6501552207 650-abc-7425 (650)605 09 96 650-537-82-34 650_919_64 6509318724 650-xyz-1653"

desen = r"(\d{3})-([a-z]{3})-(\d{4})"
eslesen = re.finditer(desen, veri)

for es in eslesen:
    print(es.group())
```

    650-abc-7425
    650-xyz-1653

Görüldüğü üzere aranan desene uygun 2 adet sonuç elde ettik; **650-abc-7425** ve **650-xyz-1653**. 

Parantez içine aldığımız desenlerin her biri **bir grubu ifade ediyor**.  Bu değerleri ekrana yazdırmak için `group()` metodunu kullandık. `group()` metodu ile `group(0)` metodu aynıdır. Desenimizde (parantez içinde) 3 grup olduğu için `group(1), group(2)` ve `group(3)` yöntemiyle, eşleşen 3 gruba ayrı ayrı erişebiliriz. Aşağıdaki kodları inceleyin;

```python
desen = r"(\d{3})-([a-z]{3})-(\d{4})"
eslesen = re.finditer(desen, veri)

print("1. Grup Değerleri:")
for es in eslesen:
    print(es.group(1))
```

    1. Grup Değerleri:
    650
    650

```python
desen = r"(\d{3})-([a-z]{3})-(\d{4})"
eslesen = re.finditer(desen, veri)

print("2. Grup Değerleri:")
for es in eslesen:
    print(es.group(2))
```

    2. Grup Değerleri:
    abc
    xyz

```python
desen = r"(\d{3})-([a-z]{3})-(\d{4})"
eslesen = re.finditer(desen, veri)

print("3. Grup Değerleri:")
for es in eslesen:
    print(es.group(3))
```

    3. Grup Değerleri:
    7425
    1653

Parantez metakarakteri hakkında detaylı bilgiye [Gruplama ve Etikeleme]({filename}re_gruplar.md) sayfasından erişebilirsiniz.
