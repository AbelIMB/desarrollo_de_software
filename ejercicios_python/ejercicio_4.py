
def celcius_Farenheit(val):
    fahrenheit = (val * 9/5) + 32
    return fahrenheit
def farenheit_Celcius(val):
    celsius = (val - 32) * 5/9
    return celsius

def ingresoDatos():
    valor = int(input("Ingrese solo valor numérico de la temperatura: "))
    escala = input("Ingrese la escala original: ")

    if escala == ('c' or 'C'):
        valor=celcius_Farenheit(valor)
        escala='F'
    elif escala == ('f' or 'F'):
        valor=farenheit_Celcius(valor)
        escala='C'

    print(f"Resultado: {valor} {escala}°")

#MAIN
if __name__ == '__main__':
    import sys

ingresoDatos()