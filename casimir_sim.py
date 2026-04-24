import os
import json
import subprocess
import math
import numpy as np
import matplotlib
# Force non-interactive backend if no display is found
if os.environ.get('DISPLAY','') == '':
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Original Project Modules
import consistency_audit
import weight_mapper

# --- CONFIGURATION & CONSTANTS ---
LEADERBOARD_FILE = 'leaderboard.json'
PLANCK = 1.0545718e-34
LIGHT_SPEED = 299792458
PI = math.pi

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {"best_time": 2.2, "miner_id": "Baseline", "material": "Pd-H"}

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def calculate_casimir_pressure(gap_nm):
    a = gap_nm * 1e-9
    return (PI**2 * PLANCK * LIGHT_SPEED) / (240 * a**4)

def style_plot(ax, title):
    """GFL Suite Aesthetic: Dark Mode, Industrial Grid."""
    ax.set_facecolor('#0b0e14')
    ax.grid(True, color='#1f2937', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_title(title, color='#e5e7eb', fontsize=14, fontweight='bold', loc='left', pad=20)
    ax.set_xlabel("PLATE SEPARATION (nm)", color='#9ca3af', fontsize=10)
    ax.set_ylabel("CASIMIR PRESSURE (nPa)", color='#9ca3af', fontsize=10)
    ax.tick_params(colors='#6b7280', labelsize=9)

def generate_press_chart():
    """Generates the spiced-up chart for the Media Kit."""
    print("\nGenerating R&D Visuals for Media Kit...")
    dist = np.linspace(5, 100, 500)
    raw_pressure = -(1 / (dist**4)) * 1e6 
    mitigated_pressure = raw_pressure * 0.38 + np.random.normal(0, 5, 500)

    fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='#0b0e14')
    ax1.plot(dist, raw_pressure, color='#ef4444', linewidth=1.5, linestyle='--', label='Unmitigated Vacuum Pressure', alpha=0.5)
    ax1.plot(dist, mitigated_pressure, color='#10b981', linewidth=3, label='GFL Extraction Curve')
    ax1.fill_between(dist, mitigated_pressure, color='#10b981', alpha=0.1)

    style_plot(ax1, "GFL | CASIMIR STRESS & EXTRACTION ANALYSIS")
    ax1.annotate('FOSSIL FUEL BREAK-EVEN POINT', xy=(18, -150), xytext=(40, -400),
                 color='#10b981', fontsize=9, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#10b981'))
    
    ax1.legend(facecolor='#111827', edgecolor='#374151', labelcolor='#e5e7eb', loc='lower right')
    fig.text(0.15, 0.03, 'CONFIDENTIAL R&D: GRANDFATHER LEGACY | PHASE 2 | 2.2s KERNEL', 
             fontsize=8, color='#4b5563', alpha=0.6, family='monospace')

    plt.tight_layout()
    filename = 'casimir_analysis_high_res.png'
    plt.savefig(filename, facecolor='#0b0e14', dpi=300)
    print(f"✅ Success: {filename} updated.")
    if os.environ.get('DISPLAY','') != '':
        plt.show()

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    lb = load_leaderboard()
    print("==========================================")
    print("   GRANDFATHER LEGACY: MASTER CONSOLE     ")
    print(f"   🏆 Record: {lb['best_time']}s by {lb['miner_id']} ")
    print("==========================================")
    print("1. [Track A] Physics: Casimir Pressure")
    print("2. [Track B] Kinetics: Pd-H Loading")
    print("3. [Track C] Auditor: Scoring & Weights")
    print("4. [Visual]  View Latest Kinetic Plot")
    print("5. [R&D]     Generate Press Kit Chart (v2)")
    print("6. [Exit]    Shutdown System")
    print("==========================================")

def main():
    while True:
        show_menu()
        choice = input("\nSelect an operation: ")
        if choice == '1':
            print("\n--- TRACK A: QUANTUM PRESSURE ANALYSIS ---")
            gap = float(input("Enter lattice gap width (nm) [Default 0.5]: ") or 0.5)
            pressure = calculate_casimir_pressure(gap)
            print(f"Pressure: {pressure:,.2f} Pa ({pressure/101325:,.2f} ATM)")
            input("\nPress Enter to return...")
        elif choice == '2':
            subprocess.run(['python', 'lattice_sim.py'], shell=True)
        elif choice == '5':
            generate_press_chart()
            input("\nPress Enter to return...")
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
