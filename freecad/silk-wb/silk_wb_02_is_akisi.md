Title: FreeCAD - Silk WB - 02 - İş Akışı
Date: 2024-02-11 20:10
Modified: 2024-02-11 20:30
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, İş Akışı, Akış
Author: Mustafa Halil

# Silk ÇalışmaTezgahı İş Akışı

**Silk WB**'in temel iş akışları aşağıdaki gibidir:

1 - Eskiz(ler) [Sketch(es)] bir tasarımın ana yüzeyleri üzerinde kontrol sağlar. Yüzey(ler), çizilen eskizlere (sketch) bağlı olarak oluşturulur. O nedenle doğru eskiz (sketch) çizmek çok önemlidir.

+ Eskiz(ler)  > Kontrol Çokgeni ( Sketch(es) > Control Polygon)

+ Kontrol Çokgeni > Kübik Eğri  (Control Polygon > Cubic Curve)

+ 3 veya 4 Kontrol Çokgeni > Kontrol Izgarası (3 or 4 Control Polygons > Control Grid)

+ Kontrol Izgarası > Kübik Yüzey (Control Grid > Cubic Surface )
  
  ![Bezier Primary Surfaces By Master Layout Sketch](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/development_FC_models/parametric/FreeCAD%200.17.9528/Bezier%20Primary%20Surfaces%20By%20Master%20Layout%20Sketch.gif)

2 - Ana yüzeyleri alt bölümlere ayırın ve köşeleri karıştırın

+ Kübik Eğri > Eğri Üzerindeki Noktalar > Eğri Segmenti Kontrol Çokgeni (Cubic Curve > Points On Curve > Curve Segment Control Polygon)

+ Çeşitli yöntemler Kontrol çokgenlerini ve Kontrol Izgaralarını Segmentlerini karıştırır.

![Bezier primary Surface Volume 66-07](https://github.com/edwardvmills/NURBSlib_EVM/raw/master/development_FC_models/parametric/FreeCAD%200.17.9528/Bezier%20primary%20Surface%20Volume%2066-07.bmp.png?raw=true)

Yukarıdaki model üç yüzeyin birleştiği bir köşenin karışımını göstermektedir. Büyük bir 'yarıçap' üst yüzeyle ön yüzeyi karıştırmaktadır, ancak üstten sola ve soldan öne yüzeyler küçük bir karışım  'yarıçapına' sahiptir. Bu model, dikişlerinin %95'i boyunca (dikiş uzunluğuna göre, yaklaşık olarak) G2 pürüzsüz veya daha iyidir. Mevcut tekniğin bazı kusurları var, ancak bunlar oldukça iyi anlaşılmış durumda ve bunları düzeltmek için net bir plan var.

Uygulanan ve planlanan çalışmaların ayrıntılı bir özeti için lütfen [geliştirme planına](https://github.com/edwardvmills/Silk/wiki/Development-Plan) bakınız.

### Kaynak

Sayfada paylaşılan bilgiler [Home · edwardvmills/Silk Wiki · GitHub](https://github.com/edwardvmills/Silk/wiki) adresinden yararlanılarak oluşturulmuştur.

| Önceki Sayfa                                             |
| -------------------------------------------------------- |
| [<< 01 Genel Bakış](freecad-silk-wb-01-genel-bakis.html) |
