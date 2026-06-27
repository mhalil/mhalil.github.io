Title: FreeCAD - Silk WB - Öğretici Doküman 2.2
Date: 2024-02-21 21:00
Modified: 2024-02-21 22:50
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 2.2 (Tutorial 0.02 - P3)

### Kullanım - devam

Açık mavi eskiz olan **Anchor - xy001**'i az önce düzenledik. **zx001** ve **merge001** eskizleri de güncellendi. Bir anda nasıl bağlandıklarını görmek üzereyiz.

![ControlGrid44 and CubicSurface44 11](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2011.png)

### -8-

**zx001** eskizini düzenlemeye başlayın. (**zx002** eskizinde gereksiz kısıtlamalar varsa kaldırın.) Lütfen yalnızca ilk seferde belirtilen değişikliği yapın.

![ControlGrid44 and CubicSurface44 12](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2012.png)

Açıyı 5 ila -85 derece arasında değiştirin.

![ControlGrid44 and CubicSurface44 13](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2013.png)

Köşegeni çizilmiş dikdörtgenin, açı değiştirmekten çok daha fazlasını yaptığına, aynı zamanda önemli ölçüde uzadığına dikkat edin. Bunun nedeni, dikdörtgenin, dairenin merkezinin karşısındaki köşesinin **Anchor - xy001** ile bağlantılı olmasıdır.

Eskizden çıkın ve incelemek için modeli döndürün.

![ControlGrid44 and CubicSurface44 14](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2014.png)

**merge001**, 3B uzayda herhangi bir yönü işaret edebilen <u>*tek düğümlü bir eskizdir*</u>; burada *teğetin konumu ve xy değeri* **Anchor - xy001**'de bulunur ve *teğetin z bileşeni* **zx001** tarafından kontrol edilir. Aynı sonucu elde etmek için çizimleri yapılandırmanın başka birçok yolu vardır. Eskizlerde açılar yerine yatay ve dikey boyutlar kullanabiliriz. Bu özel yöntem, **merge001** düğümünün uzunluğunu **xy** düzleminde yansıtıldığı şekilde kontrol eder.

### -9-

**front_profile_zx** eskizini düzenlemeye başlayın.

![ControlGrid44 and CubicSurface44 15](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2015.png)

### -10-

Sol taraftaki çizgiyi tıklayın + basılı tutun, ardından sola sürükleyin,

![ControlGrid44 and CubicSurface44 16](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2016.png)

ve bırakın.

![ControlGrid44 and CubicSurface44 17](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2017.png)

Eskizdeki bir nesneyi her sürükleyip bıraktığımızda, modelin geri kalanı bırakma işlemine göre güncellenir.

### -11-

***Anchor - xy001*** ve ***zx001*** eskizlerini gizleyin.

![ControlGrid44 and CubicSurface44 18](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2018.png)

Tek bir düğüm yapmak için oldukça çaba harcadık. Çoğu zaman, tam bir 3D denetleyici gerekli değildir. En azından başlangıçta. Bu derste geri kalan eğrileri çok daha hızlı yapacağız. Aslında bunlardan birini "yanlış" yapacağız ve daha sonra bileşenlerin modülerliğini göstermek için düzelteceğiz.

### -12-

**front_profile_zx** üzerinde az önce oluşturduğumuz kırmızı düğümün tam karşısındaki noktayı seçin.

![ControlGrid44 and CubicSurface44 19](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2019.png)

Bir eskiz oluşturun. Eskizi oluşturduğumuzda etkin bir seçimimiz olduğu için, *eskiz ekleme penceresi* açılır. Varsayılan değer **Orijini Naklet**'tir ve bizim istediğimiz de budur. Tamam (OK) düğmesine basın.

![ControlGrid44 and CubicSurface44 20](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2020.png)

| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 2.1 ](freecad-silk-wb-ogretici-dokuman-21.html) | [Öğretici Doküman 2.3 >>](freecad-silk-wb-ogretici-dokuman-23.html) |

### Kaynak:

* [Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 03](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2003.md)
