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

## Geometri

Geometrik nesneler, tüm topolojik nesnelerin yapı taşlarıdır:

+ `Geom` Geometrik nesnelerin Temel sınıfı.

+ `Çizgi` Başlangıç ​​noktası ve bitiş noktası ile tanımlanan 3B düz bir çizgi.

+ `Çember` Çember veya bir merkez noktası ve başlangıç ​​ve bitiş noktası ile tanımlanan daire parçası.

+ vb.

## Topoloji

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

## Örnek: Basit topoloji oluşturun

![](https://wiki.freecadweb.org/images/7/77/Wire.png)

Şimdi daha basit geometriden inşa ederek bir topoloji oluşturacağız. Örnek olay olarak resimde görüldüğü gibi dört köşe (noktası), iki yay ve iki çizgiden oluşan bir parça kullanacağız.

## Geometri Oluşturmak

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

## Yay

![](https://wiki.freecadweb.org/images/e/ec/Circel.png)

Her yay için bir yardımcı noktaya ihtiyacımız var:

```python
VC1 = Base.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = Base.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```

## Çizgi

![](https://wiki.freecadweb.org/images/5/5b/Line.png)

Doğru (Çizgi) parçaları, iki nokta ile oluşturulabilir:

```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```

## Hepsini bir araya getirmek

Son adım, geometrik temel öğeleri bir araya getirmek ve topolojik bir şekil oluşturmaktır:

```python
S1 = Part.Shape([C1, L1, C2, L2])
```

## Prizma Yapmak/Oluşturmak

Şimdi oluşturduğunuz tel yapısını, doğrusal olarak bir yönde uzatarak katılayın ve gerçek bir 3B şekil oluşturun:

```python
W = Part.Wire(S1.Edges)
P = W.extrude(Base.Vector(0, 0, 10))
```

## Hepsini Göster

```python
Part.show(P)
```

## Temel Şekiller Oluşturun

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

## Modülleri İçe Aktar

İlk önce `Part`modülünü içe aktarmalıyız, böylece içeriğini Python'da kullanabiliriz. Ayrıca `Base`modülünü FreeCAD modülünden içe aktaracağız:

```python
import Part
from FreeCAD import Base
```

## Vektör Oluştur

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

## Kenar oluştur

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

## Şekli Ekrana Yerleştir

Şimdiye kadar bir `kenar nesnesi` oluşturduk, ancak ekranın hiçbir yerinde görünmüyor. Bunun nedeni, FreeCAD 3D sahnesinin yalnızca görüntülemesini söylediğiniz şeyi göstermesidir. Bunu yapmak için şu basit yöntemi kullanıyoruz:

```python
Part.show(edge)
```

`show` fonksiyonu, FreeCAD belgemizde bir nesne oluşturur ve ona "**kenar (edge)**" şeklimizi atar. Oluşturduklarınızı ekranda gösterme zamanı geldiğinde bunu kullanın.

## Bir Tel (Yapısı) Oluşturun

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

## Bir Yüzey Oluştur

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

## Bir Çember / Daire Oluştur

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

## Noktalar Boyunca Bir Yay Oluşturun

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

## Çokgen Oluştur

Bir çokgen, basitçe birden çok düz kenarlı bir teldir. `makePolygon()` fonksiyonu, noktaların bir listesini alır ve bu noktalardan geçen bir tel oluşturur:

```python
lshape_wire = Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
```

## Bir Bezier Eğrisi Oluşturun

Kaynak: [Topological data scripting](https://wiki.freecadweb.org/Topological_data_scripting)
