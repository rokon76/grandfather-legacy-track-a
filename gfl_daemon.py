import bittensor as bt
import time
import os

# Configuration
WALLET_NAME = 'gfl_vault'
HOTKEY_NAME = 'gfl_worker'
CHECK_INTERVAL = 300  # Check every 5 minutes

def housekeeping():
    print(f"--- GFL Daemon Heartbeat: {time.ctime()} ---")
    try:
        wallet = bt.Wallet(name=WALLET_NAME, hotkey=HOTKEY_NAME)
        subtensor = bt.Subtensor(network='finney')
        
        # 1. Network Check
        balance = subtensor.get_balance(wallet.coldkeypub.ss58_address)
        print(f"Network: Finney Connected ?")
        print(f"Treasury: {balance} TAO")

        # 2. Disk Housekeeping (Clears temporary python caches)
        os.system("find . -type d -name '__pycache__' -exec rm -rf {} +")
        print("Maintenance: Python cache cleared.")

    except Exception as e:
        print(f"ALERT: Infrastructure anomaly detected: {e}")

if __name__ == "__main__":
    print("GFL Housekeeping Daemon Started. Monitoring Infrastructure...")
    while True:
        housekeeping()
        time.sleep(CHECK_INTERVAL)