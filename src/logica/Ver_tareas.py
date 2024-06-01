# src/logica/ver_tareas.py

class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def ver_tareas(self):
        return self.tareas

    def agregar_tarea(self, titulo, descripcion):
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def marcar_tarea_como_completada(self, tarea_id):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.completada = True

    def eliminar_tarea(self, tarea_id):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != tarea_id]
