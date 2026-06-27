Title: FreeCAD - Curves WB - Surface - 04 - Sketch on Surface
Date: 2023-02-18 00:00
Modified: 2023-05-06 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Sketch
Author: Mustafa Halil

# ![sketch_surf](../../images/freecad/curves_wb/simgeler/surfaces/SketchOnSurface.svg) Sketch on Surface

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
