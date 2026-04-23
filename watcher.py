import time
import os
import json
import consistency_audit
import weight_mapper
import notifier

WATCH_PATH = "C:\\gfl\\submission.json"

print("📡 Grandfather Legacy: Background Watcher Active...")

def process_submission():
    try:
        with open(WATCH_PATH, 'r', encoding='utf-8') as f:
            sub = json.load(f)
        
        m_time = sub.get("loading_time")
        m_gap = sub.get("lattice_gap", 0.5)
        m_id = sub.get("miner_id", "Unknown")

        score = consistency_audit.run_physical_audit(None, m_time, m_gap)
        
        if score > 0:
            weight = weight_mapper.calculate_tao_emission(score)
            msg = f"🚀 *VALID SUBMISSION*\nMiner: `{m_id}`\nTime: `{m_time}s`\nWeight: `{weight:.4f}`"
            notifier.send_telegram_alert(msg)
            # Delete file after processing to wait for the next one
            os.remove(WATCH_PATH) 
        else:
            notifier.send_telegram_alert(f"⚠️ *AUDIT FAILED*\nMiner `{m_id}` submitted invalid data.")
            os.remove(WATCH_PATH)

    except Exception as e:
        print(f"Error: {e}")

while True:
    if os.path.exists(WATCH_PATH):
        process_submission()
    time.sleep(5) # Checks every 5 seconds
