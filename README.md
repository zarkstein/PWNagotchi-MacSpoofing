*****
PWNagotchi MAC Spoofing by Zarkstein
*****

The MAC address is a unique identifier assigned to a device's network card and is used to uniquely identify that device on a network.

"MAC spoofing" is a technique used to change a device's Media Access Control (MAC) address to make it appear to be another device.

When MAC spoofing is performed, an attacker can change their device's MAC address to match the MAC address of another device.

MAC spoofing can also be used to perform "man-in-the-middle" attacks, where the attacker intercepts and modifies traffic between two devices on the network.

If the MAC matches an authorized device on the network, it may allow the attacker to bypass MAC address-based security restrictions, such as access filters, and gain unauthorized access to the network.

In any case, obfuscating our device's true MAC address will always provide greater security.

PWNagotchi MacSpoofing is loaded when PWNagotchi starts up and replaces our device's original MAC with a new random MAC that changes every 15 minutes.

The newly assigned MAC is displayed in the bottom right corner of the screen and/or the user interface.


*****
Install
*****

Copy the MACSpoofing.py file to the "/etc/pwnagotchi/custom-plugins/" directory on your PWNagotchi.

Modify the "/etc/pwnagotchi/config.toml" file and make sure you have the following line:

main.custom_plugins = "/etc/pwnagotchi/custom-plugins/"

Add the following line:

main.plugins.MACSpoofing.enabled = true

Restart the PWNagotchi.


*****
Configuration
*****

By default, the plugin is configured to change the MAC address every 15 minutes (900 seconds).

You can adjust this value by modifying the plugin's code in the macspoofing.py file.


*****
How PWNagotchi MACSpoofing Works
*****

*****
Plugin Startup and Loading:
*****

When Pwnagotchi starts up, the "MAC Spoofing" plugin is automatically loaded if it is installed and enabled.

During loading, the initial state of the plugin is set up and configured to be ready for use.


*****
MAC Address Change:
*****

The plugin generates a new random MAC address for the wlan0 (WiFi) interface.

It uses the Linux ip link set command to change the MAC address of the wlan0 interface to the newly generated address.

If the MAC address change fails, the plugin makes several attempts (defined by max_retries) with waiting intervals (defined by time.sleep) before logging an error.

*****
User Interface:
*****

The plugin displays the updated MAC address in the Pwnagotchi's user interface.

It uses the LabeledValue component from the Pwnagotchi's user interface library to display the MAC address on the screen.


*****
Periodic Update:
*****

The plugin periodically updates the displayed MAC address in the user interface.

When the specified time interval elapses, the plugin generates a new MAC address and updates the user interface.

*****
Plugin Unload:
*****

When the plugin is unloaded or disabled, it removes the user interface element related to the MAC address.

This helps clean up the user interface and free up resources when the plugin is no longer in use.

*****
More Info
*****

Author information:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/

Latest plugin version available for download at:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/releases

*****
Contributions
*****

Contributions are welcome! If you have ideas for improvements, issues, or fixes, please open an issue or submit a pull request.

*****
License
*****

This plugin is released under the GPL-3.0 license. For more details, please see the LICENSE file.

*****
