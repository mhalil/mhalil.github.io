Title: Pandas - ya da operatörü
Date: 2022-07-16 00:00 
Modified: 2025-11-30 22:00
Category: Pandas
Tags: Python, Pandas, Kütüphane, Modül, Filtre, yada, operatörü
Author: Mustafa Halil

# `|` (ya da / veya) Operatörü

İki farklı kriterin de geçerli olduğu verileri filtrelemek istediğimizde **VEYA / YA DA (or)** simgesi olan `|` karakteri kullanılır.  `|` karakteri yerine `or` kelimesi kullanırsanız **hata alırsınız.**

Örnek Veri çerçevemiz aşağıda görünmektedir.

```python
import pandas as pd
imdb = pd.read_excel("Veri_Setleri/imdb.xlsx", decimal=",")
print(imdb)
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 2   | The Godfather: Part II   | 1974 | 9.0  | 488889       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| ... | ...                      | ...  | ...  | ...          |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |
| 243 | In the Heat of the Night | 1967 | 7.9  | 37081        |
| 244 | Arsenic and Old Lace     | 1944 | 7.9  | 45893        |
| 245 | Before Sunrise           | 1995 | 7.9  | 100974       |
| 246 | Papillon                 | 1973 | 7.9  | 62517        |

247 rows × 4 columns

**Yıl** sütunundaki değerin **2.000'den büyük** ya da **Oylayan_Kişi** sütunundaki değerin de **500.000'den büyük** olduğu verileri filtrelemek istersek aşağıdaki kodları kullanabiliriz.

```python
yıl_2000den_buyuk = imdb["Yıl"] > 2000
Oylayan_Kişi_500000 = imdb["Oylayan_Kişi"] > 500000

print(imdb[yıl_2000den_buyuk | Oylayan_Kişi_500000])
```

|     | Film_Adı                 | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------ | ---- | ---- | ------------ |
| 0   | The Shawshank Redemption | 1994 | 9.2  | 1071904      |
| 1   | The Godfather            | 1972 | 9.2  | 751381       |
| 3   | Pulp Fiction             | 1994 | 8.9  | 830504       |
| 4   | The Dark Knight          | 2008 | 8.9  | 1045186      |
| 6   | Schindler's List         | 1993 | 8.9  | 545703       |
| ... | ...                      | ...  | ...  | ...          |
| 231 | Shutter Island           | 2010 | 8.0  | 436151       |
| 233 | Incendies                | 2010 | 8.0  | 36751        |
| 236 | 3 Idiots                 | 2009 | 8.0  | 83178        |
| 237 | The Artist               | 2011 | 8.0  | 132672       |
| 242 | Mystic River             | 2003 | 7.9  | 256159       |

81 rows × 4 columns

> NOT: Python'da sayısal işlem yaparken, Nokta `.` karakterinin ondalık ayırıcı olarak kullanıldığını öğrenmiştik. Peki Binlik ayırıcı için alternatif bir yol oluşturulmamış mı? derseniz; Binlik ayırıcı olarak altçizgi `_` karakterini kullanabileceğimizi ifade edebilirim.

Yukarıdaki kodu ilk okuduğumuzda `2000` ifadesinin **İki Bin** mi? **Yirmi Bin** mi olduğunu ya da `500000` ifadesinin **Beş Milyon** mu? **Beşyüz Bin** mi? olduğunu hemen farkedemiyor olabiliriz. Bunu kolaylaştırmak için Binlik ayırıcı `_` karakterini kullanarak kodu aşağıdaki şekilde revize edebiliriz. Bu durumda da aynı sonucu elde ederiz.

```python
yıl_2000den_buyuk = imdb["Yıl"] > 2_000    # 2000 ile aynı
Oylayan_Kişi_500000 = imdb["Oylayan_Kişi"] > 500_000    # 500000 ile aynı

print(imdb[yıl_2000den_buyuk | Oylayan_Kişi_500000])
```

|     | Film_Adı                                          | Yıl  | Puan | Oylayan_Kişi |
| --- | ------------------------------------------------- | ---- | ---- | ------------ |
| 4   | The Dark Knight                                   | 2008 | 8.9  | 1045186      |
| 7   | The Lord of the Rings: The Return of the King     | 2003 | 8.8  | 758388       |
| 10  | The Lord of the Rings: The Fellowship of the R... | 2001 | 8.8  | 784999       |
| 14  | Inception                                         | 2010 | 8.7  | 844938       |
| 18  | The Lord of the Rings: The Two Towers             | 2002 | 8.7  | 680983       |
| 49  | The Departed                                      | 2006 | 8.4  | 540726       |
| 56  | The Dark Knight Rises                             | 2012 | 8.4  | 672751       |
| 105 | Batman Begins                                     | 2005 | 8.3  | 604923       |
| 107 | Inglourious Basterds                              | 2009 | 8.2  | 505702       |
| 162 | V for Vendetta                                    | 2005 | 8.1  | 507750       |
| 165 | The Avengers                                      | 2012 | 8.1  | 568037       |
| 216 | Pirates of the Caribbean: The Curse of the Bla... | 2003 | 8.0  | 519625       |
