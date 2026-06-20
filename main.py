from paciente import Paciente
from medico import Medico
from hospital import Hospital
from estadisticas import mostrar_estadisticas


def cargar_pacientes_desde_archivo(ruta):
    pacientes = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea == "" or linea.startswith("#"): # Ignorar lineas vacias y comentarios
                continue

            datos = linea.split(",")

            id_paciente = int(datos[0])
            nombre = datos[1]
            edad = int(datos[2])
            prioridad = int(datos[3])
            llegada = int(datos[4])
            tiempo_atencion = int(datos[5])

            pacientes.append(Paciente(id_paciente, nombre, edad, prioridad, llegada, tiempo_atencion))

    return pacientes


hospital = Hospital()

# Registrar médicos
hospital.agregar_medico(
    Medico(1, "Rivas")
)

hospital.agregar_medico(
    Medico(2, "Cubero")
)

# Registrar pacientes desde el archivo de prueba
pacientes = cargar_pacientes_desde_archivo("pacientes_prueba.txt")

for paciente in pacientes:
    hospital.agregar_paciente(paciente)

algoritmo = "FIFO"

# Asignar pacientes usando FIFO
hospital.asignar_pacientes_fifo()

# Mostrar estado inicial
print("\n=== ESTADO INICIAL ===")
hospital.mostrar_medicos()

# Simular el tiempo hasta atender a todos los pacientes
while len(hospital.atendidos) < len(pacientes):

    print(f"\n=== TIEMPO {hospital.tiempo_actual} ===")

    hospital.mostrar_medicos()

    hospital.avanzar_tiempo()
    hospital.asignar_pacientes_fifo() # Asignar a los medicos que vayan quedando libres


print("\n=== PACIENTES ATENDIDOS ===")

for paciente in hospital.atendidos:

    print(
        f"{paciente.nombre} - {paciente.estado}"
    )

print("\nCantidad atendidos:",
      len(hospital.atendidos))

# Mostrar estadísticas finales (punto 10)
mostrar_estadisticas(pacientes, hospital.medicos, algoritmo)
