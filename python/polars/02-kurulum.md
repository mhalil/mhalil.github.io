Title: Polars - 02 Kurulum
Date: 2026-06-14 22:20
Modified: 2026-06-27 22:47
Category: Polars
Tags: Python, Polars, Kütüphane, Modül, Kurulum
Author: Mustafa Halil
# Kurulum

Polars bir kütüphanedir ve kurulumu, ilgili programlama dilinin paket yöneticisini çağırmak kadar basittir.

Python

```python
pip install polars  # Veya AVX2 desteği olmayan eski CPU'lar için:
pip install polars[rtcompat]
```

Rust

```rust
cargo add polars -F lazy  # veya Cargo.toml [dependencies] polars = { version = "x", features = ["lazy", ...]}
```

## Büyük İndeks (Big Index)

Varsayılan olarak, Polars dataframe'leri 2^{32} satır (~4.3 milyar) ile sınırlıdır. Big index uzantısını etkinleştirerek bu sınırı 2^{64} (~18 kentilyon) satıra yükseltin:

Python

```bash
pip install polars[rt64]
```

Rust

```rust
cargo add polars -F bigidx  # veya Cargo.toml [dependencies] polars = { version = "x", features = ["bigidx", ...] }
```

## Eski CPU'lar (Legacy CPU)

[AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) desteği olmayan eski bir CPU'da Python için Polars kurmak için:

Python

```bash
pip install polars[rtcompat]
```

## İçe Aktarma (Importing)

Kütüphaneyi kullanmak için projenize dahil (import) edin:

Python

```python
import polars as pl
```

Rust

```rust
use polars::prelude::*;
```

## Özellik Bayrakları (Feature Flags)

Yukarıdaki komutu kullanarak Polars'ın çekirdeğini sisteminize kurmuş olursunuz. Ancak, kullanım durumunuza bağlı olarak isteğe bağlı bağımlılıkları da kurmak isteyebilirsiniz. Bunlar, boyutu en aza indirmek için isteğe bağlı hale getirilmiştir. Bayraklar programlama diline göre farklılık gösterir. Kılavuz boyunca, kullanılan bir işlevin ek bir bağımlılık gerektirdiğinde belirteceğiz.

### Python

```bash
# Örnek:
pip install 'polars[numpy,fsspec]'
```

#### Tümü (All)

| Etiket       | Açıklama                          |
|--------------|-----------------------------------|
| `all`        | Tüm isteğe bağlı bağımlılıkları kur. |

#### GPU

| Etiket | Açıklama                     |
|--------|-------------------------------|
| `gpu`  | Sorguları NVIDIA GPU'larında çalıştır. |

> **Not:**
Detaylı talimatlar ve ön koşullar için [GPU desteği](https://docs.pola.rs/user-guide/gpu-support/) bölümüne bakın.

#### Birlikte Çalışabilirlik (Interoperability)

| Etiket     | Açıklama                                           |
|------------|------------------------------------------------------|
| `pandas`   | Verileri pandas dataframe/series ile dönüştür.       |
| `numpy`    | Verileri NumPy dizileri ile dönüştür.                |
| `pyarrow`  | Verileri PyArrow tabloları/dizileri ile dönüştür.    |
| `pydantic` | Verileri Pydantic modellerinden Polars'a dönüştür.   |

#### Excel

| Etiket       | Açıklama                                        |
|--------------|--------------------------------------------------|
| `calamine`   | Excel dosyalarından calamine motoru ile oku.     |
| `openpyxl`   | Excel dosyalarından openpyxl motoru ile oku.     |
| `xlsx2csv`   | Excel dosyalarından xlsx2csv motoru ile oku.     |
| `xlsxwriter` | Excel dosyalarına XlsxWriter motoru ile yaz.     |
| `excel`      | Desteklenen tüm Excel motorlarını kur.           |

#### Veritabanı (Database)

| Etiket         | Açıklama                                                       |
|----------------|-----------------------------------------------------------------|
| `adbc`         | ADBC motoru ile veritabanlarından oku/yaz.                      |
| `connectorx`   | ConnectorX motoru ile veritabanlarından oku.                    |
| `sqlalchemy`   | SQLAlchemy motoru ile veritabanlarına yaz.                      |
| `database`     | Desteklenen tüm veritabanı motorlarını kur.                     |

#### Bulut (Cloud)

| Etiket   | Açıklama                                  |
|----------|--------------------------------------------|
| `fsspec` | Uzak dosya sistemlerinden oku/yaz.         |

#### Diğer Girdi/Çıktı (Other I/O)

| Etiket       | Açıklama                           |
|--------------|-------------------------------------|
| `deltalake`  | Delta tablolarından oku/yaz.       |
| `iceberg`    | Apache Iceberg tablolarından oku.  |

#### Diğer (Other)

| Etiket        | Açıklama                                               |
|---------------|---------------------------------------------------------|
| `async`       | LazyFrame'leri asenkron olarak topla.                   |
| `cloudpickle` | Kullanıcı tanımlı fonksiyonları serileştir.             |
| `graph`       | LazyFrame'leri grafik olarak görselleştir.              |
| `plot`        | `plot` namespace'i aracılığıyla dataframe'leri çiz.     |
| `style`       | `style` namespace'i aracılığıyla dataframe'leri stillendir. |
| `timezone`    | Zaman dilimi desteği.                                   |

### Rust

```toml
# Cargo.toml
[dependencies]
polars = { version = "0.26.1", features = ["lazy", "temporal", "describe", "json", "parquet", "dtype-datetime"] }
```

İsteğe bağlı özellikler:

-   Ek veri türleri:
    - `dtype-date`
    - `dtype-datetime`
    - `dtype-time`
    - `dtype-duration`
    - `dtype-i8`
    - `dtype-i16`
    - `dtype-i128`
    - `dtype-u8`
    - `dtype-u16`
    - `dtype-u128`
    - `dtype-categorical`
    - `dtype-struct`
- `lazy` - Lazy API:
    - `regex` - Sütun seçiminde regex kullan.
    - `dot_diagram` - Lazy mantıksal planlardan `dot` diyagramları oluştur.
- `sql` - SQL sorgularını Polars'a geçir.
- `streaming` - RAM'den büyük veri kümelerini işleyebil.
- `random` - Rastgele örneklenmiş değerlerle diziler oluştur.
- `ndarray` - `DataFrame`'den `ndarray`'e dönüştür.
- `temporal` - Zaman veri türleri için Chrono ve Polars arasında dönüşüm.
- `timezones` - Zaman dilimi desteğini etkinleştir.
- `strings` - `StringChunked` için ek string yardımcıları:
    - `string_pad` - `pad_start`, `pad_end`, `zfill` için.
    - `string_to_integer` - `parse_int` için.
- `object` - `ObjectChunked<T>` (T üzerinde generic) adı verilen genel ChunkedArray desteği. Bunlar Series'ten `Any` trait'i aracılığıyla aşağıya dönüştürülebilir.
- Performans ile ilgili:
    - `nightly` - SIMD ve özelleştirme gibi yalnızca nightly özellikleri.
    - `performant` - daha hızlı yollar, daha yavaş derleme süreleri.
    - `bigidx` - >> \\(2^{32}\\) satır bekliyorsanız bu özelliği etkinleştirin. Bu, polars'ın index olarak `u64` kullanarak çok daha fazla ölçeklenmesini sağlar. Bu özellik etkinleştirildiğinde birçok veri yapısı daha az önbellek verimli olduğu için Polars biraz daha yavaş olacaktır.
    - `cse` - Ortak alt plan eleme optimizasyonunu etkinleştir.
- IO ile ilgili:
    - `serde` - Serde serileştirme ve deserileştirme desteği. JSON ve daha fazla serde destekli serileştirme formatları için kullanılabilir.
    - `serde-lazy` - Serde serileştirme ve deserileştirme desteği. JSON ve daha fazla serde destekli serileştirme formatları için kullanılabilir.
    - `parquet` - Apache Parquet formatını oku.
    - `json` - JSON serileştirme.
    - `ipc` - Arrow'un IPC formatı serileştirme.
    - `decompress` - CSV'lerin sıkıştırmasını otomatik olarak algıla ve aç. Desteklenen sıkıştırmalar:
        - gzip
        - zlib
        - zstd
- DataFrame işlemleri:
    - `dynamic_group_by` - Önceden tanımlanmış anahtarlar yerine zaman penceresine göre gruplama. Ayrıca kayan pencere group by işlemlerini etkinleştirir.
    - `sort_multiple` - Bir dataframe'i birden çok sütuna göre sıralamaya izin ver.
    - `rows` - Satırlardan dataframe oluştur ve `dataframe`'lerden satır çıkar. Ayrıca `pivot` ve `transpose` işlemlerini etkinleştirir.
    - `join_asof` - ASOF Join, tam eşleşme yerine en yakın anahtarlarla birleştirme.
    - `cross_join` - İki dataframe'in Kartezyen çarpımını oluştur.
    - `semi_anti_join` - SEMI ve ANTI join'ler.
    - `row_hash` - DataFrame satırlarını `UInt64Chunked`'e hash'lemek için yardımcı.
    - `diagonal_concat` - Farklı şemaları birleştirerek çapraz birleştirme.
    - `dataframe_arithmetic` - Dataframe'ler ve diğer dataframe'ler veya seriler arasında aritmetik.
    - `partition_by` - Gruplara göre bölümlenmiş birden çok dataframe'e böl.
- Series/expression işlemleri:
    - `is_in` - Series'te üyelik kontrolü.
    - `zip_with` - İki `Series` / `ChunkedArray`'i birleştir.
    - `round_series` - Series'in temeldeki float türlerini yuvarla.
    - `repeat_by` - Bir dizideki öğeyi başka bir dizi tarafından belirtilen sayıda tekrarla.
    - `is_first_distinct` - Öğenin ilk benzersiz değer olup olmadığını kontrol et.
    - `is_last_distinct` - Öğenin son benzersiz değer olup olmadığını kontrol et.
    - `checked_arithmetic` - Geçersiz işlemlerde `None` döndüren kontrollü aritmetik.
    - `dot_product` - Series ve expression'lar üzerinde nokta/iç çarpım.
    - `concat_str` - String verilerini lineer zamanda birleştir.
    - `reinterpret` - Bitleri işaretli/işaretsiz olarak yeniden yorumlamak için yardımcı.
    - `take_opt_iter` - `Iterator<Item=Option<usize>>` ile bir series'ten al.
    - `mode` - En sık tekrarlanan değer(ler)i döndür.
    - `cum_agg` - `cum_sum`, `cum_min` ve `cum_max` toplamaları.
    - `rolling_window` - `rolling_mean` gibi kayan pencere fonksiyonları.
    - `interpolate` - Aradaki `None` değerlerini enterpole et.
    - `extract_jsonpath` - `StringChunked` üzerinde jsonpath sorguları çalıştır.
    - `list` - Liste yardımcıları:
        - `list_gather` - birden çok index ile alt liste al.
    - `rank` - Sıralama algoritmaları.
    - `moment` - Basıklık ve çarpıklık istatistikleri.
    - `ewma` - Üstel hareketli ortalama pencereleri.
    - `abs` - Series'in mutlak değerlerini al.
    - `arange` - Series üzerinde aralık işlemi.
    - `product` - Bir series'in çarpımını hesapla.
    - `diff` - `diff` işlemi.
    - `pct_change` - Değişim yüzdelerini hesapla.
    - `unique_counts` - Expression'larda benzersiz değerleri say.
    - `log` - Series için logaritmalar.
    - `list_to_struct` - `List` veri türünü `Struct`'a dönüştür.
    - `list_count` - Listelerdeki öğeleri say.
    - `list_eval` - Liste öğeleri üzerinde expression'lar uygula.
    - `cumulative_eval` - Kümülatif olarak artan pencereler üzerinde expression'lar uygula.
    - `arg_where` - Koşulun sağlandığı index'leri al.
    - `search_sorted` - Öğelerin sırayı korumak için eklenmesi gereken index'leri bul.
    - `offset_by` - Ayları ve artık yılları dikkate alan tarihlere ofset ekle.
    - `trigonometry` - Trigonometrik fonksiyonlar.
    - `sign` - Bir series'in öğe bazında işaretini hesapla.
    - `propagate_nans` - NaN yayan min/max toplamaları.
- DataFrame güzel yazdırma:
    - `fmt` - DataFrame biçimlendirmeyi etkinleştir.

---

1.  Yalnızca Windows'ta kullanıyorsanız gereklidir.
