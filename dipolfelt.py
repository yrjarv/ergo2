# pylint: skip-file
import numpy as np
# Konstanter
q1 = 2e-9                       # Ladning til kule 1 [C]
P1 = np.array([-0.05, 0])       # Posisjoner til kule 1 [m]
q2 = -2e-9                      # Ladning til kule 2 [C]
P2 = np.array([0.05, 0])        # Posisjoner til kule 2 [m]
k = 8.99e9                      # Coloumbkonstanten

# Elektrisk felt
def E_felt(r):
    r1 = r - P1                                     # vektor fra P1 til r
    r1_enhet = r1/np.linalg.norm(r1)                # enhetsvektor fra P1
    E1 = k*q1/np.linalg.norm(r1)**2 * r1_enhet      # elektrisk felt fra kule 1
    r2 = r - P2                                     # vektor fra P2 til r
    r2_enhet = r2/np.linalg.norm(r2)                # enhetsvektor fra P2
    E2 = k*q2/np.linalg.norm(r2)**2 * r2_enhet      # elektrisk felt fra kule 2
    E = E1 + E2                                     # summerer feltene
    return E

# Beregning
punkt = np.array([0, 0.10])
E = E_felt(punkt)

print(f'Elektrisk feltstyrke i {punkt}: E = {E} V/m')
print(f'Absoluttverdi for E: |E| = {np.linalg.norm(E)} V/m')
print(f'Vinkel mellom feltretning og x-akse: {np.arctan2(E[1],E[0])} radianer')
