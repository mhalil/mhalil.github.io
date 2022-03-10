# Komut Dosyasıyla Yazılmış Nesneler

## Takdim

Açıklamalar, ağlar ve parça nesneleri gibi standart nesne türlerinin yanı sıra, FreeCAD ayrıca [Python Özellikleri](https://wiki.freecadweb.org/App_FeaturePython) adı verilen %100 python komut dosyasıyla oluşturulmuş parametrik nesneler oluşturmak için harika bir olanak sunar. Bu nesneler, tam olarak diğer herhangi bir FreeCAD nesnesi gibi davranacak ve dosya kaydetme/yükleme sırasında otomatik olarak kaydedilecek ve geri yüklenecektir.

Anlaşılması, bilinmesi gereken bir husus var, o da şudur: FreeCAD dosyaları hiçbir zaman gömülü kod taşımaz, bu güvenlik nedenleriyledir. Parametrik nesneler oluşturmak için yazdığınız Python kodu, hiçbir zaman bir dosyanın içine kaydedilmez. Bu, başka bir makinede (bilgisayarda) böyle bir nesne içeren bir dosyayı açarsanız, bu python kodu o makinede (bilgisayarda) mevcut değilse, nesnenin tamamen yeniden oluşturulmayacağı anlamına gelir. Bu tür nesneleri başkalarına dağıtırsanız (gönderirseniz), Python komut dosyanızı da örneğin bir [Makro](https://wiki.freecadweb.org/Macros) olarak dağıtmanız, göndermeniz gerekir.

**Not:** Python kodunu bir `App::PropertyPythonObject` ile `json`serileştirmeyi kullanarak bir FreeCAD dosyası içinde paketlemek (yerleştirmek) mümkündür, ancak bu kod hiçbir zaman doğrudan çalıştırılamaz ve bu nedenle buradaki amacımız için çok kullanışlı değildir.

[Python Özellikleri](https://wiki.freecadweb.org/App_FeaturePython), tüm FreeCAD özellikleriyle aynı kuralı izler: `App`ve `GUI`bölümlerine ayrılırlar. `App` bölümü, Belge Nesnesi, nesnemizin geometrisini tanımlarken, `GUI` bölümü, Görünüm Sağlayıcı Nesnesi, nesnenin ekranda nasıl çizileceğini tanımlar. Görünüm Sağlayıcı Nesnesi, diğer FreeCAD özellikleri gibi, yalnızca FreeCAD'i kendi GUI'sinde çalıştırdığınızda kullanılabilir. Nesnenizi oluşturmak için kullanılabilecek birkaç özellik ve yöntem vardır. Özellikler, FreeCAD'in sunduğu önceden tanımlanmış özellik türlerinden herhangi biri olmalıdır ve kullanıcı tarafından düzenlenebilmeleri için özellik görünümü penceresinde görünecektir. Bu şekilde, `FeaturePython` nesneleri gerçekten ve tamamen parametriktir. `Object` ve `ViewObject` için özellikleri ayrı ayrı tanımlayabilirsiniz.

Basit / Temel Örnek

Aşağıdaki örnek, diğer birkaç örnekle birlikte  [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) dosyasında bulunabilir:

```python
''Examples for a feature class and its view provider.'''

import FreeCAD, FreeCADGui
from pivy import coin

class Box:
    def __init__(self, obj):
        '''Add some custom properties to our box feature'''
        obj.addProperty("App::PropertyLength","Length","Box","Length of the box").Length=1.0
        obj.addProperty("App::PropertyLength","Width","Box","Width of the box").Width=1.0
        obj.addProperty("App::PropertyLength","Height","Box", "Height of the box").Height=1.0
        obj.Proxy = self

    def onChanged(self, fp, prop):
        '''Do something when a property has changed'''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def execute(self, fp):
        '''Do something when doing a recomputation, this method is mandatory'''
        FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")

class ViewProviderBox:
    def __init__(self, obj):
        '''Set this object to the proxy object of the actual view provider'''
        obj.addProperty("App::PropertyColor","Color","Box","Color of the box").Color=(1.0,0.0,0.0)
        obj.Proxy = self

    def attach(self, obj):
        '''Setup the scene sub-graph of the view provider, this method is mandatory'''
        self.shaded = coin.SoGroup()
        self.wireframe = coin.SoGroup()
        self.scale = coin.SoScale()
        self.color = coin.SoBaseColor()

        data=coin.SoCube()
        self.shaded.addChild(self.scale)
        self.shaded.addChild(self.color)
        self.shaded.addChild(data)
        obj.addDisplayMode(self.shaded,"Shaded");
        style=coin.SoDrawStyle()
        style.style = coin.SoDrawStyle.LINES
        self.wireframe.addChild(style)
        self.wireframe.addChild(self.scale)
        self.wireframe.addChild(self.color)
        self.wireframe.addChild(data)
        obj.addDisplayMode(self.wireframe,"Wireframe");
        self.onChanged(obj,"Color")

    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        # fp is the handled feature, prop is the name of the property that has changed
        l = fp.getPropertyByName("Length")
        w = fp.getPropertyByName("Width")
        h = fp.getPropertyByName("Height")
        self.scale.scaleFactor.setValue(float(l),float(w),float(h))
        pass

    def getDisplayModes(self,obj):
        '''Return a list of display modes.'''
        modes=[]
        modes.append("Shaded")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self):
        '''Return the name of the default display mode. It must be defined in getDisplayModes.'''
        return "Shaded"

    def setDisplayMode(self,mode):
        '''Map the display mode defined in attach with those defined in getDisplayModes.\
                Since they have the same names nothing needs to be done. This method is optional'''
        return mode

    def onChanged(self, vp, prop):
        '''Here we can do something when a single property got changed'''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        if prop == "Color":
            c = vp.getPropertyByName("Color")
            self.color.rgb.setValue(c[0],c[1],c[2])

    def getIcon(self):
        '''Return the icon in XPM format which will appear in the tree view. This method is\
                optional and if not defined a default icon is shown.'''
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "   c None",
            ".  c #141010",
            "+  c #615BD2",
            "@  c #C39D55",
            "#  c #000000",
            "$  c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def __getstate__(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def __setstate__(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None

def makeBox():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Box")
    Box(a)
    ViewProviderBox(a.ViewObject)

makeBox()
```

## Dikkat Edilmesi Gerekenler

Nesneniz oluşturulur oluşturulmaz yeniden hesaplanması gerekiyorsa, otomatik olarak çağrılmadığı için bunu `__init__` işlevinde manuel olarak yapmanız gerekir. `Box`sınıfının `onChanged` yöntemi,  `execute` (çalıştır) fonksiyonuyla aynı etkiye sahip olduğu için bu örnek buna gerek duymaz, ancak aşağıdaki örnekler, 3B görünümde herhangi bir şey görüntülenmeden önce yeniden hesaplanma mantığına dayanır. Örneklerde bu, `ActiveDocument.recompute()` ile manuel olarak yapılır, ancak daha karmaşık senaryolarda, tüm belgenin veya `FeaturePython` nesnesinin nerede yeniden hesaplanacağına karar vermeniz gerekir.

Bu örnek, **rapor görünümü penceresi**nde bir dizi istisna yığını izi üretir. Bunun nedeni, `__init__` içine her özellik eklendiğinde `Box` sınıfının `onChanged` yönteminin çağrılmasıdır. İlki eklendiğinde, **Genişlik** ve **Yükseklik** özellikleri henüz mevcut değildir ve bu nedenle bunlara erişme girişimi başarısız olur.

`__getstate__` ve `__setstate__` için bir açıklama [obj.Proxy.Type is a dict, not a string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009&start=10#p377892) forum başlığında bulunmaktadır.

## Mevcut Yöntemler / Metotlar

[PythonÖzelliği Yöntemleri](https://wiki.freecadweb.org/FeaturePython_methods "FeaturePython methods") tüm referans kaynak için sayfaya bakın.

## Kullanılabilir Özellikler

Özellikler, `FeaturePython` nesnelerinin gerçek yapı taşlarıdır. Bunlar aracılığıyla, kullanıcı etkileşimde bulunabilecek ve nesnenizi değiştirebilecektir. Belgenizde yeni bir `FeaturePython` nesnesi oluşturduktan sonra (`obj=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Box")`), aşağıdaki kodu yazarak, kullanılabilir özelliklerin bir listesini elde edebilirsiniz:

```python
obj.supportedProperties()
```

[FeaturePython Özel Özellikler](https://wiki.freecadweb.org/FeaturePython_Custom_Properties) sayfasında daha ayrıntılı olarak açıklanan mevcut özelliklerin bir listesini elde edeceksiniz:

- [App::PropertyAcceleration](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyAcceleration "FeaturePython Custom Properties")
- [App::PropertyAngle](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyAngle "FeaturePython Custom Properties")
- [App::PropertyArea](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyArea "FeaturePython Custom Properties")
- [App::PropertyBool](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyBool "FeaturePython Custom Properties")
- [App::PropertyBoolList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyBoolList "FeaturePython Custom Properties")
- [App::PropertyColor](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyColor "FeaturePython Custom Properties")
- [App::PropertyColorList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyColorList "FeaturePython Custom Properties")
- [App::PropertyDirection](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyDirection "FeaturePython Custom Properties")
- [App::PropertyDistance](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyDistance "FeaturePython Custom Properties")
- [App::PropertyEnumeration](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyEnumeration "FeaturePython Custom Properties")
- [App::PropertyExpressionEngine](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyExpressionEngine "FeaturePython Custom Properties")
- [App::PropertyFile](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFile "FeaturePython Custom Properties")
- [App::PropertyFileIncluded](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFileIncluded "FeaturePython Custom Properties")
- [App::PropertyFloat](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFloat "FeaturePython Custom Properties")
- [App::PropertyFloatConstraint](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFloatConstraint "FeaturePython Custom Properties")
- [App::PropertyFloatList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFloatList "FeaturePython Custom Properties")
- [App::PropertyFont](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFont "FeaturePython Custom Properties")
- [App::PropertyForce](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyForce "FeaturePython Custom Properties")
- [App::PropertyFrequency](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyFrequency "FeaturePython Custom Properties")
- [App::PropertyInteger](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyInteger "FeaturePython Custom Properties")
- [App::PropertyIntegerConstraint](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyIntegerConstraint "FeaturePython Custom Properties")
- [App::PropertyIntegerList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyIntegerList "FeaturePython Custom Properties")
- [App::PropertyIntegerSet](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyIntegerSet "FeaturePython Custom Properties")
- [App::PropertyLength](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLength "FeaturePython Custom Properties")
- [App::PropertyLink](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLink "FeaturePython Custom Properties")
- [App::PropertyLinkChild](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkChild "FeaturePython Custom Properties")
- [App::PropertyLinkGlobal](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkGlobal "FeaturePython Custom Properties")
- [App::PropertyLinkHidden](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkHidden "FeaturePython Custom Properties")
- [App::PropertyLinkList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkList "FeaturePython Custom Properties")
- [App::PropertyLinkListChild](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkListChild "FeaturePython Custom Properties")
- [App::PropertyLinkListGlobal](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkListGlobal "FeaturePython Custom Properties")
- [App::PropertyLinkListHidden](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkListHidden "FeaturePython Custom Properties")
- [App::PropertyLinkSub](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSub "FeaturePython Custom Properties")
- [App::PropertyLinkSubChild](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubChild "FeaturePython Custom Properties")
- [App::PropertyLinkSubGlobal](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubGlobal "FeaturePython Custom Properties")
- [App::PropertyLinkSubHidden](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubHidden "FeaturePython Custom Properties")
- [App::PropertyLinkSubList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubList "FeaturePython Custom Properties")
- [App::PropertyLinkSubListChild](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubListChild "FeaturePython Custom Properties")
- [App::PropertyLinkSubListGlobal](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubListGlobal "FeaturePython Custom Properties")
- [App::PropertyLinkSubListHidden](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyLinkSubListHidden "FeaturePython Custom Properties")
- [App::PropertyMap](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyMap "FeaturePython Custom Properties")
- [App::PropertyMaterial](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyMaterial "FeaturePython Custom Properties")
- [App::PropertyMaterialList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyMaterialList "FeaturePython Custom Properties")
- [App::PropertyMatrix](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyMatrix "FeaturePython Custom Properties")
- [App::PropertyPath](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPath "FeaturePython Custom Properties")
- [App::PropertyPercent](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPercent "FeaturePython Custom Properties")
- [App::PropertyPersistentObject](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPersistentObject "FeaturePython Custom Properties")
- [App::PropertyPlacement](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPlacement "FeaturePython Custom Properties")
- [App::PropertyPlacementLink](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPlacementLink "FeaturePython Custom Properties")
- [App::PropertyPlacementList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPlacementList "FeaturePython Custom Properties")
- [App::PropertyPosition](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPosition "FeaturePython Custom Properties")
- [App::PropertyPrecision](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPrecision "FeaturePython Custom Properties")
- [App::PropertyPressure](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPressure "FeaturePython Custom Properties")
- [App::PropertyPythonObject](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyPythonObject "FeaturePython Custom Properties")
- [App::PropertyQuantity](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyQuantity "FeaturePython Custom Properties")
- [App::PropertyQuantityConstraint](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyQuantityConstraint "FeaturePython Custom Properties")
- [App::PropertySpeed](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertySpeed "FeaturePython Custom Properties")
- [App::PropertyString](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyString "FeaturePython Custom Properties")
- [App::PropertyStringList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyStringList "FeaturePython Custom Properties")
- [App::PropertyUUID](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyUUID "FeaturePython Custom Properties")
- [App::PropertyVacuumPermittivity](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyVacuumPermittivity "FeaturePython Custom Properties")
- [App::PropertyVector](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyVector "FeaturePython Custom Properties")
- [App::PropertyVectorDistance](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyVectorDistance "FeaturePython Custom Properties")
- [App::PropertyVectorList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyVectorList "FeaturePython Custom Properties")
- [App::PropertyVolume](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyVolume "FeaturePython Custom Properties")
- [App::PropertyXLink](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyXLink "FeaturePython Custom Properties")
- [App::PropertyXLinkList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyXLinkList "FeaturePython Custom Properties")
- [App::PropertyXLinkSub](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyXLinkSub "FeaturePython Custom Properties")
- [App::PropertyXLinkSubList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#App::PropertyXLinkSubList "FeaturePython Custom Properties")
- [Mesh::PropertyCurvatureList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Mesh::PropertyCurvatureList "FeaturePython Custom Properties")
- [Mesh::PropertyMeshKernel](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Mesh::PropertyMeshKernel "FeaturePython Custom Properties")
- [Mesh::PropertyNormalList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Mesh::PropertyNormalList "FeaturePython Custom Properties")
- [Part::PropertyFilletEdges](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Part::PropertyFilletEdges "FeaturePython Custom Properties")
- [Part::PropertyGeometryList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Part::PropertyGeometryList "FeaturePython Custom Properties")
- [Part::PropertyPartShape](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Part::PropertyPartShape "FeaturePython Custom Properties")
- [Part::PropertyShapeHistory](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Part::PropertyShapeHistory "FeaturePython Custom Properties")
- [Path::PropertyPath](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Path::PropertyPath "FeaturePython Custom Properties")
- [Path::PropertyTool](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Path::PropertyTool "FeaturePython Custom Properties")
- [Path::PropertyTooltable](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Path::PropertyTooltable "FeaturePython Custom Properties")
- [Sketcher::PropertyConstraintList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Sketcher::PropertyConstraintList "FeaturePython Custom Properties")
- [Spreadsheet::PropertyColumnWidths](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Spreadsheet::PropertyColumnWidths "FeaturePython Custom Properties")
- [Spreadsheet::PropertyRowHeights](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Spreadsheet::PropertyRowHeights "FeaturePython Custom Properties")
- [Spreadsheet::PropertySheet](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Spreadsheet::PropertySheet "FeaturePython Custom Properties")
- [Spreadsheet::PropertySpreadsheetQuantity](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#Spreadsheet::PropertySpreadsheetQuantity "FeaturePython Custom Properties")
- [TechDraw::PropertyCenterLineList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#TechDraw::PropertyCenterLineList "FeaturePython Custom Properties")
- [TechDraw::PropertyCosmeticEdgeList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#TechDraw::PropertyCosmeticEdgeList "FeaturePython Custom Properties")
- [TechDraw::PropertyCosmeticVertexList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#TechDraw::PropertyCosmeticVertexList "FeaturePython Custom Properties")
- [TechDraw::PropertyGeomFormatList](https://wiki.freecadweb.org/FeaturePython_Custom_Properties#TechDraw::PropertyGeomFormatList "FeaturePython Custom Properties")

Özel nesnelerinize özellikler eklerken şunlara dikkat edin:

* Özellikler açıklamalarında `<` veya `>` karakterlerini kullanmayın (bu, **.fcstd** dosyasındaki **xml** parçalarını bozar)

* Özellikler bir **.fcstd** dosyasında alfabetik olarak saklanır. Eğer özelliklerinizde bir şekil varsa, ismi alfabetik olarak "Şekil"den sonra gelen herhangi bir özellik şekilden SONRA yüklenecektir ve bu da garip davranışlara neden olabilir.

Özellik özniteliklerinin tam listesi [PropertyStandard C++ başlık dosyasında](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyStandard.h) görülebilir. Örneğin, kullanıcının yalnız sınırlı bir değer aralığı girmesine izin vermek istiyorsanız (örneğin `PropertyIntegerConstraint` kullanarak), Python'da yalnız özellik değerini değil, aynı zamanda alt ve üst sınırı ve adım boyutunu da içeren bir tanımlama grubu atayacaksınız, aşağıda olduğu gibi:

```python
prop = (value, lower, upper, stepsize)
```

## Özellik Türü

Varsayılan olarak özellikler güncellenebilir. Örneğin bir yöntemin, sonucunu göstermek istemesi durumunda, özellikleri salt okunur yapmak mümkündür. Ayrıca özelliği gizlemek de mümkündür. Özellik türü aşağıdakiler kullanılarak ayarlanabilir:

```python
obj.setEditorMode("MyPropertyName", mode)
```

mod, şu şekilde ayarlanabilen kısa bir tamsayıdır (int):

```python
0 -- varsayılan mod, okuma ve yazma (default mode, read and write)
1 -- Salt okunur (read-only)
2 -- gizli (hidden)
```

EditörModları, FreeCAD dosyasının yeniden yüklenmesine ayarlanmamıştır. Bu, `__setstate__` fonksiyonu tarafından yapılabilir. http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=10#p108072 adresine bakın. `setEditorMode` kullanılarak, özellikler yalnızca **PropertyEditor**'de okunur. Hala python'dan değiştirilebilirler. Bunları gerçekten okumalarını sağlamak için, ayarın doğrudan `addProperty` fonksiyonunun içine iletilmesi gerekir. Örnek için http://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709 adresine bakın.

`AddProperty` fonksiyonundaki doğrudan ayarı kullanarak, daha fazla olanağınız da olur. Özellikle, bir özelliği çıktı özelliği olarak işaretlemek ilginçtir. Bu şekilde FreeCAD, özelliği değiştirirken dokunulduğunda işaretlemeyecektir (böylece yeniden hesaplamaya gerek yoktur).

Çıktı özelliği örneği (ayrıca bkz. https://forum.freecadweb.org/viewtopic.php?t=24928):

```python
obj.addProperty("App::PropertyString","MyCustomProperty","","",8)
```

`addProperty` işlevinin son parametresinde ayarlanabilen özellik türleri şunlardır:

```
0 -- Prop_None, Özel bir özellik türü yok
1 -- Prop_ReadOnly, Özellik düzenleyicide salt okunurdur
2 -- Prop_Transient, Özellik dosyaya kaydedilmeyecek
4 -- Prop_Hidden, Özellik düzenleyicide görünmeyecek
8 -- Prop_Output, Değiştirilmiş özellik, üst kapsayıcısına (konteyner) dokunmuyor
16 -- Prop_NoRecompute, Değiştirilmiş özellik, yeniden hesaplama için kapsayıcısına (konteyner) dokunmuyor
```

[PropertyContainer için C++ kaynak kodu başlığında](https://github.com/FreeCAD/FreeCAD/blob/master/src/App/PropertyContainer.h) tanımlanan bu farklı özellik türlerini bulabilirsiniz.

## Diğer Daha Karmaşık Örnek

Bu örnek, bir oktahedron (sekizyüzlü / sekiz yüzeyli katı bir şekil) oluşturmak için [Part](https://wiki.freecadweb.org/Part_Module) modülünü kullanır, ardından `pivy` ile onun coin gösterimini oluşturur.

Kodun birinci bölümü, Document nesnesinin kendisidir:

```python
import FreeCAD, FreeCADGui, Part
import pivy
from pivy import coin

class Octahedron:
  def __init__(self, obj):
     "Add some custom properties to our box feature"
     obj.addProperty("App::PropertyLength","Length","Octahedron","Length of the octahedron").Length=1.0
     obj.addProperty("App::PropertyLength","Width","Octahedron","Width of the octahedron").Width=1.0
     obj.addProperty("App::PropertyLength","Height","Octahedron", "Height of the octahedron").Height=1.0
     obj.addProperty("Part::PropertyPartShape","Shape","Octahedron", "Shape of the octahedron")
     obj.Proxy = self

  def execute(self, fp):
     # Define six vetices for the shape
     v1 = FreeCAD.Vector(0,0,0)
     v2 = FreeCAD.Vector(fp.Length,0,0)
     v3 = FreeCAD.Vector(0,fp.Width,0)
     v4 = FreeCAD.Vector(fp.Length,fp.Width,0)
     v5 = FreeCAD.Vector(fp.Length/2,fp.Width/2,fp.Height/2)
     v6 = FreeCAD.Vector(fp.Length/2,fp.Width/2,-fp.Height/2)

     # Make the wires/faces
     f1 = self.make_face(v1,v2,v5)
     f2 = self.make_face(v2,v4,v5)
     f3 = self.make_face(v4,v3,v5)
     f4 = self.make_face(v3,v1,v5)
     f5 = self.make_face(v2,v1,v6)
     f6 = self.make_face(v4,v2,v6)
     f7 = self.make_face(v3,v4,v6)
     f8 = self.make_face(v1,v3,v6)
     shell=Part.makeShell([f1,f2,f3,f4,f5,f6,f7,f8])
     solid=Part.makeSolid(shell)
     fp.Shape = solid

  # helper mehod to create the faces
  def make_face(self,v1,v2,v3):
     wire = Part.makePolygon([v1,v2,v3,v1])
     face = Part.Face(wire)
     return face
```

Ardından, nesneyi 3B sahnesinde göstermekten sorumlu olan görünüm sağlayıcı nesnesine sahip kodları yazıyoruz:

```python
class ViewProviderOctahedron:
  def __init__(self, obj):
     "Set this object to the proxy object of the actual view provider"
     obj.addProperty("App::PropertyColor","Color","Octahedron","Color of the octahedron").Color=(1.0,0.0,0.0)
     obj.Proxy = self

  def attach(self, obj):
     "Setup the scene sub-graph of the view provider, this method is mandatory"
     self.shaded = coin.SoGroup()
     self.wireframe = coin.SoGroup()
     self.scale = coin.SoScale()
     self.color = coin.SoBaseColor()

     self.data=coin.SoCoordinate3()
     self.face=coin.SoIndexedLineSet()

     self.shaded.addChild(self.scale)
     self.shaded.addChild(self.color)
     self.shaded.addChild(self.data)
     self.shaded.addChild(self.face)
     obj.addDisplayMode(self.shaded,"Shaded");
     style=coin.SoDrawStyle()
     style.style = coin.SoDrawStyle.LINES
     self.wireframe.addChild(style)
     self.wireframe.addChild(self.scale)
     self.wireframe.addChild(self.color)
     self.wireframe.addChild(self.data)
     self.wireframe.addChild(self.face)
     obj.addDisplayMode(self.wireframe,"Wireframe");
     self.onChanged(obj,"Color")

  def updateData(self, fp, prop):
     "If a property of the handled feature has changed we have the chance to handle this here"
     # fp is the handled feature, prop is the name of the property that has changed
     if prop == "Shape":
        s = fp.getPropertyByName("Shape")
        self.data.point.setNum(6)
        cnt=0
        for i in s.Vertexes:
           self.data.point.set1Value(cnt,i.X,i.Y,i.Z)
           cnt=cnt+1

        self.face.coordIndex.set1Value(0,0)
        self.face.coordIndex.set1Value(1,1)
        self.face.coordIndex.set1Value(2,2)
        self.face.coordIndex.set1Value(3,-1)

        self.face.coordIndex.set1Value(4,1)
        self.face.coordIndex.set1Value(5,3)
        self.face.coordIndex.set1Value(6,2)
        self.face.coordIndex.set1Value(7,-1)

        self.face.coordIndex.set1Value(8,3)
        self.face.coordIndex.set1Value(9,4)
        self.face.coordIndex.set1Value(10,2)
        self.face.coordIndex.set1Value(11,-1)

        self.face.coordIndex.set1Value(12,4)
        self.face.coordIndex.set1Value(13,0)
        self.face.coordIndex.set1Value(14,2)
        self.face.coordIndex.set1Value(15,-1)

        self.face.coordIndex.set1Value(16,1)
        self.face.coordIndex.set1Value(17,0)
        self.face.coordIndex.set1Value(18,5)
        self.face.coordIndex.set1Value(19,-1)

        self.face.coordIndex.set1Value(20,3)
        self.face.coordIndex.set1Value(21,1)
        self.face.coordIndex.set1Value(22,5)
        self.face.coordIndex.set1Value(23,-1)

        self.face.coordIndex.set1Value(24,4)
        self.face.coordIndex.set1Value(25,3)
        self.face.coordIndex.set1Value(26,5)
        self.face.coordIndex.set1Value(27,-1)

        self.face.coordIndex.set1Value(28,0)
        self.face.coordIndex.set1Value(29,4)
        self.face.coordIndex.set1Value(30,5)
        self.face.coordIndex.set1Value(31,-1)

  def getDisplayModes(self,obj):
     "Return a list of display modes."
     modes=[]
     modes.append("Shaded")
     modes.append("Wireframe")
     return modes

  def getDefaultDisplayMode(self):
     "Return the name of the default display mode. It must be defined in getDisplayModes."
     return "Shaded"

  def setDisplayMode(self,mode):
     return mode

  def onChanged(self, vp, prop):
     "Here we can do something when a single property got changed"
     FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
     if prop == "Color":
        c = vp.getPropertyByName("Color")
        self.color.rgb.setValue(c[0],c[1],c[2])

  def getIcon(self):
     return """
        /* XPM */
        static const char * ViewProviderBox_xpm[] = {
        "16 16 6 1",
        "    c None",
        ".   c #141010",
        "+   c #615BD2",
        "@   c #C39D55",
        "#   c #000000",
        "$   c #57C355",
        "        ........",
        "   ......++..+..",
        "   .@@@@.++..++.",
        "   .@@@@.++..++.",
        "   .@@  .++++++.",
        "  ..@@  .++..++.",
        "###@@@@ .++..++.",
        "##$.@@$#.++++++.",
        "#$#$.$$$........",
        "#$$#######      ",
        "#$$#$$$$$#      ",
        "#$$#$$$$$#      ",
        "#$$#$$$$$#      ",
        " #$#$$$$$#      ",
        "  ##$$$$$#      ",
        "   #######      "};
        """

  def __getstate__(self):
     return None

  def __setstate__(self,state):
     return None
```

Son olarak, nesnemiz ve onun `viewobject`'i tanımlandıktan sonra, onları çağırmamız (komutu çalıştırmamız) yeterlidir (Octahedron sınıfı ve viewprovider sınıf kodu doğrudan FreeCAD python konsolunda kopyalanabilir):

```python
FreeCAD.newDocument()
a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Octahedron")
Octahedron(a)
ViewProviderOctahedron(a.ViewObject)
```

## Nesneleri Seçilebilir Yapma

Eğer nesnenizi veya en azından bir kısmını görünüm alanında tıklayarak seçilebilir yapmak istiyorsanız, onun coin geometrisini bir `SoFCSelection` düğümüne (node) dahil etmeniz gerekir. Nesnenizin widget'lar, açıklamalar vb. ile karmaşık bir temsili varsa, bunun yalnızca bir bölümünü `SoFCSelection`'a dahil etmek isteyebilirsiniz. `SoFCSelection` olan her şey, seçimi/ön seçimi algılamak için FreeCAD tarafından sürekli olarak taranır, bu nedenle gereksiz tarama ile aşırı yüklemeden kaçınmak mantıklıdır.

Sahne grafiğinin seçilebilir olan kısımları `SoFCSelection` düğümlerinin içinde olduğunda, seçim yolunu işlemek için iki yöntem sağlamanız gerekir. Seçim yolu, yoldaki her bir öğenin veya bir dizi sahne grafiği nesnesinin adlarını veren bir dize (string) biçimini alabilir. Sağladığınız iki yöntem, bir dize yolundan bir dizi sahne grafiği nesnesine dönüştüren `getDetailPath` ve sahne grafiğinde tıklanan bir öğeyi alan ve dize adını döndüren `getElementPicked`'dir (dize yolunu değil, not edin).

Molekülün öğelerini seçilebilir hale getirmek için uyarlanmış yukarıdaki molekül örneği:

```python
class Molecule:
    def __init__(self, obj):
        ''' Add two point properties '''
        obj.addProperty("App::PropertyVector","p1","Line","Start point")
        obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(5,0,0)

        obj.Proxy = self

    def onChanged(self, fp, prop):
        if prop == "p1" or prop == "p2":
            ''' Print the name of the property that has changed '''
            fp.Shape = Part.makeLine(fp.p1,fp.p2)

    def execute(self, fp):
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

class ViewProviderMolecule:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self
        self.ViewObject = obj
        sep1=coin.SoSeparator()
        sel1 = coin.SoType.fromName('SoFCSelection').createInstance()
        # sel1.policy.setValue(coin.SoSelection.SHIFT)
        sel1.ref()
        sep1.addChild(sel1)
        self.trl1=coin.SoTranslation()
        sel1.addChild(self.trl1)
        sel1.addChild(coin.SoSphere())
        sep2=coin.SoSeparator()
        sel2 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel2.ref()
        sep2.addChild(sel2)
        self.trl2=coin.SoTranslation()
        sel2.addChild(self.trl2)
        sel2.addChild(coin.SoSphere())
        obj.RootNode.addChild(sep1)
        obj.RootNode.addChild(sep2)
        self.updateData(obj.Object, 'p2')
        self.sel1 = sel1
        self.sel2 = sel2

    def getDetailPath(self, subname, path, append):
        vobj = self.ViewObject
        if append:
            path.append(vobj.RootNode)
            path.append(vobj.SwitchNode)

            mode = vobj.SwitchNode.whichChild.getValue()
            if mode >= 0:
                mode = vobj.SwitchNode.getChild(mode)
                path.append(mode)
                sub = Part.splitSubname(subname)[-1]
                if sub == 'Atom1':
                    path.append(self.sel1)
                elif sub == 'Atom2':
                    path.append(self.sel2)
                else:
                    path.append(mode.getChild(0))
        return True

    def getElementPicked(self, pp):
        path = pp.getPath()
        if path.findNode(self.sel1) >= 0:
            return 'Atom1'
        if path.findNode(self.sel2) >= 0:
            return 'Atom2'
        raise NotImplementedError

    def updateData(self, fp, prop):
        "If a property of the handled feature has changed we have the chance to handle this here"
        # fp is the handled feature, prop is the name of the property that has changed
        if prop == "p1":
            p = fp.getPropertyByName("p1")
            self.trl1.translation=(p.x,p.y,p.z)
        elif prop == "p2":
            p = fp.getPropertyByName("p2")
            self.trl2.translation=(p.x,p.y,p.z)

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None

def makeMolecule():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Molecule")
    Molecule(a)
    ViewProviderMolecule(a.ViewObject)
    FreeCAD.ActiveDocument.recompute()
```

## Basit Şekillerle Çalışmak

Parametrik nesneniz basitçe bir şekil veriyorsa, bir görünüm sağlayıcı nesnesi kullanmanıza gerek yoktur. Şekil, FreeCAD'in standart şekil gösterimi kullanılarak görüntülenecektir:

```python
import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part
class Line:
    def __init__(self, obj):
        '''"App two point properties" '''
        obj.addProperty("App::PropertyVector","p1","Line","Start point")
        obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(1,0,0)
        obj.Proxy = self

    def execute(self, fp):
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Line")
Line(a)
a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
FreeCAD.ActiveDocument.recompute()
```

**ViewProviderLine** kullanımı ile aynı kod

```python
import FreeCAD as App
import FreeCADGui
import FreeCAD
import Part

class Line:
    def __init__(self, obj):
         '''"App two point properties" '''
         obj.addProperty("App::PropertyVector","p1","Line","Start point")
         obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(100,0,0)
         obj.Proxy = self

    def execute(self, fp):
        '''"Print a short message when doing a recomputation, this method is mandatory" '''
        fp.Shape = Part.makeLine(fp.p1,fp.p2)

class ViewProviderLine:
   def __init__(self, obj):
      ''' Set this object to the proxy object of the actual view provider '''
      obj.Proxy = self

   def getDefaultDisplayMode(self):
      ''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
      return "Flat Lines"

a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Line")
Line(a)
ViewProviderLine(a.ViewObject)
App.ActiveDocument.recompute()
```

## Sahne Yapısı

Yukarıdaki örneklerin sahne grafiklerini biraz farklı şekillerde oluşturduğunu fark etmiş olabilirsiniz. Bazıları `obj.addDisplayMode(node, "modename")` kullanırken diğerleri `obj.SwitchNode.getChild(x).addChild(y)` kullanır.

Bir FreeCAD belgesindeki her özellik aşağıdaki sahne grafiği yapısını temel alır:

```
RootNode
 \- SwitchNode
     \- Shaded
      - Wireframe
      - etc
```

`SwitchNode`, FreeCAD'de hangi görüntüleme modunun seçildiğine bağlı olarak, alt öğelerinden yalnızca birini görüntüler.

`addDisplayMode` kullanan örnekler, sahne grafiklerini yalnızca coin3d sahne grafiği öğelerinden oluşturuyor. Kapakların altında, `addDisplayMode`, `SwitchNode`'a yeni bir alt öğe ekler; o düğümün adı, geçtiği görüntüleme moduyla eşleşir.

`SwitchNode.getChild(x).addChild` kullanan örnekler ayrıca, `fp.Shape = Part.makeLine(fp.p1,fp.p2)` gibi Part (Parça) tezgahındaki işlevleri kullanarak geometrilerinin bir bölümünü oluşturur. Bu, `SwitchNode` altında farklı görüntüleme modu sahne grafiklerini oluşturur; Daha sonra sahne grafiğine coin3d öğeleri eklemeye geldiğimizde, bunları `SwitchNode`'un yeni bir alt öğesini oluşturmak yerine `addChild` kullanarak mevcut görüntüleme modu sahne grafiklerine eklememiz gerekir.

Sahne grafiğine geometri eklemek için `addDisplayMode()` kullanılırken, her görüntüleme modunun `addDisplayMode()` öğesine geçirilen kendi düğümü olmalıdır; bunun için aynı düğümü tekrar kullanmayın. Bunu yapmak, seçim mekanizmasını karıştıracaktır. Her görüntüleme modunun düğümünün altına aynı geometri düğümleri eklenmişse sorun değil, yalnızca her görüntüleme modunun kökünün farklı olması gerekir.

Part (Parça) tezgahından nesneler kullanmak yerine yalnızca Coin3D sahne grafiği nesneleriyle çizilmek üzere uyarlanmış yukarıdaki molekül örneği:

```python
import Part
from pivy import coin

class Molecule:
    def __init__(self, obj):
        ''' Add two point properties '''
        obj.addProperty("App::PropertyVector","p1","Line","Start point")
        obj.addProperty("App::PropertyVector","p2","Line","End point").p2=FreeCAD.Vector(5,0,0)

        obj.Proxy = self

    def onChanged(self, fp, prop):
        pass

    def execute(self, fp):
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        pass

class ViewProviderMolecule:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        self.constructed = False
        obj.Proxy = self
        self.ViewObject = obj

    def attach(self, obj):
        material = coin.SoMaterial()
        material.diffuseColor = (1.0, 0.0, 0.0)
        material.emissiveColor = (1.0, 0.0, 0.0)
        drawStyle = coin.SoDrawStyle()
        drawStyle.pointSize.setValue(10)
        drawStyle.style = coin.SoDrawStyle.LINES
        wireframe = coin.SoGroup()
        shaded = coin.SoGroup()
        self.wireframe = wireframe
        self.shaded = shaded

        self.coords = coin.SoCoordinate3()
        self.coords.point.setValues(0, 2, [FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)])
        wireframe += self.coords
        wireframe += drawStyle
        wireframe += material
        shaded += self.coords
        shaded += drawStyle
        shaded += material

        g = coin.SoGroup()
        sel1 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel1.style = 'EMISSIVE_DIFFUSE'
        p1 = coin.SoType.fromName('SoIndexedPointSet').createInstance()
        p1.coordIndex.set1Value(0, 0)
        sel1 += p1
        g += sel1
        wireframe += g
        shaded += g

        g = coin.SoGroup()
        sel2 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel2.style = 'EMISSIVE_DIFFUSE'
        p2 = coin.SoType.fromName('SoIndexedPointSet').createInstance()
        p2.coordIndex.set1Value(0, 1)
        sel2 += p2
        g += sel2
        wireframe += g
        shaded += g

        g = coin.SoGroup()
        sel3 = coin.SoType.fromName('SoFCSelection').createInstance()
        sel3.style = 'EMISSIVE_DIFFUSE'
        p3 = coin.SoType.fromName('SoIndexedLineSet').createInstance()
        p3.coordIndex.setValues(0, 2, [0, 1])
        sel3 += p3
        g += sel3
        wireframe += g
        shaded += g

        obj.addDisplayMode(wireframe, 'Wireframe')
        obj.addDisplayMode(shaded, 'Shaded')

        self.sel1 = sel1
        self.sel2 = sel2
        self.sel3 = sel3
        self.constructed = True
        self.updateData(obj.Object, 'p2')

    def getDetailPath(self, subname, path, append):
        vobj = self.ViewObject
        if append:
            path.append(vobj.RootNode)
            path.append(vobj.SwitchNode)

            mode = vobj.SwitchNode.whichChild.getValue()
            FreeCAD.Console.PrintWarning("getDetailPath: mode {} is active\n".format(mode))
            if mode >= 0:
                mode = vobj.SwitchNode.getChild(mode)
                path.append(mode)
                sub = Part.splitSubname(subname)[-1]
                print(sub)
                if sub == 'Atom1':
                    path.append(self.sel1)
                elif sub == 'Atom2':
                    path.append(self.sel2)
                elif sub == 'Line':
                    path.append(self.sel3)
                else:
                    path.append(mode.getChild(0))
        return True

    def getElementPicked(self, pp):
        path = pp.getPath()
        if path.findNode(self.sel1) >= 0:
            return 'Atom1'
        if path.findNode(self.sel2) >= 0:
            return 'Atom2'
        if path.findNode(self.sel3) >= 0:
            return 'Line'
        raise NotImplementedError

    def updateData(self, fp, prop):
        "If a property of the handled feature has changed we have the chance to handle this here"
        # fp is the handled feature, prop is the name of the property that has changed
        if not self.constructed:
            return
        if prop == "p1":
            p = fp.getPropertyByName("p1")
            self.coords.point.set1Value(0, p)
        elif prop == "p2":
            p = fp.getPropertyByName("p2")
            self.coords.point.set1Value(1, p)

    def getDisplayModes(self, obj):
        return ['Wireframe', 'Shaded']

    def getDefaultDisplayMode(self):
        return 'Shaded'

    def setDisplayMode(self, mode):
        return mode

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None

def makeMolecule():
    FreeCAD.newDocument()
    a=FreeCAD.ActiveDocument.addObject("App::FeaturePython","Molecule")
    Molecule(a)
    b=ViewProviderMolecule(a.ViewObject)
    a.touch()
    FreeCAD.ActiveDocument.recompute()
    return a,b

a,b = makeMolecule()
```

## ParçaTasarımı (Part Design) Komut Dosyasıyla Yazılmış Nesneler

Parça Tasarımında kodlanmış nesneler oluştururken, süreç yukarıda tartışılan komut dosyası oluşturulmuş nesnelere benzer, ancak birkaç ek husus vardır. Biri 3B görünümde gördüğümüz şekil için, diğeri ise polar desen özellikleri gibi desen araçları tarafından kullanılan şekil için olmak üzere 2 şekil özelliğini ele almalıyız. Nesne şekillerinin ayrıca, halihazırda Gövdede bulunan herhangi bir mevcut malzemeyle kaynaştırılması (veya Çıkarma özellikleri durumunda ondan kesilmesi) gerekir. Nesnelerimizin yerleştirilmesini ve bağlanmasını biraz farklı hesaba katmalıyız.

Parça Tasarımı komut dosyasıyla yazılmış katı nesne özellikleri, `Part::FeaturePython` yerine `PartDesign::FeaturePython`, `PartDesign::FeatureAdditivePython` veya `PartDesign::FeatureSubtractivePython`'a dayanmalıdır. Çoğaltma özelliklerinde yalnız Toplama ve Çıkarma varyantları kullanılabilir ve `Part::FeaturePython`'a dayalıysa, kullanıcı nesneyi bir Parça Tasarım Gövdesine bıraktığında, Gövde tarafından yerel bir Parça Tasarım nesnesi olarak ele alınmak yerine bir `BaseFeature` olur. **Not**: bunların hepsinin katı olması beklenir, bu nedenle katı olmayan bir özellik yapıyorsanız bunun `Part::FeaturePython`'a dayanması gerekir, yoksa ağaçtaki bir sonraki özellik katı olarak birleşmeye çalışır ve başarısız olur .

Burada, Parça Çalışma Tezgahındaki (Part Workbench'teki) **Boru (Tube)** temel şekline (primitifine) benzer bir Boru temel şekil oluşturmanın basit bir örneği verilmiştir, ancak bu bir Parça Tasarımı (Part Design) katı özellik nesnesi olacaktır. Bunun için 2 ayrı dosya oluşturacağız: `pdtube.FCMacro` ve `pdtube.py`. `.FCMacro` dosyası, nesneyi oluşturmak için kullanıcı tarafından çalıştırılacaktır. `.py` dosyası, `.FCMacro` tarafından içe aktarılan sınıf tanımlarını tutacaktır. Bunu bu şekilde yapmanın nedeni, FreeCAD'i yeniden başlattıktan ve Borularımızdan birini içeren bir belgeyi açtıktan sonra nesnenin parametrik yapısını korumaktır.

İlk olarak, sınıf tanım dosyasını oluşturuyoruz:

```python
# -*- coding: utf-8 -*-
#classes should go in pdtube.py
import FreeCAD, FreeCADGui, Part
class PDTube:
    def __init__(self,obj):
        obj.addProperty("App::PropertyLength","Radius1","Tube","Radius1").Radius1 = 5
        obj.addProperty("App::PropertyLength","Radius2","Tube","Radius2").Radius2 = 10
        obj.addProperty("App::PropertyLength","Height","Tube","Height of tube").Height = 10
        self.makeAttachable(obj)
        obj.Proxy = self

    def makeAttachable(self, obj):

        if int(FreeCAD.Version()[1]) >= 19:
            obj.addExtension('Part::AttachExtensionPython')
        else:
            obj.addExtension('Part::AttachExtensionPython', obj)

        obj.setEditorMode('Placement', 0) #non-readonly non-hidden

    def execute(self,fp):
        outer_cylinder = Part.makeCylinder(fp.Radius2, fp.Height)
        inner_cylinder = Part.makeCylinder(fp.Radius1, fp.Height)
        if fp.Radius1 == fp.Radius2: #just make cylinder
            tube_shape = outer_cylinder
        elif fp.Radius1 < fp.Radius2:
            tube_shape = outer_cylinder.cut(inner_cylinder)
        else: #invert rather than error out
            tube_shape = inner_cylinder.cut(outer_cylinder)

        if not hasattr(fp, "positionBySupport"):
            self.makeAttachable(fp)
        fp.positionBySupport()
        tube_shape.Placement = fp.Placement

        #BaseFeature (shape property of type Part::PropertyPartShape) is provided for us
        #with the PartDesign::FeaturePython and related classes, but it might be empty
        #if our object is the first object in the tree.  it's a good idea to check
        #for its existence in case we want to make type Part::FeaturePython, which won't have it

        if hasattr(fp, "BaseFeature") and fp.BaseFeature != None:
            if "Subtractive" in fp.TypeId:
                full_shape = fp.BaseFeature.Shape.cut(tube_shape)
            else:
                full_shape = fp.BaseFeature.Shape.fuse(tube_shape)
            full_shape.transformShape(fp.Placement.inverse().toMatrix(), True) #borrowed from gears workbench
            fp.Shape = full_shape
        else:
            fp.Shape = tube_shape
        if hasattr(fp,"AddSubShape"): #PartDesign::FeatureAdditivePython and
                                      #PartDesign::FeatureSubtractivePython have this
                                      #property but PartDesign::FeaturePython does not
                                      #It is the shape used for copying in pattern features
                                      #for example in making a polar pattern
            tube_shape.transformShape(fp.Placement.inverse().toMatrix(), True)
            fp.AddSubShape = tube_shape

class PDTubeVP:
    def __init__(self, obj):
        '''Set this object to the proxy object of the actual view provider'''
        obj.Proxy = self

    def attach(self,vobj):
        self.vobj = vobj

    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        pass

    def getDisplayModes(self,obj):
        '''Return a list of display modes.'''
        modes=[]
        modes.append("Flat Lines")
        modes.append("Shaded")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self):
        '''Return the name of the default display mode. It must be defined in getDisplayModes.'''
        return "Flat Lines"

    def setDisplayMode(self,mode):
        '''Map the display mode defined in attach with those defined in getDisplayModes.\
                Since they have the same names nothing needs to be done. This method is optional'''
        return mode

    def onChanged(self, vp, prop):
        '''Here we can do something when a single property got changed'''
        #FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        pass

    def getIcon(self):
        '''Return the icon in XPM format which will appear in the tree view. This method is\
                optional and if not defined a default icon is shown.'''
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "   c None",
            ".  c #141010",
            "+  c #615BD2",
            "@  c #C39D55",
            "#  c #000000",
            "$  c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def __getstate__(self):
        '''When saving the document this object gets stored using Python's json module.\
                Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
                to return a tuple of all serializable objects or None.'''
        return None

    def __setstate__(self,state):
        '''When restoring the serialized object from document we have the chance to set some internals here.\
                Since no data were serialized nothing needs to be done here.'''
        return None
```

Ve şimdi nesneyi oluşturmak için makro dosyası içeriğini yazıyoruz:

```python
# -*- coding: utf-8 -*-

#pdtube.FCMacro
import pdtube
#above line needed if the class definitions above are place in another file: PDTube.py
#this is needed if the tube object is to remain parametric after restarting FreeCAD and loading
#a document containing the object

body = FreeCADGui.ActiveDocument.ActiveView.getActiveObject("pdbody")
if not body:
    FreeCAD.Console.PrintError("No active body.\n")
else:
    from PySide import QtGui
    window = FreeCADGui.getMainWindow()
    items = ["Additive","Subtractive","Neither additive nor subtractive"]
    item,ok =QtGui.QInputDialog.getItem(window,"Select tube type","Select whether you want additive, subtractive, or neither:",items,0,False)
    if ok:
        if item == items[0]:
            className = "PartDesign::FeatureAdditivePython"
        elif item == items[1]:
            className = "PartDesign::FeatureSubtractivePython"
        else:
            className = "PartDesign::FeaturePython" #not usable in pattern features, such as polar pattern

        tube = FreeCAD.ActiveDocument.addObject(className,"Tube")
        pdtube.PDTube(tube)
        pdtube.PDTubeVP(tube.ViewObject)
        body.addObject(tube) #optionally we can also use body.insertObject() for placing at particular place in tree
```

## Daha Fazla Bilgi için

Ek Sayfalar:

- [Öznitelikleri kaydeden komut dosyası nesneleri](https://wiki.freecadweb.org/Scripted_objects_saving_attributes "Scripted objects saving attributes")
- [Komut dosyasıyla oluşturulmuş nesneleri taşıma/yükseltme](https://wiki.freecadweb.org/Scripted_objects_migration "Scripted objects migration")
- [Ekli komut dosyası nesneleri](https://wiki.freecadweb.org/Scripted_objects_with_attachment "Scripted objects with attachment")
- [Görünüm sağlayıcılar](https://wiki.freecadweb.org/Viewprovider "Viewprovider")

Komut dosyasıyla yazılmış nesneler hakkında ilginç forum konuları:

- [Yükleme esnasında kaybolan Python nesnesi özellikleri](http://forum.freecadweb.org/viewtopic.php?f=22&t=13740)
- [Yeni FeaturePython gridir](http://forum.freecadweb.org/viewtopic.php?t=12139)
- [`__getstate__` ve `__setstate__` ile ilgili açıklama, resmi belgeler](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), [official documentation](https://docs.python.org/3/library/pickle.html#object.__getstate__)
- [Eigenmode frekansı her zaman 0?](https://forum.freecadweb.org/viewtopic.php?f=18&t=13460&start=20#p109709)
- [python özelliğinin setEdit'e düzgün bir şekilde nasıl uygulanır?](https://forum.freecadweb.org/viewtopic.php?f=22&t=21330)

Burada sunulan örneklere ek olarak, daha fazla örnek için FreeCAD kaynak kodu [src/Mod/TemplatePyMod/FeaturePython.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)'ye bakın.

<p> | <a href="https://mhalil.github.io/"> Ana Sayfa </a> | <a href="https://mhalil.github.io/freecad.html"> FreeCAD Sayfası </a> | <a href="05_Topolojik_Veri_Kodlamasi.html" > < Topolojik Veri Kodlaması </a> | <a href="#"> Sonraki Bölüm > </a> | </p>

Kaynak: [Scripted objects - FreeCAD Documentation](https://wiki.freecadweb.org/Scripted_objects)
