Title: FreeCAD - Silk WB - Öğretici Doküman 2.4
Date: 2024-02-24 18:45
Modified: 2024-02-24 19:30
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 2.4 (Tutorial 0.02 - P5)

### Kullanım - devam

### -18-

Görünümü [aksonometrik](https://wiki.freecad.org/Std_View_Menu) (üçboyutlu ancak perspektifsiz resim) olarak ayarlayın. Sonraki adımları irtibatlandırmak / açıkça göstermek için modele aynı noktadan bakıyor olmamız gerekir.

![ControlGrid44 and CubicSurface44 31](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2031.png)

### -19-

Yeni bir klasör oluşturun ve unsur ağacındaki her şeyi içine koyun. Klasörün adını **Sketches (Eskizler)** olarak değiştirin.

![ControlGrid44 and CubicSurface44 32](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2032.png)

### -20-

**front_profile_zx** eskizini seçin ve **ControlPoly4** makrosuna tıklayın / komutunu çalıştırın. ![ControlPoly4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4.png)

![ControlGrid44 and CubicSurface44 33](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2033.png)

### -21-

Sağ taraftaki iki düğümü seçin (benim modelimde Sketch033 ve Sketch037) ve ControlPoly4 makrosuna tıklayın / komutunu çalıştırın. ![ControlPoly4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4.png)

![ControlGrid44 and CubicSurface44 34](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2034.png)

### -22-

Yay eskizini seçin ve ControlPoly4 makrosuna tıklayın / komutunu çalıştırın. ![ControlPoly4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4.png)

![ControlGrid44 and CubicSurface44 35](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2035.png)

### -23-

Sol taraftaki iki düğümü seçin ve ControlPoly4 makrosuna tıklayın / komutunu çalıştırın.  ![ControlPoly4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly4.png)

![ControlGrid44 and CubicSurface44 36](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2036.png)

### -24-

Tüm eskizleri gizleyin. Şimdi yeni oluşturduğumuz ControlPoly4 nesnelerini görüyoruz.

![ControlGrid44 and CubicSurface44 37](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2037.png)

### -25-

Dört ControlPoly4 nesnesinin tümünü seçin, görünüm özelliklerine gidin (CTRL+D), **çizgi rengini** açık mavi olarak değiştirin.

![ControlGrid44 and CubicSurface44 38](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2038.png)

Unsur ağacında, ControlPoly4 nesnelerini, oluşturduğumuz sırayla seçin (CTRL + SOL CLICK). Nesnelerin aşağıdaki sıra ile seçildiklerini görmelisiniz:

* Ön
* Sağ
* Arka / Geri
* Sol

Sahneye baktığımız açıya göre, bu toplama sırası, saat yönünün tersi yönündedir. Bu da gelecekteki yüzeyin normalini bize doğru çevireceği anlamına gelir.

![ControlGrid44 and CubicSurface44 39](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2039.png)

ControlGrid44 makrosuna tıklayın / komutunu çalıştırın. ![ControlGrid44](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlGrid44.png)

![ControlGrid44 and CubicSurface44 40](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2040.png)

ControlGrid44 komutu çalışınca, belgeye bir ControlGridd44 nesnesi eklenir.

| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 2.3 ](freecad-silk-wb-ogretici-dokuman-23.html) | [Öğretici Doküman 2.5 >>](freecad-silk-wb-ogretici-dokuman-25.html) |

### Kaynak:

* [Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 05](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2005.md)
