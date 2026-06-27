Title: Pandas 10 - pivot_table() Fonksiyonunun Kullanımı
Date: 2022-07-19 15:15
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, pivot, table, pivot table
Author: Mustafa Halil

# Pandas'ta Pivot Table (Özet Tablo) Fonksiyonunun Kullanımı

Verilerinize ilişkin özet tablola oluşturmak konusunda, Excel'deki pivot tablolara aşina olabilirsiniz. Burada, `.pivot_table()` metodunu kullanarak Python ve Pandas'ta nasıl pivot (özet) tablolar oluşturacağımızı öğreneceğiz. Elimden geldiğince öğrendiklerimi bu 
sayfaya ekleyeceğim.

Pivot Tablolar, verileri hızlı bir şekilde özetleyebilmek, verilerinizin nasıl göründüğüne dair bir fikir edinebilmek için önemli bir beceridir. İşlev, Pandas'ta da bulunan
 `.groupby()` yöntemine oldukça benzer, ancak burada daha sonra göreceğimiz gibi, önemli ölçüde daha fazla özelleştirme sunar.

Bu eğitimin sonunda şunları öğrenmiş olacaksınız:

- `pivot_table()` fonksiyonu nasıl kullanılır? ve parametreleri neyi temsil eder.
- Tekil indeks veya çoklu indeks kullanarak veriler nasıl gruplanır?
- İndeksler ve sütunlar kullanılarak tablo nasıl daha farklı hale döndürülür?
- Kendi toplama yöntemlerinizi nasıl belirleyip oluşturabilirsiniz?
- Toplamlar nasıl hesaplanır ve eksik verilerle nasıl başa çıkılır?

## Python'da Pivot Tablo Nasıl Oluşturulur

Pivot tablo, daha büyük bir tablonun verilerini, bu verileri **'işleyerek'** özetlemeye yardımcı olan bir istatistik tablosudur. Microsoft Excel, PivotTable olarak bilinen pivot tabloyu popüler hale getirdi. Pandas, `.pivot_table()` fonksiyonunu kullanarak, Python'da özet tablolar oluşturmaya imkan sağlar. Fonksiyon, aşağıdaki varsayılan parametrelere sahiptir:

```python
    # .pivot_table() fonksiyonunun sözdizimi;
    import pandas as pd
    pd.pivot_table(
    data=,
    values=None, 
    index=None, 
    columns=None, 
    aggfunc='mean', 
    fill_value=None, 
    margins=False, 
    dropna=True, 
    margins_name='All', 
    observed=False,
    sort=True )     
```

Metot/Yöntem bir Veri Çerçevesi (DataFrame) alır ve ardından bir DataFrame döndürür. Aşağıdaki tablo, fonksiyonda bulunan parametrelere genel bir bakış sağlar:

| Parametre     | Varsayılan Değer | Tanım / Açıklama                                                                                                                                                                  |
| ------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data=         |                  | Özet Tablo haline getirilecek (Döndürülecek) Veri Çerçevesi (DataFrame)                                                                                                           |
| values=       |                  | Toplanacak sayı değerlerinin bulunduğu sütun (boşsa, tüm sayısal değerleri toplayacaktır)                                                                                         |
| index=        |                  | Verilerin gruplanacağı sütun veya sütunlar. Tekil sütun için bir <br>dize/string ifade olabilirken, çoklu sütunlar için bir dize/string <br>listesi (**list()** yapısı) olmalıdır |
| columns=      |                  | Verilerin gruplanacağı sütun veya sütunlar. Tekil sütun için bir <br>dize/string ifade olabilirken, çoklu sütunlar için bir dize/string <br>listesi (**list()** yapısı) olmalıdır |
| aggfunc=      | ‘mean’           | Sayısal Veriler için "ortalama, toplama,...vb" fonksiyon veya fonksiyon listesi                                                                                                   |
| fill_value=   |                  | Eksik / Kayıp değerlerin yerine atanacak değer                                                                                                                                    |
| dropna=       | True             | Tüm girişlerin **NaN** olduğu sütunları dahil etmemeyi seçmek için kullan                                                                                                         |
| margins=      | False            | Satır ve Sütunlar ekleyin Toplam değerleri ekle                                                                                                                                   |
| margins_name= | ‘All’            | Toplam satır/sütun adı                                                                                                                                                            |
| observed=     | False            | Sadece kategorik veriler içindir - Eğer `True` ise, sadece kategorik gruplar için gözlemlenen değerleri gösterir                                                                  |
| sort=         | True             | Elde edilen değerlerin sıralanıp sıralanmayacağını belirtir.                                                                                                                      |

Artık fonksiyonda bulunan parametreleri anladığınıza göre, veri setimizi yükleyelim ve verilerimizi keşfetmeye başlayalım.

## Örnek Veri Çerçevesi (DataFrame) Oluşturalım

Bu eğitimi takip etmek için örnek bir Pandas Veri Çerçevesi (DataFrame) oluşturalım. DataFrame'i aşağııdaki GitHub sayfasındaki ilgili dosyadan `pd.read_excel()` işlevini kullanarak yükleyebiliriz. Ardından, `.head()` yöntemini kullanarak veri kümesinin ilk beş kaydını yazdırabiliriz.

```python
import pandas as pd
df = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/sample_pivot.xlsx', parse_dates=['Date'])
print(df.head())
```

|     | Date       | Region | Type                | Units | Sales |
| --- | ---------- | ------ | ------------------- | ----- | ----- |
| 0   | 2020-07-11 | East   | Children's Clothing | 18.0  | 306   |
| 1   | 2020-09-23 | North  | Children's Clothing | 14.0  | 448   |
| 2   | 2020-04-02 | South  | Women's Clothing    | 17.0  | 425   |
| 3   | 2020-02-28 | East   | Children's Clothing | 26.0  | 832   |
| 4   | 2020-03-19 | West   | Women's Clothing    | 3.0   | 33    |

Yukarıda gösterilen çıktıya dayanarak, çalışmak için beş sütunumuz olduğunu görebiliriz:

| Sütun Adı | Tanım/Açıklama       |
| --------- | -------------------- |
| Date      | İşlem tarihi         |
| Region    | İşlem bölgesi        |
| Type      | Satılan giysi türü   |
| Units     | Satılan birim sayısı |
| Sales     | Satışın maliyeti     |

Artık verilerle ilgili biraz daha fazla bilgimiz olduğuna göre, Pandas'ta ilk Pivot (Özet) Tablomuzu oluşturalım.

## Pandas'ta Pivot Tablo Oluşturmak

İlk Pandas pivot tablonuzu oluşturalım. En azından, `index=` veya `column=` parametrelerini kullanarak bir tür grup anahtarı belirlemeliyiz. 
Aşağıdaki örneklerde DataFrame fonksiyonu yerine Pandas fonksiyonunu 
kullanıyoruz. Bu nedenle, `data=` parameresini belirtmemiz gerekiyor. Yöntemi doğrudan DataFrame'e uygularsak (örneğin: `df.pivot_table(...)`), bu parametre `data= df` şeklinde ima edilmiş olur.

```python
sales_by_region = pd.pivot_table(data=df, index='Region')
print(pivot)
```

| Region | Sales      |
| ------ | ---------- |
| East   | 408.182482 |
| North  | 438.924051 |
| South  | 432.956204 |
| West   | 452.029412 |

Yukarıdaki kodu, daha anlaşılır olduğunu düşünenler aşağıdaki şekilde yazıp çalıştırabilir. İkisi de aynı sonucu verir.

```python
sales_by_region = pd.pivot_table(
    data=df,
    index='Region'
)
print(pivot)
```

| Region | Sales      |
| ------ | ---------- |
| East   | 408.182482 |
| North  | 438.924051 |
| South  | 432.956204 |
| West   | 452.029412 |

Çıktıyı parçalara bölüp irdeleyelim.

1. `pd.pivot_table()` fonksiyonu kullanılarak oluşturulan, **sales_by_region** adlı yeni bir DataFrame oluşturduk.
2. Veri Çerçevesi (DataFrame) olarak, `df`'yi belirtik ve `index='region'` parametresi ile **region** sütununu indeks değeri olarak belirledik, yani veriler bölge sütununa göre gruplanacak.

Diğer tüm parametreler varsayılan değerlerine bırakıldığı için Pandas şu varsayımı yaptı:

- Veriler, her sütunun ortalamasına göre toplanmalıdır (aggfunc='mean')
- Değerler herhangi bir sayısal sütun olmalıdır

## Pandas Özet Tablosunda Sadece Belirli Sütunları Toplamak

Yukarıdaki örnekte, `values=` parametresini değiştirmediniz. Bu nedenle, tüm sayısal sütunlar toplanmış oldu. Bu, her zaman ideal olmayabilir. Bu nedenle Pandas, tek bir sütunu temsil eden tek bir dize/string veya birden çok sütunu temsil eden bir 
dizi/string listesi iletmemize izin verir.

Şimdi kodumuzu, sadece **Satışların (Sales)** ortalamasını hesaplayacak şekilde değiştirelim:

```python
pivot = pd.pivot_table(data=df, index='Region', values='Sales')
print(pivot)
```

| Region | Sales      |
| ------ | ---------- |
| East   | 408.182482 |
| North  | 438.924051 |
| South  | 432.956204 |
| West   | 452.029412 |

Tüm sayısal sütunları toplamak yerine yalnızca belirtilen sütunun toplandığını görebiliriz.

## Pandas Özet Tablosunda Toplama Yöntemleriyle Çalışmak

Pandas'ta ilk pivot tablonuzu oluşturduğunuza göre, şimdi toplama yöntemlerini değiştirmeye çalışalım. Bu, verilerinizin nasıl bir araya getirilmesini istediğinizi belirtmenize olanak tanır. Pandas'ın gücünün gerçekten ortaya çıktığı yer burasıdır ve karmaşık analizleri kolaylıkla hesaplamanıza olanak tanır.

## Pandas Özet Tablosunda Toplama Yöntemini Belirtmek

Verilerin bir pivot tabloda nasıl toplandığını değiştirmek için `aggfunc=` (aggregation function yani toplama fonksiyonu) parametresini kullanabilirsiniz. Pandas, varsayılan olarak verileri toplamak için `.mean()` yöntemini kullanır. `'mean'`, `'sum'` veya `'max'` gibi adlandırılmış bir işlevi veya `np.mean` gibi çağrılabilir bir fonksiyon/işlevi iletebilirsiniz.

Şimdi tüm bölgelerdeki satışlarımızın **toplamını** bulmak için davranışımızı değiştirmeye çalışalım:

```python
pivot = pd.pivot_table(data=df, index='Region', aggfunc='sum')
print(pivot)
```

| Region | Sales  | Units  |
| ------ | ------ | ------ |
| East   | 167763 | 8110.0 |
| North  | 138700 | 4359.0 |
| South  | 59315  | 2798.0 |
| West   | 61476  | 2624.0 |

## Pandas DataFrame'de Çoklu Toplama Yöntemi

Benzer şekilde, bir Pandas pivot tablosuna birden çok toplama yöntemi belirtebiliriz. Bu oldukça kolaydır ve sadece bir fonksiyon listesi yazmanızı gerektirir ve fonksiyon, tüm değer barındıran sütunlarına uygulanır. Hem **ortalama** hem de **toplam** için değerler üretelim:

```python
pivot = pd.pivot_table(data=df, index='Region', aggfunc=['mean', 'sum'])
print(pivot)
```

| Region | mean       |           | sum    |        |
| ------ | ---------- | --------- | ------ | ------ |
|        | Sales      | Units     | Sales  | Units  |
| East   | 408.182482 | 19.732360 | 167763 | 8110.0 |
| North  | 438.924051 | 19.202643 | 138700 | 4359.0 |
| South  | 432.956204 | 20.423358 | 59315  | 2798.0 |
| West   | 452.029412 | 19.294118 | 61476  | 2624.0 |

Bunun ne kadar kolay olduğunu ve ne kadar daha fazla veri sağladığını görebiliyoruz! Sayısal verileri içeren her sütun için hem **ortalama** hem de **toplam** oluşturuldu.

## Farklı Sütunlar için Farklı Toplama Yöntemi Belirtmek

Şimdi, Farklı Sütunlar için Farklı Toplama Yöntemi Belirtmek istediğinizi hayal edin. 
Bunu yapmak için, aşağıdaki anahtar/değer çifti biçimini içeren bir **sözlüğü** iletebilirsiniz: `'sütun': fonksiyon`. `Birimlerin (Units) toplamını ve ortalama satış sayısını` hesaplamak istediğimizi varsayalım:

```python
pivot = pd.pivot_table(
    data=df,
    index='Region',
    aggfunc={'Sales': 'mean', 'Units': 'sum'}
)

print(pivot)
```

| Region | Sales      | Units  |
| ------ | ---------- | ------ |
| East   | 408.182482 | 8110.0 |
| North  | 438.924051 | 4359.0 |
| South  | 432.956204 | 2798.0 |
| West   | 452.029412 | 2624.0 |

Bu, aynı DataFrame'de farklı temel performans göstergeleri arasında karşılaştırılan verileri kolayca görmenizi sağlar.

## Pandas'ta Özet Tablolarında Özel Toplamaları

Pandas, ayrıca özel bir fonksiyonu **.pivot_table()** fonksiyonu olarak kullanmanızı (pandas fonksiyonuna dönüştürmeyi) sağlar. Bu, ihtiyaçlarınıza göre özel olarak tasarlanmış analizlerle çalışma yeteneğimizi büyük ölçüde genişletir! Bir sütunun ortalamasını herhangi bir aykırı değer olmadan hesaplayan bir fonksiyona nasıl 
dönüştürebileceğimizi görelim.

Pandas, veri aralığındaki yüzdelerine göre seçmek istediğimiz bir dizi değeri tanımlamamıza izin veren bir **.quantiles()** yöntemiyle birlikte gelir. Diyelim ki, verilerin üst ve alt **%10**'unu kaldırarak bir sütunun ortalamasını hesaplamak istedik. Aşağıdaki fonksiyonu tanımlayabiliriz:

```python
import numpy as np
def mean_no_outliers(values):
    no_outliers = values.quantile([0.1, 0.9])
    mean = np.mean(no_outliers)
    return mean
```

Yukarıdaki fonksiyon, `.pivot_table()` fonksiyonu tarafından iletilen `değerler (values)` olacak olan tek bir parametreyi kabul eder. Değerler daha sonra `.quantile()` metodu/yöntemi kullanılarak filtrelenir. Son olarak, bu değerlerin 
ortalaması hesaplanır. Satış (Sales) sütunumuza uygulanan pivot tablomuzda bunu (ve normal `ortalama (mean)` toplamayı) nasıl kullanabileceğimizi görelim.

```python
pivot = pd.pivot_table(
    data=df,
    index='Region',
    aggfunc=['mean', mean_no_outliers],
    values='Sales'
)

print(pivot)
```

| Region | mean       | mean_no_outliers |
| ------ | ---------- | ---------------- |
|        | Sales      | Sales            |
| East   | 408.182482 | 436.0            |
| North  | 438.924051 | 484.5            |
| South  | 432.956204 | 434.1            |
| West   | 452.029412 | 497.0            |

## Daha Karmaşık Pandas Pivot Tabloları

Artık `.pivot_table()` fonksiyonunun Pandas'ta nasıl kullanıldığını anladığınıza göre, şimdi anlayışımızı nasıl genişletebileceğimize bir göz atalım. Bu bölümde, Pandas pivot 
tablolarımıza nasıl sütun ve çoklu indeks ekleyeceğinizi öğreneceksiniz.

## Pandas Özet Tablosuna Sütun Eklemek

Bir Pandas pivot tablosuna sütun eklediğimizde, verilere başka bir boyut ekleriz. `index=` parametresi verileri dikey olarak bölerken, `column=` parametresi verileri yatay olarak gruplar ve böler. Bu, okunması kolay bir tablo oluşturmamızı sağlar. Verileri **Type** sütununa göre bölmek için `column=` parametresini nasıl kullanabileceğimizi görelim.

```python
pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales'
)

print(pivot)
```

| Type       | Children's Clothing | Men's Clothing | Women's Clothing |
| ---------- | ------------------- | -------------- | ---------------- |
| **Region** |                     |                |                  |
| East       | 405.743363          | 423.647541     | 399.028409       |
| North      | 438.894118          | 449.157303     | 432.528169       |
| South      | 412.666667          | 475.435897     | 418.924528       |
| West       | 480.523810          | 465.292683     | 419.188679       |

Tamamen başka bir veri boyutunu eklemenin ne kadar kolay olduğunu görebiliriz. Bu, gruplandırmalar arasındaki farkları okunması kolay bir biçimde belirlememizi sağlar.

## Pandas Özet Tablolarına Birden Çok Dizin Eklemek

Sütunlar yatay bir boyut eklerken, verilerimizde mantıksal bir hiyerarşi olduğunda birden çok dizin de belirtebiliriz. Örneğin, pivot tablomuza bir tarih boyutu ekleyebiliriz. Verilerimizi çeyreklere göre gruplandırmak için Pandas'ın yerleşik tarih formatını kullanalım. Bu, daha sonra, verilerimizi belirli bir süre boyunca görselleştirmemizi 
sağlar. Bunun nasıl çalıştığını görelim:

```python
pivot = pd.pivot_table(
    data=df,
    index=['Region',df['Date'].dt.quarter],
    columns='Type',
    values='Sales'
)

pivot.head()
```

|            | Type       | Children's Clothing | Men's Clothing | Women's Clothing |
| ---------- | ---------- | ------------------- | -------------- | ---------------- |
| **Region** | **Date**   |                     |                |                  |
| East       | 1          | 423.241379          | 369.250000     | 428.948718       |
| 2          | 274.800000 | 445.425000          | 456.816327     |                  |
| 3          | 425.382353 | 506.421053          | 342.386364     |                  |
| 4          | 453.866667 | 405.666667          | 364.795455     |                  |
| North      | 1          | 394.727273          | 450.869565     | 489.944444       |

Bu, çok indeksli bir Pandas DataFrame döndürür. Daha karmaşık görünse de, çok indeksli bir Pandas DataFrame'deki verilere erişim, diğer herhangi bir DataFrame'deki verilere erişmeye oldukça benzer şekilde çalışır. Bununla birlikte, artık 1 yerine **iki dizin sütunumuz** olduğundan, bir dize/string dizini iletebiliriz. Diyelim sadece **Doğu Bölgesi(East), Çeyrek 1** ve **Erkek giyim (Men's Clothing)** kesişimine erişmek istedik, bu durumda, aşağıdaki kodu kullanabiliriz:

```python
print(pivot.loc[('East', 1), "Men's Clothing"])
```

```
369.25
```

## Panda Pivot Tablolarını Özelleştirmek

Bu başlık altında, Pandas pivot tablolarınızı nasıl özelleştireceğinizi öğreneceksiniz. Bu, toplamları ekleme ve eksik verilerle çalışma gibi daha da fazla özelleştirme eklemenize olanak tanır. Ayrıca, belirli bir değerle ortaya çıkan bir pivot tabloda, eksik verileri nasıl dolduracağınızı da öğreneceksiniz.

## Pandas Özet Tablolarına Toplamların Eklemesi

Pandas pivot tablosuna toplamları nasıl ekleyeceğinizi öğrenerek başlayalım. Bu, bir boole değeri kabul eden `margins=` parametresi tarafından kontrol edilir. Varsayılan olarak bu, `False` olarak ayarlanmıştır, ancak `True` olarak değiştirildiğinde, **toplamlar satırlara ve sütunlara eklenir**. Bunun neye benzediğini görelim:

```python
pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales',
    margins=True
)

print(pivot)
```

| Type       | Children's Clothing | Men's Clothing | Women's Clothing | All        |
| ---------- | ------------------- | -------------- | ---------------- | ---------- |
| **Region** |                     |                |                  |            |
| East       | 405.743363          | 423.647541     | 399.028409       | 408.182482 |
| North      | 438.894118          | 449.157303     | 432.528169       | 438.924051 |
| South      | 412.666667          | 475.435897     | 418.924528       | 432.956204 |
| West       | 480.523810          | 465.292683     | 419.188679       | 452.029412 |
| All        | 427.743860          | 444.257732     | 415.254717       | 427.254000 |

Varsayılan olarak, Pandas toplamları 'All (Tümü)' olarak adlandırır. 
Bu etiketleri yeniden adlandırmak istiyorsanız, değerleri yeniden etiketlemek üzere bir dize/string iletmek için `margins_name=` parametresini kullanabilirsiniz.

```python
pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales',
    margins=True,
    margins_name='Total'
)

print(pivot)
```

| Type       | Children's Clothing | Men's Clothing | Women's Clothing | Total      |
| ---------- | ------------------- | -------------- | ---------------- | ---------- |
| **Region** |                     |                |                  |            |
| East       | 405.743363          | 423.647541     | 399.028409       | 408.182482 |
| North      | 438.894118          | 449.157303     | 432.528169       | 438.924051 |
| South      | 412.666667          | 475.435897     | 418.924528       | 432.956204 |
| West       | 480.523810          | 465.292683     | 419.188679       | 452.029412 |
| Total      | 427.743860          | 444.257732     | 415.254717       | 427.254000 |

## Pandas Özet Tablosunda Eksik/Kayıp Verilerle Başa Çıkmak

Pandas hiçbir verinin olmadığı bir kesitle karşılaştığında, ortaya çıkan pivot tabloya bir `NaN` değeri ekler. DataFrame'imizi bazı eksik verileri içerecek şekilde değiştirelim:

```python
import numpy as np
df.loc[(df['Region'] == 'East') & (df['Type'] == "Children's Clothing"), 'Sales'] = np.NaN

pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales',
)

print(pivot)
```

| Type       | Children's Clothing | Men's Clothing | Women's Clothing |
| ---------- | ------------------- | -------------- | ---------------- |
| **Region** |                     |                |                  |
| East       | NaN                 | 423.647541     | 399.028409       |
| North      | 438.894118          | 449.157303     | 432.528169       |
| South      | 412.666667          | 475.435897     | 418.924528       |
| West       | 480.523810          | 465.292683     | 419.188679       |

Özellikle teknik bilgisi olmayan kullanıcılar için bir `NaN` değeri görmek her zaman ideal olmayabilir. Bu nedenle Pandas, bu eksik veri noktalarını doldurmak için bir değer iletmenizi sağlayan `fill_value=` parametresini sunar. Örneğin, tüm bu `NaN` değerleri **0** ile doldurmak istersek, basitçe bu parametreyi ekleyebiliriz:

```python
import numpy as np
df.loc[(df['Region'] == 'East') & (df['Type'] == "Children's Clothing"), 'Sales'] = np.NaN

pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales',
    fill_value=0
)

print(pivot)
```

| Type       | Children's Clothing | Men's Clothing | Women's Clothing |
| ---------- | ------------------- | -------------- | ---------------- |
| **Region** |                     |                |                  |
| East       | 0.000000            | 423.647541     | 399.028409       |
| North      | 438.894118          | 449.157303     | 432.528169       |
| South      | 412.666667          | 475.435897     | 418.924528       |
| West       | 480.523810          | 465.292683     | 419.188679       |

## Pandas Özet Tablo Verilerini Sıralamak

Pandas'a, sürüm 1.3.0'dan başlayarak, elde edilen DataFrame'i sıralamanıza olanak tanıyan yeni bir parametre eklendi. Eskiden, önce DataFrame'i oluşturmanız ve ardından verileri sıralamak için bir yöntem iletmeniz gerekirdi. Şimdi, elde ettiğiniz DataFrame'inizi sıralamaya yardımcı olması için `sort=True` parametresini/argümanını basitçe iletebilirsiniz.

```python
pivot = pd.pivot_table(
    data=df,
    index='Region',
    values='Sales',
    sort=True
)

print(pivot)
```

| Region | Sales      |
| ------ | ---------- |
| East   | 409.107383 |
| North  | 438.924051 |
| South  | 432.956204 |
| West   | 452.029412 |

Pandas varsayılan olarak pivot tabloyu artan düzende sıralar. Ne yazık ki, daha karmaşık sıralama için (farklı sütunlar arasında olduğu gibi), yine de `.sort_values()` yöntemini peşpeşe uygulamanız gerekir.

## Python Pivot Tablolarını Filtrelemek

Bu başlıkta, bir Pandas pivot tablosunu nasıl filtreleyeceğinizi öğreneceksiniz. Pivot tablolar genellikle oldukça büyük olabileceğinden, bir pivot tabloyu filtrelemek sonuçlara odaklanmayı sağlar. Fonksiyon bir DataFrame döndürdüğünden, DataFrame'i başka herhangi bir filtrede yaptığınız gibi filtreleyebilirsiniz. **Çeyrekler ve bölgeler (quarters and regions)** üzerinden değerler toplayarak pivot tablomuzu yeniden oluşturalım.

```python
pivot = pd.pivot_table(
    data=df,
    index=['Region', df['Date'].dt.quarter],
    values='Sales'
)

pivot.head()
```

| Region | Date | Sales      |
| ------ | ---- | ---------- |
| East   | 1    | 400.293333 |
|        | 2    | 451.696629 |
|        | 3    | 391.857143 |
|        | 4    | 380.338028 |
| North  | 1    | 462.142857 |

Şimdi yapabileceğimiz şey, ya skaler bir değere ya da dinamik bir değere göre filtrelemek. Örneğin, sabit kodlanmış bir değere göre basitçe filtreleyebiliriz. Ancak, örneğin, sadece Satış ortalamasının (Sales average) genel ortalamadan (overall average) daha büyük olduğu kayıtları gösterecek şekilde filtrelemek istedik, aşağıdaki filtreyi 
yazabiliriz:

```python
print(pivot[pivot['Sales'] > pivot['Sales'].mean()])
```

| Region | Date | Sales      |
| ------ | ---- | ---------- |
| East   | 2    | 451.696629 |
| North  | 1    | 462.142857 |
|        | 2    | 442.034884 |
|        | 3    | 447.200000 |
| South  | 1    | 465.263158 |
| 2      | 2    | 440.628571 |
| West   | 1    | 475.000000 |
|        | 3    | 444.884615 |
|        | 4    | 466.209302 |

Bu kod, tam olarak istediğimizi görmemizi sağladı.

## Sonuç ve Özet

Bu eğitim içeriğinde, doğrudan bir Pandas DataFrame'den Excel stili pivot tablolar oluşturmak için Pandas `.pivot_table()` fonksiyonunun/işlevinin nasıl kullanılacağını öğrendiniz. 
Fonksiyon/İşlev, çok çeşitli parametreler aracılığıyla önemli esneklik sağlar. Aşağıdaki bölüm, öğrendiklerinizin bir özetini sunar:

- Pandas pivot_table() fonksiyonu, Excel stili pivot tablolar oluşturmak için tanıdık bir arabirim sağlar
- Fonksiyonlar, verilerin satır ve sütunlara göre nasıl bölüneceğini/gruplanacağını belirtmek için en azından `index=` veya `column=` parametrelerini gerektirir.
- Fonksiyon, özel işlevlerin kullanılması da dahil olmak üzere bir veya birden çok toplama yöntemini hesaplayabilir
- Fonksiyon, diğer herhangi bir DataFrame gibi filtrelenebilen veya sorgulanabilen bir DataFrame döndürür.

### Kaynak:

Bu Eğitimin hazırlanmasında faydalandığım kaynağın bağlantısını paylaşmak istiyorum. [Pivot Tables in Pandas with Python for Python and Pandas - datagy](https://datagy.io/python-pivot-tables/)

[← Önceki Bölüm](pandas-09-veri-gruplama-yontemleri.html) | [Sonraki Bölüm →](pandas-11-melt-fonksiyonunun-kullanimi.html)

