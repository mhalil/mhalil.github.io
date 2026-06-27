Title: FreeCAD - Curves WB - Curves - 06 - Split curve
Date: 2022-11-18 00:00
Modified: 2023-02-18 00:00
Category: Curves WB - Curves
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Split, curve
Author: Mustafa Halil

# ![Curves_SplitCurve](../../images/freecad/curves_wb/simgeler/curves/Split_curve.svg) Split curve:

**Split curve** komutu, <u>Seçili eğri(ler)i / kenar(lar)ı parçalara ayırır.</u>  

**Kullanım:** Komutu çalıştırmak için aşağıdaki işlemleri sırasıyla uygulayın:

- Öncelikle, parçalara ayırmak istediğiniz kenarı/eğriyi ya da kenarları/eğrileri seçin.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves** menüsündeki **Split curve** seçeneğini kullanın.

![Split_curve_01](../../images/freecad/curves_wb/curves_menu/Split_curve_01.png)  
Seçili Eğri, istenilen kısımlardan 
parçalar ayrılabilir. Kısımlar, komut çalıştırıldıktan sonra **Özellikler** bölümündeki **Veri** sekmesinden ayarlanır. Varsayılan değer **50%** yani eğrinin tam ortasından bölünmesidir. 
![Split_curve_02](../../images/freecad/curves_wb/curves_menu/Split_curve_02.png)  
**Split curve** komutu ile bölünen eğriye, unsur ağacında çift tıklayarak düzenleme moduna girilebilir (düzenleme modunda unsur sarı renkli olarak gösterilir) ve bölüm/ayrım noktası, fare yardımıyla eğri üzerinde hareket ettirerek konumu değiştirilebilir.  
![Split_curve_03](../../images/freecad/curves_wb/curves_menu/Split_curve_03.png)  
![Split_curve_04](../../images/freecad/curves_wb/curves_menu/Split_curve_04.png)  
Bölme/Parçalama kısımlarını 
ayarlamak için başka bir yöntem de, aşağıdaki adımları uygulamaktır;

- **Unsur ağacı**ndan SplitCurve unsuru seçilir
- Özellikler Panelindeki **Split (Böl)** başlığı altında bulunan **Values (Değerler)** İletişim kutusu açılarak her satıra istenilen değerler yazılır.

![Split_curve_05](../../images/freecad/curves_wb/curves_menu/Split_curve_05.png)  
Eğrileri, sayısal değer belirterek 
parçalara ayırmanın dışında, diğer eğrilerle/kenarlarla kesiştiği 
noktalardan parçalara ayırmak ta mümkün. Şimdi, 4 eğriyi seçerek, 
kesişme noktalarından bölmeye/ayırmaya çalışalım.
 ![Split_curve_06](../../images/freecad/curves_wb/curves_menu/Split_curve_06.png)  
Parçalara ayırmak istediğimiz 4 eğriyi seçtik ve **Split curve** komutunu çalıştırdık.
 ![Split_curve_07](../../images/freecad/curves_wb/curves_menu/Split_curve_07.png)  
Split curve komutu uygulanan eğrilerden biri seçilir ve **Özellikler** panelindeki **Split** başlığı altındaki **Values (Değerler)** kısmınaki sayısal veriyi silelim (köşeli parantezi silmeyin.) **Cutting Objects (Kesim Nesneleri)** seçeneğinin sağındaki **üç nokta** `...` butonuna basalım.
 ![Split_curve_08](../../images/freecad/curves_wb/curves_menu/Split_curve_08.png)  
Açılan **Link** 
başlıklı diyalog kutusu, Unsur ağacındaki nesneleri görüntüleyecektir. 
Seçili eğriyi, hangi eğrileri kullanarak bölmek istiyorsak, o eğrileri 
seçmeliyiz.
 ![Split_curve_09](../../images/freecad/curves_wb/curves_menu/Split_curve_09.png)  
Görüldüğü üzere, eğrimiz, seçili eğrilerle kesişim noktalarından bölündü.
 ![Split_curve_10](../../images/freecad/curves_wb/curves_menu/Split_curve_10.png)  
Birden fazla eğriyi aynı anda 
seçerek, diğer eğrilerle kesişim noktalarından bölmek te mümkün.
 ![Split_curve_11](../../images/freecad/curves_wb/curves_menu/Split_curve_11.png)  
![Split_curve_12](../../images/freecad/curves_wb/curves_menu/Split_curve_12.png)  
Bölünmüş eğriler seçerek bir yüzey oluşturmaya çalışalım.
 ![Split_curve_13](../../images/freecad/curves_wb/curves_menu/Split_curve_13.png)  
Oluşan yeni yüzeyi, ana yüzeyden çıkaralım.
 ![Split_curve_14](../../images/freecad/curves_wb/curves_menu/Split_curve_14.png)  
Sonuç:
 ![Split_curve_15](../../images/freecad/curves_wb/curves_menu/Split_curve_15.png)  

[<<< Curves Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_00_curves_menu.md)
