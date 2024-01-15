# pylint: skip-file
# Konstanter
m   = 6.64e-27      # Masse til alfapartikkelen, kg
q_1 = 3.20e-19      # Ladning 1 [C]
q_2 = 1.26e-17      # Ladning 2 [C]

k_e = 8.99e9        # Coloumbkonstanten

# Startverdier
r = -1.0e-10
v = 1.5e7
t = 0

# Simulering av bevegelsen
delta_t = 1.0e-22

while v > 0:
    a = (-k_e * q_1 * q_2) / (m * r**2)
    v += a * delta_t
    r += v * delta_t
    t += delta_t

print(f'Alfapartikkelen snur ved r = {r:.2e} m (etter {t:.2e} s)')
