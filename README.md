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

git clone https://github.com/Vishishtata/project.git
cd project
