Title: FreeCAD - Silk WB - Öğretici Doküman 2.3
Date: 2024-02-23 21:50
Modified: 2024-02-23 22:30
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 2.3 (Tutorial 0.02 - P4)

### Kullanım - devam

Aşağıda gösterildiği gibi bir düğüm çizimi oluşturun. 100 derecelik açı, taslağın x ekseninden ölçülür.

![ControlGrid44 and CubicSurface44 21](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2021.png)
eskizden çıkın.

### -13-

ÜST GÖRÜNÜM'e (TOP VIEW) geçin.

Hiçbir şeyin seçili olmadığından emin olmak için boş alana tıklayın.

Yeni bir eskiz oluşturun. Hiçbir şey seçili olmadığı için, geleneksel düzlem seçici penceresi krşınıza gelir. **XY-Düzlemini (XY-Plane)** seçin ve **Tamam**'a (**OK**) basın.

![ControlGrid44 and CubicSurface44 22](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2022.png)

Gösterildiği gibi bir daire yayı çizin. Merkez **y eksenine kısıtlanmıştır** ve yayın uç noktaları ile **y ekseni arasında bir simetri kısıtı** vardır.

![ControlGrid44 and CubicSurface44 23](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2023.png)

eskizden çıkın.

### -14-

Hiçbir şeyin seçili olmadığından emin olmak için boş alana tıklayın.

Yeni bir eskiz oluşturun. Hiçbir şey seçili olmadığı için, geleneksel düzlem seçici penceresi karşınıza gelir. **XY-Düzlemini (XY-Plane)** seçin ve **Tamam**'a basın.

Sketcher araç çubuğundan **Harici Geometri Oluştur ([Create external geometry](https://wiki.freecad.org/Sketcher_External))** düğmesine basın, yayı seçin, komuttan çıkın.

![ControlGrid44 and CubicSurface44 24](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2024.png)

Aşağıda gösterilen düğümü çizin. Dairenin merkezi, yayın bitiş noktasındadır. Bu ilk bakışta çalışacak olan çizimdir, ancak daha sonra düzeltmemiz gerekecektir.

![ControlGrid44 and CubicSurface44 25](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2025.png)

### -15-

Hiçbir şeyin seçili olmadığından emin olmak için boş alana tıklayın.

Yeni bir eskiz oluşturun. Hiçbir şey seçili olmadığı için, geleneksel düzlem seçici penceresi karşınıza gelir. **YZ-Düzlemini (YZ-Plane)** seçin ve **Tamam**'a basın.

![ControlGrid44 and CubicSurface44 26](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2026.png)

Aşağıda gösterilen düğümü çizin. Daire merkezi, orijinin üzerindedir.

![ControlGrid44 and CubicSurface44 27](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2027.png)
Son çizilen eskizi (YZ üzerinde) seçin ve Parça Çalışma Tezgahı, Parça Menüsündeki (Part WB > Part) **Bağlantı düzenleyiciyi (Attachment editor**) etkinleştirin. Yay eskizinin sağ taraftaki uç noktasını referans nesne olarak seçin.

![ControlGrid44 and CubicSurface44 28](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2028.png)

Yayın bitiş noktası seçildiğinde, düğüm, yaya doğru hareket eder / taşınır / nakedilir. **Bağlantı Modu (Attachment mode)** varsayılan olarak **Orijini Naklet (Translate origin)** olmalıdır. İstediğimiz budur. **Tamam**'a basın.

![ControlGrid44 and CubicSurface44 29](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2029.png)

### -17-

Nerede olduğumuzu ve şimdiye kadarki çizimlerin birbirleriyle ve temel düzlemlerle nasıl ilişkili olduğunu anlamak için modeli döndürün. Bir sonraki resimde DAG görünümünü (DAG View) inceleyin:

* 3 bağımsız grup vardır
* birincisi *boş (blank)* 3D denetleyicidir, bunu göz ardı edebiliriz.
* ikinci grup ön profil ve ona bağlı iki düğümdür
* üçüncü grup yay ve ona bağlı iki düğümdür

![ControlGrid44 and CubicSurface44 30](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2030.png)



| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 2.2 ](freecad-silk-wb-ogretici-dokuman-22.html) | [Öğretici Doküman 2.4 >>](freecad-silk-wb-ogretici-dokuman-24.html) |

### Kaynak:

* [Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 04](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2004.md)
