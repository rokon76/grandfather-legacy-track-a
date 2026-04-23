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
    
    # Expanded Material Library
    plasma_wavelengths = {
        'silver': 130e-9,    # Maximum crushing force
        'gold': 137e-9,      # Baseline
        'silicon': 310e-9,   # Reduced force
        'graphite': 600e-9   # Minimum structural force (Longer lambda_p)
    }
    
    lp = plasma_wavelengths.get(material, 0)
    if lp == 0: return p_ideal
    
    # Finite Conductivity Correction Factor
    eta = 1 / (1 + (lp / d))
    return p_ideal * eta

def main():
    distances = np.linspace(5, 100, 200)
    materials = ['silver', 'gold', 'silicon', 'graphite']
    colors = ['#C0C0C0', '#d4af37', '#4a90e2', '#2c3e50'] # Silver, Gold, Blue, Charcoal
    
    print("--- Track A: Multi-Material Casimir Analysis ---")
    print(f"{'Dist (nm)':<10} | {'Silver (Pa)':<12} | {'Gold (Pa)':<12} | {'Graphite (Pa)':<12}")
    print("-" * 65)
    
    for d in [5, 10, 50]:
        row = [calculate_casimir_pressure(d, m) for m in materials]
        # Printing Silver, Gold, and Graphite for the direct comparison
        print(f"{d:<10} | {row[0]:<12.2e} | {row[1]:<12.2e} | {row[3]:<12.2e}")

    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 6))
    for m, color in zip(materials, colors):
        p_real = [calculate_casimir_pressure(d, m) for d in distances]
        plt.plot(distances, np.abs(p_real), color=color, linewidth=2, label=m.capitalize())
    
    plt.yscale('log')
    plt.title('Casimir Pressure: Structural Force Mitigation (Ag vs Au vs Si vs C)')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    
    output_file = "casimir_material_compare.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: Multi-material plot saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
