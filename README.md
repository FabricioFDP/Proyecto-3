# Simulación de Atención Hospitalaria

## Descripción

Este proyecto simula el funcionamiento de un hospital utilizando Programación Orientada a Objetos (P.O.O.). El sistema registra pacientes y médicos, administra una sala de espera y asigna pacientes mediante distintos algoritmos de scheduling. También simula el paso del tiempo durante la atención.

## Cómo ejecutar

Primero meter todos los codigos junto con el ejemplo de paciente_prueba.txt en una carpeta.
Abrir una terminal y escribir:

```bash
Primero meter todos los codigos junto con el ejemplo de paciente_prueba.txt en una carpeta.
Buscar los codigos, en caso de tener los archivo en la carpeta de descargas ejecutar en la terminal ''cd %USERPROFILE%\Downloads''
python main.py
```

## Funcionamiento

1. Registrar médicos.
2. Registrar pacientes.
3. Seleccionar algoritmo.
4. Iniciar simulación.
5. Atender pacientes.
6. Mostrar estadísticas.

## Algoritmos implementados

### FIFO

Atiende primero al paciente que llegó antes.

Como se aplica: los pacientes se guardan en la lista ''pacientes_espera'' en el orden en que llegan. Cuando un médico queda libre, ''asignar_pacientes_fifo()'' (en ''hospital.py'') llama a la función ''fifo()'' de ''scheduling.py'', que saca con ''pop(0)'' al primer paciente de la lista y se lo asigna al médico. Como siempre se saca de la posición 0, el que llegó primero siempre se atiende primero.

Ejemplo:
Paciente A -> Paciente B -> Paciente C

## Archivos del proyecto

- estadisticas.py -> estadísticas
- hospital.py -> simulación
- main.py -> ejecución
- medico.py -> médicos
- paciente.py -> pacientes
- scheduling.py -> algoritmos
