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
    
   # Material-specific Plasma Wavelengths (lambda_p) in meters
    plasma_wavelengths = {
        'silver': 130e-9,    # Maximum crushing force
        'aluminum': 80e-9,    # Very high force (UV reflector)
        'gold': 137e-9,      # Baseline
        'titanium': 250e-9,  # Mid-range
        'silicon': 310e-9,   # Semiconductor (reduced force)
        'germanium': 400e-9, # Low force
        'graphite': 600e-9   # Minimum structural force
    }
    
    lp = plasma_wavelengths.get(material, 0)
    if lp == 0: return p_ideal
    
    # Finite Conductivity Correction Factor
    eta = 1 / (1 + (lp / d))
    return p_ideal * eta

def main():
    distances = np.linspace(5, 100, 200)
    materials = ['silver', 'gold', 'silicon']
    colors = ['#C0C0C0', '#d4af37', '#4a90e2'] # Silver, Gold, Blue
    
    print("--- Track A: Multi-Material Casimir Analysis ---")
    print(f"{'Dist (nm)':<10} | {'Silver (Pa)':<12} | {'Gold (Pa)':<12} | {'Silicon (Pa)':<12}")
    print("-" * 55)
    
    for d in [5, 10, 50]:
        row = [calculate_casimir_pressure(d, m) for m in materials]
        print(f"{d:<10} | {row[0]:<12.2e} | {row[1]:<12.2e} | {row[2]:<12.2e}")

    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 6))
    for m, color in zip(materials, colors):
        p_real = [calculate_casimir_pressure(d, m) for d in distances]
        plt.plot(distances, np.abs(p_real), color=color, linewidth=2, label=m.capitalize())
    
    plt.yscale('log')
    plt.title('Casimir Pressure: Material Comparison (Ag vs Au vs Si)')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    
    output_file = "casimir_material_compare.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: Comparison plot saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
