Title: Solvespace Bölüm 6: Analiz
Date: 2022-02-26 11:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Analiz, İzle, Nokta, Hacim, Alan, Hesap, Serbestlik, Derece, Göster, 
Author: Mustafa Halil


## Bölüm 6: Analiz

## İzlenecek Nokta

SolveSpace, bir nokta hareket ederken, noktanın 
arkasında bir "iz" çizebilir. Bu, mekanizma tasarlanırken kullanışlı bir
 yöntemdir. Aşağıda gösterilen çizim üç çubuklu bir bağlantıdır:  
![İzlenecek Nokta](images/solvespace/40%20%C4%B0zlenecek%20Nokta.png)

Şekildeki bağlantılı kollara sahip sistem 
çalışırken, orta bağlantının merkez noktası, turkuaz renkli eğri boyunca
 hareket eder. Bu görüntü, bağlantılı kollar çizildikten sonra bu orta 
nokta izlenmek üzere ayarlanıp ardından bağlantı, fare ile tüm hareket 
aralığı boyunca sürüklenerek üretildi.

İzlemeye başlamak için bir nokta seçin ve `Analiz → İzlenecek Nokta`'yı seçin. Nokta hareket ettiğinde, arkasında turkuaz renkli izi çizilecektir.

İzlemeyi durdurmak için `Analiz → İzlemeyi Durdur...`'u
 seçin. İzlemeyi bir CSV (virgülle ayrılmış değer) dosyası olarak 
kaydetme seçeneği ile bir iletişim kutusu görünecektir. İzleme 
verilerini kaydetmek için iletişim kutusuna bir dosya adı yazın. İz 
versini kaydetmemek için `İptal`'i seçin veya `Esc` tuşuna basın.

İzleme verisi, her satırda bir noktaya ait anlık 
konum bilgisi olacak şekilde metin dosyası olarak kaydedilir. Her 
nokta, virgülle ayrılmış olarak x, y, z biçiminde görünür. Excel gibi 
elektronik tablolar da dahil olmak üzere birçok program bu formatı 
okuyabilir. Koordinat birimleri, dışa aktarma ölçek faktörü tarafından 
belirlenir. (Dışa aktarma ölçek faktörü 1 ise, bunlar milimetredir ve 
25.4 ise o zaman inçtir.)

Mekanizma, fare ile sürüklenerek çalıştırılırsa, 
farenin hareketi düzensiz olacağı için, izdeki (iz verisindeki) noktalar
 eşit olmayan aralıklı olacaktır. x'e karşı **t** grafiği (yukarıdaki turkuaz renkli iz gibi) etkilenmez, ancak **x** veya **y**'ye karşı **t** grafiği işe yaramaz, çünkü eğri boyunca "**hız**" sabit değildir.

Bu sorunu önlemek için, fare ile sürüklemek 
yerine bir boyutu adımlayarak noktayı hareket ettirin. Adım ölçüsünü 
seçin; bu herhangi bir mesafe veya açı olabilir. `Analiz → Adım Ölçüsünü Ayarla...`'yı seçin. Bu ölçü için yeni bitiş değerini (finish) ve adım sayısını (step) belirtin; ardından "`step dimension now` (ölçüyü şimdi adımla)"ya tıklayın.

![Adım Ölçüsü](images/solvespace/41%20Adim%20Olcusu.png)

Seçilen ölçü birden fazla adımda değiştirilecek 
ve her bir ara değerde çözülecektir. Örneğin, şimdi (başlangıçta) 10 
dereceye ayarlanmış bir ölçü düşünün. Kullanıcı bu boyutu 10 adımda 30 
dereceye çıkarır (Bitiş Ölçüsü). Bu, SolveSpace'in 30 dereceye ulaşana 
kadar 12 derecede, sonra 14 derecede, sonra 16'da vb. çözeceği anlamına 
gelir. ( Yani 30° - 10° = 20°, 10 adımda hesaplanacak ise her adımda 
20° / 10 adım = 2° artırım yapılacaktır. [ Formül = (bitiş ölçüsü - 
başlangıç ölçüsü) / adım sayısı] )

İzlenen noktanın konumu, her ara değerde 
kaydedilecektir. İz verisi dışa aktarıldığında, boyutlandırılmış 
bağlantı, sabit açısal hızla döndüğü için o, noktanın konumunu temsil 
eder.

Adım ölçüsü ayarlama özelliği, yakınsamayı da 
iyileştirebilir. Bazı zor durumlarda, bir ölçü değiştirildiğinde çözücü 
bir çözüm bulamaz. Belirtilen kısıtlamaların birden fazla çözümü varsa, 
çözücü istenmeyen bir çözüm de bulabilir. Bu durumda, boyutu tek adımda 
değiştirmek yerine yeni adım değeri atamayı denemek faydalı olabilir.

## Hacmi Hesapla

Bu özellik, çizilen parçanın hacmini bildirir. 
Aktif birimlere bağlı olarak hacim inç küp veya mililitre ve milimetre 
küp olarak verilir.

Parça düzgün eğriler (örneğin çemberler/daireler)
 içeriyorsa bu eğriler, ağ/kafes geometrisinin tam bir temsili değildir.
 Bu, ölçülen hacmin yalnızca bir tahmin olduğu anlamına gelir; Ekranda 
oldukça düzgün görünen bir ağ/kafes için yüzde bir (%1) civarında bir 
hata olabileceğini bekleyin (bilin). Bu hatayı azaltmak için daha ince 
bir nüans/akor toleransı seçin.

![Nüans/Akor (Chord) Toleransı](images/solvespace/42%20Nuans-akor%20toleransi.png)

## Alanı Hesapla

Bu özellik, geçerli çizimin alanını bildirir. 
Çizimde kullanılan aktif birimlere bağlı olarak, alan inç kare veya 
milimetre kare olarak verilir.

Kavisli (Eğrisel) yapıya ait çizimlerde alan 
ölçümü/hesabı yapılırken, parçalı doğrusal çizgi yaklaşımı kullanılarak
 hesaplama gerçekleştirilir. Bu, bazı hatalara yol açar; bu hatayı 
azaltmak için daha iyi bir nüans/akor toleransı seçin. Geçerli çizim iyi
 biçimlendirilmiş bir düzlem eğrisi değilse (örneğin, kapalı bir eğri 
değilse veya kendisiyle kesişiyorsa), alan tanımlanamadığı için, bir 
hata bildirilir.

## Serbestlik Derecelerini Göster

Bu özellik, çizimdeki hangi noktaların tamamen 
kısıtlanmadığını gösterir (yani, kullanıcı onları fareyle sürüklediğinde
 hangi noktaların hareket edeceğini). Serbest noktalar, üzerlerinde 
büyük turkuaz renkli bir kare ile gösterilir. Sıfır serbestlik dereceli 
(tamamen kısıtlanmış) bir çizimde hiçbir şey gösterilmez. Bir serbestlik
 derecesine sahip bir çizimde, bir veya daha fazla nokta 
işaretlenecektir; birden fazla noktanın işaretlenmesi mümkündür, çünkü 
bu bir serbestlik derecesi, birden çok nokta üzerinden sürüklenebilir 
olabilir.

Büyük turkuaz renkli kareleri silmek için `Düzenle → Tümünü Yeniden Oluştur`'u seçerek veya `bir noktayı sürükleyerek` ya da `ESC` tuşuna basarak çizimi yeniden çözün.

![Kısıtlanmamış Noktalar](images/solvespace/43%20Kisitlanmamis%20noktalar.png)
