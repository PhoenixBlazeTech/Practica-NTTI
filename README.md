# Generador y Visualizador de Señales

## Descripción

Esta aplicación permite generar y visualizar una señal periodica compuesta propuesta y ajustar sus algunos de sus parámetros en tiempo real. Utiliza `matplotlib` para la visualización y `numpy` para la generación de las señales.

## Funcionalidades

- Ajuste de parámetros de la señal en tiempo real mediante campos de texto interactivos.
- Visualización de la señal generada en una gráfica.

## Parámetros de la Señal

- **Amplitud (A)**: Controla la amplitud de la señal.
- **Frecuencia (f)**: Controla la frecuencia de la señal.
- **Coeficiente de Escala (k)**: Escala la señal generada.
- **Desplazamiento en Y**: Desplaza la señal en el eje Y.

## Uso

1. Ejecuta el script `practica.py`.
2. Se abrirá una ventana con una gráfica de la señal generada.
3. Ajusta los parámetros de la señal utilizando los campos de texto en la parte inferior de la ventana.
4. La gráfica se actualizará automáticamente con los nuevos valores de los parámetros.

## Requisitos

- Python 3.6 o superior
- `numpy`
- `matplotlib`

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/PhoenixBlazeTech/Practica-NTTI.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd PRACTICA-NTTI
    ```
3. Instala las dependencias:
    ```sh
    pip install numpy matplotlib scipy
    ```

## Ejecución

Para ejecutar la aplicación, usa el siguiente comando:

```sh
python practica.py
