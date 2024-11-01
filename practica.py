import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
from scipy.fft import fft,fftfreq,fftshift

"""Generamos la señal usando los parámetros de entrada"""
def generar_funcion(amplitud=1, frecuencia=1, coeficiente_de_escala=1, desplazamiento_y = 0, tiempo_max=1, num_puntos=1000):
    tiempo = np.linspace(0, tiempo_max, num_puntos) #vector de tiempo
    #Generamos la señal con dos componentes con una amplitud "desconocida"
    funcion_anormal = np.sin(2*np.pi*frecuencia*tiempo) + (1/3)*np.sin(6*np.pi*frecuencia*tiempo)
    #Calculamos el valor máximo de la señal
    max_valor = np.max(np.abs(funcion_anormal))
    #Dividimos todos los puntos del vector de la señal por el valor máximo normalizando la señal
    funcion_normalizada = funcion_anormal/max_valor
    #Con la señal normalizada, ahora es mas facil ajustar la amplitud de la señal
    funcion = coeficiente_de_escala*(desplazamiento_y + amplitud* funcion_normalizada)
    return tiempo, funcion


# Cálculo del ancho de banda (usando la frecuencia más alta - la frecuencia base)
def calcular_ancho_de_banda(frecuencia_base):
    return 3 * frecuencia_base - frecuencia_base

# Cálculo de la velocidad de transferencia
def calcular_velocidad_transferencia(ancho_de_banda):
    return 2 * ancho_de_banda


# Crear la figura y la gráfica inicial
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.15, bottom=0.45)

# Señal en el tiempo
tiempo, funcion = generar_funcion()
line1, = ax1.plot(tiempo, funcion, label="s(t)", color='b')
ax1.set_title("Señal con Componente Continua")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Amplitud")
ax1.grid(True)
ax1.legend()


#espectro de frecuencia 
def calcular_espectro(funcion, tiempo):
    num_puntos=len(funcion)
    espectro = fft(funcion)
    frecuencias = fftfreq(num_puntos,d = tiempo[1] - tiempo[0]) 
    return espectro,frecuencias,num_puntos




# Espectro en frecuencia
espectro,frecuencias,num_puntos= calcular_espectro(funcion, tiempo)
amplitud = (2/num_puntos)*abs(espectro)
# Define un umbral para los "picos altos", y asi eliminar los bajos
umbral = 0.1  # Ajusta este valor según necesites
frecuencias_altas = frecuencias[amplitud > umbral]
amplitud_alta = amplitud[amplitud > umbral]
ax2.stem(frecuencias_altas,amplitud_alta,basefmt=" ", linefmt='r-', markerfmt='ro')
ax2.set_title("Espectro S(f)")
ax2.set_xlabel("Frecuencia (Hz)")
ax2.set_ylabel("Amplitud (normalizada)")
ax2.set_xlim([0, max(frecuencias) / 50])
ax2.grid(True)

# Función para actualizar la gráfica con los nuevos valores de parámetros
def actualizar(val):
    try:
        # Obtener valores de las cajas de texto y convertirlos a float
        amplitud = float(text_amplitud.text)
        frecuencia = float(text_frecuencia.text)
        coeficiente_de_escala = float(text_coeficiente_escala.text)
        desplazamiento_y = float(text_desplazamiento_y.text)

        # Generar señal actualizada
        tiempo, nueva_funcion = generar_funcion(amplitud, frecuencia, coeficiente_de_escala, desplazamiento_y)
        
        
        # Calcular ancho de banda y velocidad de transferencia
        ancho_de_banda = calcular_ancho_de_banda(frecuencia)
        velocidad_transferencia = calcular_velocidad_transferencia(ancho_de_banda)

        # Actualizar la gráfica de la señal en el tiempo
        line1.set_ydata(nueva_funcion)
        line1.set_xdata(tiempo)
        ax1.relim()
        ax1.autoscale_view()

        # Calcular nuevo espectro y actualizar la gráfica
        nuevo_espectro,nuevas_frecuencias, num_puntos= calcular_espectro(nueva_funcion, tiempo)
        ax2.clear()
        ax2.stem(nuevas_frecuencias,(2/num_puntos)*abs(nuevo_espectro), basefmt=" ", linefmt='r-', markerfmt='ro')
        ax2.set_title("Espectro S(f)")
        ax2.set_xlabel("Frecuencia (Hz)")
        ax2.set_ylabel("Amplitud (normalizada)")
        ax2.set_xlim([0, max(frecuencias) / 50])
        ax2.grid(True)
        
        # Actualizar el texto debajo de los cuadros de entrada
        text_area.set_text(f"Ancho de Banda: {ancho_de_banda:.2f} Hz | Velocidad de Transferencia: {velocidad_transferencia:.2f} bits/s")
        
        fig.canvas.draw_idle()
    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")

# Crear campos de texto para parámetros de la señal
axbox_amplitud = plt.axes([0.15, 0.26, 0.1, 0.05])
text_amplitud = TextBox(axbox_amplitud, 'Amplitud', initial="1")
text_amplitud.on_submit(actualizar)

axbox_frecuencia = plt.axes([0.35, 0.26, 0.1, 0.05])
text_frecuencia = TextBox(axbox_frecuencia, 'Frecuencia', initial="1")
text_frecuencia.on_submit(actualizar)

axbox_coeficiente_escala = plt.axes([0.55, 0.26, 0.1, 0.05])
text_coeficiente_escala = TextBox(axbox_coeficiente_escala, 'Coef. Escala', initial="1")
text_coeficiente_escala.on_submit(actualizar)

axbox_desplazamiento_y = plt.axes([0.75, 0.26, 0.1, 0.05])
text_desplazamiento_y = TextBox(axbox_desplazamiento_y, 'Despl. Y', initial="0")
text_desplazamiento_y.on_submit(actualizar)

# Texto para mostrar el ancho de banda y velocidad de transferencia
text_area = plt.figtext(0.5, 0.2, "", ha="center", va="center", fontsize=10, color="blue")


plt.show()

