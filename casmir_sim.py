import numpy as np
import matplotlib
matplotlib.use('Agg') # Ensuring compatibility with your local C:\gfl environment
import matplotlib.pyplot as plt
import os

def calculate_casimir_pressure(distance_nm):
    """
    Calculates Casimir Pressure (Pc) for parallel ideal plates.
    Formula: Pc = -(pi^2 * h_bar * c) / (240 * d^4)
    """
    h_bar = 1.0545718e-34  # Reduced Planck constant (J*s)
    c = 2.99792458e8       # Speed of light (m/s)
    
    # Convert nanometers to meters
    d = distance_nm * 1e-9
    
    # Casimir Pressure in Pascals (N/m^2)
    pressure = -(np.pi**2 * h_bar * c) / (240 * d**4)
    return pressure

def main():
    # Range of distances from 10nm to 100nm
    distances = np.linspace(10, 100, 100)
    pressures = [calculate_casimir_pressure(d) for d in distances]
    
    print("--- Track A: Casimir QED Analysis ---")
    print(f"{'Distance (nm)':<15} | {'Pressure (Pa)':<15}")
    print("-" * 35)
    
    # Print a few key data points
    for d in [10, 20, 50, 100]:
        p = calculate_casimir_pressure(d)
        print(f"{d:<15} | {p:<15.2e}")

    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 6))
    plt.plot(distances, np.abs(pressures), color='#8e44ad', linewidth=2)
    plt.yscale('log') # Pressure scales by d^-4, so log scale is best
    plt.title('Casimir Attraction vs. Plate Distance (Log Scale)')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Magnitude of Pressure (Pa)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    output_file = "casimir_analysis.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: Casimir plot saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
