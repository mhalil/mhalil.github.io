Title: FreeCAD - Curves WB - Curves - 03 - Mixed curve
Date: 2022-11-11 00:00
Modified: 2023-03-04 00:00
Category: Curves WB - Curves
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Mixed, curve
Author: Mustafa Halil

# ![mixed_curve](../../images/freecad/curves_wb/simgeler/curves/Mixed_curve.svg) Mixed curve:

**Mixed curve**, <u>Eğrilerin formlarını Karıştırmak, Kombine etmek</u> amacıyla kullanılan komuttur.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki işlemleri sırasıyla uygulayın:

- Öncelikle karıştırmak/kombine etmek istediğiniz eğrileri seçin. (birden fazla seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves** menüsündeki **Mixed curve** seçeneğini kullanın.

Konuyu daha iyi anlayabilmek adına aşağıdaki örneğe göz atalım.  
Üst görünüşte bir eskiz açıp aşağıdaki şekli, bezier eğri ile çizelim.

![Mixed_Curve_01](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_01.png)

Yan görünüşte de yeni bir eskiz 
oluşturup aşağıdaki şekli bezier eğri ile çizelim. Her iki eğrinin de uç
 noktaları aynı konumda olsun.

![Mixed_Curve_02](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_02.png)

Sahneye İzometrik bakış açısı ile bakarsak iki eğriyi bu şekilde görüyor olmalıyız.

![Mixed_Curve_03](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_03.png)

Bezier eğrileri `CTRL` tuşu yardımıyla seçip, **Mixed curve** komutunu çalıştıralım.

![Mixed_Curve_04](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_04.png)

Komut sonrasında seçili eğriler 
gizlenir ve bu eğrilerin kesişimi/karışımı ile yeni bir eğri elde 
edilir. Sonuç aşağıdaki gibi olmalı.

![Mixed_Curve_05](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_05.png)

**Karıştırılmış / Kombine edilmiş** yeni eğriye üst görünüşten bakarsak, üst görünüşte çizdiğimiz 
("Ust_Top" isimli eskizdeki) eğriyi ile bir bir örtüştüğünü 
göreceksiniz.

![Mixed_Curve_06](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_06.png)

**Karıştırılmış / Kombine edilmiş** yeni eğriye yan görünüşten bakarsak, yan görünüşte çizdiğimiz 
("Yan_Right" isimli eskizdeki) eğriyi ile de bir bir örtüştüğünü 
göreceksiniz.

![Mixed_Curve_07](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_07.png)

Şimdi, **Mixed curve** komutuna ait **Fill Face (Yüzeyi Doldur)** özelliklerini inceleyelim.

![Mixed_Curve_08](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_08.png)

Unsur ağacından **Mixed curve** nesnesi seçili iken **Fill Face1** özelliğini **True (Doğru)** olarak değiştirirsek, 1. Eğriye ait Yüzey doldurulur.

![Mixed_Curve_09](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_09.png)

İşlem sonrası Sahneye Sağ Yan görünüşten baktığımızda elde ettiğimiz görüntü;

![Mixed_Curve_10](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_10.png)

Bu da **Fill Face2** özelliğini **True (Doğru)** olarak değiştirdiğimizde elde ettiğimiz sonuç;

![Mixed_Curve_11](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_11.png)

**Fill Face1** ve **Fill Face2** özelliğini **True (Doğru)** olarak değiştirdiğimizde elde ettiğimiz sonuç ise bu;

![Mixed_Curve_12](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_12.png)

Sol - Ön - Üst İzometrik görünüş;

![Mixed_Curve_13](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_13.png)

Bir örnek daha yaparak konuyu pekiştirelim.  
Ön görünümde iken turkuaz renkli eğriyi çizelim.

![Mixed_Curve_14](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_14.png)

Üst görünümde iken de turuncu renkli eğriyi çizelim.

![Mixed_Curve_15](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_15.png)

Sahneye izometrik bakış açısı ile bakıldığında Eğrilerin görünümü aşağıdaki gibidir.  
Önce **On_Front** ardından **Ust_Top** isimli eskizleri seçip, **Mixed curve** komutunu çalıştıralım.

![Mixed_Curve_16](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_16.png)

Komut sonrası **Mixed_curve** isimli, mavi renkli yeni nesne oluşuyor.

![Mixed_Curve_17](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_17.png)

Unsur ağacından **Mixed curve** nesnesi seçili iken **Fill Face1** özelliğini **True (Doğru)** olarak ayarlayıp yüzey oluşturalım.  
**Mixed_curve** nesnesi oluşturulurken ilk olaran **On_Front** eskizi seçildiği için **Fill Face1** özelliği **True** olarak ayarlandığında, **On_Front** eskizindeki eğri ile, **Mixed_curve** eğrisi arasında kalan bölge doldurularak yüzey oluşturulur.

![Mixed_Curve_18](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_18.png)

Aynı şekilde , Unsur ağacından **Mixed curve** nesnesi seçili iken **Fill Face2** özelliğini **True (Doğru)** olarak ayarlayıp yüzey oluşturduğumzda, **Ust_Top** eskizindeki eğri ile, **Mixed_curve** eğrisi arasında kalan bölge doldurularak yüzey oluşturulur.

![Mixed_Curve_19](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_19.png)

Görüntüyü çevirip (kamera açısını 
değiştirip) şekli incelediğimzde oluşan yüzeyleri daha net görüyoruz.

![Mixed_Curve_20](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_20.png)

Sahneye Ön (Front) bakış açısından 
baktığımızda, ilk çizdiğimiz eğri formunun korunarak yüzey 
oluşturulduğunu görüyoruz.

![Mixed_Curve_21](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_21.png)

Sahneye Üst (Top) bakış açısından 
baktığımızda da, ilk çizdiğimiz eğri formunun korunarak yüzey 
oluşturulduğunu görüyoruz.

![Mixed_Curve_22](../../images/freecad/curves_wb/curves_menu/Mixed_Curve_22.png)

[<<< Curves Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_00_curves_menu.md)
