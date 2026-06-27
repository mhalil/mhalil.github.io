Title: Solvespace Bölüm 3: Kısıtlamalar
Date: 2022-01-06 11:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Otomatik, Özel, Kısıtla, Sınırla, Genel, Çözümlenememe,  Çözüm, Başarısızlık, Referans, Ölçü, Mesafe, Çap, Açı, Yatay, Dikey, Nokta, Eğri, Düzlem, Uzunluk, Yarıçap, Oran, Fark, Orta Nokta, Simetri, Dik, Paralel, Teğet, Aynı yön, Sürükleme, Montaj, Kilit, Yorum
Author: Mustafa Halil


## Bölüm 3: Kısıtlamalar

![kisitla](images/solvespace/10%20Kisitla.png)

## Genel

Bir kısıtlama oluşturmak için önce 
sınırlandırılacak geometriyi seçin. Örneğin, iki nokta arasındaki 
mesafeyi sınırlandırırken, önce bu iki noktayı seçin. Ardından 
Sınırlandır menüsünden uygun kısıtlamayı seçin.  
Neyin seçildiğine bağlı olarak, aynı menü seçeneği 
farklı kısıtlamalar oluşturabilir. Örneğin, Mesafe / Çap menü seçeneği, 
bir daire seçilirse bir çap kısıtlaması oluşturur, ancak bir çizgi 
parçası seçilirse bir uzunluk kısıtlaması oluşturur. Seçilen öğeler, 
uygulanmak istenen kısıtlamaya karşılık gelmiyorsa (yanlış ya da hatalı 
seçim ya da kısıtlama seçeneği seçilmişse), SolveSpace bir hata mesajı 
görüntüler ve mesajda mevcut kısıtlamaların (neleri kapsadığına dair) 
bir listesi sunar.  
Çoğu kısıtlama, hem 3B hem de öngörülen biçimde 
mevcuttur. Bir çalışma düzlemi etkinse, kısıtlama, geometrinin o çalışma
 düzlemine izdüşümüne uygulanır. Hiçbir çalışma düzlemi aktif değilse, 
bu durumda kısıtlama, boş alandaki (çizim uzayındaki) gerçek geometriye 
uygulanır.  
Örneğin, aşağıda gösterilen çizgiyi göz önünde bulundurun:

![Sınırlandır / Kısıtla](images/solvespace/10%20Sinirla.png)

Çizginin uzunluğu iki farklı şekilde 
sınırlandırılmıştır. 50mm'lik üst sınırlama, çizginin gerçek uzunluğunu
 belirtir. 40mm'lik alt kısıtlama, çizginin XY düzlemine olan 
izdüşümünün uzunluğunu belirtir. (XY düzlemi sarı renkle 
vurgulanmıştır.) Noktalı mor çizgiler, çizgi parçasının öngörülen uç 
noktalarının konumlarını (izdüşüm doğrularını) belirtmek için çizilir.  
Normal çalışmada, kullanıcı bir çalışma düzlemini etkinleştirir (veya örneğin bir "`Yeni Çalışma Düzleminde Çizim Yap`"
 grubu oluşturularak bir çalışma düzlemi otomatik olarak 
etkinleştirilir). Kullanıcı daha sonra bir öğe, örneğin bir çizgi çizer.
 Bir çalışma düzlemi aktif olduğundan, çizgi o çalışma düzleminde 
oluşturulur. Kullanıcı daha sonra örneğin uzunluğunu belirterek bu 
çizgiyi sınırlandırır. Çalışma düzlemi hâlâ aktif olduğundan, kısıtlama 
aslında çizgi parçasının çalışma düzlemine izdüşümü için geçerlidir.  
Bu durumda, öngörülen mesafe 3B mesafeye eşdeğerdir.
 Çizgi parçası çalışma düzleminde bulunuyorsa, o çizgi parçasının 
çalışma düzlemine izdüşümü sadece o çizgi parçası olur. (Yani çalışma 
düzlemi içerisinde yapılan çizim öğeleri, aslında çalışılan düzlemin 
izdüşümüdür.) Bu, bir çalışma düzleminde çizim yaparken bunların çoğunun
 göz ardı edilebileceği anlamına gelir.  
Yine de, öngörülen kısıtlamaları daha karmaşık 
şekillerde kullanmak mümkündür. Örneğin, kullanıcı çalışma düzlemi A'da 
bir çizgi parçası oluşturabilir ve projeksiyonunu çalışma düzlemi B'ye 
sınırlayabilir.  
Kısıtlamalar eskiz üzerinde mor renkle 
oluşturulmuştur. Bir kısıtlamanın kendisiyle ilişkili bir etiketi varsa 
(örneğin mesafe veya açı), bu etiket fare ile sürüklenerek yeniden 
konumlandırılabilir. Boyutu değiştirmek için, etikete çift tıklayın; 
ekranda yeni değerin girilebileceği bir metin kutusu belirecektir. 
Değişikliği uygulamak için `Enter`'a, iptal etmek için `ESC`'ye basın.

## Otomatik Kısıtlamalar

Yapılandırma ekranında "**enable automatic line constraints** (otomatik çizgi kısıtlamalarını etkinleştir)" etiketli bir seçenek 
vardır. Bu seçenek işaretliyse ve çizilen çizgi neredeyse yataysa, 
çizginin ortasında yatay ve dikey bir kısıtlama (H harfi) belirecek ve 
çizginin ikinci noktasının yerine tıklandığında kısıtlama 
uygulanacaktır. Benzer şekilde, neredeyse dikey bir çizgi çizildiğinde, 
otomatik olarak bir "V" kısıtlaması görünecektir. Doğru, yatay veya 
dikeye yeterince yakın değilse, herhangi bir kısıtlama eklenmez. Çizim 
yaparken `CTRL` tuşunu basılı tutmak da bu özelliği devre dışı bırakacaktır.

![Otomatik Çizgi Kısıtlaması](images/solvespace/11%20Otomatik%20sinirla.png)

Otomatik kısıtlama fazlaysa veya çizimin aşırı 
sınırlandırılmasına neden olacaksa, çizgi yerleştirme sırasında 
kısıtlama harfi gösterilse bile oluşturulmaz. Benzer şekilde, çizimi 
aşırı sınırlayacak bir mesafe veya çap kısıtlaması eklenirse, bu 
kısıtlama bir referans (REF) olarak oluşturulacaktır. (Örneğin 
dikdörtgenin kısa kenarlarından biri ölçülendirilip kısıtlandıktan 
sonra, diğer kısa kenar da ölçülendirilmek istenildiğinde, bu ölçü REF 
etiketi ile gösterilecektir. Bu ölçü değiştirilemez, değiştirilmesine 
imkan verilmiyor anlamı çıkar.)  
Yapılandırma ekranındaki diğer bir seçenek de "**edit newly added dimensions** (yeni eklenen boyutları düzenle)" seçeneğidir. Bu seçenek 
etkinleştirildiğinde, yeni bir Mesafe, Uzunluk Oranı veya Uzunluk Farkı 
kısıtlaması eklendiğinde, belirli bir değerin girilebilmesi için giriş 
kutusu otomatik olarak görünür. Seçenek kapalıyken, kullanıcının 
kısıtlamayı oluşturması ve ardından değeri düzenlemek için üzerine çift 
tıklaması gerekir ki, bu neredeyse her zaman yapmak istediğimiz şeydir.

![Yeni Eklenen Boyutları Düzenle](images/solvespace/12%20Eklenen%20boyutu%20duzenle.png)

## Çözümlenememe (Çözüm Başarısızlığı)

Bazı durumlarda, çözücü başarısız olur. Bunun 
nedeni genellikle belirtilen kısıtlamaların tutarsız veya gereksiz 
olmasıdır. Örneğin, iç açıları 30, 50 ve 90 derece olan bir üçgen 
tutarsızdır - açıların toplamı 180 değildir, bu nedenle üçgen asla 
birleştirilemez. Bu bir hatadır.  
İç açıları 30, 50 ve 100 derece ile sınırlandırılmış
 bir üçgen de bir hatadır. Bu tutarsız değildir, çünkü açıların toplamı 
180 derecedir; ama gereksiz, çünkü bu açılardan sadece ikisinin 
belirtilmesi gerekiyor.  
Çizim tutarsız veya (kısıtlamalar) fazlaysa, grafik 
penceresinin arka planı (normal siyah renk yerine) kırmızıya boyanır ve 
özellik penceresinde bir hata görüntülenir:

![Çözücü Hatası](images/solvespace/13%20Cozucu%20Hatasi.png)

SolveSpace kolaylık sağlamak adına, çizimi tekrar
 tutarlı hale getirmek için kaldırılabilecek bir kısıtlama listesi 
hesaplar. Bunların hangi kısıtlamalar olduğunu görmek için fareyi 
özellik penceresindeki bağlantıların üzerine getirin; kısıtlama, grafik 
penceresinde vurgulanmış olarak görünecektir. Bu listedeki bir veya daha
 fazla kısıtlamayı silerek kullanıcı, çizimi tekrar tutarlı hale 
getirebilir.  
Çözücü yakınsayamadığında farklı türde bir hata 
oluşur. Bu, çözücüde bir kusur olabilir veya imkansız geometri 
belirtildiği için oluşabilir (örneğin, kenar uzunlukları 3, 4 ve 10 olan
 bir üçgen; 3 + 4 = 7 < 10). Bu durumda, benzer bir hata mesajı 
görüntülenir, ancak bir şeyleri düzeltmek için kaldırılacak bir 
kısıtlama listesi yoktur. Sorun, kısıtlamaları kaldırarak veya 
düzenleyerek veya `Düzen → Geri Al`'ı seçerek çözülebilir.

## Referans Ölçüler

( Menü Yolu: `Sınırlandır → Ölçüyü Referans Yap / Yapma` - Kısayol tuşu: `E` )  
Varsayılan olarak, ölçülendirme geometriyi 
yönlendirir. Bir çizgi parçası 20,00mm uzunluğa sahip olacak şekilde 
sınırlandırılmışsa, bu uzunluk doğru olana kadar çizgi parçası 
değiştirilir.  
Referans ölçülendirme bunun tersidir: Geometri 
ölçülendirmeyi yönlendirir. Bir çizgi parçasının uzunluğu üzerinde bir 
referans boyutu varsa, bu uzunluğu serbestçe değiştirmek yine de 
mümkündür ve boyut, bu uzunluk ne olursa olsun görüntülenir. Referans 
ölçümlendirme geometriyi kısıtlamaz.  
Bir ölçülendirmeyi referans ölçümlendirmeye dönüştürmek için, `Sınırlandır → Ölçüyü Referans Yap / Yapma`'yı seçin. Görüntülenen uzunluk veya açıya eklenen "**REF**"
 ibaresi ile bir referans boyuta dönüşür. Bir referans ölçüye çift 
tıklamak hiçbir şey yapmaz (ölçüyü değiştirmek için metin kutusu 
görüntülenmez); ölçü kullanıcı tarafından değil geometri tarafından 
belirlenir, bu nedenle referans ölçü için yeni bir değer girmek anlamlı 
değildir.

## Özel Kısıtlamalar

Belirli bir kısıtlama hakkında bilgi / yardım almak için, öncelikle herhangi bir öğe seçmeden (hiç bir şey seçili olmadan) `Sınırlandır` menüsünden ilgili seçeneği seçin. Seçmiş olduğunuz sınırlandırma 
seçeneğine ait tüm olasılıkları listeleyen bir hata mesajı 
görüntülenecektir.  
Genel olarak, öğelerin seçilme sırası önemli 
değildir. Örneğin, kullanıcı nokta-çizgi arasındaki mesafeyi 
kısıtlıyorsa, noktayı ve ardından çizgiyi veya çizgiyi ve ardından 
noktayı seçebilir ve sonuç aynı olur. Bazı istisnalar mevcuttur ve 
aşağıda belirtilmiştir.

## Mesafe / Çap

( Menü Yolu: `Sınırlandır → Mesafe / Çap` - Kısayol tuşu: `D` )  
Bu kısıtlama, bir yayın veya dairenin çapını ya da 
bir doğru parçasının uzunluğunu veyahut bir nokta ile başka bir öğe 
arasındaki mesafeyi belirler.  
Bir nokta ile bir düzlem veya bir nokta ile bir 
düzlem yüzeyi ya da bir çalışma düzleminde bir nokta ile bir çizgi 
arasındaki mesafe kısıtlanırken, mesafe işaretlenir. Mesafe, noktanın 
düzlemin üstünde veya altında olmasına bağlı olarak pozitif veya negatif
 olabilir. Mesafe çizimde her zaman pozitif olarak gösterilir; diğer 
tarafa çevirmek için negatif bir değer girin.

## Açı

( Menü Yolu: `Sınırlandır → Açı` - Kısayol tuşu: `N` )  
Bu kısıtlama, iki vektör arasındaki açıyı belirler. 
Vektör, yönü olan herhangi bir şeydir; SolveSpace'de çizgi parçaları ve 
normaller vektörlerdir. (Yani kısıtlama, iki doğru parçasına ya da bir 
doğru parçasına ve bir normale veyahut iki normale uygulanabilir.) Açı 
kısıtlaması hem projeksiyonlu (İzdüşümlü) hem de 3B uzayında mevcuttur.  
Açı daima 0 ile 180 derece arasında olmalıdır. Daha 
büyük veya daha küçük açılar girilebilir, ancak bunlar 180 derecelik 
modüle alınacaktır. Ölçülendirmede açı işareti (°) gösterilmez.  
İki doğru kesiştiğinde dört açı oluşur. Bu açılar 
iki eşit çift oluşturur. Örneğin, resimdeki çizgiler 30 derece ve 150 
derecede kesişiyor. Bu iki açı (30 ve 150) bütünler açılar olarak 
bilinir ve her zaman 180 derecedir.

![Bütünler Açı](images/solvespace/14%20Aci%20-%20referans%20aci.png)

(Çizimde açı kısıtlamalarından üçünün referans 
ölçü olduğuna dikkat edin. Açılardan herhangi biri verildiğinde, diğer 
üçünü hesaplayabiliriz; bu nedenle, bu açılardan birden fazlasını 
belirten bir çizim aşırı kısıtlanmış olur ve çözülemez.)  
Yeni bir açı kısıtlaması oluşturulduğunda, 
SolveSpace hangi tamamlayıcı açının sınırlandırılacağını keyfi olarak 
seçer. Hangi açının seçildiğini belirtmek için çizim üzerinde bir yay 
çizilir. Kısıtlama etiketi (ölçü yazısı) sürüklendikçe yay, etiketi 
(ölçüyü) takip edecektir.  
Yanlış tamamlayıcı açı sınırlandırılmışsa (yani açı 
etiketi, diğer bütünler açı ile görüntülenmek istenirse), kısıtlamayı 
(ölçü etiketini) seçip ardından `Sınırlandır → Diğer Tümler Açı`'yı seçin. Bir bütünler açıda 30 derecelik bir kısıtlama, diğerinde 150 derecelik bir kısıtlamaya tam olarak eşdeğerdir.

## Yatay / Dikey

( Menü Yolu: `Sınırlandır → Yatay` - Kısayol tuşu: ``H )  
( Menü Yolu: `Sınırlandır → Dikey` - Kısayol tuşu: `V` )  
Bu kısıtlama, bir çizgi parçasını yatay veya dikey 
olmaya zorlar. Bu kısıtlama iki noktaya da uygulanabilir, bu durumda bu 
noktaları birleştiren (sanal) doğru parçasına uygulanır, yani noktalar 
yatay da ya da dikeyde aynı hizaya göre sınırlandırılmış olur.  
Bu ısıtlama için, bir çalışma düzlemi etkin 
olmalıdır, çünkü "yatay" veya "dikey" (ibarelerinin anlamı), çalışma 
düzlemi tarafından tanımlanır.  
Mümkün olduğunda yatay ve dikey kısıtlamaları 
kullanmak iyidir. Bu kısıtlamaların çözülmesi çok basittir ve yakınsama 
sorunlarına yol açmaz. Mümkün olduğunda, çalışma düzlemlerini, çizgiler 
bu çalışma düzlemleri içinde yatay ve dikey olacak şekilde tanımlayın.

## Noktada / Eğride / Düzlemde

( Menü Yolu: `Sınırlandır → Noktada / Eğride / Düzlemde` - Kısayol tuşu: `O` )  
Bu kısıtlama, iki noktanın çakışmasını veya bir 
noktanın bir eğri üzerinde ya da bir noktanın bir düzlem üzerinde 
bulunmasını/yerleşmesini sağlar.  
Nokta-çakışma kısıtlaması, hem 3B hem de 2B (2 
boyutlu, bir düzlem üzerinde) çizimde mevcuttur. 3B nokta-çakışma 
kısıtlaması, üç serbestlik derecesini kısıtlar; 2B yalnızca iki tanesini
 kısıtlar. Bir çalışma düzleminde iki nokta çizilir ve ardından 3B'de 
çakışık olarak sınırlandırılırsa, bir hata ortaya çıkar - bunlar zaten 
bir boyutta (düzlemin normal boyutu) çakışıktır, bu nedenle üçüncü 
kısıtlama denklemi gereksizdir. (2B'de çizim yapıldığında zaten düzlem 
koordinatı, bir noktayı kısıtlamış oluyor.)  
Bir noktanın bir daire (veya bir dairenin yayı) 
üzerine yerleştirilerek kısıtlandığında, gerçek kısıtlama noktayı bu 
daire boyunca silindirik yüzey üzerinde durmaya zorlar. Nokta ve daire 
zaten aynı düzlemdeyse (örneğin, her ikisi de aynı çalışma düzleminde 
çizilmişse), nokta eğri üzerinde durur, aksi halde olmaz.

## Eşit Uzunluk / Yarıçap / Açı

( Menü Yolu: `Sınırlandır → Eşit Uzunluk / Yarıçap / Açı` - Kısayol tuşu: `Q` )  
Bu kısıtlama, iki uzunluğu, açıyı veya yarıçapı eşit olmaya zorlar.  
Eşit açı kısıtlaması, girdi olarak dört vektör 
gerektirir: iki eşit açı, her bir girdi çifti arasındaki açıdır. 
Örneğin, A, B, C ve D doğru parçalarını seçin. Kısıtlama, A ve B 
doğruları arasındaki açıyı, C ve D doğruları arasındaki açıya eşit 
olmaya zorlar. Yanlış tamamlayıcı açı seçilirse, açı kısıtlaması için 
olduğu gibi, `Sınırlandır → Diğer Bütünler Açı`'yı seçin.  
Bir çizgi öğesi ve dairenin bir yayı seçilirse, 
çizginin uzunluğu yayın uzunluğuna (yarıçapına değil) eşit olmaya 
zorlanır.

## Uzunluk Oranı

( Menü Yolu: `Sınırlandır → Uzunluk Oranı` - Kısayol tuşu: `Z` )  
Bu kısıtlama, iki doğru parçasının uzunlukları 
arasındaki oranı belirler. Örneğin, A çizgisi ve B çizgisi 2:1 uzunluk 
oranına sahipse, A 50 mm uzunluğunda ve B 25 mm uzunluğundaysa kısıtlama
 karşılanır.  
Çizgilerin seçilme sırası önemlidir; A çizgisi B 
çizgisinden önce seçilirse, oran A'nın uzunluğu: B'nin uzunluğudur.

## Uzunluk Farkı

( Menü Yolu: `Sınırlandır → Uzunluk Farkı` - Kısayol tuşu: `J` )  
Bu kısıtlama, iki doğru parçasının uzunlukları 
arasındaki farkı belirler. Örneğin, A çizgisi ve B çizgisi 5 mm uzunluk 
farkına sahipse, A 50 mm uzunluğunda ve B 55 mm uzunluğunda veya 45 mm 
uzunluğundaysa kısıtlama karşılanır.  
Daha kısa olan öğenin kısıtlamasını düzenlerken, 
negatif bir fark girilebileceğini/yazılabileceğini unutmayın. Aynı 
zamanda değer, her zaman pozitif bir sayı (mutlak fark) olarak 
görüntülenir ve pozitif sayıların girilmesi/yazılması "yönü" 
değiştirmez.

## Orta Noktada

( Menü Yolu: `Sınırlandır → Orta Noktada` - Kısayol tuşu: `M` )  
Bu kısıtlama, bir noktayı bir çizginin orta noktasında sabitlemeye/yerleştirmeye zorlar.  
Orta nokta kısıtlaması ayrıca bir çizginin orta 
noktasını bir düzleme sabitlemeye/yerleştirmeye zorlayabilir; bu, bir 
nokta oluşturmaya, o noktayı çizginin orta noktasında sınırlamaya ve 
ardından bu orta noktayı düzlemde sabitlemeye şekilde sınırlamaya 
eşdeğerdir.

## Simetrik

( Menü Yolu: `Sınırlandır → Simetrik` - Kısayol tuşu: `Y` )  
Bu kısıtlama, iki noktayı bir düzlem etrafında 
simetrik olmaya zorlar. Kavramsal olarak bu, simetri düzlemine bir ayna 
yerleştirirsek ve A noktasının yansımasına bakarsak, o zaman B 
noktasının üzerinde duruyormuş gibi görüneceği anlamına gelir.  
Simetri düzlemi, bir çalışma düzlemi seçilerek 
açıkça belirtilebilir. Veya simetri düzlemi, bir çalışma düzleminde bir 
çizgi olarak belirtilebilir; simetri düzlemi bu çizgiden geçer ve 
çalışma düzlemine diktir. Veya simetri düzlemi atlanabilir; bu durumda, 
aktif çalışma düzleminin dikey eksenine veya yatay eksenine paralel 
olduğu sonucuna varılır. Noktaların başlangıçta çizildiği konfigürasyona
 hangisinin daha yakın olduğuna bağlı olarak yatay veya dikey eksen 
seçilir.

## Dik

( Menü Yolu: `Sınırlandır → Dik` - Kısayol tuşu: `[` )  
Bu kısıtlama, 90 (doksan) derecelik bir açı 
kısıtlamasına tam olarak eşdeğerdir. (Bu kısıtlama ile seçili çizgiler 
bir birine 90° olacak şekilde sınırlandırılır.)

## Paralel / Teğet

( Menü Yolu: `Sınırlandır → Paralel / Teğet` - Kısayol tuşu: `L` )  
Bu kısıtlama, iki vektörü paralel olmaya zorlar.  
2B'de (yani, bir çalışma düzlemi aktifken), sıfır 
derecelik açı kısıtlaması paralel kısıtlamaya eşdeğerdir. 3B'de öyle 
değil.  
Bir A birim vektörü ve bir teta açısı verildiğinde, 
genel olarak A ile bir teta açısı yapan sonsuz sayıda birim vektör 
vardır. (Örneğin, bize vektör (1, 0, 0) verilmişse, o zaman (0, 1) , 0),
 (0, 0, 1) ve diğer birçok birim vektörün tümü A ile doksan derecelik 
bir açı yapar.) Ancak bu, teta = 0 için doğru değildir; bu durumda, 
sadece iki tane vardır, A ve -A.  
Bu, normal bir 3B açı kısıtlamasının yalnızca bir 
serbestlik derecesini kısıtlarken, bir 3B paralel kısıtlamanın iki 
serbestlik derecesini kısıtladığı anlamına gelir.  
Bu kısıtlama aynı zamanda bir doğruyu bir eğriye 
teğet olmaya zorlayabilir veya iki eğriyi (örneğin bir daire ve bir 
kübik eğri) birbirine teğet olmaya zorlayabilir. Bunu yapmak için, iki 
eğrinin bir uç noktasını paylaşması gerekir; bu genellikle bir 
nokta-çakışma kısıtlaması ile elde edilir. Kısıtlama onları bu noktada 
da teğet olmaya zorlayacaktır.

## Aynı Yön

( Menü Yolu: `Sınırlandır → Aynı Yön` - Kısayol tuşu: `X` )  
Bu kısıtlama, iki normali (normal doğrultuyu) aynı yönelime sahip olmaya zorlar.  
Normalin bir yönü vardır; bu yönde bir ok olarak 
çizilir. O okun yönü iki açıyla belirtilebilir. Normal, bu iki açıyı ve 
bu okla ilgili bükülmeye karşılık gelen bir ek açıyı belirtir.  
(Teknik olarak normal, bir koordinat sisteminden 
diğerine dönüş matrisini temsil eder. Dahili olarak bir birim 
kuaterniyon (dörtlü grup) olarak temsil edilir.)  
Örneğin, aşağıdaki resim, normalleri paralel olacak 
şekilde sınırlandırılmış iki çalışma düzlemini göstermektedir:

![Normal Yönleri](images/solvespace/15%20Normaller.png)

Normaller paralel olduğundan, düzlemler 
paraleldir. Ancak bir düzlem diğerine göre eğilmiştir/açılıdır, bu 
nedenle düzlemler aynı değildir. Soldaki çizgi en soldaki düzlemde yatay
 olacak şekilde sınırlandırılır ve sağdaki çizgi en sağdaki ile yatay 
olacak şekilde kısıtlanır. Çalışma düzlemlerinin normalleri paralel 
olmasına rağmen bu çizgiler paralel değildir.  
"**Aynı Yön**" kısıtlamasını "**Paralel**" kısıtlamasıyla değiştirirsek, iki çalışma düzlemi aynı olur ve iki yatay çizgi paralel hale gelir.  
Bu sınırlama, bir montaj işlemi oluştururken yararlı
 bir kısıtlamadır; tek bir "aynı yön" kısıtlaması, bağlantılı bir 
parçanın dönme serbestlik derecelerinin üçünü de sabitleyecektir.

## Sürüklendiği Yerde Montajı Kilitle

( Menü Yolu: `Sınırlandır → Sürüklendiği Yerde Montajı Kilitle` - Kısayol tuşu: `]` )  
Çözücünün, konumunu değiştirmeyeceği şekilde bir 
noktayı sınırlayın. Bu, noktanın, üzerinde olduğu (bağlı, sahibi olan) 
öğeyi veya noktanın kendisini sürükleyerek doğrudan konumun 
değiştirilmesini engellemez. Çözücüye, noktayı tamamen sınırlandırılmış 
olarak düşünmesi talimatını verir. Bu, kenarları eşit ve bir noktası 
kilitli olan bir eşkenar üçgen çizerek kolayca gösterilebilir. Bu 
kilitli noktanın karşısındaki tarafı sürüklemek konumunu değiştirmez, 
bunun yerine üçgeni yeniden boyutlandırır.

## Yorum

(Menü Yolu: `Sınırlandır → Yorum` - Kısayol tuşu: `;` [noktalı virgül] )  
Yorum, çizimde görünen tek satırlık bir metindir. Bir yorum oluşturmak için, `Sınırlandır → Yorum`'u seçin ve ardından yeni yorumun orta noktasının konumunu belirtmek için `farenin sol tuşu`na tıklayın. Yorumu taşımak için fare ile sürükleyin. Metni değiştirmek için çift tıklayın.  
Yorumun, geometri üzerinde hiçbir etkisi yoktur; 
sadece insanlar tarafından okunabilen bir nottur. Varsayılan olarak 
yorum, kısıtlamalarla aynı renkte gösterilir; ancak çizgi genişliğini ve
 rengini, metin yüksekliğini, metin kaynağını (sol, sağ, üst, alt, orta)
 ve metin açısını belirlediğimiz özel bir çizgi biçimi oluşturulup bu 
yeni biçimi yorum/açıklama biçimi olarak atayabiliriz.  
Bir çalışma düzleminde bir yorum oluşturulursa, 
metin o çalışma düzleminin yüzeyi içinde çizilecektir/konumlanacaktır. 
Aksi takdirde (örneğin; `Yeni Grup → 3d'de Çizim Yap` menü 
yolu seçildikten sonra çizim uzayına bir yorum eklenirse), metin her 
zaman ekran düzleminde öne bakacak şekilde çizilir, (yani görüntüyü / 
modeli döndürsek/çevirsek bile yorum metni düz, ve okunaklı görünür).  
Varsayılan olarak yorumlar, grupları etkin/aktif 
olmadığında, diğer tüm kısıtlamalarda olduğu gibi gizlenir. Bir yorum 
özel bir biçime atanmışsa, bu yorum, biçim (ve grup ve genel olarak 
kısıtlamalar) gösterildiği sürece, grubu etkin olmadığında bile 
gösterilecektir.

![Yeni Yorum Biçimi](images/solvespace/16%20Yeni%20Yorum%20Bicimi.png)
