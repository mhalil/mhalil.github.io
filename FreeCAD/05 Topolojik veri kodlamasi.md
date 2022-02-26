# Topolojik Veri Kodlaması

## Takdim

Burada, `Parça (Part)` modülünü doğrudan FreeCAD Python Yorumlayıcısından veya herhangi bir harici komut dosyasından nasıl kontrol edeceğinizi açıklayacağız. Python komut dosyasının FreeCAD'de nasıl çalıştığı hakkında daha fazla bilgiye ihtiyacınız varsa, [Komut Dosyası](https://wiki.freecadweb.org/Power_users_hub) bölümüne ve [FreeCAD Komut Dosyası Oluşturma Temelleri ](04_FreeCAD_Komut_ Dosyasi_Temelleri.html)sayfalarına göz attığınızdan emin olun. Python'da yeniyseniz, önce [Python'a Giriş](02_Python'a_Giris.html) bölümünü okumak iyi bir fikirdir.

### Ayrıca bakınız

+ [Parça (Part) Komut Dosyası Oluşturmak](05_Parca(Part)_Komut_Dosyasi_Olusturmak.html)

+ [OpenCASCADE](https://wiki.freecadweb.org/OpenCASCADE "OpenCASCADE")

## Sınıf (Class) diyagramı

Bu, `Parça (Part)` modülünün en önemli sınıflarına [Birleşik Modelleme Dili (UML)]((https://tr.wikipedia.org/wiki/UML)) genel bakışıdır:

![](https://wiki.freecadweb.org/images/1/13/Part_Classes.jpg)

**Sınıf diyagramı** [UML](https://tr.wikipedia.org/wiki/UML "UML") 'in en sık kullanılan [diyagramlardan](https://tr.wikipedia.org/wiki/Diyagram "Diyagram") biri olup [nesne yönelimli analiz](https://tr.wikipedia.org/wiki/Nesne_Y%C3%B6nelimli_Analiz_ve_Tasar%C4%B1m "Nesne Yönelimli Analiz ve Tasarım"), tasarım ve [programlamadaki](https://tr.wikipedia.org/wiki/Nesne_y%C3%B6nelimli_programlama "Nesne yönelimli programlama") sınıfları net ve anlaşılabilir şekilde temsil etmeyi amaçlar.

### Geometri

Geometrik nesneler, tüm topolojik nesnelerin yapı taşlarıdır:

+ `Geom` Geometrik nesnelerin Temel sınıfı.

+ `Çizgi` Başlangıç ​​noktası ve bitiş noktası ile tanımlanan 3B düz bir çizgi.

+ `Çember` Çember veya bir merkez noktası ve başlangıç ​​ve bitiş noktası ile tanımlanan daire parçası.

+ vb.

### Topoloji

Aşağıdaki topolojik veri türleri mevcuttur:

+ `Birleşik (Compound)` Herhangi bir tür topolojik nesne grubu.

+ `KompozitKatı (Compsolid)` Kompozit bir katı, yüzleri ile birbirine bağlanmış bir dizi katıdır. TEL (WIRE) ve KABUK (SHELL) kavramlarını katılara genişletir.

+ `Katı (Solid)` Kabukları ile sınırlı alanın bir parçası. Üç boyutlu.

+ `Kabuk (Shell)` Kenarlarıyla birbirine bağlanan bir dizi yüzey. Bir kabuk açık veya kapalı olabilir.

+ `Yüzey (Face)` 2B'de bir düzlemin parçasıdır; 3B'de bir yüzeyin parçasıdır. Geometrisi konturlarla sınırlandırılmıştır (kırpılmıştır). İki boyutludur.

+ `Kafes / Ağ (Wire)` Köşeleri ile birbirine bağlanan bir dizi kenar. Kenarların bağlantılı olup olmamasına bağlı olarak açık veya kapalı kontur olabilir.

+ `Kenar (Edge)` Kısıtlanmış bir eğriye karşılık gelen bir topolojik eleman. Bir kenar genellikle köşelerle sınırlıdır. Tek boyutludur.

+ `Nokta (Vertex)` Bir noktaya karşılık gelen topolojik bir öğe. Boyutsuzdur.

+ `Şekil (Shape)` Yukarıdakilerin tümünü kapsayan genel bir terim.

## Örnek: Basit topoloji oluştur

![](https://wiki.freecadweb.org/images/7/77/Wire.png)

Şimdi daha basit geometriden inşa ederek bir topoloji oluşturacağız. Örnek olay olarak resimde görüldüğü gibi dört köşe (noktası), iki yay ve iki çizgiden oluşan bir parça kullanacağız.

### Geometri Oluştur

İlk önce bu tel yapısının farklı geometrik kısımlarını oluşturuyoruz. Daha sonra bağlanması gereken parçaların aynı köşeleri paylaştığından emin olmak.

Bu yüzden önce noktaları oluşturuyoruz:

```python
import Part
from FreeCAD import Base
V1 = Base.Vector(0, 10, 0)
V2 = Base.Vector(30, 10, 0)
V3 = Base.Vector(30, -10, 0)
V4 = Base.Vector(0, -10, 0)
```

### Yay

![](https://wiki.freecadweb.org/images/e/ec/Circel.png)

Her yay için bir yardımcı noktaya ihtiyacımız var:

```python
VC1 = Base.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = Base.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```

### Çizgi

![](https://wiki.freecadweb.org/images/5/5b/Line.png)

Doğru (Çizgi) parçaları, iki nokta ile oluşturulabilir:

```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```

### Hepsini bir araya getir

Son adım, geometrik temel öğeleri bir araya getirmek ve topolojik bir şekil oluşturmaktır:

```python
S1 = Part.Shape([C1, L1, C2, L2])
```

### Prizma Oluştur

Şimdi oluşturduğunuz tel yapısını, doğrusal olarak bir yönde uzatarak katılayın ve gerçek bir 3B şekil oluşturun:

```python
W = Part.Wire(S1.Edges)
P = W.extrude(Base.Vector(0, 0, 10))
```

### Hepsini Göster

```python
Part.show(P)
```

## Temel Şekiller Oluştur

`Part (Parça)`modülündeki `make...()` yöntemleriyle temel topolojik nesneleri kolayca oluşturabilirsiniz:

```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```

Bazı mevcut `make...()` yöntemleri

+ `makeBox(l, w, h, [p, d])` (**l, w, h**) Boyutlarında **p** Noktasında bulunan ve **d** Yönünü gösteren bir **Kutu** oluşturur.

+ `makeCircle(radius)` Belirli bir Yarıçapa sahip bir **Daire** oluşturur.

+ `makeCone(radius1, radius2, height)` Verilen Yarıçap ve Yükseklikte bir **Koni**oluşturur.

+ `makeCylinder(radius, height)` Belirli bir Yarıçap ve Yükseklikte bir **Silindir** oluşturur.

+ `makeLine((x1, y1, z1), (x2, y2, z2))` İki Nokta ile bir **Çizgi** oluşturur.

+ `makePlane(length, width)` Uzunluğu ve Genişliği belirtilen bir **Düzlem** oluşturur.

+ `makePolygon(list)` Nokta Listesinden bir **Çokgen** oluşturur.

+ `makeSphere(radius)` Belirli bir Yarıçapa sahip bir **Küre** oluşturur.

+ `makeTorus(radius1, radius2)` Verilen Yarıçaplarla bir **Simit, Halka** oluşturur.

Part (Parça) modülünün kullanılabilir yöntemlerinin tam listesi için [Part API](https://wiki.freecadweb.org/Part_API) sayfasına bakın.

### Modülleri İçe Aktar

İlk önce `Part`modülünü içe aktarmalıyız, böylece içeriğini Python'da kullanabiliriz. Ayrıca `Base`modülünü FreeCAD modülünden içe aktaracağız:

```python
import Part
from FreeCAD import Base
```

### Vektör Oluştur

[Vektörler](https://tr.wikipedia.org/wiki/Vekt%C3%B6r), şekiller oluştururken en önemli bilgi parçalarından biridir. Genellikle üç sayı içerirler (ancak her zaman değil): X, Y ve Z kartezyen koordinatları. Bunun gibi bir vektör oluşturursunuz:

```python
myVector = Base.Vector(3, 2, 0)
```

Az önce, (yukarıdaki kodları yazarak) X = 3, Y = 2, Z = 0 koordinatlarında bir vektör oluşturduk. `Part` modülünde vektörler her yerde kullanılır. Parça (Part) şekilleri ayrıca,  `Vertex` adı verilen ve sadece bir vektör için bir konteyner olan başka bir nokta gösterimi türü kullanır. Bir tepe noktasının vektörüne şu şekilde erişirsiniz:

```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```

### Kenar oluştur

Kenar, iki köşesi olan bir çizgiden başka bir şey değildir:

```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Not: İki vektör ile de bir kenar oluşturabilirsiniz:

```python
ec1 = Base.Vector(0, 0, 0)
vec2 = Base.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

Bir kenarın uzunluğunu ve merkezini şöyle bulabilirsiniz:

```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```

### Şekli Ekrana Yerleştir

Şimdiye kadar bir `kenar nesnesi` oluşturduk, ancak ekranın hiçbir yerinde görünmüyor. Bunun nedeni, FreeCAD 3D sahnesinin yalnızca görüntülemesini söylediğiniz şeyi göstermesidir. Bunu yapmak için şu basit yöntemi kullanıyoruz:

```python
Part.show(edge)
```

`show` fonksiyonu, FreeCAD belgemizde bir nesne oluşturur ve ona "**kenar (edge)**" şeklimizi atar. Oluşturduklarınızı ekranda gösterme zamanı geldiğinde bunu kullanın.

### Bir Tel (Yapısı) Oluştur

Bir tel (yapısı), çok kenarlı bir çizgidir ve bir kenar listesinden, hatta bir tel listesinden oluşturulabilir:

```python
edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])
wire3.Edges
> [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
Part.show(wire3)
```

`Part.show(wire3)` komutu, telimizi oluşturan 4 kenarı gösterecektir. Diğer faydalı bilgiler kolayca alınabilir:

```python
wire3.Length
> 40.0
wire3.CenterOfMass
> Vector (5, 5, 0)
wire3.isClosed()
> True
wire2.isClosed()
> False
```

### Bir Yüzey Oluştur

Yalnızca kapalı tellerden oluşturulan yüzeyler geçerli olacaktır. Bu örnekte, tel3 kapalı bir teldir, ancak tel2 kapalı değil (yukarıya bakın, `isClosed()`: Kapalı mı?,  `True`: Doğru / Evet, `False`: Yanlış / Hayır  anlamındadır):

```python
face = Part.Face(wire3)
face.Area
> 99.99999999999999
face.CenterOfMass
> Vector (5, 5, 0)
face.Length
> 40.0
face.isValid()
> True
sface = Part.Face(wire2)
sface.isValid()
> False
```

Yalnız Yüzeylerin bir alanı olacaktır, tel ve kenarların alanı olmaz.

### Bir Çember / Daire Oluştur

Şu şekilde bir çember / daire oluşturulabilir:

```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```

Çemberi, belirli bir konumda ve belirli bir yönde oluşturmak istiyorsanız:

```python
ccircle = Part.makeCircle(10, Base.Vector(10, 0, 0), Base.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```

Çember (`ccircle`), X orijinden 10 birim uzaklıkta oluşturulacak ve X ekseni boyunca dışa bakacaktır. **Not:** `makeCircle()` konum ve normal parametreler için tanımlama gruplarını değil, yalnızca `Base.Vector()`'u kabul eder. Başlangıç ​​ve bitiş açısı vererek çemberin bir bölümünü de oluşturabilirsiniz:

```python
from math import pi
arc1 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 180, 360)
```

Açılar derece cinsinden verilmelidir. Radyan cinsinden veriniz varsa, bunları `derece = radyan * 180/pi` formülünü kullanarak ya da Python'un `math (matematik)` modülünü kullanarak derece cinsine dönüştürün:

```python
import math
degrees = math.degrees(radians)
```

### Noktalar Boyunca Bir Yay Oluştur

Maalesef `makeArc()` fonksiyonu mevcut değil, ancak üç noktadan bir yay oluşturmak için `Part.Arc()` fonksiyonuna sahibiz. Bu fonksiyon başlangıç ​​noktasını, orta nokta üzerinden geçerek bitiş noktasına birleştiren bir yay nesnesi oluşturur.  `Part.makeLine` yerine`Part.LineSegment` kullanırken olduğu gibi, Yay (Arc) nesnesinin `toShape()` fonksiyonu, bir kenar nesnesi elde etmek için çağrılmalıdır.

```python
arc = Part.Arc(Base.Vector(0, 0, 0), Base.Vector(0, 5, 0), Base.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```

`Arc()` noktalar için yalnız `Base.Vector()`'u kabul eder, demetler (tuples) için değil. Bir çemberin bir bölümünü kullanarak da bir yay elde edebilirsiniz:

```python
from math import pi
circle = Part.Circle(Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

Yaylar, çizgiler gibi geçerli kenarlardır, bu nedenle tellerde de kullanılabilirler.

### Çokgen Oluştur

Bir çokgen, basitçe birden çok düz kenarlı bir teldir. `makePolygon()` fonksiyonu, noktaların bir listesini alır ve bu noktalardan geçen bir tel oluşturur:

```python
lshape_wire = Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
```

### Bir Bezier Eğrisi Oluştur

Bezier eğrileri, bir dizi **kutup (nokta)** ve isteğe bağlı **ağırlık** kullanarak düzgün eğrileri modellemek için kullanılır. Aşağıdaki fonksiyon, bir dizi `FreeCAD.Vector()` noktasından bir `Part.BezierCurve()` oluşturur. Not: Tek bir kutup veya ağırlığı "**edinirken**" ve "**ayarlarken (set)**", endeksler 0'dan değil, **1'den başlar**.

```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```

### Bir Düzlem Oluştur

Düzlem, düz dikdörtgen bir yüzeydir. Bir düzlem oluşturmak için kullanılan yöntem şudur;

```python
makePlane(uzunluk, genişlik, [başlangıç_noktası, normalin_yönü]) 
```

Varsayılan değerler aşağıdadır;

`başlangıç_noktası = Vector(0, 0, 0) `

`normalin_yönü = Vector(0, 0, 1)``

Bu parametrelerde;`normalin-yönü = Vector(0, 0, 1)` kullanılması, pozitif Z ekseni yönüne bakan düzlemi oluştururken, `normalin_yönü = Vector(1, 0, 0)` pozitif X ekseni yönüne bakan düzlemi oluşturur:

```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, Base.Vector(3, 0, 0), Base.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```

`BoundBox`, (3, 0, 0) ile başlayan ve (5, 0, 2) ile biten bir köşegen ile düzlemi çevreleyen bir küboiddir (kübik yapıdır. BoundBox'ı, oluşturulan cismin içine sığabileceği en küçük koli hacmi gibi düşünebilirsiniz.). Burada, şeklimiz tamamen düz olduğundan, Y ekseni boyunca `BoundBox` kalınlığı sıfırdır.

**Not**: `makePlane()`,  `başlangıç_noktası` ve `normalin_yönü` için değer olarak yalnız `Base.Vector()`'ü kabul edilir, demetler (tuples) kabul edilmez.

### Bir Elips Oluştur

Bir elips oluşturmanın birkaç yolu vardır:

```python
Part.Ellipse()
```

Bu kod, Merkezi (0, 0, 0) olan büyük yarıçapı 2 ve küçük (ikinci) yarıçapı 1 olan bir elips oluşturur.

```python
Part.Ellipse(Ellipse)
```

Bu kod ise, belirtilen elipsin bir kopyasını oluşturur.

```python
Part.Ellipse(S1, S2, Center)
```

Merkez noktasında ortalanmış bir elips oluşturur; burada elipsin düzlemi Merkez, S1 ve S2 tarafından tanımlanır, ana ekseni Merkez ve S1 tarafından tanımlanır, ana yarıçapı Merkez ile S1 arasındaki mesafedir ve küçük yarıçapı S2 ve ana eksen arasındaki mesafedir.

```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```

Merkez ve normal (0, 0, 1) tarafından tanımlanan düzlemde yer alan büyük ve küçük yarıçaplı bir elips oluşturur.

```python
eli = Part.Ellipse(Base.Vector(10, 0, 0), Base.Vector(0, 5, 0), Base.Vector(0, 0, 0))
Part.show(eli.toShape())
```

Yukarıdaki kodda S1, S2 ve Merkezi (Center) geçtik. `Yay (Arc)`'a benzer şekilde, Ellipse bir kenar değil bir `elips` nesnesi oluşturur, bu nedenle görüntüleme için `toShape()` kullanarak onu bir kenara dönüştürmemiz gerekir.

**Not**: `Ellipse()`, noktalar için yalnız `Base.Vector()`'u kabul eder, demetleri kabul etmez.

```python
eli = Part.Ellipse(Base.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```

Yukarıdaki Ellipse yapıcısı için center, MajorRadius ve MinorRadius'u geçtik.

### Halka (Simit) Oluştur

Halka (Simit) oluşturmak için kullanılacak komut şu şekildedir:

```python
makeTorus(yarıçap1, yarıçap2, [nokta, yön, açı1, açı2, açı])
```

Varsayılan değerler aşağıdadır;

`nokta= Vektör(0, 0, 0)`

`yön = Vektör(0, 0, 1)`

`açı1 = 0`

`açı2 = 360`

`açı = 360`

Halkayı, büyük bir daire boyunca süpürülen küçük bir daire olarak düşünün. `yarıçap1` büyük dairenin yarıçapıdır, `yarıçap2` küçük dairenin yarıçapıdır, `nokta` halkanın merkezidir ve `yön` normal'in yöndür. `açı1` ve `açı2`, küçük daire için derece cinsinden açılardır; son `açı` parametresi halkanın oluşturulacak bölümüdür:

```python
torus = Part.makeTorus(10, 2)
```

Yukarıdaki kod, çapı 20 (yarıçap 10) ve kalınlığı 4 (küçük daire yarıçapı 2) olan bir halka oluşturacaktır.

```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
```

Yukarıdaki kod, halkanın bir dilimini oluşturacaktır.

```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 360, 180)
```

Yukarıdaki kod bir yarı-halka oluşturacaktır; Bunu yapmak için sadece son parametre değiştirilir, yani kalan açılar varsayılan değerlerdir. Açıyı 180 vermek, halka 0'dan 180'e, yani yarım halka oluşturacaktır.

### Bir Kutu veya Küboid oluştur

Bir kutu ya da Küboid oluşturmak için kullanılacak komut şu şekildedir:

```python
makeBox(uzunluk, genişlik, yükseklik, [nokta, yön])
```

Varsayılan değerler aşağıdadır;

`nokta = Vector(0, 0, 0)` 

`yön = Vector(0, 0, 1)`

```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```

### Bir Küre Oluştur

Bir Küre oluşturmak için kullanılacak komut şu şekildedir: 

```python
makeSphere(yarıçap, [nokta, yön, açı1, açı2, açı3]) 
```

Varsayılan değerler aşağıdadır;

`nokta = Vektör(0, 0, 0)``

`yön = Vektör(0, 0, 1)``

`açı1 = -90``

`açı2 = 90`

`açı3 = 360`

Buradaki `açı1` ve `açı2`, kürenin dikey en küçük (minimum) ve en büyük (maksimum) değerleridir, `açı3` ise Kürenin çapıdır.

```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), -90, 90, 180)
```

### Bir Silindir oluştur

Bir Silindir oluşturmak için kullanılacak komut şu şekildedir:

```python
makeCylinder(yarıçap, yükseklik, [nokta, yön, açı]) 
```

Varsayılan değerler aşağıdadır;

`nokta= Vector(0, 0, 0)`` 

`yön = Vector(0, 0, 1)`

`açı = 360`

```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```

### Bir Koni Oluştur

Bir Koni oluşturmak için kullanılacak komut şu şekildedir

```python
makeCone(yarıçap1, yarıçap2, yükseklik, [nokta, yön, açı])
```

Varsayılan değerler aşağıdadır;

`nokta= Vector(0, 0, 0)`

`yön = Vector(0, 0, 1)` 

`açı = 360`

```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```

## Şekilleri Değiştir

Şekilleri değiştirmenin birkaç yolu vardır. Bazıları şekilleri taşıma veya döndürme gibi basit dönüştürme işlemleridir, diğerleri ise bir şekli diğeri ile birleştirme ve çıkarma gibi daha karmaşık işlemlerdir.

## Dönüştürme İşlemleri

### Bir Şekli Dönüştür (Taşı)

Dönüştürme, bir şekli bir yerden başka bir yere taşıma eylemidir. Herhangi bir şekil (kenar, yüzey, küp, vs...) aynı şekilde dönüştürülebilir / taşınabilir:

```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(Base.Vector(2, 0, 0))
```

Bu kod, "**myShape**" şeklimizi, 2 birim X yönünde hareket ettirecektir.

### Bir Şekli Döndür

Bir şekli döndürmek için dönüş merkezini, ekseni ve dönüş açısını belirtmeniz gerekir:

```python
myShape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1), 180)
```

Yukarıdaki kod, şekli Z Ekseni etrafında 180 derece döndürecektir.

### Matris Dönüşümleri

Bir matris, 3B dünyasındaki dönüşümleri depolamak için çok uygun bir yoldur. Tek bir matriste, bir nesneye uygulanacak taşıma (öteleme), döndürme ve ölçekleme değerlerini ayarlayabilirsiniz. Örneğin:

```python
myMat = Base.Matrix()
myMat.move(Base.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
```

**Not**: FreeCAD matrisleri, radyan cinsinden çalışır. Ayrıca, bir vektör alan hemen hemen tüm matris işlemleri de üç sayı alabilir, bu nedenle bu iki satır aynı şeyi yapar:

```python
myMat.move(2, 0, 0)
myMat.move(Base.Vector(2, 0, 0))
```

Matrisimiz ayarlandıktan sonra onu şeklimize uygulayabiliriz. FreeCAD bunu yapmak için iki yöntem sunar: `transformShape()` ve `transformGeometry()`. Aradaki fark, ilkinde hiçbir deformasyon olmayacağından emin olmanızdır (aşağıdaki Şekli Ölçekleme bölümüne bakın). Dönüşümümüzü şu şekilde uygulayabiliriz:

```python
myShape.transformShape(myMat)
```

ya da

```python
myShape.transformGeometry(myMat)
```

### Şekli Ölçeklendir

Bir şekli ölçeklemek daha tehlikeli bir işlemdir, çünkü öteleme veya döndürmeden farklı olarak, eşit olmayan bir şekilde ölçekleme (X, Y ve Z için farklı değerlerle) şeklin yapısını değiştirebilir. Örneğin, yatay olarak dikeyden daha yüksek bir değere sahip bir daireyi ölçeklemek, onu matematiksel olarak çok farklı davranan bir elipse dönüştürecektir. Ölçekleme için `transformShape()`'i kullanamayız, `transformGeometry()` kullanmalıyız:

```python
myMat = Base.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```

## ## Boole (Mantık) İşlemleri

### Çıkarma

FreeCAD'de bir şekli diğerinden çıkarma işlemine "**Cut**" ismi verilir ve işlem şu şekilde gerçekleşir:

```python
cylinder = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
sphere = Part.makeSphere(5, Base.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```

### Kesişim

Aynı şekilde, iki şekil arasındaki kesişim alma işlemine "**Common**" olarak adlandırılır ve işlem şu şekilde gerçekleşir:

```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```

### Birleşim

Birleşim işlemi "**Fuse**"olarak adlandırılır ve işlem şu şekilde gerçekleşir:

```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```

### Kesit

"**Kesit**", katı bir şekil ile bir düzlem şekli arasındaki kesişme noktasıdır. Bu işlem sonucunda, Kenarlardan oluşan bir bileşik eğri olan bir kesişme eğrisi oluşur.

```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
section = cylinder1.section(cylinder2)
section.Wires
> []
section.Edges
> [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
 <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
 <Edge object at 0D8F4BB0>]
```

### Katılamak (Ekstrüzyon)

Katılama (Ekstrüzyon), düzlemsel (2 boyutlu) bir şekli, belirli bir yönde "iterek / çekerek" katı bir gövdeyle sonuçlanan eylemdir. "**Dışarı iterek**" bir **tüp (boru)** haline gelen bir **daire **düşünün:

```python
circle = Part.makeCircle(10)
tube = circle.extrude(Base.Vector(0, 0, 2))
```

Dairenizin içi boşsa, içi boş bir tüp/boru elde edeceksiniz. Daireniz aslında içi dolgulu bir diskse, sağlam bir silindir elde edeceksiniz:

```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(Base.Vector(0, 0, 2))
```

## Şekilleri Keşfedin

### Kenar analizi

### Bir Seçim Kullanın

## Örnek: OCC şişesi

### Komut Dosyası

### Detaylı Açıklama

## Örnek: Delinmiş Kutu

### Yüklemek ve Kaydetmek

Kaynak: [Topological data scripting](https://wiki.freecadweb.org/Topological_data_scripting)
