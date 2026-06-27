Title: Pandas - pyarrow
Date: 2025-11-16 22:36
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, pyarrow
Author: Mustafa Halil

# `pyarrow` String Türü ile Hızlanmak

Pandas'ta dizelerle (strings) mi çalışıyorsunuz ve beklediğinizden biraz daha yavaş olduğunu mu görüyorsunuz? Bu eğitimde, **PyArrow**'u kullanarak işleri nasıl hızlandırabileceğimizi öğreneceğiz.

Örnek olarak kullanacağımız dosyanın adı **TDK_imla.txt**. Bu dosya, satır başına bir kelime olacak şekilde toplam 76.183 kelime içeren bir imla sözlüğüdür.

Elimizdeki dosyaya dayanarak bir seri (series) oluşturalım.

```python
import pandas as pd

dosya = "TDK_imla.txt"
seri = pd.Series(ilk_kelime.strip() for ilk_kelime in open(dosya))
print(seri)
```

Oluşturulan seri `seri` olarak adlandırılır ve `pd.series` kullanılarak, dosya adının üzerindeki her kelimeyi yineleyip (iterate edip) yeni satır karakterlerinden ve baştaki/sondaki boşluklardan temizleyerek (`strip()`) oluşturulur. Serinin uzunluğu kontrol edildiğinde, 76.183 kelime olduğu görülür

Çıktı (dosya içeriği):

```python
0                    ab
1                   aba
2                 abacı
3              abacılık
4                 abadi
              ...      
76178        zürriyetli
76179       zürriyetsiz
76180    zürriyetsizlik
76181             züyuf
76182        züyuf akçe
Length: 76183, dtype: object
```

Serinin uzunluğunu bulmak için aşağıdaki kodu kullanabiliriz.

```python
len(seri)
```

Çıktı:

```python
76183
```

Her bir satırdaki kelimenin karakter uzunluğunu bulmak istediğimizi düzünelim.

**Yöntem 1: `apply()` Kullanımı**

Pandas'ta döngü çalıştırmanın çok kötü bir fikir olduğu bilinmektedir, çünkü uzun sürer. Alternatif olarak **apply()** metodu kullanılabilir.

```python
print(seri.apply(len))
```

Çıktı:

```python
0         2
1         3
2         5
3         8
4         5
         ..
76178    10
76179    11
76180    14
76181     5
76182    10
Length: 76183, dtype: int64
```

Yukarıdaki kod, orijinal serinin indeksiyle eşleşen ve değeri her bir elemanın uzunluğu olan yeni bir seri döndürür.

Bu işlemi **Jupyter Notebook**'ta uygularken `%timeit` kodunu ekleyip (çalışmayı zamanlayıp) çalıştırırsak ;

```python
%timeit seri.apply(len)
```

Çıktı:

```python
17.8 ms ± 278 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

işlemin **17.8 milisaniye** sürdüğü gösterilir.

**Yöntem 2: `str` Erişimcisi Kullanımı (Vektörleştirilmiş Yöntem)**

Pandas'ta dizelerle (string ifadelerle) çalışırken en iyi ve en hızlı olarak kabul edilen yol, **str** **erişimcisi (accessor)** kullanmak olabilir. **seri.str.len()** ifadesi kullanılır

```python
 print(seri.str.len())
```

Çıktı:

```python
0         2
1         3
2         5
3         8
4         5
         ..
76178    10
76179    11
76180    14
76181     5
76182    10
Length: 76183, dtype: int64
```

Bu işlemi **Jupyter Notebook**'ta uygularken `%timeit` kodunu ekleyip (çalışmayı zamanlayıp) çalıştırırsak ;

```python
%timeit seri.str.len()
```

```python
17.4 ms ± 1.12 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

Bu işlemin, 17.8 milisaniye yerine **17.4 milisaniye** sürerek, yaklaşık **% 2,25 daha hızlı olduğunu gösterir.** Ancak bu hızlanma son derecede azdır.

**Ek Örnekler: İlk Karakteri Almak / Elde etmek**

1. **apply** **ile:** İlk karakteri almak için lambda fonksiyonu (`lambda x: x[0]`) ile **seri.apply** kodu kullanılır.

```python
seri.apply(lambda x: x[0])
```

 Çıktı:

```python
0        a
1        a
2        a
3        a
4        a
        ..
76178    z
76179    z
76180    z
76181    z
76182    z
Length: 76183, dtype: object
```

```python
%timeit seri.apply(lambda x: x[0])
```

```python
7.6 ms ± 193 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Bu işlem **7.6 milisaniye** sürer.

2. **str.get()** **ile:** Köşeli parantezin eşdeğeri olan `seri.str.get(0)` kullanılır.

```python
print(seri.str.get(0))
```

Çıktı:

```python
0        a
1        a
2        a
3        a
4        a
        ..
76178    z
76179    z
76180    z
76181    z
76182    z
Length: 76183, dtype: object
```

```python
%timeit seri.str.get(0)
```

Çıktı:

```python
14.8 ms ± 176 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

Bu işlem daha uzun sürer; 7.6 milisaniye yerine **14.8 milisaniye** sürerek neredeyse **iki kat daha uzun** sürer.

**Ek Örnekler: İlk Üç Karakteri Alma (Dilimleme - Slice)**

1. ****apply()** ile: Dilimleme (`[:3]`) içeren bir lambda fonksiyonu ile **seri.apply** kullanılır.

```python
print(seri.apply(lambda x: x[:3]))
```

Çıktı:

```python
0         ab
1        aba
2        aba
3        aba
4        aba
        ... 
76178    zür
76179    zür
76180    zür
76181    züy
76182    züy
Length: 76183, dtype: object
```

```python
%timeit seri.apply(lambda x: x[:3])
```

Çıktı:

```python
11.1 ms ± 357 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Bu işlem **11.1** milisaniye sürer.

2. **str.slice** **ile:** **s.str.slice(0, 3)** kullanılır.

```python
print(seri.str.slice(0,3))
```

Çıktı:

```python
0         ab
1        aba
2        aba
3        aba
4        aba
        ... 
76178    zür
76179    zür
76180    zür
76181    züy
76182    züy
Length: 76183, dtype: object
```

```python
%timeit seri.str.slice(0,3)Çıktı:
```

Çıktı:

```python
10.2 ms ± 226 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Bu işlem **10.2** milisaniye sürer. Bu, yine %8 kadar daha hızlıdır, ancak hala şüpheli bir durum vardır.

**Sorunun Kaynağı: `DType` ve Bellek Yükü**

Neden hızlı olması gereken bu vektörleştirilmiş yöntemler ya sadece biraz daha hızlıdır ya da daha yavaştır? 76.183 kelime çok küçük bir veri seti değildir.

Sorun temel olarak **DType**'tır:

**seri.dtype** sorgulandığında, değerin **O** veya **object** olduğu görülür.

```python
print(seri.dtype)
```

Çıktı:

```python
dtype('O')
```

Bu, serideki değerlerin **Python nesneleri** olarak depolandığı anlamına gelir.

Normalde, Pandas'ta tam sayılar gibi veriler perde arkasında NumPy değerleri (örneğin 64 bitlik `int64`'ler) kullanılarak depolanır, ancak dizeler söz konusu olduğunda durum böyle değildir.

Dizeler (String ifadeler), **PyArrow** yerine **Python dizeleri** olarak depolanmaktadır.

Hem `apply` hem de `str` yöntemlerini çalıştırdığımızda, **Python belleğine gidilmesi, dize nesnesinin çekilmesi ve ardından üzerinde metodun çağrılması** gerekir.

Buradaki **ek yük (overhead)** yöntemin kendisi veya vektörleştirme değildir; Yük, verinin Python'ın belleğinden alınmasını gerektiren **veri tipinin kendisidir.**

## Çözüm: PyArrow Kullanımı

Diğer seçenek **PyArrow** kullanmaktır.

PyArrow, Pandas'ın birçok bölümünde hala deneyseldir, ancak dizeler için oldukça iyi çalışmaktadır.

PyArrow, **Arrow kütüphanesi** ile çalışmak için bir Python sarmalayıcısıdır (wrapper).

Arrow, sıkıştırmayı yöneten ve dizeleri dahili olarak işleyen, **süper hızlı, bellekteki bir veri yapısıdır**.

PyArrow kullanıldığında, artık dizeleri kullanmak için Python belleğine gitmek gerekmeyecektir.

## PyArrow ile Testlerin Yeniden Yapılması

Testleri yeniden yapalım, ancak bu sefer seriyi oluştururken `dtype=` parametresi `"string[pyarrow]"` olarak belirtelim. Bu, verinin farklı bir şekilde depolandığını gösterir.

```python
seri = pd.Series([ilk_kelime.strip() 
                 for ilk_kelime in open(dosya)], dtype="string[pyarrow]")

print(seri)
```

Çıktı:

```python
0                    ab
1                   aba
2                 abacı
3              abacılık
4                 abadi
              ...      
76178        zürriyetli
76179       zürriyetsiz
76180    zürriyetsizlik
76181             züyuf
76182        züyuf akçe
Length: 76183, dtype: string
```

Daha önceki (ilk) çıktıda `Length: 76183, dtype: object` yazarken bu kez `Length: 76183, dtype: string` çıktısını alıyoruz.

`dtype` çıktısına da bakalım;

```python
print(seri.dtype)
```

Çıktı:

```python
string[pyarrow]
```

Yukarıdaki kodları uzun uzun yazmadan sadece zaman kodları ve çıktılarını inceleyelim. 

Her bir satırdaki kelimenin karakter uzunluğunu bulmak için `apply()` metodunu kullanalım.

```python
%timeit seri2.apply(len)
```

Çıktı:

```python
16 ms ± 70.4 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Aynı işlemi string metodu ile bulalım;

```python
%timeit seri2.str.len()
```

Çıktı:

```python
992 μs ± 1.33 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

Görüldüğü gibi string metodu apply() metoduna kıyasla **(16 / 0.99 =) 16** kat daha hızlı.

Kelimelerin ilk karakterini apply metodu ile ne kadar sürede elde ederiz;

```python
%timeit seri2.str.get(0)
```

Çıktı:

```python
26.6 ms ± 202 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)ss
```

Kelimelerin ilk 3 karakterini apply metodu ile ne kadar sürede elde ederiz;

```python
%timeit seri2.apply(lambda x: x[:3])
```

Çıktı:

```python
11.6 ms ± 83.5 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Kelimelerin ilk 3 karakterini string metodu ile ne kadar sürede elde ederiz;

```python
%timeit seri2.str.slice(0,3)
```

Çıktı:

```python
847 μs ± 726 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

Aradaki hız farkı, (11.6/0.847 = 13.695) yaklaşık 14 kat

## PyArrow Sonuçları (Karşılaştırmalı)

| İşlem                  | Orijinal DType (`object`) Süresi | PyArrow DType (`string[pyarrow]`) Süresi | Hızlanma                                                   |
| ---------------------- | -------------------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| `seri.apply(len)`      | 17,8 ms                          | 16 milisaniye                            | Hızlanma yok, Yavaşlama var                                |
| `seri.str.len()`       | 17,4 ms                          | **992 μs**                               | Yaklaşık **%95** zaman tasarrufu (**17,5** kat daha hızlı) |
| `seri.str.get(0)`      | 14,8 ms                          | **26,6 milisaniye**                      | Hızlanma yok, Yavaşlama var                                |
| `seri.str.slice(0, 3)` | 10,2 ms                          | **847 μs**                               | **12 kat** daha hızlı                                      |

**PyArrow** ile `str.len()` ve `str.slice()` gibi vektörleştirilmiş yöntemler kullanıldığında, hız inanılmaz derecede artmaktadır. Daha büyük dosya boyutu ile çalışıldığında elde ettiğimiz hız daha fazla artacaktır.

PyArrow'un performansı artırma şeklini, bir kütüphanenin yavaş bir depo alanındaki (Python belleği) dağınık verileri tek tek çağırıp işlemesine kıyasla, **verileri hızlı bir depoya (Arrow) taşıyıp düzenli bir şekilde içeride toplu olarak işlemesine** benzetebiliriz; bu, tüm işin hızını veri transferi yerine doğrudan hesaplamaya odaklar.

Pandas'ta dizelerle (strings) çalışırken karşılaşılan performans darboğazlarının temel nedeni, **verinin depolanma biçimi** ile ilgilidir

Bu darboğaz, kullanılan yöntemden (örneğin, `apply` veya vektörleştirilmiş `str` erişimcisi) ziyade, verinin altında yatan **veri tipi (DType)** kaynaklıdır.

## Sonuç ve Uyarı

Sonuçlara baktığımızda, Pandas'taki dizelerle yapılan her şey için **PyArrow**'a geçirilmesi gerektiğini **söyleyemeyiz.**

PyArrow'un hala daha yavaş olduğu yerler mevcuttur ve kullanıma geçmeden önce kullanım durumunun dikkatlice kontrol edilmesi önerilir. Ancak kullanım durumunuz PyArrow dizeleriyle çalışıyorsa, gerçek kodunuzda neredeyse hiçbir değişiklik yapmadan süper, süper hızlı dize çalışmalarından gerçekten fayda sağlayabilirsiniz.

## Kaynak:

* [Why Pandas string methods are slow — and how PyArrow makes them 20× faster - YouTube](https://www.youtube.com/watch?v=Ovz8F464uo0)
