*****
PWNagotchi MAC Spoofing v.0.1 by Zarkstein
*****

"MAC spoofing" is a technique used to change the MAC (Media Access Control) address of a network device to make it appear as another.

The MAC address is a unique identifier assigned to a device's network card, and it is used to uniquely identify that device on a network.

When MAC spoofing is performed, an attacker can change the MAC address of their device to match the MAC address of another device.

If the MAC matches an authorized device on the network, it can allow the attacker to bypass MAC address-based security restrictions, such as access filters, and gain unauthorized access to the network.

MAC spoofing can also be used to perform "man-in-the-middle" attacks, where the attacker intercepts and modifies traffic between two devices on the network.

In any case, even if the MAC does not match an authorized device on the network, it still allows us to hide the real MAC of our device.

PWNagotchi MacSpoofing v.0.1 is loaded when PWNagotchi starts up and replaces the original MAC of our device, assigning it a new random MAC that changes every 60 seconds.

The newly assigned MAC is displayed in the bottom right corner of the display.

*****
Install
*****


Copy the file MACSpoofing.py into the directory "/etc/pwnagotchi/custom-plugins/" on your PWNagotchi.

Modify the file "/etc/pwnagotchi/config.toml" and ensure that you have the following line:

main.custom_plugins = "/etc/pwnagotchi/custom-plugins/"

Add the following line:
main.plugins.MACSpoofing.enabled = true

Restart the PWNagotchi.


*****
More Info: 
https://github.com/zarkstein/PWNagotchi-MacSpoofing-v.0.1/
*****
