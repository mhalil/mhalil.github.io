# 06 Topolojik veri kodlaması

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

+ **Geom** Geometrik nesnelerin Temel sınıfı.

+ **Çizgi** Başlangıç ​​noktası ve bitiş noktası ile tanımlanan 3B düz bir çizgi.

+ **Çember** Çember veya bir merkez noktası ve başlangıç ​​ve bitiş noktası ile tanımlanan daire parçası.

+ vb.
  
  

## Topoloji

Aşağıdaki topolojik veri türleri mevcuttur:

+ **Birleşik (Compound)** Herhangi bir tür topolojik nesne grubu.

+ **KompozitKatı (Compsolid)** Kompozit bir katı, yüzleri ile birbirine bağlanmış bir dizi katıdır. TEL (WIRE) ve KABUK (SHELL) kavramlarını katılara genişletir.

+ **Katı (Solid)** Kabukları ile sınırlı alanın bir parçası. Üç boyutlu.

+ **Kabuk (Shell)** Kenarlarıyla birbirine bağlanan bir dizi yüzey. Bir kabuk açık veya kapalı olabilir.

+ **Yüzey (Face)** 2B'de bir düzlemin parçasıdır; 3B'de bir yüzeyin parçasıdır. Geometrisi konturlarla sınırlandırılmıştır (kırpılmıştır). İki boyutludur.

+ **Kafes / Ağ (Wire)** Köşeleri ile birbirine bağlanan bir dizi kenar. Kenarların bağlantılı olup olmamasına bağlı olarak açık veya kapalı kontur olabilir.

+ **Kenar (Edge)** Kısıtlanmış bir eğriye karşılık gelen bir topolojik eleman. Bir kenar genellikle köşelerle sınırlıdır. Tek boyutludur.

+ **Nokta (Vertex)** Bir noktaya karşılık gelen topolojik bir öğe. Boyutsuzdur.

+ **Şekil (Shape)** Yukarıdakilerin tümünü kapsayan genel bir terim.

## Örnek: Basit topoloji oluşturun

![](https://wiki.freecadweb.org/images/7/77/Wire.png)

Şimdi daha basit geometriden inşa ederek bir topoloji oluşturacağız. Örnek olay olarak resimde görüldüğü gibi dört köşe (noktası), iki yay ve iki çizgiden oluşan bir parça kullanacağız.
