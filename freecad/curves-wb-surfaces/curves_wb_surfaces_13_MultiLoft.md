Title: FreeCAD - Curves WB - Surface - 13 - MultiLoft 
Date: 2023-04-27 00:00
Modified: 2023-04-28 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, MultiLoft 
Author: Mustafa Halil

# ![multiLoft](../../images/freecad/curves_wb/simgeler/surfaces/MultiLoft.svg) MultiLoft

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

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
