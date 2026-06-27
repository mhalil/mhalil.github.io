Title: FreeCAD - Curves WB - Surface - 17 - Rotation Sweep
Date: 2024-04-28 00:00
Modified: 2025-11-15 18:02
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Rotation Sweep, Rotation, Sweep
Author: Mustafa Halil

![sweep_around](../../images/freecad/curves_wb/simgeler/surfaces/RotationSweep.svg) **Rotation Sweep:**  
Rotation Sweep, Bir veya birkaç profili bir yol boyunca ve bir nokta etrafında süpürerek yüzey oluşturmak için kullanılan kullanışlı bir komuttur. TrimPath özelliğinin False olarak ayarlanması halinde, Süpürme (sweep) yüzeyi, tüm yola uyacak şekilde ekstrapole edilecektir.

Bu komut, bir ucundan bir süpürme yoluna temas eden ve diğer ucunda bir merkez noktada buluşan bir profil listesini süpürmek için kullanılır. Yani süpürülecek olan profil, yol ile temas etmelidir. Profilin diğer uç noktası ise döndürme noktasını oluşturacaktır. O nedenle birden fazla profil seçilerek Rotation Sweep komutu çalıştırılacaksa, tüm profillerin döndürme merkezinin temas halinde olması daha doğru sonuçlar üretme adına faydalı olacak diye düşünüyorum.

**Kullanım:** **Rotation Sweep (Döndürerek Süpür)** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- 3D Görünümünde **Öncelikle bir süpürme yolu (path)**, ardından döndürülerek süpürülecek olan **profil ya da profilleri** seçin. (Birlikte seçim için `CTRL` tuşunu kullanın) (Süpürme yolu, istenen eskiz çizgilerini **JoinCurve**'üdür. Yani nesne tek parça olmalıdır. 3D ekranda yolun bir kısmını seçtiğinizde tüm nesne seçili olmalıdır.)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Rotation Sweep** seçeneğini kullanın.

**Profiller ile çalışırken aklınızda bulunması gereken bir kaç husus;**

* Profiller merkezin veya süpürme yolunun dışına taşarsa otomatik olarak kırpılır.

* Yüzey giriş eğrilerine mükemmel şekilde uyar.

* Yolun uçlarında profil yoksa, yüzey dış profillerde durabilir (TrimPath=True) veya süpürme yolunun uçlarına kadar uzanabilir (TrimPath=False)

* Gerektiğinde eskiz çizgilerini **JoinCurve** komutu ile birleştirmek,

* Süpürme yolu ya da profilleri gerektiğinde ortadan bölmek ve 2 süpürme profili elde etmek için **SplitCurve** komutunu kullanabileceğinizi unutmayın.

* **Rotation Sweep** tarafından desteklenmeyen rasyonel bspline’ları önlemek için, **JoinCurve**’nin **ShapeApproximation** özellikleri **True** olarak ayarlanmıştır.

* Teğet desteği elde etmek için süpürme yolu ekstrüde edilir.

* **ExtraProfiles (EkstraProfiller)** özelliği, yüzey oluşturulmadan önce ekstrapole edilebilecek ekstra 
  profil sayısını belirtir. Süpürmeye bazı ekstra yüzey teğetlik 
  profilleri eklemek için artırılır.

* **FaceSupport (YüzeyDesteği)** özelliği, süpürme yolu için bir yüzey desteğinin belirtilmesini sağlar. Giriş profilleri bu yüzle G1 sürekliliğine sahipse, oluşturulan ekstra profiller de yüzeyle G1 sürekliliğine sahip olacak ve yüzey de öyle 
  olacaktır.

* **SmoothTop** özelliği, yüzeyin dönme merkezi etrafında teğet olmaya zorlanmasını sağlar. Girdi profilleri dönme merkezi etrafında ortak bir düzleme teğet DEĞİLSE, 
  yüzey bu bölgedeki profillere uymayacaktır.

* **Rotation Sweep** komutu ile yüzey oluşturulduktan sonra, istenirse ilave profiller eklenerek yüzey revize edilebilir. Bu **Input Shapes** başlığı altında bulunan **Profiles** özelliği sayesinde gerçekleştirilir.

## 1. Çalışma;

Elimizde 3 Eskizden (Sketch) oluşan bir çalışma var. Aşağıda çalışmanın izometrik görüntüsü mevcut.

![Rotation_Sweep_01](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_01.png)

Sketch (Ön Görünüm — XZ Düzlemi)
![Rotation_Sweep_02](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_02.png)
Sketch001 (Sağ Yan Görünüm — YZ Düzlemi)
![Rotation_Sweep_03](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_03.png)
Sketch002 (Üst Görünüm — XY Düzlemi)
![Rotation_Sweep_04](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_04.png)
3D ekranında **öncelikle bir yol (path)**, ardından **bir ucu bu yola temas eden bir profil** seçip **Rotation Sweep** komutunu çalıştırıyoruz.
![Rotation_Sweep_05](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_05.png)
Seçilen Profilin **diğer ucu dönüş merkezi** olacak şekilde, profil yol boyunca döndürülerek süpürüldü. oluşan yüzey aşağıda görünmektedir.
![Rotation_Sweep_06](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_06.png)
3D ekranında **öncelikle bir yol (path)**, ardından **bir ucu bu yola temas eden bir profil** ve bu profilin diğer ucuna (dönüş merkezine) temas eden bir başka profil seçip **Rotation Sweep** komutunu çalıştıralım. Toplamda 2 profil seçmiş olduk ancak ikinci 
seçtiğimiz profil birden fazla çizgi/eğri parçasından oluştuğu için 
sadece bir çizgiyi seçtik ve bu parça yol ile temas halinde değil.
![Rotation_Sweep_07](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_07.png)
Unsur ağacından **Rotation_Sweep** nesnesini seçip **Trim Path (Yolu Kırp)** seçeneğini incelediğimizde, değerin varsayılan olarak **True (Doğru / Evet)** şeklinde geldiğini ve bu nedenle profilin yol boyunca süpürülürken, merkez nokta hizasına geldiğinde kırpıldığını görüyoruz.
![Rotation_Sweep_08](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_08.png)
**Trim Path (Yolu Kırp)** seçeneğini **False (Yanlış / Hayır)** olarak değiştirisek, profilin yol boyunca kırpılmadan süpürüldüğünü ve bu şekilde bir yüzey oluşturduğunu görürüz.
![Rotation_Sweep_09](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_09.png)
3D ekran içerisinde modeli döndürüp, farklı açıdan baktığımızda ikinci 
eskizin, yüzey oluşturma esnasında hiç dahlinin olmadığını daha net 
görürüz. Bunun sebebi, eskizin birden çok çizgi / eğri / yay, …vb parça 
içermesidir.
![Rotation_Sweep_10](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_10.png)
**Curves Çalışma Tezgahının** önceki konularında, çoklu çizgi / eğri parçalarını nasıl tek bir eğriye dönüştüreceğimizi incelemiştik. Unsur ağacından **Sketch001** eskizini seçip, **Curves** Menüsündeki **JoinCurves** seçeneğini kullanarak yeni bir eğri oluşturuyoruz.
![Rotation_Sweep_11](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_11.png)
Komut sonrası Unsur ağacımızda, **JoinCurve** adında yeni bir nesnemizin (unsurumuzun) oluştuğunu görüyoruz.
![Rotation_Sweep_12](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_12.png)
**Sketch001** yerine **JoinCurve** nesnemizi seçerek, iki profil + bir yoldan oluşan yüzey oluşturmaya çalışıp sonucu inceleyelim.
![Rotation_Sweep_13](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_13.png)
Sonuç karşımızda ve tam istediğimiz gibi. Birbirine temas eden 3 eğriden oluşan kusursuz bir yüzey.
![Rotation_Sweep_14](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_14.png)
Görüntüyü döndürerek yüzeyimizi inceleyelim. Harika değil mi?
![Rotation_Sweep_15](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_15.png)

## 2. Çalışma;

Elimizde 3 adet eskiz mevcut. Herbir eskizde **B-Spline** nesneleri var. Bu nesnelerden **Sketch — yol (path)** isimli eskizdeki b-spline nesnesi **iki adet b-spline** eğrisinden oluşmaktadır.
![Rotation_Sweep_16](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_16.png)
**Sketch — yol (path)** isimli eskiz içeriğindeki **b-spline** nesnesi aşağıdaki gibidir. Üst Görünüm — XY Düzlemi;
![Rotation_Sweep_17](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_17.png)
**Sketch001 — Profil_1** isimli eskiz içeriğindeki **b-spline** nesnesi aşağıdaki gibidir. Ön Görünüm — XZ Düzlemi;
![Rotation_Sweep_18](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_18.png)
**Sketch002 — Profil_2** isimli eskiz içeriğindeki **b-spline** nesnesi aşağıdaki gibidir. Sağ Yan Görünüm — YZ Düzlemi;
![Rotation_Sweep_19](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_19.png)
Aşağıda şekilde yeşil renk ile işaretli eğrilerden önce aşağıdaki (XY düzlemindeki) yolu, ardından `CTRL` tuşuna basılı tutarak sol taraftaki (XZ düzlemindeki) eğriyi seçerek **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_20](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_20.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir.
![Rotation_Sweep_21](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_21.png)
Modeli çevirip diğer taraftan bakalım;
![Rotation_Sweep_22](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_22.png)
Şimdi aşağıdaki resimde işaretli eğrilerden önce yol eğrisini, ardından profil eğrisini seçerek **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_23](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_23.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir.
![Rotation_Sweep_24](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_24.png)
Modeli çevirip diğer taraftan bakalım;
![Rotation_Sweep_25](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_25.png)
Son oluşturduğum **Rotation_Sweep001** nesnesini siliyorum. Biraz önceki gibi önce yol ve ardından profil eğrisini seçtikten sonra, **Rotation_Sweep** nesnesinin açık uçlarındaki eğrileri de seçime dahil ederek (resimdeki tüm yeşil eğrileri seçerek) **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_26](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_26.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir. **Rotation_Sweep** nesnesi ile **Rotation_Sweep001** nesnesi birbiri ile tam olarak örtüştü.
![Rotation_Sweep_27](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_27.png)
Modeli çevirip diğer taraftan bakalım; Oluşan Yüzeyler arasında boşluk kalmadı.
![Rotation_Sweep_28](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_28.png)

## 3. Çalışma;

3 adet **Freehand_BSpline** nesnesinden oluşan bir çizimimiz mevcut. Bunlardan önce yolu (**Freehand_BSpline001**),
![Rotation_Sweep_29](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_29.png)
Ardından profili (**Freehand_BSpline002**) seçelim.
![Rotation_Sweep_30](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_30.png)
Sonrasında **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_31](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_31.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir.
![Rotation_Sweep_32](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_32.png)
Şimdi ise, XY Düzlemindeki ikinci eğri olan **Freehand_BSpline** nesnesini ve **Rotation_Sweep** nesnesi açık uçlarından birine ait eğriyi seçerek **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_33](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_33.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir. Gördüğünüz gibi **Rotation_Sweep** nesnesi ile **Rotation_Sweep001** nesnesi arasında bir boşluk kaldı.
![Rotation_Sweep_34](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_34.png)
**Rotation_Sweep001** nesnesinin **Input Shapes** başlığı altında bulunan **Profiles** özelliğini kullanarak bu açığı kapatmaya çalışalım. (**Profiles** özelliğinin yanında bulunan üç nokta butonuna basarak **Link** penceresini açıyor ve 3D ekranından **Rotation_Sweep** nesnesinin açık ucunu seçiyoruz.)
![Rotation_Sweep_35](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_35.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir. **Rotation_Sweep** ve **Rotation_Sweep001** nesnesi kusursuz olarak birleşmiş oldu.
![Rotation_Sweep_36](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_36.png)

## 4. Çalışma;

5 adet **Freehand_BSpline** nesnesinden oluşan bir çizimimiz mevcut.

![Rotation_Sweep_37](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_37.png)
Eğrilerden **Yol nesnesi (Freehand_BSpline — Close Path)** kapalı bir eğridir. (Eğrinin **Periodic** özelliği **true** olarak ayarlandığı için eğri otomatik olarak kapandı.) Önce yol eğrisinin ardından profil eğrisini seçip **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_38](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_38.png)
Elde ettiğimiz yüzeyin izometrik görüntüsü aşağıdaki gibidir.
![Rotation_Sweep_39](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_39.png)
Modele Sağ Yan, Üst ve Ön görünüşten baktığımızda, Oluşan yüzeyin diğer eğrilerle irtibatının olmadığını net olarak görüyoruz.
![Rotation_Sweep_40](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_40.png)
Şimdi de yol eğrisinin ardından 2 adet profil eğrisi seçip **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_41](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_41.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir. **Rotation_Sweep** nesnesinin **Trim Path (Yolu Kırp)** özelliği varsayıla olarak **true (doğru)** şeklinde ayarlandığı için, döndürerek süpürme işlemi, seçili 2 profille sınırlı kaldı, tüm yol boyunca devam etmedi.
![Rotation_Sweep_42](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_42.png)
**Trim Path (Yolu Kırp)** özelliğini **false (yanlış)** olarak değiştirdiğimizde ise oluşan yüzey, yol boyunca devam ettiriliyor.
![Rotation_Sweep_43](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_43.png)
Modele Üst, Sağ Yan ve Ön görünüşten baktığımızda, Oluşan yüzeyin dönüş 
merkezi etrafından ve seçili profiller baz alınarak devam ettirildiğini 
ve diğer (seçilmeyen) eğrilerle hâlâ irtibatının olmadığını görüyoruz.
![Rotation_Sweep_44](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_44.png)
Son olarak ta, önce yol eğrisini, ardından tüm irtibatlı eğrileri seçerek **Rotation Sweep** komutunu çalıştırıyoruz.
![Rotation_Sweep_45](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_45.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir.
![Rotation_Sweep_46](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_46.png)
Modele Ön, Sağ Yan ve Üst görünüşten baktığımızda, Oluşan yüzeyin dönüş 
merkezi etrafında ve tüm seçili profiller baz alınarak üretildiği için 
tüm eğrilerle irtibatlı olduğunu görüyoruz.
![Rotation_Sweep_47](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_47.png)

## 5. Çalışma;

**Freehand_BSpline001** (yol) eğrisi ve bu eğriye temas eden **Freehand_BSpline002 — Profil** eğrisini kullanarak **Rotation Sweep** komutu ile yüzey oluşturmak isteyelim.

![Rotation_Sweep_48](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_48.png)
Önce yolu ardından profili seçip **Rotation Sweep** komutunu çalıştırıyoruz.
![Rotation_Sweep_49](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_49.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir. Profil, tüm yol eğrisi boyunca döndürülerek süpürüldü ve yüzey oluştu.
![Rotation_Sweep_50](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_50.png)
**Freehand_BSpline001** (yol) eğrisini seçerek **SplitCurve** komutunu çalıştırıyoruz.
![Rotation_Sweep_51](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_51.png)
Unsur ağacına **SplitCurve** isimli yeni bir unsur eklendi.
![Rotation_Sweep_52](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_52.png)
**SplitCurve** nesnesini seçip özelliklerine baktığımızda yol profilin, yay 
uzunluğunun tam orta noktasından (%50) iki parçaya bölündüğünü 
görebiliriz.
![Rotation_Sweep_53](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_53.png)
Unsur ağacındaki **SplitCurve** nesnesini seçerek özellikleri aşağıdaki şekilde düzenleyelim; * **Values** : [] * **Cutting Object** : Freehand_BSpline002 — Profil
![Rotation_Sweep_54](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_54.png)
Gördüğünüz gibi **Freehand_BSpline001** (yol) eğrisi, **Freehand_BSpline002 — Profil** eğrisi ile temas ettiği noktadan 2 parçaya bölünmüş oldu.
![Rotation_Sweep_55](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_55.png)
İki parçaya ayrılmış olan **eğrinin bir parçasını** seçip ardından profil eğrisini seçerek **Rotation Sweep** komutunu çalıştıralım.
![Rotation_Sweep_56](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_56.png)
Görüldüğü üzere profil sadece seçili eğri (yol) **parçası** boyunca döndürülüp süpürülerek yüzey oluşturuldu. Profil eğrisini, yol eğrisine temas eden noktasının yerini değiştirerek oluşan yüzeyi düzenleyebiliriz.
![Rotation_Sweep_57](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_57.png)

## 6. Çalışma;

Bu çalışmada, **Rotation Sweep** komutunun **Face Support (Yüzey Desteği)** özelliğini inceleyeceğiz.Öncelikle sahnedeki nesneleri sırayla inceleyelim. Elimizde bir adet Elips (**Ellipse**) nesnesi var. Üst bakıştan baktığımızda, elips aşağıdaki gibi görünüyor.

![Rotation_Sweep_58](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_58.png)
**Offset2D** komutu ile elipsin 3 mm büyük kopyasını oluşturuyor ve Z ekseninde bir miktar yukarı taşıyoruz.
![Rotation_Sweep_59](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_59.png)
**Ellipse** ve **Offset2D** nesneleri, Ön (front) görünümden aşağıdaki şekilde görünüyor.
![Rotation_Sweep_60](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_60.png)
**Ruled Surface** komutu yardımıyla, **Ellipse** ve **Offset2D** nesnelerinden bir yüzey oluşturuyoruz.
![Rotation_Sweep_61](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_61.png)
Oluşan Yüzey, Ön görünümden aşağıdaki şekilde görünüyor.
![Rotation_Sweep_62](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_62.png)
**Ellipse** ve **Offset2D** nesnelerine temas edecek şekilde iki ayrı eskiz çiziyoruz. (**Sketch** ve **Sketch001**)
![Rotation_Sweep_63](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_63.png)
**Sketch** ve **Sketch001** Eskizleri birden fazla eğri parçasına sahip olduğu için **Rotation Sweep** komutunda profil olarak seçildiklerinde sorun çıkabilir. Bu sorunun önüne geçmek için **Sketch** ve **Sketch001** nesnelerine ayrı ayrı **JoinCurve** komutunu uygulayarak, eskiz içerisindeki çizgi, yay, eğir, …vb parçaları birleştiriyor ve tek bir eğri nesnesi elde ediyoruz. (**JoinCurve001** ve **JoinCurve002** eğrileri aşağıda mor renk ile görünmektedir.)
![Rotation_Sweep_64](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_64.png)
Önce **Ellipse** nesnesini (yol olarak) ardından **JoinCurve001** ve **JoinCurve002** eğrilerini (profil olarak) seçerek, **Rotation Sweep** komutunu çalıştıralım.qqq
![Rotation_Sweep_65](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_65.png)
Elde ettiğimiz yüzey aşağıda göründüğü gibidir. Profiller, ortak temas 
noktaları etrafında döndürülerek kendi aralarındaki eğri boyunca 
süpürüldü ve yüzey oluştu.
![Rotation_Sweep_66](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_66.png)
**Rotation_Sweep** nesnesi seçilerek, **Trim Path (Yolu Kırp)** özelliği **false** olarak ayarlıyoruz. Böylece, oluşan yüzeyin tüm yol eğrisi boyunca süpürülerek yüzey oluşturmasını sağlamış oluyoruz.
![Rotation_Sweep_67](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_67.png)
Gizlemiş olduğumuz **Ruled _Surface** nesnesini görünür hale getiriyoruz.
![Rotation_Sweep_68](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_68.png)
Oluşan yüzeyin (**Rotation_Sweep** nesnesi) **Ruled _Surface** nesnesi ile olan irtibatını aşağıdaki resimden görebilirsiniz. **Rotation_Sweep** nesnesi ön görünümde, **Ruled _Surface** nesnesine teğet ancak diğer bakış açılarında bu tür bir ilişki mevcut değil.

![Rotation_Sweep_69](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_69.png)
**Rotation_Sweep** nesnesine **Face Support (Yüzey Desteği)** özelliği kazandırmak için Özellikler panelinde **Face Support** özelliğinin yanındaki **üç nokta butonuna** `...` tıklıyoruz.
![Rotation_Sweep_70](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_70.png)
Açılan **Link (Bağlantı)** penceresinden, **Ruled _Surface** nesnesini seçip **Tamam** butonuna basıyoruz.
![Rotation_Sweep_71](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_71.png)
Artık **Rotation_Sweep** nesnesi, **Ruled _Surface** nesnesine teğet olacak şekilde biçim kazanmış oldu.
![Rotation_Sweep_72](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_72.png)
Yüzeyin yeni şeklini aşağıdaki resimden inceleyebilirsiniz.
![Rotation_Sweep_73](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_73.png)
İsterseniz **IsoCurve** komutu ile **Rotation_Sweep** nesnesine UV yönelimli bir kafes yapısı uygulayabilirsiniz.
![Rotation_Sweep_74](../../images/freecad/curves_wb/surfaces_menu/Rotation_Sweep_74.png)

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
