import os
import json
import subprocess
import consistency_audit
import weight_mapper

LEADERBOARD_FILE = 'leaderboard.json'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    return {"best_time": 2.2, "miner_id": "Baseline", "material": "Graphite-Pd"}

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def show_menu():
    leaderboard = load_leaderboard()
    print("==========================================")
    print("   GRANDFATHER LEGACY: MASTER CONSOLE     ")
    print(f"   🏆 Record: {leaderboard['best_time']}s by {leaderboard['miner_id']}")
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
            print("\nLaunching Track A Physics Engine...")
            # Placeholder for future Casimir logic integration
        
        elif choice == '2':
            print("\nLaunching Track B Lattice Simulation...")
            subprocess.run(['python', 'lattice_sim.py'], shell=True)
            
        elif choice == '3':
            print("\nLaunching Track C Mathematical Auditor...")
            submission_file = 'submission.json'
            
            if os.path.exists(submission_file):
                with open(submission_file, 'r') as f:
                    sub = json.load(f)
                
                m_time = sub.get("loading_time")
                m_id = sub.get("miner_id")
                m_mat = sub.get("material")
                
                # Step A: Audit
                score = consistency_audit.run_physical_audit(None, m_time)
                
                # Step B: Weight Mapping
                weight = weight_mapper.calculate_tao_emission(score)
                
                # Step C: Leaderboard Check
                lb = load_leaderboard()
                if m_time < lb['best_time']:
                    print(f"\n🎊 NEW WORLD RECORD: {m_time}s!")
                    save_leaderboard({"best_time": m_time, "miner_id": m_id, "material": m_mat})
                
                print(f"\n[SUMMARY] Verified: {m_id} | Rank: {score} | Weight: {weight:.4f}")
            else:
                print(f"\n❌ Error: No submission.json found.")

        elif choice == '4':
            if os.path.exists('loading_kinetics.png'):
                os.startfile('loading_kinetics.png') if os.name == 'nt' else subprocess.run(['open', 'loading_kinetics.png'])
            else:
                print("\n❌ Error: No plot found.")

        elif choice == '5':
            break
        
        input("\nPress Enter to return to menu...")
        clear_screen()

if __name__ == "__main__":
    main()
