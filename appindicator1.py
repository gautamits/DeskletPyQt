

import os
import signal
import json
from subprocess import call
from urllib2 import Request, urlopen, URLError
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7') 

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify



APPINDICATOR_ID = 'myappindicator'
def search(_):
	call(["python","search.py"])
def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('icon.jpg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_joke = gtk.MenuItem('Joke')
    item_joke.connect('activate', joke)
    menu.append(item_joke)

    item_search = gtk.MenuItem('Search')
    item_search.connect('activate', search)
    #item_search.connect(search)
    menu.append(item_search)

    item_preferences = gtk.MenuItem('Preferences')
    item_preferences.connect('activate', preferences)
    menu.append(item_preferences)

    item_database = gtk.MenuItem('Update Database')
    item_database.connect('activate', database)
    menu.append(item_database)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    


    menu.show_all()
    return menu

def fetch_joke():
    request = Request('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
    response = urlopen(request)
    joke = json.loads(response.read())['value']['joke']
    return joke

def joke(_):
    notify.Notification.new("<b>Joke</b>", fetch_joke(), None).show()
def preferences(_):
	call(["python","preferences.py"])
def  database(_):
	call(["python","database.py"])

def quit(_):
    notify.uninit()
    gtk.main_quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
