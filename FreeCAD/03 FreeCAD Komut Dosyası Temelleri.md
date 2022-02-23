# FreeCAD'de Komut Dosyası Oluşturmanın (Scripting) Temelleri

## FreeCAD'de Python komut dosyası oluşturmak

FreeCAD, Python komut dosyaları tarafından tamamen kontrol edilecek şekilde sıfırdan oluşturulmuştur. Arayüz, sahne içeriği ve hatta bu içeriğin 3B görünümlerdeki temsili gibi FreeCAD'in neredeyse tüm bölümlerine yerleşik Python yorumlayıcısından veya kendi komut dosyalarınızdan erişilebilir. Sonuç olarak, FreeCAD muhtemelen bugün mevcut olan en kapsamlı özelleştirilebilir mühendislik uygulamalarından biridir.

Python'a aşina değilseniz, internette öğreticiler aramanızı ve yapısına hızlıca göz atmanızı öneririz. Python öğrenmesi çok kolay bir dildir, özellikle de bir yorumlayıcı içinde çalıştırılabilir, burada basit komutlar, programları tamamlamaya kadar, hiçbir şeyi derlemeye gerek kalmadan anında çalıştırılabilir. FreeCAD, yerleşik bir Python yorumlayıcısına sahiptir. Aşağıda gösterildiği gibi **Python konsolu** etiketli pencereyi görmüyorsanız, `Görünüm → Paneller → Python konsolu` altında etkinleştirebilirsiniz.

## Yorumlayıcı

Yorumlayıcıdan, sistem tarafından kurulmuş tüm Python modüllerinize, yerleşik FreeCAD modüllerine ve daha sonra kurduğunuz tüm ek FreeCAD modüllerine erişebilirsiniz. Aşağıdaki ekran görüntüsü Python yorumlayıcısını göstermektedir.

![freecad_python_konsolu](E:\FreeCAD\FreeCAD Scripting Eğitimi\img\01_freecad_python_konsol.png)

Yorumlayıcıdan Python kodunu çalıştırabilir ve mevcut sınıflara ve işlevlere göz atabilirsiniz. FreeCAD, FreeCAD dünyasını keşfetmek için çok kullanışlı bir `sınıf tarayıcısı (class browser)` sağlar: Bilinen bir sınıfın adını ve ardından bir nokta yazdığınızda (bu sınıftan bir şey eklemek istediğiniz anlamına gelir), aralarında gezinebileceğiniz bir sınıf tarayıcı penceresi açılır. Mevcut alt sınıflar ve yöntemler tarayıcıda görüntülenir. Bir şey seçtiğinizde, ilişkili bir yardım metni (varsa) görüntülenir:

![python konsol class browser](E:\FreeCAD\FreeCAD Scripting Eğitimi\img\07_python_konsolu_class_browser.png)

Yani, buraya `App.` yazarak başlayın. veya `Gui.` ve ne olduğunu görün. Modüllerin ve sınıfların içeriğini keşfetmenin daha genel bir Python yolu da `print(dir())` komutunu kullanmaktır. Örneğin, `print(dir())` yazıldığında, o anda FreeCAD'de yüklü olan tüm modüller listelenir. `print(dir(App))` size Uygulama modülü vb. içindeki her şeyi gösterecektir.

Yorumlayıcının bir başka kullanışlı özelliği de komut geçmişine geri dönme ve daha önce yazdığınız bir kod satırını alma olasılığıdır. Komut geçmişinde gezinmek için `Yukarı ok` veya `Aşağı ok` tuşlarını kullanmanız yeterlidir.

Yorumlayıcı penceresine sağ tıklayarak, tüm geçmişi kopyalamak (tam bir komut dosyası oluşturmadan önce bir şeylerle deneme yapmak istediğinizde, bu yöntem kullanışlıdır) veya tam yolu olan bir dosya adı eklemek gibi birkaç başka seçeneğiniz de vardır.

## Python Yardımı

FreeCAD **Yardım** menüsünde, Python ve FreeCAD yerleşik modülleri dahil olmak üzere FreeCAD yorumlayıcısı tarafından kullanılabilen tüm Python modüllerinin eksiksiz, gerçek zamanlı olarak oluşturulmuş belgelerini içeren bir tarayıcı penceresi açacak olan **Otomatik python modülleri belgeleri** etiketli bir giriş bulacaksınız; Sistem tarafından kurulan modüller ve FreeCAD ek modülleri. Orada bulunan belgeler, her bir modül geliştiricisinin kodunu belgelemek için ne kadar çaba sarf ettiğine bağlıdır, ancak Python modülleri oldukça iyi belgelenmiş olmalarıyla ünlüdür. Bu dokümantasyon sisteminin çalışması için FreeCAD pencereniz açık kalmalıdır. **Python komut dosyası oluşturma belgeleri**, size [Power users hub](https://wiki.freecadweb.org/Power_users_hub) wiki bölümüne hızlı bir bağlantı sağlar.

## Dahili (Built-in) Modüller

FreeCAD, **Grafiksel Kullanıcı Arayüzü (GUI)** olmadan da çalıştırılabilecek şekilde tasarlandığından, hemen hemen tüm işlevleri iki gruba ayrılır: `App` adlı **Çekirdek** işlevselliği ve `Gui` adlı **GUI** işlevselliği. Bu iki modüle, sırasıyla `FreeCAD` ve `FreeCADGui` adlarıyla, yorumlayıcının dışındaki komut dosyalarından da erişilebilir.

+ `App` modülünde, dosyaları açma veya kapatma yöntemleri gibi uygulamanın kendisiyle ve etkin belgeyi ayarlamak veya içeriklerini listelemek gibi belgelerle ilgili her şeyi bulacaksınız.
+ `Gui` modülünde, çalışma tezgahları ve bunların araç çubukları gibi Gui öğelerine erişmek ve bunları yönetmek için araçlar ve daha da ilginci, tüm FreeCAD içeriğinin grafiksel gösterimi bulacaksınız.

FreeCAD gelişimi oldukça hızlı büyüdüğü için bu modüllerin içeriklerini listelemek pek kullanışlı değildir. Ancak sağlanan iki tarama aracı (sınıf tarayıcısı (class browser) ve Python yardımı) size her an eksiksiz ve güncel belgeler sağlamalıdır.

## App ve Gui Nesneleri

Daha önce de belirtildiği gibi, FreeCAD'de her şey çekirdek ve temsile ayrılmıştır. Bu, 3D nesneleri içerir. Nesnelerin **tanımlayıcı özelliklerine** (FreeCAD'deki özellikler olarak adlandırılır) `App` modülü üzerinden erişebilir ve `Gui` modülü aracılığıyla **ekranda temsil edildikleri şekli** değiştirebilirsiniz. Örneğin, bir küpün bir `App` nesnesinde depolanan, onun **tanımlanan özellikleri** (genişlik, uzunluk, yükseklik gibi) ve `Gui` nesnesinde depolanan **görünüm özellikleri** (yüzey rengi, çizim modu gibi) vardır.

İşleri bu şekilde yapmak, algoritmaların herhangi bir görsel parçayı önemsemeye gerek kalmadan yalnızca özelliklerin tanım bölümünde çalışması veya hatta belgenin içeriğini listeler, elektronik tablolar veya öğe analizi gibi grafik olmayan uygulamaya yönlendirmesi gibi çok çeşitli kullanımlara izin verir.

Belgenizdeki her `App` nesnesine karşılık gelen bir `Gui` nesnesi vardır. Aslında belgenin kendisi hem `App` hem de `Gui` nesnesine sahiptir. Bu, elbette, yalnızca FreeCAD'i tam arayüzü ile çalıştırdığınızda geçerlidir. Komut satırı sürümünde `GUI` yoktur, bu nedenle yalnızca `App` nesneleri kullanılabilir. Bir `App` nesnesi '**yeniden hesaplanacak**' olarak her işaretlendiğinde (örneğin parametrelerinden biri değiştiğinde), nesnelerin `Gui` bölümünün yeniden oluşturulduğunu unutmayın, bu nedenle doğrudan `Gui` nesnesinde yapılan tüm değişiklikler kaybolabilir.

Bir nesnenin `App` kısmına erişmek için şunu yazın:
    myObject = App.ActiveDocument.getObject("ObjectName")
burada `"ObjectName"`, nesnenizin adıdır. Şunları da yazabilirsiniz:
    myObject = App.ActiveDocument.ObjectName
Aynı nesnenin `Gui` kısmına erişmek için şunu yazın:
    myViewObject = Gui.ActiveDocument.getObject("ObjectName")
burada `"ObjectName"`, nesnenizin adıdır. Şunları da yazabilirsiniz:
    myViewObject = App.ActiveDocument.ObjectName.ViewObject

Komut satırı modundaysanız ve GUI'nız yoksa, son satır `None` değerini döndürür.

## Belge Nesneleri

FreeCAD'de tüm çalışmalarınız belgelerin içinde bulunur. Bir belge, geometrinizi içerir ve bir dosyaya kaydedilebilir. Aynı anda birkaç belge açılabilir. Belge, içinde bulunan geometri gibi, `App` ve `Gui` nesnelerine sahiptir. `App` nesnesi gerçek geometri tanımlarınızı içerirken `Gui` nesnesi belgenizin farklı görünümlerini içerir. Her biri çalışmanızı farklı bir yakınlaştırma faktörüyle veya farklı bir yönden görüntüleyen birkaç pencere açabilirsiniz. Bu görünümlerin tümü, belgenizin `Gui` nesnesinin bir parçasıdır.

    myDocument = App.ActiveDocument

Yeni bir belge oluşturmak için şunu yazın:
    myDocument = App.newDocument("Document Name")

Şu anda açık olan (etkin) belgenin `Gui` kısmına erişmek için şunu yazın:
    myGuiDocument = Gui.ActiveDocument

Geçerli görünüme erişmek için şunu yazın:
    myView = Gui.ActiveDocument.ActiveView

## Ek modülleri kullanmak

`FreeCAD` ve `FreeCADGui` modülleri, yalnızca FreeCAD belgesinde nesnelerin oluşturulmasından ve yönetilmesinden sorumludur. Aslında geometri oluşturmak veya değiştirmek gibi başka bir şey yapmıyorlar. Bunun nedeni, geometrinin birkaç türde olabilmesi ve bu nedenle her biri belirli bir geometri türünü yönetmekten sorumlu ek modüller gerektirmesidir. Örneğin, **OpenCascade** çekirdeğini kullanan [Part (Parça) Tezgahı](https://wiki.freecadweb.org/Part_Workbench), [BRep](http://en.wikipedia.org/wiki/Boundary_representation) tipi geometriyi oluşturabilir ve değiştirebilir. [Mesh Workbench (Kafes/Ağ Çalışma Tezgahı)](https://wiki.freecadweb.org/Mesh_Workbench) ise mesh nesneleri oluşturabilir ve değiştirebilir. Bu şekilde FreeCAD, tümü aynı belgede bir arada bulunabilen çok çeşitli nesne türlerini işleyebilir ve gelecekte yeni türler kolayca eklenebilir.

## Nesneler Oluşturmak

Her modülün kendi geometrisiyle uğraşma yöntemi vardır, ancak genellikle yapabildikleri tek şey belgede nesneler oluşturmaktır. Ancak FreeCAD belgesi, modüller tarafından sağlanan mevcut nesne türlerinin de farkındadır:

    FreeCAD.ActiveDocument.supportedTypes()

bu kod, oluşturabileceğiniz tüm olası nesneleri listeler. Örneğin, bir Mesh (Ağ/Kafes modülü ile) ve bir Part (Parça modülü ile) oluşturalım:

    myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
    myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")

İlk argüman (*"Mesh::Feature"*) nesne türüdür, ikincisi (*"myMeshName"*) nesnenin adıdır. İki nesnemiz neredeyse aynı görünüyor: Henüz herhangi bir geometri içermiyorlar ve `dir(myMesh)` ve `dir(myPart)` ile incelediğinizde özelliklerinin çoğu aynı. Bir şey dışında, `myMesh`'in **Mesh** özelliği ve `myPart`'ın **Shape** özelliği vardır. `Mesh` ve `Part` verilerinin depolandığı yer burasıdır. Örneğin, bir `Part` küpü oluşturalım ve onu `myPart` nesnemizde saklayalım:

    import Part
    cube = Part.makeBox(2, 2, 2)
    myPart.Shape = cube

Küpü `myMesh` nesnesinin **Mesh** özelliği içinde saklamayı deneyebilirsiniz, ancak bu bir hata verecektir. Bunun nedeni, her özelliğin yalnızca belirli bir türü depolamak için yapılmış olmasıdır. Bir **Mesh** özelliğinde, yalnızca `Mesh` modülü ile oluşturulan öğeleri kaydedebilirsiniz. Çoğu modülün ayrıca geometrilerini belgeye eklemek için bir kısayolu olduğunu unutmayın:

    import Part
    cube = Part.makeBox(2, 2, 2)
    Part.show(cube)

## Nesneleri Değiştirmek

Bir nesneyi değiştirmek aynı şekilde yapılır:

    import Part
    cube = Part.makeBox(2, 2, 2)
    myPart.Shape = cube

Şimdi şekli daha büyük bir şekille değiştirelim:

    biggercube = Part.makeBox(5, 5, 5)
    myPart.Shape = biggercube

## Nesneleri Sorgulamak

Bir nesnenin türüne her zaman şöyle bakabilirsiniz:

    myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
    print(myObj.TypeId)

veya bir nesnenin, temel olan nesnelerin birinden (Part Feature, Mesh Feature, vb.) türetilmiş olup olmadığını kontrol edin:

    print(myObj.isDerivedFrom("Part::Feature"))

Artık FreeCAD ile gerçekten oynamaya/çalışmaya başlayabilirsiniz! Kullanılabilir modüllerin ve araçlarının tam listesi için [Kategori:API](https://wiki.freecadweb.org/Category:API) bölümünü ziyaret edin.

Kaynak: [FreeCAD Scripting Basics](https://wiki.freecadweb.org/FreeCAD_Scripting_Basics)
