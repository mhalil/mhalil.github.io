Title: FreeCAD - Silk WB - Öğretici Doküman 2.6
Date: 2024-02-26 21:45
Modified: 2024-02-26 22:20
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 2.6 (Tutorial 0.02 - P7)

### Kullanım - devam

![ControlGrid44 and CubicSurface44 50](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2050.png)

![ControlGrid44 and CubicSurface44 51](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2051.png)

![ControlGrid44 and CubicSurface44 52](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2052.png)

![ControlGrid44 and CubicSurface44 53](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2053.png)

![ControlGrid44 and CubicSurface44 54](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2054.png)

![ControlGrid44 and CubicSurface44 55](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2055.png)

### -32-

Şimdi dramatik bir değişiklik yapalım: tüm yay eskizini 200mm aşağı taşıyalım. Çizimi seçin, (**Düzen** menüsünden **Yerleşim...** seçeneğine tıklayın) ve veri sekmesi altında yerleşimini düzenleyin, (Z : -200mm )

![ControlGrid44 and CubicSurface44 56](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2056.png)

![ControlGrid44 and CubicSurface44 57](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2057.png)

Neler oluyor? Aşağıdaki resimde sol taraftaki düğüm poligonu doğru hareket etti ve yayı takip etti, ancak diğer taraf hareket etmedi! ControlPoly44 nesnesinde kırmızı bir bayrak var ve güncellenmiyor.

Doğru hareket eden düğüm YZ üzerinde çizildi ve ardından yay noktasına bağlandı.

Doğru hareket etmeyen düğüm XY üzerinde çizildi ve bir geometri bağlantısı aracılığıyla yaya bağlandı. Bu sadece yay da XY üzerinde olduğu sürece çalışır! Değilse, geometri bağlantısı hala çalışır, ancak düğüm taslağına yansıtıldığı için, bu aslında iki noktayı birbirine bağlamaz.

**Bağlantı düzenleyici (attachment editor**)  eskizleri bağlamak için doğru yoldur. Bir başka avantajı da eskizlerimizde orijini daha fazla kullanmamızdır. Bu temelde her eskizde ilk iki kısıtlamayı serbest olarak verir.

### -33-

Bağlantısı kesilmiş düğüm eskizini seçin, **Bağlantı düzenleyiciyi (attachment editor**) başlatın, referans olarak yay uç noktasını seçin.

![ControlGrid44 and CubicSurface44 58](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2058.png)

Izgara ve yüzey kaybolur, ancak endişelenmeyin, hemen geri döneceklerdir. Düğüm eskizi artık yay noktasına bağlı, ancak eskiz çizimini de düzenlememiz gerekiyor.    

### -34-

Çizimi düzenleyin. Düğümün dairesini orijine yerleştirin, bu daire artık yayın tam ucundadır (çizginin de geldiğinden emin olun). Çokgen, ızgara ve yüzey hemen geri gelecektir.

Bugünlük bu kadar. Umarım çok fazla hata yoktur, çünkü bir günde çok fazla şey  anlatmaya çalıştım. Eğer bir şey tam olarak çalışmazsa, bana bildirin ve düzelteyim.

![ControlGrid44 and CubicSurface44 59](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2059.png)

![ControlGrid44 and CubicSurface44 60](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2060.png)

| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 2.5 ](freecad-silk-wb-ogretici-dokuman-25.html) | [Öğretici Doküman 3.1 >>](freecad-silk-wb-ogretici-dokuman-31.html) |

### Kaynak:

* [Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 07](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2007.md)
