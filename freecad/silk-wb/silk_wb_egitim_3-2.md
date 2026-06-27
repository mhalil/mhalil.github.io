Title: FreeCAD - Silk WB - Öğretici Doküman 3.2
Date: 2024-03-10 17:55
Modified: 2024-03-10 18:35
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 3.2 (Tutorial 0.03 - P2)

### Kullanım - devam

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 10](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2010.png)

* Unsur (model) ağacında yeni bir klasör oluşturun ve tüm **Point_onCurve** nesnelerini içine taşıyın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 11](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2011.png)

* Yay eğrisinin, en sol ucundaki noktanın **u** değerini **0,0** olarak ayarlayın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 12](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2012.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 13](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2013.png)

* Çizgi eğrisinin, sol ucuna doğru olan noktanın **u** değerini **0,22** olarak ayarlayın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 14](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2014.png)

* Çizgi eğrisinin, sağ ucuna doğru olan noktanın **u** değerini **0,70** olarak ayarlayın

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 15](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2015.png)

### -4-

Eğriyi yeni oluşturduğumuz noktalara göre keseceğiz. Seçmek istediğiniz nesneleri tanımlamayı ve unsur ağacında seçmeyi unutmayın. Özellikle bir eğri uç noktasının üzerinde yer alan bir **Point_onCurve** seçmeniz gerekiyorsa, 3B görünümde seçim tam olarak gerçekleşmeyebilir, o nedenle unsur ağacından seçim yapmak doğru ve kesinlik sağlar.

* **CubicCurve_4** **Yay**ını seçin

* Ctrl + ilk **Point_onCurve**'ü seçin (yay eğrisinin ortası)

* Ctrl + ikinci **Point_onCurve**'ü seçin (iki eğrinin birleşim köşesi)

* ControlPoly4_segment makrosu / komuunu çalıştırın  ![Point_onCurve](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4_segment.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 16](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2016.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 17](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2017.png)

İşlem sonucunda bir **ControlPoly4_segment** nesnesi oluşturulur. Bunu seçin ve **veri** sekmesine gidin. Bu nesnenin oluşumunda görev alan (altta yatan) eğri bağlantısını ve iki nokta bağlantılarını görebilirsiniz.

İlk eğitimde açıklandığı gibi, kütüphanenin varsayılan davranışı, doğrudan eğriler ve yüzeyler yerine önce bir kontrol poligonu veya bir kontrol ızgarası oluşturmaktır.

Segmentler oluşturmaya devam edelim!

* **CubicCurve_4** **Yay**ını seçin

* **Ctrl** + ilk **Point_onCurve**'ü seçin (yay eğrisinin ortası)

* **Ctrl** + üçüncü **Point_onCurve**'ü seçin (yay eğrisinin en ucunda, resimlerde solda)

* **ControlPoly4_segment** makrosunu / komutunu çalıştırın  ![ControlPoly4_segment](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4_segment.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 18](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2018.png)

İkinci **segment çokgeni**nizi oluşturduktan sonra, ikisini de (ControlPoly4_segment_000 ve ControlPoly4_segment_001) seçin, Çizgi kalınlıklarını **1,0** , renklerini **açık mavi**, Nokta boyutlarını **4,0** , renklerini **koyu mavi** olarak ayarlayın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 19](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2019.png)

Bu Eğitim birkaç sayfaya (Öğretici Dokümana) bölünmüştür, bu nedenle sayfa başına en fazla 10 tam boyutlu ekran görüntüsü vardır.

| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 3.1 ](freecad-silk-wb-ogretici-dokuman-31.html) | [Öğretici Doküman 3.3 >>](freecad-silk-wb-ogretici-dokuman-33.html) |

### Kaynak:

* [Tutorial 0.03 Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 - page 02](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2002.md)
