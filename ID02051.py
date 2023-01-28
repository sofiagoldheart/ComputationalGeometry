import matplotlib.pyplot as plt

# Crear el plano cartesiano y establacer dimensiones.
ancho = 10
alto = 10
fig, ax = plt.subplots(figsize=(ancho, alto))

# Dibujar cuadricula
ax.grid(which='both', color='silver', linewidth=1, linestyle='-', alpha=0.2)

# Línea de eje vertical color azul:
ax.axhline(y=0, color='blue', linewidth=2)
# Flecha de eje vertical color cyan:
arrow_y = dict(markersize=8, color='cyan', clip_on=False)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_y)
# Línea de eje horizontal color rojo:
ax.axvline(x=0, color='red', linewidth=2)
# Flecha de eje horizontal color naranja:
arrow_x = dict(markersize=8, color='orange', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_x)

ax.xaxis.set_tick_params(which='both', direction='in', labelsize=15)
ax.yaxis.set_tick_params(which='both', direction='in', labelsize=15)

# Incrementa en 5 unidades en cada cuadrante y utiliza marcas a cada 0.5 de unidad.
ax.xaxis.set_ticks(range(-20, 21, 5))
ax.yaxis.set_ticks(range(-20, 21, 5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))

# Nombra el eje vertical como alpha y el eje horizontal como beta.
#Incrementa la letra de los ejes a 20.
ax.set_xlabel(r'$\alpha$', fontsize=20)
ax.set_ylabel(r'$\beta$', fontsize=20)


# Mostrar el plano cartesiano
plt.show()
