import os
import subprocess
import weight_mapper  # Phase 2 Integration

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
            subprocess.run(['python', 'casimir_sim.py'], shell=True)
        
        elif choice == '2':
            print("\nLaunching Track B Lattice Simulation...")
            # This triggers the kinetics and saves the .png
            subprocess.run(['python', 'lattice_sim.py'], shell=True)
            
        elif choice == '3':
            print("\nLaunching Track C Mathematical Auditor...")
            # We import and run the audit logic
            import consistency_audit
            
            # For this Phase 2 test, we use the Ni-Pd Alloy record (2.00s)
            miner_time = 2.00 
            score = consistency_audit.run_physical_audit(None, miner_time)
            
            # --- PHASE 2 INTEGRATION ---
            print("\n--- Phase 2: Tokenomic Payout ---")
            weight = weight_mapper.calculate_tao_emission(score)
            
            print(f"\n[SUMMARY] Submission Verified.")
            print(f"RANK: {score} | WEIGHT: {weight:.4f}")
            print("------------------------------------------")

        elif choice == '4':
            plot_path = 'loading_kinetics.png'
            if os.path.exists(plot_path):
                print(f"\nOpening {plot_path}...")
                os.startfile(plot_path) if os.name == 'nt' else subprocess.run(['open', plot_path])
            else:
                print("\n❌ Error: No plot found. Run Option 2 first.")

        elif choice == '5':
            print("\nShutting down Grandfather Legacy console. Goodbye.")
            break
        
        else:
            print("\n❌ Invalid selection. Please try again.")
        
        input("\nPress Enter to return to menu...")
        clear_screen()

if __name__ == "__main__":
    main()
