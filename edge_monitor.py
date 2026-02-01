import random
import time

# Simulation of Edge Computing Logic for Healthcare
def monitor_vitals():
    print("--- Edge Node Active: Monitoring Patient Vitals ---")
    while True:
        # Simulating sensor data (Heart Rate)
        heart_rate = random.randint(60, 120) 
        
        # Edge Processing: Immediate decision making
        if heart_rate > 100:
            print(f"ALERT: High Heart Rate Detected ({heart_rate} BPM)! Triggering Local Alarm...")
            # In a real system, this would send an MQTT alert immediately
        else:
            print(f"Normal Activity: {heart_rate} BPM. Syncing to Cloud...")
        
        time.sleep(2) # Local processing interval

if __name__ == "__main__":
    monitor_vitals()
