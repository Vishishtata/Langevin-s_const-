# project

# H3+ Langevin Rate Calculator

A small but functional Python tool to calculate Langevin rate constants for ion-neutral reactions.

## Overview

This project calculates the Langevin rate constant (KL), which describes the collision rate between ions and neutral molecules. KL is widely used in astrochemistry to model reaction rates in interstellar clouds.

## Features

- Calculate KL for any ion-neutral pair.
- Accepts:
  - Ion charge (`charge_ion`)  
  - Polarizability of the neutral atom/molecule (`alpha`) in Å³  
  - Reduced mass of the ion-neutral system (`mu`) in amu
- Outputs KL in cm³/s.
- Modular function structure for easy integration into AI pipelines or simulation projects.

## Installation

1. Clone the repo:

git clone git clone https://github.com/Vishishtata/project.git
cd project

2. Run the calculator
    
python langevins_const.py

3. usage example

from langevins_const import calculate_langevin_rate

# Example: H3+ and H2
charge_ion = 1          # H3+ charge
alpha = 1.95            # H2 polarizability in Å³
mu = 0.667              # in amu

kl = 2 * math.pi * charge_ion * math.sqrt(alpha/mu) * 3.2e-10 
print(f"KL : {kl:.2e} cm³/s")

Expected output : 
 
 KL : 1.80e-09 cm³/s
