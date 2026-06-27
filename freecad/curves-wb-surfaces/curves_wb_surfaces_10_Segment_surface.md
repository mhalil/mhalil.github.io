Title: FreeCAD - Curves WB - Surface - 10 - Segment surface
Date: 2023-03-16 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface,Segment
Author: Mustafa Halil

# ![segment_surface](../../images/freecad/curves_wb/simgeler/surfaces/SegmentSurface.svg) Segment surface

**Segment surface** komutu, seçili yüzeyi yatay, düşey ya da her iki yönde parçalara bölmek/ayırmak için kullanılır.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir yüzey seçin.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Segment surface** seçeneğini kullanın.

Parçaya parçalamak/bölmek istediğimiz yüzey, aşağıdaki resimde görülmektedir.  
![Segment_Surface_01](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_01.png)  
Öncelikle bölünmek istenilen Yüzey seçilmeli ardından **Segment surface** komutu çalıştırılmalı.
![Segment_Surface_02](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_02.png)  
Komut çalıştırıldıktan sonra elde edilen sonuç aşağıda görülmektedir.
![Segment_Surface_03](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_03.png)  
Unsur ağacından **Segment_Surface** öğesini seçip, komuta ait ayarları inceleyelim.  
**Option (Seçenek)** özelliği, **Auto (Otomatik)** iken **Option Auto** ayarı altındaki **Direction (Yön / Yönelim)** seçeneği **U** olarak seçildiğinde, seçili yüzey **U** yönünde otomatik olarak bölümlendi/parçalara ayrıldı.
![Segment_Surface_04](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_04.png)  
**Option Auto** ayarı altındaki **Direction (Yön / Yönelim)** seçeneğini **V** olarak değiştirdiğimizde, seçili yüzey **V** yönünde otomatik olarak bölümlendi/parçalara ayrıldı.
![Segment_Surface_05](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_05.png)  
**Direction (Yön / Yönelim)** seçeneğini **Both (Her ikisi)** olarak değiştirirsek, tahmin edeceğiniz üzere, seçili yüzey hem **U** hemde **V** yönünde (ızgara şeklinde) otomatik olarak bölümlenir/parçalara ayrılır.
![Segment_Surface_06](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_06.png)  
**Option (Seçenek)** özelliği, **Custom (Özel)** olarak değiştirildiğinde, **Option Custom (Özel'in Seçenekleri)** isimli yeni özellikler paneli karşımıza çıkıyor.
![Segment_Surface_07](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_07.png)  
İlk olarak **Knots U** özelliğini inceleyelim.  
**Knots U** seçeneği, **U** yönünde noktalar belirtmemizi ve yüzeyi bu noktalara göre parçalara ayırmamızı sağlar.  
Unsur ağacından **Segment_Surface** öğesini seçiliyken özellikler panelinden **Knots U** seçeneğinin yanındaki butona tıklayın.
![Segment_Surface_08](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_08.png)  
Karşımıza çıkan **List (Liste)** diyalog kutusuna, her satıra bir değer yazmak kaydı ile 0 (sıfır) ile 1 (bir) arasında değerler yazın.  
Burada bahsedilen 0 (sıfır) ve 1 (bir) değeri yüzeyi, bölmek için belirtilecek yüzdelik değerlerdir. (örneğin 0.5 değeri %50 yani tam ortadan böl anlamına gelmektedir.)  
Örnek olarak **0.1** ve **0.5** değerlerini yazalım.  
**NOT:** Ondalık değerleri yazarken, virgül kullanılmamalıdır. Ondalık ayırıcı olarak (Python programlama dilinde olduğu gibi) **Nokta** karakteri kullanılmalıdır. (Python'da virgül karakteri, parametreleri ayırmak için kullanılır.)
![Segment_Surface_09](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_09.png)  
Görüldüğü üzere, seçil yüzey **U** yönünde %10 ve %50 mertebesinden kesilerek 3 yüzeye bölündü.
![Segment_Surface_10](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_10.png)  
Yüzeyi **V** yönünde de %25 ve %65 oranından keselim.
![Segment_Surface_11](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_11.png)  
Sonuç aşağıda görülüyor. **Knots U** ve **Knots V** değerleri değiştirildiğinde yüzey otomatik olarak yeni değerlere göre bölümlenecektir.
![Segment_Surface_12](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_12.png)  
Üst görünüşten bakarak kesim oranları daha net görüntülenebilir.
![Segment_Surface_13](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_13.png)  
**Segment_Surface** öğesinin **Option Custom (Özel'in Seçenekleri)** özelliğinin **Knots U** ve **Knots V** seçeneklerinin farklı bir kullanımını daha görelim.  
Bunun için sahneye öncelikle bir silindir ekliyoruz ve yarıçapını 1.00 mm olarak belirtiyoruz.
![Segment_Surface_14](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_14.png)  
Silindir yüzeyini seçerek **Surface** menüsündeki **Segment surface** komutunu çalıştırıyoruz.
![Segment_Surface_15](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_15.png)  
Silindir nesnesini gizliyoruz ve oluşan Segment Yüzeyini görüyoruz.
![Segment_Surface_16](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_16.png)  
**Option (Seçenek)** özelliği, **Custom (Özel)** olarak değiştiriyoruz.
![Segment_Surface_17](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_17.png)  
**Knots U** değerini 3.14 olarak belirtiyoruz. Bu işlem sonrası yüzey **U** yönünde tam ortadan ikiye bölünüyor.  
Bunun sebebini açıklamak gerekirse;  
Yüzeyi oluşturan Çemberin yarıçapı 1.00mm olduğu için çemberin çevre uzunluğu (2*pi*r formülü ile hesaplandığında) 6.28mm olmaktadır. 
Doğal olarak 3.14 değeri uzunluğun yarısına tekabül ettiği için yüzey yam ortadan ikiye bölünüyor.
![Segment_Surface_18](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_18.png)  
**Knots U** değerini aşağıdaki resimde gösterildiği şekilde revize ettiğimizde ise yüzey (neredeyse) 4 eşit parçaya bölünmüş oluyor.
![Segment_Surface_19](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_19.png)  
Sonuca dair görüntü;
![Segment_Surface_20](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_20.png)  
**Segment_Surface** öğesinin **Option Custom (Özel'in Seçenekleri)** özelliğinin bir diğer seçeneği olan **Knots UProvider** ve **Knots VProvider** 'ı inceleyelim.  
Bunun için öncelikle, oluşturduğumuz Silindir nesnesine ait bir çemberi seçelim ve ardından **Curve** menüsünden **Discretize** komutunu çalıştıralım.
![Segment_Surface_21](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_21.png)  
Komut sonrasında, seçili çember boyunca eşit aralıklı 100 adet nokta oluşturuldu.
![Segment_Surface_22](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_22.png)  
Silindiri ve Segment Yüzeyini gizleyerek, **Discretize** komutunu ile oluşturulan noktaları inceleyelim.
![Segment_Surface_23](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_23.png)  
Segment Yüzeyi görüntüleyelim ve **Discretize** komutunu ile oluşturulan noktaların sayısını **6** olarak değiştirelim. Böylece, çember çevre uzunluğu boyunca eşit aralıklı **6** adet nokta elde etmiş olduk.
![Segment_Surface_24](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_24.png)  
**Segment_Surface** öğesinin **Option Custom (Özel'in Seçenekleri)** özelliğinin **Knots UProvider** seçeneğini kullanarak oluşturduğumuz 6 noktayı değer olarak atayalım.
![Segment_Surface_25](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_25.png)  
Butona basınca karşımıza çıkan **Bağlantı (Link)** penceresinden, **6** noktaya ait öğeyi (Discretize_Edge) seçip ardından OK (Tamam) butonuna basıyoruz.
![Segment_Surface_26](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_26.png)  
İşlem sonrası seçili yüzey, belirlenen öğedeki (Discretize_Edge) nokta sayısı ve konumundan parçalara ayrılıyor.
![Segment_Surface_27](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_27.png)  
Unsur ağacından **Discretized_Edge** öğesi seçilerek **Number (Sayı)** değeri **10** olarak değiştirildiğinde/güncellendiğinde, Segment Yüzeyi **U** yönünde **10** eşit parçaya bölünüyor.
![Segment_Surface_28](../../images/freecad/curves_wb/surfaces_menu/Segment_Surface_28.png)  

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
