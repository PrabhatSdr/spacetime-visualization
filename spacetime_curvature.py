import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LightSource
from matplotlib.cm import get_cmap

##FIGURE SETUP
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("black")

##SPACETIME FABRIC
N = 80
x = np.linspace(-8, 8, N)
y = np.linspace(-8, 8, N)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2) + 1e-3
Z = -2.0 / np.sqrt(R)  
Z = np.clip(Z, -2.5, 0.5) 
Z_flat = np.where(R < 1.0, -2.5, Z)  

ls = LightSource(azdeg=30, altdeg=60)
cmap_fabric = get_cmap('inferno')
rgb = ls.shade(Z_flat, cmap=cmap_fabric, vert_exag=1.0, blend_mode='overlay')

fabric_surface = ax.plot_surface(
    X, Y, Z_flat,
    facecolors=rgb,
    alpha=0.85,
    linewidth=0,
    antialiased=True,
    shade=True
)
fabric_surface.set_edgecolor('none')

##SUN
phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:60j]
sun_radius = 1.2 

x_sun = sun_radius * np.sin(phi) * np.cos(theta)
y_sun = sun_radius * np.sin(phi) * np.sin(theta)
z_sun = sun_radius * np.cos(phi)

I = (np.sin(phi) - np.sin(phi).min()) / (np.sin(phi).max() - np.sin(phi).min())
sun_colors = plt.cm.afmhot(0.5 + 0.5 * I)

ax.plot_surface(
    x_sun, y_sun, z_sun,
    facecolors=sun_colors,
    linewidth=0,
    antialiased=True,
    shade=True,
    alpha=1.0
)

#Glow
glow_radius = 1.8
x_glow = glow_radius * np.sin(phi) * np.cos(theta)
y_glow = glow_radius * np.sin(phi) * np.sin(theta)
z_glow = glow_radius * np.cos(phi)

glow_colors = np.ones((*x_glow.shape, 4))
glow_colors[..., 0] = 1.0
glow_colors[..., 1] = 0.8
glow_colors[..., 2] = 0.4
glow_colors[..., 3] = 0.15

ax.plot_surface(
    x_glow, y_glow, z_glow,
    facecolors=glow_colors,
    alpha=0.2,
    linewidth=0,
    antialiased=True
)

## PLANET
orbit_radius = 5.0
planet_radius = 0.4

phi_p, theta_p = np.mgrid[0:np.pi:15j, 0:2*np.pi:30j]
x_p0 = planet_radius * np.sin(phi_p) * np.cos(theta_p)
y_p0 = planet_radius * np.sin(phi_p) * np.sin(theta_p)
z_p0 = planet_radius * np.cos(phi_p)

planet_colors = plt.cm.cool((phi_p / np.pi) * 0.5 + 0.5)
planet_surface = [ax.plot_surface(
    x_p0 + orbit_radius, y_p0, z_p0,
    facecolors=planet_colors,
    linewidth=0,
    antialiased=True
)]


(planet_dot,) = ax.plot([orbit_radius], [0], [0], 'o', color='deepskyblue', markersize=10)

# Orbit path (ring)
theta_orbit = np.linspace(0, 2*np.pi, 200)
x_orbit = orbit_radius * np.cos(theta_orbit)
y_orbit = orbit_radius * np.sin(theta_orbit)
z_orbit = np.zeros_like(theta_orbit)
ax.plot(x_orbit, y_orbit, z_orbit, color="deepskyblue", linestyle="--", linewidth=1.5, alpha=0.6)

##LIGHT RAY
b = 3.0  # Light ray further from sun
x_light = np.linspace(-8, 8, 300)
y_light = np.full_like(x_light, b)
z_light = -1.0 * b / (x_light**2 + b**2 + 0.2)
ax.plot(x_light, y_light, z_light, color="white", linewidth=2.5, alpha=0.9)

def update(frame):
    ax.view_init(elev=30, azim=frame)

    # Planet motion - orbit around the sun
    t = np.radians(frame * 3) 
    x_c, y_c, z_c = orbit_radius * np.cos(t), orbit_radius * np.sin(t), 0.0

    global planet_surface
    for surf in planet_surface:
        surf.remove()
    planet_surface[:] = [ax.plot_surface(
        x_p0 + x_c, y_p0 + y_c, z_p0 + z_c, 
        facecolors=planet_colors,
        linewidth=0,
        antialiased=True
    )]

    planet_dot.set_data([x_c], [y_c])
    planet_dot.set_3d_properties([z_c])

    return planet_surface + [planet_dot]

ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 120),
                    interval=50, blit=False, repeat=True)

##AXIS SETTINGS
ax.set_xlim([-8, 8])
ax.set_ylim([-8, 8])
ax.set_zlim([-2.8, 2.0])
ax.set_box_aspect([1, 1, 1]) 
ax.set_axis_off()

plt.suptitle("Spacetime Curvature with Orbiting Planet",
             color="white", fontsize=16, weight="bold", y=0.92)

plt.show()