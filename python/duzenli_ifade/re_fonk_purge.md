Title: Düzenli İfadeler - purge
Date: 2023-09-01 00:00
Modified: 2025-11-02 15:16
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Purge

# purge() Fonksiyonu

`purge()` metodu, **düzenli ifade (regex) önbelleğini temizlemek için kullanılır**. `re` modülü, derlenmiş düzenli ifade desenlerini ve ilgili verileri bir önbellekte saklar. Bu önbellek, aynı desenleri tekrar tekrar derlememek ve performansı artırmak için kullanılır. Ancak, bazen bu önbelleği temizlemek isteyebilirsiniz, özellikle çok sayıda düzenli ifade deseni kullanılıyorsa veya bellek kullanımını kontrol etmek istiyorsanız bu fonksiyonun kullanmalısınız.

İşte `purge()` fonksiyonunun kullanımı:

```python
import re

# Örnek düzenli ifade deseni
pattern1 = re.compile(r'\b\w+\b')
pattern2 = re.compile(r'\d+')

# re modülü önbelleği temizleme
re.purge()

# Yeniden derleme yapmadan önce temizlenmiş önbelleği kullanmak
result1 = pattern1.findall("This is a sample text.")
result2 = pattern2.findall("123 456")

print(result1)
print(result2)
```

Çıktı:

```python
['This', 'is', 'a', 'sample', 'text']
['123', '456']
```

Bu örnekte, `re.purge()` fonksiyonu çağrılarak `re` modülünün önbelleği temizlenir. Daha sonra, temizlenmiş önbelleği kullanarak `pattern1` ve `pattern2` düzenli ifade desenlerini tekrar derleriz.

`re.purge()` fonksiyonu genellikle programın çalışma süresi boyunca biriken düzenli ifade desenlerini temizlemek için kullanılır. Ancak, bu işlemi yapmak, genel performansı olumsuz etkileyebilir, çünkü bir sonraki derleme işlemi için aynı desenin tekrar derlenmesi gerekecektir. Bu nedenle, önbelleği temizlemek konusunda dikkatli olunmalıdır ve ihtiyaç doğrultusunda kullanılmalıdır.
