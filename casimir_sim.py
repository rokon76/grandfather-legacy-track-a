import numpy as np
import matplotlib.pyplot as plt

def calculate_casimir_pressure(dist_nm, lambda_p):
    """Calculates Casimir pressure based on plasma wavelength."""
    c = 3e8
    hbar = 1.054e-34
    dist_m = dist_nm * 1e-9
    # Simplified Lifshitz-type approximation for research
    pressure = (hbar * c * np.pi**2) / (240 * dist_m**4) * (lambda_p / (lambda_p + dist_m))
    return pressure

def main():
    print("--- Track A: Casimir Material Analysis ---")
    distances = np.linspace(5, 50, 100)
    
    # Expanded Material Library
    materials = {
        'Gold': 137e-9,
        'ITO': 200e-9,
        'Silicon': 310e-9,
        'Germanium': 400e-9,
        'Graphite': 600e-9
    }
    
    plt.figure(figsize=(10, 6))
    for name, lp in materials.items():
        pressures = [calculate_casimir_pressure(d, lp) for d in distances]
        plt.plot(distances, pressures, label=f"{name} (λp={lp*1e9:.0f}nm)")
        print(f"✅ Simulated {name} lattice profile.")

    plt.yscale('log')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Pressure (Pa)')
    plt.title('Casimir Pressure vs. Distance (Material Comparison)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    plt.savefig('casimir_comparison.png')
    print("\n[SUCCESS] Plot saved as casimir_comparison.png")

if __name__ == "__main__":
    main()
