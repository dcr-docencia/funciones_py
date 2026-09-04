import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Graficar (representar en el plano cartesiano), algunos elementos puntuales (x,f(x))

def scatter_r_r(x_val,f,
                titulo='$f(x)$'+' vs. '+'$x$',color_puntos='red',eje_x='$x$',eje_y='$f(x)$'):
  #Creamos el área de la figura donde se hará la gráfica
  plt.figure(dpi=150)
  plt.gca().set_axisbelow(True)
  plt.axhline(0,c='k')
  plt.axvline(0,c='k')
  plt.grid(linestyle='--')
  # Creamos la gráfica
  plt.scatter(x_val,f(x_val),c=color_puntos,zorder=3)
  # Añadimos título, nombres de ejes, valores en los ejes, líneas discontínuas, etc
  plt.title(titulo)
  plt.xlabel(eje_x)
  plt.ylabel(eje_y)
  delta_xval=x_val.max()-x_val.min()
  delta_f=f(x_val).max()-f(x_val).min()
  plt.xlim(x_val.min()-delta_xval*0.15,x_val.max()+delta_xval*0.15)
  plt.ylim(f(x_val).min()-delta_f*0.15,f(x_val).max()+delta_f*0.15)
  #plt.xticks(np.arange(x_val.min(),5,1))
  #plt.yticks(np.arange(-1,12,1))
  # Añadimos el texto indicando los elementos de
  for val in x_val:
      plt.text(val+delta_xval*0.01,f(val)+delta_f*0.03,'(%.f,%.f)'%(val,f(val)),fontsize=10)
  plt.show()

# Graficar (representar en el plano cartesiano), los elementos (x,f(x)) en un intervalo de R:

def plot_r_r(x_val,f,
                titulo='$f(x)$'+' vs. '+'$x$',color_linea='red',eje_x='$x$',eje_y='$f(x)$'):
  #Creamos el área de la figura donde se hará la gráfica
  plt.figure(dpi=150)
  plt.gca().set_axisbelow(True)
  plt.axhline(0,c='k')
  plt.axvline(0,c='k')
  plt.grid(linestyle='--')
  # Creamos la gráfica
  plt.plot(x_val,f(x_val),c=color_linea,zorder=3)
  # Añadimos título, nombres de ejes, valores en los ejes, líneas discontínuas, etc
  plt.title(titulo)
  plt.xlabel(eje_x)
  plt.ylabel(eje_y)
  delta_xval=x_val.max()-x_val.min()
  delta_f=f(x_val).max()-f(x_val).min()
  plt.xlim(x_val.min(),x_val.max())
  plt.ylim(f(x_val).min(),f(x_val).max())
  plt.show()

# Gráfica de función de R2 a R

def plot_r2_r(x_val,y_val,g,
                titulo='Gráfica de $g(x,y)$',color_escala='viridis',eje_x='x',eje_y='y',eje_z='g(x,y)'):
  # Definimos la matriz en RxR
  X, Y = np.meshgrid(x_val, y_val)
  Z = g(X, Y)
  # Graficamos la superficie en Plotly
  fig = go.Figure(data=[go.Surface(
      x=X, y=Y, z=Z,
      showscale=False,
      colorscale='viridis',
      contours=dict(
          x=dict(show=True, color='black', start=-1.5, end=1.5, size=0.1),
          y=dict(show=True, color='black', start=-1.5, end=1.5, size=0.1)
      )
  )])
  # Configuramos el diseño: Ejes y tamaño
  fig.update_layout(
      title=dict(
          text=titulo, # Aquí va tu título
          x=0.5, # Esto lo centra perfectamente en la gráfica
          font=dict(size=20) # Ajusta el tamaño de la letra
      ),
      scene = dict(
          xaxis_title=eje_x,
          yaxis_title=eje_y,
          zaxis_title=eje_z
      ),
      width=900,  # Ancho de la figura
      height=900, # Alto de la figura
      margin=dict(l=0, r=0, b=0, t=30) # Elimina los márgenes blancos extra (como un tight_layout)
  )

  # Mostramos la gráfica
  fig.show()

# Gráfica de curva de nivel x^2+y^2=1

def curve_level():
  # Definimos la matriz en RxR
  x_val = np.linspace(-1.5, 1.5, 100)
  y_val = np.linspace(-1.5, 1.5, 100)
  X, Y = np.meshgrid(x_val, y_val)
  def g(x,y):
    return x**2+y**2
  # Graficamos la curva de nivel g(x,y)=1
  #Creamos el área de la figura donde se hará la gráfica
  plt.figure(dpi=100, figsize=(10,10))
  plt.gca().set_axisbelow(True)
  plt.axhline(0,c='k')
  plt.axvline(0,c='k')
  plt.grid(linestyle='--')
  #Creamos la gráfica
  plt.contour(X,Y,g(X,Y),levels=[1], colors='r')
  plt.xlabel('$x$')
  plt.ylabel('$y$')
  plt.title('Curva de nivel $g(x,y)=1$\n')
  # Graficamos un vector de módulo 1
  plt.quiver(0, 0, np.cos(np.pi/4), np.sin(np.pi/4), angles='xy', scale_units='xy', scale=1, color='darkblue', width=0.005)
  plt.text(0.5,0.4,'$r=1$',c='darkblue',fontsize=12)
  # Mostramos la gráfica
  plt.show()

# Gráfica de mapa de contorno

def contour(x_val,y_val,g,niveles,
            titulo='Mapa de contorno para g(x,y)\n',eje_x='$x$',eje_y='$y$'):
  # Definimos una matriz de valores en RxR a graficar
  X,Y = np.meshgrid(x_val, y_val)
  Z = g(X,Y)

  #Creamos el área de la figura donde se hará la gráfica
  plt.figure(dpi=150, figsize=(6,6))
  plt.gca().set_axisbelow(True)
  plt.axhline(0,c='k')
  plt.axvline(0,c='k')
  plt.grid(linestyle='--')
  #Creamos las gráficas
  colores = plt.cm.Set1.colors[:]
  for n in range(len(niveles)):
      plt.contour(X,Y,g(X,Y),levels=[niveles[n]], colors=colores[n])
      plt.plot([], [], color=colores[n], label='g(x,y)=%.1f'%niveles[n])
  plt.xlabel(eje_x)
  plt.ylabel(eje_y)
  plt.title(titulo)
  plt.legend(facecolor='white', edgecolor='none',framealpha=1)
  # Mostramos la gráfica
  plt.show()

# Gráfica de isosuperficies dinámica

def isosurface(x_val,y_val,z_val,F,niveles,
               titulo="Isosuperficie Dinámica: F(x,y,z) = C",eje_x='x',eje_y='y',eje_z='z'):  
  # Matriz para graficar
  X, Y, Z = np.meshgrid(x_val, y_val, z_val)

  # 2. DEFINES TU FUNCIÓN AQUÍ (Ejemplo: Esfera)
  valores = F(X,Y,Z)

  # --- CONSTRUIMOS LA FIGURA ---
  fig = go.Figure()

  # CAPA ÚNICA: La isosuperficie inicial
  fig.add_trace(go.Isosurface(
      x=X.flatten(), y=Y.flatten(), z=Z.flatten(), value=valores.flatten(),
      isomin=niveles[0], isomax=niveles[0], # Forzamos a que sea una sola capa fina
      surface_count=1,
      showscale=False,
      colorscale='viridis',
      opacity=0.6,
      caps=dict(x_show=False, y_show=False, z_show=False) # Quita las "tapas" cuadradas
  ))

  # --- CREAMOS LOS FOTOGRAMAS (ANIMACIÓN DEL DESLIZADOR) ---
  frames = []
  for c in niveles:
      frames.append(go.Frame(
          name=str(c),
          data=[go.Isosurface(
              isomin=c,
              isomax=c  # Actualizamos el nivel de la superficie en cada fotograma
          )]
      ))
  fig.frames = frames

  # --- AGREGAMOS EL DESLIZADOR (SLIDER) ---
  sliders = [dict(
      active=0,
      currentvalue=dict(prefix='Nivel de la isosuperficie (C): '),
      pad=dict(t=50),
      steps=[dict(
          method='animate',
          args=[[str(c)], dict(mode='immediate', frame=dict(duration=0, redraw=True), transition=dict(duration=0))],
          label=f"{c:.2f}"
      ) for c in niveles]
  )]

  # --- CONFIGURAMOS EL DISEÑO Y LA CÁMARA ---
  fig.update_layout(
      sliders=sliders,
      scene=dict(
          xaxis_title=eje_x, yaxis_title=eje_y, zaxis_title=eje_z,
          # MUY IMPORTANTE: Fijamos los límites de la "caja" para que no haga zoom automático
          xaxis=dict(range=[-3, 3]),
          yaxis=dict(range=[-3, 3]),
          zaxis=dict(range=[-3, 3])
      ),
      width=800, height=800, margin=dict(l=0, r=0, b=0, t=50),
      title=dict(text=titulo, x=0.5, font=dict(size=20))
  )

  fig.show()
