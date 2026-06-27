Title: FreeCAD - Silk WB - Öğretici Doküman 3.4
Date: 2024-03-17 14:05
Modified: 2024-03-17 14:35
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 3.4 (Tutorial 0.03 - P4)

### Kullanım - devam

### -7-

* Köşeyi oluşturan iki **CubicCurve_4** nesnesini seçin, **ControlPoly6** komutunu çalıştırın. ![ControlPoly6](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/ControlPoly6.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 30](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2030.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 31](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2031.png)

Bu komut, **ControlPoly6_FilletBezier** türünde bir ilk 6 noktalı kübik NURBS kontrol poligonumuzu oluşturur (**ControlPoly6**). Bu poligonlar bir kez daha, **ControlPoly6** nesneleri doğrudan modellemek için kullanılabilir, ancak kübik bezier segmentini birleştirmek amacıyla var olurlar. Bir **ControlPoly6** üzerindeki ekstra noktalar ona esneklik kazandırır, ancak aynı zamanda kesinlikle çok çirkin eğriler yapmayı da kolaylaştırır.

Uzun vadede, bu kütüphane için plan, ana tasarım esnekliği için daha yüksek dereceli Bezier'i tanıtmak (5 noktalı Bezier kuartik, 6 noktalı kuintik, vb.) ve tabiri caizse NURBS'yi köşelerde tutmaktır. Bezier eğrileri, beklenmedik bir şekilde ortada bükülmelerini önleyen bazı kendi kendini yumuşatma özelliklerine sahiptir. Genel bir NURBS kendi sınırları içinde çok kaba olabilir.

Bu durumda, **ControlPoly6** bağlı olduğu iki eğriye dikkatlice bakar, bir uçtaki eğriliği belirler, diğer uçta ve makul bir kontrol çokgeni üretmek için NURBS'de kalan serbestlik dereceleri hakkında bir tahminde bulunur.

* Çokgen çizgi rengini açık mavi olarak ayarlayın
* Çokgen nokta rengini koyu mavi, boyutunu 4.0 olarak ayarlayın

### -8-

* **ControlPoly6_FilletBezier** nesnesini seçin, **CubicCurve_6** komutunu çalıştırın. ![CubicCurve6](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/CubicCurve6.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 32](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2032.png)

Bu komut, yukarıdaki **ControlPoly6** nesnesiyle ilişkili gerçek eğriyi oluşturur.

* rengi koyu turuncuya çevir.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 33](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2033.png)

* **CubicCurve_6** nesnesini Extrude edin. (Parça Çalışma Tezgahındaki Ekstrüzyon (Part WB > Extrude) komutunu çalıştırın)

* Yinelenen yüzeyleri kontrol edin/ FreeCAD'in eğriyi nereye koymaya karar verdiğini bulun (unsur ağacı mı yoksa parça  ekstrüzyonunun altına mı yoksa her ikisine de mi?)

* Görüntüleme modunu gölgeli, rengi açık turuncu, ekstrüzyon boyutlarını segment eğrisi ekstrüzyonları ile aynı olarak ayarlayın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 34](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2034.png)

Görünür kenar çizgilerinin olmaması ve üç yeni yüzey parçasının da aynı renkte olması çok önemlidir. İki yüzeyin birleştiği yerde kenar çizgilerinin çizilmiş olması pürüzsüz bir birleşme yanılsaması yaratabilir, ancak modeli render ettiğinizde veya işlediğinizde hiçbir çizgi kalmaz. Birdenbire birleşimin kusurları çığlık atacaktır! Yan yana iki yüzey neredeyse hiçbir zaman o kadar kötü görünmez, ancak bir gövdeye çok sayıda yama yaptığınızda, her yerde çarpı işareti oluşturan tüm dikişleri gerçekten görmek istemezsiniz.

Aşağıdaki resimlerde dikiş yerlerinde eğrilik eşleşmesi var. Bu iyi bir başlangıçtır. Bir tasarımın ilk aşamasında, ana (Bezier) çizgiler değişirken, kenar karışımlarının mükemmel olmasına gerek yoktur. Kaba karışımları görebilmek ve aksaklıkları ayarlayabilmek, ana tasarıma rehberlik etmek için çok yararlıdır.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 354](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2035.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 36](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2036.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 37](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2037.png)

*Bir sonraki eğitim, dikiş kalitesini incelemek ve G3'e ulaşmak için parametreleri manuel olarak değiştirmek için bu modelde zaten mevcut olan nesneleri kullanmayı ele alacaktır, eğrilik eşleşmesinin değişimi!*

### Bu Proje, [Silk Repository](http://edwardvmills.github.io/Silk/)'ye taşındı

#### Bir sonraki öğretici [FreeCAD forumunda](https://forum.freecad.org/viewtopic.php?f=22&t=23243&start=70#p188431) bulunabilir, kayık modelinin nerede başladığını görmek için geri dönüp yorum dizisinin önceki bölümlerini okuyabilirsiniz. Bu bağlantılar sizi yüzeyleri birbirine karıştırmaya başladığımız bir noktaya götürecektir.

| Önceki Sayfa                                                         |
| -------------------------------------------------------------------- |
| [<< Öğretici Doküman 3.3 ](freecad-silk-wb-ogretici-dokuman-33.html) |

### Kaynak:

* [Tutorial 0.03 Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 - page 04](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2004.md)
