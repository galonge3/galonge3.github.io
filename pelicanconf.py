#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gregory Alonge'
SITENAME = u'Greg Alonge'
SITEURL = 'https://galonge3.github.io/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

MAIN_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('About', '/pages/about.html'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-themes/cebong'

MARKUP = ('md')

SITELOGO = '/images/seattle.JPG'

STATIC_PATHS = ['images']

SOCIAL = []

LINKS = []

SUMMARY_MAX_LENGTH = 100
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
