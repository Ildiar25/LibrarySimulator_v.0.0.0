# Gestión de una Biblioteca

**Objetivo**: Modelar una biblioteca utilizando jerarquía de clases y polimorfismo en Python.

**Descripción**: Simular una biblioteca que pueda contener información diversa. Entre ella podremos encontrar los
clientes registrados o los libros almacenados. Deberá implementar la lectura, escritura y guardado de archivos externos
(ya sean tipo *.txt o *.csv) y un registro horario de cuándo se retiran los libros. También se deberá implementar el bloque
_'try - except'_ para lanzar y capturar excepciones.

**Elementos**: Sus principales clases serán _Libro_, _Lector_ y _Biblioteca_. Se pueden añadir más si es necesario.

---

### · Clase Libro:
Objeto que representará un libro cuyos atributos son:
- **ISBN**_(int): Representará un código de 10 dígitos
- **Título**_(str): El nombre del libro
- **Autor**_(str): El nombre del autor
- **Género**_(str): El género del libro
- **Estado**_(str): Estado del libro (_Disponible_, _Prestado_, _Reservado_)

Se complementará con los siguientes métodos:
- **Prestar()**: Cambiará el estado del libro a _Prestado_.
- **Devolver()**: Cambiará el estado del libro a _Disponible_.
- **Reservar()**: Cambiará el estado del libro a _Reservado_.

---

### · Clase Cliente:
Objeto que representará un cliente cuyos atributos son:
- **ID**_(str): Representará un código de de 10 dígitos alfanuméricos aleatorio
- **Nombre**_(str): Nombre del cliente
- **Apellido**_(str): Apellido del cliente
- **Máximos Prestados**_(int): Un número máximo de libros que puede llevarse
- **Libros Prestados**_(list): Lista de libros prestados totales con su fecha

Se complementará con los siguientes métodos:
- **CogerLibro()**: Intenta coger un libro teniendo en cuenta si tiene alguno ya y el estado del libro elegido
- **DevolverLibro()**: Devuelve el libro prestado
- **ReservarLibro()**: Permite reservar un libro si no se puede coger

---

### · Clase Biblioteca:
Objeto que representará la biblioteca cuyos atributos son:
- **CatalogoLibros**_(list): Lectura y carga del archivo "libros registrados"
- **ClientesRegistrados**_(list): Lectura y carga del archivo "clientes registrados"

Se complementará con los siguientes métodos:
- **RegistrarLibro()**: Añade un libro al registro de libros
- **RegistrarCliente()**: Añade un cliente al registro de clientes
- **MostrarCatalogo()**: Muestra por pantalla los libros registrados
- **MostrarClientes()**: Muestra por pantalla la lista de clientes registrados
- **BuscarLibro()**: Busca un libro por su ISBN en el catálogo

---

### · Recursos Adicionales:
- https://docs.python.org/3/tutorial/classes.html
- https://www.youtube.com/watch?v=yBVmedkIlUA
- https://fragmentosdecodigo.home.blog/2020/11/28/ejemplos-de-programacion-orientada-a-objetos-poo-en-python/
