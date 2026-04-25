import bittensor as bt

def check_gfl_infrastructure():
    # Initialize the wallet object (metadata only, no password needed for balance check)
    wallet = bt.Wallet(name='gfl_vault', hotkey='gfl_worker')
    
    # Connect to the Bittensor "Finney" network
    subtensor = bt.Subtensor(network='finney')
    
    print("--- GFL Infrastructure Pulse ---")
    print(f"Coldkey: {wallet.coldkeypub.ss58_address}")
    print(f"Hotkey:  {wallet.hotkey_str}")
    
    try:
        # Fetch the balance from the chain
        balance = subtensor.get_balance(wallet.coldkeypub.ss58_address)
        print(f"Current Treasury Balance: {balance}")
        print("Status: Handshake Successful ?")
    except Exception as e:
        print(f"Status: Connection Error ?\nDetails: {e}")

if __name__ == "__main__":
    check_gfl_infrastructure()