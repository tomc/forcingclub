#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Carmichael'
SITENAME = 'Forcing.&#x2663;'
SITEURL = ''
SITESUBTITLE = 'Exploring the game of bridge one hand at a time.'
FAVICON = 'images/clubonly-logo.png'
EMAIL = 'tomc74@gmail.com'

BACKDROP_IMAGE = '/images/image_maps__500_750_vertical_1fe6b8_115842_0.png'


PATH = 'content'
STATIC_PATHS = ('images', 'pdfs')

DEFAULT_CATEGORY = 'Misc'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
IMGLINKS = (('ACBL', '/images/acbl-logo-cropped.png','http://acbl.org/'),
         ('USBF', '/images/usbflogo2.png','http://usbf.org/'),
         ('WBF', '/images/wbf-logo.png','http://worldbridge.org/'),
		 ('Bridge Winners', '/images/bridgewinners-logo.png','https://bridgewinners.com'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/tomc74'),)
		  
PROFILE_IMAGE = '/images/acbl-small.jpg'
SITE_DESCRIPTION = '''
Welcome to Tom Carmichael's bridge website.
<br>&nbsp;</br>
Tom is an ACBL Grand Life Master, Bridge Teacher and Professional Player.
<br>&nbsp;</br>
His hobbies outside of bridge include tabletop games and computers.'''		  

DEFAULT_PAGINATION = 10
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True