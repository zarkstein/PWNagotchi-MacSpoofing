
===================================================================
PWNagotchi MAC Spoofing v.0.1 por Zarkstein
===================================================================
ENGLISH:
===================================================================

"MAC spoofing" is a technique used to change the MAC (Media Access Control) address of a network device to make it appear as another.

The MAC address is a unique identifier assigned to a device's network card, and it is used to uniquely identify that device on a network.

When MAC spoofing is performed, an attacker can change the MAC address of their device to match the MAC address of another device.

If the MAC matches an authorized device on the network, it can allow the attacker to bypass MAC address-based security restrictions, such as access filters, and gain unauthorized access to the network.

MAC spoofing can also be used to perform "man-in-the-middle" attacks, where the attacker intercepts and modifies traffic between two devices on the network.

In any case, even if the MAC does not match an authorized device on the network, it still allows us to hide the real MAC of our device.

PWNagotchi MacSpoofing v.0.1 is loaded when PWNagotchi starts up and replaces the original MAC of our device, assigning it a new random MAC that changes every 60 seconds.

The newly assigned MAC is displayed in the bottom right corner of the display.

===================================================================
Installation of PWNagotchi MAC Spoofing v.0.1 by Zarkstein
===================================================================

Copy the file MACSpoofing.py into the directory "/etc/pwnagotchi/custom-plugins/" on your PWNagotchi.

Modify the file "/etc/pwnagotchi/config.toml" and ensure that you have the following line:
main.custom_plugins = "/etc/pwnagotchi/custom-plugins/"

Add the following line:
main.plugins.MACSpoofing.enabled = true

Restart the PWNagotchi.

===================================================================
More Info: 
https://github.com/zarkstein/PWNagotchi-MacSpoofing-v.0.1/

===================================================================



===================================================================
PWNagotchi MAC Spoofing v.0.1 por Zarkstein
===================================================================
ESPAÑOL:
===================================================================

El "MAC spoofing" es una técnica utilizada para cambiar la dirección MAC (Media Access Control) de un dispositivo de red para hacer que parezca que es otra. 

La dirección MAC es un identificador único asignado a la tarjeta de red de un dispositivo, y se utiliza para identificar de manera única dicho dispositivo en una red.

Cuando se realiza el MAC spoofing, un atacante puede cambiar la dirección MAC de su dispositivo para que coincida con la dirección MAC de otro dispositivo. 

Si la MAC coincide con un dispositivo autorizado en la red puede permitir al atacante eludir restricciones de seguridad basadas en la dirección MAC, como filtros de acceso, y obtener acceso no autorizado a la red. 

El MAC spoofing también se puede utilizar para realizar ataques de tipo "man in the middle", donde el atacante intercepta y modifica el tráfico entre dos dispositivos en la red.

En todo caso, aunque la MAC no coincida con un dispositivo autorizado en la red, siempre nos permite ocultar la MAC real de nuestro dispositivo.

PWNagotchi MacSpoofing v.0.1 se carga al iniciar el PWNagotchi y sustituye la MAC original de nuestro dispositivo y le asigna una nueva MAC aleatoria que va cambiando cada 60 seg.

La nueva MAC asignada se muestra en la parte inferior derecha en el display.

===================================================================
Instalación de PWNagotchi MAC Spoofing v.0.1
===================================================================

Copia el archivo MACSpoofing.py en el directorio "/etc/pwnagotchi/custom-plugins/" de tu PWNagotchi.

Modifica el archivo "/etc/pwnagotchi/config.toml" y comprueba que tienes la siguiente linea:
main.custom_plugins = "/etc/pwnagotchi/custom-plugins/"

Añade la siguiente linea:
main.plugins.MACSpoofing.enabled = true

Reinicia el PWNagotchi.

===================================================================
Más info:
https://github.com/zarkstein/PWNagotchi-MacSpoofing-v.0.1/
===================================================================


