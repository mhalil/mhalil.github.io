Title: FreeCAD - Curves WB - Surface - 09 - Gordon surface
Date: 2023-03-14 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Gordon
Author: Mustafa Halil

# ![gordon](../../images/freecad/curves_wb/simgeler/surfaces/GordonSurface.svg) Gordon surface

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
