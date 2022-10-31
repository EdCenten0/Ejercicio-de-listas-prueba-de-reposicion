
# Carlos Eduardo Chavarria Centeno
# Universidad Centroamericana (UCA)
# ALgoritmos y estructuras de datos
# 30-10-2022

import os;

nombrePaciente = []
edadPaciente = []
fechaIngresoPaciente = []
domicilioPaciente = []

def ingresar():

    nombrePacienteVar = input("Ingrese el nombre del paciente: ")
    edadPacienteVar = input("Ingrese la edad del paciente: ")
    fechaIngresoPacienteVar = input("Ingrese la fecha de ingreso del paciente: ")
    domicilioPacienteVar = input("Ingrese el domicilio del paciente: ")
    nombrePaciente.append(nombrePacienteVar)
    edadPaciente.append(edadPacienteVar)
    fechaIngresoPaciente.append(fechaIngresoPacienteVar)
    domicilioPaciente.append(domicilioPacienteVar)


def main():


    ingresar()

main()