Title: Solvespace Bölüm 7: Dışa Aktarım
Date: 2022-03-10 15:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Dışa Aktar, Export, Resim, Kesit, 2D, 2B, Görüntü, TelKafes, Üçgen, Yüzey, Mesh, STL, OBJ, STEP
Author: Mustafa Halil


## Bölüm 7: Dışa Aktarım

## Resim olarak dışa aktar...

Bu seçenek, ekranda görüntülenenlerin bitmap 
(vektörel olmayan resim) görüntüsünü dışa aktarır. Bu işlem, ekran 
görüntüsü almaya eşdeğerdir. Bu seçenek, insan tarafından okunabilir 
çıktı üretmek için kullanışlıdır.

`Dosya → Resim olarak dışa aktar...`'ı seçin. Görüntü, çoğu grafik yazılımının açabileceği bir **PNG** uzantılı dosya olarak dışa aktarılır.

## Kesiti 2d olarak dışarı aktar...

Bu seçenek, katı modeli belirli bir düzlem 
boyunca kesecektir. (Ekrana bakıldığında görünen 2 boyutlu çizimin arka 
planında kalan kısım görünmeyecekir, görünmeyen kısım ile görünen kısmı 
ayıran hayali düzlemden bahsediliyor.) Bu düzlemde bulunan (Ekrana 
bakıldığında görünen 2 boyutlu çizimin) katı modeldeki tüm çizgiler ve 
eğriler dışa aktarılacaktır. Katı modelden bu düzlemde yer almayan 
çizgiler ve eğriler yok sayılır. Bu seçenek genel olarak, örneğin bir 
lazer veya su jeti kesicisi için bir 3B modelden 2B CAM verileri 
oluşturulurken uygundur.  
Bir bölümü dışa aktarmadan önce, parçanın hangi 
düzleminin dışa aktarılacağını belirtmek gerekir. Bu şu şekilde 
belirtilebilir:

**Bir yüzey;**  
Bu düzlem yüzüyle aynı düzlemde olan tüm yüzeyler 
dosyada görünecektir. Yüzlerin seçilebilmesi için önce gösterilmesi ve 
seçilebilir olması gerekir; Bunun için Özellik Penceresinin üst 
satırındaki ilgili bağlantıya tıklayın.

**Bir nokta ve iki çizgi veya vektör;**  
Dışa aktarma düzlemi noktadan geçer ve iki doğruya 
veya vektöre paraleldir. İki çizgi veya vektör dikse, dışa aktarılan 
dosyada x ve y ekseni haline gelirler. Geçerli görünümde hangisi daha 
yataysa, x ekseni ve diğeri y ekseni olur.  
Bu, görünümü doksan derece döndürerek (bu yüzeyin 
düzleminde) dışa aktarılan dosyayı doksan derece döndürmenin mümkün 
olduğu anlamına gelir. Benzer şekilde, ön tarafa arkadan bakacak şekilde
 parçayı döndürerek, çalışma dışa aktarıldığında, oluşan görüntü 
aynalanmış vaziyette oluşturulur.

**Aktif çalışma düzlemi;**  
Bir çalışma düzlemi etkinse ve dışa aktarma komutu 
seçildiğinde hiçbir şey seçilmemişse, SolveSpace etkin çalışma düzlemi 
ile aynı düzlemde olan tüm yüzeyleri dışa aktaracaktır. Çalışma 
düzleminin yatay ve dikey eksenleri, dışa aktarılan dosyada x ve y 
ekseni haline gelir.

![Seçili Yüzeyi 2d olarak dışa aktar](images/solvespace/44%20Egriler%20Parcali.png)

![Seçili Yüzeyin PDF Uzantılı Dışa Aktarılmış Hali](images/solvespace/45%20Kesiti%202d%20olarak%20aktar.png)

Dışa aktarılan dosyanın birimleri, yapılandırma ekranında belirtilebilecek dışa aktarma ölçek faktörü tarafından belirlenir.  
Çizim eğriler içeriyorsa, dışa aktarılan dosya bu 
eğrileri tam olarak temsil edebilir (SVG tam daireleri destekler), 
yaklaşık olarak ancak düzgün bir eğriyle (PDF yalnızca bir daireyi tam 
olarak temsil edemeyen kübik eğrileri destekler) veya parçalı doğrusal 
segmentler olarak temsil edebilir (HPGL dosyasındaki bir daire). 
Eğrileri parçalı doğrusal olarak çıktı almaya zorlamak için yapılandırma
 ekranında '`curves as piecewise linear` (*eğrileri parçalı doğrusal olarak*)'
 seçeneğini aktifleştirin. Çıktı dosyasındaki renkler, görüntüleyiciniz 
tarafından kullanılan renk alanına bağlı olarak ekranda görüntülenen 
modelin renklerine tam olarak uymayabilir.

![Eğrileri parçalı doğrusal olarak](images/solvespace/46%20Yuzey%20Kesiti.png)

## Görüntüyü 2d olarak dışa aktar...

Bu seçenek, modeli görüntülediğinizde ekrana 
yansıtıldığı gibi, 3B modeli bir düzleme yansıtacaktır. Projeksiyon 
düzleminde yer alan çizgiler ve eğriler herhangi bir değişiklik 
yapılmadan dışa aktarılır; projeksiyon düzleminde yer almayan çizgiler 
ve eğriler, projeksiyon nedeniyle kısaltılmış görünecektir.

Bu seçenek genellikle vektör formatında, insan 
tarafından okunabilir bir çizim oluştururken uygundur. Yalnızca katı 
modeldeki çizgileri değil, tüm çizgileri dışa aktardığı için de 
yararlıdır; bu nedenle, kullanıcı çizgilerden ve eğrilerden bir eskiz 
çizerse, ancak bunu katı bir model oluşturmak için ekstrüde etmek 
istemezse, bu seçeneği kullanarak yalın çizimlerini 2d biçiminde dışa 
aktarabilir.

Projeksiyon düzlemi, ekrandaki model 
döndürülerek, fare ile merkeze sürüklenerek seçilir. Dışa aktarılan 
dosyanın orijini (merkezi), ekrandaki görünümün merkezine karşılık gelir
 ve bu nedenle kaydırma ile (fare ile sağa sürüklenerek) hareket 
ettirilebilir. Projeksiyon düzlemini tam olarak belirtmek için, görünümü
 bir çalışma düzlemine yönlendirin veya `Görünüm → En Yakın Dik / İzometrik Görünüm` (kısayol tuşları `F2` ve `F3`) ve `Görünüm → Noktayı Merkezde Görüntüle` (kısayol tuşları `F4`) komutlarını kullanın.

Varsayılan olarak, görünümün çıktısında gizli 
çizgiler kaldırılmış olacak ve kavisli bir yüzeyin öne bakan yerinden 
arkaya baktığı her yere ek çizgiler çizilecektir. Bu genellikle istenen 
sonuçtur. Parçanın tel kafes görünümünü oluşturmak için dışa aktarmadan 
önce "**hidden-lns** (*gizli çizgiler*)" öğesini gösterin.

EPS, SVG, PDF gibi bazı dosya biçimleri, gölgeli 
yüzeyleri destekler. Kullanıcı böyle bir dosya formatında dışa aktarım 
yapıyorsa ve yapılandırma ekranında "`export shaded 2d triangles` (*gölgeli 2d üçgenleri dışa aktar*)"
 seçeneği işaretlemişse, görünüm, modelin düz gölgeli yüzeylerini 
içerecektir. Aydınlatma, modelin ekrandaki görünümüyle aynı şekilde 
hesaplanır. Bu nedenle, konfigürasyon ekranındaki ışık yönleri (`light direcition`) ve yoğunlukları (`intensity`) değiştirilerek, yüzeylerin gölge yönleri değiştirilebilir.

![Gölgeli 2d üçgenleri dışa aktar](images/solvespace/47%20Golgeli%202d%20ugcgenler.png)

![Işık yönleri ve yoğunlukları](images/solvespace/48%20Isik%20yonleri.png)

Dışa aktarılan dosyanın birimleri, yapılandırma 
ekranında belirtilebilecek dışa aktarma ölçek faktörü tarafından 
belirlenir. Çizimde bir katı model varsa ve yüzeyler gizlenip gizli 
çizgiler gösterilerek dışa aktarım yapılırsa, dosya yalnızca çizgi 
parçalarını içerecektir; tüm eğriler, belirtilen nüans/akor toleransıyla
 çizgilere ayrılır. Çizimde doğrusal uzatarak ya da tam/kısmi döndürerek
 katılanmış katı model mevcut değilse ve gizli çizgiler görünür 
durumdaysa, eğriler mümkün olduğunca tam biçimde dışa aktarılacaktır.

Normaller, veri noktaları ve resim öğeleri, vektör biçimleri için dışa aktarılmaz.

## 3d TelKafes olarak dışa aktar...

Bu seçenek, `Dosya → Görüntüyü 2d olarak Dışa Aktar...` ile hemen hemen aynı şekilde davranır; ancak çizgileri ve eğrileri 
belirtilen 2d düzleme yansıtmak yerine çizgileri ve eğrileri 3d olarak 
dışa aktarır.

3d TelKafes, herhangi bir yüzey veya katı 
içermez. Bu aktarım seçeneği, genellikle katı parçaların görüntülenmesi 
veya üretilmesi için uygun değildir. Bunun için bir Üçgensel Mesh (ağ) 
veya bir NURBS yüzey (STEP) dosyası kullanın.

## Üçgensel Mesh olarak dışa aktar (STL, OBJ)

Bu seçenek, tüm parçayı temsil eden bir 3B 
üçgensel ağ (mesh) oluşturacaktır. Çoğu 3d yazıcının yazılımı da dahil 
olmak üzere, çoğu 3D CAM yazılımı bir STL dosyasını kabul eder.

Aktif gruptaki ağ (kafes yapısı) dışa 
aktarılacaktır; bu, ekranda görüntülenen aynı ağdır (kafes yapısıdır). 
STL dosyası için koordinat sistemi, parçanın çizildiği koordinat 
sistemiyle aynıdır. Farklı bir koordinat sistemi kullanmak için (örn. 
parçayı döndürmek veya çevirmek için), parça istenen konumda olacak 
şekilde bir montaj oluşturun ve ardından montajın bir STL dosyasını dışa
 aktarın.

STL dosyasının ölçü birimleri, yapılandırma ekranında belirtilebilecek olan dışa aktarma ölçek faktörü/katsayısı (`export scale factor`) tarafından belirlenir.

![Dışa aktarma ölçek faktörü (katsayısı)](images/solvespace/49%20Olcek%20Faktoru.png)

## Yüzeyleri dışa aktar (STEP)

Model, NURBS yüzeyleri olarak temsil ediliyorsa 
(sadece bir üçgensel ağ olarak değil), kullanıcı bu tam yüzeyleri bir 
STEP dosyası olarak dışa aktarabilir. Bu tür dışa aktarım işlemi mümkün 
olduğunda, işlem herhangi bir hata oluşturmadığından dolayı genellikle 
en iyi seçimdir. Birçok CAM, hızlı prototipleme ve diğer CAD araçları 
bir STEP dosyasını kabul edecektir.

Hangi ölçek faktörü/katsayısı uygulanırsa uygulansın, STEP dosyası her zaman milimetre birimlerini gösterecektir.
