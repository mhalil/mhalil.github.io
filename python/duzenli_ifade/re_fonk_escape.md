Title: Düzenli İfadeler - escape
Date: 2023-09-01 00:00
Modified: 2025-11-02 13:28
Category: Düzenli İfadeler
Tags: Python, Düzenli İfadeler, Regular Expressions, Regex, Re, Kütüphane, Modül, Escape

# escape() Fonksiyonu

`escape()` metodu (fonksiyonu), **bir metni düzenli ifade (regular expression) içinde kullanılmaya uygun hale getirmek için kullanılır.** Bu fonksiyon, metindeki özel karakterleri kaçış karakterleri ile değiştirir, böylece bu karakterler düzenli ifade içinde özel anlam taşımazlar ve doğrudan metin olarak eşleştirilebilirler.

Örneğin, bir kullanıcının girdiği metni doğrudan bir düzenli ifade içinde kullanmak istediğinizi düşünün. Kullanıcının girdisi içinde özel karakterler bulunabilir ve bu karakterlerin düzenli ifade içinde kullanılması sorunlara neden olabilir. `escape()` fonksiyonu, bu tür durumlar için kullanışlıdır.

Örneğin, elimizde kullanıcı tarafından tanımlanmış bir değişken (`user_input`) olduğunu ve bu değişkenin, düzenli ifadelerde kullanılan özel karakterler içerdiğini düşünün. 
`user_input` değişkenini `escape()` metoduna parametre olarak verdiğimizde nasıl bir sonuç elde ettiğimizi görelim;

```python
user_input = "(.*$"
escaped_input = re.escape(user_input)
print(escaped_input)
```

Kullanıcı tarafından belirlenen `(.*$` ifadesi, `escape()` metodu sayesinde aşağıdaki hale dönüştürülerek, düzenli ifadelerle rahatça kullanılabilecek hale getirilmiş olur.

**Çıktı**:

```
\(\.\*\$
```

İşte örneğe ait tüm kodlar:

```python
import re

user_input = "(.*$"

# Kullanıcı girdisini düzenli ifade içinde güvenli hale getirme
escaped_input = re.escape(user_input)

# Düzenli ifadeyi kullanma
pattern = re.compile(escaped_input)
result = pattern.match("(.*$")

print(result.group())  
```

**Çıktı**:

```python
'(.*$'
```

Bu örnekte, `re.escape()` fonksiyonu, `user_input` içindeki özel karakterleri kaçış karakterleriyle değiştirir ve bu düzenli ifade içinde güvenli bir şekilde kullanılabilir hale getirir. Bu, kullanıcının girdisinin düzenli ifade içinde istenmeyen yan etkiler oluşturmasını önler.

Bu fonksiyon özellikle dinamik olarak oluşturulan düzenli ifadelerde veya kullanıcı tarafından sağlanan metinlerle çalışırken güvenlik sağlamak için önemlidir.
