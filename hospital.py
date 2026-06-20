from scheduling import fifo

class Hospital:
    def __init__(self):
        self.medicos = [] # Lista de médicos en el hospital
        self.pacientes_espera = [] # Lista de pacientes en espera
        self.atendidos = [] # Lista de pacientes atendidos
        self.tiempo_actual = 0 # Tiempo actual en el hospital
    
    def agregar_medico(self, medico):
        self.medicos += [medico]
    
    def agregar_paciente(self, paciente):
        self.pacientes_espera += [paciente]
        
    def asignar_pacientes_fifo(self):
        for medico in self.medicos:
            if medico.disponible:
                paciente = fifo(self.pacientes_espera)
                if paciente is not None:
                    
                    medico.paciente_asignado = paciente
                    medico.disponible = False
                    medico.tiempo_atencion_restante = paciente.tiempo_atencion
                    paciente.estado = "en atencion"
                    paciente.tiempo_inicio_atencion = self.tiempo_actual
                    paciente.tiempo_espera = self.tiempo_actual - paciente.llegada
                    
    def mostrar_medicos(self):
        for medico in self.medicos:
            
            if medico.disponible:
                print(f"Médico {medico.nombre}: Disponible") 
            else:
                print(f"Médico {medico.nombre}: Atendiendo a {medico.paciente_asignado.nombre}")
                
    def avanzar_tiempo(self):
        self.tiempo_actual += 1
        
        for medico in self.medicos:
            if not medico.disponible:
                
                medico.tiempo_atencion_restante -= 1
                
                if medico.tiempo_atencion_restante <= 0:
                    
                    medico.paciente_asignado.estado = "atendido"
                    medico.pacientes_atendidos += 1
                    
                    self.atendidos += [medico.paciente_asignado]
                    medico.paciente_asignado = None
                    
                    medico.disponible = True
                    
                    medico.tiempo_atencion_restante = 0