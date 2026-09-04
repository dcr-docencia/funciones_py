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
  delta_x=x_val.max()-x_val.min()
  delta_y=y_val.max()-y_val.min()
  # Graficamos la superficie en Plotly
  fig = go.Figure(data=[go.Surface(
      x=X, y=Y, z=Z,
      showscale=False,
      colorscale=color_escala,
      contours=dict(
          x=dict(show=True, color='black', start=x_val.min(), end=x_val.max(), size=0.03*delta_x),
          y=dict(show=True, color='black', start=y_val.min(), end=y_val.max(), size=0.03*delta_y)
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

#Gráficas dinámina de curvas de nivel proyectadas

def plot_curves(x_val,y_val,g,niveles,
                titulo='Gráfica dinámina de curvas de nivel proyectadas',eje_x='x',eje_y='y',eje_z='g(x,y)'):
  X, Y = np.meshgrid(x_val, y_val)
  Z = g(X,Y)
  delta_x=x_val.max()-x_val.min()
  delta_y=y_val.max()-y_val.min()

  # 3. Alturas del plano interactivo
  alturas = niveles

  # 4. EL TRUCO MAESTRO: Matplotlib calcula las curvas de nivel por nosotros en segundo plano
  curvas_x = []
  curvas_y = []
  fig_temp, ax_temp = plt.subplots() # Figura invisible temporal
  for c in niveles:
      cs = ax_temp.contour(X, Y, Z, levels=[c])
      x_frame, y_frame = [], []
      for seg in cs.allsegs[0]: # Extrae los polígonos exactos de la curva
          x_frame.extend(seg[:,0].tolist() + [np.nan]) # np.nan separa curvas desconectadas
          y_frame.extend(seg[:,1].tolist() + [np.nan])
      curvas_x.append(x_frame)
      curvas_y.append(y_frame)
  plt.close(fig_temp) # Cerramos la figura para que no moleste

  # --- CONSTRUIMOS LA FIGURA ---
  fig = go.Figure()

  # CAPA A: La superficie blanca con malla
  fig.add_trace(go.Surface(
      x=X, y=Y, z=Z,
      colorscale=[[0, 'white'], [1, 'white']], opacity=0.3, showscale=False,
      contours=dict(
          x=dict(show=True, color='gray', start=x_val.min(), end=x_val.max(), size=0.03*delta_x),
          y=dict(show=True, color='gray', start=y_val.min(), end=y_val.max(), size=0.03*delta_y)
      ),
      name='Superficie'
  ))

  # CAPA B: El plano móvil gris
  fig.add_trace(go.Surface(
      x=X, y=Y, z=np.ones_like(X) * alturas[0],
      colorscale=[[0, 'cyan'], [1, 'cyan']], opacity=0.2, showscale=False,
      name='Plano de corte'
  ))

  # CAPA C: La línea de intersección EN el plano (Roja)
  # Le damos la altura z correspondiente al corte
  z_surf = [alturas[0] if not np.isnan(x) else np.nan for x in curvas_x[0]]
  fig.add_trace(go.Scatter3d(
      x=curvas_x[0], y=curvas_y[0], z=z_surf,
      mode='lines', line=dict(color='red', width=6),

  ))

  # CAPA D: La curva proyectada EN EL PISO (Negra)
  # Forzamos la altura z a 0
  z_floor = [0 if not np.isnan(x) else np.nan for x in curvas_x[0]]
  fig.add_trace(go.Scatter3d(
      x=curvas_x[0], y=curvas_y[0], z=z_floor,
      mode='lines', line=dict(color='black', width=6),
      name='proyección'
  ))

  # --- FOTOGRAMAS (LA ANIMACIÓN) ---
  frames = []
  for i, c in enumerate(alturas):
      # En cada paso, la roja sube, la negra se queda en 0
      z_surf = [c if not np.isnan(x) else np.nan for x in curvas_x[i]]
      z_floor = [0 if not np.isnan(x) else np.nan for x in curvas_x[i]]

      frames.append(go.Frame(
          name=str(c),
          data=[
              go.Surface(), # A: La superficie no cambia
              go.Surface(z=np.ones_like(X) * c), # B: El plano sube
              go.Scatter3d(x=curvas_x[i], y=curvas_y[i], z=z_surf), # C: La curva roja se actualiza
              go.Scatter3d(x=curvas_x[i], y=curvas_y[i], z=z_floor) # D: La proyección se actualiza
          ]
      ))
  fig.frames = frames

  # --- DESLIZADOR ---
  sliders = [dict(
      active=0,
      currentvalue=dict(prefix='Niveles (z): '),
      pad=dict(t=50),
      steps=[dict(
          method='animate',
          args=[[str(c)], dict(mode='immediate', frame=dict(duration=0, redraw=True), transition=dict(duration=0))],
          label=f"{c:.2f}"
      ) for c in alturas]
  )]

  # --- DISEÑO ---
  fig.update_layout(
      showlegend=False,
      sliders=sliders,
      scene=dict(
          xaxis_title=eje_x, yaxis_title=eje_y, zaxis_title=eje_z,
          zaxis=dict(range=[0, g(X,Y).max()]) # Fijamos el piso en 0
      ),
      width=900, height=900, margin=dict(l=0, r=0, b=0, t=50),
      title=dict(text=titulo, x=0.5, font=dict(size=20))
  )

  fig.show()

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
  colores = plt.cm.tab20.colors[:]
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
