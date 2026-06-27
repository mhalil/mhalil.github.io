Title: FreeCAD - Silk WB - Öğretici Doküman 2.5
Date: 2024-02-25 21:30
Modified: 2024-02-25 22:00
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 2.5 (Tutorial 0.02 - P6)

### Kullanım - devam

### -26-

Izgaranın rengini açık mor olarak değiştirin.

![ControlGrid44 and CubicSurface44 41](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2041.png)

### -27-

Izgara hala seçiliyken CubicSurface44 makrosuna tıklayın / komutunu çalıştırın. ![CubicSurface44](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/CubicSurface44.png)

![ControlGrid44 and CubicSurface44 42](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2042.png)

### -28-

Yüzeyin rengini turuncu olarak değiştirin ve saydamlığı 40 olarak değiştirin. Renk ve şeffaflık, görüntünün derinliğini daha iyi algılamak için kullanışlıdır. Belki başka renkleri tercih edersiniz, asıl mesele gri bir yüzey üzerindeki bir grup siyah çizgiyi deşifre etmeye çalışmanın beyni zorlaması ve kontrastın beyninizi diğer görevler için serbest bırakmasıdır.

![ControlGrid44 and CubicSurface44 43](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2043.png)

Modeli döndürün ve inceleyin. Kontrol çizgilerinin yüzeyin neresinden geçtiğine dikkat edin. Çizgilerin açılarının yüzeyin eğrilerine nasıl yol açtığını anlamaya çalışın.

![ControlGrid44 and CubicSurface44 44](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2044.png)

### -29-

Eskizleri tekrar açın, görünür hale getirin.

![ControlGrid44 and CubicSurface44 45](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2045.png)

### -30-

Yay eskizini aşağıda gösterildiği gibi düzenleyin. Yay merkezini kontrol eden dikey boyutu 10'dan 100'e yükseltin.

![ControlGrid44 and CubicSurface44 46](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2046.png)

![ControlGrid44 and CubicSurface44 47](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2047.png)

Boyut girdi kutusunda enter tuşuna bastığınızda, model bilgisayarınızın kaldırabileceği kadar hızlı güncellenecektir. Yay eskizi kendisine bağlı düğüm eskizlerini, bu düğüm eskizleri kendilerine bağlı ControlPoly4'leri, bunlar kendilerine bağlı ControlGrid44'ü ve bu da yüzeyin kendisini öteleyecektir! Büyük modellerde, güncellemenin model boyunca basamaklandırıldığını görebilirsiniz.

Bir boyut girildiğinde çizim hemen güncellenir. Sürükle ve bırak işlemi sonucu her bıraktığınızda çizim güncellenir. **DİKKAT** Çizimdeki değişiklik ızgaranın tamamen bozulmasına neden olursa, ortaya çıkan yüzeyin hesaplanması çok zor olur ve FreeCAD'in takılmasına neden olabilir. Bu FreeCAD'in değil, NURBS'lerin kendi sınırlamasıdır. FreecAD'e sıkıştırılmış ve katlanmış bir NURBS hesaplamasını söylerseniz, elinden gelenin en iyisini yapacaktır, ancak sonuç çirkin olacak ve işlemci süresinde çok pahalıya mal olacaktır!

Genel olarak, bir ızgara kendini çok fazla geçmemeli ve açılar minimum düzeyde tutulmalıdır. Bir şeyleri sadece gerçekten ihtiyacınız olduğu kadar bükün. Pratik yapmanın yerini hiçbir şey tutamaz. Çizginin nerede olduğunu bilmek için modeller yaparsınız ve çarpmalarını/takılmalarını sağlarsınız.

Şaşırtıcı olan şey, bunu yapmak için zaman harcarsanız, çok hızlı bir şekilde, doğru yolda olup olmadığınızı anlamak için yalnızca ızgarayı görmeniz gerektiğini anlayacaksınız. Doğru yüzeyi elde etmek için pratik yaparken, eskizleri düzenlerken  yüzeyleri gizleyebilirsiniz. Doğrudan ızgaralarla çalışmak size hız ve işlemci gücü avantajı sağlayacaktır.  Yüzeyler gizlenmiş halde sadece ızgaralarla çalışmak temelde 0 (sıfır)  işlemci gücü gerekir. Ne kadar bilgisayar gücünüz olduğu umurumda değil, %99'unu kilitlemek sizi yavaşlatacaktır.

İyi bir ara adım, değiştirmediğiniz yüzeyleri gizlemek, ızgaralarını açık bırakmak ve yalnızca odaklandığınız yüzeyleri görüntülemektir.

### -31-

Aşağıdaki resimlerde gösterilen değişiklikleri çoğaltın. (veya bu eğitimin son önemli noktası için 32. adıma atlayın)

Düzenlenmekte olan eskiz, her resimde DAG görünümünde vurgulanacaktır.

![ControlGrid44 and CubicSurface44 48](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2048.png)

![ControlGrid44 and CubicSurface44 49](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2049.png)

![ControlGrid44 and CubicSurface44 50](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2050.png)

| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 2.4 ](freecad-silk-wb-ogretici-dokuman-24.html) | [Öğretici Doküman 2.6 >>](freecad-silk-wb-ogretici-dokuman-26.html) |

### Kaynak:

* [Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 06](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2006.md)
