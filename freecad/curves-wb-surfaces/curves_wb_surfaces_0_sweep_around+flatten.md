Title: FreeCAD - Curves WB - Surface - 0 - 
Date: 2022-11-05 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface
Author: Mustafa Halil

![zebra](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/zebra.svg) **ZebraTool:**  
**ZebraTool** komutu, yüzeylerin birleşim yerlerindeki sürekliliği ve yüzeyler arası geçiş yumuşaklığını incelememize yardımcı olmak için, yüzey üzerinde değişen siyah ve beyaz 
şeritlerden müteşekkil **Zebra dokusu** görüntüler.  
Zebra çizgileri, standart bir ekranda görülmesi zor olabilecek bir yüzeydeki küçük değişiklikleri görmenizi sağlar. **ZebraTool** komutu, uzun ışık şeritlerinin çok parlak bir yüzey üzerindeki yansımasını simüle eder. ZebraTool sayesinde bir yüzeydeki bozuklukları veya kusurları kolayca görebiliriz.  
**ZebraTool**, modellerimizin kalitesini, hızlı ve ayrıntılı bir şekilde görmek için kullanılabilecek güçlü bir araçtır. Yüksek kaliteli, iyi görünen bir yüzeye sahip olmak istiyorsak, ZebraTool aracını kullanmak faydalı olacaktır.

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **ZebraTool** seçeneğini kullanın.
- ZebraTool parametrelerini ihtiyacınıza göre değiştirin.

**Parametreler:**  
**Black Stripes Width:** Siyah şerit genişliğini değiştirir.  
**Scale:** Zebra çizgilerini ölçeklendirir.  
**Rotation:** Zebra çizgilerini döndürür.  

**ZebraTool** komutunu incelemek için **Sketcher (Eskizci)** çalışma tezgahındaki **Bezier eğrisi** komutu yardımıyla, bir biri ile bağlantılı 3 adet eğri oluşturuyorum.
![ZebraTool_01](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_01.png)  
Oluşturduğum eğrileri, **Part (Parça)** çalışma tezgahındaki **Extrude (Katıla)** komutu ile, katılıyorum/ekstrude ediyorum.
![ZebraTool_02](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_02.png)  
Komutu çalıştırmak için Curves araç çubuğunda bulunan ZebraTool düğmesine basabilir, ya da Surface menüsündeki **ZebraTool** seçeneğini kullanabilirsiniz.  
**Not:**  
*ZebraTool komutundan çıkmak için **`Quit (Çık)`** düğmesine tıklayın.*  
![ZebraTool_03](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_03.png)  
Yüzeylerin birleşim noktalarındaki kusurları, sürekliliği veya yüzeyler arası geçiş yumuşaklığını inceleyebilmek için **Scale** ve **Rotation** Parametrelerini değiştirerek, zebra çizgilerinin **Ölçeğini** ve **Yönünü** değiştiriyorum.
![ZebraTool_04](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_04.png)  
Modeli iki yönden de inceliyorum ve birleşim noktalarının sorunlu olduğunu görüyorum.
![ZebraTool_05](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_05.png)  
Yüzeylerin birbirini teğete yakın şekilde takip etmesi için, oluşturduğum eskizi (sketch'i) düzenliyorum.
![ZebraTool_06](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_06.png)  
Bezier eğrilerin uç (birleşim) noktalarındaki eğriselliğin neredeyse eşit olduğunu görebiliyoruz.
![ZebraTool_07](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_07.png)  
Yüzeylerin birbirini teğete yakın şekilde takip etmesi amacıyla düzenlediğim eskizin (sketch'in) son hali aşağıdadır.
![ZebraTool_08](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_08.png)  
Yüzeylerin birleşim noktalarındaki sürekliliği ve yüzeyler arası geçiş yumuşaklığını inceleyebilmek için **ZebraTool** komutunu tekrar çalıştırıyor, **Scale** ve **Rotation** parametrelerini, bakış açıma uygun olacak şekilde değiştiriyorum.
 !ZebraTool_09[](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_09.png)  
Modeli daha yakından inceleyelim.
![ZebraTool_10](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_10.png)  
Bir de modelin diğer tarafına bakalım.
![ZebraTool_11](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_11.png)  
Yakından incelediğimizde, yüzey sürekliliği gayet güzel ve temiz görünüyor.
![ZebraTool_12](../../images/freecad/curves_wb/surfaces_menu/ZebraTool_12.png)  

![trimFace](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/trimFace.svg) **Trim face:**  
**Trim face** komutu, kesişme eğrisi oluşturmadan yüzleri kırpmanıza olanak tanır. Bu, yüzeyleri eğrilerle kırpan veya ayıran komuttur.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle eğri(ler)i / kenar(lar)ı ve ardından yüzey(ler)i seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Trim face** seçeneğini kullanın.

Aşağıdaki şekilde göreceğiniz gibi elimizde eğrisel bir yüzey ve bir elips var.  
![TrimFace_01](../../images/freecad/curves_wb/surfaces_menu/TrimFace_01.png)  
Evvela **Üst görünüşe** geçerek önce eğriyi ardından yüzeyi seçiyoruz. Yüzeyi seçerken **eğrinin dış ya da iç kısmında** kalan bir yerin seçilmesinin önemli olduğu bilinmelidir. Aşağıdaki örnekte, Eğri seçildikten sonra, eğrinin **dış kısmında kalan** bir yere tıklanarak seçimin yapıldı ve ardından **Trim face** komutu çalıştırılmıştır.
![TrimFace_02](../../images/freecad/curves_wb/surfaces_menu/TrimFace_02.png)  
İşlem sonucu karşımızda. Yüzey seçimi yaparken, Eğrinin dışında kalan bir yere tıkladığımız için **bu bölümün kalmasını istiyorum, geri kalan kısmı sil, at** demiş oluyoruz.
![TrimFace_03](../../images/freecad/curves_wb/surfaces_menu/TrimFace_03.png)  
Modelin İzometrik görünümü bu şekildedir.
![TrimFace_04](../../images/freecad/curves_wb/surfaces_menu/TrimFace_04.png)  
Önce eğriyi ardından **eğrinin iç kısmında** kalan bir yeri seçerek yüzey seçimi yaptıktan sonra **Üst görünüşe** geçerek **Trim face** komutu çalıştırıp sonucu görelim.
![TrimFace_05](../../images/freecad/curves_wb/surfaces_menu/TrimFace_05.png)  
İşlem sonucu elde ettiğimiz model bu şekilde:
![TrimFace_06](../../images/freecad/curves_wb/surfaces_menu/TrimFace_06.png)  
Oluşan yüzeye **Parça Çalışma Tezhagı (Part WB)** içerisindeki **3D Offset..** komutu ile et kalınlığı verip kenarlarını da **Fillet** komutu ile yuvarlatırsak ne elde etmiş oluruz acaba? :)
![TrimFace_06.2](../../images/freecad/curves_wb/surfaces_menu/TrimFace_06.2.png)  
Dikkat ettiyseniz, yukarıdaki anlatımlarda **Trim face** komutunu çalıştırmadan önce, sürekli **Üst görünüşe geçilmesi** ifade edildi. Bunun sebebi, **Trim face** komutunun, sahneye bakış açısı doğrultusunda çıkarma/silme işlemi yapmasıdır. Aşağıdaki örnekte, sahneye izometrik bakış açısı ile bakıldığı esnada önce eğri ardından **eğrinin iç kısmındaki yüzey** seçilerek "Trim face" komutunu uygulanmaktadır.
![TrimFace_07](../../images/freecad/curves_wb/surfaces_menu/TrimFace_07.png)  
Sonuç, beklediğimiz gibi.
![TrimFace_08](../../images/freecad/curves_wb/surfaces_menu/TrimFace_08.png)  
Sonuca daha yakından bakacak olursak;
![TrimFace_09](../../images/freecad/curves_wb/surfaces_menu/TrimFace_09.png)  
Bu kez de sahneye farklı bir bakış açısı ile bakarak, eğrinin dışında kalan yüzey kısmını seçerek **Trim face** komutunu çalıştıralım.
![TrimFace_10](../../images/freecad/curves_wb/surfaces_menu/TrimFace_10.png)  
Yüzeyin, seçilen (eğrinin dışında kalan) kısmı kaldı, seçilmeyen (eğrinin iç kısmı) silinip atıldı.
![TrimFace_11](../../images/freecad/curves_wb/surfaces_menu/TrimFace_11.png)  
Modelin izometrik görünümü:
![TrimFace_12](../../images/freecad/curves_wb/surfaces_menu/TrimFace_12.png)  
`Trim face` komutunu kullanmak için çember, elips, dikdörtgen,..vb kapalı eğri kullanmak zorunda değiliz. Aşağıdaki resme bakın.
![TrimFace_13](../../images/freecad/curves_wb/surfaces_menu/TrimFace_13.png)  
Üst görünüşten bakarak önce eğri parçalarını ardından yüzeyi seçiyorum.
![TrimFace_14](../../images/freecad/curves_wb/surfaces_menu/TrimFace_14.png)  
Yüzey seçimi yaparken, eğrinin alt kısmına tıklıyorum.
![TrimFace_15](../../images/freecad/curves_wb/surfaces_menu/TrimFace_15.png)  
**Trim face** komutu çalıştırıldığında, seçili yüzey tarafı (eğrinin alt kısmı) kalıyor, eğrinin üst kısmı kesilip atılıyor.
![TrimFace_16](../../images/freecad/curves_wb/surfaces_menu/TrimFace_16.png)  
İşlem sonrası izometrik görünüş;
![TrimFace_17](../../images/freecad/curves_wb/surfaces_menu/TrimFace_17.png)  
Bu kez, üst görünüşten bakarak önce eğri parçalarını ardından eğrinin üst kısmındaki yüzeyi seçerek komutu çalıştırıyorum.
![TrimFace_18](../../images/freecad/curves_wb/surfaces_menu/TrimFace_18.png)  
Beklediğimiz gibi, eğrinin alt kısmındaki yüzey parçası siliniyor.
![TrimFace_19](../../images/freecad/curves_wb/surfaces_menu/TrimFace_19.png)  
İzometrik görünüş;
![TrimFace_20](../../images/freecad/curves_wb/surfaces_menu/TrimFace_20.png)  
Eğer bir kaç yüzey parçasının uc uca eklenmesi ile elde edilmiş yüzey yapısı varsa, bu komut nasıl çalışır, bu konuyu inceleyelim.
![TrimFace_21](../../images/freecad/curves_wb/surfaces_menu/TrimFace_21.png)  
Eğri parçalarının ardından, en sağdaki yüzeyin üst kısmını seçiyorum. Yüzey rengine bakarak hangi yüzeylerin seçili olduğunu anlayabilirsiniz.
![TrimFace_22](../../images/freecad/curves_wb/surfaces_menu/TrimFace_22.png)  
Gördüğünüz gibi "Trim face" komutu, sadece seçili yüzeyi etkiledi. Seçilmeyen yüzeylerin tamamı silindi.
![TrimFace_23](../../images/freecad/curves_wb/surfaces_menu/TrimFace_23.png)  
İzometrik görünüş;
![TrimFace_24](../../images/freecad/curves_wb/surfaces_menu/TrimFace_24.png)  
Yüzey seçimi yaparken Sağ taraftan başlayarak bağlantılı üç yüzeyi **Ctrl** tuşu yardımıyla seçiyorum.
![TrimFace_25](../../images/freecad/curves_wb/surfaces_menu/TrimFace_25.png)  
Görülüyor ki, sadece seçili 3 yüzey üzerinde kesme işlemi uygulanmış.
![TrimFace_26](../../images/freecad/curves_wb/surfaces_menu/TrimFace_26.png)  
Seçilmeyen tüm yüzeyler silinmiş.
![TrimFace_27](../../images/freecad/curves_wb/surfaces_menu/TrimFace_27.png)  
Şimdi tüm yüzeyleri seçerek komutu çalıştıralım.
![TrimFace_28](../../images/freecad/curves_wb/surfaces_menu/TrimFace_28.png)  
Sonuç beklediğimiz gibi, tüm yüzeyler üzerinde kesim işlemi gerçekleşmiş.
![TrimFace_29](../../images/freecad/curves_wb/surfaces_menu/TrimFace_29.png)  
İzometrik görünüş (Sol - Üst)
![TrimFace_30](../../images/freecad/curves_wb/surfaces_menu/TrimFace_30.png)  
İzometrik görünüş (Sağ - Üst)
![TrimFace_31](../../images/freecad/curves_wb/surfaces_menu/TrimFace_31.png)  

![isocurve](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/isocurve.svg) **IsoCurve:**  
**IsoCurve** komutu, seçilen bir yüzeye UV yönelimli bir kafes yapısı uygular. Yani seçili yüzeyin, Yatay ve Düşey doğrultularında, yüzeyi kaplayacak şekilde, belirlenen sayıda eğriden oluşan wireframe denilen kafes yapısına oluşturur. Oluşan eğriler yüzeye
 temas eder.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir veya birkaç yüzey seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **IsoCurve** seçeneğini kullanın.

Daha önce Modellemiş olduğum Burgu Vazo çalışmasını açıyorum. Herhangi bir yüzey seçili olmadığı için, **IsoCurve** butonu pasif vaziyette.  
![IsoCurve_1](../../images/freecad/curves_wb/surfaces_menu/IsoCurve_1.png)  
Bir yüzey seçtim ve butonu aktif hale geldi.
![IsoCurve_2](../../images/freecad/curves_wb/surfaces_menu/IsoCurve_2.png)  
Aktifleşen **IsoCurve** butonuna tıklıyorum ve seçili yüzey üzerinde 5 yatay ve 5 düşey eğriden müteşekkil bir kafes yapısı oluşuyor.
![IsoCurve_3](../../images/freecad/curves_wb/surfaces_menu/IsoCurve_3.png)  
Unsur ağacından **IsoCurve** nesnesi seçiliyken, **Özellikler** panelinde **Iso Curve** başlığı altında **Number U** ve **Number V** değerleri değiştirilerek, kafes yapısını oluşturan eğri sayısı artırılıp azaltılabilir.
![IsoCurve_4](../../images/freecad/curves_wb/surfaces_menu/IsoCurve_4.png)  
Burgu Vazo nesnemizi gizleyip **IsoCurve** komutu ile oluşturduğumuz kafes yapısını incelersek, aşağıdaki şekil ile karşılaşırız.
![IsoCurve_5](../../images/freecad/curves_wb/surfaces_menu/IsoCurve_5.png)  

![sketch_surf](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/sketch_surf.svg) **Sketch on Surface:**  
Bu komut sayesinde seçili yüzeyin, sanal UV'si açılır ve bu düzlem yüzeye 2 boyutlu Eskiz (sketch) çizimi yapmamıza imkan verilir. 
Komut sonlandırıldığında, çizilen 2 boyutlu eskiz, yüzey üzerine uygulanır.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir yüzey seçin.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Sketch on Surface** seçeneğini kullanın.

Yüzüğe benzer İçi boş bir silindir modelin dış yüzeyine eskiz (şekiller) çizip, bu eskizi, silindir yüzeyinden çıkarmaya çalışalım.  
**Parça Çalışma Tezgahı (Part WB)** komutlarından olan **Tüp/Boru (Tube)** komutunu çalıştırıp parametrelerimizi belirleyelim.
![SketchOnSurface_01](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_01.png)  
Modelin dış yüzeyini seçip **Surface** menüsündeki **Sketch on surface** komutunu çalıştıralım.
![SketchOnSurface_02](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_02.png)  
Komut sonrasında, Unsur ağacında **Sketch on Surface** ve **Mapped_Sketch** unsurlarının oluştuğunu göreceksiniz.
![SketchOnSurface_03](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_03.png)  
**Mapped_Sketch** unsuruna çif tıklayarak düzenleme moduna girdiğimizde referans çizgilerden oluşan bir dikdörtgen göreceksiniz. Bu dikdörtgen şekil, seçili yüzeyin kumaş gibi açılıp karşınıza sunulduğu UV yapısını temsil eder. Anlaşılması açısından, **U:** eskizin X eksenini, **V:** eskizin Y ekseninin tanımlar diyebiliriz.
![SketchOnSurface_04](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_04.png)  
Referans çizgilerden oluşan bir dikdörtgenin içine istediğiniz şekli çizebilirsiniz. Aşağıdaki şekli çizip çoğaltarak sonucu görmek istiyorum.
![SketchOnSurface_05](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_05.png)  
Çizimin doğrusal 10 kopyasını çıkarıyorum / çoğaltıyorum ve Sol paneldeki **Close** butonu ile eskizden çıkıyorum.
![SketchOnSurface_06](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_06.png)  
Eskizi rahat çizebilmek adına Boru (Tube) modelini gizlemiştim. Şimdi unsur ağacından Tube nesnesini seçip tekrar **Boşluk (Space)** tuşu yardımıyla görünür hale getirelim.
![SketchOnSurface_07](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_07.png)  
Sonuç, beklediğimiz gibi. Çizdiğimiz eskiz, Boru (Tube) modelinin seçili yüzeyine ilişkilendirildi.
![SketchOnSurface_08](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_08.png)  
Şimdi sıra, **Sketch on Surface** komutunun **Ayarlarını (Settings)** incelemeye geldi.
![SketchOnSurface_09](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_09.png)  
**Fill Faces (Yüzeyleri Doldur)** seçeneği, çizilen eskizin kapalı çokgenlerinin iç kısmını doldurarak, yüzeye dönüştürür.
![SketchOnSurface_10](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_10.png)  
**Thickness (Kalınlık)** seçeneği, çizilen eskize, extrude komutuna benzer şekilde kalınlık kazandırır. **Fill Faces (Yüzeyleri Doldur)** seçeneği **true** ya da **false** olabilir. Her iki seçenekte de komut çalışır.
![SketchOnSurface_11](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_11.png)  
**Offset (Ötele)** seçeneği, Çizilen eskizin, seçilen yüzeyden ne kadar ötelenerek eşleştirileceğini belirttiğimiz ayar bölümüdür.
![SketchOnSurface_12](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_12.png)  
Ayarlar bölümündeki değerler her zaman pozitif olmak zorunda değildir. Örneğin **Thickness** değerini Negatif yapalım ve sonucu görelim.
![SketchOnSurface_13](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_13.png)  
Görüldüğü üzere **Thickness** değeri negatif olduğunda, eskiz, ters doğrultuda kalınlık kazandı. Son olarak ta, **Tube** nesnemizden, kalınlık verdiğimiz eskiz nesnemizi çıkaralım. Önce **Tube** sonra **Sketch on surface** nesnemizi seçelim.
![SketchOnSurface_14](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_14.png)  
**Parça Çalışma Tezgahı (Part WB)** komutlarından olan **Kes (Cut)** komutu ile 2. seçili nesneyi, ilk seçili nesneden çıkaralım.
![SketchOnSurface_15](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_15.png)  
Sonuç ortada:
![SketchOnSurface_16](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_16.png)  
Yüzey'e şekil yerine Yazı ekleyip boşluk oluşturmaya çalışalım ve **Sketch on Surface** komutunun **Rötuş/Düzeltme (Touchup)** ayarlarını inceleyelim. Yukarıda anlatılanlara benzer şekilde **Mapped_Sketch** unsuruna çif tıklayarak düzenleme moduna girdiğimizde referans çizgilerden oluşan bir dikdörtgen içerisine yazımıza ekliyoruz.
![SketchOnSurface_17](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_17.png)  
Bezier eğrinin, eğrilik tarakları ve kontrol noktaları kapatıldığında yazımız daha net görünüyor.
![SketchOnSurface_18](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_18.png)  
Düzenleme işlemini tamamlayıp eskizden çıktığımızda, yazımız yüzeye uygulanmış olur.
![SketchOnSurface_19](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_19.png)  
Gizlemiş olduğumuz **Boru/Tüp (Tube)** nesnemizi görüntüleyelim.
![SketchOnSurface_20](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_20.png)  
**Rötuş/Düzeltme (Touchup)** ayarlarını inceleyelim.  
**Reverse U:** Yüzeye çizilen eskizi, U yönünde (bu örnekte X ekseni doğrultusunda yani YZ düzleminde) ters çevirir.  
![SketchOnSurface_21](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_21.png)  
**Reverse V:** Yüzeye çizilen eskizi, V yönünde (bu örnekte Z ekseni doğrultusunda yani XY düzleminde) ters çevirir.  
![SketchOnSurface_22](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_22.png)  
**Swap UV:** U ve V eksenlerinin yerlerini değiştirir, UV yapısını 90 derece çevirir / değiştirir gibi düşünebilirsiniz. Örnekte modellediğimiz **Boru/Tüp (Tube)** nesnemiz kısa olduğu için UV'nin 90 derece çevrilmesi oluşan yapı net olarak anlaşılamıyor. Kendi modellerinizde bu ayarı değiştirerek sonucu görebilirsiniz.
![SketchOnSurface_23](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_23.png)  
Yukarıdaki örnekte olduğu gibi, yüzeye eşleştirdiğimiz yazımıza kalınlık verip boru nesnemizden çıkaralım.
![SketchOnSurface_24](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_24.png)  
![SketchOnSurface_25](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_25.png)  
**Boru/Tüp (Tube)** nesnemizin yarısı keselim.
![SketchOnSurface_26](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_26.png)  
Nesnenin keskin köşeleri hoş görünmüyor, keskin köşelere radyus kazandıralım (yuvarlatalım).
![SketchOnSurface_27](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_27.png)  
Bu şekilde daha hoş görünüyor;
![SketchOnSurface_28](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_28.png)  
![SketchOnSurface_29](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_29.png)  
**Sketch on Surface** komutu ile Eğrisel yüzeylerin UV açılımı yapıldığında, bazen ölçüler beklendiğinden farklı olur. 
Aşağıdaki örneklerle konuyu inceleyelim.
![SketchOnSurface_30](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_30.png)  
Yüzeyi seçip **Sketch on Surface** komutunu çalıştıralım.
![SketchOnSurface_31](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_31.png)  
**Mapped_Sketch** unsuruna çift tıklayarak düzenleme moduna girelim.
![SketchOnSurface_32](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_32.png)  
Gördüğünüz gibi, **U yönü:** 1mm, **V yönü:** 50mm belirlenerek **UV** oluşturulmuş.
![SketchOnSurface_33](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_33.png)  
1mm olan ölçüyü 75mm olarak değiştiriyoruz.
![SketchOnSurface_34](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_34.png)  
Referans çizgiler içerisinde kalacak şekilde bir eskiz çiziyor ve **Close** butonuna basarak eskizi kapatıyoruz.
![SketchOnSurface_35](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_35.png)  
Eskiz, yüzeye eşleştirildi.
![SketchOnSurface_36](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_36.png)  
Eskizi kapalı yüzey olarak ayarlıyor ve kalınlık kazandırarak sonuçları görüyoruz.
![SketchOnSurface_37](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_37.png)  
**Sketch on Surface** nesnesine kalınlık kazandırıp **Offset** nesnesini gizlersek elde edeceğimiz sonuca ait görüntüleri aşağıda görebiliriz;
![SketchOnSurface_38](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_38.png)  
**Offset** nesnesi ile **Sketch on Surface** nesnelerini bir birinden çıkarıyoruz.

![SketchOnSurface_39](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_39.png)  
Sonucu, farklı bir bakış açısından inceliyoruz.
![SketchOnSurface_40](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_40.png)  
**Sketch on Surface** komutunun ayarlarından biri olan **Extra Objects**'i inceleyelim.
![SketchOnSurface_41](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_41.png)  
**Taslak Çalışma Tezgahı (Draft WB)** komutlarından biri olan **Metinden şekil (Shape from text)** ile bir metin oluşturduk. Aşağıdaki görüntüye bakarsanız, Metin ile **Sketch on Surface** düzleminin faklı yönlere baktığı ve Z ekseninde farklı seviyelerde olduğunu göreceksiniz.
![SketchOnSurface_42](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_42.png)  
Yazıyı X ekseninde 90 derece çevrirerek iki doğrultuyu da eşitledik ancak Z ekseninde hala farklı seviyedeler.
![SketchOnSurface_43](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_43.png)  
Metnin (ShapeString) açı ve konum ayarlarını değiştirerek, metni, Mapped_Sketch'in ortasına taşıdık.
![SketchOnSurface_44](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_44.png)  
Çizim, şu an aşağıdaki gibi görünüyor. Unsur ağacından **Sketch on Surface** seçilir ve ayarlar kısmından **Extra Objects** kısmındaki butona basılırsa;
![SketchOnSurface_45](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_45.png)  
Açılan **Bağlantı (Link)** penceresi karşımıza gelir. Bu bölümde Metni (**ShapeString**) seçelim.
![SketchOnSurface_46](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_46.png)  
**Bağlantı (Link)** penceresindeki **OK** butonuna bastığımızda, seçmiş olduğumuz metnin, **Sketch on Surface** yüzeyine uygulandığını göreceksiniz.
![SketchOnSurface_47](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_47.png)  
Orjinal Metni (ShapeString) gizleyelim.
![SketchOnSurface_48](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_48.png)  
**Sketch on Surface**'e kalınlık kazandıralım.
![SketchOnSurface_49](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_49.png)  
Unsur ağacından Orjinal Metni (**ShapeString**) seçip ayarlar kısmından **Metnin içeriğini (string)** ya da **metin boyutunu (Size)** değiştirirsek yazının güncellendiğini görürüz.
![SketchOnSurface_50](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_50.png)  
Eskiz içerisinde Metnimizin konumunu değiştirelim.
![SketchOnSurface_51](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_51.png)  
Sonucun nasıl olduğunu görüyorsunuz. İstersek çalışmaya pozitif yönde kalınlık verir dışa doğru katılarız.
![SketchOnSurface_52](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_52.png)  
İstersek negatif yönde tarafa kalınlık verip, gövdeden çıkarırız.
![SketchOnSurface_53](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_53.png)  
Farklı bir bakış açısından sonucu incelersek;
![SketchOnSurface_54](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_54.png)  
Metni **Kes (Cut)** komutu ile Gövdeden çıkarmış olsak bile bu aşamada orjinal metni değiştirdiğimizde, sonuç otomatik olarak güncellenir.
![SketchOnSurface_55](../../images/freecad/curves_wb/surfaces_menu/SketchOnSurface_55.png)  

![sw2r](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/sw2r.svg) **Sweep2Rails:**  
**Sweep2Rails** komutu, düzlemsel bir yüzeyden, bir dizi eğri (ray) aracılığıyla eğrisel şekilli **nokta bulutu, profil/ray eğrileri** ya da **tel kafes yapısı** oluşturmamızı sağlar. Konunun anlaşılması için aşağıdaki metinleri okuyup resimleri inceleyin lütfen.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir düzlem yüzey ve bir dizi (en az 2) eğri seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Sweep2Rails** seçeneğini kullanın.

Konunun anlaşılması amacıyla, Kürek ucuna benzer bir parça modelleyeceğiz. Öncelikle aşağıdaki resimde gördüğünüz eğrileri çizdim.  
![Sweep2Rails_01](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_01.png)  
Doğrusal bir yüzey oluşturmak için 2 eğriyi seçerek, Parça Çalışma Tezgahındaki (Part WB'teki) **Düzenli Yüzey Oluştur (Create ruled surface)** komutunu çalıştırdım.
![Sweep2Rails_02](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_02.png)  
Düzlem yüzey ile 2 adet ray eğrisini seçerek Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da **Surface** menüsündeki **Sweep2Rails** seçeneğini kullanın.
![Sweep2Rails_03](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_03.png)  
İşlem sonucunda düzlem yüzey kaybolacak ve varsayılan olarak bir **noktalar / nokta bulutu (points)** oluşacaktır.
![Sweep2Rails_04](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_04.png)  
Unsur ağacından **Sweep_2_rails** nesnesi seçilir, **Veri** Sekmesinden **Profile Samples** ve **Rail Samples** değerleri değiştirilerek, oluşan **nokta bulutu (points), profil(profile) / ray(rail) eğrileri** ya da **tel kafes yapısı (wireframe)** ile oynanabilir.
![Sweep2Rails_05](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_05.png)  
Değerleri değiştirip yapıdaki değişimi görelim;  
**Profile Samples**:40  
**Rail Samples**: 20 
![Sweep2Rails_06](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_06.png)  
Unsur ağacından **Sweep_2_rails** nesnesi seçerek **Görünüm** Sekmesindeki **Görünüm Biçimi (Display Mode)** seçeneklerini değiştirerek, **nokta bulutu, profil/ray eğrileri** ya da **tel kafes yapısı** arasında geçiş yapılabilir.  
**Profiller (Profiles):** 
![Sweep2Rails_07](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_07.png)  
**Raylar (Rails):** 
![Sweep2Rails_08](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_08.png)  
**Tel Kafes Yapısı (Wireframe):** 
![Sweep2Rails_09](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_09.png)  
Oluşan nokta bulutu, profil/ray eğrileri ya da tel kafes yapısı, [**Approximate**](https://mhalil.github.io/Freecad_curves_wb_curves.html#approximate) komutu yardımı ile eğrisel yüzeye dönüştürülebilir.
![Sweep2Rails_10](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_10.png)  
Yeni oluşan eğrisel yüzeye, Parça Çalışma Tezgahındaki (Part WB'teki) **3D Offset...** komutu ile et kalınlığı verirsek, aşağıdaki sonucu elde ederiz.
![Sweep2Rails_11](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_11.png)  
**Sweep2Rails** komutu ile, yukarıda oluşturmuş olduğumuz düzlem yüzeyi kullanarak, iki adet eğri yerine bir dizi (örneğin 3 adet) ve farklı yönlerde eğri (ray) kullanarak nokta bulutu ve sonrasında yüzey oluşturalım. Böylece bu komutun gücünü daha net 
görelim.  
Ray (Rail) olarak kullanacağımız 3 adet eğri aşağıda gösterilmektedir.
![Sweep2Rails_12](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_12.png)  
3 eğriyi ve bir yüzeyi `Ctrl` tuşu yardımıyla seçiyoruz.
![Sweep2Rails_13](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_13.png)  
**Sweep2Rails** komutunu çalıştırıyoruz.
![Sweep2Rails_14](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_14.png)  
Oluşan noktaları (points), [**Approximate**](https://mhalil.github.io/Freecad_curves_wb_curves.html#approximate) komutu yardımı ile eğrisel yüzeye dönüştürüyoruz.
![Sweep2Rails_15](../../images/freecad/curves_wb/surfaces_menu/Sweep2Rails_15.png)  
Sonuç sizce de şık olmadı mı?

![profileSupport](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/profileSupport.svg) **Profile support plane:**  
**Profile support plane** komutu, seçili (kenar çizgisi ya da eğriye ait) iki noktadan geçen ve sahneye bakış açısına dik **bir Düzlem** oluşturur.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir eğri veya kenar çizgisi üzerinde birer seçim yapın. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Profile support plane** seçeneğini kullanın.

Bir Eskiz (Sketch) içerisine bir çizgi ve bir bezier eğri çizerek komutun kullanımını inceleyelim.  
![Profile_Support_Plane_01](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_01.png)  
Çizgiden ve bezier eğriden birer yer seçip **Profile support plane** komutunu çalıştıralım.
![Profile_Support_Plane_02](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_02.png)  
Görüldüğü üzere, seçilen yerlerden (noktalardan) geçen ve (sahneye) bakış açımıza dik bir düzlem oluştu.
![Profile_Support_Plane_03](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_03.png)  
Unsur ağacından, ilgili Profili seçip **Veri (Data)** sekmesindeki özelliklere bakarsak, düzlemin oluşmasında **Edge1, Edge2, Parameter1** ve **Parameter2** değerlerinin etkin olduğunu görürüz.
![Profile_Support_Plane_04](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_04.png)  
Oluşan Düzleme izometrik görünümden bakacak olursak aşağıdaki sonucu elde ederiz.  
**Edge1 ve Edge2** değerleri, Düzlemin oluşması esnasında kullanılan Kenar ve Eğrileri temsil eder.
![Profile_Support_Plane_05](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_05.png)  
**Parameter1** değerini değiştirip **10,00** olarak ayarlarsak ne olur, görelim.
![Profile_Support_Plane_06](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_06.png)  
Oluşan düzlemenim yeni halini, izometrik görünümden bakarak tekrar inceleyelim.  
![Profile_Support_Plane_07](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_07.png)  
**Parameter2** değerini değiştirip **1,00** olarak ayarlarsak ne olur, bir de onu görelim. 
![Profile_Support_Plane_08](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_08.png)  
Bir de **Parameter1** değerini **1000,00** olarak ayarlamaya çalışalım.
![Profile_Support_Plane_09](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_09.png)  
Sonuç aşağıdaki gibi, **Parameter1** değerini **1000,00** olarak ayarlamaya çalışmamıza rağmen **ENTER** tuşuna basar bazmaz, değer 50,00 olarak değiştirildi.
![Profile_Support_Plane_10](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_10.png)  
Bunun sebebini öğrenmek için Eskiz (Sketch) içerisine girip çizginin uzunluğuna bakarsak, sol taraftaki çizginin toplam uzunluğunun 50,00 birim olarak belirtilmiş olduğunu görürüz. Yani **Parameter1**'in alabileceği en büyük değer 50,00'dir. 

![Profile_Support_Plane_11](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_11.png)  
**Parameter2**'nin alabileceği değer aralığını inceleyecek olursak, müsaade edilen değerlerin 0,00 ile 1,00 arasında olduğunu görürüz.  
Yani Eğriler yüzdelik olarak ifade ediliyor. Örneğin **Parameter2** değerinin **0 (sıfır)** olarak belirtilmesi, oluşan düzlemin, eğrinin uç kısmından (sıfır noktasından) geçmesi demek oluyor.
![Profile_Support_Plane_12](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_12.png)  
Kenar ve eğrinin uç noktalarından geçen düzlemin İzometrik görünümü.
![Profile_Support_Plane_13](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_13.png)  
Kenar ve eğrinin dört noktasından geçen düzlemler.
![Profile_Support_Plane_14](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_14.png)  
Dört Düzlemim izometrik görünümü;
![Profile_Support_Plane_15](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_15.png)  
**Profile support plane** komutu ile yapılabilecek güzel bir uygulama örneği;  
Düzlemler oluştur, düzlemler üzerine eskizler çiz.
![Profile_Support_Plane_16](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_16.png)  
[Approximate](https://mhalil.github.io/Freecad_curves_wb_curves.html#approximate) komutu ile yüzey oluştur.
![Profile_Support_Plane_17](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_17.png)  
**Parça Çalışma Tezhagı (Part WB)** içerisindeki **3D Offset..** komutu ile et kalınlığı ver, **Aynala (Mirror)** komutu ile simetriğini oluştur ve iki simetrik gövdeyi **Birleştir (Union)** komutu ile tek gövde haline getir.
![Profile_Support_Plane_18](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_18.png)  
Düzlem oluşumunda kullanılan eğrilerin ve dolayısıyla düzlemin değişimini inceleyelim.
![Profile_Support_Plane_19](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_19.png)  
Aynı eskizde(sketch) bulunan iki nesneyi (çizgi ve eğri) seçerek bir düzlem oluşturalım. Ardından, Düzlem oluşumundaki eğriyi değiştirmek için Özellikler bölümündeki ilgili butona tıklayalım.
![Profile_Support_Plane_20](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_20.png)  
Açılan **Bağlantı (Link)** penceresinden, öncelikle seçili olan eğriyi silmek için **Temizle (Clear)** butonuna basın.
![Profile_Support_Plane_2Profile_Support_Plane_2](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_21.png)  
Düzlem oluşumu için gerekli ikinci bir nesne seçilmesi için bu ekranın aşağıdaki gibi boş olmasını sağlıyoruz.
![Profile_Support_Plane_22](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_22.png)  
Sahneden, yeni bir nesne (çizgi, eğri, çember, yay, ...vb) seçelim.
![Profile_Support_Plane_23](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_23.png)  
**OK** butonuna bastığımızda, düzlem, ilk seçilen kenar çizgisi ile son seçilen yay parçası ayarında oluşacaktır.
![Profile_Support_Plane_24](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_24.png)  
Düzlemin güncel halinin izometrik görünümü aşağıdadır.
![Profile_Support_Plane_25](../../images/freecad/curves_wb/surfaces_menu/Profile_Support_Plane_25.png)  

![Pipeshell](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/profile.svg) **Pipeshell profile:**  
**Pipeshell profile** komutu, **Parça Çalışma Tezgahı (Part WB)** ve **Parça Tasarımı Çalışma Tezgahı (Part Desing WB)** komutlarından olan **Süpür/Borula (Sweep/AddivitePipe)** komutlarında kullanılan **süpürülecek olan kesit alan (boru kesiti)** oluşturmaya yarayan komuttur. Anlatım biraz kafa karıştırıcı olabilir. Aşağıdaki açıklamaları ve sonraki komut olan **Pipeshell** komutunu okurken konuyu daha net anlayacağınızı düşünüyorum.

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle 3D ekranı içinden ya da Unsur agacından bir nesne (eğri, çizgisi, çember, ...vb) seçin.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Pipeshell profile** seçeneğini kullanın.

3D ekranı içinden (sahneden) ya da Unsur agacından bir nesne (eğri, çizgisi, çember, ...vb) seçin.  
![Pipeshell_profile_01](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_01.png)  
Curves araç çubuğunda bulunan butona basarak ya da **Surface** menüsünden seçerek **Pipeshell profile** komutunu çalıştırın.
![Pipeshell_profile_02](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_02.png)  
Seçili olan nesne gizlenecek ve ona bağlı yeni bir nesne oluşturulacaktır. Oluşan yeni nesneyi Unsur agacında **Profile** ismi ile görebilirsiniz. Bu nesnenin rengi varsayılan olarak mavi olarak ayarlanır.
![Pipeshell_profile_03](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_03.png)  
Süpürülecek tüm nesneleri sıra ile seçerek **Pipeshell profile** komutunu çalıştırın.
![Pipeshell_profile_04](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_04.png)  
Kesit olması istenilen (süpürülecek) nesne sadece daire, çember ya da elips olmak zorunda değil. Kapalı çokgenler de kesit olarak seçilebilir.
![Pipeshell_profile_05](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_05.png)  
![Pipeshell_profile_06](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_06.png)  
Hatta Kesit, kapalı nesne olmak zorunda da değil.
![Pipeshell_profile_07](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_07.png)  
![Pipeshell_profile_08](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_08.png)  
Araba kaportası oluşturacak şekiller de, kesit olarak kullanılabilir.
![Pipeshell_profile_09](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_09.png)  
![Pipeshell_profile_10](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_10.png)  
![Pipeshell_profile_11](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_profile_11.png)  

![pipeshell](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/pipeshell.svg) **Pipeshell:**  
**Pipeshell** komutu, **Parça Çalışma Tezgahı (Part WB)** ve **Parça Tasarımı Çalışma Tezgahı (Part Desing WB)** komutlarından olan **Süpür/Borula (Sweep/AddivitePipe)** ve **Çatıla (Loft)** komutlarına benzer şekilde bir yol boyunca **seçili kesit alanını süpürerek yüzey oluşturur**. Komut kabaca, Sweep ve Loft komutlarının birer benzeridir diyebiliriz.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle **3D Ekranı içerisinden (sahneden)** süpürülecek yol (eğri, yay, çizgi, ...vb) seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Ardından **Unsur ağacından**, (sahne içerisinden seçmemelisiniz) **Pipeshell profile** komutu ile oluşturulmuş kesitleri seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Pipeshell** seçeneğini kullanın.

**3D Ekranı içerisinden** yolu (eğri, yay, çizgi, ...vb) seçin. Daha sonra **Unsur ağacından**, (sahne içerisinden değil) **Pipeshell profile** komutu ile oluşturulmuş kesitleri (profilleri) seçin ve **Pipeshell** komutunu çalıştırın.
![Pipeshell_01](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_01.png)  
**Pipeshell** komutu çalıştırılınca aşağıdaki şekil oluştu. Yani seçili Yol boyunca, Kesitler (Profiller) arasına yeni kesitler ebatları nispetinde eklendi. 
![Pipeshell_02](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_02.png)  
Unsur ağacından **Pipeshell** nesnesi seçilip **Output (Çıktı/Ürün/Sonuç)** seçeneği **Surface (Yüzey)** olarak ayarlanırsa, aşağıdaki şekli elde ederiz.
![Pipeshell_03](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_03.png)  
Yüzeye dönüştürülen çizimin arka kısmında bir bozukluk olduğunu görüyoruz.
![Pipeshell_04](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_04.png)  
Görüntüyü çevirip modeli incelediğimizde, Son Kesitin (profilin) başlangıç noktasının, diğer profillerden farklı yönde olduğunu tespit ediyoruz. Yüzey oluşturulurken, profillerin noktaları referans alındığı için, modelin son kısımda bir bozulma yaşanmış. Gelin bu bozukluğu düzeltelim.
![Pipeshell_05](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_05.png)  
Bozulmanın yaşandığı kesit (profil), **Sketch004** eskizi referans alınarak oluşturulduğu için, bu eskizde yapacağımız düzenleme, Profili de etkileyecek, düzeltecektir.  
Unsur ağacından **Sketch004** eskizini seçip, **Attachment** ayarlarından **Açı** değerini inceliyoruz.
![Pipeshell_06](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_06.png)  
**Sketch004** eskizinin, **Attachment** ayarındaki **Açı** değerini **180** olarak değiştirerek, eskizi kendi merkezindeki Z ekseninde 180 derece döndürüyoruz. Gördüğünüz gibi, modeldeki bozulma düzeliyor ve istediğimiz / beklediğimiz sonucu elde ediyoruz. Bazen, bozulmanın olduğu eskizi düzenleme modunda açıp değiştirerek te benzer sonuç elde edebiliyoruz. Dairesel kesitli eskizlerde yukarıda uyguladığımız yöntemin (ayarlarda değişiklik yapmak) daha uygun olduğu kanaatindeyim.
![Pipeshell_07](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_07.png)  
[**Pipeshell profile**](https://mhalil.github.io/Freecad_curves_wb_surfaces.html#pipeshellprofile) komutu anlatılırken çizdiğimiz farklı kesitlere ait örnek çalışmaların **Pipeshell** komutu ile yüzeye dönüştürülmüş hallerini aşağıda görüp inceleyebilirsiniz.
![Pipeshell_08](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_08.png)  
![Pipeshell_09](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_09.png)  
![Pipeshell_10](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_10.png)  
![Pipeshell_11](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_11.png)  
![Pipeshell_12](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_12.png)  
![Pipeshell_13](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_13.png)  
![Pipeshell_14](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_14.png)  

![gordon](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/gordon.svg) **Gordon surface:**  
**Gordon surface** komutu, bir dizi eğriyi bir yüzey olarak birleştirmek için kullanılır. Bu komut, birçok farklı endüstride, özellikle tasarım veya üretim sürecinde üç boyutlu 
yüzeylerin oluşturulması gerektiğinde (tasarımın daha akıcı ve doğal bir şekilde görünmesini sağlar), özellikle de CNC işleme, kalıp yapımı ve üretim süreçlerinde sıkça kullanılır.  
Bu komut, yüzey için bir destekleyici çizgi veya eğri ağı gerektirir. Yüzey, bu çizgilerin arasında üzeri "örtülü" yapı şeklinde oluşacaktır.

![GordonSurface_01](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_01.png) 
**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- İlk olarak, birkaç eğri oluşturun. Bunlar, bir yüzey oluşturmak için birleştirilecek eğriler olacaktır. Eğrileri, FreeCAD'deki çeşitli araçlarla (farklı çalışma tezgahlarındaki komutlarla) veya bir CAD programından alınan dosyalarla 
  oluşturabilirsiniz.
- Yukarıdaki resimdeki mavi çizgiler (kaburgalar), yüzey boyunca farklı noktalarda yüzeyin şeklini temsil eder. Bunlar yüzey boyunca enine kesitler olarak veya, yüzeyin "örtüleceği/çadırlanacağı" destekler olarak düşünülebilir.
- Sarı çizgiler, mavi çizgilerle tanımlanan enine kesitler ("kaburgalar") arasındaki yüzeyin kapsamını ve şeklini (rayları) temsil eder.
- Şimdi yüzeyi tanımlayacak olan tüm çizgileri (Yukarıdaki örnekte mavi ve sarı eğrileri) seçin.
- Seçim sırası, dikiş veya çadırlama/örtüleme sırasını tanımlar.
- Yüzeyi tanımlayan tüm çizgileri seçmek için çoklu seçimi kullanın. (`Ctrl` tuşunu basılı tutarken sol tıklayın.)
- Sırayla önce kaburgaları seçin. (Yukarıdaki örnekte, soldan sağa veya sağdan sola mavi eğrileri seçin.)
- Ctrl tuşunu basılı tutmaya devam edin ve kapsam çizgilerini ("rayları") seçin. (Yukarıdaki örnekte sarı eğrileri.)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surfaces** menüsündeki **Gordon surface** seçeneğini kullanın.

**Özellikler**  
**Gordon Surface** komutunun **Veri (Data)** sekmesindeki özelliklerini inceleyelim.  
**Placement (Yerleşim)** : Ortaya çıkan Gordon yüzeyinin yerleşimini ayarlamak için kullanılabilir. Detay için [buraya bakınız.](https://wiki-freecad-org.translate.goog/Placement?_x_tr_sl=auto&_x_tr_tl=tr&_x_tr_hl=tr)  
**Not:** Yerleştirme özellikleri, yüzeyi oluşturmak için kullanılan eğrilerin/çizgilerin yerleşimini ayarlamaz, yalnızca yüzeyi ayarlar.  
**Label (Etiket)** : Yüzey için kullanıcı tarafından belirlenen etiket (ad). (Varsayılan: Gordon)  
**Output (Üretim/Çıktı)** : Yüzeyin Üretim/Çıktı tipini tanımlar. (Varsayılan değer: Yüzey, Seçenekler: Yüzey, Tel Kafes)  
**Gordon>Max Ctrl Pts** : En fazla kontrol noktası miktarı (Varsayılan değer: 80)  
**Gordon>Sources (Kaynaklar)** : Gordon yüzeyini oluşturmak için kullanılan, kullanıcı tarafından seçilen çizgiler/eğriler.  
**Gordon>Tol3D** : 3D tolerans (Varsayılan değer: 0.01)  
**Wireframe>Samples U** : U yönündeki örnekleme sayısı. (Varsayılan değer: 16)  
Bu değer, Üretim/Çıktı özelliği **Tel Kafes** olarak ayarlandığında, **ağın yoğunluğunu** belirlemek için kullanılır.
 **Wireframe>Samples V** : V yönündeki örnekleme sayısı. (Varsayılan değer: 16)  
Bu değer, Çıktı özelliği Tel Kafes olarak ayarlandığında ağın yoğunluğunu belirlemek için kullanılır.  
Aşağıda, Tel kafes (Wireframe) modunda ve `U` ve `V` değerleri **16** olan (U=16, V=16) Gordon Yüzeyi gösterilmektedir.
![GordonSurface_02](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_02.png) **Wireframe**  
Samples U: 16  
Samples V: 16
![GordonSurface_03](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_03.png) **Wireframe**  
Samples U: 32  
Samples V: 16
![GordonSurface_04](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_04.png) **Wireframe**  
Samples U: 32  
Samples V: 32
![GordonSurface_05](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_05.png) **Surface** 
![GordonSurface_06](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_06.png)

**Notlar:**  

- Her grubun eğrileri (kaburgalar ve raylar) diğer grubun tüm eğrilerine temas etmelidir.  
  Başka bir deyişle, burada gösterildiği gibi bir ızgara veya ağ deseni oluşturmalıdırlar:
 ![GordonSurface_07](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_07.png)- Genel olarak, ortaya çıkan Gordon yüzeyinin **yüzey normali**, eğrilerin yönü ile belirlenecektir  
  Eğriler +Y'den -Y'ye yönüne doğru çizilirse elde edilen yüzey normali +Z yönünde olurken, eğriler -Y'den +Y'ye doğru çizildiğinde, yüzeyin normal yönelimli -Z yönünde olur.

- Gordon Surface komutu ile oluşturulan 2 boyutlu yüzey, **Parça Çalışma Tezgahı'nın (Part WB)** [Katıla (Extrude)](https://wiki-freecad-org.translate.goog/Part_Extrude?_x_tr_sl=auto&_x_tr_tl=tr&_x_tr_hl=tr) ya da [**3D Offset**](https://wiki-freecad-org.translate.goog/Part_Offset?_x_tr_sl=auto&_x_tr_tl=tr&_x_tr_hl=tr) komutları ile 3 boyutlu katı model haline getirilebilir.

- Oluşan 2 boyutlu yüzey, **ParçaTasarımı Çalışma Tezgahı (PartDesign WB)** ile de 3 boyutlu katı model haline getirilebilir  
  Bunun için yüzeyi bir gövde içine sürükleyerek **Base Feature (Temel Unsur)** oluşturulur, daha sonra **Katıla (Pad)** komutu kullanılır.

![GordonSurface_08](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_08.png) 
![GordonSurface_09](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_09.png) 
![GordonSurface_10](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_10.png) 
![GordonSurface_11](../../images/freecad/curves_wb/surfaces_menu/GordonSurface_11.png)

![segment_surface](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/segment_surface.svg) **Segment surface:**  
**Segment surface** komutu, seçili yüzeyi yatay, düşey ya da her iki yönde parçalara bölmek/ayırmak için kullanılır.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir yüzey seçin.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Segment surface** seçeneğini kullanın.

Parçaya parçalamak/bölmek istediğimiz yüzey, aşağıdaki resimde görülmektedir.  
![Segment_Surface_01](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_01.png)  
Öncelikle bölünmek istenilen Yüzey seçilmeli ardından **Segment surface** komutu çalıştırılmalı.
![Segment_Surface_02](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_02.png)  
Komut çalıştırıldıktan sonra elde edilen sonuç aşağıda görülmektedir.
![Segment_Surface_03](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_03.png)  
Unsur ağacından **Segment_Surface** öğesini seçip, komuta ait ayarları inceleyelim.  
**Option (Seçenek)** özelliği, **Auto (Otomatik)** iken **Option Auto** ayarı altındaki **Direction (Yön / Yönelim)** seçeneği **U** olarak seçildiğinde, seçili yüzey **U** yönünde otomatik olarak bölümlendi/parçalara ayrıldı.
![Segment_Surface_04](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_04.png)  
**Option Auto** ayarı altındaki **Direction (Yön / Yönelim)** seçeneğini **V** olarak değiştirdiğimizde, seçili yüzey **V** yönünde otomatik olarak bölümlendi/parçalara ayrıldı.
![Segment_Surface_05](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_05.png)  
**Direction (Yön / Yönelim)** seçeneğini **Both (Her ikisi)** olarak değiştirirsek, tahmin edeceğiniz üzere, seçili yüzey hem **U** hemde **V** yönünde (ızgara şeklinde) otomatik olarak bölümlenir/parçalara ayrılır.
![Segment_Surface_06](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_06.png)  
**Option (Seçenek)** özelliği, **Custom (Özel)** olarak değiştirildiğinde, **Option Custom (Özel'in Seçenekleri)** isimli yeni özellikler paneli karşımıza çıkıyor.
![Segment_Surface_07](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_07.png)  
İlk olarak **Knots U** özelliğini inceleyelim.  
**Knots U** seçeneği, **U** yönünde noktalar belirtmemizi ve yüzeyi bu noktalara göre parçalara ayırmamızı sağlar.  
Unsur ağacından **Segment_Surface** öğesini seçiliyken özellikler panelinden **Knots U** seçeneğinin yanındaki butona tıklayın.
![Segment_Surface_08](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_08.png)  
Karşımıza çıkan **List (Liste)** diyalog kutusuna, her satıra bir değer yazmak kaydı ile 0 (sıfır) ile 1 (bir) arasında değerler yazın.  
Burada bahsedilen 0 (sıfır) ve 1 (bir) değeri yüzeyi, bölmek için belirtilecek yüzdelik değerlerdir. (örneğin 0.5 değeri %50 yani tam ortadan böl anlamına gelmektedir.)  
Örnek olarak **0.1** ve **0.5** değerlerini yazalım.  
**NOT:** Ondalık değerleri yazarken, virgül kullanılmamalıdır. Ondalık ayırıcı olarak (Python programlama dilinde olduğu gibi) **Nokta** karakteri kullanılmalıdır. (Python'da virgül karakteri, parametreleri ayırmak için kullanılır.)
![Segment_Surface_09](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_09.png)  
Görüldüğü üzere, seçil yüzey **U** yönünde %10 ve %50 mertebesinden kesilerek 3 yüzeye bölündü.
![Segment_Surface_10](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_10.png)  
Yüzeyi **V** yönünde de %25 ve %65 oranından keselim.
![Segment_Surface_11](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_11.png)  
Sonuç aşağıda görülüyor. **Knots U** ve **Knots V** değerleri değiştirildiğinde yüzey otomatik olarak yeni değerlere göre bölümlenecektir.
![Segment_Surface_12](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_12.png)  
Üst görünüşten bakarak kesim oranları daha net görüntülenebilir.
![Segment_Surface_13](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_13.png)  
**Segment_Surface** öğesinin **Option Custom (Özel'in Seçenekleri)** özelliğinin **Knots U** ve **Knots V** seçeneklerinin farklı bir kullanımını daha görelim.  
Bunun için sahneye öncelikle bir silindir ekliyoruz ve yarıçapını 1.00 mm olarak belirtiyoruz.
![Segment_Surface_14](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_14.png)  
Silindir yüzeyini seçerek **Surface** menüsündeki **Segment surface** komutunu çalıştırıyoruz.
![Segment_Surface_15](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_15.png)  
Silindir nesnesini gizliyoruz ve oluşan Segment Yüzeyini görüyoruz.
![Segment_Surface_16](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_16.png)  
**Option (Seçenek)** özelliği, **Custom (Özel)** olarak değiştiriyoruz.
![Segment_Surface_17](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_17.png)  
**Knots U** değerini 3.14 olarak belirtiyoruz. Bu işlem sonrası yüzey **U** yönünde tam ortadan ikiye bölünüyor.  
Bunun sebebini açıklamak gerekirse;  
Yüzeyi oluşturan Çemberin yarıçapı 1.00mm olduğu için çemberin çevre uzunluğu (2*pi*r formülü ile hesaplandığında) 6.28mm olmaktadır. 
Doğal olarak 3.14 değeri uzunluğun yarısına tekabül ettiği için yüzey yam ortadan ikiye bölünüyor.
![Segment_Surface_18](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_18.png)  
**Knots U** değerini aşağıdaki resimde gösterildiği şekilde revize ettiğimizde ise yüzey (neredeyse) 4 eşit parçaya bölünmüş oluyor.
![Segment_Surface_19](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_19.png)  
Sonuca dair görüntü;
![Segment_Surface_20](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_20.png)  
**Segment_Surface** öğesinin **Option Custom (Özel'in Seçenekleri)** özelliğinin bir diğer seçeneği olan **Knots UProvider** ve **Knots VProvider** 'ı inceleyelim.  
Bunun için öncelikle, oluşturduğumuz Silindir nesnesine ait bir çemberi seçelim ve ardından **Curve** menüsünden **Discretize** komutunu çalıştıralım.
![Segment_Surface_21](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_21.png)  
Komut sonrasında, seçili çember boyunca eşit aralıklı 100 adet nokta oluşturuldu.
![Segment_Surface_22](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_22.png)  
Silindiri ve Segment Yüzeyini gizleyerek, **Discretize** komutunu ile oluşturulan noktaları inceleyelim.
![Segment_Surface_23](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_23.png)  
Segment Yüzeyi görüntüleyelim ve **Discretize** komutunu ile oluşturulan noktaların sayısını **6** olarak değiştirelim. Böylece, çember çevre uzunluğu boyunca eşit aralıklı **6** adet nokta elde etmiş olduk.
![Segment_Surface_24](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_24.png)  
**Segment_Surface** öğesinin **Option Custom (Özel'in Seçenekleri)** özelliğinin **Knots UProvider** seçeneğini kullanarak oluşturduğumuz 6 noktayı değer olarak atayalım.
![Segment_Surface_25](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_25.png)  
Butona basınca karşımıza çıkan **Bağlantı (Link)** penceresinden, **6** noktaya ait öğeyi (Discretize_Edge) seçip ardından OK (Tamam) butonuna basıyoruz.
![Segment_Surface_26](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_26.png)  
İşlem sonrası seçili yüzey, belirlenen öğedeki (Discretize_Edge) nokta sayısı ve konumundan parçalara ayrılıyor.
![Segment_Surface_27](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_27.png)  
Unsur ağacından **Discretized_Edge** öğesi seçilerek **Number (Sayı)** değeri **10** olarak değiştirildiğinde/güncellendiğinde, Segment Yüzeyi **U** yönünde **10** eşit parçaya bölünüyor.
![Segment_Surface_28](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_28.png)  

![spring](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/spring.svg) **Compression Spring:**  
**Compression Spring (Baskı Yayı)** komutu, adından anlaşıldığı üzere, baskı yayı / sıkıştırma yayı oluşturmak için kullanılan komuttur.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Compression Spring** seçeneğini kullanın. Bu sayede sahneye bir baskı yayı (eğrisi) eklenir.

**Curves** araç çubuğunda bulunan ilgili düğmeye, ya da **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Compression Spring (Baskı Yayı)** butonuna basarak komutu çalıştıralım. Sahnenin boş olduğunu, Unsur ağacında hiç bir öğe olmadığına dikkat edin.  

![Compression_Spring_01](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_01.png)  
Komut çalıştırılınca sahneye bir Baskı Yayı (eğrisi) ekleniyor. Unsur ağacından **CompSpring** öğesi seçildiğinde, Baskı yayına ait parametreler aşağıdaki gibi görüntüleniyor. Baskı Yayının **Diameter (Çap)** değeri **4 mm** olarak belirlenmiş. Bu değeri değiştirerek sonucu inceleyelim.
![Compression_Spring_02](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_02.png)  
Baskı Yayının **Diameter (Çap)** değerini **10 mm** olarak değiştirdiğimizde, Baskı yayı otomatik olarak güncelleniyor.
![Compression_Spring_03](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_03.png)  
Baskı Yayını oluşturan bir diğer parametre olan **Length (Boy/Uzunluk/Mesafe)** değerini değiştirerek soncu görelim.  
**10 mm** olan **Length (Boy/Uzunluk/Mesafe)** değerini **5 mm** olarak değiştirdiğimizde görüyoruz ki, baskı yayı daha kısa mesafeye sahip olarak oluşturuldu, yani baskı yayı sıkışmış bir şekil aldı diyebiliriz. Bu parametre değiştirilerek gerçekci animasyon 
oluşturulabilir.
![Compression_Spring_04](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_04.png)  
**Turns (Çevrim/Dönüş)** değeri, Baskı Yayı oluşturulurken eğrinin kaç tur döndürülerek yay oluşturulması gerektiğini belirttiğimiz parametredir. Vidalarda **Hatve / Adım** değeri ile aynı değerdir.  
**5** olan **Turns** değerini **2** olarak değiştirdiğimizde elde ettiğimiz yayın görüntüsü aşağıdadır. Bu ayar ile Eğri, başlangıç noktasından itibaren 2 tur çevrilerek yay elde edildi.
![Compression_Spring_05](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_05.png)  
**Wire Output**, Baskı Yayının görünümünün ayarlandığı parametredir. **Wire Output (Tel Ürün/Sonuç)** parametresinin alabileceği değerler **true (doğru)** ve **false (yanlış)** ile sınırlıdır. Parametre değerini **false (yanlış)** olarak belirlediğimizde, **Baskı Yayı Tel olarak görünmesin** demiş oluyoruz ve baskı yayı dairesel kesitli bir yaya dönüşmüş oluyor.
![Compression_Spring_06](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_06.png)  
**Wire Output** parametresi **false (yanlış)** olarak değiştirildiğinde elde ettiğimiz dairesel kesite ait çap değerini, **Wire Diameter (Tel Çapı)** parametresi ile belirleyebiliyoruz.  
**0,5 mm** olan **Wire Diameter (Tel Çapı)** parametre değerini **1,25 mm** olarak değiştirdiğimizde, Baskı Yayının görünümü de eş zamanlı olarak güncelleniyor.
![Compression_Spring_07](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_07.png)  
**Flatness (Düzlük / Düzgünlük)** parametresi, Baskı Yayının uç noktalarının düzlemsel olarak ayarlanmasını sağlayan parametredir.  
**Flatness (Düzlük / Düzgünlük)** parametre değeri **0 (sıfır)** iken oluşan Yaya ait Ön Görünüm, aşağıdaki gibidir.
![Compression_Spring_08](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_08.png)  
**Flatness (Düzlük / Düzgünlük)** parametre değerini artırarak Yayın düzlemsel bir yüzeye tam olarak oturması / temas yüzey alanının artırılması sağlamak sağlanabilir.  
**Flatness** değerini **4** olarak değiştirerek elde ettiğimiz Yaya bakalım
![Compression_Spring_09](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_09.png)  
Baskı Yayının **Diameter (Çap)** parametresini incelemek için sahneye yarıçapı **5 mm** olan bir silindir nesnesi ekliyorum.
![Compression_Spring_10](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_10.png)  
**ComSpring** nesnesinin **Wire Output** parametresini **false (yanlış)** olarak ayarlıyorum. Sonuç aşağıda.
![Compression_Spring_11](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_11.png)  
Sahneye **Ön Görünüm**'den baktığımda Baskı Yayının **Diameter (Çap)** değerinin Silindire kıyasla nasıl göründüğünü daha net olarak görebiliyorum.
![Compression_Spring_12](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_12.png)  
Silindir yarıçapını **8 mm** (Çapı 16mm), Baskı Yayının Çap değerini de **16 mm** olarak ayarladığımda sonuç yine değişmiyor. Yani Baskı Yayının Çap değeri olarak kastedilen değer, Yayın **Dıştan Dışa** olan çap mesafesidir. Yani **Wire Diameter (Tel Çapı)** parametre değeri, Baskı Yayının konulacağı deliğe/yuvaya ait çap değerini temsil ediyor. 
![Compression_Spring_13](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_13.png)  
**Wire Diameter (Tel Çapı)** parametre değerini artırmamıza rağmen, oluşan Baskı Yayının et kalınlığının içe doğru büyüdüğü, yayın dış çapın değişmediği, iç çap değerinin azaldığı, aşağıdaki görüntüden net bir şekilde görülmüş oluyor.
![Compression_Spring_14](../../images/freecad/curves_wb/surfaces_menu/Compression_Spring_14.png)  

![reflectLines](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/reflectLines.svg) **Reflect Lines:**  
**Reflect Lines (Akis Çizgileri/Eğrileri)**, sahneye olan bakış açısı temel alınarak, seçili nesne(ler)in ya da yüzeylerin dış kontur çizgisini (silüetini) eğriler vasıtası elde etmeye
 yarayan komuttur. **Reflect Line** komutu ile oluşturulan/elde edilen eğriler, **Draft Workbench'te (Taslak Çalışma Tezgahında)** bulunan komutlarla birlikte kullanılabilir. Tarif anlaşılmamış olabilir, komutu uygulayarak anlayalım.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle nesne(ler) veya yüzey(ler) seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Reflect Lines** seçeneğini kullanın.

**Reflect Lines** komutu uygulayarak eğri elde etmek istediğimiz nesne aşağıda görülmektedir.  
![Reflect_Lines_01](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_01.png)  
Unsur ağacından, ilgili nesneyi seçerek **Reflect Lines** komutunu çalıştırıyoruz. Bu algoritma, şeklin **ViewDir** yönündeki izdüşümünü hesaplar.
![Reflect_Lines_02](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_02.png)  
Oluşan Akis/Yansıtma Eğrileri görmek için, Unsur ağacından, ilgili nesneyi (Thickness) seçerek gizliyoruz.  
**Özellikler** panelindeki **Source** parametresi, hangi nesne(ler) ya da yüzey(ler) seçilerek Akis Eğrisi oluşturulduğunu belirtir.
![Reflect_Lines_03](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_03.png)  
**Cleaning Options (Temizlik Seçemekleri)** başlıklı Özellik bölümünde bulunan **Remove Duplicates (Yinelenenleri Kaldır)** parametresi, **true (doğru)** olarak ayarlanırsa, belirtilen **Cleaning Tolerance (Temizleme Toleransı)** değeri ile belirlenen miktardan yakın olan noktalar arasındaki çizgielri/eğrileri siler/temizler.
![Reflect_Lines_04](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_04.png)  
**Edge Type (Kenar Biçimi)** başlıklı Özellik bölümünde bulunan **Out Line** parametresi, nesnenin siluet çizgilerinin ana hatlarıyla **eğrileri** ile çizilmeyeceğini belirttiğimiz kısımdır. Bu parametre **false (yanlış/hayır)** olarak ayarlanırsa, oluşan Akis Çizgilerinin/Eğrilerinin, **eğrisel parçaları** gizlenir. 
![Reflect_Lines_05](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_05.png)  
Yukarıdaki çizimde bu parametrenin sonuçları tam olarak belli olmadı. Bunun için sahneye Eğrisel hatlara sahip yeni bir nesne ekleyerek parametreyi inceleyelim.  
Sahneye bir **Halka** nesnesi ekleyelim, nesneyi seçelim ve **Reflect Lines** komutunu çalıştıralım.
![Reflect_Lines_06](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_06.png)  
**Out Line** parametresi **true (doğru/evet)** iken elde edilen sonuç;
![Reflect_Lines_07](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_07.png)  
**Out Line** parametresi **false (yanlış/hayır)** iken elde edilen sonuç aşağıdadır. Görüldüğü üzere Nesnenin dış hattına (silüetine) ait eğri gizlendi. 
![Reflect_Lines_08](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_08.png)  
**Rg1Line** parametresi, iki yüzey arasındaki **G1-sürekliliğindeki** pürüzsüz kenarı görüntülemek ya da gizlemek için kullanılır.
![Reflect_Lines_09](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_09.png)  
**RgNLine** parametresi, bir yüzeye iliştirilmiş **CN-sürekliliğindeki** kenarı görüntülemek ya da gizlemek için kullanılır.
![Reflect_Lines_10](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_10.png)  
**Sharp** parametresi, keskin kenar (**C0-sürekliliği)** görüntülemek ya da gizlemek için kullanılır. 
![Reflect_Lines_11](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_11.png)  
**Edge Type (Kenar Biçimi)** başlığında bulunan parametrelerinin tamamı **true (doğru/evet)** olarak ayarlanmışken, sahneye **Ön Görünüm (Front)** bakış açısı ile baktığımızda aşağıdaki görüntüyü görürüz.
![Reflect_Lines_12](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_12.png)  
sahneye **Sağ Yan Görünüm (Right)** bakış açısı ile baktığımızda aşağıdaki görüntüyü görürüz.
![Reflect_Lines_13](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_13.png)  
Sahneye **Sol-Ön-Üst (Left-Front-Top)** bakış açısı kesişimi olan köşeden baktığımızda aşağıdaki görüntüyü görürüz.  
Dikkat ettiyseniz şu ana kadar **Reflect Lines** başlıklı özellik kısmında **On Shape** parametresi sürekli **true (doğru/evet)** olarak ayarlanmıştı. Bu sayede **Reflect Lines** komutu sonrası elde edilen Akis Çizgileri/Eğrileri 3 boyutlu (3B) olarak elde edilmiş oldu. Tam olarak aynı şey olmasa da, komut sonrası Nesne, Wireframe (Tel Kafes) görünümünde görüntülenmiş gibi bir sonuç elde edilir.
![Reflect_Lines_14](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_14.png)  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlandığında Akis eğrileri, **XY düzleminde** oluşturulur. Yani sonuç 2 Boyutlu (2B) bir yapıya sahiptir. XY Düzlemine dik açıdan (düzlemin Normal doğrultusundan) yani **Üst Görünümden** bakıldığında gerçek sonuç görüntülenir. Bu komut, **TechDraw**'a geçmeden (OnShape özelliği devre dışı bırakıldığında) bir nesnenin 2B görünümünü elde etmek için kullanılabilir. 
![Reflect_Lines_15](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_15.png)  
Sahneye Üst Görünümden (Top) baktığımızda, doğru görüntüyü elde etmiş oluyoruz.  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlandığında (ReflectLines XY düzleminde olduğunda), **ViewPos** ve **UpDir** özellikleri kullanılabilir. Bu durumda, Akis Çizgilerinin Konumunun ve Yöneliminin ayarlanmasına izin verilir.
![Reflect_Lines_16](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_16.png)  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlandığında, sahneye **Sağ Yan Görünümden (Right)** bakıldığında görülen şekil aşağıdaki gibidir. Akis Eğrilerinin 2 boyutlu (2B) olduğu net olarak görünüyor.
![Reflect_Lines_17](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_17.png)  
Sahneye Ön Görünümden (Front) bakıldığında görülen şekil aşağıdaki gibidir. Akis/Yansıma Eğrilerinin 2 boyutlu (2B) olduğu net olarak görünüyor.
![Reflect_Lines_18](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_18.png)  
Sahnede **X, Y, Z eksen çizgilerini** göstererek **Thickness** nesnesinin, orijin (0,0,0) noktasına göre nasıl bir konumda olduğuna bakalım. Görüyoruz ki **Thickness** nesnesi temelde, orijin noktasına altıgen şekil çizilip bir yol boyunca süpürülerek (Sweep komutu ile) elde edilmiş. Yani **Thickness** adındaki altıgen boru/kanalın bir ucu tam olarak orijin (0,0,0) noktasında bulunuyor.
![Reflect_Lines_19](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_19.png)  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlanıp sahneye **Üst Görünümden (Top)** bakıldığında **View Pos** parametre değerleri [42,80 31,79 17,80] olarak görünmektedir. Bu değerler **Thickness** nesnesi XY düzlemine 2B olarak dönüştürüldüğünde orijinin bulunduğu koordinatları göstermektedir. 
![Reflect_Lines_20](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_20.png)  
**View Pos** değerlerini değişirilerek nesnenin konumunu (orijin noktasını hareket ettirerek) farklı noktaya taşıyabiliriz. Örneğin Nesnenin orijin noktasını (0,0,0) noktasına 
taşıyalım.
![Reflect_Lines_21](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_21.png)  
**View Dir (Kamera/Bakış Açısı Yönü/Doğrultusu)** parametre değerleri, **Reflect Lines (Akış Eğrileri)** oluşturulurken sahneye hangi bakış açısından (kamera yönünden) ve 
mesafesinden bakıldığına dair koordinat değerlerinin belirlendiği ve ayarlandığı kısımdır.
![Reflect_Lines_22](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_22.png)  
3 boyutlu **Thickness** nesnesi **Reflect Lines** komutu ile Akış/Yansıtma Eğrilerine dönüştürülmeden önce kamera görünümü (bakış açısı) aşağıdaki resimde görüldüğü gibi **Sol-Ön-Üst (Left-Front-Top)** kesişim noktalarında idi (Gezinme Küpüne bakabilirsiniz). Bu açı, kabaca (1, -1, 1) değerlerine karşılık gelir. Nesneye olan yaklığa bağlı olarak bu değer aynı oranda artar ya da azalır. İncelediğimizde kamera 
konumunun (0,58 -0,58 0,58) koordinatlarında iken Akış/Yansıtma Eğrileri
 oluşturulduğunu görüyoruz.
![Reflect_Lines_23](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_23.png)  
**Üst Görünümde (Top)** iken **Thickness** nesnesinin ve Akış/Yansıtma Eğrisinin görüntüsü aşağıdaki gibidir. Yani kamera konumunun (0,58 -0,58 0,58) koordinatlarında iken Akış/Yansıtma Eğrileri oluşturuldu ve XY Düzlemine ektarıldı.
![Reflect_Lines_24](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_24.png)  
Sahneye aşağıdaki şekilde yani örnek kamera koordinatı (1,00 1,00 1,00) ya da katları ile bakmış olsaydık ve **Reflect Lines** komutunu çalıştırarak Akış/Yansıtma Eğrisi oluştursaydık nasıl bir sonuç elde ederdik artık biliyorsunuz.
![Reflect_Lines_25](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_25.png)  
Madem kamera konumuna (bakış açısına) ait X, Y ve Z koordinatları pozitif yönlü, o zaman biz de **View Dir** parametre değerlerini pozitif olarak değiştirelim.
![Reflect_Lines_26](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_26.png)  
**Up Dir (Yukarı Yön Doğrultusu)** parametre değerleri ise, Akış/Yansıtma Eğrisi oluştururken hangi koordinatların Yukarı Yönü gösterdiğini belirlediğimiz değerlerdir. X ve Y koordinatlarını sıfırlar ve sadace Z koordinatını pozitif bir değer belirleyerek istediğimizi elde edebiliriz.  
Aşağıdaki resimde görüldüğü üzere, bir defa oluşturulan Akış/Yansıtma Eğrisine ait parametrele değerleri değiştirilerek Temel nesnenin farklı doğrultu ve mesafelerindeki görüntüleri yeniden oluşturulabiliyor/güncellenebiliyor.
![Reflect_Lines_27](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_27.png)  
**Visible (Görünürlük))** parametresi, Akış/Yansıtma Eğrisi oluşturulurken NSeçili Nesnenin Kamera tarafından Görünen ya da Görünmeyen çizgilerin temel alınacağını belirlediğimiz ayar kısmıdır.  
Unsur ağacından **ReflectLines** nesnesi seçilir ve **Visible (Görünürlük))** parametresi **false (yanlış/hayır)** olarak değiştirilirse aşağıdaki resimde göründüğü gibi bir önceki 
haline kıyasla görünür çizgiler kaybolur, görünmeyen çizgiler görünür hale gelir.
![Reflect_Lines_28](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_28.png)  
Aynı nesnenin bir adet Akis çizgisi oluşturalım ve **Visible (Görünürlük))** parametresi **true (doğru/evet)** olarak ayarlayalım. Rengini turkuaz olarak belirleyelim.
![Reflect_Lines_29](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_29.png)  
Aynı nesnenin bir adet daha Akis çizgisini oluşturalım ve **Visible (Görünürlük))** parametresi **false (yanlış/hayır)** olarak ayarlayalım. Rengini de pembe olarak belirleyelim.
![Reflect_Lines_30](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_30.png)  
Her iki Akis Çizgisinin **On Shape** parametresi **true (doğru/evet)** olarak ayarlandıüğı için eğriler 3 boyutlu oluşmuş olacaktır.
![Reflect_Lines_31](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_31.png)  
Sahneye farklı açılardan bakarsak ta eksik/kayıp bir çizgi kalmamış olduğunu görürüz.
![Reflect_Lines_32](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_32.png)  

![multiLoft](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/multiLoft.svg) **MultiLoft:**  
Adı üstünde, ÇokluÇatılama. Birden fazla **yüzeyi**, loft komutu mantığı ile birbirine bağlayarak 3D nesne elde etmemizi sağlayan komut. Biliyorsunuz, **PartDesing** çalışma tezgahında bir eskiz içerisinde birden fazla kapalı alan varsa, bu eskiz **Extrude** ya da **Loft** komutu ile 3 boyutlu hale getirilemiyor. `MultiLoft` komutu, bize bu noktada kolaylık sağlıyor. Aşağıdaki örnek uygulamaları incelediğinizde ne demek istediğimi anlayacaksınız.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle çatılamak istediğiniz yüzeyleri seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **MultiLoft** seçeneğini kullanın.

Bir eskiz (sketch) içerisinde 3 adet kapalı çokgen çiziyoruz.  
![MultiLoft_01](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_01.png)  
Çizdiğimiz 2 boyutlu (2B) eskizi, **Part** Çalışma Tezgahındaki **Extrude** komutu ile **0,01 mm** değerinde katılayarak 3 boyutlu (3B) nesne haline getiriyoruz. 
![MultiLoft_02](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_02.png)  
**MultiLoft** komutunu kullanabilmek için yüzey alanına ihtiyaç vardır. Bu yüzeyi, **Extrude** komutu ile elde edebileceğimiz gibi, **Surface** ya da **Draft** Çalışma Tezgahları komutlarıyla da elde edebiliriz. Aşağıda, eskiz kenarlarını seçerek oluşturulmuş yüzeyler gösterilmektedir.
![MultiLoft_03](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_03.png)  
**Extrude** komutu ile katıladığımız nesneyi seçerek, **Draft** Çalışma Tezgahı komutlarından olan **Clone (Klon)** komutu ile 3 kez klonluyoruz (kopyasını çıkarıyoruz).
![MultiLoft_04](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_04.png)  
Klonladığımız her kopyayı Z ekseninde bir miktar yukarı taşıyoruz.
![MultiLoft_05](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_05.png)  
Orijinal nesne ile birlikte tüm kopyaları seçerek **MultiLoft** komutunu çalıştırıyoruz.
![MultiLoft_06](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_06.png)  
Nesne ve kopyaları (klonları) paralel olduğu için, **MultiLoft** komut sonucu, **Extrude** komutuna benzer bir sonuç elde ediyoruz.
![MultiLoft_07](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_07.png)  
**MultiLoft** komut sonrası gizlenmiş olan **Extrude** nesnelerini görüntülediğimizde, değişiklik öncesi tüm klonların birbirine paralel ve aynı doğrultuda olduğunu görebiliyoruz.
![MultiLoft_08](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_08.png)  
Şimdi klonları sıra il seçip, **Z** ekseninde **10**'ar derece çevirelim. Klonlar arası mesafeyi daha önce **20 mm** olarak belirlediğimiz, özellikler panelinde görünüyor..
![MultiLoft_09](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_09.png)  
Nesnemizim 4 adet klonunu oluşturduğumuz için, son klonu, **Z** ekseninde **40 derece** çevirmiş olduk. Gördüğünüz gibi klonların açı veya konum bilgilerini değiştirdiğimizde, MultiLoft komutu sonucu elde edilen 3D nesnemiz de anlık olarak güncellenip değişiyor.
![MultiLoft_10](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_10.png)  
Orijinal Eskizin içerisine girip eskizi düzenlediğimizde (ekleme / silme) ne olacağını inceleyelim.
![MultiLoft_11](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_11.png)  
Gördüğünüz gibi, eskizi onaylayıp çıktığımız an, yapılan değişiklik diğer klonlara da yansıyor ve MultiLoft komutu yapılan değişikliklere uygun sonuç veriyor.
![MultiLoft_12](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_12.png)  
Eskizde yeni bir değişiklik yapalım ve sonucu görelim.
![MultiLoft_13](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_13.png)  
Sonuçta eskize eklenen yeni nesne döndürülmüş olarak katılanırken, kama kanalı (slot) şeklinin içerisine çizilen geometri dolayısı ile yapıda bir boşluk oluşturuldu.
![MultiLoft_14](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_14.png)  
Bir başka örnek daha yapalım. Bir eskizde 2 kapalı alan oluşturalım ve bu eskizi 3 defa kopyalayalım. 
![MultiLoft_15](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_15.png)  
Her bir eskizde, şekillerin ebatlarını ve konumlarını (X, Y, Z koordinatı) ve X ekseni etrafındaki açılarını değiştirelim. Ortadaki eskizin Y ekseni ile açısı 45 derece (x ekseni etrafında 45 derece çevrildi), koordinatları: (0, 30, -10) 
![MultiLoft_16](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_16.png)  
Alt kısımdaki eskizin Y ekseni ile açısı 0 (sıfır) derece (Y ekseni üzerinde ya da paralel), koordinatları: (0, 340, -50)
![MultiLoft_17](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_17.png)  
2 boyutlu eskizleri sırası ile yüzeye kavuşturuyoruz. Aşağıdaki örnekte **Part** Çalışma Tezgahındaki **Extrude** komutunu kullanarak nesneleri 3 boyutlu (3B) haline getirdim. 
![MultiLoft_18](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_18.png)  
**Extrude** kalınlığı olarak **0,01mm** değeri belirledim. Sonuçta elde etmek istediğim şey, bir yüzeye sahip olmak. 2 boyutlu bir yüzey elde etmek isterseniz **Draft** Çalışma Tezgahı komutlarından biri olan **Upgrade** komutunu da kullanabilirsiniz.
![MultiLoft_19](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_19.png)  
3 eskizi de yüzeye kavuşturduktan sonra sıra, nesneleri seçip **MultiLoft** komutunu çalıştırmaya geldi.
![MultiLoft_20](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_20.png)  
Veeee sonuç karşınızda.
![MultiLoft_21](../../images/freecad/curves_wb/surfaces_menu/MultiLoft_21.png)  

![blendSurf](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/blendSurf.svg) **BlendSurface:**  
**BlendSurface** komutu, iki yüzeyi, seçili kenarları arasında yeni yüzey oluşturarak bağlar. Komutu çalıştırmadan önce birinci yüzeye ait bir kenarın ve yüzeyin kendisinin, sonrasında ikinci yüzeyin bir kenarının ve yüzeyin kendisinin seçilmesi gerekir.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle, birinci yüzeye ait bir kenarı ve yüzeyin kendisini seçin. (Önce yüzey sonra kenar da seçilebilir. Birlikte seçim için `CTRL` tuşunu kullanın)
- İkinci olarak, ikinci yüzeyin bir kenarını sonra yüzeyin kendisini seçin. (Önce yüzey sonra kenar da seçilebilir. Tüm seçim işlemlerinde `CTRL` tuşuna basılı tutun)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **BlendSurface** seçeneğini kullanın.

**BlendSurface** komutunun kullanımına yönelik örnekler yapalım.  
Aşağıda, kenar çizgileri birbirine 45 derece açılı duran 3 adet kare şekil (yüzey) var. Şekillerin tamamı aynı düzlemde ve birbirine paralel konumda.
![BlendSurface_01](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_01.png)  
Sol kısımdaki şeklin yüzeyini ve kenarını `CTRL` tuşuna basılı tutarak seçiyoruz, ardından ortadaki şeklin yüzeyi ve kenar çizgisini `CTRL` tuşu yardımıyla seçiyoruz. Seçim işlemi tamamlandıktan sonra araç çubuğunda bulunan `BlendSurface` düğmesine basıyoruz. İşlem sonucunda seçili kenarlar arasında yeni bir düzlem yüzey oluşturuldu. Yüzeyin kenarları eğriler vasıtası ile elde edildi.
![BlendSurface_02](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_02.png)  
Yeni oluşan **Blend_Surface** yüzeyini, Unsur ağacından seçerek özelliklerini incelediğimizde, yüzeyi oluşturan eğrilerin süreklilik değerlerinin ne olduğunu görüyoruz. Bu değerleri isteğimiz doğrultusunda değiştirebiliyoruz.
![BlendSurface_03](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_03.png)  
Birinci (Continuity1) ve ikinci (Continuity2) eğrinin değerlerini **2**'den **5**'e yükseltip sonucu inceliyoruz.
![BlendSurface_04](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_04.png)  
Sahnenin ortasındaki ve sağ alt kısmındaki şekillerin de ilgili yüzey ve kenar çizgilerini seçerek **BlendSurface** komutu çalıştıralım. İşlem sonucu yeni bir yüzey (mavi renkli) oluştuğunu aşağıdaki resimde görüyoruz.
![BlendSurface_05](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_05.png)  
Unsur ağacından **Blend_Surface001** isimli yeni yüzeyi seçerek eğrilerin süreklilik (Continuity1 / Continuity2) değerlerini değiştirerek oluşan yüzey şeklini inceliyoruz.
![BlendSurface_06](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_06.png)  
**BlendSurface** komutu, sadece paralel yüzeyde çalışmaz. Aşağıdaki örnekte, birbirine 90 derece açı ile konumlanmış yüzeyleri görmektesiniz. **BlendSurface** komutunu, bu yüzeyler arasında eğrisel bir yüzey oluşturmak için kullanalım.
![BlendSurface_07](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_07.png)  
Kenar ve Yüzeyleri seçerek **BlendSurface** komutu çalıştırıyoruz.
![BlendSurface_08](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_08.png)  
İşlem sonrası oluşan eğrisel yüzeyi aşağıda görmektesiniz.
![BlendSurface_09](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_09.png)  
**Blend_Surface002** yüzeyinin süreklilik değerleri;  
Continuity1:**2**  
Continuity2: **2** 
![BlendSurface_10](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_10.png)  
**Blend_Surface002** yüzeyinin süreklilik değerlerini değiştiriyor ve elde edilen yüzeyi inceliyoruz;  
Continuity1:**9**  
Continuity2: **2** 
![BlendSurface_11](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_11.png)  
Sahnenin sol kısmında duran ve **YZ** düzlemine paralel konumdaki şekli seçerek, **Z** ekseninde aşağı doğru taşıyoruz. 
![BlendSurface_12](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_12.png)  
`OK` (Tamam) butonuna basıp şeklin yeni konumu onaylandığında, **BlendSurface** komutu ile oluşturulan yüzey (**Blend_Surface002** ), otomatik olarak güncelleniyor.
![BlendSurface_13](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_13.png)  
**Blend_Surface002** yüzeyinin süreklilik değerleri incelendiğinde biraz önce belirlediğimiz değerlerin geçerli olduğu görülüyor.;  
Continuity1:**9**  
Continuity2: **2** 
![BlendSurface_14](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_14.png)  
**BlendSurface** komutunu kullanabileceğimiz güzel bir örnekle konuyu kapatalım.  
**Part** Çalışma Tezgahında Parametrik Silindir oluşturalım. Silindirin Yarıçap değerini **2,00 mm**, Yükseklik değerini **5,00 mm** olarak belirleyelim.
![BlendSurface_15](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_15.png)  
Silindirin **2** adet kopyasını çıkararak, aşağıdaki resimde göründüğü gibi, silindirleri birbiri ile 120'şer derece açı ile konumlandıralım.
![BlendSurface_16](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_16.png)  
Silindirlerden birinin çemberini seçerek **Discretize** komutunu çalıştıralım. **Discretize** komutu hakkında daha fazla bilgi için [BURAYI](https://mhalil.github.io/Freecad_curves_wb_curves.html#discretize) ziyaret edebilirsiniz.
![BlendSurface_17](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_17.png)  
Komut çalıştrıldıktan sonra seçili eğri üzerinde Varsayılan olarak Number (Sayı) algoritması ile **100** adet nokta oluşturulur. 
![BlendSurface_18](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_18.png)  
Number (Sayı) parametresi **4** olarak değiştirildiğinde, oluşan nokta sayısı ve noktalar arası mesafe, güncellendi. 
![BlendSurface_19](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_19.png)  
Aynı işlemleri diğer Silindirlere de uygulayarak, her bir silindirin bir yüzeyindeki çember üzerine, eşit aralıklı **4**'er adet nokta ekliyoruz.
![BlendSurface_20](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_20.png)  
Silindir yüzeyini seçerek **Surface** menüsündeki **Segment surface** komutunu çalıştırıyoruz. **Segment surface** komutu hakkında daha fazla bilgi almak isterseniz [BURAYI](https://mhalil.github.io/Freecad_curves_wb_surfaces.html#segmentsurface) ziyaret edebilirsiniz.
![BlendSurface_21](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_21.png)  
Komut çalıştırıldıktan sonra silindir nesnesini gizliyoruz ve oluşan Segment Yüzeyi (Segment_Surface) görüyoruz.  
**Option (Seçenek)** özelliği, **Custom (Özel)** olarak değiştiriyoruz.  
![BlendSurface_22](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_22.png)  
**Knots UProvider** seçeneğini kullanarak oluşturduğumuz **4** noktayı değer olarak atayalım. **Knots UProvider** seçeneğinin yanındaki `...` butonuna basınca karşımıza çıkan **Bağlantı (Link)** penceresinden, **4** noktaya ait öğeyi (**Discretize_Edge**) seçip ardından `OK` (Tamam) butonuna basıyoruz. 
![BlendSurface_23](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_23.png)  
İşlem sonrası seçili yüzey, belirlenen öğedeki (**Discretize_Edge**) nokta sayısı ve konumundan itibaren dikey parçalara ayrılıyor. 
![BlendSurface_24](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_24.png)  
Aynı işlemleri diğer silindirler için de yapıyoruz. Böylece, **BlendSurface** komutu ile birleştirilecek yüzey ve kenarları elde etmiş olduk.
![BlendSurface_25](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_25.png)  
Aşağıda gösterildiği şekilde **Segment_Surface** ve **Segment_Surface_002** nesnelerinin kenar ve yüzeyleri seçerek **BlendSurface** komutunu çalıştırıyoruz.
![BlendSurface_26](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_26.png)  
Seçilen kenar ve yüzeylerin konum ve açılarına bağlı olarak yeni bir eğrisel yüzey (mavi renkli yüzey) oluşuyor. 
![BlendSurface_27](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_27.png)  
**Segment_Surface** ve **Segment_Surface_001** nesnelerine de aynı işlemi uyguluyoruz.
![BlendSurface_28](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_28.png)  
**Segment_Surface_001** ve **Segment_Surface_002** nesnelerine de aynı işlemi uyguluyor ve sonucu inceliyoruz. Oluşan yeni yüzeylerin arasında bir boşluk (yırtık) olduğunu görüyoruz. 
![BlendSurface_29](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_29.png)  
Eğrisel Üçgen yapısına sahip boşluğu kapatmak/doldurmak için **Surface** Çalışma tezgahı komutlarından **Boundaries** komutunu kullanıyoruz.
![BlendSurface_30](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_30.png)  
Komut doğru bir şekilde çalıştırılıp tamamlandıktan sonra, yırtık / boşluk kısmı kapanmış oluyor.
![BlendSurface_31](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_31.png)  
Sonuçu beğeninize sunuyorum.
![BlendSurface_32](../../images/freecad/curves_wb/surfaces_menu/BlendSurface_32.png)  

![blendSolid](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/blendSolid.svg) **BlendSolid:**  
**BlendSolid** komutu, seçili iki yüzeyi, bu yüzeylere ait seçili 2'şer kenarı referans alarak birleştirir. Komut, **Extrude**, **Loft** ve **Sweep** komutlarına benzetilebilir.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir eğri (veya kenar çizgisi) ve yüzey seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **BlendSolid** seçeneğini kullanın.

Sahnede aynı ölçülere sahip iki adet küp nesnesi var. Bu küpler, **Part Çalışma Tezgahı** ile oluşturuldu.  
![BlendSolid_01](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_01.png)  
İlk olarak birinci küpün bir yüzeyini ve seçili yüzeye ait iki kenar çizgisini seçiyoruz.
![BlendSolid_02](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_02.png)  
Ardından ikinci küpün bir yüzeyini ve seçili yüzeye ait iki kenarı seçiyoruz.
![BlendSolid_03](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_03.png)  
Curves araç çubuğunda bulunan **BlendSolid** düğmesi ile ya da **Surface** menüsündeki **BlendSolid** seçeneği ile komutu çalıştırıyoruz.
![BlendSolid_04](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_04.png)  
İşlem sonrası, seçili iki yüzey, seçili kenarlar referans alınarak birleştirildi. Unsur ağacında **Blend_Solid** nesnesi oluştu. Seçili kenarlar birbirine paralel ve aynı düzlemde olduğu için sonuç **Extrude** komutuna benzer bir çıktı verdi.
![BlendSolid_05](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_05.png)  
Küplerden birinin açısını ve konumunu değiştirip sonucu inceleyelim.  
Sahnenin solunda bulunan küpü, **X** eksenin etrafında çevirip **Z** ekseninde yukarı yönde taşıyalım.
![BlendSolid_06](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_06.png)  
**BlendSolid** komutu sonucu elde ettiğimiz **Blend_Solid** unsuru, nesnelerin açısının ve konumunun değişmesi sonucunda yeniden hesaplanarak güncellendi.
![BlendSolid_07](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_07.png)  
**Continuity1** ve **Continuity2** süreklilik değerleri varsayılan olarak **2** atanmış. Bu değeri **0** (sıfır) olarak değiştirirsek, **Blend_Solid** unsuru, eğrisel formunu kaybedip, doğrusal bir hal alır.
![BlendSolid_08](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_08.png)  
**Continuity1** ve **Continuity2** süreklilik değerleri değiştirilerek farklı sonuçlar elde edilebilir.
![BlendSolid_09](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_09.png)  
Küpü biraz da **Y** ekseninde çevirelim.
![BlendSolid_10](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_10.png)  
Sonuç gayet başarılı. Yapılan değişiklik neticesinde, burkulmuş bir cisim elde etmiş olduk.
![BlendSolid_11](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_11.png)  
Küpün ebatlarını (ölçülerini) değiştirelim.
![BlendSolid_12](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_12.png)  
Sahneye sağ yan görünüşten bakıp sonucu inceleyelim.
![BlendSolid_13](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_13.png)  
Küpün açısını ve konumunu ilk değerine geri getirip, ölçüsü değişmiş halde bırakalım.
![BlendSolid_14](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_14.png)  
**BlendSolid** komutunu, bir de **Part Design** Çalışma Tezgahı ile oluşturduğumuz prizmatik nesnelere üzerinde kullanmaya çalışalım.  
Kare ve Dikdörtgen şekiller çizip **Pad** komutu ile kalınlık verdiğimiz küplerin yüzey ve kenarlarını seçip **BlendSolid** komutunu çalıştıralım.
![BlendSolid_15](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_15.png)  
Unsur ağacında **Blend_Solid** unsuru oluştu ancak, sonuç istediğimiz gibi olmadı. **BlendSolid** komutunun çalışması için ilave işlem uygulamamız gerekiyor.
![BlendSolid_16](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_16.png)  
**Part Design** Çalışma Tezgahında oluşturduğumuz Gövde (Body) nesnelerini, **Part** Çalışma Tezgahı komutu yardımıyla **Bileşik (Compound)** hale getiriyoruz. 
![BlendSolid_17](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_17.png)  
**Bileşik (Compound)** komutu düğmesi, araç çubuğunda da mevcut.
![BlendSolid_18](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_18.png)  
Gövde nesnelerini Bileşiğe dönüştürüldükten sonra, yüzey ve kenarları seçerek **BlendSolid** komutunu tekrar çalıştıralım.
![BlendSolid_19](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_19.png)  
Sonuç başarılı. Yüzeylere ait seçili kenarlar, aşağıdaki resimde yeşil renkli olarak görünüyor.
![BlendSolid_20](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_20.png)  
Dikdörtgenler prizmasının açısını değiştirelim.
![BlendSolid_21](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_21.png)  
Burkulmuş doğrusal nesne elde ettik.
![BlendSolid_22](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_22.png)  
Dikdörtgenler prizmasının konumunu da değiştirip **Z** ekseninde yukarı taşıyalım.
![BlendSolid_23](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_23.png)  
Bu kez, burkulmuş eğrisel nesne elde etmiş olduk.
![BlendSolid_24](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_24.png)  
Bir de, dikdörtgen dışındaki şekilleri inceleyelim. Sahneye Dikdörtgenler prizması ile bir Silindir ekleyelim.
![BlendSolid_25](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_25.png)  
Yüzeyleri ve kenarları seçip, **BlendSolid** komutunu çalıştıralım.
![BlendSolid_26](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_26.png)  
Görüldüğü üzere, Unsur ağacında **Blend_Solid** nesnesi oluştu ancak sonuç beklediğimiz gibi olmadı. Unsur ağacında **Blend_Solid** nesnesinde Ünlem işareti olduğuna dikkat edin.
![BlendSolid_27](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_27.png)  
Komutun doğru sonuç vermemesinin, istediğimiz sonucu elde edemememizin sebebi, Silindirin seçili yüzeyine ait sadece bir kenar çizgisi olmasıdır.
![BlendSolid_28](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_28.png)  
Silindirin kesit alanını, bir çember yerine birden fazla (örneğin 4) yay parçası ile oluşturalım.
![BlendSolid_29](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_29.png)  
Silindir nesnesini **Bileşik (Compound)** hale getirelim.
![BlendSolid_30](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_30.png)  
Birer Yüzey ve 2'şer kenar çizgisi seçerek **BlendSolid** komutunu çalıştıralım.
![BlendSolid_31](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_31.png)  
Komut bu kez başarılı sonuç verdi. Seçili kenarlara bağlı olarak Eğrisel bir yapı elde edildi.
![BlendSolid_32](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_32.png)  
**Blend_Solid** nesnesinin **Continuity1** ve **Continuity2** süreklilik değerleri **0** (sıfır) olarak değiştirildiğinde, **Loft** komutuna benzer doğrusal yapı elde edildi.  
**Fuse** parametresi, **false** olarak ayarlandığı için oluşan **Blend_Solid** nesnesi ayrı bir nesne olarak unsur ağacında görüntüleniyor.
![BlendSolid_33](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_33.png)  
Silindirin konumunu ve açısını değiştirip, **Continuity1** ve **Continuity2** süreklilik değerlerini artırdığımızda aşağıdaki sonucu elde ediyoruz.
![BlendSolid_34](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_34.png)  
**Fuse** parametresini, **true** olarak ayarladığımızda **Blend_Solid** nesnesi, bağlantılı olduğu nesnelerle (Dikdörtgenler prizması ve Silindir) birleştirilip tek bir nesne olarak unsur ağacında görüntülenir.
![BlendSolid_35](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_35.png)  

![flatten](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/flatten.svg) **Flatten face:**  
**Flatten face** komutu, silindirik ve konik yüzlerden, bir düzlem yüzey oluşturur. Kısaca, seçili silindirik veya konik yüzeyin UV'sini açar.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir eğri (veya kenar çizgisi) ve yüzey seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Flatten face** seçeneğini kullanın.

Araç yalnızca gerçek bir matematiksel koni veya silindir tarafından desteklenen yüzlerde çalışır.  
Bu konunun önceki sayfasında tartışılan durum budur, yüzey açıkça silindirik veya konik bir yüz olarak tanımlanmamıştır/algılanmamıştır ve bu nedenle yassılaştırma aracı 
üzerinde çalışmaz, en azından şu anda çalışmaz. bu tür durumları desteklemek için genişletilecek. ancak yüzün gerçekten geliştirilebilir olduğu bu gibi durumlarda mesh yöntemi işe yaramalı ve oldukça iyi sonuçlar vermelidir. 

(https://forum.freecad.org/viewtopic.php?style=10&t=22675&start=1260)

Yüzü düzleştir Konik ve silindirik yüzlerden düz gelişmiş bir yüz oluşturur
 **Kullanım**:
 3B Görünümde konik veya silindirik bir yüz seçmelisiniz.
 InPlace özelliği, açılmış yüzü kaynak yüze (InPlace = True) veya XY düzlemine (InPlace = False) teğet koyar.  
UV açıldıktan sonra, yüzey oluştur / kalınlık kazandır, TechDraw'a ekle.

AÇIKLAMA_VE_RESİM  ...

![sweep_around](https://raw.githubusercontent.com/tomate44/CurvesWB/9aac6c2365311724487f79df3343dab90ddcb819/freecad/Curves/resources/icons/sweep_around.svg) **Rotation Sweep:**  
KISA_ACIKLAMA  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir eğri (veya kenar çizgisi) ve yüzey seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Rotation Sweep** seçeneğini kullanın.

AÇIKLAMA_VE_RESİM  ...

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön](freecad-curves-wb-surface-00-menu-komutlari.html)

