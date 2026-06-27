Title: Polars - 01 Başlarken
Date: 2026-06-14 22:10
Modified: 2026-06-27 22:27
Category: Polars
Tags: Python, Polars, Kütüphane, Modül, join, concat, select, with_columns, filter, group_by
Author: Mustafa Halil

# Başlarken

Bu bölüm, Polars ile başlamanıza yardımcı olmak için hazırlanmıştır. İlk kurulum ve yapılandırmadan temel işlevselliklere kadar kütüphanenin tüm temel özelliklerini kapsar. Eğer ileri düzey bir kullanıcıysanız veya dataframe'ler konusunda deneyimliyseniz, doğrudan [bir sonraki kurulum bölümüne]({filename}02-kurulum.md) geçebilirsiniz.

## Polars'ı Kurma

Python

```python
pip install polars
```

Rust

```rust
cargo add polars -F lazy  # veya Cargo.toml [dependencies] polars = { version = "x", features = ["lazy", ...]}
```

## Okuma & Yazma

Polars, yaygın dosya formatları (csv, json, parquet gibi), bulut depolama (S3, Azure Blob, BigQuery) ve veritabanları (postgres, mysql gibi) için okuma ve yazma desteği sunar. Aşağıda küçük bir dataframe oluşturuyor ve bunu diske yazıp geri okumayı gösteriyoruz.

Python

```python
import polars as pl
import datetime as dt

df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            dt.date(1997, 1, 10),
            dt.date(1985, 2, 15),
            dt.date(1983, 3, 22),
            dt.date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

print(df)
```

Rust

```rust
use chrono::prelude::*;
use polars::prelude::*;

let mut df: DataFrame = df!(
    "name" => ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
    "birthdate" => [
        NaiveDate::from_ymd_opt(1997, 1, 10).unwrap(),
        NaiveDate::from_ymd_opt(1985, 2, 15).unwrap(),
        NaiveDate::from_ymd_opt(1983, 3, 22).unwrap(),
        NaiveDate::from_ymd_opt(1981, 4, 30).unwrap(),
    ],
    "weight" => [57.9, 72.5, 53.6, 83.1],  // (kg)
    "height" => [1.56, 1.77, 1.65, 1.75],  // (m)
)
.unwrap();
println!("{df}");
```

Çıktı:

```
shape: (4, 4)
┌────────────────┬────────────┬────────┬────────┐
│ name           ┆ birthdate  ┆ weight ┆ height │
│ ---            ┆ ---        ┆ ---    ┆ ---    │
│ str            ┆ date       ┆ f64    ┆ f64    │
╞════════════════╪════════════╪════════╪════════╡
│ Alice Archer   ┆ 1997-01-10 ┆ 57.9   ┆ 1.56   │
│ Ben Brown      ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   │
│ Chloe Cooper   ┆ 1983-03-22 ┆ 53.6   ┆ 1.65   │
│ Daniel Donovan ┆ 1981-04-30 ┆ 83.1   ┆ 1.75   │
└────────────────┴────────────┴────────┴────────┘
```

Aşağıdaki örnekte dataframe'i `output.csv` adlı bir csv dosyasına yazıyoruz. Ardından `read_csv` ile geri okuyoruz ve sonucu incelemek için yazdırıyoruz.

Python

```python
df.write_csv("docs/assets/data/output.csv")
df_csv = pl.read_csv("docs/assets/data/output.csv", try_parse_dates=True)
print(df_csv)
```

Rust

```rust
use std::fs::File;

let mut file = File::create("docs/assets/data/output.csv").expect("could not create file");
CsvWriter::new(&mut file)
    .include_header(true)
    .with_separator(b',')
    .finish(&mut df)?;
let df_csv = CsvReadOptions::default()
    .with_has_header(true)
    .with_parse_options(CsvParseOptions::default().with_try_parse_dates(true))
    .try_into_reader_with_file_path(Some("docs/assets/data/output.csv".into()))?
    .finish()?;
println!("{df_csv}");
```

Çıktı:

```
shape: (4, 4)
┌────────────────┬────────────┬────────┬────────┐
│ name           ┆ birthdate  ┆ weight ┆ height │
│ ---            ┆ ---        ┆ ---    ┆ ---    │
│ str            ┆ date       ┆ f64    ┆ f64    │
╞════════════════╪════════════╪════════╪════════╡
│ Alice Archer   ┆ 1997-01-10 ┆ 57.9   ┆ 1.56   │
│ Ben Brown      ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   │
│ Chloe Cooper   ┆ 1983-03-22 ┆ 53.6   ┆ 1.65   │
│ Daniel Donovan ┆ 1981-04-30 ┆ 83.1   ┆ 1.75   │
└────────────────┴────────────┴────────┴────────┘
```

CSV dosya formatı ve diğer veri formatları hakkında daha fazla örnek için kılavuzun [IO bölümüne](https://docs.pola.rs/user-guide/io/) bakın.

## Expression'lar (İfadeler) ve Context'ler (Bağlamlar)

*Expression'lar* Polars'ın ana güçlü yönlerinden biridir çünkü veri dönüşümlerini ifade etmek için modüler ve esnek bir yol sağlarlar.

İşte bir Polars expression örneği:

```python
pl.col("weight") / (pl.col("height") ** 2)
```

Tahmin edebileceğiniz gibi, bu expression "weight" adlı sütunu alır ve değerlerini "height" sütunundaki değerlerin karesine bölerek bir kişinin Vücut Kütle Endeksini (BMI'ını) hesaplar. Yukarıdaki kodun soyut bir hesaplamayı ifade ettiğini unutmayın: expression ancak bir Polars *context*'i içinde sonuçları olan bir seri haline gelir.

Aşağıda farklı context'ler içinde Polars expression'larına örnekler göstereceğiz:

- `select`
- `with_columns`
- `filter`
- `group_by`

Expression'lar ve context'ler hakkında daha [detaylı bilgi için ilgili kılavuz bölümüne](https://docs.pola.rs/user-guide/concepts/expressions-and-contexts/) bakın.

### `select`

`select` context'i, bir dataframe'den sütunları seçmenize ve manipüle etmenize olanak tanır. En basit durumda, sağladığınız her expression sonuç dataframe'indeki bir sütuna karşılık gelir:

Python

```python
result = df.select(
    pl.col("name"),
    pl.col("birthdate").dt.year().alias("birth_year"),
    (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .select([
        col("name"),
        col("birthdate").dt().year().alias("birth_year"),
        (col("weight") / col("height").pow(2)).alias("bmi"),
    ])
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (4, 3)
┌────────────────┬────────────┬───────────┐
│ name           ┆ birth_year ┆ bmi       │
│ ---            ┆ ---        ┆ ---       │
│ str            ┆ i32        ┆ f64       │
╞════════════════╪════════════╪═══════════╡
│ Alice Archer   ┆ 1997       ┆ 23.791913 │
│ Ben Brown      ┆ 1985       ┆ 23.141498 │
│ Chloe Cooper   ┆ 1983       ┆ 19.687787 │
│ Daniel Donovan ┆ 1981       ┆ 27.134694 │
└────────────────┴────────────┴───────────┘
```

Polars ayrıca "expression expansion" (expression genişletme) adı verilen bir özelliği de destekler; bu özellikte tek bir expression birden çok expression için kısa yol görevi görür. Aşağıdaki örnekte, "weight" ve "height" sütunlarını tek bir expression ile manipüle etmek için expression expansion kullanıyoruz. Expression expansion kullanırken `.name.suffix` ile orijinal sütun adlarına bir sonek ekleyebilirsiniz:

Python

```python
result = df.select(
    pl.col("name"),
    (pl.col("weight", "height") * 0.95).round(2).name.suffix("-5%"),
)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .select([
        col("name"),
        (cols(["weight", "height"]).as_expr() * lit(0.95))
            .round(2, RoundMode::default())
            .name()
            .suffix("-5%"),
    ])
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (4, 3)
┌────────────────┬───────────┬───────────┐
│ name           ┆ weight-5% ┆ height-5% │
│ ---            ┆ ---       ┆ ---       │
│ str            ┆ f64       ┆ f64       │
╞════════════════╪═══════════╪═══════════╡
│ Alice Archer   ┆ 55.0      ┆ 1.48      │
│ Ben Brown      ┆ 68.88     ┆ 1.68      │
│ Chloe Cooper   ┆ 50.92     ┆ 1.57      │
│ Daniel Donovan ┆ 78.94     ┆ 1.66      │
└────────────────┴───────────┴───────────┘
```

[Temel işlemler](https://docs.pola.rs/user-guide/expressions/basic-operations/) veya [expression expansion'da sütun seçimleri](https://docs.pola.rs/user-guide/expressions/expression-expansion/) hakkında daha fazla bilgi için kılavuzun diğer bölümlerine göz atabilirsiniz.

### `with_columns`

`with_columns` context'i `select` context'ine çok benzer ancak `with_columns` **sütunları seçmek yerine dataframe'e ekler**. Sonuçta oluşan dataframe'in orijinal dataframe'in dört sütununa ek olarak `with_columns` içindeki expression'lar tarafından eklenen iki yeni sütunu içerdiğine dikkat edin:

Python

```python
result = df.with_columns(
    birth_year=pl.col("birthdate").dt.year(),
    bmi=pl.col("weight") / (pl.col("height") ** 2),
)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .with_columns([
        col("birthdate").dt().year().alias("birth_year"),
        (col("weight") / col("height").pow(2)).alias("bmi"),
    ])
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (4, 6)
┌────────────────┬────────────┬────────┬────────┬────────────┬───────────┐
│ name           ┆ birthdate  ┆ weight ┆ height ┆ birth_year ┆ bmi       │
│ ---            ┆ ---        ┆ ---    ┆ ---    ┆ ---        ┆ ---       │
│ str            ┆ date       ┆ f64    ┆ f64    ┆ i32        ┆ f64       │
╞════════════════╪════════════╪════════╪════════╪════════════╪═══════════╡
│ Alice Archer   ┆ 1997-01-10 ┆ 57.9   ┆ 1.56   ┆ 1997       ┆ 23.791913 │
│ Ben Brown      ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   ┆ 1985       ┆ 23.141498 │
│ Chloe Cooper   ┆ 1983-03-22 ┆ 53.6   ┆ 1.65   ┆ 1983       ┆ 19.687787 │
│ Daniel Donovan ┆ 1981-04-30 ┆ 83.1   ┆ 1.75   ┆ 1981       ┆ 27.134694 │
└────────────────┴────────────┴────────┴────────┴────────────┴───────────┘
```

Yukarıdaki örnekte ayrıca yeni sütunların adlarını belirtmek için `alias` yöntemi yerine adlandırılmış expression'lar kullanmayı tercih ettik. `select` ve `group_by` gibi diğer context'ler de adlandırılmış expression'ları kabul eder.

### `filter`

`filter` context'i, orijinal dataframe'in satırlarının bir alt kümesiyle ikinci bir dataframe oluşturmamızı sağlar:

Python

```python
result = df.filter(pl.col("birthdate").dt.year() < 1990)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .filter(col("birthdate").dt().year().lt(lit(1990)))
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (3, 4)
┌────────────────┬────────────┬────────┬────────┐
│ name           ┆ birthdate  ┆ weight ┆ height │
│ ---            ┆ ---        ┆ ---    ┆ ---    │
│ str            ┆ date       ┆ f64    ┆ f64    │
╞════════════════╪════════════╪════════╪════════╡
│ Ben Brown      ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   │
│ Chloe Cooper   ┆ 1983-03-22 ┆ 53.6   ┆ 1.65   │
│ Daniel Donovan ┆ 1981-04-30 ┆ 83.1   ┆ 1.75   │
└────────────────┴────────────┴────────┴────────┘
```

Ayrıca birden çok koşul ifadesini ayrı parametreler olarak sağlayabilirsiniz; bu, hepsini `&` ile birleştirmekten daha kullanışlıdır:

Python

```python
result = df.filter(
    pl.col("birthdate").is_between(dt.date(1982, 12, 31), dt.date(1996, 1, 1)),
    pl.col("height") > 1.7,
)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .filter(
        col("birthdate")
            .is_between(
                lit(NaiveDate::from_ymd_opt(1982, 12, 31).unwrap()),
                lit(NaiveDate::from_ymd_opt(1996, 1, 1).unwrap()),
                ClosedInterval::Both,
            )
            .and(col("height").gt(lit(1.7))),
    )
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (1, 4)
┌───────────┬────────────┬────────┬────────┐
│ name      ┆ birthdate  ┆ weight ┆ height │
│ ---       ┆ ---        ┆ ---    ┆ ---    │
│ str       ┆ date       ┆ f64    ┆ f64    │
╞═══════════╪════════════╪════════╪════════╡
│ Ben Brown ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   │
└───────────┴────────────┴────────┴────────┘
```

### `group_by`

`group_by` context'i, bir veya daha fazla expression boyunca aynı değeri paylaşaorijinal dataframe'de göründükleri sırayla sunmaya zorlar.orijinal dataframe'de göründükleri sırayla sunmaya zorlar.n dataframe satırlarını bir araya getirmek için kullanılabilir. Aşağıdaki örnek, her on yılda kaç kişinin doğduğunu sayar:

Python

```python
result = df.group_by(
    (pl.col("birthdate").dt.year() // 10 * 10).alias("decade"),
    maintain_order=True,
).len()
print(result)
```

Rust

```rust
// Python'daki `maintain_order=True` davranışını istiyorsanız `group_by_stable` kullanın.
let result = df
    .clone()
    .lazy()
    .group_by([(col("birthdate").dt().year() / lit(10) * lit(10)).alias("decade")])
    .agg([len()])
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (2, 2)
┌────────┬─────┐
│ decade ┆ len │
│ ---    ┆ --- │
│ i32    ┆ u32 │
╞════════╪═════╡
│ 1990   ┆ 1   │
│ 1980   ┆ 3   │
└────────┴─────┘
```

`maintain_order` anahtar kelime argümanı, Polars'ı sonuç gruplarını **orijinal dataframe'de göründükleri sırayla sunmaya zorlar.** Bu, gruplama işlemini yavaşlatır ancak örneklerin tekrarlanabilirliğini sağlamak için burada kullanılmıştır.

`group_by` context'ini kullandıktan sonra `agg` ile sonuç grupları üzerinde toplama işlemleri yapabiliriz:

Python

```python
result = df.group_by(
    (pl.col("birthdate").dt.year() // 10 * 10).alias("decade"),
    maintain_order=True,
).agg(
    pl.len().alias("sample_size"),
    pl.col("weight").mean().round(2).alias("avg_weight"),
    pl.col("height").max().alias("tallest"),
)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .group_by([(col("birthdate").dt().year() / lit(10) * lit(10)).alias("decade")])
    .agg([
        len().alias("sample_size"),
        col("weight")
            .mean()
            .round(2, RoundMode::default())
            .alias("avg_weight"),
        col("height").max().alias("tallest"),
    ])
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (2, 4)
┌────────┬─────────────┬────────────┬─────────┐
│ decade ┆ sample_size ┆ avg_weight ┆ tallest │
│ ---    ┆ ---         ┆ ---        ┆ ---     │
│ i32    ┆ u32         ┆ f64        ┆ f64     │
╞════════╪═════════════╪════════════╪═════════╡
│ 1990   ┆ 1           ┆ 57.9       ┆ 1.56    │
│ 1980   ┆ 3           ┆ 69.73      ┆ 1.77    │
└────────┴─────────────┴────────────┴─────────┘
```

### Daha Karmaşık Sorgular

Context'ler ve içlerindeki expression'lar, ihtiyaçlarınıza göre daha karmaşık sorgular oluşturmak için zincirlenebilir. Aşağıdaki örnekte, şimdiye kadar gördüğümüz context'lerin bazılarını birleştirerek daha karmaşık bir sorgu oluşturuyoruz:

Python

```python
result = (
    df.with_columns(
        (pl.col("birthdate").dt.year() // 10 * 10).alias("decade"),
        pl.col("name").str.split(by=" ").list.first(),
    )
    .select(
        pl.all().exclude("birthdate"),
    )
    .group_by(
        pl.col("decade"),
        maintain_order=True,
    )
    .agg(
        pl.col("name"),
        pl.col("weight", "height").mean().round(2).name.prefix("avg_"),
    )
)
print(result)
```

Rust

```rust
let result = df
    .clone()
    .lazy()
    .with_columns([
        (col("birthdate").dt().year() / lit(10) * lit(10)).alias("decade"),
        col("name").str().split(lit(" ")).list().first(),
    ])
    .select([all().exclude_cols(["birthdate"]).as_expr()])
    .group_by([col("decade")])
    .agg([
        col("name"),
        cols(["weight", "height"])
            .as_expr()
            .mean()
            .round(2, RoundMode::default())
            .name()
            .prefix("avg_"),
    ])
    .collect()?;
println!("{result}");
```

Çıktı:

```
shape: (2, 4)
┌────────┬────────────────────────────┬────────────┬────────────┐
│ decade ┆ name                       ┆ avg_weight ┆ avg_height │
│ ---    ┆ ---                        ┆ ---        ┆ ---        │
│ i32    ┆ list[str]                  ┆ f64        ┆ f64        │
╞════════╪════════════════════════════╪════════════╪════════════╡
│ 1990   ┆ ["Alice"]                  ┆ 57.9       ┆ 1.56       │
│ 1980   ┆ ["Ben", "Chloe", "Daniel"] ┆ 69.73      ┆ 1.72       │
└────────┴────────────────────────────┴────────────┴────────────┘
```

## Dataframe'leri Birleştirme

Polars, iki dataframe'i birleştirmek için çeşitli araçlar sağlar. Bu bölümde, bir `join` ve bir `concat` (birleştirme) örneği gösteriyoruz.

### Dataframe'lerde `Join` (Birleştirme)

Polars birçok farklı `join` algoritması sunar. Aşağıdaki örnek, bir sütunun dataframe'ler arasındaki satırlar arasında bir karşılık kurmak için benzersiz bir tanımlayıcı olarak kullanılabildiği durumda iki dataframe'i birleştirmek için `left outer join`'in nasıl kullanılacağını gösterir:

Python

```python
df2 = pl.DataFrame(
    {
        "name": ["Ben Brown", "Daniel Donovan", "Alice Archer", "Chloe Cooper"],
        "parent": [True, False, False, False],
        "siblings": [1, 2, 3, 4],
    }
)

print(df.join(df2, on="name", how="left"))
```

Rust

```rust
let df2: DataFrame = df!(
    "name" => ["Ben Brown", "Daniel Donovan", "Alice Archer", "Chloe Cooper"],
    "parent" => [true, false, false, false],
    "siblings" => [1, 2, 3, 4],
)
.unwrap();

let result = df
    .clone()
    .lazy()
    .join(
        df2.lazy(),
        [col("name")],
        [col("name")],
        JoinArgs::new(JoinType::Left),
    )
    .collect()?;

println!("{result}");
```

Çıktı:

```
shape: (4, 6)
┌────────────────┬────────────┬────────┬────────┬────────┬──────────┐
│ name           ┆ birthdate  ┆ weight ┆ height ┆ parent ┆ siblings │
│ ---            ┆ ---        ┆ ---    ┆ ---    ┆ ---    ┆ ---      │
│ str            ┆ date       ┆ f64    ┆ f64    ┆ bool   ┆ i64      │
╞════════════════╪════════════╪════════╪════════╪════════╪══════════╡
│ Alice Archer   ┆ 1997-01-10 ┆ 57.9   ┆ 1.56   ┆ false  ┆ 3        │
│ Ben Brown      ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   ┆ true   ┆ 1        │
│ Chloe Cooper   ┆ 1983-03-22 ┆ 53.6   ┆ 1.65   ┆ false  ┆ 4        │
│ Daniel Donovan ┆ 1981-04-30 ┆ 83.1   ┆ 1.75   ┆ false  ┆ 2        │
└────────────────┴────────────┴────────┴────────┴────────┴──────────┘
```

Polars, kılavuzun [joins bölümünde](https://docs.pola.rs/user-guide/transformations/joins/) öğrenebileceğiniz birçok farklı join algoritması sağlar.

### Dataframe'lerde `Concat` (Birleştirme)

Dataframe'leri birleştirmek (concatenate), kullanılan yönteme bağlı olarak daha uzun veya daha geniş bir dataframe oluşturur. Diğer kişilerden veri içeren ikinci bir dataframe'imiz olduğunu varsayarsak, daha uzun bir dataframe oluşturmak için dikey birleştirme kullanabiliriz:

Python

```python
df3 = pl.DataFrame(
    {
        "name": ["Ethan Edwards", "Fiona Foster", "Grace Gibson", "Henry Harris"],
        "birthdate": [
            dt.date(1977, 5, 10),
            dt.date(1975, 6, 23),
            dt.date(1973, 7, 22),
            dt.date(1971, 8, 3),
        ],
        "weight": [67.9, 72.5, 57.6, 93.1],  # (kg)
        "height": [1.76, 1.6, 1.66, 1.8],  # (m)
    }
)

print(pl.concat([df, df3], how="vertical"))
```

Rust

```rust
let df3: DataFrame = df!(
    "name" => ["Ethan Edwards", "Fiona Foster", "Grace Gibson", "Henry Harris"],
    "birthdate" => [
        NaiveDate::from_ymd_opt(1977, 5, 10).unwrap(),
        NaiveDate::from_ymd_opt(1975, 6, 23).unwrap(),
        NaiveDate::from_ymd_opt(1973, 7, 22).unwrap(),
        NaiveDate::from_ymd_opt(1971, 8, 3).unwrap(),
    ],
    "weight" => [67.9, 72.5, 57.6, 93.1],  // (kg)
    "height" => [1.76, 1.6, 1.66, 1.8],  // (m)
)
.unwrap();

let result = concat([df.clone().lazy(), df3.lazy()], UnionArgs::default())?.collect()?;
println!("{result}");
```

Çıktı:

```
shape: (8, 4)
┌────────────────┬────────────┬────────┬────────┐
│ name           ┆ birthdate  ┆ weight ┆ height │
│ ---            ┆ ---        ┆ ---    ┆ ---    │
│ str            ┆ date       ┆ f64    ┆ f64    │
╞════════════════╪════════════╪════════╪════════╡
│ Alice Archer   ┆ 1997-01-10 ┆ 57.9   ┆ 1.56   │
│ Ben Brown      ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   │
│ Chloe Cooper   ┆ 1983-03-22 ┆ 53.6   ┆ 1.65   │
│ Daniel Donovan ┆ 1981-04-30 ┆ 83.1   ┆ 1.75   │
│ Ethan Edwards  ┆ 1977-05-10 ┆ 67.9   ┆ 1.76   │
│ Fiona Foster   ┆ 1975-06-23 ┆ 72.5   ┆ 1.6    │
│ Grace Gibson   ┆ 1973-07-22 ┆ 57.6   ┆ 1.66   │
│ Henry Harris   ┆ 1971-08-03 ┆ 93.1   ┆ 1.8    │
└────────────────┴────────────┴────────┴────────┘
```

Polars, dikey ve yatay birleştirmenin yanı sıra çapraz birleştirme de sağlar. Bunlar hakkında daha fazla bilgiyi kılavuzun [concatenations bölümünde](https://docs.pola.rs/user-guide/transformations/concatenation/) bulabilirsiniz.
