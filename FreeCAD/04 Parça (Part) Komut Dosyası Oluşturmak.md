# 05 Parça (Part) Komut Dosyası Oluşturmak

## Takdim

`Part (Parça)` modülünde kullanılan ana veri yapısı, [OpenCASCADE](https://wiki.freecadweb.org/OpenCASCADE)'den [BRep](http://en.wikipedia.org/wiki/Boundary_representation) veri türüdür. `Part` modülünün hemen hemen tüm içeriği ve nesne türleri, Python komut dosyasında mevcuttur. Bu, **Çizgiler**, **Daireler** ve **Yaylar** gibi geometrik temel şekilleri ve **Noktalar, Kenarlar, Kafes/Ağ Yapıları, Yüzeyler, Katılar ve Bileşikler** gibi tüm **TopoShapes** aralığını içerir. Bu nesnelerin her biri için çeşitli oluşturma yöntemleri mevcuttur ve bazıları için, özellikle **TopoShapes** için, **boole birleşim/fark/kesişim** gibi gelişmiş işlemler de mevcuttur. Daha fazla bilgi için [FreeCAD Komut Dosyası Oluşturma Temelleri](04_FreeCAD_Komut_ Dosyasi_Temelleri.html) sayfasında açıklandığı gibi `Part (Parça)` modülünün içeriğini keşfedin.

Oluşturulabilecek en temel nesne, basit bir *Data* `Placement` özelliğini, rengini ve görünümünü tanımlayan temel özelliklere sahip bir [Parça Özelliğidir (Part Feature)](https://wiki.freecadweb.org/Part_Feature).

2B geometrik nesnelerde kullanılan diğer bir basit nesne, [Sketcher SketchObject](https://wiki.freecadweb.org/Sketcher_SketchObject) ve çoğu [Draft öğelerinin](https://wiki.freecadweb.org/Draft_Workbench) temeli olan [Part Part2DObject](https://wiki.freecadweb.org/Part_Part2DObject)'dir.

### Ayrıca bakınız

+ [Topolojik veri kodlaması](https://wiki.freecadweb.org/Topological_data_scripting)
+ [OpenCASCADE](https://wiki.freecadweb.org/OpenCASCADE)

## Test komut dosyası

Bir komut dosyasıyla [Parça Temel Şekillerinin](https://wiki.freecadweb.org/Part_Primitives) oluşturulmasını test edin. *0.19 sürümünde tanıtıldı*

```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Bu betik (script), programın kurulum dizininde bulunur ve temel şekillerin nasıl oluşturulduğunu görmek için incelenebilir.

```
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

## Örnekler

### Çizgi

Bir çizgi öğesi oluşturmak için [Python konsolu](https://wiki.freecadweb.org/Python_console)na geçin ve şunu girin:

```python
import FreeCAD as App
import Part

doc = App.newDocument()

line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
obj = doc.addObject("Part::Feature", "Line")
obj.Shape= line.toShape()

doc.recompute()
```

Yukarıdaki Python örneğini adım adım inceleyelim:

```python
import FreeCAD as App
import Part
doc = App.newDocument()
```

Bu, FreeCAD ve `Part (Parça)` modüllerini yükler ve yeni bir belge oluşturur.

```python
line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
```

Çizgi (`line`) aslında bir çizgi parçasıdır, dolayısıyla başlangıç ve bitiş noktası vardır.

```python
obj = doc.addObject("Part::Feature", "Line")
obj.Shape= line.toShape()
```

Bu, belgeye bir `Parça (Part) `nesne türü ekler ve çizgi parçasının şekil temsilini, eklenen nesnenin `Shape` özelliğine atar. Burada bir `TopoShape `oluşturmak için bir geometrik temel şekil (`Part.LineSegment`) kullandığımızı anlamak önemlidir (`toShape` yöntemiyle). Belgeye yalnız şekil eklenebilir. FreeCAD'de geometrik temel şekilleri "**bina yapıları**" olarak kullanılır.

    doc.recompute()

Bu komut belgeyi günceller. Bu aynı zamanda yeni Part nesnesinin görsel temsilini de hazırlar.

Bir  çizgi parçasının başlangıç ​​ve bitiş noktası doğrudan yapıcıda belirtilerek de oluşturulabileceğini unutmayın, örneğin `Part.LineSegment(nokta1, nokta2)` veya burada yaptığımız gibi varsayılan bir çizgi oluşturup özelliklerini daha sonra ayarlayabiliriz.

Bir Çizgi, ayrıca şu kod bloğunu yazarak (fonksiyon oluşturarak) ta oluşturuşabilir: 

```python
import FreeCAD as App
import Part

def my_create_line(pt1, pt2, obj_name):
    obj = App.ActiveDocument.addObject("Part::Line", obj_name)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    App.ActiveDocument.recompute()
    return obj

line = my_create_line((0, 0, 0), (0, 10, 0), "LineName")
```

# Çember / Daire

Bir çember / daire benzer şekilde oluşturulabilir:

```python
import FreeCAD as App
import Part

doc = App.activeDocument()

circle = Part.Circle() 
circle.Radius = 10.0  
obj = doc.addObject("Part::Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Veya şu kod bloğunu yazarak (fonksiyon oluşturarak) ta çember oluşturabilisiniz:

```python
import FreeCAD as App
import Part

def my_create_circle(rad, obj_name):
    obj = App.ActiveDocument.addObject("Part::Circle", obj_name)
    obj.Radius = rad

    App.ActiveDocument.recompute()
    return obj

circle = my_create_circle(5.0, "CircleName")
```

Alternatif olarak, merkezini, eksenini ve yarıçapını tanımlayarak bir daire oluşturabiliriz:

```python
import FreeCAD as App
import Part

doc = App.activeDocument()

center = App.Vector(1, 2, 3)
axis = App.Vector(1, 1, 1)
radius = 10
circle = Part.Circle(center, axis, radius)
obj = doc.addObject("Part::Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Veya çember çevresi üzerinde üç nokta tanımlayarak (3 noktaya teğet çember):

```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(0, 0, 10)
circle = Part.Circle(p1, p2, p3)
obj = doc.addObject("Part::Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Tekrar  not edin, bir şekil oluşturmak için daireyi (geometrik temel şekilleri) kullandık. Elbette daha sonra aşağıdakileri yaparak yapı geometrimize hala erişebiliriz:

```python
shape = obj.Shape
edge = shape.Edges[0]
curve = edge.Curve
```

Burada  nesnemizin (`obj`)  Şeklini (`Shape`) ve ardından Kenarlar (`edges`) listesini alıyoruz. Bu durumda şekli tek bir daireden oluşturduğumuz için sadece bir kenar olacaktır.  Bu yüzden Kenarlar listesinde yalnızca ilk öğeyi alıyoruz ve ardından eğrisini (`curve`) alıyoruz. Her kenarın, dayandığı geometrik temel nesne olan bir  Eğrisi vardır.

# Yay

Bir yay şu şekilde oluşturulabilir:

```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
arc = Part.Arc(p1, p2, p3)
obj = doc.addObject("Part::Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

Bu kod,  yarım daire çizer. Merkez (0, 0, 0) konumundadır. Yarıçap 10'dur. P1, +X eksenindeki başlangıç ​​noktasıdır. P2, +Y ekseninde orta nokta ve P3, -X ekseninde bitiş noktasıdır.

Ayrıca bir çemberden bir yay da oluşturabiliriz:

```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
circle = Part.Circle(p1, p2, p3)
arc = Part.ArcOfCircle(circle, 0.0, 0.7854)
obj = doc.addObject("Part::Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

Bu kodun çalışabilmesi için bir daireye ve radyan cinsinden bir başlangıç ​​açısına ve bitiş açısına ihtiyacı var.

Kaynak: [Part scripting - FreeCAD Documentation](https://wiki.freecadweb.org/Part_scripting)
