Title: Solvespace Bölüm 2: Çizim Öğeleri (Objeleri)
Date: 2022-12-26 12:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Çizim, Öğe, Obje, Yapı, Geometri, Yardımcı, Referans, Nokta, Çalışma Düzlemi, Çizgi, Parça, Dikdörtgen, Daire, Çember, Yay, Teğet, Radyus, Kübik, Bezier, Eğri, TrueType, Yazı Tipi, Metin, Resim, Görüntü, Öğe, Böl, Kırp, Trim
Author: Mustafa Halil


## Bölüm 2: Çizim Öğeleri (Objeleri)

![Çizim Öğeleri](images/solvespace/007%20Cizim%20Ogeleri.png)

### Yapı Geometrisi (Yardımcı Geometri)

Normal çalışmada, kullanıcı bir taslakta çizgi ve 
eğriler çizer. Bu eğriler üretilecek geometriyi tanımlar; sonuçta parmak
 freze, lazer veya başka bir kesici alet, bu eğriler boyunca kesecektir.

Bazı durumlarda son kısımda (geometrinin sonuçlanma 
kısmında) görünmemesi gereken bir çizgi (yardımcı çizgi) çizmekte fayda 
var. Örneğin, kullanıcı simetrik bir parça için bir merkez çizgisi 
çizmek isteyebilir; ancak bu merkez çizgisi yalnızca bir kılavuzdur ve 
aslında CAM verileriyle dışa aktarılmamalıdır. Bu çizgilere (sadece 
çizgi olmak zorunda değil) Yapı çizgileri (yardımcı çizgier) denir.

Bir öğeyi yalnızca yapı öğesi olarak işaretlemek için `Çizim → Yapıyı Değiştir`'i seçin (Kısayol tuşu `G`).
 Bir yapı öğesi, ekranda yeşil renkle çizilmesi ve varsayılan olarak 
dışa aktarma için geometriye (ekstrüde edilecek, tornalanacak veya 
süpürülecek bölüme) katkıda bulunmaması dışında diğer herhangi bir obje 
gibi davranacaktır. Ayrıca '`G`' klavye kısayolunu kullanarak yeni bir öğe çizerken yapı geometrisini değiştirebilirsiniz.

### Referans noktası

Bu öeğe, tek bir nokta ile tanımlanır.

Referans noktası oluşturulduğunda bir çalışma düzlemi
 etkinse, o referans noktası her zaman çalışma düzleminde yer alacaktır.
 Hiçbir çalışma düzlemi aktif değilse, referans noktası 3d olarak 
serbest olacaktır. (Bu, örneğin bir çizgi parçasının uç noktaları dahil 
olmak üzere tüm noktalar için aynı davranıştır.)

Referans noktaları tipik olarak yapı geometrisi 
olarak kullanılır. Kullanıcı, çizgi bölümlerinin veya diğer öğelerin 
boyutlandırılmasını basitleştirmek için referans noktalarını 
yerleştirebilir.

### Çalışma Düzlemi

Bu varlık bir nokta ve bir normal ile belirtilir. Nokta orijinini, normal ise oryantasyonunu (yönülimi) tanımlar.  
Bir çalışma düzlemi, 2d'de (2 boyutta) bir taslak 
çizmeyi mümkün kılar. Bir çalışma düzlemi etkinse, çizilen tüm öğeler o 
çalışma düzleminde bulunmalıdır.

Açıkça çalışma düzlemleri oluşturmak neredeyse hiç 
gerekli değildir. Bunun yerine, Yeni Çalışma Düzlemi grubunda yeni bir 
taslak (çizim) oluşturun.

### Çizgi Parçası

Bu öğe, iki uç nokta (çizginin başlangıç ve bitiş 
noktaları) ile belirtilir. Bir çalışma düzlemi etkinse, iki uç nokta her
 zaman o çalışma düzleminde bulunur.

Çizgi Parçası (Bölümü / Segmenti) oluşturmak için `Çizim → Çizgi Parçası`'nı
 seçin ve ardından çizginin bir uç noktasına sol tıklayın. Ardından fare
 düğmesini bırakın; diğer uç nokta şimdi sürükleniyor.

Yeni oluşturulan çizgi parçasıyla bir bitiş noktası 
paylaşan başka bir çizgi parçası oluşturmak (çoklu çizgiden oluşan 
geometri üretmek) için tekrar sol tıklayın. Bu, kapalı çokgenler 
çizmenin hızlı bir yoludur.

Çizgi parçaları çizmeyi durdurmak / sonlandırmak için `Escape` tuşuna basın veya `farenin sağ tuşu`na
 tıklayın. Otomatik bir kısıtlama eklenirse, SolveSpace yeni çizgi 
parçaları çizmeyi de durduracaktır. (Örneğin, art arda sol tıklayarak ve
 ardından son kez sol tıklamadan önce imleci başlangıç noktasının 
üzerine getirerek kapalı bir çokgen çizin. Çoklu çizginin bitiş noktası,
 başlangıç noktasında uzanacak şekilde sınırlandırılacaktır ve bir 
kısıtlama eklendiğinden, SolveSpace çizimi durduracaktır.)

### Dikdörtgen

Bu öğe, kapalı bir eğri oluşturacak şekilde 
düzenlenmiş iki dikey ve iki yatay çizgi parçasından oluşur. 
Başlangıçta, dikdörtgen fare ile çapraz olarak zıt iki köşe ile 
belirtilir. Dikdörtgendeki doğru parçaları (ve noktalar), sıradan doğru 
parçalarıyla aynı şekilde sınırlandırılabilir.

Dört doğru parçası çizerek ve uygun kısıtlamaları 
ekleyerek aynı şekli elle çizmek te mümkün olacaktır. Dikdörtgen komutu,
 aynı şeyi çizmenin daha hızlı bir yoludur.

Çalışma düzlemi, "**yatay**" ve "**dikey**"
 ifadelerini tanımladığı için, dikdörtgen çizildiğinde çalışma düzlemi 
aktif olmalıdır. (Yani dikdörtgen komutu ile geometri çizilirken, 
mecburen yatay ve dikey sınırlama eklenmelidir, bir çalışma düzlemi 
aktif değilse yatay ve dikeyin neye göre, hangi yöne göre olduğu 
bilinemez, bu nedenle bir dikdörtgen çizildiğinde çalışma düzlemi aktif 
olmalıdır.)

Dikdörtgen oluşturmak için `Çizim → Dikdörtgen`'i seçin (Kısayol tuşu `R`)

### Daire / Çember

Bu öğe, merkez noktası, çapı ve normali ile belirtilir.

Çember oluşturmak için `Çizim → Çember`'i seçin (Kısayol tuşu `C`)
 ve ardından merkeze sol tıklayın. Ardından fare düğmesini bırakın; fare
 hareket ettirildiğinde çemberin çapı sürüklenir. Çapı yerleştirmek için
 tekrar sol tıklayın.

Bir çalışma düzlemi etkinse, o zaman merkez noktası o
 çalışma düzleminde olmalıdır ve dairenin normali çalışma düzleminin 
normaline paraleldir (bu, dairenin, çalışma düzleminin yüzeyinde olduğu 
anlamına gelir).

Hiçbir çalışma düzlemi aktif değilse, o zaman merkez 
noktası boşlukta serbest vaziyettedir ve dairenin yönünü belirlemek için
 normal (normali temsil eden oklar) sürüklenebilir (veya 
sınırlandırılabilir).

### Çember Yayı

Bu öğe, merkez noktası, iki uç noktası ve normali ile belirtilir.

Yayı oluşturmak için `Çizim → Çember Yayı`'nı
 seçin (Kısayol tuşu A) ve ardından uç noktalarından birine sol 
tıklayın. Ardından fare düğmesini bırakın; fare hareket ettirildiğine 
diğer uç nokta sürüklenir. Yay oluşturulurken merkez nokta da, tam bir 
yarım daire oluşturacak şekilde sürükleniyor.

Diğer uç noktayı yerleştirmek için tekrar sol 
tıklayın ve ardından merkezi istenen konuma sürükleyin. Yay, birinci 
noktadan ikinci noktaya saat yönünün tersine çizilir.

Çember Yayı, bir çalışma düzleminde çizilmelidir; boş alanda çizilemez.

### Noktada Teğet Yay / Radyus

Keskin bir köşeyi yuvarlamak için (örneğin, iki çizgi
 arasında), genellikle köşede her iki çizgiye de teğet olan bir yay 
(radyus) oluşturmak isteriz.

Bu, çizgi ve yayın birleştiği yerde pürüzsüz bir görünüm oluşturacaktır. Bu yayları `Çizim → Çember Yayı` ve `Sınırlandır → Paralel / Teğet` menü yollarındaki komutları kullanarak elle çizmek te mümkün olabilir, ancak bunları otomatik olarak oluşturmak daha kolaydır.

Komut uygulandığında çizgilerin ilk parçaları yapı 
çizgileri olacak ve yaya bağlanan iki yeni çizgi oluşturulacak. Yayın 
çapı (oluşan radyus çapı) daha sonra **Mesafe / Çap** veya **Eşit Uzunluk / Yarıçap** kısıtlamaları ile olağan şekilde sınırlandırılabilir.

Varsayılan olarak, teğet yayın (radyus) yarıçapı otomatik olarak seçilir. Bunu değiştirmek için, hiçbir şey seçilmeden `Çizim → Noktada Teğet Yay`'ı
 seçin. Özellik penceresinde yarıçapın belirtilebileceği bir ekran 
görünecektir. Bu ekranda, komut sonrası, orijinal çizgilerin ve 
eğrilerin korunup korunmayacağını, korunacaksa yapı çizgileriyle 
değiştirilip değiştirilmeyeceğini (üzerlerine kısıtlamalar koymak 
istiyorsanız bu yararlı olabilir) veya silinip silinmeyeceğini belirtmek
 de mümkündür.

### Kübik Bezier Eğri

Bu öğe, en az iki eğri-üzerinde nokta ve her bir uçta
 bir eğri-dışı kontrol noktası ile belirtilir (yani toplamda eğri-dışı 
iki nokta [eğrinin başlangıç ve bitiş noktaları]). Yalnızca 
eğri-üzerinde iki nokta varsa, bu bir Bezier kübik bölümdür ve dört 
nokta tam olarak Bezier kontrol noktalarıdır.

Eğri üzerinde daha fazla nokta varsa, bu, birden 
fazla Bezier kübik segmentten oluşan sürekli (C2) interpolasyonlu (Yani 
eğri birbirini sürekli şekilde takip eden ve keskin köşe, kırıklı yapı 
barındırmayan) eğri olduğunu gösterir. Bu kullanışlı bir eğri türüdür, 
çünkü bölümlerin birleştiği yerlerde bile her yerde pürüzsüz bir 
görünüme sahiptir.

Bezier kübik spline oluşturmak için `Çizim → Bezier Kübik Eğri`'yi seçin. Ardından kübik parçanın bir uç noktasını belirtmek için `Farenin sol tuşu`na
 tıklayın. Fare düğmesini bırakıp fareyi hareket ettirdiğinizde; kübik 
segmentin diğer uç noktası sürüklenir. Daha fazla eğri noktası eklemek 
için `farenin sol tuşu`na tıklayın. Eğriyi bitirmek için `Farenin sağ tuşu`na tıklayın veya ESC tuşuna basın.

İki kontrol noktası başlangıçta uç noktalar 
arasındaki düz bir hat’ta yerleştirilir; bu, küpün başlangıçta düz bir 
çizgi olarak göründüğü anlamına gelir. İstenilen eğriyi oluşturmak için 
kontrol noktalarını sürükleyin.

Kapalı bir eğri (teknik olarak, bir "periyodik eğri")
 oluşturmak için, eğriyi her zamanki gibi oluşturarak başlayın, eğri 
üzerinde ilave noktalar (yani yeni eğri parçaları) oluşturmak için `sol tıklayın`. Ardından fareyi eğrideki ilk noktanın üzerine getirin ve `sol tıklayın`.
 Eğri, ilk nokta da dahil olmak üzere her yerde C2 sürekliliğinde (yani 
pürüzsüz, kırıksız) olacak olan periyodik bir eğriye dönüştürülecektir.

### TrueType Yazı Tipinde Metin

Bu öğe, metnin her köşesinde bulunan dört nokta ile 
tanımlanır. Noktalar arasındaki mesafe metnin yüksekliğini ve 
genişliğini belirler; aralarındaki çizginin açısı metnin yönünü belirler
 ve konumları metnin konumunu belirler.

Metni oluşturmak için `Çizim → TrueType Yazı Tipinde Metin` menü yolunu seçin (Kısayol tuşu `T`). Ardından metnin sol üst nokta konumunu belirtmek için `farenin sol butonu` ile tıklayın. Fareyi hareket ettirdiğinizde Metnin sağ alt noktasının 
konumu sürüklenir; bu noktayı yerleştirmek / sabitlemek için tekrar `farenin sol butonu`na tıklayın.

Metnin Yazı tipini değiştirmek için metin öğesini 
seçin. Özellik Penceresinde, bilgisayarınızda yüklü yazı tiplerinin bir 
listesi görünür; Kullanmak istediğiniz yazı tipini seçmek için yazı tipi
 adına `sol tıklayın`. Görüntülenen metni (metnin içeriğini) değiştirmek için metin öğesini seçin ve Özellik Penceresindeki `[change]` bağlantısına (text = ‘Abc’ [change]) tıklayın.

![Yazı Tipini ve Metni Değiştir](images/solvespace/008%20Metni%20degis.png)

### Resim / Görüntü

Bu öğe, bir çizime bir bitmap referans görüntüsü 
yerleştirmek için kullanılabilir. Bu öğe, TrueType Metin öğelerine 
benzer şekilde, görüntüyü konumlandırmak, sınırlamak ve yönlendirmek 
için kullanılabilen dört kontrol noktası ile tanımlanır. Görüntü 
öğeleri, tipik olarak diğer objeleri çizmek veya izlemek için referans 
olarak kullanılır ve daha sonra kaldırılır. Bu nedenle, Görüntü öğeleri 
dışa aktarılamaz.

### Öğeleri Böl ve Kırp

Bazı durumlarda, üst üste binen/çakışan şekiller 
oluşturarak ve ardından fazla çizgileri kaldırarak/silerek çizim yapmak 
istenir. Örneğin, bu durumda bir daire ve bir dikdörtgen çizilir; iki 
kısa çizgi ve kısa yay daha sonra tek bir kapalı şekil oluşturmak için 
silinir.

![Öğeleri Böl / Kırp](images/solvespace/009%20b%C3%B6l%2C%20k%C4%B1rp.png)

Çizgi fazlalıklarını kırpmak için, öğeleri kesiştiği 
yerden bölmek gerekir. SolveSpace çizgileri, daireleri, yayları ve 
Bezier eğrilerini birbiri ile bölebilir (yani metin, resim ,...vb öğeler
 bir çizgi, çember,...vb ile bölünemez). Bunu yapmak için, bölünecek iki
 öğeyi seçin ve ardından `Çizim → Kesişme Yerinde Eğrileri Böl` Menü yolunu seçin (Kısayol tuşu `I` {büyük harf ile Isparta’nın I’sı} ve i {küçük har ile İstanbul’un 
i’si}). Bu, her özgün öğeyi siler ve kesişen bir uç noktayı paylaşan iki
 yeni öğeyle değiştirir. Fazla çizgiler daha sonra her zamanki gibi 
silinebilir (ya da yapısı değiştirilerek referans olarak 
kullanılabilir).

Orijinal öğeler silindiği için orijinal öğeler 
üzerindeki tüm sınırlamalar / kısıtlamalar da silinir. Bu, çizimin bölme
 işleminden sonra artık istendiği gibi (daha önce sınırlandırıldığı 
şekliyle) sınırlandırılamayacağı anlamına gelir (Yani yeniden 
sınırlandırılması gerekir). Bir öge, bölünmeden önce yapı öğesi olarak 
işaretlenirse, bölme işlemi sonucunda silinmez, dolayısıyla 
kısıtlamalar devam eder.
