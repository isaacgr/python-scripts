# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import network
gc.collect()

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('...')
        wlan.connect('Home Wireless', '5F954D3D')
        while not wlan.isconnected():
            pass
    print(wlan.ifconfig())
do_connect()
