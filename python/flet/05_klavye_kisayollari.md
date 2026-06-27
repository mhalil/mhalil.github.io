Title: Flet 05 - Klavye Kısayolları
Date: 2024-02-11 16:05
Category: Flet
Tags: Python, Flet, Kütüphane, Modül, GUI, Arabirim, Klavye, Kısayol, Shortcut
Author: Mustafa Halil

# Klavye Kısayolları

Sağlam bir klavye desteği, web'inizi ve özellikle masaüstü uygulamanızı kullanırken kullanıcı üretkenliği için bir anahtardır. Gerçekten de, sürekli olarak fare ve klavye arasında geçiş yapmak gerçekten can sıkıcı olabilir.

Form kontrollerinin `.autofocus` özelliğine ve [TextField.focus()](https://flet.dev/docs/controls/textfield#focus) metoduna ek olarak Flet, "**global**" klavye olaylarının işlenmesine olanak tanır.

Tüm  tuş vuruşlarını (basılan tuşları) yakalamak için `page.on_keyboard_event` işleyicisini uygulayın. Olay işleyici parametresi `e`, aşağıdaki özelliklere sahip bir `KeyboardEvent` sınıfı örneğidir:

* `key` - basılan bir tuşun metinsel gösterimi, örn. `A`, `Enter` veya `F5`.

* `shift` - `True` ise "**Shift**" tuşuna basılır.

* `ctrl` - `True` ise "**Ctrl**" tuşuna basılır.

* `alt` - `True` ise "**Alt (Option)**" tuşuna basılır.

* `meta` - `True` ise "**Command**" tuşuna basılır.

Basit bir kullanım örneği görelim:

```python
import flet as ft

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )

ft.app(target=main)
```

![keyboard-shortcuts](https://flet.dev/img/docs/getting-started/keyboard-shortcuts.png)

Burada [daha gelişmiş bir örnek](https://github.com/flet-dev/examples/blob/main/python/controls/page/keyboard-events.py) mevcut.

| Önceki Bölüm                                                      | Sonraki Bölüm                                 |
| ----------------------------------------------------------------- | --------------------------------------------- |
| [<<< 04 Kullanicidan Girdi Almak](flet-04-kullanicidan-girdi-almak.html) | [06 Büyük Listeler >>>](flet-06-buyuk-listeler.html) |
