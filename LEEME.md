*****
PWNagotchi MAC Spoofing por Zarkstein
*****

La dirección MAC es un identificador único asignado a la tarjeta de red de un dispositivo, y se utiliza para identificar de manera única ese dispositivo en una red.

El "spoofing de MAC" es una técnica utilizada para cambiar la dirección MAC (Control de Acceso a Medios) de un dispositivo de red para hacer que parezca ser otro.

Cuando se realiza el spoofing de MAC, un atacante puede cambiar la dirección MAC de su dispositivo para que coincida con la dirección MAC de otro dispositivo.

El spoofing de MAC también se puede utilizar para realizar ataques de "hombre en el medio", donde el atacante intercepta y modifica el tráfico entre dos dispositivos en la red.

Si la MAC coincide con un dispositivo autorizado en la red, puede permitir al atacante eludir restricciones de seguridad basadas en direcciones MAC, como filtros de acceso, y obtener acceso no autorizado a la red.

En cualquier caso ofuscar la verdadera MAC de nuestro dispositivo siempre nos aportará mayor seguridad.

PWNagotchi MacSpoofing se carga cuando PWNagotchi se inicia y reemplaza la MAC original de nuestro dispositivo, asignándole una nueva MAC aleatoria que cambia cada 15 minutos.

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
Configuración
*****

Por defecto, el plugin está configurado para cambiar la dirección MAC cada 15 minutos. 

Puedes ajustar este valor modificando el código del plugin en el archivo macspoofing.py.


*****
FUNCIONAMIENTO
*****
¿Cómo funciona PWNagotchi MACSpoofing?
*****

*****
Inicio y Carga del Plugin:
*****

Cuando Pwnagotchi se inicia, el plugin "MAC Spoofing" se carga automáticamente si está instalado y activado.

Durante la carga, se establece el estado inicial del plugin y se configura para estar listo para su uso.
        

*****
Cambio de Dirección MAC:
*****

El plugin genera una nueva dirección MAC aleatoria para la interfaz wlan0 (WiFi).

Utiliza el comando ip link set de Linux para cambiar la dirección MAC de la interfaz wlan0 a la nueva dirección generada.

Si el cambio de dirección MAC falla, el plugin realiza varios intentos (definidos por max_retries) con intervalos de espera (definidos por time.sleep) antes de registrar un error.


*****
Interfaz de Usuario:
*****

El plugin muestra la dirección MAC actualizada en la interfaz de usuario de Pwnagotchi.

Utiliza el componente LabeledValue de la biblioteca de interfaz de usuario de Pwnagotchi para mostrar la dirección MAC en la pantalla.


*****
Actualización Periódica:
*****

El plugin actualiza periódicamente la dirección MAC mostrada en la interfaz de usuario.

La frecuencia de actualización está definida por el intervalo de tiempo especificado en self.last_update_time.

Cuando transcurre el intervalo de tiempo especificado, el plugin genera una nueva dirección MAC y actualiza la interfaz de usuario.


*****
Descarga del Plugin:
*****

Cuando el plugin se descarga o se desactiva, elimina el elemento de la interfaz de usuario relacionado con la dirección MAC.

Esto ayuda a limpiar la interfaz de usuario y liberar recursos cuando el plugin ya no está en uso.


*****


*****
Más información
*****

Información sobre el autor:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/

Última versión del plugin disponible para descargar en:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/releases



*****
Contribuciones
*****

¡Las contribuciones son bienvenidas! Si tienes ideas para mejoras, problemas o correcciones, por favor, abre un issue o envía un pull request.


*****
Licencia
*****

Este plugin se publica bajo la licencia GPL-3.0. Para más detalles, por favor, consulta el archivo LICENSE.

*****
