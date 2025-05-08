Parte 1: Teoría (4 puntos)
1.	Explica las diferencias entre el protocolo TCP y el protocolo UDP. ¿Cuándo elegirías uno sobre el otro?

TCP y UDP son protocolos de transmisión de datos de usar, ambos forman partes de de la capa de transporte. Ambos tienen distintos enfoques.
TCP: Establece una conexión lógica entre el emisor y el receptor antes de enviar cualquier dato. Esto permite que los datos se transmitan en orden y el receptor pueda reconocerlos. Si hay corrupción de datos en el proceso el protocolo lo reenviara hasta se logre enviar correctamente. TCP tambien ajusta la velocidad de transmisión acorde a la configuración de red de esta manera se garantiza que los datos se envíen sin errores y en secuencia.
UDP: Este es un protocolo sin conexión( no hay conexión con el receptor). Los paquetes de datos se envían lo mas rápido posible y no hay garantía de que estos lleguen. Lo hace de forma rápida y eficiente. Este protocolo tiene menos sobrecarga que TCP.
Para saber cuando usar TCP y UDP se debe considerar el equilibrio entre eficiencia y confiabilidad. Esto va a depender de los requisitos y su aplicación. En juegos en línea, por ejemplo, se suelen usar prtotocolos de transmisión UDP y para los chat en línea TCP.

2.	Describe brevemente el modelo cliente-servidor y su importancia en el desarrollo de servicios de comunicaciones.
El modelo cliente-servidor es un esquema de interacción de red en donde un cliente que puede ser un software o dispositivo solicita servicios y recursos aa un servidor que tambien puede ser un software o dispositivo.
3.	¿Cuál es la diferencia entre una petición HTTP de tipo GET y una de tipo POST? Proporciona un caso de uso para cada una.
GET es un tipo de petición que utiliza el cliente para solicitar algún servicio al servidor y POST es aquella que utiliza el servidor para enviar la información que se es solicitada.
4.	¿Qué es una API y por qué es fundamental en el desarrollo de software para comunicaciones?
La API es una interfaz de programación de aplicaciones que permite la comunicaciones entre si de distintas aplicaciones.
