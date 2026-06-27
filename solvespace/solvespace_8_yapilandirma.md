Title: Solvespace Bölüm 8: Yapılandırma
Date: 2022-03-10 18:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Yapılandırma, Kullanıcı, Malzeme, Renk, Işık, Yön, Nüans, Akor, Chord, Tolerans, Parça, Sayı, Perspektif, Faktör, Çarpan, Katsayı, Izgara, Yakalama, Mesafe, Aralık, Dışa Aktar, Export, Aktar, Ölçek, Kesici, Yarıçap, Öteleme, Miktar, 2B, 2D, Üçgen, Gölge, Eğri, Parça, Doğru, Tuval, Boyut, Beyaz, Çizgi, Düzelt, Arka, Yüzey, Kırmızı, Göster, Kapalı, Kontur, Çizim, Denetle, Kontrol Et, G Kodu, Parametre
Author: Mustafa Halil


## Bölüm 8: Yapılandırma

## Kullanıcı / Malzeme Renkleri

**Özellik Penceresi** ekranında, 
belirli gruplar için (örneğin uzatarak katıla, tam ve kısmi döndürerek 
katıla) sekiz renkten oluşan bir palet görüntülenir (`User Color (r, g, b)`). Bu palet, kullanıcının o grup tarafından oluşturulan herhangi bir yüzeyin rengini seçmesine izin verir.

Bu sekiz renk, bileşenleri ile burada 
belirtilmiştir. Bileşenler 0' ile 1.0 aralığında sayı değerleri ile 
temsil edilir. "0, 0, 0" rengi siyah ve "1, 1, 1" beyazdır. Bileşenler 
"kırmızı, yeşil, mavi” sırasına göre belirtilmiştir.

![Kullanıcı Renkleri](images/solvespace/50%20Kullanici%20renkleri.png)

Palet renklerinde yapılan bir değişiklik, palette
 varolan bir yüzeyin rengi artık görünmese bile, çizimdeki varolan 
yüzeylerin rengini değiştirmez.

## Işık Yönleri

Derinlik izlenimi oluşturmak için 3 boyutlu 
kısım, simüle edilmiş aydınlatma ile görüntülenir. Yönlü ve ortam ışığı 
olmak üzere iki tür ışık vardır. Bu ışıkların yönleri ve yoğunlukları (`Light Directions`) kullanıcı tercihine göre değiştirilebilir.

Işık yönlerinin bir konumu yoktur; sanki çok uzaklardan geliyormuş gibi düşünün, ışığın sadece yönü var. Bu yön "**sağ, üst, ön**" olmak üzere 3 bileşende belirtilmiştir. Ekranın **sağ** tarafından gelen ışık "**1, 0, 0**" ile temsil edilir. Ekranın **solundan** ışık gelmesi isteniyorsa "**-1, 0, 0**" şeklinde ayarlama yapılmalıdır. Ekranın **önünden** gelen ışığı "**0, 0, 1**" ile ifade edebiliriz. Ortam ışığının yönü yoktur ve dolgu ışığı her yönden eşit yoğunlukta etki eder bir görevi görür.

Yoğunluk 0 ile 1 arasında olmalıdır. Yoğunluğu 0 
(sıfır) olan bir ışığın etkisi yoktur ve 1 değeri tam parlak ışıktır. 
Ortam ışığının yoğunluğunu 1'e ayarlanırsa "düz gölgeleme" efekti elde 
edilir.

İki yönlü ışık kullanılır. Yalnızca biri 
isteniyorsa, yoğunluğu sıfıra ayarlanarak ikincisi devre dışı 
bırakılabilir. Parça döndürüldüğünde veya çevrildiğinde ışıklar hareket 
etmez.

![Işık Yönleri ve yoğunluğu](images/solvespace/51%20Isik%20yonleri.png)

## Nüans/Akor (Chord) Toleransı ve En Fazla Parça Sayısı

SolveSpace her zaman kavisli kenarları veya 
yüzeyleri tam olarak temsil etmez. Eğriler bazen parçalı doğrusal 
bölümlere, yüzeyler ise bazen üçgenlere bölünür.

Bu, bazı hataları ortaya çıkarır. Nüans/Akor 
(Chord) toleransı, ne kadar hatanın ortaya çıktığını belirler; bu 
tolerans, tam eğri ile ona yaklaşık doğru parçaları arasındaki en fazla 
mesafeyi ayarlar. Nüans/Akor toleransı azaltılırsa, daha iyi bir 
yaklaşım elde etmek için daha fazla çizgi parçası oluşturulacaktır.

Yapılandırma ekranında iki Nüans/Akor tolerans 
değeri vardır. Birincisi, çizimin toplam boyutunun yüzdesi olarak 
belirtilir ve uzunluk birimlerindeki değeri de hesaplanır ve gösterilir.
 Bu, tek bir daireden oluşan bir çizimin çok düzgün eğrilere sahip 
olacağı anlamına gelirken, küçük delikli büyük bir nesnenin daha az 
segmenti olabilir, çünkü delik genel çizimden çok daha küçüktür ve boyut
 olarak Nüans/Akor toleransına daha yakındır.

İkinci değer, mm cinsinden mutlak bir değer olan "`export chord tolerance` (*dışa aktarma Nüans/Akor toleransı*)dır". 3B yazdırma için bir **üçgensel ağı (mesh)** veya işleme için **g kodu**nu dışa aktarırken, bu değer, ortaya çıkan parçanın ideal kavisli yüzeylerden ne kadar sapabileceğini belirleyecektir.

SovleSpace, NURBS yüzeyini veya farklı gruplardan
 üçgensel ağları birleştirirken bazı hesaplamalarda Akor (Kiriş) 
toleransını kullanır. Bu, bir mantıksal (boolean) işlemi başarısız 
olduğunda, bazı durumlarda Nüans/Akor toleransında ayarlamalar yapmak 
sorunu "çözebilir" anlamına gelir.

Ağın (Mesh) inceliği, belirtilen en fazla parçalı
 doğrusal parça sayısı ile de sınırlıdır. Nüans/Akor toleransı ne kadar 
iyi olursa olsun, tek bir eğri asla bu sayıda çizgi parçasından 
fazlasına bölünmeyecektir.

![Nüans / Akor (Chord) Toleransı](images/solvespace/52%20Nuans-Chord%20Toleransi.png)

## Perspektif Faktörü

3 boyutlu bir parçayı ekranda görüntülemek için, 
çizimin 2 boyutlu olarak yansıtılması gerekir. Ortak seçim, paralel bir 
izdüşümdür. Paralel izdüşüm yaklaşımında, gerçek hayatta paralel olan 
herhangi iki çizgi, çizimde de paraleldir. Paralel izdüşüm, aksonometrik
 izdüşüm olarak da bilinir. İzometrik ve ortografik görünümler paralel 
izdüşümlerin örnekleridir.

Görüntüyü 2B'ye dönüştürmenin başka bir yolu da perspektif projeksiyonudur (`Perspective Factor`).
 Perspektif projeksiyonda, "kameraya" yakın olan nesneler, uzaktaki 
nesnelerden daha büyük görünür. Bu, gerçek hayatta paralel olan bazı 
doğruların çizimde paralel olmayacağı anlamına gelir; temel mantık 
olarak paralel çizgiler ya da uzantıları kameradan uzaklaştıkça ileride,
 kaybolan bir noktada birleşecekler.

Aşağıdaki resim bir perspektif projeksiyondur. 
Tüm kare kesikler aynı boyuttadır, ancak öndekiler (izleyiciye daha 
yakın olanlar) daha büyük, arkadakiler ise daha küçük gösterilmiştir.

![Perspektif Görünüm](images/solvespace/53%20perspektif%20gorunum.png)

Bir sonraki görüntü paralel bir izdüşümdür (Orto 
grafik yani dik görünüm). Tüm kare kesikler çizimde aynı boyuttadır. 
(Üst kısımdaki kesikler biraz daha büyük görünebilir, ancak bu bir optik
 illüzyondur, çünkü göz, görüntüleri perspektifle görmeye alışmıştır.)

![Paralel / Orto grafik / Dik Görünüm](images/solvespace/54%20ortho%20gorunum.png)

Perspektif projeksiyon genellikle daha gerçekçi 
görünür ve daha iyi bir derinlik izlenimi verir. Dezavantajı ise, 
perspektifin görüntüyü bozması ve kafa karışıklığına neden 
olabilmesidir.

Varsayılan olarak, SolveSpace paralel (orthographic) bir projeksiyon görüntüler. Bir perspektif projeksiyonu görüntülemek için `Görünüm → Perspektif Projeksiyonu Kullan`'ı seçin ve perspektif faktörünün sıfır olmadığından emin olun. Varsayılan olarak, **perspektif katsayısı** *(çarpanı)* 0,3'tür. "Kameradan" modele olan mesafe, perspektif katsayısına bölünen bin piksele eşittir.

![Perspektif Katsayısı (Çarpanı, Faktörü)](images/solvespace/55%20Perspektif%20katsayisi.png)

## Izgara Yakalama Mesafesi/Aralığı

Bu, ızgara yakalama mesafesinin ( **Snap Grid Spacing** ) inç veya milimetre cinsinden derecesini belirtir. Varsayılan olarak ızgara görüntülenmez; `Görünüm → Yakalama Izgarasını Göster` seçilerek gösterilebilir. Noktalar hiçbir zaman ızgaraya otomatik 
olarak tutturulmaz. Bir noktayı, ızgaraya tutturmak için o noktayı seçin
 ve ardından `Düzen → Seçimi Izgaraya Tuttur`'u seçin (Kısayol tuşu: `. [nokta]`). Yorumlar da (`Kısıtla→ Yorum`) (Kısayol tuşu: `; [noktalı virgül]`) ızgaraya aynı şekilde tutturulabilir.

## Dışa Aktarım Ölçek Katsayısı

Dahili olarak, SolveSpace uzunlukları milimetre 
cinsinden temsil eder. Geometriyi dışa aktarmadan önce, bu uzunluklar, 
dışa aktarma ölçek katsayısına ( **Export Scale Factor** ) bölünür. Bu ölçek katsayısı, dışa aktarılan dosyanın birimlerini belirler.

Ölçek katsayısı 1'e eşit olarak ayarlanırsa, dışa
 aktarılan dosyalar milimetre birimindedir. Ölçek katsayısı 25.4 olarak 
ayarlanırsa, 1 inç = 25,4 mm olduğundan dolayı, dışa aktarılan dosyalar 
inç biriminde olacaktır.

SolveSpace Sağ-El koordinat sisteminde çalışır. 
Ölçek faktörü negatifse, dışa aktarılan dosya Sol-El bir koordinat 
sisteminde görünür (böylece sağ yönlü bir vida dişi sol yönlü olur ve 
metin yansıtılmış/aynalanmış olarak görünür).

![Dışa Aktarım Ölçek Katsayısı (Faktörü)](images/solvespace/56%20DisaAktarim-OlcekKatsayisi.png)

## Kesici Yarıçapı Öteleme Miktarı

Bir 2b (2d) görünümü veya kesiti dışa aktarırken, bu seçenek kesici yarıçap telafi miktarı (tolerans) ( **Cutter Radius Offset** ) uygulamak için kullanılabilir. Dışa aktarılan geometrideki tüm 
eğriler, belirtilen yarıçapla ötelenir/kaydırılır. Bu, bazı durumlarda 
özel CAM yazılımı olmadan çalışmayı mümkün kılabilir.

Kesici yarıçapı, mevcut moda göre inç veya 
milimetre olarak belirtilir. Kesici yarıçap telafisini devre dışı 
bırakmak için bu öteleme / kaydırma değerini (ofseti) sıfıra ayarlayın.

Kesici yarıçap telafi değeri, yalnız kırıklı doğrusal parçalarda uygulanabilir. Bu, "`export curves as piecewise linear` (*eğrileri, parçalı doğrular olarak dışa aktar*)" "**hayır**"
 olarak ayarlansa bile, çıktı dosyasında eğrilerin (daireler, Beziers, 
vb.) çizgi parçaları olarak yaklaşılacağı anlamına gelir.

![Kesici Yarıçapı Öteleme Miktarı](images/solvespace/57%20Kesici%20Y.Cap%20Otele.png)

## 2b (2d) Üçgenleri Gölgeli olarak Dışa Aktar

Parçanın görünümü dışa aktarılırken, kullanıcı 
yalnızca parçanın kenarlarını dışa aktarabilir (tel kafes veya gizli 
çizgileri kaldırılmış çizim üretmek için) veya kullanıcı parçanın 
yüzlerinin rengini ve aydınlatmasını göstermek için düz gölgeli 
yüzeyleri dışa aktarabilir.

Tüm dışa aktarma dosya biçimleri, gölgeli 
üçgenleri desteklemez; Gölgeli görünüm desteğini şu anda SVG, EPS ve PDF
 dosya biçimleri destekliyor, ancak DXF ve HPGL desteklemiyor.

![2 Boyutlu Üçgenleri Gölgeli Olarak Dışa Aktar](images/solvespace/58%20Golgeli%20Ucgenler.png)

## Eğrileri Parçalı Doğrular Olarak Dışa Aktar

Düzgün bir eğri (daire veya Bezier eğrisi gibi) 
iki yöntem ile dışa aktarılabilir: ya tam olarak ya da ona yaklaşık bir 
dizi doğru parçası olarak. Bu `Export Curves as Piecewise Linear` seçeneği işaretlenmezse, mümkün olduğu sürece, geometri, mutlak eğriler
 şeklinde dışa aktarılacaktır. Seçenek işaretlenirse, eğriler her zaman 
parçalı doğrusal segmentler (doğru parçaları) olarak dışa aktarılır.

Bu seçenek yararlıdır çünkü bazı CAM veya diğer 
yazılımlar mutlak/kesin eğrileri içe aktaramaz, ancak hemen hemen tüm 
yazılımlar parçalı doğrusal segmentleri içe aktarabilir.

![Eğrileri Parçalı Doğrular Olarak Dışa Aktar](images/solvespace/59%20Parcali%20Dogrular.png)

## Tuval Boyutunu Dışa Aktar

Bu ayar ( `Export Canvas Size` ), dışa
 aktarılan herhangi bir 2b (2d) geometrisi için tuval boyutunu (çizim 
alanı, sınırı, çerçeveyi) belirtir. Örneğin, bir PDF dosyasındaki tuval 
boyutu kağıt boyutudur ve bir PostScript dosyasındaki tuval boyutu EPS 
sınır kutusudur (BoundingBox). Bu seçenek, iki yoldan biriyle 
belirtilebilir: ya sabit bir boyut olarak ya da dışa aktarılan 
geometrinin etrafındaki bir dizi kenar boşluğu olarak.

![Tuval Boyutu Ayarı](images/solvespace/60%20Tuval%20Boyutu.png)

## Dışa Aktarılan Beyaz Çizgileri Düzelt

Varsayılan olarak, SolveSpace siyah bir arka plan
 üzerine beyaz çizgiler çizer. Ancak çoğu dışa aktarma dosyası biçimi, 
beyaz renkli bir arka plan varsayar; Bu, dışa aktarılan beyaz çizgilerin
 okunaksız olacağı anlamına gelir. Varsayılan olarak, SolveSpace, bu tür
 bir dosya biçimini dışa aktarırken, herhangi bir beyaz (yaklaşık %75 
griden daha açık) renkleri siyah olarak yeniden oluşturacaktır. Bu 
seçenek (`Fix White Exported Lines`) ile bu davranış devre dışı bırakılabilir.

![Dışa Aktarılan Beyaz Çizgileri Düzelt](images/solvespace/61%20BeyazCizgileri%20Duzelt.png)

## Üçgenlerin Arka Yüzeylerini Kırmızıyla Göster

SolveSpace her zaman katı kabuklarla çalışır. Bu,
 normal çalışmada, yalnızca bir yüzeyin dışının görünür olması gerektiği
 anlamına gelir.

Kendi kendisi ile kesişen bir kabuk çizilirse, iç
 yüzeyler açığa çıkabilir. Grafik kartının üçgenleri nasıl oluşturduğuna
 bağlı olarak, bir iç yüzeyden birkaç tane başıboş piksel "görünebilir".
 Bu ayar (`Draw Triangle Back Faces in Red`), bu yüzeylerin gözardı ediplip edilmeyeceği veya kırmızıyla vurgulanıp vurgulanmayacağını belirler.

![Üçgenlerin Arka Yüzeylerini Kırmızıyla Göster](images/solvespace/62%20Kirmizi%20Arka%20Yuzeyler.png)

![Üçgenlerin Arka Yüzeylerini Kırmızıyla Göster](images/solvespace/63%20Kirmizi%20Arka%20Yuzeyler.png)

## Kapalı Konturlar için Çizimi Denetle / Kontrol Et

Çoğu katılama işlemi (uzatarak katılama 
(ekstrüzyon), tam ve kısmi döndürerek katılama gibi) yalnız kendi 
kendini kesmeyen kapalı kontura sahip, düzlemsel (2 boyutlu) çizimlerde
 çalışır. SolveSpace varsayılan olarak, çizimi denetler ve bu 
kurallardan herhangi birini ihlal eden bir şey görürse, sorunu, çizim 
üzerinde belirterek kullanıcıyı uyarır. Bu ayar (`Check for Closed Contours`)
 aktif ise ve bir kontur açıksa, açık (boşta duran) uç noktalarından 
birinin yanında bir mesaj görüntülenir. Bir kontur kendi kendini 
kesiyorsa, kesişme noktasında bir mesaj görüntülenir.

![Kapalı Konturlar için Eskizi (Çizimi) Kontrol Et / Denetle](images/solvespace/19%20Kapali%20olmayan%20kontur.png)

## G Kodu Parametreleri

SolveSpace bir CAM programı değildir, ancak 2d parçalar için basit **G kodu**nu
 dışa aktarabilir. Doğru kesici yarıçap dengelemesi uygulayarak (veya 
çizimi kesici yarıçapını göz önünde bulundurup çizerek), ek CAM yazılımı
 olmadan 2d parçaların profilini çıkarmak mümkündür. Parçanın XY 
düzleminde olduğu varsayılır. Z ekseni boyunca kesme derinliği burada 
belirtildiği gibidir; hangi işaretin aşağıya karşılık geldiğine bağlı 
olarak pozitif veya negatif bir değer yazın/belirtin. İş parçasının üst 
kısmının Z = 0'da olduğu varsayılır ve kesici, dönerken iş parçasının 5 
mm yukarısındaki bir boşluk düzleminde hareket eder.

Tüm ölçü birimleri, geçerli moda göre inç veya 
milimetre (veya ilerlemeler/beslemeler için inç veya dakika başına 
milimetre) cinsindendir.

G Kodu Parametrelerini (`G Code Parameters`) bu bölümden ayarlayabilirsiniz.

![G Kodu Parametreleri](images/solvespace/65%20G%20Kod.png)
