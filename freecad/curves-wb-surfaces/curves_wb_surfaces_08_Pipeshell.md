Title: FreeCAD - Curves WB - Surface - 08 - Pipeshell 
Date: 2023-02-28 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Pipeshell 
Author: Mustafa Halil

# ![pipeshell](../../images/freecad/curves_wb/simgeler/surfaces/Pipeshell.svg) Pipeshell

**Pipeshell** komutu, **Parça Çalışma Tezgahı (Part WB)** ve **Parça Tasarımı Çalışma Tezgahı (Part Desing WB)** komutlarından olan **Süpür/Borula (Sweep/AddivitePipe)** ve **Çatıla (Loft)** komutlarına benzer şekilde bir yol boyunca **seçili kesit alanını süpürerek yüzey oluşturur**. Komut kabaca, Sweep ve Loft komutlarının birer benzeridir diyebiliriz.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle **3D Ekranı içerisinden (sahneden)** süpürülecek yol (eğri, yay, çizgi, ...vb) seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Ardından **Unsur ağacından**, (sahne içerisinden seçmemelisiniz) **Pipeshell profile** komutu ile oluşturulmuş kesitleri seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Pipeshell** seçeneğini kullanın.

**3D Ekranı içerisinden** yolu (eğri, yay, çizgi, ...vb) seçin. Daha sonra **Unsur ağacından**, (sahne içerisinden değil) **Pipeshell profile** komutu ile oluşturulmuş kesitleri (profilleri) seçin ve **Pipeshell** komutunu çalıştırın.
![Pipeshell_01](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_01.png)  
**Pipeshell** komutu çalıştırılınca aşağıdaki şekil oluştu. Yani seçili Yol boyunca, Kesitler (Profiller) arasına yeni kesitler ebatları nispetinde eklendi. 
![Pipeshell_02](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_02.png)  
Unsur ağacından **Pipeshell** nesnesi seçilip **Output (Çıktı/Ürün/Sonuç)** seçeneği **Surface (Yüzey)** olarak ayarlanırsa, aşağıdaki şekli elde ederiz.
![Pipeshell_03](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_03.png)  
Yüzeye dönüştürülen çizimin arka kısmında bir bozukluk olduğunu görüyoruz.
![Pipeshell_04](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_04.png)  
Görüntüyü çevirip modeli incelediğimizde, Son Kesitin (profilin) başlangıç noktasının, diğer profillerden farklı yönde olduğunu tespit ediyoruz. Yüzey oluşturulurken, profillerin noktaları referans alındığı için, modelin son kısımda bir bozulma yaşanmış. Gelin bu bozukluğu düzeltelim.
![Pipeshell_05](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_05.png)  
Bozulmanın yaşandığı kesit (profil), **Sketch004** eskizi referans alınarak oluşturulduğu için, bu eskizde yapacağımız düzenleme, Profili de etkileyecek, düzeltecektir.  
Unsur ağacından **Sketch004** eskizini seçip, **Attachment** ayarlarından **Açı** değerini inceliyoruz.
![Pipeshell_06](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_06.png)  
**Sketch004** eskizinin, **Attachment** ayarındaki **Açı** değerini **180** olarak değiştirerek, eskizi kendi merkezindeki Z ekseninde 180 derece döndürüyoruz. Gördüğünüz gibi, modeldeki bozulma düzeliyor ve istediğimiz / beklediğimiz sonucu elde ediyoruz. Bazen, bozulmanın olduğu eskizi düzenleme modunda açıp değiştirerek te benzer sonuç elde edebiliyoruz. Dairesel kesitli eskizlerde yukarıda uyguladığımız yöntemin (ayarlarda değişiklik yapmak) daha uygun olduğu kanaatindeyim.
![Pipeshell_07](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_07.png)  
[**Pipeshell profile**](https://mhalil.github.io/Freecad_curves_wb_surfaces.html#pipeshellprofile) komutu anlatılırken çizdiğimiz farklı kesitlere ait örnek çalışmaların **Pipeshell** komutu ile yüzeye dönüştürülmüş hallerini aşağıda görüp inceleyebilirsiniz.
![Pipeshell_08](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_08.png)  
![Pipeshell_09](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_09.png)  
![Pipeshell_10](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_10.png)  
![Pipeshell_11](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_11.png)  
![Pipeshell_12](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_12.png)  
![Pipeshell_13](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_13.png)  
![Pipeshell_14](../../images/freecad/curves_wb/surfaces_menu/Pipeshell_14.png)  

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
