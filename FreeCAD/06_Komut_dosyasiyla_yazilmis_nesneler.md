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







<p> | <a href="https://mhalil.github.io/"> Ana Sayfa </a> | <a href="https://mhalil.github.io/freecad.html"> FreeCAD Sayfası </a> | <a href="05_Topolojik_Veri_Kodlamasi.html" > < Topolojik Veri Kodlaması </a> | <a href="#"> Sonraki Bölüm > </a> | </p>

Kaynak: [Scripted objects - FreeCAD Documentation](https://wiki.freecadweb.org/Scripted_objects)
