import os, sys, matplotlib
import mplfinance as mpf
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

class Handler():
    def __init__(self):
        global builder, conn, MD
        matplotlib.use('GTK3Agg')
        
    def b(self,id):
        return builder.get_object(id)
    def connect(self,button):
        pass
    def refresh(self,button):
        pass
    def create_orders(self, button):
        pass
    def higher(self, button):
        pass
    def lower(self, button):
        pass
    def close_application(self, event, data):
        # plt.close('all')
        print("Application closed successfully.")

class App(Gtk.Application):
    __gtype_name__ = 'DashBoard'

    def __init__(self):
        global builder
        
        Gtk.Application.__init__(self,application_id="in.otnemio.dashboard")
        self.connect("activate",self.on_activate)
        self.builder = Gtk.Builder()
        builder = self.builder
        self.builder.add_from_file("app.glade")
        self.builder.connect_signals(Handler())

    def on_activate(self, app):
        self.window = self.builder.get_object("appwindow1")
        self.window.maximize()
        self.window.set_application(app)
        self.apply_css()
        self.window.present()
    
    def apply_css(self):
        screen = Gdk.Screen.get_default()
        css_provider = Gtk.CssProvider()
        try:
            css_provider.load_from_path('main.css')
            context = Gtk.StyleContext()
            context.add_provider_for_screen(screen, css_provider,
                                            Gtk.STYLE_PROVIDER_PRIORITY_USER)
        except GLib.Error as e:
            print(f"Error in theme: {e} ")
    


def initialize():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    initialize()
    app = App()
    app.run(sys.argv)