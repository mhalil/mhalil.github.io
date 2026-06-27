Title: Solvespace Bölüm 4: Gruplar
Date: 2022-01-25 00:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Grup, Gruplama, Çizim, Calışma Düzlemi, Kopya, Dogrusal, Dairesel, Uzat, Katıla, Ekstrude, Döndür, Kısmi, Helis, Bağla, Montaj, 
Author: Mustafa Halil


## Bölüm 4: Gruplar

Grupların listesini görüntülemek için Özellik penceresinin ana sayfasına gidin. Buna, Özellik penceresinin `sol üst köşesindeki bağlantı`dan veya `ESC` tuşuna basarak erişilebilir. Bir grubun sayfasını görüntülemek için listede adını tıklayın.  
Tüm grupların bir adı vardır. Grup 
oluşturulduğunda varsayılan bir ad atanır (ör. "g008-extrude"). 
Kullanıcı bu ismi değiştirebilir; bunu yapmak için Özellik penceresinde 
grubun sayfasına gidin ve [`rename` (yeniden adlandır)] öğesini seçin.

![Grubu yeniden adlandır](images/solvespace/17%20Grubu%20yeniden%20adlandir.png)

Bir katı oluşturan (örn. Ekstrüzyon ile veya döndürerek) gruplar, Özellik penceresindeki sayfada görüntülenen bir "`solid model as` (*katı model olarak*)" seçeneğine sahiptir. Grup, modele malzeme ekleyerek `birleşim` veya malzemeyi çıkararak `fark` olarak birleştirilebilir. Üçüncü bir seçenek, yalnızca her iki katının içine giren malzemeyi koruyan `kesişim`dir. Yani burada bulunan seçenekler ile iki katı maddenin `birleşimi`, `kesişimi` ya da `farkı` alınabilir.

`Birleşim`, `fark` ve `kesişim` işlemleri ya üçgen ağlar olarak ya da tam NURBS yüzeyleri olarak 
gerçekleştirilebilir. Üçgen ağların hesaplanması hızlı ve sağlamdır, 
ancak parçalı doğrusal segmentler olarak yaklaşılması için herhangi bir 
düzgün eğri gerektirirler. NURBS yüzey işlemleri o kadar sağlam değildir
 ve bazı geometri türleri için başarısız olacaktır; ancak bunlar tam 
olarak düzgün eğrileri temsil eder, bu da örneğin birçok parçalı 
doğrusal kenar yerine dairesel bir yayın tam bir daire olarak göründüğü 
bir DXF'yi dışa aktarmayı mümkün kılar.

![Katı Model Olarak (Birleştir, Çıkar ya da Kesişimi al)](images/solvespace/18%20Kat%C4%B1%20model.png)

Bu grupların da ürettikleri yüzeylerin 
(örneğin fark / çıkarma işlemi) rengini belirleyen bir rengi vardır. 
Rengi değiştirmek için, Özellik penceresinde grubun sayfasındaki renk 
örneklerinden birine tıklayın. (Şekil 18'e bakın, `solid model as` kısmındaki `color` seçeneği)  
Grubun özellik penceresindeki sayfası, ayrıca 
tüm isteklerin ve tüm kısıtlamaların bir listesini içerir. Bir 
kısıtlamayı veya isteği tanımlamak için fareyi, (örneğin bir kısıtlama) 
adının üzerine getirin; (farenin üzerine geldiği kısıtlama) grafik 
penceresinde vurgulanmış olarak görünecektir. Seçmek için özellik 
penceresindeki bağlantıya tıklayın. Bu, grafik penceresinde gerçek 
nesnenin üzerine gelip tıklamaya eşdeğerdir.

## 3B'de Çizim Yap

Bu, kullanıcının çizgiler, daireler, yaylar ve diğer eğriler çizebileceği yeni bir boş grup oluşturur.  
Nihai amaç, genellikle kapalı bölümler (üçgen 
veya dairesel kesikli bir kare veya daha karmaşık bir şekle sahip bir 
kare gibi) çizmektir. Bu bölümler, sonraki gruplar için bir girdidir. 
Örneğin, bir ekstrüzyon grubu, düz bir bölüm (kapalı bir dair, eğri ya 
da çokgen çizimi) alır ve bunu bir katı oluşturmak için kullanır.

Gruptaki tüm öğeler kapalı döngüler halinde 
birleştirilebiliyorsa, bu durumda döngülerin kapsadığı alan çok koyu 
mavi renkte gölgelenir. Bu, sonraki bir grup tarafından süpürülecek veya
 ekstrüde edilecek veya döndürülerek katılanacak alandır.

## Yeni Calışma Düzleminde Cizim Yap

Bu, yeni bir "`3B'de Çizim Yap`"a benzer yeni bir boş grup oluşturur. Aradaki fark, "`Yeni Çalışma Düzleminde Çizim Yap`"ın
 aynı zamanda bir çalışma düzlemi oluşturmasıdır. Çalışma düzlemi, çizim
 oluşturulduğunda seçilen objelere göre oluşturulur. Bunlar şunlar 
olabilir:

**Bir nokta ve iki doğru parçası**  
Yeni çalışma düzleminin başlangıç noktası 
belirtilen noktadadır. Bir nokta ve iki çizgi parçası seçiliyken ve `Yeni Grup → Yeni Çalışma Düzleminde Çizim Yap` menü yolu ile komut çalıştırılırsa, Seçilen nokta orijin yani merkez 
olmak üzere, seçili iki çizgi ile çakışık bir çalışma düzlemi 
oluşturulacak, Çalışma düzlemi iki çizgiye paraleldir. (yani, kullanıcı
 o yüzey/düzlem üzerinde çizim yapacaktır).

**Bir Nokta**  
Yeni çalışma düzleminin başlangıç noktası, 
belirtilen noktadadır. Çalışma düzlemi, taban koordinat sistemine 
diktir; örneğin, yatay ve dikey eksenleri +y ve -z yönlerinde veya +x ve
 +z yönlerinde veya herhangi bir başka kombinasyonda olabilir.  
Çalışma düzleminin oryantasyonu, çalışma düzlemi
 oluşturulduğunda görünümün konumundan çıkarılır; görünüm en yakın 
ortografik görünüme yakalanır ve çalışma düzlemi buna hizalanır.  
Bir parça çoğunlukla doksan derecelik açılardan 
oluşuyorsa, bu, çalışma düzlemleri oluşturmanın hızlı bir yoludur.

Yeni grubun ilişkili çalışma düzlemi, otomatik olarak etkin çalışma düzlemi olarak ayarlanır.

Bu gruptaki öğeler kapalı eğriler 
oluşturmuyorsa ekranda bir hata mesajı görüntülenir ve boşluk boyunca 
kırmızı bir çizgi çizilir. Eğrilerin tümü eş düzlemli değilse de bir 
hata görüntülenir. Konfigürasyon kısmından `check sketch for closed contour` (*kapalı kontur için eskizi kontrol et*)
 ayarını kapatırsanız, oluşturulan eskizin/çizimin, kapalı geometri 
oluşturup oluşturmadığı kontrol edilmez ve ekranda hata mesajı ve 
kırmızı çizgi gösterilmez.

![Kapalı olmayan kontur](images/solvespace/19%20Kapali%20olmayan%20kontur.png)

## Dogrusal Kopya

Bu grup, aktif gruptaki geometriyi alır ve düz bir çizgi boyunca birçok kez kopyalar.

Doğrusal Kopya grubu oluşturulduğunda, bir 
çalışma düzlemi etkinse, öteleme vektörü bu çalışma düzlemine paralel 
olmalıdır. Aksi takdirde, öteleme vektörü boş uzayda herhangi bir yere 
gidebilir.

Oluşturulacak kopya sayısı kullanıcı 
tarafından belirlenir. Bu değeri değiştirmek için grup sayfasındaki 
metin penceresindeki [change (değiştir)] bağlantısını tıklayın (Şekil 
20)

Kopyalar tek taraflı veya çift taraflı 
ötelenebilir. Kopyalar tek tarafa ötelenmişse, orijinal eskiz (taslak), 
tüm kopyaların solunda (veya üstünde, altında vb.) görünecektir. 
Kopyalar çift tarafa ötelenmişse, orijinal eskiz kopyaların ortasında 
görünecektir. (Şekil 20 ve 21)

![Tek Taraflı Doğrusal Kopya](images/solvespace/20%20Dogrusal%20Kopyala.png)

![Çift Taraflı Doğrusal Kopya](images/solvespace/21%20Cift%20Tarafli%20Dogrusal%20Kopyala.png)

Doğrusal Kopya komutu ile oluşturulacak 
kopyalar, orijinalinden veya 1 numaralı kopyadan (copy #1) başlayarak 
ötelenebilir. Öteleme işlemi, orijinalden başlıyorsa, öteleme orijinal 
eskizi içerecektir. (Yani ötelemenin 1. elemanı her zaman çizilen 
geometri olacak ve orijinal konumunda üretilecektir.) Öteleme komutu 1 
numaralı kopyadan (copy #1) başlıyorsa, orijinal eskiz çıktıya dahil 
edilmez. (Böylece 1 elemanlı bir kopya, giriş geometrisinin tek bir 
kopyasını oluşturur ve kullanıcının bunu uzayda herhangi bir yere 
çevirmesine olanak tanır.)

Etkin grup bir eskiz (taslak) çizimiyse, (3d 
çizim, yeni çalışma düzleminde çizim), çizim kademeli olarak 
tekrarlanır. Bu durumda, kullanıcı tipik olarak bir bölüm çizer, adım 
atar ve o bölümü tekrar eder ve ardından adımı çıkarır ve tekrar eder.

Aktif grup bir katı ise (ekstrüde edilmiş, 
helislenmiş, döndürmüş), katı model adımlanır ve tekrarlanır (adım adım 
kopyası çıkarılır). Bu durumda, kullanıcı bir bölüm çizecek, bölümü 
ekstrüde edecek ve ardından ekstrüzyonu adım adım tekrarlayacaktır.

Bazı durumlarda, bu iki olasılık (adım 
ekstrüzyonla & ekstrüzyonu adımla) eşdeğerdir. Çevirme vektörü kesit
 düzlemine paralel değilse, o zaman sadece ikinci seçenek çalışacaktır.

![Katıyı doğrusal olarak kopyala](images/solvespace/22%20Katiyi%20Otele.png)

## Dairesel Kopya

Bu grup, aktif gruptaki geometriyi alır ve bir daire boyunca defalarca kopyalar.

Grubu oluşturmadan önce, kullanıcı dönme 
eksenini seçmelidir. Bunu yapmanın bir yolu, bir nokta ve bir doğru 
parçası veya bir normal (normal doğrusu) seçmektir; dönme ekseni 
noktadan geçer ve doğru parçasına paralel veya normaldir.

Bir çalışma düzlemi aktifse, sadece bir 
noktayı seçmek de mümkündür; bu durumda, dönme ekseni o noktadan geçer 
ve çalışma düzlemine diktir. Bu, dönüşün çalışma düzlemi düzlemi içinde 
kaldığı anlamına gelir.

![Aktif Çalışma Düzleminde Dairesel Olarak Çoğalt / Kopyala](images/solvespace/23%20Aktif%20Calisma%20Duzleminde%20Dairesel%20Kopya.png)

Bir çalışma düzlemi aktifse, sadece bir 
noktayı seçmek de mümkündür; bu durumda, dönme ekseni o noktadan geçer 
ve çalışma düzlemine diktir. Bu, dönüşün çalışma düzlemi içinde kaldığı 
anlamına gelir.

Adım ve tekrar seçenekleri (tek taraflı / çift taraf, orijinal ile / kopya #1 ile), doğrusal kopyalama gruplarıyla aynıdır.

Kopya sayısı, **Doğrusal Kopya** ile aynı şekilde belirtilir. Döndürülmüş geometri henüz 
sınırlandırılmamışsa, kopyalar bir daire etrafında eşit aralıklarla 
yerleştirilecektir; örneğin 5 kopya istenirse kopyalar arasındaki açı 
değeri (boşluk) 360 / 5 = 72 derece olur.

Kopyaları tam bir daireden daha az (veya daha
 fazla) değer boyunca yerleştirmek için, fare ile kopyalardan birinin 
üzerindeki bir noktayı sürükleyin; dönüş açısı adımı değiştirildiği 
için geri kalan her şey bunu takip edecektir. Kısıtlamalar (örneğin bir 
açı kısıtlaması veya bir konum üzerinde nokta kısıtlaması) dönüş açısını
 tam olarak belirtmek için kullanılabilir.

![Dairesel olarak kopyala ve kısıtla](images/solvespace/24%20Dairesel%20Kopya.png)

![Dairesel olarak kopyala ve Çıkart](images/solvespace/25%20Dairesel%20Kopya%20Cikart.png)

## Uzatarak Katıla (Ekstrude)

Bu grup düz bir bölüm alır ve onu bir katı 
oluşturmak için ekstrüde eder, (düzlemi, normali yönünde uzatarak 
katılar). Düz kısım, Uzatarak Katıla grubu oluşturulduğunda grubun aktif
 olan kısmından alınır. (Bu genellikle çalışma düzleminde bir çizimdir 
veya 3B'de bir çizimdir, ancak bir adım ve tekrar da olabilir.)

Eskiz (Çizim) tek taraflı veya çift taraflı 
(simetrik) ekstrüde edilebilir. Çizim tek taraflı ekstrüde edilirse, 
oluşan yeni katı parça, orijinal çizimin tamamen üst veya alt kısmında 
oluşur. Ekstrüzyon yönünü ve ayrıca ekstrüzyon derinliğini belirlemek 
için yeni yüzeyde bir noktayı sürükleyin. Ekstrüzyon derinliği yaklaşık 
olarak doğru göründüğünde, kısıtlamalar kullanılarak tam olarak 
belirlenebilir. Örneğin, kullanıcı yeni ekstrüde edilmiş kenarlardan 
birinin uzunluğunu sınırlayabilir.

Çizim çift taraflı (simetrik) ekstrüde 
edilirse, orijinal çizim, yeni katının tam orta noktasında yer alır. Bu,
 katının orijinal çizim düzlemine göre simetrik olduğu anlamına gelir. 
Parça simetriye sahip olduğunda sonraki boyutlandırma genellikle daha 
basit hale gelir, bu nedenle mümkün olduğunda çift taraflı ekstrüzyon 
yapmak yararlıdır.

Uzatarak Katılama (Ekstrüde) Grubu 
oluşturulduğunda, bir çalışma düzlemi etkin olmalıdır ve ekstrüzyon yolu
 otomatik olarak o çalışma düzlemine normal (yönde) olacak şekilde 
sınırlandırılır. Bu örneğin, bir dikdörtgenin, bir dikdörtgen prizma 
oluşturacak şekilde ekstrüde edildiği anlamına gelir. Ekstrüzyon bir 
serbestlik derecesine sahiptir, bu nedenle tek bir mesafe kısıtlaması 
onu tamamen sınırlayacaktır. (Eğer `Yeni Grup → 3d'de Çizim Yap` (kısayol tuşu: `Shift+3`)
 seçeneği kullanılarak 3B uzayında, yani ekrana bakış açımız düzleminde
 bir eskiz çizer, çizim yaparsak) Ekstrüzyon oluşturmadan önce diğer 
çalışma düzlemi seçilerek (`Çizim → Çalışma Düzleminde`), 
çizimin, çizildiği çalışma düzleminden farklı bir çalışma düzlemine dik 
ekstrüzyon oluşturmak mümkündür. Bu, eğri ekstrüzyonlar oluşturmak için 
kullanılabilir.

Varsayılan olarak, yeni bir ekstrüzyon 
grubunda hiçbir çalışma düzlemi etkin değildir. Bu, kısıtlamaların 3 
boyutlu olarak uygulanacağı anlamına gelir; örneğin, bir uzunluk 
kısıtlaması, bir düzleme yansıtılan uzunluk üzerinde değil, gerçek 
uzunluk üzerinde bir kısıtlamadır. Bu genellikle istenen davranıştır, 
ancak bir çalışma düzlemini olağan şekilde etkinleştirmek mümkündür (onu
 seçip ardından `Çizim → Çalışma Düzleminde`'yi seçerek).

![3d'de Eskiz Çiz](images/solvespace/26%203d'de%20eskiz.png)

![Eskizi, XZ Düzleminde Uzatarak Katıla](images/solvespace/27%20XZ%20Duzleminde%20Uzatarak%20Katila.png)

![Eskizi, YZ Düzleminde Uzatarak Katıla](images/solvespace/28%20YZ%20Duzleminde%20Uzatarak%20Katila.png)

## Tam Döndürerek Katıla

Bu grup, düz bir çizimi (düzleme çizilmiş 2 
boyutlu kapalı kontura sahip bir eskizi) alır ve bunu belirli bir eksen 
etrafında süpürerek / döndürerek bir katıya dönüştürür. Tam Döndürerek 
Katılama grubu oluşturulduğunda aktif olan gruptan kesit alınır , yani 
aktif grupta çizilen eskiz, Tam Döndürerek Katılama kesit yapısıdır.

Tam Döndürerek Katılama grubu oluşturmak için bir çizgiyi seçip `Yeni Grup → Tam döndürerek katıla`'ı seçin (kısayol tuşu: `Shift+L`).
 Seçilen doğru parçası, dönüş eksenini belirtir. Çark grubu oluşturmanın
 bir başka yöntemi ise bir nokta ve bir çizgi parçası ya da normal 
doğrultusu seçmek, sonrasında `Shift+L` kısayolunu kullanmaktır.

Kesit, eğri boyunca süpürüldüğü için kendi 
kendisiyle kesişmemelidir. Kesit dönme eksenini keserse, kendisini 
keseceği için işlem başarısız olur.

![Tam Döndürerek Katıla komutu uygulanacak eskiz (kesit)](images/solvespace/29%20Kesit.png)

![Tam Döndürerek Katıla komutu sonrası oluşan Katı Model](images/solvespace/30%20Tam%20Dondurerek%20Katila.png)

## Kısmi Döndürerek Katıla

Bu grup düz bir çizim alır ve bunu belirli 
bir eksen etrafında süpürerek / döndürerek bir katı model oluşturur. Bu 
grup ile Tam Döndürerek Katıla grubu arasındaki fark, Kısmi Döndürerek 
Katıla komutunun eskizi (çizimi) tam 360 derece süpürmemesidir. Ortaya 
çıkan katı model, belirli bir açıyla sürüklenebilir veya kısıtlanabilir.
 360 derecenin ötesine sürüklenirse, bu, Tam Döndürerek Katıla grubuyla
 tamamen aynı katıyı oluşturacaktır.

Tam Döndürerek Katıla komutu anlatılırken 
çizilen eskize, Kısmi Döndürerek Katıla komutu uygulanıp kesit belirli 
bir açıya kadar sürüklenirse oluşan örnek görüntüyü aşağıda (Resim 31) 
görebilirsiniz.

![Kısmi Döndürerek Katıla komutu sonrası oluşan katı model](images/solvespace/31%20K%C4%B1smen%20Dondurerek%20Katila.png)

## Helis

Bu grup, düz bir çizimi (düzlem yüzeyde 
yapılan iki boyutlu kapalı kontura sahip bir eskizi) alır ve belirli bir
 eksen etrafında süpürürken aynı zamanda o eksen boyunca öteler. Sonuç 
olarak, vida dişleri veya diğer bükülmüş yüzeyleri modellemek için 
kullanılabilen sarmal bir yüzey oluşur. En yaygın iki yaklaşım, spiral 
bir şekil oluşturmak için çizim düzleminde bir eksen veya standart 
ekstrüzyonun bükülmüş bir versiyonu gibi davranan bir şey oluşturmak 
için çizim düzlemine dik bir eksen kullanmaktır.

![Helis Yay](images/solvespace/32%20Helis%20Yay.png)

Bir Helis grubu oluşturulduğunda, sarmalın 
ekseni boyunca bir yapı hattı da oluşturulacaktır. Bu çizginin uçlarını 
veya eksen üzerindeki diğer noktaları sürüklemek, sarmal ekstrüzyonun 
uzunluğunu değiştirecektir. Eksen üzerinde olmayan noktaları sürüklemek,
 bir **Kısmi Döndürerek Katıla** grubuna benzer şekilde 
sarmalın açısını değiştirir. Bir sarmalın açısı, çok uzun spiral 
şekillerin veya bir cıvata üzerindeki tüm dişlerin tek bir grupta 
oluşturulmasına izin vermek için 360 dereceden çok daha fazla olabilir.

![Helis Cıvata](images/solvespace/33%20Helis%20Civata.png)

## Bağla / Montajla

SolveSpace'de "parça" dosyaları ve "montaj" 
dosyaları arasında bir ayrım yoktur; bir dosyayı diğerine bağlamak her 
zaman mümkündür. Bir "montaj", yalnızca bir veya daha fazla parçayı 
birbirine bağlayan bir parça dosyasıdır.

Bağlantılı dosyası, montaj (derleme) içinde 
düzenlenemez. Tam olarak kaynak dosyada göründüğü gibi karşımıza çıkar, 
ancak isteğe bağlı bir konum ve yönlendirme ile dahil edilmiştir. Bu, 
bağlantılı parçanın altı serbestlik derecesine sahip olduğu anlamına 
gelir.

Parçayı taşımak (çevirmek) için üzerinde 
herhangi bir noktayı tıklayın ve sürükleyin. Parçayı döndürmek için 
herhangi bir noktayı tıklayın ve `Shift+Farenin Sol tuşu` ile Sürükleyin veya `Ctrl+Farenin Sol tuşu` ile Sürükleyin. Parçanın konumu ve yönü, diğer herhangi bir geometrinin kısıtlandığı şekilde, kısıtlamalarla sabitlenebilir.

Parça ayrıca altı serbestlik dereceli bir 
3Dconnexion kontrolör ile dönüştürülebilir. Bir montajdaki bir parçayı 
manipüle etmek için, o parça içindeki herhangi bir objeyi seçin 
(örneğin, bir nokta, bir çizgi parçası veya bir normal). 3Dbağlantı 
denetleyicisi, görünümü dönüştürmek yerine o kısmı hareket ettirir.

Ekranın içine veya dışına istenmeyen bir dönüş yapmamaya dikkat edin, çünkü bu hareket kolayca algılanamayabilir.

Parçayı ekrana dik olana en yakın koordinat ekseni (x, y veya z ekseni) etrafında tam olarak doksan derece döndürmek için `Düzen → İçe Aktarılanları 90° Döndür`'ü
 seçin. Bağlı gruptaki bir obje seçilirse, o gruptaki parça döndürülür. 
Bir içe aktarma grubu etkinse, etkin gruptan parça döndürülür.

**Aynı Yön** kısıtlaması, 
özellikle montaj parçaları bağlanırken kullanışlıdır. Bu tek kısıtlama, 
bağlantılı parçanın dönüşünü tamamen belirler. (Bağlantılı kısımda bir 
normal seçin, onu sınırlamak için başka bir normal seçin ve `Kısıtla → Aynı Yön`'ü seçin).

Bağlantılı kısım ayrıca ilişkili bir ölçek 
faktörüne sahiptir. Bu, parçanın daha küçük veya daha büyük bir 
versiyonunu bağlamayı mümkün kılar. Ölçek faktörü negatifse, parça ölçek
 faktörünün mutlak değeri ile ölçeklenir ve aynalanır.

![Montaj - Ölçek Değeri](images/solvespace/34%20Montaj%20Olcek.png)

SolveSpace ayrıca elektronik tasarım 
araçlarından baskılı devre kartlarını tanımlayan IDF (.emn) dosyalarını 
içe aktarma yeteneğine de sahiptir. Bu, muhafazaları tasarlamak ve bir 
montaj içindeki uyumu kontrol etmek için kullanışlıdır. Çizim objeleri 
ve devre kartını bir ekstrüzyon oluşturulacak ve ölçüm almak için 
kullanılabilir.

Dışa aktarım gruplarının özel bir "**solid model as** (*katı model olarak*)" seçeneği vardır: olağan "**birleşim**", "**fark**" ve "**kesişim**"e ek olarak, "birleştirme" seçeneğine sahiptirler. "**Montaj**"
 seçeneği, birbiriyle karışmaması (engellememesi) gereken parçalar bir 
montajda birleştirilirken kullanılmalıdır. Montajın karışmadığını 
doğrulamak için, `Analiz → Engelleyici Parçaları Göster`'i seçin.

Montaj komutu ile oluşturulan içe aktarma 
grubu, kapalı bir kontur oluşturan bir çizim içeriyorsa, bu grup, kontur
 aynı dosya içinde çizilmiş gibi aynı şekilde ekstrüde edilebilir. Bu, A
 dosyasına bir bölüm çizmenin, bu bölümü B dosyasına içe aktarmanın 
(bazı keyfi öteleme ve döndürmelerle) ve ardından B dosyasındaki 
parçanın bir özelliğini oluşturmak için ekstrüde etmenin mümkün olduğu 
anlamına gelir. A dosyasında yapılacak herhangi bir değişiklik, parça 
yeniden oluşturulduğunda B dosyasına iletilecektir.

Benzer şekilde, A dosyasına açık bir bölüm 
çizmek, bu bölümü B dosyasına bağlamak ve daha sonra bu bölümü kapatmak 
için B dosyasına ek çizgiler veya eğriler (aynı grupta veya başka bir 
grupta) çizmek mümkündür. C dosyası B dosyasına bağlanırsa, kapalı bölüm
 ekstrüde edilebilir. Bu, kullanıcının orijinaldeki bir değişikliğin o 
geometriyi kullanan tüm parçalara yayılacağı şekilde birden çok 
dosyadaki bölümleri veya bir bölümün bölümlerini yeniden kullanmasına 
olanak tanır.

Bir montaj dosyası yüklendiğinde, SolveSpace 
bağlantılı dosyaların tümünü de yükler. Bağlantılı dosyalar mevcut 
değilse, bir hata oluşur. Bir montaj dosyasını başka bir bilgisayara 
aktarırken, bağlantılı tüm dosyaları da aktarmak gerekir.
