import math

charge_ion = float(input("Enter the elementarycharge on ion (eg 1 for +1) : ")) 
alpha = float(input("Enter the polarizability of neutral atom (Å³, e.g., 1.95) : ")) 
mu = float(input("Enter the reduced mass of ion-neutral system (amu, e.g., 2.32): ")) 

kl = 2 * math.pi * charge_ion * math.sqrt(alpha/mu) * 3.2e-10 
print(f"KL : {kl:.2e} cm³/s")