"""\
OnePM battery monitor and power manager.

@author: Aaron Mavrinac
@contact: mavrinac@gmail.com
@license: GPL-3
"""

import os
import gtk
from sys import prefix

sharepath = os.path.join( prefix, "share/onepm" )
if not os.path.isdir( sharepath ):
    sharepath = "../data"

class OneBatteryStatusIcon( gtk.StatusIcon ):
    def __init__( self ):
        gtk.StatusIcon.__init__( self )
        self.set_tooltip( "Battery Monitor" )
        self.set_from_file( os.path.join( sharepath, "icons", "battery-missing.png" ) )
        self.set_visible( True )

if __name__ == '__main__':
    battery_status = OneBatteryStatusIcon()
    gtk.main()
