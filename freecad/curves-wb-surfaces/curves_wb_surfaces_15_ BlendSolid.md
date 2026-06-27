Title: FreeCAD - Curves WB - Surface - 15 - BlendSolid
Date: 2023-05-07 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, BlendSolid, Blend, Solid
Author: Mustafa Halil

# ![blendSolid](../../images/freecad/curves_wb/simgeler/surfaces/BlendSolid.svg) BlendSolid

**BlendSolid** komutu, seçili iki yüzeyi, bu yüzeylere ait seçili 2'şer kenarı referans alarak birleştirir. Komut, **Extrude**, **Loft** ve **Sweep** komutlarına benzetilebilir.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir eğri (veya kenar çizgisi) ve yüzey seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **BlendSolid** seçeneğini kullanın.

Sahnede aynı ölçülere sahip iki adet küp nesnesi var. Bu küpler, **Part Çalışma Tezgahı** ile oluşturuldu.  
![BlendSolid_01](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_01.png)  
İlk olarak birinci küpün bir yüzeyini ve seçili yüzeye ait iki kenar çizgisini seçiyoruz.
![BlendSolid_02](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_02.png)  
Ardından ikinci küpün bir yüzeyini ve seçili yüzeye ait iki kenarı seçiyoruz.
![BlendSolid_03](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_03.png)  
Curves araç çubuğunda bulunan **BlendSolid** düğmesi ile ya da **Surface** menüsündeki **BlendSolid** seçeneği ile komutu çalıştırıyoruz.
![BlendSolid_04](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_04.png)  
İşlem sonrası, seçili iki yüzey, seçili kenarlar referans alınarak birleştirildi. Unsur ağacında **Blend_Solid** nesnesi oluştu. Seçili kenarlar birbirine paralel ve aynı düzlemde olduğu için sonuç **Extrude** komutuna benzer bir çıktı verdi.
![BlendSolid_05](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_05.png)  
Küplerden birinin açısını ve konumunu değiştirip sonucu inceleyelim.  
Sahnenin solunda bulunan küpü, **X** eksenin etrafında çevirip **Z** ekseninde yukarı yönde taşıyalım.
![BlendSolid_06](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_06.png)  
**BlendSolid** komutu sonucu elde ettiğimiz **Blend_Solid** unsuru, nesnelerin açısının ve konumunun değişmesi sonucunda yeniden hesaplanarak güncellendi.
![BlendSolid_07](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_07.png)  
**Continuity1** ve **Continuity2** süreklilik değerleri varsayılan olarak **2** atanmış. Bu değeri **0** (sıfır) olarak değiştirirsek, **Blend_Solid** unsuru, eğrisel formunu kaybedip, doğrusal bir hal alır.
![BlendSolid_08](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_08.png)  
**Continuity1** ve **Continuity2** süreklilik değerleri değiştirilerek farklı sonuçlar elde edilebilir.
![BlendSolid_09](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_09.png)  
Küpü biraz da **Y** ekseninde çevirelim.
![BlendSolid_10](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_10.png)  
Sonuç gayet başarılı. Yapılan değişiklik neticesinde, burkulmuş bir cisim elde etmiş olduk.
![BlendSolid_11](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_11.png)  
Küpün ebatlarını (ölçülerini) değiştirelim.
![BlendSolid_12](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_12.png)  
Sahneye sağ yan görünüşten bakıp sonucu inceleyelim.
![BlendSolid_13](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_13.png)  
Küpün açısını ve konumunu ilk değerine geri getirip, ölçüsü değişmiş halde bırakalım.
![BlendSolid_14](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_14.png)  
**BlendSolid** komutunu, bir de **Part Design** Çalışma Tezgahı ile oluşturduğumuz prizmatik nesnelere üzerinde kullanmaya çalışalım.  
Kare ve Dikdörtgen şekiller çizip **Pad** komutu ile kalınlık verdiğimiz küplerin yüzey ve kenarlarını seçip **BlendSolid** komutunu çalıştıralım.
![BlendSolid_15](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_15.png)  
Unsur ağacında **Blend_Solid** unsuru oluştu ancak, sonuç istediğimiz gibi olmadı. **BlendSolid** komutunun çalışması için ilave işlem uygulamamız gerekiyor.
![BlendSolid_16](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_16.png)  
**Part Design** Çalışma Tezgahında oluşturduğumuz Gövde (Body) nesnelerini, **Part** Çalışma Tezgahı komutu yardımıyla **Bileşik (Compound)** hale getiriyoruz. 
![BlendSolid_17](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_17.png)  
**Bileşik (Compound)** komutu düğmesi, araç çubuğunda da mevcut.
![BlendSolid_18](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_18.png)  
Gövde nesnelerini Bileşiğe dönüştürüldükten sonra, yüzey ve kenarları seçerek **BlendSolid** komutunu tekrar çalıştıralım.
![BlendSolid_19](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_19.png)  
Sonuç başarılı. Yüzeylere ait seçili kenarlar, aşağıdaki resimde yeşil renkli olarak görünüyor.
![BlendSolid_20](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_20.png)  
Dikdörtgenler prizmasının açısını değiştirelim.
![BlendSolid_21](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_21.png)  
Burkulmuş doğrusal nesne elde ettik.
![BlendSolid_22](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_22.png)  
Dikdörtgenler prizmasının konumunu da değiştirip **Z** ekseninde yukarı taşıyalım.
![BlendSolid_23](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_23.png)  
Bu kez, burkulmuş eğrisel nesne elde etmiş olduk.
![BlendSolid_24](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_24.png)  
Bir de, dikdörtgen dışındaki şekilleri inceleyelim. Sahneye Dikdörtgenler prizması ile bir Silindir ekleyelim.
![BlendSolid_25](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_25.png)  
Yüzeyleri ve kenarları seçip, **BlendSolid** komutunu çalıştıralım.
![BlendSolid_26](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_26.png)  
Görüldüğü üzere, Unsur ağacında **Blend_Solid** nesnesi oluştu ancak sonuç beklediğimiz gibi olmadı. Unsur ağacında **Blend_Solid** nesnesinde Ünlem işareti olduğuna dikkat edin.
![BlendSolid_27](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_27.png)  
Komutun doğru sonuç vermemesinin, istediğimiz sonucu elde edemememizin sebebi, Silindirin seçili yüzeyine ait sadece bir kenar çizgisi olmasıdır.
![BlendSolid_28](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_28.png)  
Silindirin kesit alanını, bir çember yerine birden fazla (örneğin 4) yay parçası ile oluşturalım.
![BlendSolid_29](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_29.png)  
Silindir nesnesini **Bileşik (Compound)** hale getirelim.
![BlendSolid_30](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_30.png)  
Birer Yüzey ve 2'şer kenar çizgisi seçerek **BlendSolid** komutunu çalıştıralım.
![BlendSolid_31](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_31.png)  
Komut bu kez başarılı sonuç verdi. Seçili kenarlara bağlı olarak Eğrisel bir yapı elde edildi.
![BlendSolid_32](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_32.png)  
**Blend_Solid** nesnesinin **Continuity1** ve **Continuity2** süreklilik değerleri **0** (sıfır) olarak değiştirildiğinde, **Loft** komutuna benzer doğrusal yapı elde edildi.  
**Fuse** parametresi, **false** olarak ayarlandığı için oluşan **Blend_Solid** nesnesi ayrı bir nesne olarak unsur ağacında görüntüleniyor.
![BlendSolid_33](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_33.png)  
Silindirin konumunu ve açısını değiştirip, **Continuity1** ve **Continuity2** süreklilik değerlerini artırdığımızda aşağıdaki sonucu elde ediyoruz.
![BlendSolid_34](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_34.png)  
**Fuse** parametresini, **true** olarak ayarladığımızda **Blend_Solid** nesnesi, bağlantılı olduğu nesnelerle (Dikdörtgenler prizması ve Silindir) birleştirilip tek bir nesne olarak unsur ağacında görüntülenir.
![BlendSolid_35](../../images/freecad/curves_wb/surfaces_menu/BlendSolid_35.png)  

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
