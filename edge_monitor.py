import random
import time
from datetime import datetime

def sync_to_cloud(data_summary):
    """Simulates the 4th Tier: Cloud Sync for long-term records"""
    print(f"  [CLOUD SYNC] Archiving summary at {datetime.now().strftime('%H:%M:%S')}: {data_summary}")
def monitor_vitals(patient_id="P-101"):
    print(f"---  Edge Node Active: Monitoring Patient {patient_id} ---")
    print("Logic: Local processing for low-latency alerts \n") 
    reading_count = 0
    while True:
        reading_count += 1       
        # 1. Data Capture (Tier 1)
        heart_rate = random.randint(60, 120)
        spo2 = random.randint(90, 100)
        timestamp = datetime.now().strftime("%H:%M:%S")   
        # 2. Edge Analysis (Tier 2) - Threshold Logic
        print(f"[{timestamp}] Reading #{reading_count}: HR: {heart_rate} BPM | SpO2: {spo2}%") 
        if heart_rate > 100 or spo2 < 94:
            # 3. Local Alert (Tier 3) - Immediate Action
            print(f" [ALERT] CRITICAL VITALS DETECTED!")
            if heart_rate > 100: print(f"   -> Tachycardia Warning: {heart_rate} BPM")
            if spo2 < 94: print(f"   -> Hypoxia Warning: {spo2}% SpO2")
            print(f"   -> Local siren triggered. Latency: < 10ms")
        else:
            print(f" [STATUS] Normal Activity.")
        # 4. Cloud Sync (Tier 4) - Every 5 readings
        if reading_count % 5 == 0:
            summary = {"Avg_HR": heart_rate, "Status": "Stable"}
            sync_to_cloud(summary)        
        print("-" * 50)
        time.sleep(2) # Local processing interval
if __name__ == "__main__":
    try:
        monitor_vitals()
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
