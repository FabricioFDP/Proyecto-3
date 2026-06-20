def fifo(pacientes_espera):
    if len(pacientes_espera) > 0:
        return pacientes_espera.pop(0) # Elimina y devuelve el primer paciente en la lista
    return None # Si no hay pacientes en espera, devuelve None
