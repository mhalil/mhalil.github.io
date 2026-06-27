Title: Solvespace Bölüm 5: Çizgi Biçimleri
Date: 2022-03-03 11:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Çizgi, Biçim, Kozmetik, Kısıtla, Yorum, Seçim, Izgara, Görünüm, Yakala, Göster, Düzen, Çizgi, Biçim
Author: Mustafa Halil


## Bölüm 5: Çizgi Biçimleri

Bir çizginin veya eğrinin rengini, çizgi 
genişliğini veya diğer yardımcı çizgi (kozmetik) özelliklerini doğrudan 
değiştirmek asla mümkün değildir. Bunun yerine, bir öğenin kozmetik 
özellikleri, o öğe bir çizgi biçimine (stilini) atanarak belirtilebilir.
 Biçim rengi, çizgi genişliğini, metin yüksekliğini, metin kaynağını, 
metin dönme açısını ve bir nesnenin ekranda ve dışa aktarılan bir 
dosyada nasıl görüneceğini (ve olup olmayacağını) belirleyen diğer bazı 
özellikleri belirtir.

SolveSpace'in temel renk şeması, varsayılan 
biçimler (stiller) tarafından tanımlanır. Bunları görüntülemek için, 
Özellik penceresindeki ana ekrandan "`line styles` (*çizgi biçimleri/stilleri*)"ni
 seçin. Örneğin, çizgilerin varsayılan olarak beyaz, kısıtlamaların mor 
ve noktaların yeşil olarak belirlendiği yer burasıdır. Varsayılan 
biçimler değiştirilebilir. Bu değişiklikler kullanıcı yapılandırmasına 
(Windows'ta kayıt defteri, diğer platformlarda bir .json dosyası) 
kaydedilecek ve o bilgisayarda açılan tüm dosyalara uygulanacaktır.

![Çizgi Biçimleri](images/solvespace/35%20Cizgi%20Bicimi.png)

Çizimi güzelleştirmek (Kozmetik) veya başka 
amaçlar için özel biçimler oluşturmak da mümkündür. (Örneğin, lazer 
kesiciler, kesilecek gücü ve beslemeyi belirtmek için genellikle bir 
çizginin rengini kullanır.) Özel bir biçim oluşturmak için stil 
ekranında "`create a new custom style` (*yeni bir özel stil oluştur*)"ui seçin. Yeni stil, `s-100-new-custom-style` (*s-100-yeni -özel-biçim*) varsayılan adı ile stiller listesinin altında görünecektir.

![Yeni Özel Çizgi Biçimi/Stili](images/solvespace/36%20Yeni%20Cizgi%20Bicimi.png)

Bir stili değiştirmek için stiller listesindeki 
bağlantısını tıklayın. Renk, her bileşenin 0 ile 1 arasında olduğu 
kırmızı, yeşil, mavi seçenekleri olarak belirtilir. Çizgi genişliği 
piksel, inç veya milimetre olarak belirtilebilir. Çizgi genişliği piksel
 cinsinden belirtilirse, dışa aktarılan bir dosyadaki çizgi genişliği 
ekrandaki yakınlaştırma düzeyine bağlı olacaktır. Kullanıcı görüntüyü 
uzaklaştırırsa (böylece model ekranda daha küçük görünür), geometri 
küçülür, ancak piksel cinsinden ölçülen çizgiler aynı boyutta kalır; bu,
 dışa aktarılan dosyadaki modele kıyasla çizgilerin daha kalın 
görüneceği anlamına gelir.

Öğeler (çizgiler, çemberler veya yaylar gibi) bir
 çizgi stiline atanabilir. Bunu yapmanın bir yolu, Özellik penceresinde 
istenen çizgi stilinin ekranına girmek ve ardından istenen objeleri 
seçmektir. Ardından metin penceresindeki "`assign to style ...` (*... stilini ata*)" bağlantısını tıklayın. Bunu yapmanın başka bir yolu, varlığa sağ tıklayıp bağlam menüsünü kullanarak stile atamaktır.

![Yeni Çizgi Biçimini Uygula](images/solvespace/37%20Cizgi%20Bicimi%20Ata.png)

![Çizgi Biçiminin Uygulanmış Hali](images/solvespace/38%20Cizgi%20Bicimi%20Atanmis.png)

Yorumlara da (`Kısıtla → Yorum`) biçim
 (stil) atanabilir. Stil, metin yüksekliğini, metnin derece cinsinden 
dönüş açısını ve metnin hangi noktadan (üst, alt, sol, sağ, orta) 
hizalanacağını belirtmek için kullanılabilir. Izgarası Yakalama (`Görünüm → Yakalama Izgarasını Göster`, `Düzen → Seçimi Izgaraya Tuttur`) genellikle kozmetik metin oluştururken kullanışlıdır.

Kullanıcı tarafından oluşturulan stiller, 
geometriyle birlikte .slvs dosyasına kaydedilir. Kullanıcı tarafından 
oluşturulan stiller içeren bir parça bağlanırsa, stiller içe aktarılmaz;
 ancak bağlantılı varlıklar için stil tanımlayıcıları korunur. Bu, 
kullanıcının bağlanan (yani, "montajlanan") dosyadaki çizgi stillerini 
belirleyebileceği anlamına gelir.

Bir biçim/stil gizlenmişse, o stildeki tüm 
nesneler, grupları gösterilse bile gizlenecektir. Bir stil dışa 
aktarılabilir olarak işaretlenmemişse, o stildeki nesneler ekranda 
görünür, ancak dışa aktarılan bir dosyada görünmez. Bu davranış, yapı 
hatlarının davranışına benzer.

![Çizgi biçimini ekrandan göster/gizle](images/solvespace/39%20Cizgi%20Bicimini%20Gizle.png)
