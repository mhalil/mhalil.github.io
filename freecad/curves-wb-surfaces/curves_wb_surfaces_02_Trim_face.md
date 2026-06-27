Title: FreeCAD - Curves WB - Surface - 02 - Trim face
Date: 2023-02-12 00:00
Modified: 2023-05-01 00:00
Category: Curves WB - Surfaces
Tags: FreeCAD, Curves, Workbench, ÇalışmaTezgahı, Surface, Trim, face, Trim face
Author: Mustafa Halil

# ![trimFace](../../images/freecad/curves_wb/simgeler/surfaces/TrimFace.svg) **Trim face:**

**Trim face** komutu, kesişme eğrisi oluşturmadan yüzleri kırpmanıza olanak tanır. Bu, yüzeyleri eğrilerle kırpan veya ayıran komuttur.  

**Kullanım:** Komutu çalıştırmak için aşağıdaki adımları sırası ile uygulayın:

- Öncelikle eğri(ler)i / kenar(lar)ı ve ardından yüzey(ler)i seçin. (Birlikte seçim için `CTRL` tuşunu kullanın)
- Curves araç çubuğunda bulunan ilgili düğmeye basın, ya da
- **Curves WB** (Çalışma Tezgahındayken) **Surface** menüsündeki **Trim face** seçeneğini kullanın.

Aşağıdaki şekilde göreceğiniz gibi elimizde eğrisel bir yüzey ve bir elips var.  
![TrimFace_01](../../images/freecad/curves_wb/surfaces_menu/TrimFace_01.png)  
Evvela **Üst görünüşe** geçerek önce eğriyi ardından yüzeyi seçiyoruz. Yüzeyi seçerken **eğrinin dış ya da iç kısmında** kalan bir yerin seçilmesinin önemli olduğu bilinmelidir. Aşağıdaki örnekte, Eğri seçildikten sonra, eğrinin **dış kısmında kalan** bir yere tıklanarak seçimin yapıldı ve ardından **Trim face** komutu çalıştırılmıştır.
![TrimFace_02](../../images/freecad/curves_wb/surfaces_menu/TrimFace_02.png)  
İşlem sonucu karşımızda. Yüzey seçimi yaparken, Eğrinin dışında kalan bir yere tıkladığımız için **bu bölümün kalmasını istiyorum, geri kalan kısmı sil, at** demiş oluyoruz.
![TrimFace_03](../../images/freecad/curves_wb/surfaces_menu/TrimFace_03.png)  
Modelin İzometrik görünümü bu şekildedir.
![TrimFace_04](../../images/freecad/curves_wb/surfaces_menu/TrimFace_04.png)  
Önce eğriyi ardından **eğrinin iç kısmında** kalan bir yeri seçerek yüzey seçimi yaptıktan sonra **Üst görünüşe** geçerek **Trim face** komutu çalıştırıp sonucu görelim.
![TrimFace_05](../../images/freecad/curves_wb/surfaces_menu/TrimFace_05.png)  
İşlem sonucu elde ettiğimiz model bu şekilde:
![TrimFace_06](../../images/freecad/curves_wb/surfaces_menu/TrimFace_06.png)  
Oluşan yüzeye **Parça Çalışma Tezhagı (Part WB)** içerisindeki **3D Offset..** komutu ile et kalınlığı verip kenarlarını da **Fillet** komutu ile yuvarlatırsak ne elde etmiş oluruz acaba? :)
![TrimFace_06.2](../../images/freecad/curves_wb/surfaces_menu/TrimFace_06.2.png)  
Dikkat ettiyseniz, yukarıdaki anlatımlarda **Trim face** komutunu çalıştırmadan önce, sürekli **Üst görünüşe geçilmesi** ifade edildi. Bunun sebebi, **Trim face** komutunun, sahneye bakış açısı doğrultusunda çıkarma/silme işlemi yapmasıdır. Aşağıdaki örnekte, sahneye izometrik bakış açısı ile bakıldığı esnada önce eğri ardından **eğrinin iç kısmındaki yüzey** seçilerek "Trim face" komutunu uygulanmaktadır.
![TrimFace_07](../../images/freecad/curves_wb/surfaces_menu/TrimFace_07.png)  
Sonuç, beklediğimiz gibi.
![TrimFace_08](../../images/freecad/curves_wb/surfaces_menu/TrimFace_08.png)  
Sonuca daha yakından bakacak olursak;
![TrimFace_09](../../images/freecad/curves_wb/surfaces_menu/TrimFace_09.png)  
Bu kez de sahneye farklı bir bakış açısı ile bakarak, eğrinin dışında kalan yüzey kısmını seçerek **Trim face** komutunu çalıştıralım.
![TrimFace_10](../../images/freecad/curves_wb/surfaces_menu/TrimFace_10.png)  
Yüzeyin, seçilen (eğrinin dışında kalan) kısmı kaldı, seçilmeyen (eğrinin iç kısmı) silinip atıldı.
![TrimFace_11](../../images/freecad/curves_wb/surfaces_menu/TrimFace_11.png)  
Modelin izometrik görünümü:
![TrimFace_12](../../images/freecad/curves_wb/surfaces_menu/TrimFace_12.png)  
`Trim face` komutunu kullanmak için çember, elips, dikdörtgen,..vb kapalı eğri kullanmak zorunda değiliz. Aşağıdaki resme bakın.
![TrimFace_13](../../images/freecad/curves_wb/surfaces_menu/TrimFace_13.png)  
Üst görünüşten bakarak önce eğri parçalarını ardından yüzeyi seçiyorum.
![TrimFace_14](../../images/freecad/curves_wb/surfaces_menu/TrimFace_14.png)  
Yüzey seçimi yaparken, eğrinin alt kısmına tıklıyorum.
![TrimFace_15](../../images/freecad/curves_wb/surfaces_menu/TrimFace_15.png)  
**Trim face** komutu çalıştırıldığında, seçili yüzey tarafı (eğrinin alt kısmı) kalıyor, eğrinin üst kısmı kesilip atılıyor.
![TrimFace_16](../../images/freecad/curves_wb/surfaces_menu/TrimFace_16.png)  
İşlem sonrası izometrik görünüş;
![TrimFace_17](../../images/freecad/curves_wb/surfaces_menu/TrimFace_17.png)  
Bu kez, üst görünüşten bakarak önce eğri parçalarını ardından eğrinin üst kısmındaki yüzeyi seçerek komutu çalıştırıyorum.
![TrimFace_18](../../images/freecad/curves_wb/surfaces_menu/TrimFace_18.png)  
Beklediğimiz gibi, eğrinin alt kısmındaki yüzey parçası siliniyor.
![TrimFace_19](../../images/freecad/curves_wb/surfaces_menu/TrimFace_19.png)  
İzometrik görünüş;
![TrimFace_20](../../images/freecad/curves_wb/surfaces_menu/TrimFace_20.png)  
Eğer bir kaç yüzey parçasının uc uca eklenmesi ile elde edilmiş yüzey yapısı varsa, bu komut nasıl çalışır, bu konuyu inceleyelim.
![TrimFace_21](../../images/freecad/curves_wb/surfaces_menu/TrimFace_21.png)  
Eğri parçalarının ardından, en sağdaki yüzeyin üst kısmını seçiyorum. Yüzey rengine bakarak hangi yüzeylerin seçili olduğunu anlayabilirsiniz.
![TrimFace_22](../../images/freecad/curves_wb/surfaces_menu/TrimFace_22.png)  
Gördüğünüz gibi "Trim face" komutu, sadece seçili yüzeyi etkiledi. Seçilmeyen yüzeylerin tamamı silindi.
![TrimFace_23](../../images/freecad/curves_wb/surfaces_menu/TrimFace_23.png)  
İzometrik görünüş;
![TrimFace_24](../../images/freecad/curves_wb/surfaces_menu/TrimFace_24.png)  
Yüzey seçimi yaparken Sağ taraftan başlayarak bağlantılı üç yüzeyi **Ctrl** tuşu yardımıyla seçiyorum.
![TrimFace_25](../../images/freecad/curves_wb/surfaces_menu/TrimFace_25.png)  
Görülüyor ki, sadece seçili 3 yüzey üzerinde kesme işlemi uygulanmış.
![TrimFace_26](../../images/freecad/curves_wb/surfaces_menu/TrimFace_26.png)  
Seçilmeyen tüm yüzeyler silinmiş.
![TrimFace_27](../../images/freecad/curves_wb/surfaces_menu/TrimFace_27.png)  
Şimdi tüm yüzeyleri seçerek komutu çalıştıralım.
![TrimFace_28](../../images/freecad/curves_wb/surfaces_menu/TrimFace_28.png)  
Sonuç beklediğimiz gibi, tüm yüzeyler üzerinde kesim işlemi gerçekleşmiş.
![TrimFace_29](../../images/freecad/curves_wb/surfaces_menu/TrimFace_29.png)  
İzometrik görünüş (Sol - Üst)
![TrimFace_30](../../images/freecad/curves_wb/surfaces_menu/TrimFace_30.png)  
İzometrik görünüş (Sağ - Üst)
![TrimFace_31](../../images/freecad/curves_wb/surfaces_menu/TrimFace_31.png)  

[<<< Surfaces Menü Komutlarına Ait Sayfaya Dön]({filename}curves_wb_surfaces_00_menu.md)
