import os, sys, matplotlib
import mplfinance as mpf
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

class Handler():
    def __init__(self):
        global builder, conn, MD
        matplotlib.use('GTK3Agg')
        self.fetch_instruments()
        
    def b(self,id):
        return builder.get_object(id)
    def fetch_instruments(self):
        list1 = self.b('lstInstruments1')

        instruments = ['A','B']
        for instrument in instruments:
            button = Gtk.Button.new_with_label(instrument)
            button.connect("pressed",self.display_instrument)
            row = Gtk.ListBoxRow()
            row.add(button)
            list1.insert(row,-1)
        list1.show_all()
    def display_instrument(self,button):
        heading1 = self.b('lblHeading1')
        symbol = button.get_label()
        heading1.set_text(symbol)
        # self.display_historical_chart(symbol)
        # self.display_current_chart(symbol)
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