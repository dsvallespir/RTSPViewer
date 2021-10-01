## RTSPViewer Dahua 4Ch 

#### Introducción 🚀
RTSPViewer es un reproductor de stream por protocolo RTSP para DVRs Dahua de 4 canales escrito en Python 3.9, haciendo uso de PyQt 5.15.4 y OpenCV 4.5.2.52
## ¿Cómo funciona? ✔️
Su funcionamiento consiste básicamente en leer el _stream_ mediante la librería OpenCV para los canales del 1 al 4 y reproducirlos _frame por frame_ utilizando un mecanismo rudimentario de multiplexación en el tiempo.

La sintáxis de la conexión por RTSP utilizada es la siguiente:
```
rtsp://USER:CLAVE@IP:PUERTO/cam/realmonitor?channel=CANAL&subtype=STREAM
```
## Ejecutando las pruebas ⚙️

Las pruebas realizadas sobre equipos de demostración resultaron favorables

## Links ⌨️

Puede consultar la [wiki](https://dahuawiki.com/Remote_Access/RTSP_via_VLC) de Dahua para más información de acceso remoto.

En esta [página](https://dahuawiki.com/Live_Demo) encontrarás equipos de demostración funcionando en tiempo real para hacer tus pruebas.

## Construido con 🛠️

_Herramientas utilizadas para crear el proyecto_

* PyQt - Biblioteca gráfica de Qt para python
* [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) - Librería para Visión por Ordenador
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE de Python

## Cosas a corregir y a futuro 📋

* La cuadricula de video no se ajusta automáticamente al expandir o contraer la ventana principal. Se debe corregir
* La cuadrícula debería ser configurable. A implementar a futuro.
* Se extenderá la cantidad de cámaras a 16. A implementar a futuro.
* Se implementará con QThread. A implementar a futuro.


## Autor ✒️

**Sebastián Vallespir**
* [GitHub](https://github.com/dsvallespir) 
* [LinkedIn](https://www.linkedin.com/in/sebastian-vallespir/)

