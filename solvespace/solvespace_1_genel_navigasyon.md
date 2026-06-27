Title: Solvespace Bölüm 1: Genel Navigasyon
Date: 2021-11-21 00:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Genel, Navigasyon, Grafik Penceresi, Model Görünümü, Ölçü, Boyut, Giriş, Birim, Özellik Penceresi, Özellik, Pencere, Tarayıcı, Öğe, Göster,  Gizle
Author: Mustafa Halil


## Bölüm 1: Genel Navigasyon

Bu, SolveSpace için bir başvuru 
kılavuzudur. Programa giriş niteliğinde (Çizim ve Modelleme öğretme 
amaçlı) değildir; Bunun için [öğreticilere](https://solvespace.com/tutorial.pl) bakın.

### Genel Navigasyon/Gezinim

Kullanıcı arayüzü iki pencereden oluşur: 
çoğunlukla grafik içeren büyük bir pencere (Grafik Penceresi) ve 
çoğunlukla metin içeren daha küçük bir pencere (özellikler penceresi). 
Grafik penceresi geometriyi çizmek ve 3 boyutlu modeli görüntülemek için
 kullanılır. özellikler penceresi model hakkında bilgi sağlar ve ayrıca 
ayarları ve sayısal parametreleri değiştirmek için kullanılabilir.

### Grafik Penceresi ve Model Görünümü

Görünümü kaydırmak için fareyi `sağ tuşuna (butonuna)` basarak sürükleyin.  
Görünümü döndürmek (çevirmek) için fareyi `orta tuşuna (tekerleğine)` basarak sürükleyin. Bu, parçayı ters çevirir, böylece daha önce 
gizlenmiş olan (sahneye bakıldığında arkada kalan) yüzeyler görünür hale
 gelir.

Görünümü monitör düzlemi içinde döndürmek için `Ctrl+Farenin orta tuşu` basılıyken sürükleyin.

`Shift+Farenin orta tuşuna` basıp sürükleyerek kaydırmak veya `Shift+Farenin sağ tuşuna` basıp sürükleyerek döndürmek de mümkündür. Eğer altı serbestlik 
dereceli bir 3Dconnexion kontrolör bağlıysa (örneğin, bir 
SpaceNavigator) bu, modelin görünümünü dönüştürmek için de 
kullanılabilir.

Görünümü Yakınlaştırmak veya Uzaklaştırmak için `Farenin tekerleğini` çevirin. Görünüm menüsünü veya ilgili klavye kısayollarını ( **`+`** ve **`-`** ) kullanarak da yakınlaştırma yapmak mümkündür. Düzlemler de dahil 
olmak üzere bazı özellikler her zaman ekranda aynı boyutta çizilir ve bu
 nedenle yakınlaştırmadan etkilenmez.

Komutların çoğu üç farklı şekilde 
kullanılabilir: menüden, klavye kısayolundan veya araç çubuğundan. Araç 
çubuğu, grafik penceresinin sol üst kısmında görüntülenir. Bir simgenin 
ne anlama geldiğini öğrenmek için fareyi üzerine getirin (Komutun ve 
kısayol tuşu bilgileri görüntülenecektir). Araç çubuğunu göstermek veya 
gizlemek için **Görünüm → Araç çubuğunu Göster'i (View → Show Toolbar)** seçin.

Parçanın tümünü ekrana sığdıracak şekilde görüntüyü yakınlaştırmak için `Görünüm → Sığdıracak şekilde Yakınlaş'ı (View → Zoom To Fit.)` seçin (Kısayol tuşu **`F`** ‘dir). Bu komut, parçanın tam olarak ekrana sığması için yakınlaştırma 
seviyesini ayarlar ve ardından parçayı ekrana ortalamak için taşır. 
Taşıma işleminden parçanın dönüşü etkilenmez (Bakış açısı 
değiştirilmez).

Bir çalışma düzlemi etkinse, görünümü çalışma düzlemine hizalamak için **Görünüm → Görünümü çalışma Düzlemine Hizala'yı (View → Align View to Workplane)** seçin (veya **`W`** tuşuna basın). Bunu yaptıktan sonra ekranın düzlemi çalışma düzlemi 
ile çakışıyor ve çalışma düzleminin merkezi ekranın ortasında oluyor. 
Yakınlaştırma düzeyi bu komuttan etkilenmez.

Ortogonal (dikey) bir görünümde, koordinat 
(x, y veya z) eksenlerinden biri yatay, diğeri ise dikeydir. Görünümü en
 yakın Ortogonal (dikey) görünüme yönlendirmek için **Görünüm → En Yakın Orto Görünüm (View → Nearest Ortho View)** menü yolunu seçin (Kısayol tuşu **`F2`** ‘dir). İzometrik görünümde, üç koordinat ekseninin tümü aynı 
uzunlukta yansıtılır ve koordinat eksenlerinden biri dikeydir. Görünümü 
en yakın izometrik görünüme yönlendirmek için Görünüm → En Yakın 
İzometrik Görünümü (View → Nearest Iso View) menü yolunu seçin (Kısayol
 tuşu **`F3`** ‘tür).

Belirli bir noktanın, ekranın tam merkezinde olacak şekilde görüntü kaydırılmak istenirse, o noktayı seçin ve ardından `Görünüm → Noktayı Merkezde Görüntüle` menü yolunu seçin (Kısayol tuşu **`F4`** ‘tür).  
X, Y ve Z koordinat eksenleri her zaman grafik 
penceresinin sol alt kısmında kırmızı, yeşil ve mavi olarak 
görüntülenir. Bu eksenler canlıdır: Yani diğer normallerle aynı şekilde 
fare ile vurgulanabilir ve seçilebilirler. (Bu, koordinat eksenlerinin 
ekranda her zaman kolayca erişilebilir olduğu anlamına gelir; örneğin X 
eksenine paralel bir çizgiyi sınırlandırırken bundan faydalanabiliriz.)

### Ölçü (Boyut) Girişi ve Birimler

ölçüler (Boyutlar), milimetre veya inç olarak
 görüntülenebilir. Milimetre ölçülerin ondalık kısmı (noktadan sonrası) 
her zaman iki basamakla (45.23) ve inç ölçüleri her zaman üç basamakla 
(1.781) görüntülenir.

Mevcut görüntüleme (ölçü) birimlerini değiştirmek için `Görünüm → ölçü Birimleri → İnç / Milimetre cinsinden (Choose View → Dimensions Units → Inches/Millimeters)` menü yolunu kullanın. Bu, çizili olan modeli değiştirmez; Kullanıcı 
görüntülenen ölçü birimini inç’ten milimetreye değiştirirse, örneğin 1.0
 olarak girilen ölçü, 25.40 olarak görüntüleniyor.

Tüm ölçüler, geçerli görüntüleme birimlerine 
göre yazılır, belirtilir. Bir ölçü girilmesinin beklendiği çoğu yerde, 
tek bir sayı yerine aritmetiksel ifadeler ( örneğin; 4*20 + 7) girmek te
 mümkündür.

### Özellik Penceresi (Tarayıcısı)

özellik penceresi, bağımsız bir palet penceresi olarak görünür. Bu pencere, `Sekme (TAB)` tuşuna basılarak veya `Görünüm → özellik Tarayıcısını Göster (View → Show Property Window)` seçilerek gösterilebilir veya gizlenebilir. özellikler penceresi bir web tarayıcısı gibi çalışır.  
Altı çizili metinler birer bağlantıdır. Bir bağlantıyı etkinleştirmek için `fare ile (Sol tuş)` tıklayın. Bağlantılar, özellik penceresindeki diğer sayfalara gitmek için kullanılabilir. örneğin, "`home`" ekranı, çizimdeki grupların bir listesidir:

![özellik Penceresi (Tarayıcısı)](https://mhalil.github.io/images/solvespace/002%20%C3%96zellik_Penceresi.png)

Bir grubun sayfasına gitmek için o grubun 
adını tıklayın (ör. "g002-düzlemde çizim"). Bağlantılar ayrıca çizimdeki
 eylemleri tetikleyebilir. örneğin, yukarıdaki ekran görüntüsünde tüm 
gruplar gösterilmektedir. Bir grubu gizlemek için "`shown (gösterilen)`" sütunundaki kutuyu tıklayın.  
özellik penceresi bazen kolaylık sağlamak için, 
komutla alakalı muhtemel sayfaya otomatik olarak gider. örneğin, yeni 
bir grup oluşturulduğunda, özellik penceresi o yeni grubun sayfasını 
görüntüler. Sol üst köşedeki "`Home (ana sayfa)`" bağlantısını tıklayarak (veya `ESC` tuşuna basarak) ve oradan bağlantıları takip ederek farklı bir sayfaya gitmek her zaman mümkündür.  
çizim objeleri seçildiğinde (örneğin, kullanıcı 
fare ile bir öğe üzerine tıkladığında), bu öge ile ilgili bilgiler 
özellik penceresinde görüntülenir. Tek bir öğe seçilirse, o öğe hakkında
 bilgi görüntülenir. örneğin, bir çemberin/dairenin merkezi 
(koordinatları) ve yarıçapı, özellik penceresinde görüntülenir.

Birden çok öğe seçilirse, özellik penceresi bazen hepsiyle ilgili bilgileri görüntüleyebilir. Bu durum şunları içerir:

- İki nokta: noktalar arasındaki mesafe
- Bir nokta ve bir düzlem yüzeyi: noktadan düzleme olan mesafe
- İki nokta ve bir vektör: vektör boyunca yansıtılan noktalar arasındaki mesafe
- İki düzlem yüzeyi: düzlem yüzleri arasındaki açı

### Öğeleri Goster / Gizle

çizim daha karmaşık hale geldikçe, gereksiz 
bilgileri gizlemek faydalı olabilir. SolveSpace bunu yapmak için birkaç 
farklı yol sunar.  
özellik penceresinin üst kısmında bir dizi simge
 görünür. Bu simgeler, çizimdeki farklı öğeleri gizlemeyi ve göstermeyi 
mümkün kılar:

![özellik Penceresi Araç çubuğu Simgeleri](https://mhalil.github.io/images/solvespace//003%20Goster_Gizle.png)

**1- Pasif Grupların çalışma Düzlemleri (Workplanes from inactive groups)**

"`Yeni çalışma Düzleminde çizim Yap`"
 menü seçeneği ile bir çalışma grubu oluşturulduğunda, ilişkili bir 
çalışma düzlemi otomatik olarak oluşturulur. Bu düzlemleri görüntülemek /
 gizlemek için bu seçenek kullanılabilir. Normal şartlarda Oluşturulan 
çalışma düzlemleri, ya o grup görünür olduğunda (yani öğe gösterilirken)
 ya da yalnızca o grup hem görünür hem de aktif olduğunda görünür.

**2- Normaller (Normals)**

Varsayılan olarak normaller, normal yönünde 
(düzleme dik) mavi-gri oklar olarak çizilir/gösterilir. Bu normaller, 
(örneğin onları kısıtlamak için) fare ile seçilebilir. Bu simge onları 
gizlemek için kullanılabilir.

**3- Noktalar (Points)**

Varsayılan olarak noktalar yeşil kare olarak 
çizilir/gösterilir. Bu noktalar, fareyle seçilebilir (örneğin onları 
sınırlamak için). Bu simge noktaları gizlemek / göstermek için 
kullanılabilir. Noktalar gizlenmişse, fare üzerlerine geldiğinde 
görünmeye devam edecekler ve yine de seçilebilirler. (versiyon 3’te bu 
mümkün değildir.)

**4- Yapı öğeleri (Construction Entities)**

çizim esnasında oluşturulan Yapı öğelerinin (Yardımcı çizgilerin) görüntülenmesi veya gizlenmesini

**5- Kısıtlamalar (sınırlamalar) ve ölçüler (boyutlar) (Constraints and dimensions)**

Bir kısıtlama oluşturulduğunda (örneğin ölçü,
 diklik, teğet, açı,...vb), bu kısıtlamanın grafiksel bir temsili, 
ekranda mor renk ile görüntülenir. Bir gruptaki kısıtlama, yalnız o grup
 etkin olduğunda görünür. Grup etkin iken bu kısıtlamaları gizlenmek 
istenirse u simgeyi kullanılır.

**6- Yüzeylerin Fare ile Seçilebilirliği (Faces selectable with the mouse)**

3d modeldeki bazı yüzeyler seçilebilir. 
örneğin, kullanıcı parçanın bir düzlem yüzünü seçebilir ve bir noktayı o
 düzleme uzayacak şekilde sınırlayabilir. Yüzeyler görüntüleniyorsa, 
fare üzerlerine geldiğinde yüzeyler farklı renkle vurgulanmış olarak 
görünecektir. Kullanıcı, diğer herhangi bir öğede (nokta, çigi,...vb) 
olduğu gibi, yüzeyi fare tıklaması ile seçer.

**7- Katı modelin gölgeli görünümü (Shaded view of solid model)**

3D parça, derinlik hissi / izlenimi vermek 
için ışık efektleriyle birlikte opak bir katı olarak görüntülenir. Bu 
simge, o görünümü gizlemek için kullanılabilir.

**8- Katı modelin kenarları (kenar çizgileri) (Edges of solid model)**

Katı modelin iki farklı yüzeyinin buluştuğu 
her yerde çizgiler çizilir. Kenarlar (kenar çizgileri) gösteriliyor 
ancak gölgeleme gizliyse, bir tel kafes görüntüsü ortaya çıkıyor. 
Kenarlar gösterildiğinde ağların (mesh) görüntülenmesi belirgin şekilde 
daha yavaş olabilir. NURBS yüzeylerinin gösterimi, kenarlar 
gösterildiğinde fark edilir şekilde daha yavaş olmayacaktır. Kenarların 
rengi çizgi stillerinde ayarlanabilir.

**9- Katı Modelin Ana Hatları (Outline of solid model)**

Katı Modelin Ana Hattını (Dış Konturunu) ayrı bir çizgi tipi, rengi ve kalınlık ile görüntülemek için bu buton kullanılabilir.

**10- Katı modelin üçgen örgüsü (Triangle mesh of solid model)**

3 boyutlu parça modeli birçok üçgenden 
oluşuyor; örneğin, dikdörtgen bir yüzey, iki üçgenle temsil edilir. 
Modeldeki üçgenleri göstermek için bu simgeyi kullanın. Bu, dışa 
aktarmadan önce örgünün / ağın (mesh) ne kadar ince veya kaba olduğunu 
görmenin iyi bir yoludur.

**11- Noktalı çizgiler (Stipple occluded (hidden) lines)**

Parça (bakış açımıza göre) belirli bir 
açıdayken, parçadaki bazı çizgiler katı parçanın içine gömüldükleri (ya 
da parçanın arkasında kaldığı) için görünmez olacaktır. Bu çizgileri 
göstermek için (Parça şeffafmış gibi) bu simgeyi kullanın. Bu, parçanın 
hacmi içinde kalan bir taslak çizerken kullanışlıdır.

Yukarıdaki seçeneklere ilave olarak, tüm 
grupları gizlemek ve göstermek mümkündür. Bir grup gizliyse, o gruptaki 
tüm öğeler (çizgi parçaları, çemberler, yaylar, noktalar vb.) gizlenir. 
Katı model (3 boyutlu parça) bundan etkilenmez; yani gizli bir grup, bir
 silindir oluşturmak üzere ekstrüde edilmiş bir daire içeriyorsa, 
(çember, nokta,... vb öğeler gizlenmesine rağmen ) silindir görünür 
durumda kalacaktır.

Bir grubu gizlemek için, `ESC` tuşuna basarak veya özellik Penceresinin sol üstündeki bağlantıyı (`home`)
 seçerek Ana Ekrana gidin. çiziminizin içeriğine bağlı olarak (uzun ya 
da kısa) bir grup listesi görüntülenir. Bir grup görünür durumdaysa, "`shown (gösterilen)`"
 sütunundaki onay kutusu işaretlenir. Böylece onay kutusunu artık 
işaretlenmemiş hale gelirve grup gizlenir. Grupların görünür / gizle 
durumu parça dosyasına kaydedilir. Bir parça bir montaj dosyasına 
bağlanırsa, parça dosyasında görünen objeler montaj dosyasında da 
görünür olacak ve gizlenmiş olan objeler de gizlenecektir.
