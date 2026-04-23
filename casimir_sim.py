import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def calculate_casimir_pressure(distance_nm):
    """
    Calculates Casimir Pressure (Pc) for parallel ideal plates.
    """
    h_bar = 1.0545718e-34  # Reduced Planck constant
    c = 2.99792458e8       # Speed of light
    d = distance_nm * 1e-9 # Convert nm to meters
    
    # Pc = -(pi^2 * h_bar * c) / (240 * d^4)
    pressure = -(np.pi**2 * h_bar * c) / (240 * d**4)
    return pressure

def main():
    # NEW RANGE: 5nm to 50nm for higher resolution at close proximity
    distances = np.linspace(5, 50, 100)
    pressures = [calculate_casimir_pressure(d) for d in distances]
    
    print("--- Track A: High-Resolution Casimir Analysis ---")
    print(f"{'Distance (nm)':<15} | {'Pressure (Pa)':<15}")
    print("-" * 35)
    
    for d in [5, 10, 25, 50]:
        p = calculate_casimir_pressure(d)
        print(f"{d:<15} | {p:<15.2e}")

    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 6))
    plt.plot(distances, np.abs(pressures), color='#8e44ad', linewidth=2, label='Ideal Casimir Force')
    plt.yscale('log')
    plt.title('Casimir Pressure: 5nm to 50nm (High Resolution)')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.axvspan(5, 10, color='red', alpha=0.1, label='Critical Stress Zone')
    plt.legend()
    
    output_file = "casimir_analysis_high_res.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: High-res plot saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
