import pytest
from cine import Pelicula

"""
    Crear un archivo de pruebas llamado test_cine.py que cubra diversos escenarios para la venta de entradas.
    Asegurarse de que las pruebas verifiquen que la función vender_entradas en cine.py devuelva los resultados esperados.
    Las pruebas deben garantizar que el programa de venta de entradas funcione correctamente en diferentes situaciones, tales como:
        Compra de entradas con asientos suficientes.
        Compra de entradas con asientos insuficientes.
        Compra de cero entradas.
"""

def test_venta_entradas_suficiente():
    pelicula=Pelicula("Test 1", 10, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Test 1. Total: $50"
    assert pelicula.asientos_disponibles == 5

def test_venta_entradas_insuficiente():
    pelicula = Pelicula("Test 2", 3, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula.asientos_disponibles == 3

def test_vender_cero_entradas():
    pelicula = Pelicula("Test 3", 10, 10)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Test 3. Total: $0"
    assert pelicula.asientos_disponibles == 10