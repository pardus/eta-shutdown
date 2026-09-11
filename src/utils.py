#!/usr/bin/env python3

import sys
import gi

gi.require_version('Gio', '2.0')
from gi.repository import GLib, Gio

def get_system_capabilities():
    try:
        proxy = Gio.DBusProxy.new_for_bus_sync(
            Gio.BusType.SYSTEM,
            Gio.DBusProxyFlags.NONE,
            None,
            "org.freedesktop.login1",
            "/org/freedesktop/login1",
            "org.freedesktop.login1.Manager",
            None
        )

        def check_cap(method):
            res = proxy.call_sync(method, None, Gio.DBusCallFlags.NONE, -1, None)
            return res[0] in ["yes", "challenge"]

    except:
        def check_cap(method):
            return None

    return {
        "CanPowerOff" : check_cap("CanPowerOff"),
        "CanReboot" :check_cap("CanReboot"),
        "CanSuspend" :check_cap("CanSuspend"),
        "CanHibernate" :check_cap("CanHibernate"),
        "CanHybridSleep" : check_cap("CanHybridSleep")
    }


if __name__ == "__main__":
    print(get_system_capabilities())
