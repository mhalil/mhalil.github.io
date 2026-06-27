Title: FreeCAD - Curves WB - Surface - 05 - Sweep2Rails
Date: 2023-02-19 00:00
Modified: 2023-05-07 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Sweep2Rails, Sweep, Rail
Author: Mustafa Halil

# ![sw2r](../../images/freecad/curves_wb/simgeler/surfaces/Sweep2Rails.svg) Sweep2Rails

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
