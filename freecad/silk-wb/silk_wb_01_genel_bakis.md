Title: FreeCAD - Silk WB - 01 - Genel Bakış
Date: 2023-06-30 00:00
Modified: 2024-02-11 20:00
Category: Silk WB
Tags: FreeCAD, Silk, Workbench, ÇalışmaTezgahı, Genel, Bakış
Author: Mustafa Halil

# Silk ÇalışmaTezgahına Genel Bakış

Tasarım ve mühendislik için yüksek kaliteli ve düşük ağırlıklı yüzey modelleme araçları barındıran çalışma tezgahı.

![silk](https://github.com/edwardvmills/Silk/raw/master/Resources/Demo_files/Silk_Front_Page_02.png?raw=true)

## Silk ÇalışmaTezgahı (WorkBench) Nedir?

Silk ÇalışmaTezgahı (WorkBench), FreeCAD'de NURBS yüzeyleri oluşturan bir Harici çalışma tezgahıdır.
Silk, NURBS Düşük derece ve dikiş sürekliliğine odaklanan yüzey modelleme araçlarıdır.

![silk_demo](https://github.com/edwardvmills/Silk/raw/master/Resources/Demo_files/Silk_Demo_03_01.png?raw=true)

## Tanımlar

**NURBS**: formu/şekli nispeten az sayıda "kontrol noktası" tarafından kontrol edilen, pürüzsüz eğriler ve yüzeylerdir. 
Adından da anlaşılacağı gibi, "kontrol noktaları", kullanıcının eğrileri veya yüzeyleri kontrol etmek için değiştirdiği şeylerdir. 
Bir NURBS'nin "iyileştirilmesi" derecesi tarafından kontrol edilir ve bir kontrol noktasının "etki mesafesi" NURBS'nin düğüm vektörü tarafından kontrol edilir.

**Düşük Derece (Low Degree)**: Silk NURBS eğrileri ve yüzeyleri, istenilen amaca uygun minimum derecededir. Düğüm vektörleri küçük bir tutarlı kümede tutulur. Genellikle NURBS modelleme problemlerinde görünen çözüm, düğümlerin derecesini ve sayısını artırmaktır. Bu tamamen geçerli olsa da, kontrol noktalarının hesaplama zorluklarını ve organizasyon zorluklarını artırıyor. Silk, çözülen her problem için mutlak minimum matematiksel karmaşıklığa sahip araçlar sağlamayı amaçlar.

**Dikiş Sürekliliği (Seam Continuity)**: Silk'in amacı, farklı NURBS bölümlerinden karmaşık modellerin oluşturulmasına olanak tanımak, alternatif olarak mevcut yüzeylere sürekli olacak yeni yüzeyler oluşturmak veya yüzeylerin başlangıçta süreksizliklerle oluşturulduğu yerlerde, yumuşak geçişler oluşturmak için araçlar sağlamaktır.

Aşağıdaki animasyon, eğri ve yüzey sürekliliğinin tam mühendislik kontrolü ile eskizler aracılığıyla ince yüzey ayarını göstermektedir. Profil kontrol çiziminde kullanılan kontrol noktası sayısının az olduğuna dikkat edin. Belirli bir karmaşıklığa kadar Silk, eskiz düzenleme ile neredeyse gerçek zamanlı olarak güncellenir.

![anim](https://github.com/edwardvmills/Silk/raw/master/Resources/Demo_files/Steering_Wheel_01_01.gif?raw=true)

## Kısıtlamalar

Silk, uzun vadede verimli ve kullanıcı dostu araçlar sağlamayı amaçlasa da, şu anda işlevlerine GUI erişimi olan düşük seviyeli bir kitaplık gibi davranıyor. Bağımsız işlevler, ayrı belge nesneleri oluşturur ve gelecekte, karmaşık iç içe nesneler oluşturmak için ilgili işlevler otomatik olarak birbirine zincirlenebilir. Mevcut nesnelerin, hem bireysel belge nesneleri olarak hem de gelecekte alt nesneler olarak kalma olasılığı çok yüksektir.

Mevcut durumda modelleme yapılabilir ve ortaya çıkan veri yapıları verimlidir, ancak süreç zahmetli olabilir. Kullanıcı dostu olmaya yönelik en iyi yol, büyük ölçüde FreeCAD topluluğu içinde parçaların, katı gövdelerin, düzeneklerin ve nesne bağlantılarının nasıl organize edildiğine dair çeşitli tartışmaların sonucuna bağlı olacaktır.

Bu arada Silk, FreeCAD'de başka türlü bulunmayan (örn. `3D spline`) birkaç araç sunar ve genel olarak yüzey tasarımı, kontrol stratejileri, veri yapıları ve algoritmalar için bir sanal alan olarak görülebilir.

![Steering_Wheel_03_05](https://github.com/edwardvmills/Silk/raw/master/Resources/Demo_files/Steering_Wheel_03_05.png?raw=true)

## Kurulum

Silk ÇalışmaTezgahı (WorkBench), `Araçlar -> Eklenti Yöneticisi (Tools -> Addon Manager)` menü yolu kullanılarak ulaşılan, [FreeCAD Eklenti Yöneticisi (Addon Manager)](https://wiki.freecadweb.org/AddonManager) aracılığıyla kolayca kurulabilir.

### Kaynak

Sayfada paylaşılan bilgiler [edwardvmills/Silk](https://github.com/edwardvmills/Silk) adresinden yararlanılarak oluşturulmuştur.

| Önceki Sayfa                                         | Sonraki Sayfa                                      |
| ---------------------------------------------------- | -------------------------------------------------- |
| [<< 00 Silk WB Giriş](freecad-silk-wb-00-giris.html) | [02 İş Akışı >>](freecad-silk-wb-02-is-akisi.html) |
