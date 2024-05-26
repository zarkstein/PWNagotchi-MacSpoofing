## PWNagotchi MacSpoofing Plugin INFO

## What is a MAC address

The MAC address is a unique identifier assigned to the network card of a device connected to a network.

For example, a typical MAC address would look like this: AB:CD:EF:12:34:56.

In this MAC address we can find two parts:

# OUI (Organizationally Unique Identifier):
The first three pairs of characters in a MAC address represent the OUI, which identifies the manufacturer of the network device.
The Institute of Electrical and Electronics Engineers (IEEE) assigns OUIs to manufacturers and ensures that they are unique.
Manufacturers can request an OUI from the IEEE and then use it in their devices.

# Device identifier (ID):
The last three pairs of characters in a MAC address represent the unique identifier of the device on the network.
This identifier is assigned by the device manufacturer for each model of one of its products.

Therefore, a MAC address provides a unique way to identify both the device manufacturer and the specific device on a network.
This unique identification is essential for network operation and management, allowing devices to communicate with each other efficiently and securely.


## What is MAC Spoofing

"MAC spoofing" is a technique used to change the MAC address of a network device to make it appear to be another device.

MAC spoofing on a Pwnagotchi can provide several advantages:

# Anonymity and privacy:
By periodically changing the Pwnagotchi's MAC address, you make it difficult for other devices or networks to track or identify the Pwnagotchi consistently.
This can help preserve user anonymity and privacy during penetration testing or network audits.

# Bypass MAC based security restrictions:
By changing the MAC address, the Pwnagotchi can bypass security restrictions that are based on the MAC address of the devices. For example, if a Wi-Fi network only allows access to devices with specific MAC addresses, MAC spoofing can allow Pwnagotchi to access the network without needing to know the authorized MAC addresses.

# Device identity obfuscation:
MAC spoofing can cause the Pwnagotchi to appear as another type of device on the network, which can make it difficult for other users or network administrators to identify the device.
This can be useful for performing penetration tests more stealthily or to avoid detection by network security measures.

# Identity diversification:
By periodically changing the MAC address, the Pwnagotchi can present itself as multiple distinct devices on the network.
This can be useful for simulating multiple users or devices in a network audit, allowing different behaviors or vulnerabilities to be detected and analyzed.

In summary, MAC spoofing on a Pwnagotchi can provide anonymity, security restriction bypass, identity obfuscation, and identity diversification, which can be beneficial for performing penetration testing, network audits, and other cybersecurity-related activities.


## PWNagotchi MacSpoofing Plugin

PWNagotchi MacSpoofing Plugin is an extension for PWNagotchi, a Raspberry Pi-based Wi-Fi network pentesting device.
https://pwnagotchi.ai/

This plugin automatically changes the MAC address of the wlan0 interface of our Pwnagotchi and displays it on the screen (or not) according to your specific needs.

## Requirements

- PWNagotchi installed and configured.
- Internet connection to download and update the plugin.


## Installing PWNagotchi MacSpoofing Plugin

1. Download the MACSpoofing.py file from this repository:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/

2. Copy the MACSpoofing.py file to your "/etc/pwnagotchi/custom-plugins/" directory on your microSD card.

3. Modify your /etc/pwnagotchi/config.toml file and add the following line:

main.plugins.macspoofing.enabled = true

NOTE: You can also activate it from the Plugins section of the web control panel.

4. Restart your PWNagotchi.


## Features of PWNagotchi MacSpoofing Plugin

The plugin will start working when you start your PWNagotchi and then perform the following functions:

- Automatic change of MAC address of the PWNagotchi
- MAC address customization using a Cisco specific OUI
- Show the new MAC on screen
- Periodic update of the MAC address every 15 minutes
- Writing the log with information about the new assigned MAC address


*****
Use and Configuration
*****

## Customizable variables

You can customize how the plugin works in the MACSpoofing.py code to suit your specific needs:

update_interval:This variable determines how often the MAC address is changed.
  You can adjust the value in seconds to change the MAC address more or less frequently.
  For example, if you want to change the MAC address every 10 minutes, you can set update_interval = 600.

mac_on_display: This variable controls whether or not the new MAC address is displayed in the user interface.
  If you set mac_on_display = True (the new MAC address will be displayed on the screen).
  If you set mac_on_display = False (MAC address will not be displayed on the screen).
  In both cases the new MAC address will be saved in the log.

oui: This variable represents the Organizational Unique Identifier (OUI) that is used as a prefix to generate the MAC address.
  You can change this value to use a different OUI to customize the appearance of the generated MAC address.
  If you want the MAC address to appear to belong to a specific company you can change the OUI to one of the following:

Cisco Systems, Inc.: 00:01:42
Apple, Inc.: 00:11:24
Intel Corporation: 00:00:86
Samsung Electronics Co., Ltd.: 00:16:32
Microsoft Corporation: 00:0F:FB
Huawei Technologies Co., Ltd.: 00:E0:FC
Dell Inc.: 00:14:22
Hewlett Packard Enterprise: 00:50:56
Sony Corporation: 00:0A:89
Google LLC: 00:1A:11

Below is an example of how you can customize these variables in the MACSpoofing.py code:

def __init__(self):
 self.mac_on_display = True # Show the new MAC in the UI
 self.update_interval = 600 # Change MAC address every 10 minutes
 self.oui = "00:11:24" # OUI to modify the Raspberry manufacturer ID to identify it as an Apple product.


*****
More information
*****

Information about the author:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/

Latest version of the plugin available for download at:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/releases

*****
Contributions
*****

Contributions are welcome! If you have ideas for improvements, issues or fixes, please open an issue or submit a pull request.
