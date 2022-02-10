# Python'a Giriş

Bu bölümün amacı, Python programlama dili hakkında kısaca bilgi vermek ve ardından FreeCAD programı içerisinde Python kodu yazmayı ve/veya yazdığımız kodları çalıştırmayı öğrenmektir.
Bu, Python'a yeni başlayanlar için kısa bir eğitimdir. Python, açık kaynaklı, çok platformlu bir programlama dilidir. Onu diğer programlama dillerinden farklı kılan ve yeni kullanıcılar için çok erişilebilir kılan çeşitli özelliklere sahiptir:

+ Python, İnsanlar tarafından okunabilecek şekilde tasarlanmıştır, bu da öğrenmeyi ve anlamasını nispeten kolaylaştırır.
+ Python Yorumlanır bir dildir, bu, programların çalıştırılmadan önce derlenmesine gerek olmadığı anlamına gelir. Python kodu dilerseniz satır satır dahi olsa anında çalıştırılabilir.
+ Python, bir betik dili olarak diğer programlara gömülebilir. FreeCAD, gömülü bir Python yorumlayıcısına sahiptir. FreeCAD'in parçalarını işlemek için Python kodu yazabilirsiniz. Bu çok güçlüdür, kendi araçlarınızı oluşturabileceğiniz anlamına gelir.
+ Genişletilebilir, yeni modülleri Python kurulumunuza kolayca bağlayabilir ve işlevselliğini artırabilirsiniz. Örneğin, Python'un görüntüleri okumasına ve yazmasına, Twitter ile iletişim kurmasına, işletim sisteminiz tarafından gerçekleştirilecek görevleri zamanlamasına ,... vb. izin veren modüller vardır.

Aşağıdakiler python konusunda temel bir bilgilerdir ve bu eksiksiz bir eğitim değildir. Ancak FreeCAD ve mekanizmaları (yöntemi, tekniği, düzeneği) hakkında daha fazla araştırma yapmak için iyi bir başlangıç noktası sağlayacağını umuyorum. Aşağıdaki kod parçacıklarını bir Python yorumlayıcısına girmenizi şiddetle tavsiye ederiz.

# Yorumlayıcı (İnterpreter)

Genellikle bilgisayar programları yazarken, bir metin düzenleyici veya özel programlama ortamınızı (temelde bazı ek araçlar içeren bir metin düzenleyicidir) açarsınız, programınızı yazarsınız, ardından derler ve çalıştırırsınız. Genellikle giriş sırasında bir veya daha fazla hata yapılır, bu nedenle programınız çalışmaz. Kodların doğru çalışmamasına dair neyin yanlış gittiğini bildiren bir hata mesajı bile alabilirsiniz. Ardından metin düzenleyicinize geri dönün, hataları düzeltin, tekrar çalıştırın, programınız istendiği gibi çalışana kadar tekrarlayın.

Python'da tüm süreç Python yorumlayıcısı içinde şeffaf bir şekilde yapılabilir. Yorumlayıcı, basitçe Python kodunu yazabileceğiniz komut istemine sahip bir Python penceresidir. Python'u bilgisayarınıza yüklediyseniz (Windows veya Mac kullanıyorsanız Python web sitesinden indirin, GNU/Linux kullanıyorsanız paket havuzunuzdan yükleyin), başlat menünüzde bir Python yorumlayıcısı olacaktır. Ancak, daha önce de belirtildiği gibi, FreeCAD ayrıca yerleşik bir Python yorumlayıcısına sahiptir.

![Python_konsolu](img/python_konsolu.png)

FreeCAD içerisinde Python konsolunu Göremiyorsanız, **Görünüm → Paneller → Python konsolu**'na tıklayın. Python konsolu yeniden boyutlandırılabilir ve ayrıca yerinden ayrılabilir / taşınıp hareket ettirilebilir.

**Yorumlayıcı**, öncelikle bilgisayarınızda kurulu olan **Python sürüm bilgisini**, ardından komut istemi olan bir `>>>` sembolünü gösterir. Yorumlayıcı içerisinde kod yazmak basittir: her satır bir talimattır. Enter tuşuna bastığınızda, kod satırınız yürütülür/çalıştırılır. Örneğin, şunu yazmayı deneyin: 

`print("merhaba")`

***print()***, ekrana bir şey yazdıran bir Python komutudur. Enter'a bastığınızda işlem gerçekleştirilir ve **"merhaba"** mesajı yazdırılır. Bir hata yaparsanız, örneğin şunu yazalım:

`print(merhaba)`

Python bunun hatalı bir kod olduğunu size hemen söyleyecektir. Bu durumda Python **merhaba** ifadesinin ne olduğunu bilmiyor. `" "` (çift tırnak işaretleri) karakterleri, içeriğin bir metin parçası için programlama jargonu olan bir **dize (string)** olduğunu belirtir. Bunlar olmadan `print()` komutu **merhaba**'yı tanımıyor. Yukarı oka basarak son kod satırına geri dönebilir ve kodu düzeltebilirsiniz.

Python yorumlayıcısı ayrıca yerleşik bir yardım sistemine sahiptir. Diyelim ki `print(merhaba)` ile neyin yanlış gittiğini anlamadık ve komut hakkında özel bilgi istiyoruz:

`help("print")`

Bu komutu yazıp çalıştırdığınızda `print()` komutunun yapabileceği her şeyin uzun ve eksiksiz bir açıklamasını alacaksınız (açıklamalar konsol ekranında görüntülenecektir).
Artık Python yorumlayıcısını anladığınıza göre, daha ciddi şeylerle devam edebiliriz.

# Değişkenler


# Modüller