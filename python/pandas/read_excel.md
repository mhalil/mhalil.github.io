Title: Pandas - read_excel
Date: 2022-07-09 21:10
Modified: 2025-11-29 17:06
Category: Pandas
Tags: Python, Pandas, read_excel, Kütüphane, Modül, Excel, LibreOfis
Author: Mustafa Halil

# read_excel() Metodu

**MS Excel** (xls, xlsx, xlsm ve xlsb) ve **Libre Ofis Calc** (odf, ods ve odt) dosyalarının içeriğini çalışmamıza dahil etmek için `read_excel()` fonksiyonunu kullanmalıyız. 

> **Libre Ofis Calc** dosyalarının içeriğini okuyabilmek için "**openpyxl**" kütüphanelerinin / modüllerinin yüklü olması gerekir.

Aşağıda, **MS Excel** ve **Libre Ofis Calc** programları ile oluşturulan hesap tablolarının Veri Çerçevelerine (Data Frame'e) nasıl dönüştürüleceğini ve nasıl kullanılacağı konusunu detayı olarak inceleyeceğiz.

<u>Bu metot;</u>

- **xls, xlsx, xlsm, xlsb, odf, ods** ve **odt** uzantılı dosyaları destekler.
- Yerel bir dosya sisteminde veya bir URL'de depolanan excel dosyalarını yükleyebilir.
- URL için **http, ftp, s3** ve **dosya**yı destekler.
- Ayrıca tek bir çalışma sayfasından veya bir sayfa listesinden okumayı da destekler.
- İki sayfa okunurken, **DataFrame** bir Sözlük (Dict) yapısı döndürür.

## Sözdizimi:

```python
pandas.read_excel(io, sheet_name=0, *, header=0, names=None, 
        index_col=None, usecols=None, dtype=None, engine=None, 
        converters=None, true_values=None, false_values=None, skiprows=None, 
        nrows=None, na_values=None, keep_default_na=True, na_filter=True,
        verbose=False, parse_dates=False, date_parser=<no_default>, 
        date_format=None, thousands=None, decimal='.', comment=None, 
        skipfooter=0, storage_options=None, dtype_backend=<no_default>, 
        engine_kwargs=None)
```

Bu metot kullanıldığında, varsayılan olarak, excel dosyasının **ilk çalışma sayfası** yüklenir ve **ilk satır** Veri Çerçevesi (DataFrame) **başlığı (sütun adı)** olarak ayarlanır.

```python
import pandas as pd
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx")
print(dogumlar.head())
```

|     | Yıl  | Toplam  | Ocak   | Şubat  | Mart   | Nisan  | Mayıs  | Haziran | Temmuz | Ağustos | Eylül  | Ekim   | Kasım | Aralık |
| --- | ---- | ------- | ------ | ------ | ------ | ------ | ------ | ------- | ------ | ------- | ------ | ------ | ----- | ------ |
| 0   | 2001 | 1323341 | 170397 | 103476 | 107912 | 102585 | 110391 | 111722  | 119752 | 120963  | 109590 | 103662 | 92554 | 70337  |
| 1   | 2002 | 1229555 | 155065 | 103446 | 102175 | 95976  | 99501  | 102627  | 109747 | 108061  | 99701  | 96216  | 89285 | 67755  |
| 2   | 2003 | 1198927 | 138670 | 89548  | 101046 | 92574  | 99531  | 104644  | 109225 | 109159  | 98766  | 94838  | 89542 | 71384  |
| 3   | 2004 | 1222484 | 141538 | 94596  | 100696 | 100801 | 102214 | 105728  | 111102 | 110425  | 98492  | 94840  | 90833 | 71219  |
| 4   | 2005 | 1244041 | 142311 | 94234  | 100529 | 97441  | 106833 | 108536  | 111066 | 111430  | 103273 | 103310 | 92364 | 72714  |

Pandas kütüphanesi, tablo okumayı kolaylaştırır ve birden çok satıra yayılan (birleştirilmiş hücrelerdeki) verileri, (ilgili sütunu işleyerek) her hücreye kopyalar. Orjinal tablomuz aşağıdaki gibidir.

![nba](../../images/python/pandas/nba.png)

```python
nba2 = pd.read_excel("Veri_Setleri/nba.xlsx")
print(nba2)
```

|     | Name                   | Team            | Number | Position | Age  | Height | Weight | College           | Salary     |
| --- | ---------------------- | --------------- | ------ | -------- | ---- | ------ | ------ | ----------------- | ---------- |
| 0   | Avery Bradley          | Boston Celtics  | 0.0    | PG       | 25.0 | 6-2    | 180.0  | Texas             | 7730337.0  |
| 1   | Jae Crowder            | Boston Celtics  | 99.0   | SF       | 25.0 | 6-6    | 235.0  | Marquette         | 6796117.0  |
| 2   | John Holland           | Boston Celtics  | 30.0   | SG       | 27.0 | 6-5    | 205.0  | Boston University | NaN        |
| 3   | R.J. Hunter            | Boston Celtics  | 28.0   | SG       | 22.0 | 6-5    | 185.0  | Georgia State     | 1148640.0  |
| 4   | Thomas Robinson        | Brooklyn Nets   | 41.0   | PF       | 25.0 | 6-10   | 237.0  | Kansas            | 981348.0   |
| 5   | Henry Sims             | Brooklyn Nets   | 14.0   | C        | 26.0 | 6-10   | 248.0  | Georgetown        | 947276.0   |
| 6   | Donald Sloan           | Brooklyn Nets   | 15.0   | PG       | 28.0 | 6-3    | 205.0  | Texas A&M         | 947276.0   |
| 7   | Thaddeus Young         | Brooklyn Nets   | 30.0   | PF       | 27.0 | 6-8    | 221.0  | Georgia Tech      | 11235955.0 |
| 8   | Arron Afflalo          | New York Knicks | 4.0    | SG       | 30.0 | 6-5    | 210.0  | UCLA              | 8000000.0  |
| 9   | Lou Amundson           | New York Knicks | 17.0   | PF       | 33.0 | 6-9    | 220.0  | UNLV              | 1635476.0  |
| 10  | Thanasis Antetokounmpo | New York Knicks | 43.0   | SF       | 23.0 | 6-7    | 205.0  | NaN               | 30888.0    |
| 11  | Carmelo Anthony        | New York Knicks | 7.0    | SF       | 32.0 | 6-8    | 240.0  | Syracuse          | 22875000.0 |
| 12  | Jose Calderon          | New York Knicks | 3.0    | PG       | 34.0 | 6-3    | 200.0  | NaN               | 7402812.0  |
| 13  | Cleanthony Early       | New York Knicks | 11.0   | SF       | 25.0 | 6-8    | 210.0  | Wichita State     | 845059.0   |

Pandas kütüphanesi sayesinde, **Team** Sütunundaki birleştirilmiş hücrelerde bulunan veriler, hücrelere ayrı ayrı kopyalanarak düzgün, bir veri çevçevesi oluşturmamızı sağlamış oldu. 
Benzer işlemi, **Eksik / Kayıp Veri Tespiti ve Düzenleme Yöntemleri** bölümündeki [fillna]({filename}fillna.md) fonksiyonu'nun **method parametresi**ni kullanarak ta gerçekleştirebiliriz.

# Parametreler

## header ve names parametreleri

`read_excel()` metodu, Excel'deki ilk satırı varsayılan olarak bir başlık kabul eder ve bunu Veri Çerçevesi (DataFrame) sütun adları olarak kullanır. Excel dosyasındaki ilk satırın başlık değil, bir veri olduğu düşünüldüğünde, yani sadece verilerden oluşan excel dosyası ile çalıştığımızda, `header=None` parametresi kullanılmalıdır. Bu durumda Başlık (sütun adlarını) belirtmek için `names` parametresi kullanılır.

İlk olarak **OSD** uzantılı bir dosyayı (ODS, LibreOfis Calc Programının uzantısıdır , siz bu dosya yerine MS Excel'in kayıt formatı olan XLS ya da XLSX uzantılı dosya da kullanabilirsiniz.) çalışmamıza dahil edip içeriğine bakalım.

```python
import pandas as pd
basliksiz = pd.read_excel("Veri_Setleri/basliksiz.ods")
print(basliksiz.head())
```

|     | 9   | 82  | 246 |
| --- | --- | --- | --- |
| 0   | 7   | 78  | 180 |
| 1   | 8   | 83  | 565 |
| 2   | 6   | 82  | 486 |
| 3   | 4   | 37  | 615 |
| 4   | 2   | 18  | 341 |

Yukarıdaki örnekte gördüğünüz üzere, ilk satır başlık değil, veriden oluşuyor. Bunu `header=None` ve `names` parametreleri ile düzenleyelim.

```python
baslik = ["Birler", "Onlar", "Yüzler"]
basliksiz = pd.read_excel("Veri_Setleri/basliksiz.ods", 
                            header = None, names = baslik )
print(basliksiz.head())
```

|     | Birler | Onlar | Yüzler |
| --- | ------ | ----- | ------ |
| 0   | 9      | 82    | 246    |
| 1   | 7      | 78    | 180    |
| 2   | 8      | 83    | 565    |
| 3   | 6      | 82    | 486    |
| 4   | 4      | 37    | 615    |

## sheet_name Parametresi

Excel dosyamızın içinde birden fazla çalışma sayfası (sekme) bulunması halinde, istediğimiz çalışma sayfasına erişebilmek için, `sheet_name` parametresini kullanmalıyız.

Aylara göre doğum sayılarını barındıran dosyamızı çalışmamıza dahil edip ilk 5 veriye göz atalım.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx")
print(dogumlar.head())
```

|     | Yıl  | Toplam  | Ocak   | Şubat  | Mart   | Nisan  | Mayıs  | Haziran | Temmuz | Ağustos | Eylül  | Ekim   | Kasım | Aralık |
| --- | ---- | ------- | ------ | ------ | ------ | ------ | ------ | ------- | ------ | ------- | ------ | ------ | ----- | ------ |
| 0   | 2001 | 1323341 | 170397 | 103476 | 107912 | 102585 | 110391 | 111722  | 119752 | 120963  | 109590 | 103662 | 92554 | 70337  |
| 1   | 2002 | 1229555 | 155065 | 103446 | 102175 | 95976  | 99501  | 102627  | 109747 | 108061  | 99701  | 96216  | 89285 | 67755  |
| 2   | 2003 | 1198927 | 138670 | 89548  | 101046 | 92574  | 99531  | 104644  | 109225 | 109159  | 98766  | 94838  | 89542 | 71384  |
| 3   | 2004 | 1222484 | 141538 | 94596  | 100696 | 100801 | 102214 | 105728  | 111102 | 110425  | 98492  | 94840  | 90833 | 71219  |
| 4   | 2005 | 1244041 | 142311 | 94234  | 100529 | 97441  | 106833 | 108536  | 111066 | 111430  | 103273 | 103310 | 92364 | 72714  |

Kodumuza `sheet_name = "ortalama"` ibaresi ekleyerek, aynı dosyadaki "**ortalama**" isimli sekmede bulunan verileri inceleyelim.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                            sheet_name = "ortalama")
print(dogumlar.head())
```

|     | Yıl  | Toplam  | Ortalama      |
| --- | ---- | ------- | ------------- |
| 0   | 2001 | 1323341 | 110278.416667 |
| 1   | 2002 | 1229555 | 102462.916667 |
| 2   | 2003 | 1198927 | 99910.583333  |
| 3   | 2004 | 1222484 | 101873.666667 |
| 4   | 2005 | 1244041 | 103670.083333 |

Gördüğünüz gibi, kodumuza `sheet_name = "ortalama"` ibaresi ekleyerek, aynı excel dosyasının **ortalama** isimli çalışma sayfasındaki verileri, çalışmamıza veri çerçevesi olarak ekledik.

Birden fazla çalışma sayfasını, çalışmamıza dahil etmek (içe aktarmak) istersek, `sheet_name` parametresine **bir liste girdisi** vermeliyiz. Bu durumda çıktı, bir **sözlük yapısı (dict)** olacaktır.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                            sheet_name = ["ortalama", "2001-2021"])
print(dogumlar)
```

```python
{'ortalama':      Yıl   Toplam       Ortalama
 0   2001  1323341  110278.416667
 1   2002  1229555  102462.916667
 2   2003  1198927   99910.583333
 3   2004  1222484  101873.666667
 4   2005  1244041  103670.083333
 5   2006  1255432  104619.333333
 6   2007  1289992  107499.333333
 7   2008  1295511  107959.250000
 8   2009  1266751  105562.583333
 9   2010  1261169  105097.416667
 10  2011  1252812  104401.000000
 11  2012  1294605  107883.750000
 12  2013  1297505  108125.416667
 13  2014  1351088  112590.666667
 14  2015  1336908  111409.000000
 15  2016  1316204  109683.666667
 16  2017  1299419  108284.916667
 17  2018  1255258  104604.833333
 18  2019  1188524   99043.666667
 19  2020  1115821   92985.083333
 20  2021  1079842   89986.833333,
 '2001-2021':      Yıl   Toplam    Ocak   Şubat    Mart   Nisan   Mayıs  Haziran  Temmuz  \
 0   2001  1323341  170397  103476  107912  102585  110391   111722  119752   
 1   2002  1229555  155065  103446  102175   95976   99501   102627  109747   
 2   2003  1198927  138670   89548  101046   92574   99531   104644  109225   
 3   2004  1222484  141538   94596  100696  100801  102214   105728  111102   
 4   2005  1244041  142311   94234  100529   97441  106833   108536  111066   
 5   2006  1255432  128708   94760  104126   97624  103903   112016  115097   
 6   2007  1289992  131276   93927  102807  100159  108119   110359  122324   
 7   2008  1295511  130424   98099  102962  102877  107003   110089  119977   
 8   2009  1266751  122407   92414   99419  103432  103783   107847  117160   
 9   2010  1261169  119444   95023  103583   99477  103676   109441  113639   
 10  2011  1252812  118547   92484  100992   95348   94131   104086  114390   
 11  2012  1294605  119556   99966  105499   98880  105807   110056  118649   
 12  2013  1297505  118373   94803  102471   96865  106757   109672  123758   
 13  2014  1351088  121694   96802  105603  105652  112448   115978  129616   
 14  2015  1336908  120373   99169  105792  103110  105254   115681  130945   
 15  2016  1316204  114274  100640  105166  101947  104080   117994  120126   
 16  2017  1299419  114968   95567  101700   96132  106274   115827  122894   
 17  2018  1255258  107530   90002  101283   94776  104719   110383  117967   
 18  2019  1188524  104044   85510   96631   93013  105166    97965  112628   
 19  2020  1115821   94888   83433   89503   88526   93159    99232  105970   
 20  2021  1079842   80733   77535   86214   82789   88506    94266   99252   

     Ağustos   Eylül    Ekim   Kasım  Aralık  
 0    120963  109590  103662   92554   70337  
 1    108061   99701   96216   89285   67755  
 2    109159   98766   94838   89542   71384  
 3    110425   98492   94840   90833   71219  
 4    111430  103273  103310   92364   72714  
 5    117298  107158  105773   93167   75802  
 6    118169  111055  109888   99639   82270  
 7    120048  114470  107978   97389   84195  
 8    116229  115824  105407   96155   86674  
 9    113082  110324  104427  101610   87443  
 10   121152  112959  105048  102970   90705  
 11   123634  110338  108327  102413   91480  
 12   121625  112913  110716  104182   95370  
 13   126296  119030  111754  105566  100649  
 14   123296  116428  112839  106319   97702  
 15   124833  114366  107951  104959   99868  
 16   122386  110811  108538  104386   99936  
 17   116715  107105  107818  100436   96524  
 18   109182   99981   98320   92936   93148  
 19   100478   96018   93428   87540   83646  
 20   100407   97334   93290   92189   87327  }
```

## decimal Parametresi

Harici kaynaktan içe aktararak oluşturduğumuz veri çerçevelerini incelediğimizde, sayısal olduğunu düşündüğümüz bazı değerlerin, **metinsel (string)** olduğunu farkederiz. Bunun sebebi, farklı ülkelerin farklı bölgesel ayarlar kullanmalarından kaynaklanır. Örneğin Ülkemiz ve Avrupa ülkelerinde sayıların ondalık kısımlarını temsil etmek için **virgül (,)**, binlik basamakları ayırmak için **nokta (.)** karakteri kullanılırken bazı Ülkelerde bunun tersi kullanılmaktadır.
Elimde, interneten indirmiş olduğum IMDB (Internet Movie Data Base) verilerinden oluşan bir excel dosyası bulunmaktadır. Bu dosyayı veri çerçevesine dönüştürüp içeriğini inceleyelim.

```python
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx")
print(imdb)
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9,2  | 1071904      |
| 1   | The Godfather            | 1972 | 9,2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9    | 488889       |
| 3   | Pulp Fiction             | 1994 | 8,9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8,9  | 1045186      |
| ... | ...                      | ...  | ...  | ...          |
| 242 | Mystic River             | 2003 | 7,9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7,9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7,9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7,9  | 100974       |
| 246 | Papillon                 | 1973 | 7,9  | 62517        |

247 rows × 4 columns

Gördüğüm kadarı ile **Film_Adı** sütunu **object (yani string)** diğer sütunlar ise **float (ondalıklı sayı)** veri tipinde gibi görünüyor. Sütun biçimlerinin tahmin ettiğim gibi olup olmadığını teyit etmek için **dtype** paramatresini kullanıyorum.

```python
print(imdb.dtypes)
```

```python
Film_Adı        object
Yıl              int64
Puan            object
Oylayan_Kişi     int64
dtype: object
```

Çıktıyı incelediğimde, **Puan** isimli sütun verilerinin de **object (yani string)** oluğunu görüyorum. Yani Bu sütundaki verilerle matematiksel işlem yapmaya çalışırsam ya hata mesajı alacak ya da yanlış sonuç elde edeceğim. Bunu da örneklerle inceleyelim. **Puan** sütununun 2 katını alıp yeni bir sütun olarak veri çerçevesine eklemeyi deneyelim.

```python
imdb["Puan_2"] = imdb["Puan"] * 2
print(imdb)
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi | Puan_2 |
| --- | ------------------------ | ---- | ---- | ------------ | ------ |
| 0   | The Shawshank Redemption | 1994 | 9,2  | 1071904      | 9,29,2 |
| 1   | The Godfather            | 1972 | 9,2  | 751381       | 9,29,2 |
| 2   | The Godfather: Part II   | 1974 | 9    | 488889       | 18     |
| 3   | Pulp Fiction             | 1994 | 8,9  | 830504       | 8,98,9 |
| 4   | The Dark Knight          | 2008 | 8,9  | 1045186      | 8,98,9 |
| ... | ...                      | ...  | ...  | ...          | ...    |
| 242 | Mystic River             | 2003 | 7,9  | 256159       | 7,97,9 |
| 243 | In the Heat of the Night | 1967 | 7,9  | 37081        | 7,97,9 |
| 244 | Arsenic and Old Lace     | 1944 | 7,9  | 45893        | 7,97,9 |
| 245 | Before Sunrise           | 1995 | 7,9  | 100974       | 7,97,9 |
| 246 | Papillon                 | 1973 | 7,9  | 62517        | 7,97,9 |

247 rows × 5 columns

Çıktıya bakarsak, **Puan_2** ismiyle oluşturduğumuz yeni sütundaki değerler, **Puan** isimli sütunun 2 katından değil, 2 defa yanyana yazılmazsından oluştu. Bunun sebebi, verilerin **string (metin)** yapıda olmasıdır.
Bu tür sorunları bertaraf etmek için, `decimal` paramatresini kullanmamız gerekir. Harici veriyi veri çerçevesine dönüştürürken `decimal = ","` parametresini kullanırsak, `","` ibaresi bulunan sayısal değerlerden oluşan string ifadeler, **float (ondalıklı sayı)** veri tipine dönüştürülür.

```python
imdb_2 = pd.read_excel("Veri_Setleri/imdb.xlsx", decimal=",")
print(imdb_2)
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9.0  | 488889       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| ... | ...                      | ...  | ...  | ...          |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       |
| 246 | Papillon                 | 1973 | 7.9  | 62517        |

247 rows × 4 columns

```python
print(imdb_2.dtypes)
```

```
Film_Adı         object
Yıl               int64
Puan            float64
Oylayan_Kişi      int64
dtype: object
```

Çıktı incelendiğinde görüyoruz ki, **Puan** isimli sütun **float (ondalıklı sayı)** veri tipine dönüşmüş oldu. Yukarıda yaptığımız işlemi (**Puan** sütununun 2 katını alıp yeni bir sütun olarak veri çerçevesine eklemeyi) tekrar deneyelim.

```python
imdb_2["Puan_2"] = imdb_2["Puan"] * 2
print(imdb_2)
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi | Puan_2 |
| --- | ------------------------ | ---- | ---- | ------------ | ------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      | 18.4   |
| 1   | The Godfather            | 1972 | 9.2  | 751381       | 18.4   |
| 2   | The Godfather: Part II   | 1974 | 9.0  | 488889       | 18.0   |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       | 17.8   |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      | 17.8   |
| ... | ...                      | ...  | ...  | ...          | ...    |
| 242 | Mystic River             | 2003 | 7.9  | 256159       | 15.8   |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        | 15.8   |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        | 15.8   |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       | 15.8   |
| 246 | Papillon                 | 1973 | 7.9  | 62517        | 15.8   |

247 rows × 5 columns

İstediğimiz şeyi başardık. **Puan_2** sütunu, **Puan** sütununun 2 katından oluşmuş oldu.

## index_col Parametresi

Veri Çerçevesi (Data Frame) oluştururken sütunlardan birini, indeks değeri olarak ayarlamak/atamak istersek, `index_col` parametresini kullanabiliriz.
Öncelikle elimizdeki excel dosyamızı veri çerçevesine dönüştürüp içeriğine göz atalım.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                            sheet_name = "ortalama")
print(dogumlar).head()
```

|     | Yıl  | Toplam  | Ortalama      |
| --- | ---- | ------- | ------------- |
| 0   | 2001 | 1323341 | 110278.416667 |
| 1   | 2002 | 1229555 | 102462.916667 |
| 2   | 2003 | 1198927 | 99910.583333  |
| 3   | 2004 | 1222484 | 101873.666667 |
| 4   | 2005 | 1244041 | 103670.083333 |

Oluşan veri çerçevesindeki **Yıl** sütununu indeks olarak ayarlayalım.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                            sheet_name = "ortalama", index_col=0)
print(dogumlar.head())
```

| Yıl  | Toplam  | Ortalama      |
| ---- | ------- | ------------- |
| 2001 | 1323341 | 110278.416667 |
| 2002 | 1229555 | 102462.916667 |
| 2003 | 1198927 | 99910.583333  |
| 2004 | 1222484 | 101873.666667 |
| 2005 | 1244041 | 103670.083333 |

İşlem başarılı. **Yıl** Sütunu, indeks olarak ayarlandı.

## usecols Parametresi (Sütunları Atla)

Bir Excel çalışma sayfasını ya da farklı kaynaktan alınan veriyi, Pandas ile Veri Çerçevesine (DataFrame'e) dönüştürürken, **bazı sütunları atlamamız / göz ardı etmemiz** gerekebilir, bunu `usecols` parametresi kullanarak yapabiliriz. Bu parametre, tamsayı (int), metin (str), list-like veya callable (varsayılan None) değerlerini alır. Sütun
adlarının veya konumlarının listesini belirtmek için, bir dize (string) listesi veya bir tamsayı (int) listesi kullanmalıyız.

Aylara Göre Doğum Sayıları tablosunu yukarıda görmüştük. Bu tabloda 14 sütun bulunmaktadır. Sadece istediğimiz aylara ait sütun bilgilerini görüntülemek istersek `usecols` parametresine ya **ay isimlerini** ya da **ayın sütun indis değerini** yazmamız gerekir. Her iki kullanımı da görelim.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                        usecols=["Yıl", "Ocak", "Haziran", "Ağustos"])
print(dogumlar.head())
```

|     | Yıl  | Ocak   | Haziran | Ağustos |
| --- | ---- | ------ | ------- | ------- |
| 0   | 2001 | 170397 | 111722  | 120963  |
| 1   | 2002 | 155065 | 102627  | 108061  |
| 2   | 2003 | 138670 | 104644  | 109159  |
| 3   | 2004 | 141538 | 105728  | 110425  |
| 4   | 2005 | 142311 | 108536  | 111430  |

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                        usecols=[0,2,7,9])
print(dogumlar.head())
```

|     | Yıl  | Ocak   | Haziran | Ağustos |
| --- | ---- | ------ | ------- | ------- |
| 0   | 2001 | 170397 | 111722  | 120963  |
| 1   | 2002 | 155065 | 102627  | 108061  |
| 2   | 2003 | 138670 | 104644  | 109159  |
| 3   | 2004 | 141538 | 105728  | 110425  |
| 4   | 2005 | 142311 | 108536  | 111430  |

`usecols` parametresine, <u>sütun isimlerini yazarken</u>, sütun isimleri metinsel (string) ifade olduğu için **çift tırnak işareti `"`** kullandığımıza, <u>indis değeri yazarken</u> , indis değerleri tamsayı (int) olduğu için, tırnak işareti kullanmadığımıza dikkat edin.

Ayrıca, `usecols` parametresini, sütun aralığı belirterek te kullanabiliriz. Veri çerçevemizin sütunlarını, Excel programının sütun isimleri gibi (A, B, C,... şeklinde) düşünerek aralık belirtebiliriz. Aşağıdaki örnek, ne demek istediğimi daha net 
anlatacaktır.

```python
dogumlar = pd.read_excel("Veri_Setleri/AyaGöreDoğumlar.xlsx", 
                        usecols="C:G")
print(dogumlar.head())
```

|     | Ocak   | Şubat  | Mart   | Nisan  | Mayıs  |
| --- | ------ | ------ | ------ | ------ | ------ |
| 0   | 170397 | 103476 | 107912 | 102585 | 110391 |
| 1   | 155065 | 103446 | 102175 | 95976  | 99501  |
| 2   | 138670 | 89548  | 101046 | 92574  | 99531  |
| 3   | 141538 | 94596  | 100696 | 100801 | 102214 |
| 4   | 142311 | 94234  | 100529 | 97441  | 106833 |

Oluşturduğumuz Veri Çerçevemizdeki **Yıl** Sütunu **A**'ya, **Toplam** sütunu **B**'ye, **Ocak** Sütunu da **C**'ye denk geldiği için, çıktımız **Ocak** Ayından başlayıp **G** sütununa denk gelen **Mayıs** ayına kadar olan aralığı alarak çıktı olarak bize sundu.

## skiprows Parametresi (Satırları atla)

Bir Excel çalışma sayfasını ya da farklı kaynaktan alınan veriyi, Pandas ile Veri Çerçevesine (DataFrame'e) dönüştürürken, **bazı satırları atlamamız / göz ardı etmemiz** gerekebilir, bunu `skiprows` parametresi kullanarak yapabiliriz. Bu, parametre olarak, list-like, tamsayı (int) veya callable (isteğe bağlı) değerlerini alır. Bu parametre ile ilk birkaç satırı, seçilen satırı ve belirttiğimiz satır aralığını atlayabiliriz.

```python
basliksiz = pd.read_excel("Veri_Setleri/SatırAtla.xlsx")
print(basliksiz.head(10))
```

|     | Unnamed: 0               | Unnamed: 1 | Unnamed: 2 | Unnamed: 3   |
| --- | ------------------------ | ---------- | ---------- | ------------ |
| 0   | mhg                      | NaN        | NaN        | NaN          |
| 1   | NaN                      | NaN        | 654        | NaN          |
| 2   | NaN                      | NaN        | NaN        | NaN          |
| 3   | Film_Adı                 | Yıl        | Puan       | Oylayan_Kişi |
| 4   | The Shawshank Redemption | 1994       | 9,2        | 1071904      |
| 5   | The Godfather            | 1972       | 9,2        | 751381       |
| 6   | The Godfather: Part II   | 1974       | 9          | 488889       |
| 7   | Pulp Fiction             | 1994       | 8,9        | 830504       |
| 8   | The Dark Knight          | 2008       | 8,9        | 1045186      |
| 9   | 12 Angry Men             | 1957       | 8,9        | 264112       |

Atlamak / gözardı etmek istediğimiz satırları tek tek te belirtebiliriz.

```python
basliksiz = pd.read_excel("Veri_Setleri/SatırAtla.xlsx", 
                        skiprows=[0,1,2,3,5,8,10,12])
print(basliksiz.head(10))
```

|     | Film_Adı                                          | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ---- | ---- | ------------ |
| 0   | The Godfather                                     | 1972 | 9,2  | 751381       |
| 1   | The Godfather: Part II                            | 1974 | 9    | 488889       |
| 2   | The Dark Knight                                   | 2008 | 8,9  | 1045186      |
| 3   | Schindler's List                                  | 1993 | 8,9  | 545703       |
| 4   | Fight Club                                        | 1999 | 8,8  | 814389       |
| 5   | Star Wars: Episode V - The Empire Strikes Back    | 1980 | 8,8  | 519895       |
| 6   | The Lord of the Rings: The Fellowship of the R... | 2001 | 8,8  | 784999       |
| 7   | One Flew Over the Cuckoo's Nest                   | 1975 | 8,7  | 447005       |
| 8   | Goodfellas                                        | 1990 | 8,7  | 465445       |
| 9   | Seven Samurai                                     | 1954 | 8,7  | 161969       |

## Ondalık ve Binlik Ayırıcı Uygulaması

### Ondalık Ayırıcı

Excel dosyası okurken birlikte kullanılabilecek pek çok parametre vardır. Kodun okunurluğunu artırmak adına farklı yazım tarzı da kullanılabilir. Bir örnekle açıklayalım.

```python
import pandas as pd

df = (pd
        .read_csv("nba.xlsx", index_col="Name")
        .groupby("Team")["Age"].mean()
        .nlargest(10)
        .map(lambda x: f"{x:.2f}")
    )
```

Yukarıdaki kodun çıktısına `print(df)` komutu ile bakıp, kod parçalarını teker teker açıklayalım.

Çıktı:

```python
Team
San Antonio Spurs        31.60
Dallas Mavericks         29.73
Cleveland Cavaliers      29.53
Los Angeles Clippers     29.47
Miami Heat               28.93
Memphis Grizzlies        28.39
Atlanta Hawks            28.20
Washington Wizards       27.87
Golden State Warriors    27.67
Los Angeles Lakers       27.53
Name: Age, dtype: object
```

Kod parçalarını açıklayalım;

```python
.read_csv("nba.xlsx", index_col="Name")
```

Bu kod, `py` uzantılı dosya ile aynı konumdaki `nba.xlsx` dosyasını, veri çerçevesine dönüştürüp `df` adına atar. `index` bilgisi olarak `Name` sütunu ayarlanır.

```python
.groupby("Team")["Age"].mean()
```

`Team` yani **Takım** adına göre gruplama yapılır, `Age` yani **Yaş** ortalamaları hesaplatılır.

```python
.nlargest(10)
```

En büyük 10 değer seçilir.

```python
.map(lambda x: f"{x:.2f}")
```

Hesaplanan yaş ortalamalarının ondalık kısmı 2 basamakla sınırlandırılır.

### Binlik Ayırıcı

Bir de **Salary (Maaş)** bilgilerine göre sıralama yapalım ve **binlik ayırıcıyı** görelim.

Maaş toplamlarına göre en yüksek 15 Takım bilgisini görelim;

```python
import pandas as pd

df = (pd
        .read_csv("nba.xlsx", index_col="Name")
        .groupby("Team")["Salary"].sum()
        .nlargest(15)
        .map(lambda x: f"{x:.2f} $")
    )

print(df)
```

Çıktı:

```python
Team
Cleveland Cavaliers      106988689.00 $
Los Angeles Clippers      94854640.00 $
Oklahoma City Thunder     93765298.00 $
Golden State Warriors     88868997.00 $
Chicago Bulls             86783378.00 $
San Antonio Spurs         84442733.00 $
New Orleans Pelicans      82750774.00 $
Miami Heat                82515673.00 $
Charlotte Hornets         78340920.00 $
Memphis Grizzlies         76550880.00 $
Washington Wizards        76328636.00 $
Houston Rockets           75283021.00 $
New York Knicks           73303898.00 $
Atlanta Hawks             72902950.00 $
Los Angeles Lakers        71770431.00 $
Name: Salary, dtype: object
```

Ondalık ayırıcı 2 basamakla sınırlandırıldı ancak binlik ayırıcı ayarlanmadı. O nedenle ücretlerin okunması zor. Kodun `.map(lambda x: f"{x:.2f} $"` kısmında `.2f` 'ten önce  virgül konulursa `.map(lambda x: f"{x:,.2f} $"` binlik ayırıcı olarak virgül belirlenmiş olur. Kodu ve çıktısını görelim;

```python
import pandas as pd

df = (pd
        .read_csv("nba.xlsx", index_col="Name")
        .groupby("Team")["Salary"].mean()
        .nlargest(15)
        .map(lambda x: f"${x:,.2f} $")
    )

print(df)
```

Çıktı:

```python
Team
Cleveland Cavaliers      106,988,689.00 $
Los Angeles Clippers      94,854,640.00 $
Oklahoma City Thunder     93,765,298.00 $
Golden State Warriors     88,868,997.00 $
Chicago Bulls             86,783,378.00 $
San Antonio Spurs         84,442,733.00 $
New Orleans Pelicans      82,750,774.00 $
Miami Heat                82,515,673.00 $
Charlotte Hornets         78,340,920.00 $
Memphis Grizzlies         76,550,880.00 $
Washington Wizards        76,328,636.00 $
Houston Rockets           75,283,021.00 $
New York Knicks           73,303,898.00 $
Atlanta Hawks             72,902,950.00 $
Los Angeles Lakers        71,770,431.00 $
Name: Salary, dtype: object
```

Görüldüğü gibi, maaşın binlik kısımları virgül ile ayrılmı oldu ve okunurluğu kolaylaştırıldı.

İstersek Binlik ayırıcı olarak virgül `,` yerine alt çizgi `_` karakteri de kullanılabilir.

```python
import pandas as pd

df = (pd
        .read_csv("nba.xlsx", index_col="Name")
        .groupby("Team")["Salary"].mean()
        .nlargest(15)
        .map(lambda x: f"${x:_.2f} $")
    )

print(df)
```

Çıktı:

```python
Team
Cleveland Cavaliers      106_988_689.00 $
Los Angeles Clippers      94_854_640.00 $
Oklahoma City Thunder     93_765_298.00 $
Golden State Warriors     88_868_997.00 $
Chicago Bulls             86_783_378.00 $
San Antonio Spurs         84_442_733.00 $
New Orleans Pelicans      82_750_774.00 $
Miami Heat                82_515_673.00 $
Charlotte Hornets         78_340_920.00 $
Memphis Grizzlies         76_550_880.00 $
Washington Wizards        76_328_636.00 $
Houston Rockets           75_283_021.00 $
New York Knicks           73_303_898.00 $
Atlanta Hawks             72_902_950.00 $
Los Angeles Lakers        71_770_431.00 $
Name: Salary, dtype: object
```

## Kaynaklar:

* [pandas.read_excel &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel)

* [Google Gemini](https://gemini.google.com)
