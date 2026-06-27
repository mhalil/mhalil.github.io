Title: Pandas - read_csv
Date: 2022-07-09 20:30
Modified: 2025-11-25 16:35
Category: Pandas
Tags: Python, Pandas, DataFrame, Veri Çerçevesi, read_csv, Kütüphane, Modül, CSV
Author: Mustafa Halil

# read_csv() Fonksiyonu

`read_csv` fonksiyonu, Pandas kütüphanesinin en önemli araçlarından biridir ve temel olarak **virgülle ayrılmış değerler (CSV)** formatındaki dosyaları okuyarak bunları **Veri Çerçevesi (DataFrame)** adı verilen, satır ve sütunlardan oluşan tablo yapısına dönüştürmek için kullanılır.

Basitçe söylemek gerekirse, bu fonksiyon, bilgisayarınızdaki bir veri dosyasını (örneğin, bir Excel dosyasının dışa aktarılan hali gibi) alır ve Python'da kolayca analiz edebileceğiniz, düzenleyebileceğiniz ve işleyebileceğiniz bir tabloya çevirir.

## Sözdizimi:

```python
pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, 
        delimiter=None, header='infer', names=<no_default>, 
        index_col=None, usecols=None, dtype=None, engine=None, 
        converters=None, true_values=None, false_values=None, 
        skipinitialspace=False, skiprows=None, skipfooter=0, 
        nrows=None, na_values=None, keep_default_na=True, 
        na_filter=True, verbose=<no_default>, skip_blank_lines=True, 
        parse_dates=None, infer_datetime_format=<no_default>, 
        keep_date_col=<no_default>, date_parser=<no_default>, 
        date_format=None, dayfirst=False, cache_dates=True, 
        iterator=False, chunksize=None, compression='infer', 
        thousands=None, decimal='.', lineterminator=None, 
        quotechar='"', quoting=0, doublequote=True, escapechar=None, 
        comment=None, encoding=None, encoding_errors='strict', 
        dialect=None, on_bad_lines='error', 
        delim_whitespace=<no_default>, low_memory=True,  
        memory_map=False, float_precision=None, storage_options=None, 
        dtype_backend=<no_default>)
```

## Temel İşlevi:

`pandas.read_csv()`'nin yaptığı şey budur:

1. **Dosyayı bulur ve açar:** Fonksiyona verdiğiniz dosya yolundaki (veya URL'deki) CSV dosyasını açar.

2. **Veriyi okur:** Dosyanın içeriğini satır satır okur.

3. **Ayırıcıyı kullanır:** Her satırdaki verilerin hangi karakterle ayrıldığını (genellikle `,` virgül, ama bazen `;` noktalı virgül veya `\t` sekme olabilir) belirler.

4. **Tablo oluşturur:** Okuduğu veriyi kullanarak bir **Pandas DataFrame** oluşturur. Bu DataFrame, veriyi tablo şeklinde (sütun başlıkları ve satır indeksleri ile) temsil eder.

Bu fonksiyon, dosyanın nerede olduğunu, hangi ayırıcı karakterin kullanıldığını, hangi satırın başlık (header) olduğunu, hangi sütunların veri tipi (dtype) olduğunu ve daha birçok şeyi kontrol etmeniz için çok sayıda **parametreye** sahiptir.

## Başlıca Parametreler:

`pandas.read_csv()` fonksiyonunun en sık kullanılan ve en önemli parametreleri aşağıda tablo halinde açıklanmıştır:

| Parametre                | Tipi                                           | Varsayılan Değer          | Açıklama                                                                                                                                                                                         |
| ------------------------ | ---------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `filepath_or_buffer`     | str, path object veya file-like object         | *Yok*                     | Okunacak dosyanın **yolu** (bilgisayarınızdaki konum) veya **URL'si** (internet adresi). Bu, zorunlu olan tek parametredir.                                                                      |
| `sep` (veya `delimiter`) | str                                            | **','** (virgül)          | Veri sütunlarını birbirinden ayırmak için kullanılan karakter. Örneğin, dosya noktalı virgülle ayrılmışsa (`name;age;city`), `sep=';'` olarak ayarlanır.                                         |
| `header`                 | int, list of int, **'infer'** veya **None**    | **'infer'**               | Sütun isimlerini içeren satırın satır numarası (**0'dan başlar**). `header=0` ilk satırı başlık olarak kullanır. `None` olarak ayarlanırsa Pandas sütunlara otomatik isimler verir (0, 1, 2...). |
| `names`                  | list-like                                      | *Yok*                     | Sütun başlıkları için kullanılacak **isimlerin listesi**. Eğer dosyanın başlık satırı yoksa veya var olan başlıkları geçersiz kılmak istiyorsanız kullanılır.                                    |
| `index_col`              | int, str, list of int veya str                 | **None**                  | Hangi sütunun **satır etiketi** (index) olarak kullanılacağını belirtir. Sütun adı veya sütun numarası olarak verilebilir.                                                                       |
| `dtype`                  | dtype veya dict                                | **None**                  | Sütunların veri tipini (örneğin, tam sayı, metin, ondalıklı sayı) belirlemek için kullanılır. Örneğin, `{'sutun_adı': str}`                                                                      |
| `skiprows`               | int veya list of int                           | **None**                  | Okuma sırasında **atlanacak** satır sayısı veya atlanacak satır numaralarının listesi.                                                                                                           |
| `na_values`              | scalar, list-like veya dict                    | *Varsayılan NA değerleri* | Verideki hangi değerlerin **eksik veri** (`NaN`) olarak yorumlanacağını belirler. Örneğin, `na_values=['N/A', 'eksik']`.                                                                         |
| `parse_dates`            | bool, list of int/str, list of lists veya dict | **False**                 | Hangi sütunların **tarih ve saat** nesnesi olarak ayrıştırılmaya çalışılacağını belirler. `True` ise dizin sütununu ayrıştırmaya çalışır.                                                        |
| `encoding`               | str                                            | **'utf-8'**               | Dosyanın hangi karakter kodlamasıyla (encoding) yazıldığını belirtir. Türkçe karakter sorunu yaşanıyorsa, `encoding='latin1'` veya `encoding='cp1254'` denenebilir.                              |

### `header` parametresi

`read_csv ()` fonksiyonu, CSV dosyasındaki ilk satırı varsayılan olarak bir başlık kabul eder ve bunu Veri Çerçevesi (DataFrame) sütun adları olarak kullanır. CSV dosyasındaki  ilk satırın başlık değil, bir veri olduğu düşünüldüğünde, yani sadece verilerden oluşan CSV dosyası ile çalıştığımızda, `header=None` parametresi kullanılmalıdır. 

İlk olarak bir CSV dosyasını çalışmamıza dahil edip içeriğine bakalım.

```python
import pandas as pd

basliksiz = pd.read_csv("Veri_Setleri/basliksiz.csv")
print(basliksiz
```

|     | 9   | 82  | 246 |
| --- | --- | --- | --- |
| 0   | 7   | 78  | 180 |
| 1   | 8   | 83  | 565 |
| 2   | 6   | 82  | 486 |
| 3   | 4   | 37  | 615 |
| 4   | 2   | 18  | 341 |

Yukarıdaki örnekte gördüğünüz üzere, ilk satır başlık değil, veriden oluşuyor. Bunu `header=None` parametresi ile düzenleyelim.

```python
basliksiz = pd.read_csv("Veri_Setleri/basliksiz.csv", header = None )
print(basliksiz
```

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   | 9   | 82  | 246 |
| 1   | 7   | 78  | 180 |
| 2   | 8   | 83  | 565 |
| 3   | 6   | 82  | 486 |
| 4   | 4   | 37  | 615 |

Bu durumda sütun isimleri (0, 1, 2) otomatik olarak atanır.

### `names` Parametresi

Sadece verilerden oluşan yani başlık satırı bulunmayan bir CSV dosyası ile çalıştığımızda, `header=None` parametresi kullanılmalıdır demiştik. Bu durumda Başlık (sütun adlarını) belirtmek için `names` parametresi kullanılmalı. `names` parametresine değer olarak, sütun sayısı ile eş uzunlukta bir liste tipi veri atanmalı.

Yukarıdaki örnekte gördüğünüz üzere, ilk satır başlık değil, veriden oluşuyor. Bunu `header=None` ve `names` parametreleri ile düzenleyelim.

```python
baslik = ["Birler", "Onlar", "Yüzler"]
basliksiz = pd.read_csv("Veri_Setleri/basliksiz.csv", 
                            header = None, names = baslik )
print(basliksiz
```

|     | Birler | Onlar | Yüzler |
| --- | ------ | ----- | ------ |
| 0   | 9      | 82    | 246    |
| 1   | 7      | 78    | 180    |
| 2   | 8      | 83    | 565    |
| 3   | 6      | 82    | 486    |
| 4   | 4      | 37    | 615    |

### `sep` veya `delimiter` Parametreleri:

Çalıştığımız dosyada verileri birbirinden ayırmak için kullanılan karakteri belirtmek için `sep` ya da `delimiter` parametreleri kullanılır. İkisi de aynı sonucu verir. Örneğin, dosyadaki bilgiler birbirinden noktalı virgülle ayrılmışsa (örneğin: `name; age; city`), `sep=';'` olarak ayarlanır.

Örnek Verimiz (csv dosya içeriğimiz);

```python
 0   | 9   | 82  | 246 
 1   | 7   | 78  | 180 
 2   | 8   | 83  | 565 
 3   | 6   | 82  | 486 
 4   | 4   | 37  | 615 
```

Elimizde, yukarıdaki gibi `|` pipe karakteri ile ayrılmış verilerden oluşan bir csv dosyası olduğunu düşünürsek, `read_csv()` metodunun `sep` ya da `delimiter` parametresini `|` pipe karakteri ile işaret etmemiz gerekir.

```python
import pandas as pd

baslik = ["Birler", "Onlar", "Yüzler"]

df = pd.read_csv("csv.csv", 
            delimiter = "|", # sep  = "|" ifadesi de yazılabilir
            header = None, names = baslik)
print(df)
```

Çıktı:

```python
   Birler  Onlar  Yüzler
0       9     82     246
1       7     78     180
2       8     83     565
3       6     82     486
4       4     37     615
```

### `index_col` Parametresi

`index_col` parametresini anlatmak için **nba.csv** isimli dosyasınının içeriğini çalışmamıza aktarıp, veri çerçevesine dönüştürelim;

```python
import pandas as pd
nba_csv = pd.read_csv("Veri_Setleri/nba.csv")
print(nba_csv)
```

|     | Name          | Team           | Number | Position | Age  | Height | Weight | College           | Salary    |
| --- | ------------- | -------------- | ------ | -------- | ---- | ------ | ------ | ----------------- | --------- |
| 0   | Avery Bradley | Boston Celtics | 0.0    | PG       | 25.0 | 6-2    | 180.0  | Texas             | 7730337.0 |
| 1   | Jae Crowder   | Boston Celtics | 99.0   | SF       | 25.0 | 6-6    | 235.0  | Marquette         | 6796117.0 |
| 2   | John Holland  | Boston Celtics | 30.0   | SG       | 27.0 | 6-5    | 205.0  | Boston University | NaN       |
| 3   | R.J. Hunter   | Boston Celtics | 28.0   | SG       | 22.0 | 6-5    | 185.0  | Georgia State     | 1148640.0 |
| 4   | Jonas Jerebko | Boston Celtics | 8.0    | PF       | 29.0 | 6-10   | 231.0  | NaN               | 5000000.0 |

Harici kaynaktan veri alarak oluşturduğumuz veri çerçevesinin indeks değerini, istediğimiz sütuna eşitleyebiliriz. Bunu yapmak için `index_col` parametresini kullanmalıyız. Örneğin NBA oyuncularının verileri barındıran CSV uzantılı dosyanın **Name** Sütununu, veri çerçevemizin **indeks sütunu** haline getirip veri çerçevemize göz atalım.

```python
nba_csv = pd.read_csv("Veri_Setleri/nba.csv", index_col="Name")
print(nba_csv.head())
```

|               | Team           | Number | Position | Age  | Height | Weight | College           | Salary    |
| ------------- | -------------- | ------ | -------- | ---- | ------ | ------ | ----------------- | --------- |
| Name          |                |        |          |      |        |        |                   |           |
| Avery Bradley | Boston Celtics | 0.0    | PG       | 25.0 | 6-2    | 180.0  | Texas             | 7730337.0 |
| Jae Crowder   | Boston Celtics | 99.0   | SF       | 25.0 | 6-6    | 235.0  | Marquette         | 6796117.0 |
| John Holland  | Boston Celtics | 30.0   | SG       | 27.0 | 6-5    | 205.0  | Boston University | NaN       |
| R.J. Hunter   | Boston Celtics | 28.0   | SG       | 22.0 | 6-5    | 185.0  | Georgia State     | 1148640.0 |
| Jonas Jerebko | Boston Celtics | 8.0    | PF       | 29.0 | 6-10   | 231.0  | NaN               | 5000000.0 |

Gördüğünüz gibi artık **indeks bilgileri**, **Oyuncu isimleri**ne dönüşmüş oldu.

## F-String ile Veri Biçimlendirmek

### Ondalık Ayırıcı

CSV dosyası okurken birlikte kullanılabilecek pek çok parametre vardır. Kodun okunurluğunu artırmak adına aşağıdaki gibi farklı yazım tarzı da kullanılabilir. Bir örnekle açıklayalım.

```python
import pandas as pd

df = (pd
        .read_csv("nba.csv", index_col="Name")
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
.read_csv("nba.csv", index_col="Name")
```

Bu kod, `py` uzantılı dosya ile aynı konumdaki `nba.csv` dosyasını, veri çerçevesine dönüştürüp `df` adına atar. `index` bilgisi olarak `Name` sütunu ayarlanır.

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

Maaş ortalamalarına göre en yüksek 15 Takım bilgisini görelim;

```python
import pandas as pd

df = (pd
        .read_csv("nba.csv", index_col="Name")
        .groupby("Team")["Salary"].mean()
        .nlargest(15)
        .map(lambda x: f"${x:.2f}")
    )

print(df)
```

Çıktı:

```python
Team
Cleveland Cavaliers      $7642049.21
Miami Heat               $6347359.46
Los Angeles Clippers     $6323642.67
Oklahoma City Thunder    $6251019.87
Golden State Warriors    $5924599.80
Chicago Bulls            $5785558.53
San Antonio Spurs        $5629515.53
Memphis Grizzlies        $5467920.00
Charlotte Hornets        $5222728.00
Washington Wizards       $5088575.73
Houston Rockets          $5018868.07
Atlanta Hawks            $4860196.67
Los Angeles Lakers       $4784695.40
Sacramento Kings         $4778911.07
Dallas Mavericks         $4746582.13
Name: Salary, dtype: object
```

Ondalık ayırıcı 2 basamakla sınırlandırıldı ancak binlik ayırıcı ayarlanmadı. O nedenle ücretlerin okunması zor. Kodun `.map(lambda x: f"${x:.2f}"` kısmında `.2f` 'ten önce  virgül konulursa `.map(lambda x: f"${x:,.2f}"` binlik ayırıcı olarak virgül belirlenmiş olur. `f"${x:,.2f}` ifadeki `$` ifadesi ise değerin önüne dolar sembolü ($) eklemek için kullanılır. `Kodu ve çıktısını görelim;

```python
import pandas as pd

df = (pd
        .read_csv("nba.csv", index_col="Name")
        .groupby("Team")["Salary"].mean()
        .nlargest(15)
        .map(lambda x: f"${x:,.2f}")
    )

print(df)
```

Çıktı:

```python
Team
Cleveland Cavaliers      $7,642,049.21
Miami Heat               $6,347,359.46
Los Angeles Clippers     $6,323,642.67
Oklahoma City Thunder    $6,251,019.87
Golden State Warriors    $5,924,599.80
Chicago Bulls            $5,785,558.53
San Antonio Spurs        $5,629,515.53
Memphis Grizzlies        $5,467,920.00
Charlotte Hornets        $5,222,728.00
Washington Wizards       $5,088,575.73
Houston Rockets          $5,018,868.07
Atlanta Hawks            $4,860,196.67
Los Angeles Lakers       $4,784,695.40
Sacramento Kings         $4,778,911.07
Dallas Mavericks         $4,746,582.13
Name: Salary, dtype: object
```

Görüldüğü gibi, maaşın binlik kısımları virgül ile ayrılmı oldu ve okunurluğu kolaylaştırıldı.

İstersek Binlik ayırıcı olarak virgül `,` yerine alt çizgi `_` karakteri de kullanılabilir.

```python
import pandas as pd

df = (pd
        .read_csv("nba.csv", index_col="Name")
        .groupby("Team")["Salary"].mean()
        .nlargest(15)
        .map(lambda x: f"${x:_.2f}")
    )

print(df)
```

Çıktı:

```python
Team
Cleveland Cavaliers      $7_642_049.21
Miami Heat               $6_347_359.46
Los Angeles Clippers     $6_323_642.67
Oklahoma City Thunder    $6_251_019.87
Golden State Warriors    $5_924_599.80
Chicago Bulls            $5_785_558.53
San Antonio Spurs        $5_629_515.53
Memphis Grizzlies        $5_467_920.00
Charlotte Hornets        $5_222_728.00
Washington Wizards       $5_088_575.73
Houston Rockets          $5_018_868.07
Atlanta Hawks            $4_860_196.67
Los Angeles Lakers       $4_784_695.40
Sacramento Kings         $4_778_911.07
Dallas Mavericks         $4_746_582.13
Name: Salary, dtype: object
```

F-String konusunu incelemek isterseniz, konunun detaylarına [BURADAN]({filename}../f-string.md) ulaşabilirsiniz.

## Kaynaklar:

* [pandas.read_csv &#8212; pandas 2.3.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

* [Google Gemini](https://gemini.google.com)
