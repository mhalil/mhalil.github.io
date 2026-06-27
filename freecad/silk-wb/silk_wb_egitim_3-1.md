Title: FreeCAD - Silk WB - Öğretici Doküman 3.1
Date: 2024-03-09 13:35
Modified: 2024-03-09 15:30
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 3.1 (Tutorial 0.03 - P1)

## İki kübik Bezier eğrisinin köşesini harmanlama - 0.17.10980 üzerinde test edildi

## Point_onCurve, ControlPoly4_segment, ControlPoly6 ve CubicCurve6 makroları / komutları

Burada eğrilerle çalışmak için gösterilen yöntemler, yüzeylerle çalışmak için kullanılan yöntemlerle neredeyse aynıdır.

`Point_onCurve` ve `ControlPoly4_segment` ifadeleri sırasıyla bir eğri boyunca noktaları ve bir eğrinin bölümlerini (bu noktalarda) tanımlar.

`ControlPoly6` ve `CubicCurve6` ifadeleri sırasıyla 6 kontrol noktalı bir kübik NURBS eğrisini kontrol eder ve kullanır.

## Motivasyon

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 00](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2000.png)

Düz bir çizgi, bir karıştırma eğrisi kullanılarak, sabit eğriliğe sahip gerçek bir yaya  dönüştürülür. Eğrilik süreklidir (bu henüz üst sınıf yüzey kaplama değildir, ancak yol boyunca önemli bir adımdır).

Bir Bezier eğrisinin uçlarındaki eğriliği eşleştirmek çok zordur. Bazı durumlarda mümkündür, ancak sonuç genellikle tasarım açısından tatmin edici değildir (eğrilik eşleşir, ancak eğriler eskisi gibi görünmez). Amacım Bezier ile geniş konturlar tasarlamak olduğu için, Bezier eğri/yüzey çiftlerini temiz bir şekilde birleştirmek için özel bir eğriye/yüzeye ihtiyacım var.

`ControlPoly6` ve `CubicCurve6` burada devreye girer. Bu nesneler kendi başlarına modelleme yapmak için kullanılabilir, ancak Bezier nesnelerini harmanlama görevi için özel olarak oluşturulmuştur.

Dereceyi hala kübik olarak sınırlarken 4 değil 6 kontrol noktası olması, bizi Bezier nesnelerinin ötesine, kütüphanenin ilk tam NURBS'süne götürür. Ek noktalar, eğrinin her bir ucundaki eğriliği bağımsız olarak ayarlamamıza olanak tanır. Bu, yukarıdaki resimde gösterilmektedir. Keskin bir köşede buluşan iki Bezier eğrisi verildiğinde, keyfi  hareket noktaları (kırmızı noktalar) tanımlayabilir ve iki eğriyi hareket noktaları ve köşeler arasında harmanlayabiliriz.

NURBS'nin kübik olarak sınırlandırılması, mozaikleme işleminin ve diğer tüm dahili NURBS işlevlerinin verimli olmasını sağlar. Yukarıdaki karışımın `ControlPoly6`'sı kutunun dışında gösterilmiştir. Eğrilik sürekliliği (G2) sağlar ve varsayılan ayarlar kaba taslaklar için uygundur. Dikkatli bir ayarlama ile bizi G3'e veya çok yakınına götürebilecek manuel olarak ayarlanabilir parametreler vardır. Bu ayarlamalar başlı başına bir konudur ve burada sadece göz atılacaktır.

### Bu özel eğitim için hedef kitle

Bu eğitim, FreeCAD'in bilgili kullanıcılarına Silk Workbench (eski adıyla NURBSlib_EVM kütüphanesi) hakkında bir fikir vermek için hazırlanmıştır. Şu anda temel FreeCAD eylemleri hakkında hiçbir açıklama yapılmamaktadır.

Tembel için bir başlangıç noktası modeli ve bir nihai model ekledim.

### Bu eğitimi takip etmek için gerekenler

* [Öğretici Doküman 1](freecad-silk-wb-ogretici-dokuman-1.html) kesinlikle zorunludur (özellikle kurulum kısmı)

* [Öğretici Doküman 2.1](freecad-silk-wb-ogretici-dokuman-21.html) şiddetle tavsiye edilir ancak teknik olarak gerekli değildir

* [FreeCAD](https://www.freecad.org/) 0.17'de bir makro / eklenti (addon) yöneticisi ile çalışma tezgahı kurma,  yeteneği gereklidir 

* FreeCAD'de çizgi ve yay çizimleri oluşturma becerisi

* FreeCAD'deki üç temel düzlemin anlaşılması

* Inkscape veya Illustrator'da bulunan NURBS veya Bezier eğrileri hakkında en azından belli belirsiz bir fikre sahip olmak çok faydalıdır

### Dosyalar

Öncelikle, [master](https://github.com/edwardvmills/NURBSlib_EVM) adresindeki **Tutorial Models / Point_onCurve ControlPoly4_segment ControlPoly6 ve CubicCurve6** klasöründe bulunan aşağıdaki dosyaları kopyalayın:

* *Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 00 starting point.FCStd*

* *Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 01 finish.FCStd*

### Kullanım

### -1-

**Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 00 starting point.FCStd** dosyasını açın.

Bunu hemen ***Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 in progress.FCStd*** adıyla ya da istediğiniz başka bir isimle kaydetmenizi tavsiye ederim. Bu, orjinal dosyayı korumak içindir.

( Model ağacını net bir şekilde okuyabilmek, simgeleri görebilmek ve nesne bağımlılıklarını anlamak için DAG görünümünü kontrol edebilmek için aşağıdaki grafikleri (ekran görüntülerini) browser'ınızda tam ekran boyutunda açabilirsiniz. )

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 01](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2001.png)

Bu model, başlangıç unsurlarından oluşan bir klasör içerir:

* Düz bir çizginin taslağı

* Bir ucundan düz çizgiye bağlanmış bir yay çizimi

* Düz çizgi taslağına bağlı `ControlPoly4_Arc` nesneleri (her ikisinin de neden "`Arc`" tipini kullandığını merak ediyorsanız [Öğretici Doküman 1](freecad-silk-wb-ogretici-dokuman-1.html)'e bakın. bu sadece basit bir örnek model için hızlı ve kolay bir hiledir)

* Yukarıdaki kontrol çokgenlerine bağlı `CubicCurve_4` nesneleri

* Yukarıdaki `CubicCurve_4` nesnelerine bağlı ekstrüzyon yüzeyleri (bunlar **PartDesign** değil, **Part workbench**'te bulunan' **extrude** komutu kullanılarak yapılmıştır). Bir eğriyi ekstrüde etmek (katılamak), eğrilerin vurgularını görmemizi sağlar. Kötü vurgular, kendi başlarına gayet iyi görünen iki eğrinin bir yüzeyde kullanıldığında çok yapay görünmesine neden olur. Eğer [Öğretici Doküman 2](freecad-silk-wb-ogretici-dokuman-21.html)'de' çalıştıysanız, ızgaralarla uğraşmadan hızlı bir şekilde test yüzeyi oluşturabilmeyi değerlendireceksiniz!

### -2-

Eskizleri gizleyin ve **CubicCurve** nesnelerini gösterin (unsur ağacından seçin ve görünürlüğü değiştirmek için **boşluk** tuşuna basın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 02](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2002.png)

* **CubicCurve_4** **yayının** merkezi (ortası) ile iki eğrinin birleştiği yer arasında bir yere (noktaya) tıklayın (aşağıdaki resme bakın)

* Point_onCurve makrosunu / komutunu çalıştırın ![Point_onCurve](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/Point_OnCurve.png)

![qq](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2003.png)

* Model (unsur) ağacından **Point_onCurve** nesnesini seçin

* Görünüm sekmesine gidin

* Nokta boyutunu 5.0 olarak ayarlayın

* Rengi kırmızı olarak ayarlayın

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 04](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2004.png)

* **Point_onCurve** nesnesi hala seçiliyken, **veri** sekmesine gidin
  referans eğri bağlantısına dikkat edin

* Nesnenin bir **Position** özelliğine sahip olduğuna dikkat edin (diğer nesneler tarafından kullanılır)

* **u** olarak etiketlenen son parametre eğri boyunca parametrik konumdur (0.0 başlangıç noktası, 1.0 bitiş noktasıdır)

* **u**'yu 0,60 olarak değiştirin.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 05](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2005.png)

Nokta, varsayılan olarak fare tıklamasının konumunda oluşturulur. Ortaya çok yakın tıklamaktan kaçınmak iyidir. Eğrinin bir ucuna veya diğer ucuna çok daha yakın tıklandığında, **u** değeri her zaman 0 veya 1'e çok daha yakın olur. Bu, söz konusu eğri için **u**'nun hangi yöne gittiğini ve noktayı eğri boyunca istediğiniz yöne nasıl kaydıracağınızı görmeyi kolaylaştırır.

Şu anda, tıklamak ve manuel olarak ayarlamak parametreleri ayarlamanın tek iki yoludur (sonunda daha birçok yöntem planlanmaktadır. Zor değiller, sadece zaman alıcılar).

### -3-

Aşağıdaki resimlerde gösterildiği gibi eğrilere daha fazla nokta ekleyin (ve bunları da kırmızı renk ve 5.0 boyutunda yapın)

* Yay eğrisi, iki eğrinin köşesine çok yakın. **u** değerini 1.0 olarak ayarlayın, böylece nokta, köşenin üzerinde olur.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 06](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2006.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 07](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2007.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 08](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2008.png)

Sonraki birkaç resmi takip edin: önce tüm noktaları oluşturun, ardından boyut ve rengi değiştirmek için hepsini bir kerede seçin, ardından **"u"** değerlerini ayarlayın (ayrıntılar yol boyunca tekrarlanacaktır, bu özet, ne yaptığımıza dair genel bir bakış sağlamak içindir)

* Yay eğrisi, en sol uca çok yakın. **u** değerini **0,0** olarak ayarlayın, böylece uzak kenarda olur
* Çizgi eğrisi üzerine eklenen nokta, köşeye doğru olsun ancak çok yakın olmasın. **u** değerini **0,22**'ye ayarlayın
* Çizgi eğrisi üzerine eklenen diğer nokta, sağ uca doğru olsun. **u** değerini **0,7**'ye ayarlayın

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 09](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2009.png)

Bu Eğitim birkaç sayfaya (Öğretici Dokümana) bölünmüştür, bu nedenle sayfa başına en fazla 10 tam boyutlu ekran görüntüsü vardır.

| Önceki Sayfa                                                         | Sonraki Sayfa                                                       |
| -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [<< Öğretici Doküman 2.6 ](freecad-silk-wb-ogretici-dokuman-26.html) | [Öğretici Doküman 3.2 >>](freecad-silk-wb-ogretici-dokuman-32.html) |

### Kaynak:

* [Tutorial 0.03 Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 - page 01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2001.md)
