AUTHOR = 'Halil'
SITELOGO = 'theme/img/avatar.png'
SITENAME = 'm.halil blogu'
SITETITLE = "Kişisel Bloğum"
SITESUBTITLE = '3D Dünyası ve Programlama'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'Flex-master'

HOME_HIDE_TAGS = False

MAIN_MENU = True
MENUITEMS = (	("Arşiv", "/archives.html"),
    		("Kategoriler", "/categories.html"),
    		("Etiketler", "/tags.html"),
    		)
PYGMENTS_STYLE = "monokai"
BROWSER_COLOR = "#0091d9"

THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE_DARK = 'monokai'
PYGMENTS_STYLE = "monokai"

# Blogroll
LINKS = (	('mhalil.github', 'https://github.com/mhalil'),
	 	)

# Social widget
SOCIAL = (('AcikKaynakci', 'https://twitter.com/AcikKaynakci'),
          ('ArtStation', 'https://www.artstation.com/mustafahalil'),
          ('GrabCAD', 'https://grabcad.com/mustafa.halil-1'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
