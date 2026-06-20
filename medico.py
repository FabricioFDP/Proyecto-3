class Medico:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
        self.disponible = True # True si el médico está disponible, False si está atendiendo a un paciente
        self.paciente_asignado = None # Paciente que el médico está atendiendo actualmente
        self.tiempo_atencion_restante = 0 # Tiempo restante para atender al paciente asignado
        self.pacientes_atendidos = 0 # Contador de pacientes que ya atendio, lo usa estadisticas.py