import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def calculate_casimir_pressure(distance_nm, material='gold'):
    """
    Calculates Casimir Pressure with a correction for Finite Conductivity.
    """
    h_bar = 1.0545718e-34 
    c = 2.99792458e8       
    d = distance_nm * 1e-9 
    
    # Ideal Pressure
    p_ideal = -(np.pi**2 * h_bar * c) / (240 * d**4)
    
    # Finite Conductivity Correction (Plasma Wavelength of Gold ~137nm)
    # This is a simplified correction factor for real-world metals
    lambda_p = 137e-9 
    eta = 1 / (1 + (lambda_p / d))
    
    return p_ideal * eta

def main():
    distances = np.linspace(5, 100, 200)
    p_ideal = [calculate_casimir_pressure(d, material='ideal') / (1 / (1 + (137e-9 / (d*1e-9)))) for d in distances]
    p_real = [calculate_casimir_pressure(d, material='gold') for d in distances]
    
    print("--- Track A: Refined Casimir Analysis (Gold) ---")
    print(f"{'Distance (nm)':<15} | {'Ideal (Pa)':<15} | {'Real (Pa)':<15}")
    print("-" * 50)
    
    for d in [5, 10, 50]:
        real = calculate_casimir_pressure(d)
        ideal = real / (1 / (1 + (137e-9 / (d*1e-9))))
        print(f"{d:<15} | {ideal:<15.2e} | {real:<15.2e}")

    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 6))
    plt.plot(distances, np.abs(p_ideal), 'k--', alpha=0.5, label='Theoretical Ideal')
    plt.plot(distances, np.abs(p_real), color='#d4af37', linewidth=2, label='Gold (Finite Conductivity)')
    
    plt.yscale('log')
    plt.title('Casimir Pressure: Ideal vs. Real-World Gold')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.legend()
    
    output_file = "casimir_refined.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: Refined plot saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
