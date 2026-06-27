Title: FreeCAD - Curves WB - Surface - 12 - Reflect Lines 
Date: 2023-03-19 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Reflect, Line
Author: Mustafa Halil

# ![reflectLines](../../images/freecad/curves_wb/simgeler/surfaces/ReflectLines.svg) Reflect Lines

**Reflect Lines (Akis Çizgileri/Eğrileri)**, sahneye olan bakış açısı temel alınarak, seçili nesne(ler)in ya da yüzeylerin dış kontur çizgisini (silüetini) eğriler vasıtası elde etmeye
 yarayan komuttur. **Reflect Line** komutu ile oluşturulan/elde edilen eğriler, **Draft Workbench'te (Taslak Çalışma Tezgahında)** bulunan komutlarla birlikte kullanılabilir. Tarif anlaşılmamış olabilir, komutu uygulayarak anlayalım.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle nesne(ler) veya yüzey(ler) seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Reflect Lines** seçeneğini kullanın.

**Reflect Lines** komutu uygulayarak eğri elde etmek istediğimiz nesne aşağıda görülmektedir.  
![Reflect_Lines_01](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_01.png)  
Unsur ağacından, ilgili nesneyi seçerek **Reflect Lines** komutunu çalıştırıyoruz. Bu algoritma, şeklin **ViewDir** yönündeki izdüşümünü hesaplar.
![Reflect_Lines_02](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_02.png)  
Oluşan Akis/Yansıtma Eğrileri görmek için, Unsur ağacından, ilgili nesneyi (Thickness) seçerek gizliyoruz.  
**Özellikler** panelindeki **Source** parametresi, hangi nesne(ler) ya da yüzey(ler) seçilerek Akis Eğrisi oluşturulduğunu belirtir.
![Reflect_Lines_03](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_03.png)  
**Cleaning Options (Temizlik Seçemekleri)** başlıklı Özellik bölümünde bulunan **Remove Duplicates (Yinelenenleri Kaldır)** parametresi, **true (doğru)** olarak ayarlanırsa, belirtilen **Cleaning Tolerance (Temizleme Toleransı)** değeri ile belirlenen miktardan yakın olan noktalar arasındaki çizgielri/eğrileri siler/temizler.
![Reflect_Lines_04](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_04.png)  
**Edge Type (Kenar Biçimi)** başlıklı Özellik bölümünde bulunan **Out Line** parametresi, nesnenin siluet çizgilerinin ana hatlarıyla **eğrileri** ile çizilmeyeceğini belirttiğimiz kısımdır. Bu parametre **false (yanlış/hayır)** olarak ayarlanırsa, oluşan Akis Çizgilerinin/Eğrilerinin, **eğrisel parçaları** gizlenir. 
![Reflect_Lines_05](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_05.png)  
Yukarıdaki çizimde bu parametrenin sonuçları tam olarak belli olmadı. Bunun için sahneye Eğrisel hatlara sahip yeni bir nesne ekleyerek parametreyi inceleyelim.  
Sahneye bir **Halka** nesnesi ekleyelim, nesneyi seçelim ve **Reflect Lines** komutunu çalıştıralım.
![Reflect_Lines_06](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_06.png)  
**Out Line** parametresi **true (doğru/evet)** iken elde edilen sonuç;
![Reflect_Lines_07](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_07.png)  
**Out Line** parametresi **false (yanlış/hayır)** iken elde edilen sonuç aşağıdadır. Görüldüğü üzere Nesnenin dış hattına (silüetine) ait eğri gizlendi. 
![Reflect_Lines_08](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_08.png)  
**Rg1Line** parametresi, iki yüzey arasındaki **G1-sürekliliğindeki** pürüzsüz kenarı görüntülemek ya da gizlemek için kullanılır.
![Reflect_Lines_09](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_09.png)  
**RgNLine** parametresi, bir yüzeye iliştirilmiş **CN-sürekliliğindeki** kenarı görüntülemek ya da gizlemek için kullanılır.
![Reflect_Lines_10](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_10.png)  
**Sharp** parametresi, keskin kenar (**C0-sürekliliği)** görüntülemek ya da gizlemek için kullanılır. 
![Reflect_Lines_11](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_11.png)  
**Edge Type (Kenar Biçimi)** başlığında bulunan parametrelerinin tamamı **true (doğru/evet)** olarak ayarlanmışken, sahneye **Ön Görünüm (Front)** bakış açısı ile baktığımızda aşağıdaki görüntüyü görürüz.
![Reflect_Lines_12](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_12.png)  
sahneye **Sağ Yan Görünüm (Right)** bakış açısı ile baktığımızda aşağıdaki görüntüyü görürüz.
![Reflect_Lines_13](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_13.png)  
Sahneye **Sol-Ön-Üst (Left-Front-Top)** bakış açısı kesişimi olan köşeden baktığımızda aşağıdaki görüntüyü görürüz.  
Dikkat ettiyseniz şu ana kadar **Reflect Lines** başlıklı özellik kısmında **On Shape** parametresi sürekli **true (doğru/evet)** olarak ayarlanmıştı. Bu sayede **Reflect Lines** komutu sonrası elde edilen Akis Çizgileri/Eğrileri 3 boyutlu (3B) olarak elde edilmiş oldu. Tam olarak aynı şey olmasa da, komut sonrası Nesne, Wireframe (Tel Kafes) görünümünde görüntülenmiş gibi bir sonuç elde edilir.
![Reflect_Lines_14](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_14.png)  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlandığında Akis eğrileri, **XY düzleminde** oluşturulur. Yani sonuç 2 Boyutlu (2B) bir yapıya sahiptir. XY Düzlemine dik açıdan (düzlemin Normal doğrultusundan) yani **Üst Görünümden** bakıldığında gerçek sonuç görüntülenir. Bu komut, **TechDraw**'a geçmeden (OnShape özelliği devre dışı bırakıldığında) bir nesnenin 2B görünümünü elde etmek için kullanılabilir. 
![Reflect_Lines_15](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_15.png)  
Sahneye Üst Görünümden (Top) baktığımızda, doğru görüntüyü elde etmiş oluyoruz.  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlandığında (ReflectLines XY düzleminde olduğunda), **ViewPos** ve **UpDir** özellikleri kullanılabilir. Bu durumda, Akis Çizgilerinin Konumunun ve Yöneliminin ayarlanmasına izin verilir.
![Reflect_Lines_16](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_16.png)  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlandığında, sahneye **Sağ Yan Görünümden (Right)** bakıldığında görülen şekil aşağıdaki gibidir. Akis Eğrilerinin 2 boyutlu (2B) olduğu net olarak görünüyor.
![Reflect_Lines_17](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_17.png)  
Sahneye Ön Görünümden (Front) bakıldığında görülen şekil aşağıdaki gibidir. Akis/Yansıma Eğrilerinin 2 boyutlu (2B) olduğu net olarak görünüyor.
![Reflect_Lines_18](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_18.png)  
Sahnede **X, Y, Z eksen çizgilerini** göstererek **Thickness** nesnesinin, orijin (0,0,0) noktasına göre nasıl bir konumda olduğuna bakalım. Görüyoruz ki **Thickness** nesnesi temelde, orijin noktasına altıgen şekil çizilip bir yol boyunca süpürülerek (Sweep komutu ile) elde edilmiş. Yani **Thickness** adındaki altıgen boru/kanalın bir ucu tam olarak orijin (0,0,0) noktasında bulunuyor.
![Reflect_Lines_19](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_19.png)  
**On Shape** parametresi **false (yanlış/hayır)** olarak ayarlanıp sahneye **Üst Görünümden (Top)** bakıldığında **View Pos** parametre değerleri [42,80 31,79 17,80] olarak görünmektedir. Bu değerler **Thickness** nesnesi XY düzlemine 2B olarak dönüştürüldüğünde orijinin bulunduğu koordinatları göstermektedir. 
![Reflect_Lines_20](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_20.png)  
**View Pos** değerlerini değişirilerek nesnenin konumunu (orijin noktasını hareket ettirerek) farklı noktaya taşıyabiliriz. Örneğin Nesnenin orijin noktasını (0,0,0) noktasına 
taşıyalım.
![Reflect_Lines_21](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_21.png)  
**View Dir (Kamera/Bakış Açısı Yönü/Doğrultusu)** parametre değerleri, **Reflect Lines (Akış Eğrileri)** oluşturulurken sahneye hangi bakış açısından (kamera yönünden) ve 
mesafesinden bakıldığına dair koordinat değerlerinin belirlendiği ve ayarlandığı kısımdır.
![Reflect_Lines_22](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_22.png)  
3 boyutlu **Thickness** nesnesi **Reflect Lines** komutu ile Akış/Yansıtma Eğrilerine dönüştürülmeden önce kamera görünümü (bakış açısı) aşağıdaki resimde görüldüğü gibi **Sol-Ön-Üst (Left-Front-Top)** kesişim noktalarında idi (Gezinme Küpüne bakabilirsiniz). Bu açı, kabaca (1, -1, 1) değerlerine karşılık gelir. Nesneye olan yaklığa bağlı olarak bu değer aynı oranda artar ya da azalır. İncelediğimizde kamera 
konumunun (0,58 -0,58 0,58) koordinatlarında iken Akış/Yansıtma Eğrileri
 oluşturulduğunu görüyoruz.
![Reflect_Lines_23](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_23.png)  
**Üst Görünümde (Top)** iken **Thickness** nesnesinin ve Akış/Yansıtma Eğrisinin görüntüsü aşağıdaki gibidir. Yani kamera konumunun (0,58 -0,58 0,58) koordinatlarında iken Akış/Yansıtma Eğrileri oluşturuldu ve XY Düzlemine ektarıldı.
![Reflect_Lines_24](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_24.png)  
Sahneye aşağıdaki şekilde yani örnek kamera koordinatı (1,00 1,00 1,00) ya da katları ile bakmış olsaydık ve **Reflect Lines** komutunu çalıştırarak Akış/Yansıtma Eğrisi oluştursaydık nasıl bir sonuç elde ederdik artık biliyorsunuz.
![Reflect_Lines_25](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_25.png)  
Madem kamera konumuna (bakış açısına) ait X, Y ve Z koordinatları pozitif yönlü, o zaman biz de **View Dir** parametre değerlerini pozitif olarak değiştirelim.
![Reflect_Lines_26](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_26.png)  
**Up Dir (Yukarı Yön Doğrultusu)** parametre değerleri ise, Akış/Yansıtma Eğrisi oluştururken hangi koordinatların Yukarı Yönü gösterdiğini belirlediğimiz değerlerdir. X ve Y koordinatlarını sıfırlar ve sadace Z koordinatını pozitif bir değer belirleyerek istediğimizi elde edebiliriz.  
Aşağıdaki resimde görüldüğü üzere, bir defa oluşturulan Akış/Yansıtma Eğrisine ait parametrele değerleri değiştirilerek Temel nesnenin farklı doğrultu ve mesafelerindeki görüntüleri yeniden oluşturulabiliyor/güncellenebiliyor.
![Reflect_Lines_27](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_27.png)  
**Visible (Görünürlük))** parametresi, Akış/Yansıtma Eğrisi oluşturulurken NSeçili Nesnenin Kamera tarafından Görünen ya da Görünmeyen çizgilerin temel alınacağını belirlediğimiz ayar kısmıdır.  
Unsur ağacından **ReflectLines** nesnesi seçilir ve **Visible (Görünürlük))** parametresi **false (yanlış/hayır)** olarak değiştirilirse aşağıdaki resimde göründüğü gibi bir önceki 
haline kıyasla görünür çizgiler kaybolur, görünmeyen çizgiler görünür hale gelir.
![Reflect_Lines_28](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_28.png)  
Aynı nesnenin bir adet Akis çizgisi oluşturalım ve **Visible (Görünürlük))** parametresi **true (doğru/evet)** olarak ayarlayalım. Rengini turkuaz olarak belirleyelim.
![Reflect_Lines_29](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_29.png)  
Aynı nesnenin bir adet daha Akis çizgisini oluşturalım ve **Visible (Görünürlük))** parametresi **false (yanlış/hayır)** olarak ayarlayalım. Rengini de pembe olarak belirleyelim.
![Reflect_Lines_30](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_30.png)  
Her iki Akis Çizgisinin **On Shape** parametresi **true (doğru/evet)** olarak ayarlandıüğı için eğriler 3 boyutlu oluşmuş olacaktır.
![Reflect_Lines_31](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_31.png)  
Sahneye farklı açılardan bakarsak ta eksik/kayıp bir çizgi kalmamış olduğunu görürüz.
![Reflect_Lines_32](../../images/freecad/curves_wb/surfaces_menu/Reflect_Lines_32.png)  

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
