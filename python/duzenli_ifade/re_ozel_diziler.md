Title: Düzenli İfadeler - Ozel Diziler
Date: 2023-09-02 15:40
Modified: 2025-11-06 12:50
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Metakarakter, Ozel Diziler, Özel Diziler

# Özel Diziler

## \s   Boşluk (Space) Karakterinin Yerini Tutan Özel Dizi.

Bu sembol (`\s`), bir karakter dizisi içinde geçen **boşlukları (boşluk, tab ve enter karakterlerini) yakalamak** için kullanılır.

```python
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]

for i in a:
    nesne = re.search("[0-9]\s[A-Za-z]+",i)
    if nesne:
        print(nesne.group())
```

    5 Ocak
    4 Ekim

Yukarıdaki örnekte, bir sayı ile başlayan, ardından bir adet boşluk karakteri içeren, sonra da bir büyük veya küçük harfle devam eden karakter dizilerini ayıkladık. Burada boşluk karakterini `\s` simgesi ile gösterdiğimize dikkat edin.

## \S   Boşluk Karakterinin Dışındaki Karakterlerin Tutan Özel Dizi.

`\S` özel dizisi, **boşluk olmayan karakterleri** yakalar.

```python
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]

for i in a:
    nesne = re.search("\d+\S\w+",i)
    if nesne:
        print(nesne.group())
```

    27Mart

## \d   Rakamların (Digit) Yerini Tutan Özel Dizi.

Bu sembol, bir karakter dizisi içinde geçen **rakamları (ondalık sayıları) eşleştirmek için** kullanılır. `[0-9]` ifadesi ile arasında önemli bir fark vardır. **\d** yazdığımızda, Arapça, Rusça, Çince,...vb dillerdeki rakamları da yakalar, eşleştirir. Çok dilli metinlerle çalışırken bu konuya dikkat etmek gerekir.

Buraya kadar olan örneklerde bu işlevi yerine getirmek için `[0-9]` ifadesinden yararlanıyorduk. Şimdi artık aynı işlevi daha kısa yoldan, `\d` dizisi ile yerine getirebiliriz. İsterseniz yine yukarıdaki örnekten gidelim:

```python
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]

for i in a:
    nesne = re.search("\d\s[A-Za-z]+",i)
    if nesne:
        print(nesne.group())
```

    5 Ocak
    4 Ekim

Burada, `[0-9]` yerine `\d` yerleştirerek daha kısa yoldan sonuca vardık.

## \D  Rakam Olmayan Karakterlerin Yerini Tutan Özel Dizi.

`\D` özel dizisi **rakam (ondalık sayı) olmayan karakterleri** yakalar. Yani `[^0-9]` ile eşdeğerdir.

```python
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]

for i in a:
    nesne = re.search("\D+",i)
    if nesne:
        print(nesne.group())
```

     Ocak
    Mart
     Ekim
    Nisan 

```python
for i in a:
    nesne = re.search("\s\D+",i)
    if nesne:
        print(nesne.group())
```

     Ocak
     Ekim

## \w   Alfanümerik Karakterlerin Yerini Tutan Özel Dizi.

Bu sembol, bir karakter dizisi içinde geçen **alfanümerik karakterleri (harf, rakam) ve buna ek olarak alt çizgi karakterini** `_` bulmak için kullanılır. 

Bu özel dizi şu ifadeyle aynı anlama gelir: `[a-zA-Z0-9_]`. Bu ifadeyi yazmaktansa `\w` yazmanın ne kadar kolay olduğu ortada.

```python
a = "abc123_$%+"
print(re.search("\w*", a).group())
```

    abc123_

## \W   Alfanümerik Karakterlerin Dışındaki Karakterlerin Yerini Tutan Özel Dizi.

Bu sembol **Harf, rakam ve alt çizgi karakteri dışında** herhangi bir şeyle eşleşir. 

Bu özel dizi şu ifadeyle aynı anlama gelir: `[^a-zA-Z0-9_]` ile eşdeğerdir

```python
b = ["abc", "123", "$%+"]

for i in b:
    print(re.search("\W*", i).group())
```

    $%+

Şimdi bu özel diziler için genel bir örnek verip konuyu kapatalım.

```python
veriler = [ "esra : istinye 05331233445", 
            "esma : levent 05322134344", 
            "sevgi : dudullu 05354445434", 
            "kemal : sanayi 05425455555", 
            "osman : tahtakale 02124334444",
            "metin : taksim 02124344332"]
```

Amacımız bu listede yer alan isim ve telefon numaralarını `isim > telefon numarası` şeklinde almak:

```python
for veri in veriler:
    nesne = re.search(r"(\w+)\s+:\s(\w+)\s+(\d+)",veri)
    if nesne:
        print("{} > {}".format(nesne.group(1), nesne.group(3)))
```

    esra > 05331233445
    esma > 05322134344
    sevgi > 05354445434
    kemal > 05425455555
    osman > 02124334444
    metin > 02124344332

Burada formülümüz şu şekilde: `Bir veya daha fazla karakter` + `bir veya daha fazla boşluk` + `’:’ işareti` + `“bir adet boşluk` + `bir veya daha fazla sayı`

**.format** biçimi kullanmak zorunda değiliz, aynı çıktıya aşağıdaki kod ile de ulaşabiliriz;

```python
for veri in veriler:
    nesne = re.search(r"(\w+)\s+:\s(\w+)\s+(\d+)",veri)
    if nesne:
        print(nesne.group(1), ">", nesne.group(3))
```

**Çıktı**:

```python
esra > 05331233445
esma > 05322134344
sevgi > 05354445434
kemal > 05425455555
osman > 02124334444
metin > 02124344332
```

## \A Metin Başında Eşleşme Kontrolü

`\A` meta karakteri, **bir düzenli ifadenin (string ifade çok satırlı da olsa) yalnız başlangıcı ile eşleşme olup olmadığını tespit eder.** Başka bir deyişle, `\A` ifadesi sadece tüm metnin başlangıcında eşleşmeye çalışır. `^` (şapka) metakarakteri ile tüm paragraf başlarında eşleşme olup olmadığı kontrol edilirken `\A` ile sadece metnin en baş kısmına bakılır. 

`\A` metakarakterinin `findall` fonksiyonu ile (çok satırlı / paragraflı metin içinde) kullanımına bir örnek verelim.

```python
import re
metin = """Python (C, C++, Perl, Ruby ve benzerleri gibi) bir programlama dilidir ve tıpkı öteki programlama dilleri gibi, önünüzde duran kara kutuya, yani bilgisayara hükmetmenizi sağlar.
Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
Peki neden piyasada iki farklı Python sürümü var ve bu bizim için ne anlama geliyor?
Python programlama dili 1990 yılından bu yana geliştirilen bir dil. Bu süre içinde pek çok Python programı yazıldı ve insanların kullanımına sunuldu. Şu anda piyasada Python’ın 2.x serisinden bir sürümle yazılmış pek çok program bulunuyor. 3.x serisi ise ancak son yıllarda yaygınlık kazanmaya başladı."""

desen = r"\AP\w+"
eslesme = re.findall(desen, metin, re.MULTILINE)

for eslesen in eslesme:
    print(eslesen)
```

Yukarıdaki kodu incelersek; desen, **P** harfi ile başlayan ve devamında alfanümerik harf gruplarının geldiği tüm kelimelerin tespit edilmeye çalışıldığını görüyoruz. `findall` fonksiyonu içerisinde `re.MULTILINE` ifadesi kullanılmasına rağmen `\A` metakarakteri tüm paragraflarda eşleşme aramaz, sadece metnin başını kontrol eder. Kodun çıktısı aşağıdadır.

```python
Python
```

## \Z Metin Sonunda Eşleşme Kontrolü

`\Z` metakarakteri, **dizelerin (stringlerin) sonunda eşleşme olup olmadığını sorgulamak için kullanılır.** Bu sembol arama/eşleştirme işleminin karakter dizisinin en sonuna bakmasını sağlıyor. Bu metakarakter çok satırlı bir metin içinde kullanılıyorsa, **sadece metnin en sonuna, son satırın sonuna bakar, her satırın sonundaki kelime ile eşleşme olup olmadığına bakmaz.** Çok satırlı metinde eşleştirme yapmak için `re.M` ya da `re.MULTILINE` ifadesini koda eklemek gerekir. **Sadece kendinden önceki BİR karaktere BAKMIYOR**. Hatırlarsınız `^` metakarakteri eşleştirme işleminin karakter dizisinin en başından başlamasını sağlıyordu.

Bir örnek verelim;

```python
import re

metin = """Python (C, C++, Perl, Ruby ve benzerleri gibi) bir programlama dilidir ve tıpkı öteki programlama dilleri gibi, önünüzde duran kara kutuya, yani bilgisayara hükmetmenizi sağlar.
Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. 
Dediğimiz gibi, Python bir programlama dilidir. Üstelik pek çok dile kıyasla öğrenmesi kolay bir programlama dilidir. Bu yüzden, eğer daha önce hiç programlama deneyiminiz olmamışsa, programlama maceranıza Python’la başlamayı tercih edebilirsiniz.
Eğer daha önce Python programlama dili ile ilgili araştırma yaptıysanız, şu anda piyasada iki farklı Python serisinin olduğu dikkatinizi çekmiş olmalı. 15.12.2023 tarihi itibariyle piyasada olan en yeni Python sürümleri Python 2.7.18 ve Python 3.12.1’dir.
Eğer bir Python sürümü 2 sayısı ile başlıyorsa (mesela 2.7.15), o sürüm Python 2.x serisine aittir. Yok eğer bir Python sürümü 3 sayısı ile başlıyorsa (mesela 3.7.0), o sürüm Python 3.x serisine aittir."""

desen = r"\w+r\.\Z"       

eslesme = re.findall(desen, metin, re.MULTILINE)

for eslesen in eslesme:
    print(eslesen)
```

Yukarıdaki kodu incelersek; desen ile öncesinde alfanümerik harf gruplarının geldiği sonrasında ise **r.** ile biten kelimelerin tespit edilmeye çalışıldığını görüyoruz. `findall` fonksiyonu içerisinde `re.MULTILINE` ifadesi kullanılmasına rağmen tüm paragraflarda eşleşme aranmaz. `\Z` metakarakteri ile **sadece son paragrafın bitiminde** eşleşme olup olmadığı sorgulanır. Kodun çıktısı aşağıdaki gibidir.

```python
aittir.
```

Eğer desende `\Z` yerine `$` karakteri kullanılsaydı, sonuç nasıl olurdu, inceleyelim.

```python
desen = r"\w+r\.$"       

eslesme = re.findall(desen, metin, re.MULTILINE)

for eslesen in eslesme:
    print(eslesen)
```

**Çıktı**:

```textile
sağlar.
dir.
aittir.
```

## \b Kelime Sınırını Belirten Özel Dizi

`\b` sembolü ile Kelimenin nasıl **başlaması**, nasıl **bitmesi** ya da tam olarak **sınırlarının ne olması** gerektiğini belirtebiliriz.

```python
veri = "Doğum günüm 01.02.1980. Ağabeyim Doğum günü ise 03.04.1975'te doğdu. Bilgisayarın ip adresi 04.05.18741'dir."
desen = r"\b[A-Z]\w+"
b_harf = re.findall(desen, veri)

print(b_harf)
```

    ['Doğum', 'Ağabeyim', 'Doğum', 'Bilgisayarın']

Büyük harf ile başlayan kelimeleri görmek istediğimizde yukarıdaki deseni kullanabiliriz.

Cümle sonlarını bulmak için ise aşağıdaki (nokta ve boşluktan oluşan) desen işimize yarayabilir.

```python
desen = r"\w+\.\s\b"
cumle_sonu = re.findall(desen, veri)

print(cumle_sonu)
```

    ['1980. ', 'doğdu. ']

```python
veri = "Doğum günüm 01.02.1980. ağabeyim ise 03.04.1975'te doğdu. bilgisayarımın ip adresi 04.05.18741'dir."

desen = r"\d{2}\.\d{2}\.\d{4}"
d_gunleri = re.findall(desen, veri)

print(d_gunleri)
```

    ['01.02.1980', '03.04.1975', '04.05.1874']

Görüldüğü gibi desene uygun sonuçlar aldık ancak çıktıdaki son değer, doğum günü olmamasına rağmen desenle eşleşti. Bu sorunu çözmek için, deseni başlangıç ve bitiş sınırlarını belirterek tanımlamalıyız. Yani desenin başına ve sonuna `\b` sembolünü eklemeliyiz.

```python
desen = r"\b\d{2}\.\d{2}\.\d{4}\b"
d_gunleri = re.findall(desen, veri)

print(d_gunleri)
```

    ['01.02.1980', '03.04.1975']

Desenin başına ve sonuna `\b` sembolünü ekleyerek, kelimenin tüm sınırlarını tanımlamış olduk. Bu desen ile; Kelime başında 2 adet rakam, ardından 1 nokta (.) sonrasında tekrar 2 adet rakam ve ardından nokta (.) gelsin son olarak ta 4 adet rakam olsun demiş olduk. Bu desen sayesinde **04.05.18741** değerini safdışı bırakış olduk.

Eğer verimizde tarih yazım biçimi farklı (örneğin nokta (.) ve taksim, bölü (/) işareti) olan birden fazla değerler olsaydı nasıl bir yol izlemeliydik? Buna da bir örnek verelim.

```python
veri = "Doğum günüm 01.02.1980. ağabeyim ise 03/04/1975'te doğdu. bilgisayarımın ip adresi 04.05.18741'dir."

desen = r"\b\d{2}[./]\d{2}[./]\d{4}\b"
d_gunleri = re.findall(desen, veri)

print(d_gunleri)
```

    ['01.02.1980', '03/04/1975']

Gördüğünüz gibi nokta (.) ve taksim nam-ı diğer bölü (/) işaretini, köşeli parantez içerisine yazarak alternatif seçenekler oluşturmuş olduk.

**NOT:** **Nokta işaretini** desen içinde doğrudan yazarken kaçış dizisi olan ters taksim işaretini yazmamız gerekiyor. Oysa köşeli parantez içerisinde yazdığımızda kaçış dizini olan ters bölü işaretini kullanmıyoruz. Bu, Köşeli parantezin bir özelliğidir. Diğer sembolleri de nokta gibi yazabiliyoruz.

## \B Özel Dizisi

`\b` özel dizisinin tam tersidir.

Örneğin `py\b` deseni, **py** ile biten dizilerle eşleşirken `py\B` deseni,    **py** ifadesini içeren ancak **py** ile **BİTMEYENLERLE** eşleşir. 

```python
metin = "Recep Ramazan Seher (Halil) Sertaç Halili zaman erkek Halil. şeker 2.345 python, py3, py2 py py. py!"
desen = r"\w+er\b" # başında alfanümerik karakterler olan sonu "er" ile biten kelimeleri bul.

print(re.findall(desen, metin))
```

    ['Seher', 'şeker']

`"\w+er\b"` deseni ile, başında alfanümerik karakterler olan sonu **er** ile biten kelimeleri bulmaya çalıştık.

```python
liste = ['Recep', 'Ramazan', 'Seher', '(Halil)', 'manzara',	'Sertaç', 
		'Halili', 'zaman', 'erkek', 'Halil.', 'şeker', '2.345',
		'python,', 'py3,', 'py2', 'py', 'py.', 'py!']

desen = r"er\B" 

for oge in liste:
    if re.search(desen, oge):
        print(oge)
```

    Sertaç
    erkek

`"er\B"` deseni ile, içinde **er** ifadesi **olan** ancak sonu **er** ile **bitmeyen** kelimeleri bulmaya çalıştık.

```python
desen = r"\Ber\B" 

for oge in liste:
    if re.search(desen, oge):
        print(oge)
```

    Sertaç

`"\Ber\B"` deseni ile, içinde **er** ifadesi **olan** ancak başında ve sonunda **er** ifadesi **bulunmayan** kelimeleri bulmaya çalıştık.
