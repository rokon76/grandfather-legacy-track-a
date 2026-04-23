import os
import json
import subprocess
import consistency_audit
import weight_mapper

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("==========================================")
    print("   GRANDFATHER LEGACY: MASTER CONSOLE     ")
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
            print("Running Casimir pressure gradients...")
        
        elif choice == '2':
            print("\nLaunching Track B Lattice Simulation...")
            subprocess.run(['python', 'lattice_sim.py'], shell=True)
            
        elif choice == '3':
            print("\nLaunching Track C Mathematical Auditor...")
            
            # --- NEW AUTOMATED FILE READING LOGIC ---
            submission_file = 'submission.json'
            
            if os.path.exists(submission_file):
                with open(submission_file, 'r') as f:
                    data = json.load(f)
                
                miner_time = data.get("loading_time")
                miner_id = data.get("miner_id")
                
                print(f"📂 Found submission from {miner_id} ({miner_time}s)")
                
                # Step A: Audit the score
                score = consistency_audit.run_physical_audit(None, miner_time)
                
                # Step B: Map to TAO Weight
                print("\n--- Phase 2: Tokenomic Payout ---")
                weight = weight_mapper.calculate_tao_emission(score)
                
                print(f"\n[SUMMARY] Submission Verified.")
                print(f"RANK: {score} | WEIGHT: {weight:.4f}")
            else:
                print(f"\n❌ Error: No '{submission_file}' found.")
                print("Please run 'python miner_template.py' first to generate a result.")
            # ------------------------------------------

        elif choice == '4':
            plot_path = 'loading_kinetics.png'
            if os.path.exists(plot_path):
                print(f"\nOpening {plot_path}...")
                if os.name == 'nt': os.startfile(plot_path)
                else: subprocess.run(['open', plot_path])
            else:
                print("\n❌ Error: No plot found. Run Option 2 first.")

        elif choice == '5':
            print("\nShutting down Grandfather Legacy console. Goodbye.")
            break
        
        input("\nPress Enter to return to menu...")
        clear_screen()

if __name__ == "__main__":
    main()
