## RTSPViewer Dahua 4Ch 

#### Introducci贸n 馃殌
RTSPViewer es un reproductor de stream por protocolo RTSP para DVRs Dahua de 4 canales escrito en Python 3.9, haciendo uso de PyQt 5.15.4 y OpenCV 4.5.2.52
## 驴C贸mo funciona? 鉁旓笍
Su funcionamiento consiste b谩sicamente en leer el _stream_ mediante la librer铆a OpenCV para los canales del 1 al 4 y reproducirlos _frame por frame_ utilizando un mecanismo rudimentario de multiplexaci贸n en el tiempo.

La sint谩xis de la conexi贸n por RTSP utilizada es la siguiente:
```
rtsp://USER:CLAVE@IP:PUERTO/cam/realmonitor?channel=CANAL&subtype=STREAM
```
## Ejecutando las pruebas 鈿欙笍

Las pruebas realizadas sobre equipos de demostraci贸n resultaron favorables

## Links 鈱笍

Puede consultar la [wiki](https://dahuawiki.com/Remote_Access/RTSP_via_VLC) de Dahua para m谩s informaci贸n de acceso remoto.

En esta [p谩gina](https://dahuawiki.com/Live_Demo) encontrar谩s equipos de demostraci贸n funcionando en tiempo real para hacer tus pruebas.

## Construido con 馃洜锔?

_Herramientas utilizadas para crear el proyecto_

* PyQt - Biblioteca gr谩fica de Qt para python
* [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) - Librer铆a para Visi贸n por Ordenador
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE de Python

## Cosas a corregir y a futuro 馃搵

* La cuadricula de video no se ajusta autom谩ticamente al expandir o contraer la ventana principal. Se debe corregir
* La cuadr铆cula deber铆a ser configurable. A implementar a futuro.
* Se extender谩 la cantidad de c谩maras a 16. A implementar a futuro.
* Se implementar谩 con QThread. A implementar a futuro.


## Autor 鉁掞笍

**Sebasti谩n Vallespir**
* [GitHub](https://github.com/dsvallespir) 
* [LinkedIn](https://www.linkedin.com/in/sebastian-vallespir/)

