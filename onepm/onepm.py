"""\
OnePM battery monitor and power manager.

@author: Aaron Mavrinac
@contact: mavrinac@gmail.com
@license: GPL-3
"""

import os
import gtk
from gobject import timeout_add
from sys import prefix


sharepath = os.path.join( prefix, "share/onepm" )
if not os.path.isdir( sharepath ):
    sharepath = "../data"


class OneBatteryStatusIcon( gtk.StatusIcon ):
    def __init__( self ):
        gtk.StatusIcon.__init__( self )
        self.file_acstate = "/proc/acpi/ac_adapter/ADP0/state"
        self.file_batstate = "/proc/acpi/battery/BAT0/state"
        self.file_batinfo = "/proc/acpi/battery/BAT0/info"
        self.set_from_file( os.path.join( sharepath, "icons", "battery-missing.png" ) )
        self.set_visible( True )
        self.update()
        # update every 20 seconds
        timeout_add( 20000, self.on_timeout )

    def update( self ):
        # set icon
        icon = "battery-"
        if self.battery_level == 100.0 and self.ac_adapter_online:
            icon += "charged"
        elif self.battery_level > 95.0:
            icon += "100"
        elif self.battery_level > 80.0:
            icon += "080"
        elif self.battery_level > 60.0:
            icon += "060"
        elif self.battery_level > 40.0:
            icon += "040"
        elif self.battery_level > 20.0:
            icon += "020"
        else:
            icon += "000"
        if self.battery_level < 100.0 and self.battery_charging:
            icon += "-charging"
        self.set_from_file( os.path.join( sharepath, "icons", icon + ".png" ) )
        # set tooltip
        tooltip = "Battery " + str( int( self.battery_level ) ) + "%"
        if self.battery_charging:
            tooltip += " (Charging)"
        elif self.ac_adapter_online:
            tooltip += " (AC)"
        self.set_tooltip( tooltip )

    def on_timeout( self, *args ):
        self.update()
        return True

    @property
    def ac_adapter_online( self ):
        if open( self.file_acstate ).readline().split()[ 1 ] == 'on-line':
            return True
        return False

    @property
    def battery_charging( self ):
        if open( self.file_batstate ).readlines()[ 2 ].split()[ 2 ] == 'charging':
            return True
        return False

    @property
    def battery_level( self ):
        return 100.0 * \
            float( open( self.file_batstate ).readlines()[ 4 ].split()[ 2 ] ) \
            / float( open( self.file_batinfo ).readlines()[ 2 ].split()[ 3 ] )


if __name__ == '__main__':
    battery_status = OneBatteryStatusIcon()
    gtk.main()
