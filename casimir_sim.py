import os
import json
import subprocess
import math
import consistency_audit
import weight_mapper

# --- CONFIGURATION ---
LEADERBOARD_FILE = 'leaderboard.json'
PLANCK = 1.0545718e-34
LIGHT_SPEED = 299792458
PI = math.pi

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except: pass
    return {"best_time": 2.2, "miner_id": "Baseline", "material": "Pd-H"}

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def calculate_casimir_pressure(gap_nm):
    a = gap_nm * 1e-9
    return (PI**2 * PLANCK * LIGHT_SPEED) / (240 * a**4)

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    lb = load_leaderboard()
    print("==========================================")
    print("   GRANDFATHER LEGACY: MASTER CONSOLE     ")
    print(f"   🏆 Record: {lb['best_time']}s by {lb['miner_id']}")
    print("==========================================")
    print("1. [Track A] Physics: Casimir Pressure")
    print("2. [Track B] Kinetics: Pd-H Loading")
    print("3. [Track C] Auditor: Scoring & Weights")
    print("4. [Visual]  View Latest Kinetic Plot")
    print("5. [Exit]    Shutdown System")
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
        
        elif choice == '2':
            print("\nLaunching Track B Simulation...")
            subprocess.run(['python', 'lattice_sim.py'], shell=True)
            
        elif choice == '3':
            print("\nLaunching Track C Auditor...")
            if os.path.exists('submission.json'):
                try:
                    with open('submission.json', 'r', encoding='utf-8') as f:
                        sub = json.load(f)
                    
                    m_time = sub.get("loading_time")
                    m_gap = sub.get("lattice_gap", 0.5)
                    m_id = sub.get("miner_id", "Unknown")

                    # Perform Physics-Based Audit
                    score = consistency_audit.run_physical_audit(None, m_time, m_gap)
                    
                    if score == -1:
                        print(f"\n❌ AUDIT FAILURE: Physical Inconsistency detected!")
                        print(f"Miner {m_id} claimed {m_time}s with {m_gap}nm gap. Rejected.")
                    elif score > 0:
                        weight = weight_mapper.calculate_tao_emission(score)
                        lb = load_leaderboard()
                        if m_time < lb['best_time']:
                            print(f"\n🎊 NEW WORLD RECORD: {m_time}s!")
                            save_leaderboard({"best_time": m_time, "miner_id": m_id, "material": sub.get("material")})
                        print(f"\n[SUMMARY] Verified: {m_id} | Score: {score:.2f} | Weight: {weight:.4f}")
                    else:
                        print("\n⚠️ Submission did not beat the 2.2s benchmark.")
                except Exception as e:
                    print(f"❌ Error reading submission: {e}")
            else:
                print("\n❌ Error: No submission.json found.")
                
        elif choice == '4':
            if os.path.exists('loading_kinetics.png'):
                os.startfile('loading_kinetics.png')
            else: print("\n❌ No plot found.")
                
        elif choice == '5': break
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
