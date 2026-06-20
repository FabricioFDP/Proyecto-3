class Paciente:
    def __init__(self, id, nombre, edad, prioridad, llegada, tiempo_atencion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.prioridad = prioridad
        self.llegada = llegada
        self.tiempo_atencion = tiempo_atencion
        self.tiempo_restante = tiempo_atencion
        self.estado = "en espera"
        self.tiempo_inicio_atencion = None # Se llena cuando un medico empieza a atenderlo, sirve para calcular el tiempo de espera
        self.tiempo_espera = 0 # Se calcula cuando un medico lo recibe, lo usa estadisticas.py