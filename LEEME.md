*****
PWNagotchi MAC Spoofing por Zarkstein
*****

La dirección MAC es un identificador único asignado a la tarjeta de red de un dispositivo, y se utiliza para identificar de manera única ese dispositivo en una red.

El "spoofing de MAC" es una técnica utilizada para cambiar la dirección MAC (Control de Acceso a Medios) de un dispositivo de red para hacer que parezca ser otro.

Cuando se realiza el spoofing de MAC, un atacante puede cambiar la dirección MAC de su dispositivo para que coincida con la dirección MAC de otro dispositivo.

El spoofing de MAC también se puede utilizar para realizar ataques de "hombre en el medio", donde el atacante intercepta y modifica el tráfico entre dos dispositivos en la red.

Si la MAC coincide con un dispositivo autorizado en la red, puede permitir al atacante eludir restricciones de seguridad basadas en direcciones MAC, como filtros de acceso, y obtener acceso no autorizado a la red.

En cualquier caso, incluso si la MAC no coincide con un dispositivo autorizado en la red, nos permite ofuscar la verdadera MAC de nuestro dispositivo.

PWNagotchi MacSpoofing v.0.1 se carga cuando PWNagotchi se inicia y reemplaza la MAC original de nuestro dispositivo, asignándole una nueva MAC aleatoria que cambia cada 60 segundos.

La nueva MAC asignada se muestra en la esquina inferior derecha de la pantalla y/o la interfaz de usuario.


*****
Instalación
*****


Copia el archivo MACSpoofing.py en el directorio "/etc/pwnagotchi/custom-plugins/" en tu PWNagotchi.

Modifica el archivo "/etc/pwnagotchi/config.toml" y asegúrate de tener la siguiente línea:

main.custom_plugins = "/etc/pwnagotchi/custom-plugins/"

Agrega la siguiente línea:

main.plugins.MACSpoofing.enabled = true

Reinicia el PWNagotchi.


*****
Más información: 
https://github.com/zarkstein/PWNagotchi-MacSpoofing/
*****
