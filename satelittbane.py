# pylint: skip-file
import numpy as np
import matplotlib.pyplot as plt

# Konstanter
m = 100           # masse satellitt, kg
M = 5.972e24      # masse av jorda, kg
gamma = 6.67e-11  # gravitasjonskonstanten, Nm^2/kg^2 (IKKE ENDRE)

# Startverdier
r = np.array([4e7, 0])    # posisjonen til satellitten, m
v = np.array([0, 2.4e3])  # farten til satellitten, m/s
t = 0                  # tid, s

# Liste for lagring av verdier
r_liste = [r]  # liste med posisjoner

# Variable krefter, beregning av kraftsum og akselerasjon
def akselerasjon(r):
  G_abs = gamma*m*M/np.linalg.norm(r)**2  # absoluttverdi gravitasjon, N
  e_r = -r/np.linalg.norm(r)              # enhetsvektor mot sentrum av jorda
  G = G_abs*e_r                 # gravitasjonskraft med riktig retning
  aks = G/m                     # akselerasjon, m/s^2
  return aks

# Simulerer bevegelsen så lenge det ikke har gått 1*10^5 s
# og banen er over jordoverflaten.
dt = 10  # tidssteg, s

while t < 1e5 and np.linalg.norm(r) > 6.371e6:
  a = akselerasjon(r)  # beregner akselerasjon
  v = v + a*dt         # beregner ny fart
  r = r + v*dt         # beregner ny posisjon
  t = t + dt           # ny tid

  #Lagring av 2D-verdier
  r_liste = np.concatenate([r_liste, [r]])

# Tegner graf
plt.axis("equal")                            # like akser
plt.title("Satellittbane")                   # tittel
plt.xlabel("$x$ / m")                        # navn på x-aksen
plt.ylabel("$y$ / m")                        # navn på y-aksen
plt.gca().add_artist(plt.Circle((0,0), 6.37e6))  # sirkel som viser jorda
plt.plot(r_liste[:,0], r_liste[:,1])         # plotter posisjonen
plt.show()                                   # viser grafen