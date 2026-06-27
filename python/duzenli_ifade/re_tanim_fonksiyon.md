Title: Düzenli İfadeler - Tanım ve Fonksiyonlar
Date: 2023-09-01 00:00
Modified: 2025-10-30 21:22
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül

# Düzenli İfadeler (Regular Expressions)

**Düzenli ifadeler (RegEx ya da Regular Expression)**, bir arama işleminde eşleştirilecek **deseni** temsil eden özel dizelerdir. Bir başka tanımla bir karakter dizisi içinde bulunan, belli bir düzene uyan eşleşmeleri bulmanıza ve yönetmenize yardımcı olacak **desenler** oluşturmanıza izin veren bir metin dizisidir (bir string ifadedir). Bir metinde geçen karakterleri **RegEx desenleri (pattern)** kullanarak arayabiliriz. 

Tanım biraz karmaşık gelmiş olabilir. Ancak kısa bir örnek vererek konuyu açıklamaya çalışayım. Diyelim ki elimizde uzun bir metin var. Bu metin içerisindeki sayıları, telefon numaralarını, e-posta adreslerini, ...vb bir yapıyı otomatik olarak bulmak / tespit etmek isteyelim. Bu durumda bulmak istediğimiz yapıyı temsil eden bir **desen** tanımlayarak metinde eşleşen tüm sonuçları bulabiliriz. Deyatlı açıklama ve örneklerle konuyu daha iyi öğreneceksiniz. 

Düzenli ifadeler **Java** ve **Perl** gibi programlama dillerinden **grep, sed** ve metin düzenleyici **vim** gibi metin işleme araçlarına kadar çok çeşitli bilgi işlem uygulamalarında kullanılan önemli bir araçtır. 

**Düzenli ifadeler sayesinde ne yapabiliriz bir bakalım :**

* **Yer değiştirme:** Belirli parçaları değiştirir. Örnek olarak metin içerisindeki tüm büyük harfleri küçük harf ya da tüm küçük harfleri büyük harfe dönüştürebilirsiniz.

* **Doğrulama :** Yazdığınız bir program olsun, bu programda büyük veya küçük harf, nokta veya rakam gibi kriterleri karşılayıp karşılamadığını kontrol edebilirsiniz.

* **Arama :** Bir metin içerisindeki tüm ögeleri aratabilirsiniz. Örneğin telefon numaraları ya da e-posta adresleri gibi.

* **Koordinat ile hareket etme :** Örneğin, bir dizindeki belirli paketleri, dosyaları işlemek isteyebilirsiniz ancak yalnızca belirli koşulları karşılıyorlarsa, komut satırında çalıştırabiliyorsunuz.

* **Metni Yeniden Biçimlendirme :** Örneğin, Bir programdaki verileri metin dosyası olarak dışa aktarabilir, ardından düzenini değiştirerek metin düzenleyicisi kullanarak başka bir programa aktarabilirsiniz.

Python’daki düzenli ifadelere ilişkin her şey, bir modül içinde tutulur. Bu modülün adı **re**'dir. **re** modülü Python'ın dahili (build-in) modüllerindendir. İlave olarak yüklememize gerek yoktur. Bilgisayarınızda Python yüklü ise, **re modülü** de yüklenmiş ve kullanıma hazır olarak bekliyordur.

Düzenli ifadeleri kullanabilmemiz için öncelikle bu **re** modülünü içe aktarmamız gerekir:

```python
import re
```

## RegEx Fonksiyonları / Metotları

**re** modülü bir veride geçen karakterleri bulmamıza ve değiştirmemize olanak sağlayan bazı fonksiyonlara sahiptir. Bunlar;

| **Fonksiyon / Metot** | **Açıklama**                                                                                                                                                                                                                             |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **match()**           | Karakter dizisinin başında eşleşme olup olmadığını göster. Aranılan desen, stringin başında bulunduğu durumda eşleşmenin konumunu belirten bir eşleşme nesnesi üretir. Herhangi bir eşleşme bulunamadığı durumda **None** değeri üretir. |
| **search()**          | Eşleşme olup olmadığını göster. **match()** fonksiyonu ile aynı işlevi vardır. Yalnızca ilk eşleşmeye dair eşleşme nesnesi üretir.                                                                                                       |
| **findall()**         | Tüm eşleşmeleri gösterir (liste halinde). Aranılan desen string içerisinde bulunduğu durumda, yakaladığı tüm eşleşmeleri liste olarak getirir.                                                                                           |
| **finditer()**        | Belirtilen desenlerin karakter dizileri içerisindeki konumunu bulmak için kullanabiliriz                                                                                                                                                 |
| **split()**           | Aranılan desen string içerisinde bulunduğu durumda, string’i eşleştiği bölgelerden  böler ve bölünmüş halini liste olarak getirir. Herhangi bir eşleşme olmadığı durumda stringin kendisini getirir.                                     |
| **sub()**             | Eşleşmeleri verilen ifade ile değiştir. Aranılan deseni string içerisinde bulduğu durumda, verilen diğer string değeri ile değiştirir.                                                                                                   |
| **subn()**            | Eşleşmeleri verilen ifade ile değiştir, kaç adet değişiklik yapıldığını gösterir                                                                                                                                                         |
| **escape()**          | Bir metni, düzenli ifade içinde kullanılmaya uygun hale getirmek için kullanılır                                                                                                                                                         |
| **compile()**         | Düzenli İfadeleri Derlemek için kullanılır                                                                                                                                                                                               |
| **purge()**           | Düzenli ifade önbelleğini temizlemek için kullanılır                                                                                                                                                                                     |

# Kaynaklar:

Düzenli İfadeler (Regular Expressions) konusu hazırlanırken faydalanılan tüm kaynakları, her sayfada ayrı ayrı belitrmek yerine burada toplu olarak belirtmek istiyorum. 

* [İstihza YazBel](https://python-istihza.yazbel.com/standart_moduller/regex.html)
* [python.sitesi.web.tr](https://python.sitesi.web.tr/python-regex.html)
* [Zeynep ENGİN](https://medium.com/@zeynepengin/regular-expressions-d%C3%BCzenli-i%CC%87fadeler-2e75f44d4f6f)
* [Yakın Kampüs](https://www.youtube.com/watch?v=bKWzIvYZmfA)
* [Python Dersleri- 45 - REGEX (REGULAR EXPRESSION) (2023) - YouTube](https://www.youtube.com/watch?v=V3Jr2sAHNno)
* [ChatGPT](https://chat.openai.com)
