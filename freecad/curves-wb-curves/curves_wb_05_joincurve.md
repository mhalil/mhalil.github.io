Title: FreeCAD - Curves WB - Curves - 05 - JoinCurve
Date: 2022-11-15 00:00
Modified: 2023-03-21 00:00
Category: Curves WB - Curves
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Join, Curve
Author: Mustafa Halil

# ![Curves_JoinCurve](../../images/freecad/curves_wb/simgeler/curves/joinCurves.svg) JoinCurve:

**JoinCurve** komutu <u>seçilen çizgileri/eğrileri birleştirerek tek bir Bezier Eğri (BSpline) haline getirir.</u>  

**Kullanım:** 
Komutu çalıştırmak için aşağıdaki işlemleri sırasıyla uygulayın:

- 3B görünümde bir veya birkaç kenar seçin. (birden fazla seçim için `CTRL` tuşunu kullanın)
- Kenarlar art arda eklenmelidir. Eskizden (Sketch'ten) , herhangi bir şeklin kenarları seçilebilir.
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves** menüsündeki **JoinCurve** seçeneğini kullanın.
- İşlem sonunda tüm seçili kenarlar birleştirilerek tek bir Bezier eğri (BSpline) olur.

**JoinCurve** komutunu ve özelliklerini bir uygulama yaparak öğrenmeye çalışalım.  
Aşağıdaki resimde görüldüğü üzere elimizde bir adet altıgen eskiz ve bir adet dikdörtgenler prizması var.
 ![JoinCurve_01](../../images/freecad/curves_wb/curves_menu/JoinCurve_01.png) Sahnede bulunan dikdörtgenler prizmasının 5 kenarını seçelim.
 ![JoinCurve_02](../../images/freecad/curves_wb/curves_menu/JoinCurve_02.png) Seçimi, sıralı olarak gerçekleştirelim yani birbirini takip eden kenarları ardarda seçelim ve **JoinCurve** komutunu çalıştıralım.
 ![JoinCurve_03](../../images/freecad/curves_wb/curves_menu/JoinCurve_03.png) Unsur ağacına bakarsak, sahneye **JoinCurve** adında yeni bir nesne eklendiğini görürüz. Yeni nesneyi net olarak görmek için dikdörtgenler prizmasını gizliyorum.  
3B sahnesinde JoinCurve nesnesinin herhangi bir noktası 
seçildiğinde bütün eğri seçili hale gelir. Aşağıdaki resimde seçili 
kısımlar yeşil renk ile gösteriliyor.
 ![JoinCurve_04](../../images/freecad/curves_wb/curves_menu/JoinCurve_04.png) **Corner Break (Köşe Kır)** parametresi **true (doğru/evet)** olarak değiştirildiğinde, **JoinCurve** nesnesinin her bir çizgi parçası ayrı ayrı seçilebilir hale geliyor. 
Aşağıdaki resimde seçili kısımlar yeşil renk ile gösteriliyor.
 ![JoinCurve_05](../../images/freecad/curves_wb/curves_menu/JoinCurve_05.png) **Force Closed (Kapatmaya Zorla)** parametresi **true (doğru/evet)** olarak ayarlanırsa, **JoinCurve** eğrisinin, uç noktaları birleştirilir ve kapalı eğri oluşturması sağlanır.  
**Corner Break** parametresini **false (yanlış/hayır)** olarak ayarlı iken **Force Closed (Kapatmaya Zorla)** parametresi **true (doğru/evet)** olarak ayarlandığında elde edilen sonuç aşağıdadır.
 ![JoinCurve_06](../../images/freecad/curves_wb/curves_menu/JoinCurve_06.png) **Corner Break** parametresini **true (doğru/evet)** olarak ayarlı iken **Force Closed (Kapatmaya Zorla)** parametresi **true (doğru/evet)** olarak ayarlandığında ise elde edilen sonuç aşağıdadır. **Corner Break** parametresi aktif olduğu için her bir çizgi bağımsız gibi hareket 
ederek başlangıç ve uç nokta birleşmiş oluyor ve bu kez son çizgi 
parçası, önceki çizgiden ayrılıyor.
 ![JoinCurve_07](../../images/freecad/curves_wb/curves_menu/JoinCurve_07.png) **Shape Approximation** Özelliği Aktifleştirildiğinde, **JoinCurve** nesnesi , değiştirilen parametre değerlerine bağlı olarak farklı 
şekiller almaya başlıyor. Örneği aşağıdaki resme bakarsanız, sadece **Active** parametresi **true (doğru/evet)** olarak değiştirildiğinde, eğriye ait keskin köşelerde bir yumuşama/yuvarlanma olmaya başlandı.
 ![JoinCurve_08](../../images/freecad/curves_wb/curves_menu/JoinCurve_08.png) **Approx Tolerance** parametre değeri artırıldığında yumuşama/radyus değeri de artıyor.
 ![JoinCurve_09](../../images/freecad/curves_wb/curves_menu/JoinCurve_09.png) **Approx Tolerance** parametre değeri daha fazla artırıldığında, eğrinin uç noktalarında da radyus etkisi görülmeye başlanıyor.
 ![JoinCurve_10](../../images/freecad/curves_wb/curves_menu/JoinCurve_10.png) **Continuity (Süreklilik)** parametresi, açılır
 listeden çıkan seçeneklerden birinin seçilerek ayarlandığı 
özelliklerden biridir. Bu değerler, eğrinin oluşturulması aşamasında 
kullanılan algoritmik değerlerdir desek yanlış olmaz sanırım. Değeri **C3**'ten **C0**'a değiştirildiğinde elde edilen eğri profili aşağıdaki şekilde değişiyor.
 ![JoinCurve_11](../../images/freecad/curves_wb/curves_menu/JoinCurve_11.png) **Continuity (Süreklilik)** parametresi **CN** olarak ayarladığımızda ise eğri yine farklı bir hal alıyor.
 ![JoinCurve_12](../../images/freecad/curves_wb/curves_menu/JoinCurve_12.png) **Samples (Örnekleme)** parametresi, tabiri 
caizse eğrinin kaç adet çizgi parçasının uç uca eklenmesi ile elde 
edileceğini belirlediğimiz kısımdır. Değer büyüdükçe, seçili kenarlara 
daha yakın profilde eğri oluşuyor. Değeri düşürerek eğrinin alacağı 
şekli inceleyelim.
 ![JoinCurve_13](../../images/freecad/curves_wb/curves_menu/JoinCurve_13.png) Altıgen Eskiz ve JoinCurve nesnelerini kullanarak **Part Workbench (Parça Çalışma Tezgahı)** komutlarından **Sweep... (Süpür...)**'i çalıştıralım.
 ![JoinCurve_14](../../images/freecad/curves_wb/curves_menu/JoinCurve_14.png) Curves araç çubuğunda bulunan ilgili düğmeye basarak ya da **Part (Parça)** menüsündeki **Sweep... (Süpür...)** komutunu çalıştır.
 ![JoinCurve_15](../../images/freecad/curves_wb/curves_menu/JoinCurve_15.png) Profil olarak **Sketch_Altıgen**'i, süpürülecek yol (**Yolu Süper**) olarak **JoinCurve** eğrisini (3B sahnesinden) seçip onaylayalım.
 ![JoinCurve_16](../../images/freecad/curves_wb/curves_menu/JoinCurve_16.png) Oluşan 3 boyutlu **Altıgen Boru/Kanal** nesnesi aşağıda görülmektedir.
 ![JoinCurve_17](../../images/freecad/curves_wb/curves_menu/JoinCurve_17.png) Unsur ağacından **JoinCurve** nesnesini seçip **Corner Break (Köşe Kır)** parametresini **true (doğru/evet)** olarak değiştirirsek elde edeceğimiz nesne aşağıdaki hale gelir.
 ![JoinCurve_18](../../images/freecad/curves_wb/curves_menu/JoinCurve_18.png) **Continuity (Süreklilik)** parametresi **C0** olarak değiştirildiğinde 3 boyutlu şeklin aldığı hal aşağıdaki gibidir.
 ![JoinCurve_19](../../images/freecad/curves_wb/curves_menu/JoinCurve_19.png) **Continuity (Süreklilik)** parametresi **C0** iken **Reverse (Ters Çevir)** parametresi **true** olarak değiştirildiğinde 3 boyutlu şeklin aldığı hal aşağıdaki gibidir.
 ![JoinCurve_20](../../images/freecad/curves_wb/curves_menu/JoinCurve_20.png) **Continuity (Süreklilik)** parametrelerini değiştirildiğinde 3 boyutlu şeklin aldığı hali kendiniz inceleyerek görebilirsiniz.  
**Samples (Örnekleme)** değerini düşürerek aşağıdaki şekli elde edebilirsiniz.  
Gördüğünüz gibi, Eğri parametreleri değiştiğinde oluşan 
eğrinin şekli ve eğriye bağlı olan 3 boyutlu nesnenin şekli de 
değişiyor.
 ![JoinCurve_21](../../images/freecad/curves_wb/curves_menu/JoinCurve_21.png)

[<<< Curves Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_00_curves_menu.md)
