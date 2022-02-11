# FreeCAD içinde Python Komut Dosyası (Script) Oluşturmak

[Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29) kullanımı ve öğrenmesi çok kolay bir programlama dilidir. Açık kaynak kodlu, çok platformlu ve basit kabuk komut dosyalarının programlanmasından çok karmaşık programlara kadar pek çok şey için tek başına kullanılabilir. Ancak, en yaygın kullanımlarından biri, diğer uygulamalara gömülmesi kolay bir komut dosyası dilidir. FreeCAD içinde tam olarak böyle kullanılır. Python konsolundan veya özel komut dosyalarınızdan FreeCAD'e kılavuzluk yapabilir ve grafik kullanıcı arabirimi aracı olmayan çok karmaşık eylemler gerçekleştirmesini sağlayabilirsiniz. 
Örneğin, bir python betiğinden şunları yapabilirsiniz:
+ Yeni nesneler oluşturabilirsiniz
+ Mevcut nesneleri değiştirebilirsiniz
+ Bu nesnelerin 3D gösterimini değiştirebilirsiniz
+ FreeCAD arayüzünü değiştirebilirsiniz

FreeCAD'de python'u kullanmanın birkaç farklı yolu vardır:
+ "Komut satırı" tarzı bir arayüzde komutlar verebileceğiniz FreeCAD Python yorumlayıcısından. 
+ Eksik bir aracı FreeCAD arayüzüne hızlı bir şekilde eklemenin uygun bir yolu olan makrolardan.
+ Oldukça karmaşık çözümler oluşturmak için kullanılabilen harici komut dosyalarından, hatta tüm Çalışma Tezgahlarından (Workbench'lerden).

Python komut dosyası oluşturmaya devam etmeden önce Düzenle → Tercihler → Genel → Çıktı penceresine gidin ve iki kutuyu işaretleyin:
+ **Rapor görünümüne dahili Python çıktısını yeniden yönlendirin. (Redirect internal Python output to report view.)**
+ **Rapor görünümüne dahili Python hatalarını yeniden yönlendirin. (Redirect internal Python errors to report view.)**

Ardından Görünüm → Paneller'e gidin ve şunları kontrol edin:
+ **Rapor görünümü. (Report view. )**

# Python kodu yazma