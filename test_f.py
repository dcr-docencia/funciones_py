import matplotlib.pyplot as plt
import numpy as np

def graficar_parabola():
    x = np.linspace(-10, 10, 100)
    y = x**2
    
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title("¡Prueba de sistema exitosa! f(x) = x^2")
    plt.grid(True)
    plt.show()
