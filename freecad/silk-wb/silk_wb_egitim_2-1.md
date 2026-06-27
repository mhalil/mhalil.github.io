Title: FreeCAD - Silk WB - Öğretici Doküman 2.1
Date: 2024-02-19 22:55
Modified: 2024-02-20 22:15
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 2.1 (Tutorial 0.02 - P1, P2)

## ControlGrid44 ve CubicSurface44 makroları/komutları

Bu bölümde, Silk Çalışma Tezgahındaki (eski adıyla NURBSlib_EVM'deki) ControlGrid44 ve CubicSurface44 makroları/komutları anlatılacaktır.

## Bu özel eğitim / sunum için hedef kitle;

Bu eğitim, FreeCAD'in bilgili kullanıcılarına Silk çalışma tezgahı (NURBSlib_EVM kütüphanesi) hakkında bir fikir vermek için hazırlanmıştır. Şu anda temel FreeCAD eylemleri hakkında hiçbir açıklama yapılmamaktadır. Yüzey modelleme için kullanılan eskizlerle ilgili olarak FreeCAD'in şaşırtıcı Ek Düzenleyicisi üzerinde biraz daha fazla çaba harcayacağım. FreeCAD'in, 2D çizim editörü, Part Workbench bağlantı editörü ve sınırsız harici referanslarla birleştirildiğinde, şimdiye kadar gördüğüm en iyi 3D çizim sistemi olduğunu sötyleyebilirim (deneyimim Solidworks ve Autodesk Inventor ile sınırlıdır).

Silk çalışma tezgahı ile ızgara ve oluşturmak bir dakikadan az sürer, ancak (yüzeyi oluşturacak olan) çizimler doğru şekilde yani bağlantılı olmadan, komutların doğru sonuç vermesi mümkün değildir.

## Bu eğitimi takip etmek için gerekenler;

* [Öğretici 1](freecad-silk-wb-ogretici-dokuman-1.html)'i tamamlamış olmak (özellikle kurulum kısmı),
* [FreeCAD](http://www.freecadweb.org/) 0.17'de bir makro / eklenti (addon) yöneticisi ile çalışma tezgahı kurma yeteneği, 
* FreeCAD'de çizgi ve yay çizimleri oluşturma becerisi,
* FreeCAD'deki üç temel düzlemin anlaşılması,
* Inkscape veya Illustrator'da bulunan NURBS veya Bezier eğrileri hakkında en azından belli belirsiz bir fikre sahip olmak çok faydalıdır.

Bu Eğitim birkaç sayfaya bölünmüştür, bu nedenle sayfa başına en fazla 10 adet ekran görüntüsü kullanılmıştır.

## Kullanım

### -1-

[Bu bağlantıda bulunan](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%20bare%20bones.FCStd) **ControlGrid44 and CubicSurface44 bare bones.FCStd** dosyasını indirin ve açın.

Bunu hemen **ControlGrid44 and CubicSurface44 in progress.FCStd** veya istediğiniz başka bir isimle kaydetmenizi tavsiye ederim. Bu, orijinal dosyayı korumak içindir.

![ControlGrid44 and CubicSurface44 01](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2001.png)

Bu model bazı başlangıç noktası eskizlerini içermektedir:

* 3B (3D) işaretçi oluşturan bir dizi bağlantılı eskiz içeren bir klasör
* zx düzleminde üç çizgi çizimi

Eskizleri içeren **3D node controller blank - COPY-PASTE THIS FOLDER** klasörü seçin ve **CTRL + C** (kopyala)  tuşuna basın.

FreeCAD, klasörün bağlı olduğu nesneleri kopyalamak isteyip istemediğimizi soracaktır, EVET'i seçin. (sadece klasörü mü kopyalamak istediğimizi yoksa klasörün içeriğini de dahil etmek isteyip istemediğimizi soruyor. Bu durumda, her şeyi istiyoruz)

![ControlGrid44 and CubicSurface44 02](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2002.png)

### -2-

**CTRL + V** (yapıştır) tuşuna basın. Klasörü ***3D node controller - front left*** (3D düğüm denetleyicisi - sol ön)  olacak şekilde yeniden adlandırın.

![ControlGrid44 and CubicSurface44 03](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2003.png)

### -3-

Klasörü genişletin ve **Anchor - xy001**'i seçin (benimkinde içeriğe 001 eklendi, çünkü tam olarak bir kez kopyaladım/yapıştırdım. Bunu tekrar tekrar yaparsanız, nesne adlarınıza 002, 003, 004 vb. eklenecektir. Ekran görüntülerine dikkat edin, çünkü nesne adlarımız muhtemelen senkronize olmayacaktır. isterseniz, nesne adlarımı görmek ve kendinizinkini ayarlamak için ekran görüntülerini kullanabilirsiniz. Bir nesne seçin ve yeniden adlandırmak için **F2**'ye basın)

**Parça çalışma tezgahına (Part WB)** gidin, **Parça (Part) menüsü** altında, menü listesinden **bağlantı... (attachment...**) seçeneğini seçin. (bu işlevi/komutu özel bir araç çubuğuna ekledim, böylece çalışma tezgahları arasında çok fazla geçiş yapmak zorunda kalmıyorum)

![ControlGrid44 and CubicSurface44 04](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2004.png)

**front_profile_zx** eskizinin en sol noktasını seçin. Bu, noktanın kendisi olmalıdır. Çizgi değil. Çizgiyi seçmek farklı bir harika şey yapar.

![ControlGrid44 and CubicSurface44 05](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2005.png)

Noktayı seçtiğinizde, ek düzenleyicinin ilk referansın bir uç nokta olduğunu bildirdiğini görebilirsiniz, **Sketch:Vertex1**.

**Anchor - xy001**, açık mavi eskiz, seçtiğinizde hemen uç noktaya nakledilir / taşınır. Yalnızca bir eskiz (seçili eskiz) hareket eder.

Bir uç nokta seçtiğimiz için **Bağlantı modu (Attachment mode**) otomatik olarak **Orijini Naklet (Translate origin**) olarak ayarlanır. Bizim istediğimiz de bu. Tamam'a (OK) basın.

![ControlGrid44 and CubicSurface44 06](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2006.png)

### -4-

Bağlantı Düzenleyiciden (Attachment Editor) çıktıktan sonra, **Anchor - xy001** yeniden hesaplanmak üzere işaretlenir. Modeli yeniden hesaplamak için **CTRL+R** tuşlarına basın.

![ControlGrid44 and CubicSurface44 07](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2007.png)

Yeniden hesaplama işleminden sonra, tüm eskizin *front_profile_zx*'in sol ucuna taşındığını görüyoruz.

**Çapayı (Anchor) yeniden bağlamak tüm grubu taşır. Birbiriyle bağlantılı eskiz koleksiyonları, bir klasör kopyalanıp yapıştırılarak yeniden kullanılabilir. Klasöre iyi bir isim verdiğiniz sürece, içindeki her bir öğeyi yeniden adlandırmanız gerekmez. 'Kök (root)' veya 'Çapa (Anchor)' öğesini kolayca tanımlayabildiğiniz sürece, tüm grubu yeniden kullanabilirsiniz**

### -5-

Orijinal **3D node controller blank - COPY-PASTE THIS FOLDER** klasörünü gizleyin.

![ControlGrid44 and CubicSurface44 08](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2008.png)

### -6-

**Anchor - xy0001** eskizini düzenlemeye başlayın. Lütfen ilk seferde talimatları tam olarak uygulayın. Bu eskiz yenilmez değildir, sadece bir gösterimdir ve kapsamı dışında kullanılırsa kolayca bozulabilir. Daha sonra geri dönüp üzerinde biraz daha oynama fırsatı olacaktır.

Aşağıda orijinal dosyadaki eskiz durumu gösterilmektedir.

![ControlGrid44 and CubicSurface44 09](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2009.png)

### -7-

Açıyı -20 ile 85 derece arasında değiştirin. (**zx002** eskizinde gereksiz kısıtlamalar varsa kaldırın.)

![ControlGrid44 and CubicSurface44 10](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2010.png)

| Önceki Sayfa                                                      | Sonraki Sayfa                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| [<< Öğretici Doküman 1 ](freecad-silk-wb-ogretici-dokuman-1.html) | [Öğretici Doküman 2.2 >>](freecad-silk-wb-ogretici-dokuman-22.html) |

### Kaynak:

* [Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 02](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)
