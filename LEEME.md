# Complemento PWNagotchi MacSpoofing

PWNagotchi MacSpoofing Plugin es una extensión para PWNagotchi, un dispositivo de prueba de red Wi-Fi basado en Raspberry Pi.

Este complemento cambia automáticamente la dirección MAC de la interfaz wlan0 de nuestro Pwnagotchi y la muestra en pantalla (o no) según sus necesidades específicas.


## ¿Qué es una dirección MAC?

La dirección MAC es un identificador único asignado a la tarjeta de red de un dispositivo conectado a una red.

Por ejemplo, una dirección MAC típica tendría este aspecto: AB:CD:EF:12:34:56.

En esta dirección MAC podemos encontrar dos partes:

### OUI (Identificador único organizacional):
Los primeros tres pares de caracteres en una dirección MAC representan el OUI, que identifica al fabricante del dispositivo de red.
El Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) asigna OUI a los fabricantes y garantiza que sean únicos.
Los fabricantes pueden solicitar una OUI al IEEE y luego utilizarla en sus dispositivos.

### Identificador del dispositivo (ID):
Los últimos tres pares de caracteres de una dirección MAC representan el identificador único del dispositivo en la red.
Este identificador lo asigna el fabricante del dispositivo para cada modelo de uno de sus productos.

Por lo tanto, una dirección MAC proporciona una forma única de identificar tanto al fabricante del dispositivo como al dispositivo específico en una red.
Esta identificación única es esencial para la operación y administración de la red, permitiendo que los dispositivos se comuniquen entre sí de manera eficiente y segura.


## ¿Qué es la suplantación de MAC?

La "suplantación de MAC" es una técnica utilizada para cambiar la dirección MAC de un dispositivo de red para que parezca otro dispositivo.

La suplantación de MAC en un Pwnagotchi puede proporcionar varias ventajas:

### Anonimato y privacidad:
Al cambiar periódicamente la dirección MAC del Pwnagotchi, dificulta que otros dispositivos o redes rastreen o identifiquen el Pwnagotchi de manera consistente.
Esto puede ayudar a preservar el anonimato y la privacidad del usuario durante las pruebas de penetración o las auditorías de red.

### Evite las restricciones de seguridad basadas en MAC:
Al cambiar la dirección MAC, Pwnagotchi puede eludir las restricciones de seguridad que se basan en la dirección MAC de los dispositivos.
Por ejemplo, si una red Wi-Fi solo permite el acceso a dispositivos con direcciones MAC específicas, la suplantación de MAC puede permitir que Pwnagotchi acceda a la red sin necesidad de conocer las direcciones MAC autorizadas.

### Ofuscación de la identidad del dispositivo:
La suplantación de MAC puede hacer que Pwnagotchi aparezca como otro tipo de dispositivo en la red, lo que puede dificultar que otros usuarios o administradores de red identifiquen el dispositivo.
Esto puede resultar útil para realizar pruebas de penetración de forma más sigilosa o para evitar la detección por parte de las medidas de seguridad de la red.

### Diversificación de identidad:
Al cambiar periódicamente la dirección MAC, Pwnagotchi puede presentarse como múltiples dispositivos distintos en la red.
Esto puede resultar útil para simular varios usuarios o dispositivos en una auditoría de red, lo que permite detectar y analizar diferentes comportamientos o vulnerabilidades.

En resumen, la suplantación de MAC en un Pwnagotchi puede proporcionar anonimato, elusión de restricciones de seguridad, ofuscación de identidad y diversificación de identidad, lo que puede resultar beneficioso para realizar pruebas de penetración, auditorías de red y otras actividades relacionadas con la ciberseguridad.

## Requisitos

- PWNagotchi instalado y configurado.
- Conexión a Internet para descargar y actualizar el complemento.


## Instalación del complemento PWNagotchi MacSpoofing

1. Descargue el archivo MACSpoofing.py de este repositorio:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/

2. Copie el archivo MACSpoofing.py a su directorio "/etc/pwnagotchi/custom-plugins/" en su tarjeta microSD.

3. Modifique su archivo /etc/pwnagotchi/config.toml y agregue la siguiente línea:

main.plugins.macspoofing.enabled = verdadero

NOTA: También puedes activarlo desde la sección Complementos del panel de control web.

4. Reinicia tu PWNagotchi.


## Características del complemento PWNagotchi MacSpoofing

El complemento comenzará a funcionar cuando inicie su PWNagotchi y luego realizará las siguientes funciones:

- Cambio automático de dirección MAC del PWNagotchi
- Personalización de la dirección MAC
- Mostrar la nueva MAC en pantalla
- Actualización periódica de la dirección MAC cada 15 minutos
- Escribir el log con información sobre la nueva dirección MAC asignada


# Uso y Configuración
# Variables personalizables

Puede personalizar cómo funciona el complemento en el código MACSpoofing.py para satisfacer sus necesidades específicas:

- update_interval: esta variable determina con qué frecuencia se cambia la dirección MAC.
 Puede ajustar el valor en segundos para cambiar la dirección MAC con mayor o menor frecuencia.
 El valor predeterminado del intervalo es 15 minutos, update_interval = 900.
 Por ejemplo, si desea cambiar la dirección MAC cada 10 minutos, puede configurar update_interval = 600.

- mac_on_display: esta variable controla si la nueva dirección MAC se muestra o no en la interfaz de usuario.
 El valor predeterminado para mac_on_display es Verdadero.
 Si configura mac_on_display = True (la nueva dirección MAC se mostrará en la pantalla).
 Si configura mac_on_display = False (la dirección MAC no se mostrará en la pantalla).
 En ambos casos la nueva dirección MAC se guardará en el registro.

- oui: esta variable representa el identificador único organizacional (OUI) que se utiliza como prefijo para generar la dirección MAC.
 De forma predeterminada, el valor de oui = "00:11:24" (producto de Cisco)
 Puede cambiar este valor para usar una OUI diferente para personalizar la apariencia de la dirección MAC generada.
 Si desea que la dirección MAC parezca pertenecer a una empresa específica, puede cambiar el valor de OUI a uno de los siguientes:

+ Cisco Systems, Inc.: 00:01:42
+ Apple, Inc.: 00:11:24
+ Corporación Intel: 00:00:86
+ Samsung Electronics Co., Ltd.: 00:16:32
+ Corporación Microsoft: 00:0F:FB
+ Huawei Technologies Co., Ltd.: 00:E0:FC
+ Dell Inc.: 00:14:22
+ Hewlett Packard Enterprise: 00:50:56
+ Corporación Sony: 00:0A:89
+ Google LLC: 00:1A:11

#
Más información
*****

Sobre el Autor:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/

Complemento disponible para descargar en:
https://github.com/zarkstein/PWNagotchi-MacSpoofing/releases

PWNagotchi:
https://pwnagotchi.ai/


*****
Contribuciones
*****

¡Las contribuciones son bienvenidas! Si tiene ideas para mejoras, problemas o soluciones, abra un problema o envíe una solicitud de extracción.

*****
