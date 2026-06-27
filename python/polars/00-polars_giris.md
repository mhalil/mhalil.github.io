Title: Polars - 00 Giriş
Date: 2026-06-14 22:00
Category: Polars
Tags: Python, Polars, Kütüphane, Modül
Author: Mustafa Halil

# Polars Notları

![polars](../../images/python/polars/polars_github_logo.svg)

**Rust ve Python için Işık Hızında VeriÇerçevesi (DataFrame) Kütüphanesi.**

## Polars Nedir?

`Polars`, `Rust` programlama dilinde yazılmış ve temel olarak `Apache Arrow`’u kullanan bir **DataFrame kütüphanesidir**. Veri düzenleme alışkanlıklarını bilen `Polars`, okunabilir ve yüksek performanslı kod oluşturmanızı sağlayacak bir ifade dili kullanarak DataFrame'leri işlemek için tüm özellikleri içeren eksiksiz bir `Python API` 'ı sunar.

### Apache Arrow Nedir?

`Apache Arrow`, sütunlu verileri işleyen veri analitiği uygulamaları geliştirmek için dilden bağımsız bir yazılım çerçevesidir.

### Polars Kütüphanesini Ne Zaman Kullanmalıyız?

Verimiz `Pandas` için çok büyük, `Spark` için çok küçük olduğunda `Polars`  kütüphanesi iyi bir çözüm olacaktır.

## Polars - Python

Şahsen `Python` programlama diline aşina olduğum için,  `python` dilinde `polar` kütüphanesi kullanımına dair örnekler vereceğim.

![polars-pyton](../../images/python/polars/polars-logo-python.svg)

# Polars Öğrenme Yol Haritası

Bu bölüm, Polars kütüphanesinin resmi dokümantasyonunun [docs.pola.rs](https://docs.pola.rs/) Türkçe çevirisini içerir.
Her konu başlığı sıra numaralı olarak düzenlenmiştir.

---

## 1. Giriş (Foundation)

| Ders | Konu Başlığı |
|---|------|
| 01 | [Başlarken - Polars'a giriş ve temel örnek]({filename}01-baslarken.md) |
| 02 | [Kurulum - Polars'ı yükleme ve feature flag'ler]({filename}02-kurulum.md) |

## 2. Temel Kavramlar (Anlamadan ilerleme)

| Ders | Dosya | Konu |
|---|-------|------|
| 03 | `03-concepts.md` | Konseptler - Genel bakış |
| 04 | `04-data-types-and-structures.md` | Veri Tipleri ve Yapılar |
| 05 | `05-expressions-and-contexts.md` | Expression'lar ve Context'ler |
| 06 | `06-lazy-api.md` | Lazy API - Temel anlayış |
| 07 | `07-streaming.md` | Streaming (Akış) - Büyük veri işleme |

## 3. Expression'lar (En çok kullanacağınız şey)

| Ders | Dosya | Konu |
|---|-------|------|
| 08 | `08-expressions.md` | Expression'lar - Genel bakış |
| 09 | `09-basic-operations.md` | Temel İşlemler |
| 10 | `10-casting.md` | Tür Dönüşümleri (Casting) |
| 11 | `11-strings.md` | String İşlemleri |
| 12 | `12-lists-and-arrays.md` | Listeler ve Diziler |
| 13 | `13-categorical-data-and-enums.md` | Kategorik Veri ve Enum'lar |
| 14 | `14-structs.md` | Struct'lar |
| 15 | `15-missing-data.md` | Eksik Veri |
| 16 | `16-aggregation.md` | Toplama (Aggregation) |
| 17 | `17-window-functions.md` | Pencere Fonksiyonları |
| 18 | `18-folds.md` | Fold'lar (Katlamalar) |
| 19 | `19-expression-expansion.md` | Expression Genişletme |
| 20 | `20-user-defined-python-functions.md` | Kullanıcı Tanımlı Python Fonksiyonları |
| 21 | `21-numpy-functions.md` | NumPy Fonksiyonları |

## 4. Dönüşümler (Transformations)

| Ders | Dosya | Konu |
|---|-------|------|
| 22 | `22-transformations.md` | Dönüşümler - Genel bakış |
| 23 | `23-joins.md` | Birleştirmeler (Joins) |
| 24 | `24-concatenation.md` | Birleştirme (Concatenation) |
| 25 | `25-pivot.md` | Pivot Tablolar |
| 26 | `26-unpivot.md` | Unpivot (Pivot'tan Çevirme) |
| 27 | `27-time-series-parsing.md` | Zaman Serisi - Parse Etme |
| 28 | `28-time-series-filter.md` | Zaman Serisi - Filtreleme |
| 29 | `29-time-series-grouping.md` | Zaman Serisi - Gruplama (Rolling) |
| 30 | `30-time-series-resampling.md` | Zaman Serisi - Yeniden Örnekleme |
| 31 | `31-time-series-timezones.md` | Zaman Serisi - Zaman Dilimleri |

## 5. Lazy API (Performans)

| Ders | Dosya | Konu |
|---|-------|------|
| 32 | `32-lazy-overview.md` | Lazy API - Genel Bakış |
| 33 | `33-lazy-using.md` | Lazy API Kullanımı |
| 34 | `34-lazy-optimizations.md` | Optimizasyonlar |
| 35 | `35-lazy-schemas.md` | Şemalar |
| 36 | `36-lazy-datatype-exprs.md` | Veri Tipi Expression'ları |
| 37 | `37-lazy-query-plan.md` | Sorgu Planı |
| 38 | `38-lazy-execution.md` | Sorgu Yürütme |
| 39 | `39-lazy-sources-sinks.md` | Kaynaklar ve Hedefler |
| 40 | `40-lazy-multiplexing.md` | Sorgu Çoğullama |
| 41 | `41-lazy-gpu.md` | GPU Desteği |

## 6. IO (Veri Okuma/Yazma)

| Ders | Dosya | Konu |
|---|-------|------|
| 42 | `42-io-overview.md` | G/Ç (IO) - Genel Bakış |
| 43 | `43-io-csv.md` | CSV Okuma/Yazma |
| 44 | `44-io-parquet.md` | Parquet Okuma/Yazma |
| 45 | `45-io-json.md` | JSON Okuma/Yazma |
| 46 | `46-io-excel.md` | Excel Okuma/Yazma |
| 47 | `47-io-multiple.md` | Çoklu Dosya İşlemleri |
| 48 | `48-io-database.md` | Veritabanı Bağlantıları |
| 49 | `49-io-cloud-storage.md` | Bulut Depolama |
| 50 | `50-io-bigquery.md` | Google BigQuery |
| 51 | `51-io-hive.md` | Hive Desteği |
| 52 | `52-io-hugging-face.md` | Hugging Face |
| 53 | `53-io-sheets.md` | Google Sheets (Colab ile) |

## 7. SQL

| Ders | Dosya | Konu |
|---|-------|------|
| 54 | `54-sql-intro.md` | SQL - Giriş |
| 55 | `55-sql-show-tables.md` | SQL - SHOW TABLES |
| 56 | `56-sql-select.md` | SQL - SELECT |
| 57 | `57-sql-create.md` | SQL - CREATE |
| 58 | `58-sql-cte.md` | SQL - CTE (Common Table Expressions) |

## 8. İleri Düzey

| Ders | Dosya | Konu |
|---|-------|------|
| 59 | `59-plugins-overview.md` | Plugin'ler - Genel Bakış |
| 60 | `60-expr-plugins.md` | Expression Plugin'leri |
| 61 | `61-io-plugins.md` | IO Plugin'leri |
| 62 | `62-gpu-support.md` | GPU Desteği |

## 9. Geçiş Rehberleri

| Ders | Dosya | Konu |
|---|-------|------|
| 63 | `63-migration-pandas.md` | Pandas'tan Geçiş |
| 64 | `64-migration-spark.md` | Apache Spark'tan Geçiş |

## 10. Çeşitli (Misc)

| Ders | Dosya | Konu |
|---|-------|------|
| 65 | `65-ecosystem.md` | Ekosistem |
| 66 | `66-multiprocessing.md` | Çoklu İşlem (Multiprocessing) |
| 67 | `67-visualization.md` | Görselleştirme |
| 68 | `68-styling.md` | Stil Verme (Styling) |
| 69 | `69-comparison.md` | Diğer Araçlarla Karşılaştırma |
| 70 | `70-arrow.md` | Arrow Üretici/Tüketici |
| 71 | `71-polars-llms.md` | LLM'ler ile Polars Kodu Üretme |

---
# Kaynak:

* [Polars Kullanım Kılavuzu - Polars User Guide ](https://docs.pola.rs/)
