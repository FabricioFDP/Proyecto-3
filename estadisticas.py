def mostrar_estadisticas(pacientes, medicos, algoritmo):#Muestra el resumen final
    #Mostrar titulo
    print("\n===== ESTADISTICAS =====")
    #Mostrar algoritmos utilizados
    print("Algoritmo utilizado:", algoritmo)
    #Cantidad total
    total= len(pacientes)
    #Contador de atendidos
    atendidos=0
    #Acumuladores
    espera_total=0
    atencion_total=0
    #Recorrer pacientes
    for paciente in pacientes:
        if paciente.estado == "atendido":#Verificar si el paciente fue atendido
            atendidos += 1
            espera_total += paciente.tiempo_espera
            atencion_total += paciente.tiempo_atencion
    #Calcular pendientes
    pendientes= total - atendidos
    
    if atendidos>0:#Evitar la division entre cero
        promedio_espera= (espera_total / atendidos)
        promedio_atencion= (atencion_total / atendidos)
    else:
        promedio_espera=0
        promedio_atencion=0

    #Mostrar resultados
    print("Pacientes registrados:", total)
    print("Pacientes atendidos:", atendidos)
    print("Pacientes pendientes:", pendientes)
    print("Tiempo promedio de espera:", round(promedio_espera, 2), "minutos")
    print("Tiempo promedio de atención:", round(promedio_atencion, 2), "minutos")
    print("\nPacientes por medico:")
    
    for medico in medicos:#Mostrar desempeño medico
        print(medico.nombre, "->", medico.pacientes_atendidos)

    