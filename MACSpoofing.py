from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import logging
import time
import subprocess
import random

class macspoofing(plugins.Plugin):
    __author__ = 'Zarkstein'
    __version__ = '0.8'
    __license__ = 'GPL3'
    __description__ = 'Plugin for displaying and periodically changing the MAC address of wlan0 on the Pwnagotchi UI'

    def __init__(self):
        self.ready = False
        self.last_update_time = 0
        self.new_wlan_mac = ""

    def on_loaded(self):
        logging.debug("MAC Spoofing Plugin loaded.")

    def on_ready(self, agent):
        self._agent = agent
        logging.info("MAC Spoofing Plugin ready.")
        self.ready = True
        self.change_mac_address()

    def on_ui_setup(self, ui):
        ui.add_element('mac_display', LabeledValue(color=BLACK, label="", value='Initializing...',
                                                   position=(135, 95), label_font=fonts.Small, text_font=fonts.Small))

    def change_mac_address(self, interface="wlan0"):
        max_retries = 12
        retries = 0
        while retries < max_retries:
            try:
                new_mac = ":".join([random.choice("0123456789abcdef") + random.choice("0123456789abcdef") for _ in range(6)])
                command = f"ip link set dev {interface} address {new_mac}"
                subprocess.run(command, shell=True, check=True)
                logging.info(f"Changed MAC address of {interface} to {new_mac}")
                self.new_wlan_mac = new_mac
                return new_mac
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to change MAC address: {e}")
                retries += 1
                time.sleep(5)
            except Exception as e:
                logging.exception(repr(e))
                retries += 1
                time.sleep(5)
        logging.error("Failed to change MAC address after multiple retries.")
        return None

    def on_ui_update(self, ui):
        try:
            if time.time() - self.last_update_time >= 900:
                self.new_wlan_mac = self.change_mac_address()
                if self.new_wlan_mac:
                    ui.set('mac_display', f'MAC:{self.new_wlan_mac.upper()}')
                self.last_update_time = time.time()
        except Exception as e:
            logging.exception(repr(e))

    def on_unload(self, ui):
        self.ready = False
        ui.remove_element('mac_display')
        logging.info("MAC Spoofing Plugin unloaded.")

# Registering the plugin
plugins.register_plugin(macspoofing())

# Start UI Loop
plugins.loop()
