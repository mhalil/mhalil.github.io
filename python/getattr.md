Title: Python - getattr fonksiyonu
Date: 2025-11-21 12:12
Category: Cesitli
Tags: Python, getattr, Fonksiyon
Author: Mustafa Halil

# `getattr()` Fonksiyonu

`getattr()` fonksiyonu, Python'da **bir nesnenin, adı belirtilen özniteliğinin değerini dinamik olarak almak için** kullanılan yerleşik bir fonksiyondur. Bu fonksiyon, öznitelik adlarının çalışma zamanında (runtime) belirlendiği durumlarda veya metodları dinamik olarak çağırmak gerektiğinde kullanılır.

İşte `getattr()` işlevinin temel sözdizimi ve dönüş mekanizmaları:

## Sözdizimi:

`getattr()` fonksiyonu iki ana imza ile kullanılabilir, bunlardan ikincisi isteğe bağlı bir `default` (varsayılan) değer içerir:

```python
getattr(object, name)
getattr(object, name, default)
```

veya genel olarak:

```python
getattr(object, name[, default]) [1]
```

## Parametreler

`getattr()` işlevi üç ana parametre kabul eder:

1. **object** **(Nesne):** Özniteliğin değerini almak istediğiniz nesnedir.

2. **name** **(Ad/Öznitelik):** Alınmak istenen özniteliğin adını belirten bir dizedir (string).

3. **default** **(Varsayılan):** Bu parametre isteğe bağlıdır. Eğer adlandırılmış öznitelik nesnede mevcut değilse, `getattr()` işlevi bu varsayılan değeri döndürür.

## Dönüş Mekanizmaları

`getattr()` fonksiyonunun dönüş değeri, istenen özniteliğin varlığına ve isteğe bağlı `default` parametresinin sağlanıp sağlanmadığına bağlıdır:

1. **Öznitelik Mevcutsa:**

    ◦ `getattr()` fonksiyonu, adı belirtilen özniteliğin **değerini döndürür**.

    ◦ Dinamik erişim için önemli bir not; **Bir metodun da nesnenin bir özniteliği olmasıdır**. Dolayısıyla, `getattr()` bir metot adına uygulandığında, metodu döndürür ve bu metot daha sonra dinamik olarak çağrılabilir.

Python'da metotlar, özel bir tür olsalar da, tıpkı değişkenler gibi bir nesneye ait olan öznitelikler (attribute) olarak kabul edilir.

Bu temel kural şunları ifade eder:

* **Nokta Gösterimi:** Normalde bir metodu `nesne.metot_adi()` şeklinde çağırırsınız. Bu, aslında nesnenin `metot_adi` özniteliğine eriştiğiniz ve ardından bu özniteliği çalıştırdığınız (parantezlerle çağırdığınız) anlamına gelir.

* **getattr()** **Gösterimi:** `getattr(nesne, "metot_adi")` kullandığınızda, `getattr()` fonksiyonu, nesne içinde bu dize adına sahip olan özniteliği arar. Bu öznitelik bir metot olduğunda, `getattr()` işlevi metodu çağırmaz, bunun yerine **metodun kendisini (metot objesini)** döndürür.

Bu durum, `getattr()` işlevinin metotları dinamik olarak erişilebilir ve daha sonra yürütülebilir hale getirmesini sağlar.

2. **Öznitelik Mevcut Değilse:**

    ◦ **Eğer** **default** **değeri sağlanmışsa:** Fonksiyon, `default` olarak belirtilen değeri döndürür. Bu, istisnayı önlemenin bir yoludur. Örneğin, mevcut olmayan bir öznitelik için `None` varsayılan değer olarak geçilebilir.

    ◦ **Eğer** **default** **değeri atlanmışsa (belirtilmemişse):** Fonksiyon, bir `AttributeError` istisnası (hata) yükseltir.

**Özetle,** `getattr()` işlevi, öznitelik adına dinamik olarak bir dize aracılığıyla erişilmesini sağlayarak, programın öznitelik adlarını çalışma zamanında oluşturabilmesine olanak tanır. Bu, doğrudan `member.name` gibi nokta gösterimiyle erişime benzer bir sonuç verir, ancak öznitelik adının değişken olmasını sağlar.

Bu mekanizma, bir nesnedeki bir özelliğe ulaşmak için kullandığınız adrese bir postacı göndermeye benzer; adresi (öznitelik adını) bir mektup (dize) olarak sağlarsınız. Eğer adres doğruysa (öznitelik varsa), size o adresteki içeriği (öznitelik değeri) getirir. Eğer adres hatalıysa, postacı geri döner ve size bir hata bildirimi (varsayılan değer) veya bir istisna (`AttributeError`) verir.

## Örnekler

Konuyu örneklerle inceleyelim.

```python
class Personel:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

kullanici1 = Personel("Yusuf", 25)
```

**kullanici1** adında  bir nesne oluşturup `ad` olarak **Yusuf**, `yaş` olarak ta **25** değerini atıyoruz.

Şimdi **kullanici1**'in `ad` ve `yaş` bilgilerini `getattr()` fonksiyonu yardımıyla elde edelim.

```python
print(getattr(kullanici1, "ad"))
print(getattr(kullanici1, "yas"))
```

Çıktı:

```python
Yusuf
25
```

**kullanici1** nesnesinin `meslek` bilgisini (özniteliğini) sorgulayalım. Eğer böyle bir bilgi yoksa `None` değeri dönmesini isteyelim.

```python
print(getattr(kullanici1, "meslek", None))
```

Çıktı:

```python
None
```

Bulamadığı öznitelik karşısında `None` değeri yerine kendi mesajımızı da döndürebiliriz;

```python
print(getattr(kullanici1, "boy", "Bu bilgi mevcut değil"))
```

Çıktı:

```python
Bu bilgi mevcut değil
```

Bir sınıfa ait fonksiyonu, `getattr()` içerisinde nasıl kullanabiliriz derseniz;

```python
class AI:
   def genAI(self):
      return "This is your prompt"

chatGpt = AI()
output = getattr(chatGpt, "genAI")
print("The chat GPT wrote:", output())
```

Çıktı:

```python
The chat GPT wrote: This is your prompt
```

Aşağıdaki örnekte gösterildiği gibi, `getattr()` fonksiyonunu `for` döngüsü içinde kullanarak verilen bir özniteliklerin değerine erişebiliriz.

```python
info = ["name", "emp_id", "status"]

class Emp:
   def __init__(self, name, emp_id, status):
      self.name = name
      self.emp_id = emp_id
      self.status = status

emp = Emp("Ansh", 30, "Present")
print("The information of Employee:")
for i in info:
   print(getattr(emp, i))
```

Çıktı:

```python
The information of Employee:
Ansh
30
Present
```

Bir başka örnek;

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

cars = [
    Car("Toyota", "Corolla", 2020),
    Car("Ford", "Mustang", 2018),
    Car("Tesla", "Model S", 2022)
]

for car in cars:
    print(getattr(car, "brand", "Unknown"))
```

Çıktı:

```python
Toyota
Ford
Tesla
```

**Dinamik Çağırma Mekanizması**

```python
class Validation:
    ERRORS = { 
        'required' : 'The {} is required', 
        'email' : 'The {} is not a valid email address' 
    }
    # ... required() ve email() metotları burada tanımlı ... [10]

    def validate(self, data, rules):
        errors = {}
        for field, rule in rules.items():
            # 1. Kural Adını Metoda Dönüştürme
            # Örneğin, 'required' dizesi, self.required metoduna dönüşür.
            is_valid_method = getattr(self, rule) # [9, 11]

            # 2. Metodu Dinamik Olarak Çağırma
            if not is_valid_method(data[field]):
                errors[field] = self.ERRORS[rule].format(field)
        return errors
```

Bu örnekte, `getattr(self, rule)` satırı:

• `rule` dizesini alır (`'required'` veya `'email'`).

• `Validation` nesnesi içindeki ilgili metodu bulur ve döndürür.

• Dönen metot, `is_valid_method(data[field])` ile anında çağrılarak dinamik akış sağlar.

Bu sayede, hangi doğrulama metodunun çağrılacağı kodu statik olarak yazmak yerine, çalışma zamanında kurallar sözlüğünden okunabilir.

**Konuyu detaylı incelersek;**

Dinamik metot çağırma işlemi iki ayrı aşamada gerçekleşir:

**A. Aşama: Metodu Dize Adıyla Alma (Retrieval)**

Bu aşamada, metot çalışma zamanında (runtime) belirlenen bir dize adı kullanılarak nesneden alınır ve bir değişkene atanır.

**Sözdizimi:**

```
is_valid_method = getattr(self, rule)
```

• **self**: Metodu içeren nesnedir (genellikle bir sınıf örneği).

• **rule**: Çağrılacak metodun adını içeren dizedir (örneğin: `'required'` veya `'email'`).

• **is_valid_method**: Bu değişken artık doğrudan `required()` veya `email()` metodunun kendisine referans veren bir metot objesidir.

**B. Aşama: Alınan Metodu Çalıştırma (Execution)**

Metot objesi bir değişkene atandıktan sonra, bu değişken normal bir fonksiyon gibi parantezlerle çağrılabilir ve argümanları iletilebilir.

**Sözdizimi:**

```
is_valid_method(data[field])
```

Bu, programın hangi metodu çağıracağını *derleme zamanında* değil, *çalışma zamanında* karar vermesini sağlar.

Pratik Örnek: Dinamik Doğrulama Sınıfı

Kaynaklarda detaylı olarak açıklanan `Validation` (Doğrulama) sınıfı örneği, bu dinamiğin en net uygulamasını gösterir.

**Senaryo:** Bir `rules` sözlüğünde, hangi alan için hangi doğrulama kuralının (metodunun) kullanılacağı dize olarak tutulur (`'required'`, `'email'`).

**Uygulama Adımları (Kaynaklara göre):**

1. **Kuralları Yineleme:** `validate()` metodu, `rules` sözlüğünde (alan adı, kural adı) çiftlerini yineler (döngüye alır).

2. **Metodu Bulma:** Her bir döngüde, kural adını (`rule`) kullanarak `getattr()` işlevi çağrılır:

3. *Eğer* *rule* *dizesi* *'required'* *ise,* *getattr()* *işlevi* *self.required* *metodunu döndürür.* *Eğer* *rule* *dizesi* *'email'* *ise,* *getattr()* *işlevi* *self.email* *metodunu döndürür*.

4. **Metodu Çağırma:** Dönen metot objesi (`is_valid_method`), hemen ardından `data[field]` üzerindeki veriyi doğrulamak için çağrılır:

Bu yöntem sayesinde, doğrulama kurallarını eklemek veya kaldırmak için `validate()` metodunun içeriğini değiştirmeye gerek kalmaz; sadece kural adlarının dize olarak tutulduğu `rules` sözlüğünü ve ilgili metotları güncellemek yeterli olur. Bu, kodun esnekliğini (flexibility) artırır.

## Gizli Metotlara Erişim

Bir `HesapMakinesi` sınıfımızın olduğunu ve yalnızca dahili süreçler için kullanılmasını istediğimiz gizli bir `_carp()` (çarpma) metodumuz olduğunu varsayalım. Dışarıdan sadece `islem_yap()` metodu ile erişim sağlamak istiyoruz, ancak hangi işlemin yapılacağını dinamik olarak belirliyoruz.

```python
class HesapMakinesi:
    def __init__(self):
        # Varsayılan değer
        pass

    # Gizli (internal/private) metot:
    def _carp(self, a, b):
        """Bu metot sadece dahili kullanıma yönelik tasarlanmıştır."""
        return a * b

    # Gizli olmayan (public) metot:
    def topla(self, a, b):
        return a + b

    def dinamik_islem(self, islem_adi, a, b):
        # Gizli metot adını oluşturma: "carp" -> "_carp"
        gizli_metot_adi = f"_{islem_adi}" 

        # 1. getattr() ile dinamik olarak gizli metodu al:
        # getattr(self, '_carp')
        try:
            islem_metodu = getattr(self, gizli_metot_adi)

            # 2. Elde edilen metodu çağır:
            return islem_metodu(a, b)

        except AttributeError:
            return f"Hata: '{islem_adi}' isimli gizli bir işlem bulunamadı."
```

Önce `islem` nesnemizi olusturalım ardından gizli metoda erişelim.

```python
# Kullanım
islem = HesapMakinesi()

# Gizli metoda dinamik erişim ve çağırma:
# 'carp' dizesi, içeride _carp metoduna dönüştürülüyor.
sonuc = islem.dinamik_islem("carp", 5, 4) 

print(f"Çarpma Sonucu (Dinamik Gizli Erişim): {sonuc}")
```

Çıktı:

```python
Çarpma Sonucu (Dinamik Gizli Erişim): 20
```

**Kodun Açıklaması / Özeti:**

1. **Gizleme Kuralı:** Python'da, bir özniteliğin veya metodun önüne tek bir alt çizgi (`_`) getirilmesiyle (örneğin `_carp`), o öznitelik veya metot "özel" (private) olarak işaretlenir.

2. **Dinamik İsim Oluşturma:** `dinamik_islem` metodu içinde, harici olarak verilen dize adının (`'carp'`) başına alt çizgi eklenerek metot adı dize olarak oluşturulur (`'_carp'`). Bu, kaynaklarda gösterildiği gibi metot adının alt çizgiyle (`f'_{rule}'`) öneki yapılmasına benzer.

3. **getattr()** **Kullanımı:** `getattr(self, gizli_metot_adi)` ifadesi, oluşturulan bu dizeyi kullanarak nesne (`self`) içindeki **tam olarak adlandırılmış** gizli metodu (`_carp`) dinamik olarak bulur ve döndürür.

4. **Çağırma:** Dönen metot (`islem_metodu`), ardından normal bir fonksiyon gibi çağrılabilir (`islem_metodu(a, b)`).

Böylece, `getattr()` sayesinde, program metotların adlarını çalışma zamanında dize olarak birleştirerek, normalde dahili kullanım için tasarlanmış olan metotlara dahi esnek bir şekilde erişim sağlamış olur.

## Kaynaklar:

* [getattr() | Python’s Built-in Functions – Real Python](https://realpython.com/ref/builtin-functions/getattr/)
* [How to Dynamically Call a Python Object Method with Arguments Using getattr — pythontutorials.net](https://www.pythontutorials.net/blog/call-a-method-of-an-object-with-arguments-in-python/)
* [Python&#x27;s getattr function - Python Morsels](https://www.pythonmorsels.com/getattr-function/)
* [Python getattr() Function](https://www.tutorialspoint.com/python/python_getattr_function.htm)
* [Google NotebookLM](https://notebooklm.google.com/)
