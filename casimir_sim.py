import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def calculate_casimir_pressure(distance_nm, material='gold'):
    h_bar = 1.0545718e-34 
    c = 2.99792458e8       
    d = distance_nm * 1e-9 
    p_ideal = -(np.pi**2 * h_bar * c) / (240 * d**4)
    
    # Expanded Mitigation Library
    plasma_wavelengths = {
        'gold': 137e-9,      # Baseline
        'ito': 200e-9,       # Tunable Conductor
        'silicon': 310e-9,   # Semiconductor
        'germanium': 400e-9, # High-index Semiconductor
        'graphite': 600e-9   # Max Structural Stability
    }
    
    lp = plasma_wavelengths.get(material, 0)
    if lp == 0: return p_ideal
    
    eta = 1 / (1 + (lp / d))
    return p_ideal * eta

def main():
    distances = np.linspace(5, 50, 100)
    materials = ['gold', 'ito', 'silicon', 'germanium', 'graphite']
    colors = ['#d4af37', '#27ae60', '#4a90e2', '#e67e22', '#2c3e50'] 
    
    print("--- Track A: Advanced Mitigation Analysis ---")
    print(f"{'Dist (nm)':<10} | {'Gold (Pa)':<12} | {'ITO (Pa)':<12} | {'Germ (Pa)':<12} | {'Graph (Pa)':<12}")
    print("-" * 75)
    
    for d in [5, 10, 25]:
        row = [calculate_casimir_pressure(d, m) for m in materials]
        print(f"{d:<10} | {row[0]:<12.2e} | {row[1]:<12.2e} | {row[3]:<12.2e} | {row[4]:<12.2e}")

    plt.figure(figsize=(10, 6))
    for m, color in zip(materials, colors):
        p_real = [calculate_casimir_pressure(d, m) for d in distances]
        plt.plot(distances, np.abs(p_real), color=color, linewidth=2, label=m.upper())
    
    plt.yscale('log')
    plt.title('Casimir Stress Mitigation: Advanced Materials')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    
    plt.savefig("casimir_advanced_compare.png")
    print(f"\n✅ SUCCESS: Plot saved to: {os.path.abspath('casimir_advanced_compare.png')}")

if __name__ == "__main__":
    main()
