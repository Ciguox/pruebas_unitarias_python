import pytest
from biblioteca import Libro
from biblioteca import Biblioteca

#2.1. Pruebas para la clase Libro:

#   Verificar que los atributos (titulo, autor, año) se inicializan correctamente.
def test_libro_check_atributos():
    libro = Libro("Libro 1", "Autor 1", 2000)
    assert libro.titulo == "Libro 1"
    assert libro.autor == "Autor 1"
    assert libro.anio == 2000
    assert libro.prestado == False

def test_libro_check_atributos_to_str():
    libro = Libro("Libro 1", "Autor 1", 2000)
    assert str(libro) == "Libro 1 de Autor 1 (2000) - disponible"

#   Verificar cuando un libro está prestado o cuando está disponible.
def test_libro_prestado():
    libro = Libro("Libro 1", "Autor 1", 2000)
    assert libro.prestado == False
    libro.prestado = True
    assert libro.prestado == True

#2.2. Pruebas para la clase Biblioteca:

#Agregar libros: Verificar que un libro se agrega correctamente a la biblioteca.
def test_biblioteca_agregar_libro():
    biblioteca = Biblioteca()
    assert biblioteca.listar_libros() == []
    biblioteca.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    assert biblioteca.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible"]

#Eliminar libros:

#    Verificar que un libro se elimina correctamente de la biblioteca.
def test_biblioteca_eliminar_libro_existente():
    biblioteca = Biblioteca()
    assert biblioteca.listar_libros() == []
    biblioteca.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    assert biblioteca.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible"]
    biblioteca.eliminar_libro("Libro 1")
    assert biblioteca.listar_libros() == []

#    Verificar que intentar eliminar un libro que no existe no afecte la lista de libros.
def test_biblioteca_eliminar_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.listar_libros() == []
    biblioteca.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    assert biblioteca.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible"]
    biblioteca.eliminar_libro("Libro 2")
    assert biblioteca.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible"]

#Buscar libros:

#    Verificar que un libro existente se puede encontrar.
def test_biblioteca_buscar_libro_existente():
    bi = Biblioteca()
    bi.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    assert str(bi.buscar_libro("Libro 1")) == "Libro 1 de Autor 1 (2000) - disponible"

#    Verificar que la búsqueda de un libro que no existe devuelve None.
def test_biblioteca_buscar_libro_no_existente():
    bi = Biblioteca()
    assert str(bi.buscar_libro("Libro 1")) == "None"
#Listar libros:

#    Verificar que la lista de libros se retorna correctamente.
def test_biblioteca_listar_libros():
    biblioteca = Biblioteca()
    assert biblioteca.listar_libros() == []
    biblioteca.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    assert biblioteca.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible"]
    biblioteca.agregar_libro(Libro("Libro 2", "Autor 2", 2001))
    assert biblioteca.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible", "Libro 2 de Autor 2 (2001) - disponible"]

#Prestar libros:
def test_biblioteca_prestar_libros():
    bi = Biblioteca()
    bi.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    assert bi.listar_libros() == ["Libro 1 de Autor 1 (2000) - disponible"]
#    Verificar que un libro se presta correctamente.
    assert bi.prestar_libro("Libro 1") == "Has pedido prestado el libro 'Libro 1'."
#    Verificar que intentar prestar un libro ya prestado devuelve un mensaje adecuado.
    assert bi.prestar_libro("Libro 1") == "El libro 'Libro 1' ya está prestado."
#    Verificar que intentar prestar un libro que no existe devuelve un mensaje adecuado.
    assert bi.prestar_libro("Libro 2") == "El libro 'Libro 2' no se encuentra en la biblioteca."

#Devolver libros:
def test_biblioteca_devolver_libros():
    bi = Biblioteca()
    bi.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    bi.listar_libros()
    bi.prestar_libro("Libro 1")
#    Verificar que un libro se devuelve correctamente.
    assert bi.devolver_libro("Libro 1") == "Has devuelto el libro 'Libro 1'."
#    Verificar que intentar devolver un libro no prestado devuelve un mensaje adecuado.
    assert bi.devolver_libro("Libro 1") == "El libro 'Libro 1' no estaba prestado."
#    Verificar que intentar devolver un libro que no existe devuelve un mensaje adecuado.
    assert bi.devolver_libro("Libro inexistente") == "El libro 'Libro inexistente' no se encuentra en la biblioteca."