Title: FreeCAD - Curves WB - Surface - 01 - ZebraTool
Date: 2023-02-10 00:00
Modified: 2023-04-30 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, ZebraTool
Author: Mustafa Halil

# ![zebra](../../images/freecad/curves_wb/simgeler/surfaces/ZebraTool.svg) ZebraTool

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
