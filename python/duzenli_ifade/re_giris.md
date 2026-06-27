Title: Düzenli İfadeler
Date: 2023-09-01 00:00
Modified: 2025-10-30 20:11
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül

# Düzenli İfadeler (Regular Expressions - Regex )

Aşağıda detaylı olarak anlatılan Düzenli İfade konusunun Özet Tablosuna (Cheat Sheet) [BURADAN]({filename}re_ozet_tablo.md) erişebilirsiniz.

![regex](../../images/python/regex.png)

### Düzenli İfadeler (Regular Expressions) Nedir ?

> Düzenli ifadeler (Regular Expressions, kısaca "Regex" ya da "Regexp"), Python programlama dilinin en çetrefilli konularından biridir. Ama bütün zorluklarına rağmen programlama deneyimimizin bir noktasında mutlaka karşımıza çıkacak olan bu yapıyı öğrenmemizde büyük fayda var. Düzenli ifadeleri öğrendikten sonra, elle yapılması saatler sürecek bir işlemi saliseler içinde yapabildiğinizi gördüğünüzde eminim düzenli ifadelerin ne büyük bir nimet olduğunu siz de anlayacaksınız. 

> Peki, düzenli ifadeleri kullanarak neler yapabiliriz? Çok genel bir ifadeyle, bu yapıyı kullanarak metinleri veya karakter dizilerini parmağımızda oynatabiliriz. Örneğin bir web sitesinde dağınık halde duran verileri bir çırpıda ayıklayabiliriz. Bu veriler, mesela, toplu halde görmek istediğimiz web adreslerinin bir listesi olabilir. Bunun dışında, örneğin, çok sayıda belge üzerinde tek adımda istediğimiz değişiklikleri yapabiliriz.

> Ancak <u>genel bir kural olarak, düzenli ifadelerden kaçabildiğimiz müddetçe kaçmamız gerekir. Eğer Python’daki karakter dizisi metotları, o anda yapmak istediğimiz şey için yeterli geliyorsa mutlaka o metotları kullanmalıyız.</u> Çünkü karakter dizisi metotları, düzenli ifadelere kıyasla hem daha basit, hem de çok daha hızlıdır. Ama bir noktadan sonra karakter dizilerini kullanarak yazdığınız kodlar iyice karmaşıklaşmaya başlamışsa, kodların her tarafı **if** deyimleriyle dolmuşsa, hatta basit bir işlemi gerçekleştirmek için yazdığınız kod sayfa sınırlarını zorlamaya başlamışsa, işte o noktada artık düzenli ifadelerin dünyasına adım atmanız gerekiyor olabilir. 
> 
> Kaynak: [Düzenli İfadeler - Yazbel Python Belgeleri](https://python-istihza.yazbel.com/standart_moduller/regex.html)

# Konu Başlıkları

## [Düzenli İfade Metotları (Fonksiyonları)]({filename}re_tanim_fonksiyon.md)

... [**match() Metodu**]({filename}re_fonk_match.md) 

...... *span() Metodu*

...... *string Özelliği*

...... *group() Metodu*

... [**search() Metodu**]({filename}re_fonk_search.md)

...... *start() Metodu*

...... *end() Metodu*

... [**findall() Metodu**]({filename}re_fonk_findall.md)

... [**finditer() Metodu**]({filename}re_fonk_finditer.md)

...... *span() Metodu*

...... *group() Metodu*

... [**sub() Metodu**]({filename}re_fonk_sub.md)

...... *sub() ve compile() metotlarının birlikte kullanımı*

...... *argüman olarak fonksiyon kullanmak*

...... *sub() fonksiyonunun, dosya işlemleri ile kullanımı*

... [**subn() Metodu**]({filename}re_fonk_subn.md)

... [**split() Metodu**]({filename}re_fonk_split.md)

... [**compile() Metodu**]({filename}re_fonk_compile.md)

... [**escape() Metodu**]({filename}re_fonk_escape.md)

... [**purge() Metodu**]({filename}re_fonk_purge.md)

## MetaKarakterler, Özel Dizinler ve Bayraklar

... [**Meta Karakterler**]({filename}re_metakarakterler.md)

...... **[ ]** Köşeli Parantez

...... **.** Nokta

...... ***** Yıldız

...... **+** Artı

...... **?** Soru İşareti

...... **{ }** Küme Parantezi

...... **^** Şapka

...... **$** Dolar

...... \ Ters Bölü

...... **|** Dik Çizgi, Boru (Pipe) Sembolü

...... **( )** Parantez 

... [**Özel Diziler**]({filename}re_ozel_diziler.md)

...... \s

...... \S

...... \d

...... \D

...... \w

...... \W

...... \A

...... \Z

...... \b

...... \B

... [**Bayraklar (Flags)**]({filename}re_bayraklar.md)

...... *re.IGNORECASE* veya *re.I*

...... *re.MULTILINE veya re.M*

...... *re.DOTALL* veya *re.S*

...... *re.UNICODE veya re.U*

...... *re.VERBOSE veya re.X*

...... *Bayrakların Birlikte Kullanımı (re.M | re.I)*

## [Gruplama ve Etikeleme]({filename}re_gruplar.md)

... group() metodu

... groups() metodu

... (?P<...> ile Etiketleme

... Lookahead (İleriye bak)

...... *(?= ...) Pozitif Lookahead*

...... *(?! ...) Negatif Lookahead*

... Look Behind (Geriye bak)

...... *(?<=...) Pozitif Lookbehind*

...... *(?<!...) Negatif Lookbehind*

... Sonuç

# Kaynaklar:

Düzenli İfadeler (Regular Expressions) konusu hazırlanırken faydalanılan tüm kaynakları, her sayfada ayrı ayrı belirtmek yerine burada toplu olarak sunmak istiyorum. 

* [İstihza YazBel](https://python-istihza.yazbel.com/standart_moduller/regex.html)
* [python.sitesi.web.tr](https://python.sitesi.web.tr/python-regex.html)
* [Zeynep ENGİN](https://medium.com/@zeynepengin/regular-expressions-d%C3%BCzenli-i%CC%87fadeler-2e75f44d4f6f)
* [Yakın Kampüs](https://www.youtube.com/watch?v=bKWzIvYZmfA)
* [gkandemi/regex: Düzenli ifadeler](https://github.com/gkandemi/regex)
* [Python Dersleri- 45 - REGEX (REGULAR EXPRESSION) (2023)](https://www.youtube.com/watch?v=V3Jr2sAHNno)
* [ChatGPT](https://chat.openai.com)
