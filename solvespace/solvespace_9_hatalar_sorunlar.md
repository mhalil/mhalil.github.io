Title: Solvespace Bölüm 9: Bilinen Hatalar ve Sorunlar
Date: 2022-03-10 20:00
Category: Solvespace
Tags: Solvespace, 3D, 3B, CAD, Kılavuz, Hata, Sorun, Analiz, NURBS, Yüzey, Mesh, STL, Eğri, Trim, Kırp, Çizgi, Parça, Açık, Kenar, Göster, Kesişim, Böl
Author: Mustafa Halil


## Bölüm 9: Bilinen Hatalar ve Sorunlar

Mantıksal (Boolean: ekleme, çıkarma, kesişim) 
işlemleri üçgen ağlarda/kafeslerde/mesh (tam NURBS yüzeyleri yerine) 
gerçekleştirildiğinde, elde edilen ağ/kafes (mesh) yapısı kalitesi, 
genellikle düşük olacaktır. Eğriler farklı şekilde parçalı-doğrusal 
olarak yaklaştırılsaydı, daha az üçgenle eşit derecede iyi bir ağ/kafes 
yapısı elde edilebilirdi, veya ağ/kafes, uzun ince üçgenler içerebilir.

Bu, dışa aktarılan STL dosyalarının yüksek 
kaliteli bir ağ/kafes yapısı içermeyeceği anlamına gelir. Bu genellikle 
bir sorun değildir, ancak bazı uygulamalarda sorun olabilir. Özellikle, 
dışa aktarılan ağ/kafes yapısı artık tam olarak 2 manifoldlu (yani çok 
sıkı, geçirimsiz) olmayabilir. Bu sorunu `Analiz → Açık Kenarları Göster` ile kontrol edin.

Diğer bir sonuç ise üçgen sayısı arttıkça 
programın daha yavaş çalışmasıdır. Yapıyı oldukça kaba bir ağ/kafes 
yapısı ile çizmek/ oluşturmak iyi bir fikirdir. Dışa aktarmadan önce 
nüans/akor (chord) toleransını azaltın; böylece parça, daha ince bir 
ağ/kafes yapısı ile yeniden oluşturulacaktır.

NURBS yüzeylerde Mantıksal (Boolean: ekleme, 
çıkarma, kesişim) işlemler gerçekleştirildiğinde, ağ/kafes yapı kalitesi
 genel olarak çok daha iyi olacaktır. Ancak bazı yüzey kesişim türleri 
mevcut NURBS Boole'ları tarafından işlenmez, bu nedenle bazı durumlarda 
istenen işlemi bir NURBS Boole olarak gerçekleştirmek imkansız olabilir.

NURBS Boole değerleri de, nüans/akor (chord) 
toleransından etkilenir. Bu tolerans çok kabaysa işlemler başarısız 
olabilir, ancak tolerans azaldıkça rutinler yavaşlar. Sorunlar ortaya 
çıkarsa, genellikle bu toleransı değiştirmek yarar olur.

Hızı ve ağ/kafes yapı kalitesini iyileştirmek 
için parçayı daha az Boole işlemi kullanarak çizin. Örneğin delikli bir 
levha iki farklı şekilde modellenebilir. Birinci yöntem olarak; 
Kullanıcı plakayı katılar/ekstrüde edebilir ve ardından ikinci bir daire
 çizip katılar/ekstrüde eder, daireyi plakadan fark/çıkarım (difference)
 işlemi ile boşaltıp bir delik oluşturabilir. İkinci yöntem olarak ise; 
kullanıcı, hem plakanın hem de deliğin ana hatlarıyla tek bir eskiz 
olarak çizebilir ve yalnızca bir kez doğrusal katılama/ ekstrüzyon 
işlemi uygular. Son seçeneği tercih etmek daha doğrudur.

Diğer çizim programlarından aşina olduğumuz **Kırpma (Trim)** komutu, SolveSpace içerisinde de mevcuttur. Karmaşık eskizler çizilirken kırpma komutunu kullanmak yararlı olabilir. Komut'a `Çizim → Eğrileri Kesişim Yerinden Böl` menü yolundan ya da `I` (büyük harf ile `I` küçük harf ile `i`) kısayol tuşundan erişebilirsiniz. Menüdeki komut adında **Eğriler** ibaresi geçse de, komut **Çizgi Parçaları** için de kullanılabiliyor.
