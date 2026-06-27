Title: FreeCAD - Silk WB - Öğretici Doküman 1
Date: 2024-02-15 23:45
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 1 (Tutorial 0.01)

## NURBSlib_EVM'de ControlPoly4 ve CubicCurve4 makroları (komutları)

Öncelikle **NURBSlib_EVM**'nin ne olduğunu açıklayalım. NURBSlib_EVM, FreeCAD'de NURBS yüzeyleri oluşturmak için yazılmış python komut dosyaları ve makrolardır. **Silk**, **NURBSlib_EVM** projesinin yeni adıdır.

**ControlPoly4** ve **CubicCurve4** makroları (komutları) sırasıyla rasyonel bir kübik bezier eğrisini kontrol eden ve kullanan nesnelerdir

[NURBSlib_EVM projesinin ana sayfasına git.](http://edwardvmills.github.io/NURBSlib_EVM/)

## Bu özel eğitim / sunum için hedef kitle;

Bu eğitim, FreeCAD'in bilgili kullanıcılarına **NURBSlib_EVM** kütüphanesi hakkında bir fikir vermek için hazırlanmıştır. Şu anda temel FreeCAD işlemlerine ilişkin herhangi bir açıklama yapılmamaktadır.

Bir kütüphane olarak NURBSlib_EVM, model üretmek için kullanılabilecek temel öğeleri sağlar, ancak modernize edilmemiştir. Bu eğitimdeki bazı adımlar tekrarlayıcı olacaktır. Bunlar otomatikleştirilebilir ve sonunda bir çalışma tezgahı şeklinde otomatikleştirilecektir. Şu anda, nesnelerin kararlılığına ve çok yönlülüğüne öncelik verilmektedir. Arayüz minimaldır.

## Bu eğitimi / sunumu takip etmek için gerekenler

* FreeCAD 0.17'de bir makro ve Eklenti (Addon) kurma/yükleme becerisi gereklidir

* FreeCAD'de çizgi ve yay çizimleri oluşturma becerisi

* FreeCAD'deki üç temel düzlemin anlaşılması

* Inkscape veya Illustrator'da bulunan NURBS veya Bezier eğrileri hakkında en azından belli belirsiz bir fikre sahip olmak çok faydalıdır.

## Motivasyon mu? Birkaç eğitim almanız gerekecek ama hedefimiz şu:

![Bezier primary Surface Volume 66-07](https://github.com/edwardvmills/NURBSlib_EVM/raw/master/development_FC_models/parametric/FreeCAD%200.17.9528/Bezier%20primary%20Surface%20Volume%2066-07.bmp.png?raw=true)

Yukarıdaki resimde ilgi çeken unsur, ön üst köşedeki üç ana yüzeyin oldukça düzgün bir şekilde harmanlanmasıdır. Üst ve dar ön yüzey arasında büyük bir 'harmanlama yarıçapı' ve geniş yan yüzey ile ilk ikisi arasında keskin bir 'harmanlama yarıçapı' vardır. Bu yarıçaplar parametrik olarak kontrol edilir ve dikişler %95 eğrilik sürekliliğine sahiptir. Bilinen bazı kusurlar da var, ancak şimdilik olumlu yönlere odaklanalım!

Silk Çalışma Tezgahını Yüklediğinizi varsayarak açıklamaları ekliyorum.

>  Silk ÇalışmaTezgahı (WorkBench), `Araçlar -> Eklenti Yöneticisi (Tools -> Addon Manager)` menü yolu kullanılarak ulaşılan, [FreeCAD Eklenti Yöneticisi (Addon Manager)](https://wiki.freecadweb.org/AddonManager) aracılığıyla kolayca kurulabilir.

## Kullanım

### -1-

FreeCAD'de yeni bir belge açın. **Sketcher** çalışma tezgahında, sırayla uç uca bağlanmış **<u>3 çizgi içeren bir çizim</u>** yapın (çizilen ikinci çizgi birinciye ve üçüncü de ikinciye bağlanmalıdır. **Sketcher Polyline** aracını kullanmak bunun her zaman böyle olmasını sağlayacaktır). <u>Eskizde başka hiçbir şey olmamalıdır</u> (şimdilik). Çizim (Eskiz), Parça Tasarım tezgahında (Part Design WB) <u>*değil*</u>, Eskiz tezgahında (Sketcher WB) <u>*olmalıdır*</u>.

![_01 A sketch of three lines connected end to end](https://github.com/edwardvmills/NURBSlib_EVM/raw/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_01%20A%20sketch%20of%20three%20lines%20connected%20end%20to%20end.png?raw=true)

### -2-

3 çizgili taslağı seçin ve **ControlPoly4** makrosuna tıklayın (komutu çalıştırın).  ![02](https://github.com/edwardvmills/NURBSlib_EVM/raw/master/icons/ControlPoly4.png?raw=true)

Bu komutu çalıştığında, belgede bir **ControlPoly4_3L** nesnesi oluşturur. '**3L**' son ekine dikkat edin. Bu, **ControlPoly4** nesne kategorisinin birkaç farklı çeşidinden biridir.

![_03 ControlPoly4_3L object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_03%20ControlPoly4_3L%20object.png)

Üç çizgili eskiz (sketch), oluşan **ControlPoly4_3L** nesnesinin üzerinde olduğu için ControlPoly4_3L nesnesini gizler. İsterseniz ControlPoly4_3L nesnesini doğrudan görmek için eskizi (sketch'i) gizleyin.

**ControlPoly4_3L** nesnesi seçildiğinde, **Veri (Data)** Sekmesinde iki parametre görebilirsiniz:

* **Sketch** (Eskiz) - Bu girdi nesnesi seçimidir ve başka bir taslakla yeniden eşleştirilebilir (ayrıca uçtan uca tam olarak üç satırdan oluşur)

* **Weights** (Ağırlıklar) - Bu konu hakkında birazdan tekrar konuşacağız

Henüz sonuç çok ilginç değil, bu yüzden bir sonraki adıma geçelim!

### -3-

**ControlPoly_3L** nesnesini seçin ve **CubicCurve4** makrosuna tıklayın (komutu çalıştırın). ![CubicCurve4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/CubicCurve4.png)

Bu makro / komut, belgede bir **CubicCurve4** nesnesi oluşturur.

![_05 CubicCurve4 object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_05%20CubicCurve4%20object.png)

**CubicCurve4** nesnesi seçildiğinde, **Veri (Data)** Sekmesinde tek bir parametre görebilirsiniz:

* **Poly = ControlPoly4_3L** . Bu girdi nesnesi seçimini temsil eder ve herhangi bir **ControlPoly4** nesnesine yeniden eşlenebilir / değiştirilebilir. (şu anda 3 çeşidi vardır)

Neden eğri doğrudan eskizle eşlenmiyor? Ağırlıklar sadece eğri nesnesinin bir özelliği olabilir, değil mi? Aslında bu şekilde ayarlamıştım, ancak Kontrol Poligonlarını (*Control Polygons*) NURBS nesnelerinden mümkün olduğunca ayırmayı seçtim.
İşte nedeni:

* Bazen bir poligona ihtiyaç duyarız, ancak NURBS eğrisini hesaplamak gibi bir amacımız yoktur.

* NURBS'ün birçok özelliği doğrudan poligondan belirlenebilir. Bunlar başka poligonlar oluşturmak için kullanılabilir.

* İhtiyacımız olmayan eğrileri ve yüzeyleri hesaplamak, FreeCAD aşırı yüklenmeden ve çökmeden önce ne kadar inşa edebileceğimizi sınırlar.

* Nesneleri birbirinin içine yerleştirmeyi öğrenmek için uzun zaman harcayabilirim, ancak FreeCAD bu haliyle tamamen tutarlı değil ve en iyi yerleştirme stratejisinin ne olduğunu henüz bildiğimden bile emin değilim (birkaç rakip yöntemin farkındayım).

* Bu arada, tüm nesnelere isim verme ve onları klasörlerde istediğim gibi düzenleme konusunda tam bir özgürlüğe sahibim. FreeCAD'in model ağacında (unsur ağacında) bir şeyleri hareket ettirmesi gerçekten can sıkıcı (örneğin bir yüzeyi yansıtırken)

### -4-

Sketcher çalışma tezgahı içinde çizdiğiniz Orijinal eskizi (çizimi) düzenleyin. Bir çizgiyi 'sürükleyin', 'açısını ya da uzunluğunu değiştirin'...vb. işlemler yapıp eskizden çıkın. Eskiz kullanılarak oluşturulan poligon (ControlPoly4_3L) ve eğrinin (CubicCurve_4), güncellendiğini göreceksiniz.

### -5-

Artık **ControlPoly4**'e bağlı bir **CubicCurve4**'ümüz olduğuna göre, **ControlPoly4** nesnesine geri dönelim ve **ağırlık kontrollerini (weight controls)** inceleyelim.

Poligonun veri sekmesinde, **ağırlıklar (weight)** varsayılan değerleri [1,1,1,1] olan bir liste olarak görüntülenir. Listenin sağ tarafındaki **...** düğmesine basıldığında çok basit bir liste düzenleyici penceresi açılır.

![_06 the weight list of all ControlPoly4 objects](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_06%20the%20weight%20list%20of%20all%20ControlPoly4%20objects.png)

### -6-

Bu pencerede ağırlıklardan birini değiştirin. Düzenleyici penceresini kapatmak için **Tamam (Ok)** düğmesine basın.

![_07 editing a specific weight of the ControlPoly4 object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_07%20editing%20a%20specific%20weight%20of%20the%20ControlPoly4%20object.png)

### -7-

Modeli yeniden hesaplamak için "CTRL+R"** tuşuna basın. Resimde gösterilen durumda, ikinci kutup için ağırlıkları 1.0'dan 4.0'a yükseltmek eğrinin ikinci kutba doğru çizilmesine neden olur.

![_08 the CubicCurve4 object updates to the modified ControlPoly4 weight](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_08%20the%20CubicCurve4%20object%20updates%20to%20the%20modified%20ControlPoly4%20weight.png)

Ağırlıklar modeli doğrudan etkilemek için kullanılabilir, ancak temel bir modelleme stratejisi olarak önerilmez. Ağırlıkların birincil işlevi, dairelerin (ve elipslerin ve diğer koniklerin) yaylarının tam olarak dönüştürülmesine izin vermektir. Bu otomatik olarak yapılır ve genellikle karıştırılmamalıdır. Mekanizma burada python nesne modelini sunmak için açığa çıkarılmıştır.

### -8-

XY düzleminde yeni bir eskiz (çizim) başlatın. **1 daire** ve **1 çizgi** çizin. <u>Çizginin tam olarak daire merkezinde bir noktası (bitiş noktası veya başlangıç noktası) olmalıdır</u>. Çizime başka bir şey eklemeyin. İlk çizimle çakışmayacak şekilde yerleştirin. Tuhaf açılar iyidir, çünkü daha sonra bize daha fazlasını göstereceklerdir. Çizim (Eskiz), Parça Tasarım tezgahında (Part Design WB) <u><em>değil</em></u>, Eskiz tezgahında (Sketcher WB) <u><em>olmalıdır</em></u>.

![_09 a single Node sketch on xy](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_09%20a%20single%20Node%20sketch%20on%20xy.png)

Bu tür taslaklara ***Düğüm* eskizi (*Node* sketch)** denir.

### -9-

YZ düzleminde yeni bir eskiz (çizim) başlatın. Başka bir **düğüm eskizi** çizin. Diğer çizimlerle çakışmayacak şekilde yerleştirin. Tuhaf açılar iyidir, çünkü daha sonra bize daha fazlasını göstereceklerdir. Çizim (Eskiz), Parça Tasarım tezgahında (Part Design WB) <u><em>değil</em></u>, Eskiz tezgahında (Sketcher WB) <u><em>olmalıdır</em></u>.

![_10 a single Node sketch on yz](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_10%20a%20single%20Node%20sketch%20on%20yz.png)

### -10-

Her iki **Düğüm (Node) eskizi** seçin ve **ControlPoly4** makrosuna tıklayın (komutu çalıştırın). ![ControlPoly4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4.png)

![_11 run ControlPoly4 macro on two Node sketches](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_11%20run%20ControlPoly4%20macro%20on%20two%20Node%20sketches.png)

Bu komut (makro), belgede bir **ControlPoly4_2N** nesnesi oluşturur. '**2N**' son ekine dikkat edin. Bu, **ControlPoly4** nesne kategorisinin ikinci çeşididir.

![_12 ControlPoly4_2N object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_12%20ControlPoly4_2N%20object.png)

**Veri (Data)** Sekmesinde, bu nesneye ait <u>üç parametre</u> görebilirsiniz:

* **Sketch0** - bu ilk girdi nesnesinin seçimiydi ve başka bir sketch'e yeniden eşlenebilir (ayrıca bir düğüm sketch'i olmalıdır).

* **Sketch1** - bu ikinci girdi nesnesinin seçimiydi ve başka bir sketch'e yeniden eşlenebilir (ayrıca bir düğüm sketch'i olmalıdır).

* **Weights** (Ağırlıklar) - ControlPoly_3L'deki ile tamamen aynı.

Bu aşamada, unsur (model) ağacında farklı nesneleri seçerek gizlemek/göstermek için bir dakikanızı ayırın. Modeli ters çevirin ve inceleyin. <u>İki düğümün ayrı düzlemlerde olduğuna ve ControlPoly4_2N'nin düzlemsel olmayan bir çokgen oluşturmak için bunları birleştirdiğine dikkat edin.</u>

### -11-

ControlPoly_2N nesnesini seçin ve **CubicCurve4** makrosuna tıklayın (komutu çalıştırın). ![CubicCurve4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/CubicCurve4.png)

![_14 non planar CubicCurve4 object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_14%20non%20planar%20CubicCurve4%20object.png)

Bu komut (makro), belgede bir **CubicCurve4** nesnesi daha oluşturur. **Veri (Data)** Sekmesinde, bu nesneye ait <u>tek bir parametre</u> görebilirsiniz:

* **Poly = ControlPoly4_2N**. Bu girdi nesnesi seçimidir ve herhangi bir **ControlPoly4** nesnesine yeniden eşlenebilir (şu anda 3 çeşidi vardır)

Şimdi Düğüm eskizlerinin (Node sketches) ve bileşenlerinin oynadığı farklı rolleri görebiliriz. **ControlPoly4_2N**'ye geri dönelim:

* **Sketch0**'a aktarılan Düğüm, eğrinin başlangıcını kontrol eder.

* **Sketch1**'e aktarılan Düğüm, eğrinin sonunu kontrol eder.

* Her düğümdeki **dairenin merkezi** eğrinin **başlangıç** (/ **bitiş**) noktasını belirler.

* **Çizgi**, eğrinin başlangıç(/son) **teğetini** kontrol eder.

### -12- (isteğe bağlı)

**Weights (Ağırlık)** kontrollerinin çalıştığını doğrulamak için **ControlPoly4_2N** ile 5, 6 ve 7. adımları tekrarlayın. Düğüm çizimlerini düzenleyin ve eğrilerin güncellenmesini izleyin.

![_15 non planar ControlPoly4 weight edit](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_15%20non%20planar%20ControlPoly4%20weight%20edit.png)

### -13-

ZX düzleminde yeni bir eskiz (çizim) başlatın. Bir daire yayı çizin, 90 derecenin altında ALTTAN KAVİSLİ bir eğri olsun (aşağıdaki şekil gibi). Genellikle 180 dereceye kadar sorun olmaz, ancak 90 derece kaya gibi sağlamdır. Ben modelleri çok dengeli yapmayı seviyorum, bu yüzden yaylarımı gerektiği gibi bölüyorum. Bu taslağa başka ne isterseniz koyabilirsiniz, ancak önce yay çizilmelidir. Çizim (Eskiz), Parça Tasarım tezgahında (Part Design WB) <u><em>değil</em></u>, Eskiz tezgahında (Sketcher WB) <u><em>olmalıdır</em></u>.

![_16 a sketch of an arc of circle SUBTENDING 90 degrees](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_16%20a%20sketch%20of%20an%20arc%20of%20circle%20SUBTENDING%2090%20degrees.png)

### -14-

Yay içeren eskizi seçin ve **ControlPoly4** makrosuna tıklayın (komutunu çalıştırın)  ![ControlPoly4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4.png)

Bu komut, belgede bir **ControlPoly4_Arc** nesnesi oluşturur. '**Arc**' son ekine dikkat edin. Bu, **ControlPoly4** nesne kategorisinin üçüncü çeşididir.

![_18 ControlPoly4_Arc object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_18%20ControlPoly4_Arc%20object.png)

**Veri (Data)** Sekmesinde, bu nesneye <u>iki parametre</u> görebilirsiniz:

* **Sketch (Eskiz)** - Bu girdi nesnesi seçimidir ve başka bir eskizle (yay da olabilir) yeniden eşleştirilebilir.
* **Weights (Ağırlıklar)** = [1,0.8356,0.8356,1]

Bu sefer ağırlıkların varsayılan [1,1,1,1] olmadığına dikkat edin. Otomatik olarak oluşturulan değerler gerçek bir dairesel yay verecektir.

### -15-

**ControlPoly4_Arc** nesnesini seçin ve **CubicCurve4** makrosuna tıklayın (komutunu çalıştırın). ![cc](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/CubicCurve4.png)

![_20 CubicCurve4 exact arc object](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_20%20CubicCurve4%20exact%20arc%20object.png)

Bu komut, belgede bir **CubicCurve4** nesnesi daha oluşturur. ****Veri (Data)** Sekmesinde, bu nesneye ait <u>tek bir parametre</u> görebilirsiniz:

* **Poly = ControlPoly4_Arc**. Bu girdi nesnesi seçimidir ve herhangi bir ControlPoly4 nesnesine yeniden eşlenebilir (şu anda 3 çeşidi vardır)

Aynı yay ile sonuçlanacaksa 14. ve 15. adımların ne anlamı var?

* *Sketcher yayları* kuadratik NURBS'dir.
* *Yayın CubicCurve4 versiyonu* bir kübik NURBS'dir.
* *Kübik NURBS*, genellikle serbest form modelleme için uygun olduğu düşünülen en basit formdur.
* *Sketcher yayımız* *ControlPoly4_arc* veya *CubicCurve4* formuna girdikten sonra, artık yüzeyler oluşturmak için diğer eğrilerle birlikte kullanılabilir.
* (Yüzey oluşturmak için) Genellikle sadece çokgene ihtiyacımız vardır, bu nedenle yayı çizer, çokgeni yapar ve eğri yapmayı atlarız. Dönüşümü elde etmek için çok az ekstra çaba gerekir.

İşte bir sketcher yay ekstrüzyonunu dikişte tam eşleştirme ile serbest biçimli bir yüzeye karıştırmanın örnek bir resmi. Bu eğitim için KAPSAM DIŞI, sadece somut bir örnek göstermek istiyorum.

![live 66 02](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/development_FC_models/parametric/FreeCAD%200.16/blend%20arc%20to%2066%20demo/live%2066%2002.PNG)

### -16- BONUS

Herhangi bir tek eskiz için **ControlPoly4** makrosu (komutu), tam olarak 3 eskiz nesnesi (3L modu) yoksa Yay modunu kullanır. Bu her zaman eskizdeki ilk geometri nesnesi için geçerlidir. Net etki şudur ;

* eliptik yaylar tam olarak dönüştürülür.
* bir çizgi otomatik olarak üçe bölünür (bu, üç çizgi çizmek için çok tembel olduğunuzda kullanışlıdır, ancak kötü bir alışkanlıktır)
* parabol ve hiperbol henüz çalışmıyor, ancak bu sadece başlangıç noktası ve bitiş noktasını açığa çıkarma meselesi. Şu anda bu konuda endişelenmiyorum

![_21 freebie elliptic arc and line come for free](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_21%20freebie%20elliptic%20arc%20and%20line%20come%20for%20free.png)

| Önceki Sayfa 			| Sonraki Sayfa              |
| -------------------------- 	| -------------------------- |
| [<< Silk WB Giriş](freecad-silk-wb-00-giris.html)| [Öğretici Doküman 2.1 >>](freecad-silk-wb-ogretici-dokuman-21.html) |

### Kaynak:

[Edwardvmills / NURBSlib_EVM / Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)
