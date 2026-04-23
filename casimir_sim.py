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
    
    # Mitigation Material Library
    plasma_wavelengths = {
        'gold': 137e-9,      # Research Baseline
        'silicon': 310e-9,   # Semiconductor Mitigation
        'graphite': 600e-9   # Maximum Structural Stability
    }
    
    lp = plasma_wavelengths.get(material, 0)
    if lp == 0: return p_ideal
    
    eta = 1 / (1 + (lp / d))
    return p_ideal * eta

def main():
    distances = np.linspace(5, 100, 200)
    materials = ['gold', 'silicon', 'graphite']
    colors = ['#d4af37', '#4a90e2', '#2c3e50'] # Gold, Blue, Charcoal
    
    print("--- Track A: Force Mitigation Analysis ---")
    print(f"{'Dist (nm)':<10} | {'Gold (Pa)':<15} | {'Silicon (Pa)':<15} | {'Graphite (Pa)':<15}")
    print("-" * 65)
    
    for d in [5, 10, 50]:
        row = [calculate_casimir_pressure(d, m) for m in materials]
        print(f"{d:<10} | {row[0]:<15.2e} | {row[1]:<15.2e} | {row[2]:<15.2e}")

    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 6))
    for m, color in zip(materials, colors):
        p_real = [calculate_casimir_pressure(d, m) for d in distances]
        plt.plot(distances, np.abs(p_real), color=color, linewidth=2, label=m.capitalize())
    
    plt.yscale('log')
    plt.title('Casimir Pressure: Structural Mitigation Strategy')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    
    output_file = "casimir_mitigation_compare.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: Mitigation plot saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
