import numpy as np
import matplotlib.pyplot as plt

def generate_signal(A=1, f=1, k=1, t_max=2, num_points=1000):
    """
    Genera la señal s(t) con componente continua y sus frecuencias.
    """
    t = np.linspace(0, t_max, num_points)
    s_t = A + A * ((4/4) * np.sin(2 * np.pi * f * t) + (1/3) * np.sin(2 * np.pi * f * 3 * t))
    return t, s_t

def plot_signal_and_spectrum(t, s_t, A, f,bandwidth,transfer_rate):
    """
    Grafica la señal s(t) y el espectro S(f) en una sola figura con dos subgráficas.
    """
    # Crear una figura con dos subgráficas (2 filas, 1 columna)
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Primera subgráfica: Señal en el tiempo
    axs[0].plot(t, s_t, label="s(t)", color='b')
    axs[0].set_title("Señal con Componente Continua")
    axs[0].set_xlabel("Tiempo (s)")
    axs[0].set_ylabel("Amplitud")
    axs[0].grid(True)
    axs[0].legend()

    # Segunda subgráfica: Espectro en frecuencia
    freqs = [0, f, 3*f]  # Frecuencias de los componentes
    amplitudes = [A, A * (4/4), A * (1/3)]  # Amplitudes de los componentes
    axs[1].stem(freqs, amplitudes, basefmt=" ")  # Se elimina use_line_collection
    axs[1].set_title("Espectro S(f)")
    axs[1].set_xlabel("Frecuencia (Hz)")
    axs[1].set_ylabel("Amplitud")
    axs[1].grid(True)

    # Anotaciones para el ancho de banda y la velocidad de transferencia
    axs[1].text(0.1, max(amplitudes) * 0.8, f"Ancho de Banda: {bandwidth} Hz", color="red")
    axs[1].text(0.1, max(amplitudes) * 0.6, f"Velocidad de Transferencia: {transfer_rate} bits/s", color="red")

    # Ajustar el espaciado entre las subgráficas
    plt.tight_layout()
    plt.show()

def calculate_bandwidth(f):
    """
    Calcula el ancho de banda como la diferencia entre la frecuencia más alta y la frecuencia más baja.
    """
    return 3 * f - f

def calculate_transfer_rate(bandwidth):
    """
    Calcula la velocidad de transferencia en función del ancho de banda.
    """
    return 2 * bandwidth  # Este valor puede ajustarse según el contexto

# Parámetros de la señal (ingresados por el usuario)
A = float(input("Ingrese la amplitud (A): "))
f = float(input("Ingrese la frecuencia (f): "))
k = float(input("Ingrese el coeficiente de escala (k): "))

# Generar señal
t, s_t = generate_signal(A, f, k)

# Calcular y mostrar ancho de banda y velocidad de transferencia
bandwidth = calculate_bandwidth(f)
transfer_rate = calculate_transfer_rate(bandwidth)

# Graficar señal y espectro en una sola figura con dos subgráficas
plot_signal_and_spectrum(t, s_t, A, f, bandwidth,transfer_rate)


print(f"Ancho de Banda: {bandwidth} Hz")
print(f"Velocidad de Transferencia: {transfer_rate} bits/s")
