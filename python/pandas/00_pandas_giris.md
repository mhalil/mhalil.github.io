Title: Pandas - Giriş
Date: 2022-07-09 20:20
Modified:2025-11-30 15:20
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül
Author: Mustafa Halil

# Pandas Kütüphanesi Notları

**Python'a Giriş** konusuna ait notları, FreeCAD için Python ile Komut Dosyası Oluşturma (Scripting) Eğitiminde paylaşmıştık.  İlave olarak Python'ın en güçlü ve işlevsel kütüphanelerinden biri olan **Pandas**'a ait notları paylaşmaya devam ediyorum.

![pandas](../../images/pandas_logo.png)

## PANDAS NEDİR?

**Python'a Giriş** konusu ile alakalı bilgileri, [FreeCAD Eğitim Notları]({filename}../../freecad/scripting/freecad_scripting.md) bölümünde [1. Python'a Giriş]({filename}../../freecad/scripting/freecad_01_pythona_giris.md) başlığı altında paylaşmıştık. Python'da yeniyseniz ya da Python 
hakkında hiç bir şey bilmiyorsanız, öncelikle bu bölüme göz atmanızı öneririm.  

Önceki bölüme ilave olarak burada, Python'ın en güçlü ve işlevsel kütüphanelerinden biri olan **Pandas** notlarını paylaşmaya devam ediyorum.

Pandas Kütüphanesinin ne olduğu ve bu kütüphane ile (**Özellikle Veri Çerçevesi (Data Frame) konusunda**) neler yapılabildiğine dair öğrendiklerimi bu bölümde paylaşıyorum.

**Pandas**, veri işleme ve veri analizi için yazılmış olan Python kütüphanesidir.

Bu kütüphane, **Seriler (Series)** ve **Veri Çerçevesi (DataFrame)** isimli iki veri yapısının üzerine kurulmuştur. Serileri tek boyutlu diziler, Veri Çerçevelerini ise iki boyutlu matrisler (SQL ya da Excel tabloları) gibi düşünebiliriz.

**Pandas kütüphanesinin özellikleri**

- İndeksli DataFrame (veri çerçevesi) objeleri ile veri işlemesi yapabilmek.
- Hafızadaki veya farklı türlerde bulunan veriyi okuyabilmek ve yazabilmek için araçlar sağlamak.
- Veri sıralama ve bütünleşik kayıp veri senaryolarına karşı esnek imkanlar sunmak
- Veri setlerinin tekrar boyutlandırılması veya döndürülmesi.
- Etiket bazlı dilimleme, özel indeksleme ve büyük veri setlerini ayrıştırmak
- Veri çerçevesine sütun ekleme veya var olan sütunu çıkarma/silme.
- Veri gruplama özelliği ile ayırma-birleştirme uygulamaları yapılabilmek.
- Veri setlerini birleştirilmek ve birbirine eklemek.
- Çok boyutlu veriden, daha az boyutlu veri elde edilebilmek.
- Veri filtrelemek.

Kütüphane performans konusunda son derece iyidir. Bu yüzden kütüphanenin önemli parçaları CPython ve C üzerinde yazılmışlardır.

**NOT:**  
Eğitimlerde kullandığım Veri Setlerine [GitHub adresimden](https://github.com/mhalil/Pandas_Notlari/tree/main/Veri_Setleri) erişebilirsiniz.

# Pandas Fonksiyonları

## VERİ ÇERÇEVESİ (DATA FRAME) OLUŞTUR

Bu başlık altında, sıfırdan **Veri Çerçevesi** (**Data Frame**) oluşturma ya da harici kaynaktan **(MS Excel, LibreOfis Calc, CSV, JSON, URL ve Pano'dan)** okunarak veri çerçevesi oluşturma konularında kullanabileceğimiz Fonksiyonlar anlatılmıştır.

* [`DataFrame()` Metodu](pandas-dataframe.html)

* [`read_csv()` Metodu](pandas-read_csv.html)
  
  *...... `header` Parametresi*
  
  *...... `names` Parametresi*
  
  *...... `sep` ve `delimiter` Parametreleri*
  
  *...... `index_col` Parametresi*
  
  *...... Ondalık ve Binlik Ayırıcı Uygulaması*

* [`read_clipboard()` Metodu](pandas-read_clipboard.html)

* [`read_excel()` Metodu](pandas-read_excel.html)
  
  *...... `header` ve `names` Parametreleri*
  
  *...... `sheet_name` Parametresi*
  
  *...... `decimal` Parametresi*
  
  *...... `index_col` Parametresi*
  
  *...... `usecols` Parametresi (Sütunları Atla)*
  
  *...... `skiprows` Parametresi (Satırları atla)*
  
  *...... Ondalık ve Binlik Ayırıcı Uygulaması*

* [`read_html()` Metodu](pandas-read_html.html)

* [`read_json()` Metodu](pandas-read_json.html)

* [`read_table()` Metodu](pandas-read_table.html) 
  
  *...... `delimiter` Parametresi*

## VERİYİ KEŞFET (İNCELE)

Bu başlık altında, **Veri Çerçevesi** (**Data Frame**) içeriğini, sayısal bazı değerlerini ve biçimlerinin görüntülemeye dair fonksiyonları öğreneceğiz.

* [`columns` Metodu]({filename}columns.md) 

* [`describe()` Metodu]({filename}describe.md) 

* [`dtypes` Metodu]({filename}dtypes.md) 

* [`head()` Metodu]({filename}head.md) 

* [`index` Metodu]({filename}index.md) 

* [`info()` Metodu]({filename}info.md) 

* [`isin()` Metodu]({filename}isin.md) 

* [`median()` Metodu]({filename}median.md)

* [`mode()` Metodu]({filename}mode.md)

* [`shape` Metodu]({filename}shape.md) 

* [`tail()` Metodu]({filename}tail.md) 

* [`unique()` ve `nunique()` Metotları]({filename}unique_nunique.md)  

* [`value_counts()` Metodu]({filename}value_counts.md) 

## VERİ SEÇİM YÖNTEMLERİ

Bu başlık altında, Veri Çerçevesi oluştururken ya da oluşturduktan sonra istenilen satır ve sütunların seçilmesi ya da seçilmemesi konusunda kullanabileceğimiz Fonksiyonları / metotları inceleyelim. Veri çerçevesinde işimize yaramayacak verileri devre dışı bırakmak için bu yöntemleri kullanabiliriz.

* [`at[]` Metodu]({filename}at.md) 

* [`iat[]` Metodu]({filename}iat.md) 

* [`Index()` Metodu]({filename}pandas-index.md) 

* [`iloc[]` Metodu]({filename}iloc.md) 

* [`loc[]` Metodu]({filename}loc.md) 

## EKSİK - KAYIP VERİ YÖNTEMLERİ

Bu başlık altında, Veri çerçevemizde eksik veri (excel tablosundaki boş hücre gibi düşünebiliriz) olup olmadığını, varsa kaç adet olduğunu tespit edebileceğimiz Pandas fonksiyonları mevcuttur. Eksik / Kayıp verileri istersek farklı fonksiyonları kullanarak silebilir ya da istediğimiz değer ile doldurabiliriz.

* [`dropna()` Metodu]({filename}dropna.md)
  
  *...... `axis` Parametresi*
  
  *...... `inplace` Parametresi*
  
  *...... `thresh` Parametresi*

* [`fillna()` Metodu]({filename}fillna.md)
  
  *...... `value` Parametresi*
  
  *...... `method` Parametresi*
  
  *......... `backfill`*
  
  *......... `bfill`*
  
  *......... `pad`*
  
  *......... `ffill`*
  
  *......... `None`*

* [`isna()` Metodu]({filename}isna.md)

* [`isnull()` Metodu]({filename}isnull.md)

* [`notna()` Metodu]({filename}notna.md)

## VERİ DÜZENLEME YÖNTEMLERİ

Bu başlık altında, Veri çerçevemizi düzenlemek ve değiştirmek için kullanabileceğimiz fonksiyonlar anlatılmaktadır.

* [`add()` Metodu]({filename}add.md)

* [`add_prefix()` Metodu]({filename}add_prefix.md)

* [`add_suffix()` Metodu]({filename}add_suffix.md)

* [`apply()` Metodu]({filename}apply.md)
  
  *...... Kullanıcı Tanımlı Fonksiyon ile Kullanım*
  
  *...... `lambda()` Fonksiyonu ile Kullanım*

* [`assign()` Metodu]({filename}assign.md)

* [`astype()` Metodu]({filename}astype.md)

* [`convert_dtypes()` Metodu]({filename}convert_dtypes.md)

* [`drop()` Metodu]({filename}drop.md)
  
  *...... `axis` Parametresi*
  
  *...... `inplace` Parametresi*

* [`drop_duplicates()` Metodu]({filename}drop_duplicates.md)
  
  *...... `subset` Parametresi*
  
  *...... `keep` Parametresi*

* [`insert()` Metodu]({filename}insert.md)

* [`pop()` Metodu]({filename}pop.md)

* [`replace()` Metodu]({filename}replace.md)

* [`resample()` Metodu]({filename}resample.md)

* [`set_index()` Metodu]({filename}set_index.md)

* [String Metotları]({filename}string_metotlari.md)
  
  *......... `upper()` Metodu*
  
  *......... `lower()` Metodu*
  
  *......... `capitalize()` Metodu*
  
  *......... `contains()` Metodu*
  
  *......... `get()` Metodu*
  
  *......... `slice()` Metodu*

* [`to_frame()` Metodu]({filename}to_frame.md)

* [`to_numpy()` Metodu]({filename}to_numpy.md)

* [`transpose()` Metodu]({filename}transpose.md)

### Metot ve Operatör Kullanımı ile Yeni Sütun Eklemek

* [`sum()` Metodu (Toplam)]({filename}sum.md)

* [`mean()` Metodu (Ortalama)]({filename}mean.md)

* [`+ `(Toplama) Operatörü]({filename}toplama_op.md)

* [`-` (Çıkarma) Operatörü]({filename}cikarma_op.md)

* [`*` (Çarpma) Operatörü]({filename}carpma_op.md)

* [`/` (Bölme) Operatörü]({filename}bolme_op.md)

## VERİ ÇERÇEVELERİNİ BİRLEŞTİR

Pandas Kütüphanesinde Veri çerçevelerini birleştirmek için kullanılabilecek birden fazla Fonksiyon/Metot vardır. Bu başlık altında, bu Fonksiyonların kullanımı anlatılmıştır

* [`concat()` Metodu]({filename}concat.md)

* [`join()` Metodu]({filename}join.md)
  
  *...... `how` Parametresi*
  
  *......... `left`*
  
  *......... `right`*
  
  *......... `outer`*
  
  *......... `inner`*

* [`merge()` Metodu]({filename}merge.md)
  
  *...... `on` Parametresi*
  
  *...... `how` Parametresi*
  
  *......... `inner`*
  
  *......... `outer`*
  
  *......... `left`*
  
  *......... `right`*
  
  *......... `cross`*
  
  *...... `left_on` Parametresi*
  
  *...... `right_on` Parametresi*
  
  *...... `suffixes` Parametresi*

## VERİ SIRALAMA YÖNTEMLERİ

Oluşturulan Veri Çerçevelerinin, isteğimiz doğrultusunda sıralanması için kullanabileceğimiz yöntemlere, bu başlık altında değineceğiz.

Pandas üç tür sıralamayı destekler ; İndeks (dizin) etiketlerine göre sıralama, Sütun değerlerine göre sıralama ve Her ikisinin birleşimine göre sıralama.)

* [`reindex()` Metodu]({filename}reindex.md)
  
  *...... `columns` Parametresi*
  
  *...... `index` Parametresi*
  
  *...... `axis` Parametresi*
  
  *......... `index` Seçeneği*
  
  *......... `columns` Seçeneği*

* [`sort_index()` Metodu]({filename}sort_index.md)
  
  *...... `ascending` Parametresi*
  
  *...... `axis` Parametresi*

* [`sort_values()` Metodu]({filename}sort_values.md)
  
  *...... `by` Parametresi*
  
  *...... `ascending` Parametresi*
  
  *...... `na_position` Parametresi*

## VERİ FİLTRELEME YÖNTEMLERİ

Pandas kütüphanesi ile en sık yapılan işlemlerden biri de Filtreleme işlemidir. Binlerce, onbinlerce hatta milyonlarca kayıt arasından istediğimize ulaşmak için filreleme komutlarını kullanacağız. Bu bölümdeki anlatılanları da dikkatle okuyup öğrenmenizi tavsiye ederim.

Sütun içerisindeki verilere göre filtreleme uygulamak istersek; 
`VeriCervecesiAdı["SütunAdı"] operatör (==, <, ...vb) "Filtre_Kriteri"` yöntemi kullanılabilir.

Pythonda kullanıdığımız **Karşılaştırma operatörlerini (`<` , `>` , `<=`, `>=`, `==`, `!=`, )** ve **Mantıksal Operatörleri ( (and, ve) `&` ve (or, Ya da) `|`** Pandas içerisinde de kullanabiliriz.

* [`between()` Metodu]({filename}between.md)

* [`lambda()` Metodu]({filename}lambda.md)

* [Sütun Filtrelemek]({filename}sutun_filtrele.md)

### Karşılaştırma Operatorleri

* [büyüktür (`>`) Operatörü]({filename}buyuktur_op.md)

* [büyükeşit (`>=`) Operatörü]({filename}buyukesit_op.md)

* [esittir (`==`) Operatörü]({filename}esittir_op.md)

* [esit değil (`!=`) Operatörü]({filename}esitdegil_op.md)

* [küçüktür (`<`) Operatörü]({filename}kucuktur_op.md)

* [küçükeşit (`<=`) Operatörü]({filename}kucukesit_op.md)

* [Metot ve Operatörü Birlikte Kullanarak Filtrelemek]({filename}metot_ve_op.md)

### Mantıksal Operatörler

* [ve (`&`) Operatörü]({filename}ve_op.md)

* [ya da (`|`) Operatörü]({filename}yada_op.md)

## GRUPLAMA YÖNTEMLERİ

* [`groupby()` Metodu]({filename}groupby.md)
  
  *...... `mean()` Metodu*
  
  *...... `max()` Metodu*
  
  *...... `min()` Metodu*
  
  *...... `sort_values()` Metodu*
  
  *...... `count()` Metodu*
  
  *...... `value_counts()` Metodu*

* [`pandas.Grouper` Nesnesi]({filename}grouper.md)
  
  *...... `key` Parametresi*
  
  *...... `level` Parametresi*
  
  *...... `freq` Parametresi*
  
  *...... `closed` Parametresi*
  
  *......... `left`*
  
  *......... `right`*
  
  *...... `label` Parametresi*
  
  *......... `left`*
  
  *......... `right`*
  
  *...... `origin` Parametresi*
  
  *......... `epoch`*
  
  *......... `start`*
  
  *......... `start_day`*
  
  *......... `end`*
  
  *......... `end_day`*
  
  *...... `offset` Parametresi*

## DİĞER BAZI FONKSİYONLAR

* [`melt()` Metodu]({filename}melt.md)
  
  *...... `id_vars` Parametresi*
  
  *...... `var_name` Parametresi*
  
  *...... `value_name` Parametresi*

* [`pivot_table()` Metodu]({filename}pivot_table.md)
  
  *...... `values` Parametresi*
  
  *...... `index` Parametresi*
  
  *...... `columns` Parametresi*
  
  *...... `aggfunc` Parametresi*
  
  *...... `fill_value` Parametresi*
  
  *...... `margins` Parametresi*
  
  *...... `margins_name` Parametresi*
  
  *...... `sort` Parametresi*

# Pandas Veri Çerçevesi Özet Bilgileri (CheatSheet)

Pandas Veri Çerçevesi (Data Frame) komutlarını (fonksiyon, metot, parametre) bir yerde toplayarak ihtiyaç halinde, farklı konulara ait komutlara daha hızlı ulaşabileceğimiz bir **Başvuru Kılavuzu / Özet Bilgi Tablosu (CheatSheet)** oluşturmaya çalışıyorum. Başvuru kılavuzunu / Özet Bilgi Tablosunu (CheatSheet) oluştururken, komutları, **Pandas Veri Çerçevesi (Data Frame) Konu Başlıkları**na göre kategorize etmeyi planlıyorum.

Sayfaya Yeni Konu başlıkları ekledikçe, Özet Bilgi Tablosunu da güncellemeye gayret edeceğim.  
Şuana kadar oluşturduğum **Başvuru Kılavuzu / Özet Bilgi Tablosu (CheatSheet)** na ağaşıdaki bağlantıdan erişebilirsiniz.

* [Pandas Özet Bilgi Tablosu (CheatSheet) Sayfası]({filename}ozet_bilgi_tablosu.md)
