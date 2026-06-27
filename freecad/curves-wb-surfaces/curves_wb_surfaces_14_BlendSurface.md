Title: FreeCAD - Curves WB - Surface - 14 - BlendSurface  
Date: 2023-04-29 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Blend
Author: Mustafa Halil

# ![blendSurf](../../images/freecad/curves_wb/simgeler/surfaces/BlendSurf2.svg) BlendSurface

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
