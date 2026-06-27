Title: FreeCAD - Curves WB - Surface - 06 - Profile support plane
Date: 2023-02-26 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Profile, support, plane
Author: Mustafa Halil

# ![profileSupport](../../images/freecad/curves_wb/simgeler/surfaces/ProfileSupport.svg) Profile support plane

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
