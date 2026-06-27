Title: FreeCAD - Curves WB - Surface - 16 - Flatten face
Date: 2024-04-19 22:15
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Flatten Face, Flat, Flatten, Face
Author: Mustafa Halil

# ![Flatten_face](../../images/freecad/curves_wb/simgeler/surfaces/FlattenFace.svg) Flatten face

**Flatten face** (Düzlemsel Yüzey) komutu, Konik (Kesik koni olmalı, uç kısım sivri olmamalı) ve Silindirik yüzeylerden düz gelişmiş bir yüzey oluşturur. Seçili Yüzeyin UV'sini açar diyebiliriz. Başka bir ifadeyle, seçili yüzeyin düzlemsel haleni üretir.

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle bir kesik koni yüzeyi veya silindir yüzeyi seçin. 
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Flatten face** seçeneğini kullanın.

Model üzerinden düzleştirmek / UV açılımını yapmak istediğimiz konik ya da silindrik yüzeyi seçiyoruz. Araç çubuğunda bulunan **Flatten face** düğmesine basıyoruz. **Surface** menüsündeki **Flatten face** seçeneğini de kullanabiliriz.
![Flatten_face_01](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_01.png)

Komut çalıştırıldıktan sonra 3D ekranında, seçili yüzey ile temas edecek şekilde, yüzeyin UV açılımı yapılır. Oluşan Yeni Nesne (Flatten) kaynak (seçili) yüzeye teğet olacak şekilde yerleştirilir.
![Flatten_face_02](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_02.png)

Oluşan yeni nesneyi (Flatten), Unsur ağacından seçerek **In Place** ayarını **False** olarak değiştirdiğimizde, **Flatten** nesnesi **XY düzleminde** taşınır.
![Flatten_face_03](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_03.png)

Sahneye, üst görünüşten **XY düzleminden** baktığımzda **Flatten** nesnesini net olarak görebiliriz.
![Flatten_face_04](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_04.png)

Silindrik bir başka yüzeyi seçip **Flatten face** komutunu tekrar çalıştıralım.
![Flatten_face_05](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_05.png)

Oluşan Yeni Nesne (Flatten), varsayılan olarak kaynak yüzeye teğet olacak şekilde yerleştiriliyor. Dikkat ederseniz bu kez oluşan Flatten Nesnesi sadece çizgilere değil aynı zamanda yüzeye de sahip. (*Flatten face nesenesinin neden çizgiden ya da yüzeyden oluştuğunun sebebini bilemiyorum.*)
![Flatten_face_06](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_06.png)

Oluşan **Flatten001** nesnesini seçip extrude komutu ile katılamak mümkün.
![Flatten_face_07](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_07.png)

Komutu, bir diğer çizim üzerinde de deneyelim. Silindrik bir yüzey seçip komutu çalıştırıyorum.
![Flatten_face_08](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_08.png)

Sonuç ortada;
![Flatten_face_09](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_09.png)

Oluşan Yeni Nesne (Flatten) kaynak yüzeye teğet olacak şekilde (YZ Düzlemine) yerleştirildi.
![Flatten_face_10](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_10.png)

**Flatten** nesnesini seçip **Draft Çalışma Tezgahı**ndaki **Downgrade** komutu ile tüm parçaları **Edge (Kenar çizgisi)** haline dönüştürdük. 
![Flatten_face_11](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_11.png)

Tüm kenar çizgilerini (edge) seçip **Upgrade** komutunu çalıştırarak seçili çizgilerden temas halinde olanları **Wire (kablo çizgisi)** nesnesine dönüştürüyoruz.
![Flatten_face_12](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_12.png)

İç kısımdakiler hariç, kablo çizgisini (Wire) seçip **Upgrade** komutu ile seçimi **yüzey nesnesine** dönüştürüyoruz.
![Flatten_face_13](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_13.png)

Aynı işlemi, iç kısımdaki kablo çizgilerine de (wire'lara) uygulayarak yeni yüzeyler elde ediyoruz. **Part Çalışma Tezgahı**ndaki **Kes (Cut)** komutu yardımıyla Yüzeyleri birbirinden çıkararak boşluk oluşturuyoruz.
![Flatten_face_14](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_14.png)

Boşluklu düzlemsel Yüzeyi seçerek **Part Çalışma Tezgahı**ndaki **Uzat / Katıla (Extrude)** komutunu çalıştırıyoruz.
![Flatten_face_15](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_15.png)

Sonuç olarak Düzlemsel nesneye **hacim** kazandırarak nesneyi **3. boyut**a kavuşturuyoruz.
![Flatten_face_16](../../images/freecad/curves_wb/surfaces_menu/Flatten_face_16.png)

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
