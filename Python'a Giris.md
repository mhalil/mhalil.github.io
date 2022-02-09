# Python'a Giriş

Bu bölümde **Python** programlama dili hakkında kısaca bilgi verecek ve ardından **FreeCAD** programı içerisinde Python kodu yazmayı ve/veya yazdığımız kodları çalıştırmayı öğreneceğiz.

Python programlama dili, insanlar tarafından klayca okunabilecek şekilde tasarlanmıştır, bu da öğrenmeyi ve anlaşılmasını nispeten kolaylaştırır.

Python Yorumlanır bir dildir, bu, programların çalıştırılmadan önce derlenmesine gerek olmadığı anlamına gelir. Python kodu dilerseniz satır satır dahi olsa anında çalıştırılabilir.

Python, bir **betik dili (script)** olarak diğer programlara gömülebilir. FreeCAD, gömülü bir Python yorumlayıcısına sahiptir. FreeCAD'in parçalarını işlemek için Python kodu yazabilirsiniz. Bu çok güçlüdür, kendi araçlarınızı oluşturabileceğiniz anlamına gelir.

Genişletilebilir, yeni modülleri Python kurulumunuza kolayca bağlayabilir ve işlevselliğini artırabilirsiniz. Örneğin, Python'un, görüntüleri işlemesine (okumasına ve yazmasına), Twitter ile iletişim kurmasına, işletim sisteminiz tarafından gerçekleştirilecek görevleri zamanlamasına vb. izin veren modüller vardır.

Genellikle bilgisayar programları yazarken, bir metin düzenleyici veya özel programlama ortamınızı (temelde bazı ek araçlar içeren bir metin düzenleyicidir) açarsınız, programınızı yazarsınız, ardından derler ve çalıştırırsınız. Genellikle programlamaya giriş sırasında bir veya daha fazla hata yapılır, bu nedenle programınız çalışmaz. Kodların doğru çalışmamasına dair neyin yanlış gittiğini bildiren bir hata mesajı alabilirsiniz. Ardından metin düzenleyicinize geri dönün, hataları düzeltin, tekrar çalıştırın, programınız istendiği gibi çalışana kadar tekrarlayın.

Python'da tüm süreç Python yorumlayıcısı içinde şeffaf bir şekilde yapılabilir. Yorumlayıcı, basitçe Python kodunu yazabileceğiniz komut istemine sahip bir Python penceresidir. Python'u bilgisayarınıza yüklediyseniz (Windows veya Mac kullanıyorsanız Python web sitesinden indirin, GNU/Linux kullanıyorsanız paket havuzunuzdan yükleyin), başlat menünüzde bir Python yorumlayıcısı olacaktır. Ancak, daha önce de belirtildiği gibi, FreeCAD ayrıca **yerleşik bir Python yorumlayıcısına** sahiptir.

![Python_konsolu](img/python_konsolu.png)

FreeCAD içerisinde Python konsolunu Göremiyorsanız, **Görünüm → Paneller → Python konsolu**'na tıklayın. Python konsolu yeniden boyutlandırılabilir ve ayrıca yerinden ayrılabilir / taşınıp hareket ettirilebilir.

**Yorumlayıcı**, öncelikle bilgisayarınızda kurulu olan **Python sürüm bilgisini**, ardından komut istemi olan bir `>>>` sembolünü gösterir. Yorumlayıcı içerisinde kod yazmak basittir: her satır bir talimattır. Enter tuşuna bastığınızda, kod satırınız yürütülür/çalıştırılır.

# Modüller