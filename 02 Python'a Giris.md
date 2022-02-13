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

![Python_konsolu](FreeCAD/img/python_konsolu.png))

FreeCAD içerisinde Python konsolunu Göremiyorsanız, **Görünüm → Paneller → Python konsolu**'na tıklayın. Python konsolu yeniden boyutlandırılabilir ve ayrıca yerinden ayrılabilir / taşınıp hareket ettirilebilir.

**Yorumlayıcı**, öncelikle bilgisayarınızda kurulu olan **Python sürüm bilgisini**, ardından komut istemi olan bir `>>>` sembolünü gösterir. Yorumlayıcı içerisinde kod yazmak basittir: her satır bir talimattır. Enter tuşuna bastığınızda, kod satırınız yürütülür/çalıştırılır. Örneğin, şunu yazmayı deneyin: 

    print("merhaba")

**print()**, ekrana bir şey yazdıran bir Python komutudur. Enter'a bastığınızda işlem gerçekleştirilir ve **"merhaba"** mesajı yazdırılır. Bir hata yaparsanız, örneğin şunu yazalım:

    print(merhaba)

Python bunun hatalı bir kod olduğunu size hemen söyleyecektir. Bu durumda Python **merhaba** ifadesinin ne olduğunu bilmiyor. `" "` (çift tırnak işaretleri) karakterleri, içeriğin bir metin parçası için programlama jargonu olan bir **dize (string)** olduğunu belirtir. Bunlar olmadan `print()` komutu **merhaba**'yı tanımıyor. Yukarı oka basarak son kod satırına geri dönebilir ve kodu düzeltebilirsiniz.

Python yorumlayıcısı ayrıca yerleşik bir yardım sistemine sahiptir. Diyelim ki `print(merhaba)` ile neyin yanlış gittiğini anlamadık ve komut hakkında özel bilgi istiyoruz:

    help("print")

Bu komutu yazıp çalıştırdığınızda `print()` komutunun yapabileceği her şeyin uzun ve eksiksiz bir açıklamasını alacaksınız (açıklamalar konsol ekranında görüntülenecektir).
Artık Python yorumlayıcısını anladığınıza göre, daha ciddi şeylerle devam edebiliriz.

# Değişkenler

Programlamada sıklıkla bir isim altında bir değer saklamanız gerekir. İşte burada değişkenler devreye girer. Örneğin şunu yazın:

	a = "merhaba"
	print(a)

Muhtemelen burada ne olduğunu anlamışsınızdır, **merhaba** dizesini (string) **"a"** adı altında kaydettik, **"a"** değişkenine atadık. Artık **"a"** bilindiğine göre, onu herhangi bir yerde kullanabiliriz, örneğin **print()** komutunda. Değişken olarak istediğimiz herhangi bir ismi kullanabiliriz, sadece boşluk karakteri veya noktalama işaretleri kullanmamak (değişken adı rakam ile başlayamaz) ve Python anahtar kelimeleri kullanmamak gibi bazı basit kurallara uymamız gerekiyor. Örneğin şunu yazabiliriz:

	merhaba = "şahsi selamlama mesajım"
	print(merhaba)

Artık **merhaba** kelimesi tanımsız değil, bir değişken olarak tanımlanmış durumda. Değişkenler herhangi bir zamanda değiştirilebilir, bu yüzden **değişkenler** olarak adlandırılırlar, içerikleri değişebilir. Örneğin:

	degiskenim = "merhaba"
	print(degiskenim)
	degiskenim = "hoşçakal"
	print(degiskenim)

Görüldüğü üzere **degiskenim** isimli değişkenin değerini değiştirdik.

	degisken1 = "merhaba"
	degisken2 = degisken1
	print(degisken2)

Değişkenlerinize anlamlı isimler vermenizi tavsiye edilir. Bir süre sonra değişkeninizin neyi temsil ettiğini hatırlamayacaksınız. Ancak, örneğin hoşgeldiniz mesajım adını verdiyseniz, amacını kolayca hatırlayacaksınız. 

İsimlendirme çok önemli, **myVariable** ile **myvariable** aynı şey değil. Değişkeni tanımlarken isim olarak **myVariable** belirlemişseniz  ``print(myvariable)`` komutunu çalıştırmaya çalıştığınızda, değişkenin  tanımlanmadığına dair hata alacaksınız. Python’da Büyük-küçük harf duyarlılığı vardır.

# Sayılar

Tabii ki Python programları sadece metin dizileriyle değil, her türlü veriyle uğraşabilir. Önemli olan bir şey var, Python ne tür verilerle uğraştığını bilmelidir. ``Print(merhaba)`` örneğimizde ``print()`` komutunun **"merhaba"** dizgemizi tanıdığını gördük. ``" "`` karakterlerini kullanarak, aşağıdakilerin bir metin dizesi olduğunu belirttik.

``type()`` komutu ile bir değişkenin veri tipini her zaman kontrol edebiliriz:

	deger = "merhaba"
	type(deger)

Bize **myVar**'ın içeriğinin **string** için kısa olan bir ``'str'`` olduğunu söyleyecektir. Ayrıca tamsayı ve ondalıklı sayılar gibi başka temel veri türlerimiz de vardır:

	ilkSayi = 10
	ikinciSayi = 20
	print(ilkSayi + ikinciSayi)
	type(ilkSayi)

Python, 10 ve 20'nin tamsayılar olduğunu bilir, bu nedenle ``'int'`` olarak saklanırlar ve Python tamsayılarla yapabileceği her şeyi onlarla yapabilir. Bunun sonuçlarına bakın:

	ilkSayi = “10”
	ikinciSayi = “20”
	print(ilkSayi + ikinciSayi)

Burada Python'u, iki değişkenimizin **sayı değil metin parçaları** olduğunu düşünmeye zorladık. Python iki parça metni birbirine ekleyebilir, ancak bu durumda elbette herhangi bir aritmetik işlem  gerçekleştirmeyecektir, metinler yan yana yazılacaktır. 

	var1 = 13
	var2 = 15.65
	print("var1 is of type ", type(var1))
	print("var2 is of type ", type(var2))

Tam sayılar ve Ondalıklı sayılar sorunsuz bir şekilde toplanabilir:

	toplam = var1 + var2
	print(toplam)
	print(type(toplam))

**var2** bir Ondalıklı Ondalıklı sayı olduğundan, Python otomatik olarak sonucun bir Ondalıklı sayı olması gerektiğine karar verir. Ancak Python'un hangi türü kullanacağını bilmediği durumlar da vardır. Örneğin:

	varA = "merhaba 123"
	varB = 456
	print(varA + varB)

Bu kod çalıştırıldığı zaman bir hata ile karşılaşılır, **varA** bir **dizedir (string)** ve **varB** bir **tamsayıdır** ve Python ne yapacağını bilmez. Ancak, Python'u türler arasında dönüşüm yapmaya zorlayabiliriz:

	varB = str(varB)

Ayrıca bir değişkeni tamsayıya dönüştürmek için ``int()`` ve ``float()`` kullanabilir ve istersek float kullanabiliriz:

	varA = "123"
	print(int(varA))
	print(float(varA))

``print()`` komutunu birkaç şekilde kullandığımızı fark etmiş olmalısınız. Değişkenleri, toplamları, virgülle ayrılmış birkaç şeyi ve hatta başka bir Python komutunun sonucunu yazdırdık. Belki bu iki komutu da görmüşsünüzdür:

	type(varA)
	print(type(varA))

Terminal / konsol içerisinde yazdığınızda, bu iki komut aynı sonucu verecektir. Bunun nedeni, yorumlayıcıda her şeyin otomatik olarak yazdırılmasıdır. Yorumlayıcının dışında çalışan daha karmaşık programlar yazdığımızda, bunlar otomatik olarak yazdırılmayacaktır, bu nedenle ``print()`` komutunu kullanmamız gerekecek. Bunu akılda tutarak, burada ``print()`` komutu kullanmayı bırakalım. Bundan sonraki anlatımlarda, kodları terminalde yazdığınızı düşünerek şu şekilde yazacağız:

	myVar = "hello friends"
	myVar


# Listeler






# Modüller

