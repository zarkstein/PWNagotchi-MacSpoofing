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
    __version__ = '1.1'
    __license__ = 'GPL3'
    __description__ = 'Plugin for changing the MAC address periodically of wlan0 and displaying ( or not ) on the Pwnagotchi UI'

    def __init__(self):
        self.new_wlan_mac = ""
        self.mac_on_display = True  # Variable to control whether the new MAC is displayed on the screen
        self.ready = False
        self.last_update_time = 0
        self.update_interval = 900  # 900 seconds = 15 minutes
        self.oui = "00:1A:2B"  # OUI to modify the Raspberry manufacturer ID to identify it as a Cisco product.

    def on_loaded(self):
        logging.debug("MAC Spoofing Plugin loaded.")

    def on_ready(self, agent):
        self._agent = agent
        logging.info("MAC Spoofing Plugin ready.")
        self.ready = True
        self.change_mac_address()

    def on_ui_setup(self, ui):
        ui.add_element('mac_display', LabeledValue(color=BLACK, label="", value='   Initializing...',
                                                   position=(130, 95), label_font=fonts.Small, text_font=fonts.Small))

    def change_mac_address(self, interface="wlan0"):
        max_retries = 12
        retries = 0
        while retries < max_retries:
            try:
                new_mac = self.oui + ":" + ":".join([f"{random.randint(0, 255):02x}" for _ in range(3)])
                command = f"ip link set dev {interface} address {new_mac}"
                subprocess.run(command, shell=True, check=True)
                logging.info(f"Changed MAC address of {interface} to {new_mac}")
                self.new_wlan_mac = new_mac
                return new_mac
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to change MAC address:{e}")
                retries += 1
                time.sleep(10)
            except Exception as e:
                logging.exception(repr(e))
                retries += 1
                time.sleep(10)
        logging.error("Failed to change MAC address after multiple retries.")
        return None

    def on_ui_update(self, ui):
        try:
            if time.time() - self.last_update_time >= self.update_interval:
                self.new_wlan_mac = self.change_mac_address()
                if self.new_wlan_mac and self.mac_on_display:  # Show the new MAC only if mac_on_display isTrue
                    ui.set('mac_display', f'MAC:{self.new_wlan_mac.upper()}')
                else:
                    ui.set('mac_display', '')  # Do not show text on the screen
                self.last_update_time = time.time()
        except Exception as e:
            logging.exception(repr(e))

    def on_unload(self, ui):
        self.ready = False
        ui.remove_element('mac_display')
        logging.info("MAC Spoofing Plugin unloaded.")

# Register the plugin
plugins.register(macspoofing())
