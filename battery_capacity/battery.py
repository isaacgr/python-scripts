#!/usr/bin/env python3
import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GObject
import time
from threading import Thread
import subprocess

class Indicator():
    def __init__(self):
        self.app = 'test123'
        self.indicator = AppIndicator3.Indicator.new(
            self.app,'battery.png',
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label(self.get_capacity(), self.app)
        # the thread:
        self.update = Thread(target=self.show_seconds)
        # daemonize the thread to make the indicator stopable
        self.update.setDaemon(True)
        self.update.start()

    def create_menu(self):
        menu = Gtk.Menu()
        # menu item 1
        item_1 = Gtk.MenuItem('Menu item')
        # item_about.connect('activate', self.about)
        menu.append(item_1)
        # separator
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)
        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def show_seconds(self):
        t = 2
        while True:
            time.sleep(1)
            mention = self.get_capacity()
            # apply the interface update using  GObject.idle_add()
            GObject.idle_add(
                self.indicator.set_label,
                mention, self.app,
                priority=GObject.PRIORITY_DEFAULT
                )
            t += 1

    def stop(self, source):
        Gtk.main_quit()

    def get_capacity(self):
        p = subprocess.Popen(['./myapp.sh'], stdout=subprocess.PIPE)
        output, error = p.communicate()
        if error or p.returncode != 0:
            print('Error with otuput. Is controller connected?')
            return "Not connected"
        print('Got battery capacity. %s' % output.rstrip('\n'))
        return str(output.rstrip("\n"))

Indicator()
# this is where we call GObject.threads_init()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
