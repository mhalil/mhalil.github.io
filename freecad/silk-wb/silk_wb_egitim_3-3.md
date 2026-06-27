Title: FreeCAD - Silk WB - Öğretici Doküman 3.3
Date: 2024-03-17 13:30
Modified: 2024-03-17 14:05
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Eğitsel, Öğretici, Doküman, Tutorial
Author: Mustafa Halil

# Öğretici Doküman 3.3 (Tutorial 0.03 - P3)

### Kullanım - devam

### -5-

* İlk segment poligonunu seçin, **CubicCurve_4** komutunu çalıştırın ![CubicCurve4](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/icons/CubicCurve4.png)

* Eğri rengini koyu turuncu olarak ayarlayın

* ikinci segment poligonu için tekrarlayın

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 20](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2020.png)

* Soldaki yay eğrisi segmentini seçin (merkezden uzakta). Parça Çalışma Tezgahındaki Ekstrüzyon (Part WB > Extrude) komutunu çalıştırın, değeri 20 mm olarak ayarlayın.

Parça Çalışma Tezgahındaki Ekstrüzyon (Part WB > Extrude) komutunu bazen birden fazla varlık oluşturur. Önemli bir unsuru kaybetmediğinizden emin olmak için modelinizi inceleyin. Alternatif olarak, sadece ekstra öğeleri gizleyin, ancak bu daha sonra kafa karıştırıcı olabilir. Bazen Part Extrude komutu altınta yatan eğriyi ana model ağacının dışına taşır, bazen de taşımaz! Bir şeyi silmeye çalışırsanız ve bağlantılardan şikayet ederse, iptal edin!

* Ekran modunu gölgeli olarak ayarlayın (Kısayol tuşu **V + 6**) (böylece kenar çizgileri gizlenir)

* Rengi açık turuncu olarak ayarlayın

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 21](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2021.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 22](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2022.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 23](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2023.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 24](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2024.png)

### -6-

Sağdaki çizgi eğrisine de **-4-** ve **-5-** adımlarını uygulayın

* **CubicCurve_4** nesnesi ve **Point_onCurve** nesneleri ile segment çokgenleri oluşturma
* Kesit poligonlardan (poligon parçalarından) **CubicCurve_4** nesneleri oluşturun
* Dış eğri parçasını (en sağ taraf) ekstrüde edin
* Yol boyunca renkleri ve öğe boyutlarını ayarlayın.

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 25](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2025.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 26](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2026.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 27](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2027.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 28](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2028.png)

![Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 29](https://raw.githubusercontent.com/edwardvmills/NURBSlib_EVM/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2029.png)

Bu Eğitim birkaç sayfaya (Öğretici Dokümana) bölünmüştür, bu nedenle sayfa başına en fazla 10 tam boyutlu ekran görüntüsü vardır.

| Önceki Sayfa                                                         | Sonraki Sayfa                |
| -------------------------------------------------------------------- | ---------------------------- |
| [<< Öğretici Doküman 3.2 ](freecad-silk-wb-ogretici-dokuman-32.html) | [Öğretici Doküman 3.4 >>](freecad-silk-wb-ogretici-dokuman-34.html) |

### Kaynak:

* [Tutorial 0.03 Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 - page 03](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2003.md)
