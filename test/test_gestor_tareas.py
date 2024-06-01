# tests/test_gestor_tareas.py
import unittest
from src.logica.Ver_tareas import GestorTareas, Tarea

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")

    def test_ver_tareas(self):
        tareas = self.gestor.ver_tareas()
        self.assertEqual(len(tareas), 2)

    def test_marcar_tarea_como_completada(self):
        tarea_id = self.gestor.ver_tareas()[0].id
        self.gestor.marcar_tarea_como_completada(tarea_id)
        tarea_completada = self.gestor.ver_tareas_completadas()
        self.assertEqual(len(tarea_completada), 1)

    def test_eliminar_tarea(self):
        tarea_id = self.gestor.ver_tareas()[0].id
        self.gestor.eliminar_tarea(tarea_id)
        tareas = self.gestor.ver_tareas()
        self.assertEqual(len(tareas), 1)
