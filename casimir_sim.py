import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def calculate_casimir_pressure(distance_nm):
    h_bar = 1.0545718e-34  
    c = 2.99792458e8       
    d = distance_nm * 1e-9
    pressure = -(np.pi**2 * h_bar * c) / (240 * d**4)
    return pressure

def main():
    distances = np.linspace(10, 100, 100)
    pressures = [calculate_casimir_pressure(d) for d in distances]
    
    print("--- Track A: Casimir QED Analysis ---")
    for d in [10, 20, 50, 100]:
        p = calculate_casimir_pressure(d)
        print(f"{d}nm | {p:.2e} Pa")

    plt.figure(figsize=(10, 6))
    plt.plot(distances, np.abs(pressures), color='#8e44ad', linewidth=2)
    plt.yscale('log')
    plt.title('Casimir Attraction vs. Plate Distance')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    plt.savefig("casimir_analysis.png")
    print(f"\n✅ SUCCESS: Casimir plot saved.")

if __name__ == "__main__":
    main()
