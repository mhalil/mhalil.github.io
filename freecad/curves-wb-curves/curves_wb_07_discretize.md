Title: FreeCAD - Curves WB - Curves - 07 - Discretize
Date: 2022-11-20 00:00
Modified: 2023-03-25 00:00
Category: Curves WB - Curves
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Discretize
Author: Mustafa Halil

# ![Curves_Discretize](../../images/freecad/curves_wb/simgeler/curves/Discretize.svg) Discretize:

**Discretize** komutu, sahneye seçili çizgi ya da eğri boyunca, belirlenen parametre değerlerine göre noktalar ekler.  
Eklenen noktaların sayısı ve noktalar arası mesafe, seçilen **Algoritma** türü ve bu algoritmaya ait parametre değerlerine göre oluşacaktır.

**Kullanım:** Komutu çalıştırmak için aşağıdaki işlemleri sırasıyla uygulayın:

- Öncelikle Kenar ya da Eğriyi/Teli seçin.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves** menüsündeki **Discretize** seçeneğini kullanın.

![Discretize_01](../../images/freecad/curves_wb/curves_menu/Discretize_01.png) Komut çalıştrıldıktan sonra seçili eğri üzerinde **Varsayılan** olarak **Number (Sayı)** algoritması ile **100** adet nokta oluşturulur.
 ![Discretize_02](../../images/freecad/curves_wb/curves_menu/Discretize_02.png) **Number (Sayı)** parametresi 50 olarak değiştirildiğinde, oluşan nokta sayısı ve noktalar arası mesafe, güncellenir.
 ![Discretize_03](../../images/freecad/curves_wb/curves_menu/Discretize_03.png) **Discretize** komutunu, sadece **Curves** Çalışma tezgahında oluşturulan çizgi ve eğrilerle değil, **Sketch (Eskiz) / Draft (Taslak), ...vb** çalışma tezgahları komutlarıyla oluşturulan öğelere de uygulanabilir.
 ![Discretize_04](../../images/freecad/curves_wb/curves_menu/Discretize_04.png) **Sketch (Eskiz)** çalışma tezgahında çizdiğimiz Bezier eğrisini seçip **Discretize** komutunu çalıştıralım.
 ![Discretize_05](../../images/freecad/curves_wb/curves_menu/Discretize_05.png) **Varsayılan** olarak **Number (Sayı)** algoritması ile **100** adet nokta oluşturuldu.
 ![Discretize_06](../../images/freecad/curves_wb/curves_menu/Discretize_06.png) **Number (Sayı)** parametresini **300**'e yükseltirsek, toplam 300 adet nokta yani daha yüksek çözünürlüklü bir nokta blutu elde etmiş olduk.
 ![Discretize_07](../../images/freecad/curves_wb/curves_menu/Discretize_07.png) **QuasiNumber** parametresi, **Number** parametresine benzer bir sonuç veriyor. Belki farklı eğri tiplerinde 
fark daha net anlaşılabilir ancak bu örnekteki eğride her iki algoritma 
da çok yakın sonuç verdi.
 ![Discretize_08](../../images/freecad/curves_wb/curves_menu/Discretize_08.png) **Distance (Mesafe)**, noktalar arası mesafe değerlerini belirterek nokta yapısı oluşturan bir algoritma türüdür.
 ![Discretize_09](../../images/freecad/curves_wb/curves_menu/Discretize_09.png) **Distance (Mesafe)** parametresi **10,00** iken, eğri şekline uygun olarak ortalama **10 mm** aralıklı noktalar oluşturuldu.
 ![Discretize_10](../../images/freecad/curves_wb/curves_menu/Discretize_10.png) **Distance (Mesafe)** parametresi **3,00** olarak değiştiğinde, ortalama **3 mm** aralıklı noktalar oluşturuldu/ güncellendi.
 ![Discretize_11](../../images/freecad/curves_wb/curves_menu/Discretize_11.png) **Deflection** Algoritması, noktalar arası doğruluğun sapma/bozulma derecesine göre nokta elde edilmesini sağlayan algoritma türüdür.  
**Deflection** parametresi **0,10** iken elde edilen nokta yapısı aşağıdadır.
 ![Discretize_12](../../images/freecad/curves_wb/curves_menu/Discretize_12.png) **Deflection (Sapma)** parametresi **0,50** olarak değiştirildiğinde, daha yüksek sapma değerine müsade edilerek daha az sayıda nokta oluşturulması sağlanır.
 ![Discretize_13](../../images/freecad/curves_wb/curves_menu/Discretize_13.png) **Deflection (Sapma)** parametresini **1,00** olarak değiştirelim ve oluşan noktaları **parametrik çizgi**ler ile birleştirelim.
 ![Discretize_14](../../images/freecad/curves_wb/curves_menu/Discretize_14.png) Noktalar **Parametrik çizgi**ler ile birleştirildikten sonra, **Deflection (Sapma)** parametresi tekrar **0,50** olarak değiştirildiğinde, noktaların sayısı ve oluşturulma sırasının nasıl değiştiğini aşağıdaki resimde görebilirsiniz.
 ![Discretize_15](../../images/freecad/curves_wb/curves_menu/Discretize_15.png) **QuasiDeflection** algoritması da **Deflection (Sapma)** algoritmasına benzer bir yapıya sahiptir.  
**Deflection (Sapma)** parametresi **0,01** iken elde edilen nokta yapısı aşağıdadır.
 ![Discretize_16](../../images/freecad/curves_wb/curves_menu/Discretize_16.png) **Deflection (Sapma)** parametre değeri **0,10** olarak değiştiğinde elde edilen nokta yapısı aşağıdaki gibi daha düşük çözünürlüklü oluyor.
 ![Discretize_17](../../images/freecad/curves_wb/curves_menu/Discretize_17.png) **Angular-Curvature (Açısal-Eğrilik)** algoritması, bir diğer algoritma seçeneğidir.  
Bu algoritma yapısında **Açısallık (Angular), Eğrilik (Curvature)** ve **En az nokta sayısı (Minimum)** parametreleri belirtilerek nokta yapısı oluşturulur.  
Parametre değerleri aşağıdaki şekilde belirtildiğinde elde edilen sonuç aşağıda mevcuttur.  
*Açısallık (Angular): 0,10  
Eğrilik (Curvature): 0,10  
En az nokta sayısı (Minimum) : 2* ![Discretize_18](../../images/freecad/curves_wb/curves_menu/Discretize_18.png) **Açısallık (Angular)** Parametre değeri aşağıdaki şekilde değiştirildiğinde elde edilen sonuç aşağıda mevcuttur.  
*Açısallık (Angular): 2,00  
Eğrilik (Curvature): 0,10  
En az nokta sayısı (Minimum) : 2* ![Discretize_19](../../images/freecad/curves_wb/curves_menu/Discretize_19.png) **Eğrilik (Curvature)** Parametre değeri aşağıdaki şekilde değiştirildiğinde elde edilen sonuç aşağıda mevcuttur.  
*Açısallık (Angular): 2,00  
Eğrilik (Curvature): 1,00  
En az nokta sayısı (Minimum) : 2* ![Discretize_20](../../images/freecad/curves_wb/curves_menu/Discretize_20.png)

[<<< Curves Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_00_curves_menu.md)
