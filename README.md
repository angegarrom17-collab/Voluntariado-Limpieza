
1. Descripción:
Este sistema es diseñado para gestionar el impacto ambiental en zonas costeras. El propósito principal es permitir a los usuarios registrar y monitorear datos sobre fauna afectada y residuos recolectados, facilitando el análisis a través de reportes estadísticos. La aplicación busca ser una herramienta de apoyo para la toma de decisiones en temas de conservación y gestión ambiental.


2. Arquitectura
El proyecto sigue el patrón de arquitectura MVC (Modelo-Vista-Controlador) para garantizar la separación de responsabilidades y la modularidad del código:

Model: Define las entidades de negocio (AnimalAfectado, BasuraRecolectada) y su estructura de datos.

View (GUI): Interfaz gráfica modular construida con tkinter, que permite la navegación y visualización de datos sin mezclarse con la lógica.

Controller: Actúa como intermediario, gestionando los eventos de la vista y comunicándose con los servicios.

Service: Contiene la lógica de negocio, cálculos (totales, promedios) y validaciones.

Repository: Encargado de la persistencia de datos mediante archivos JSON, garantizando la carga y guardado automático.

3. Principios SOLID:
El sistema ha sido diseñado aplicando los principios SOLID para asegurar un código mantenible y escalable:

S (Responsabilidad Única): Cada clase tiene una única responsabilidad. Por ejemplo, la persistencia está delegada exclusivamente a los repositorios, y los cálculos a los servicios.

O (Abierto/Cerrado): El sistema está abierto a la extensión (podemos agregar nuevos tipos de reportes) sin necesidad de modificar el código existente en los controladores.

L (Sustitución de Liskov): Las subclases pueden reemplazar a sus clases base sin alterar el funcionamiento del sistema.

I (Segregación de Interfaz): Las interfaces y módulos están divididos de tal manera que ninguna parte del sistema depende de métodos que no utiliza.

D (Inversión de Dependencia): Los módulos de alto nivel (como el Controlador) no dependen de los detalles de implementación (lectura de archivos específicos), sino de abstracciones proporcionadas por los repositorios.

4. Instrucciones de uso
Requisitos: Tener instalado Python 3.x

Ejecución:

-Abre una terminal en la carpeta raíz del proyecto.

-Ejecuta el archivo principal mediante el comando: python main.py

Navegación:

-Al iniciar, se vera el menú principal.

-Utiliza los botones de navegación para acceder a los módulos de registro de animales o basura.

Para visualizar el reporte, se accede al módulo "Reporte General" y presiona el botón "Generar Reporte".

Datos: Los archivos JSON se cargarán automáticamente al iniciar la aplicación. 