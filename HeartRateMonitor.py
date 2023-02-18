import time

class HeartRateMonitor:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.heart_rate = 0
        
    def get_heart_rate(self):
        return self.heart_rate
    
    def set_heart_rate(self, new_heart_rate):
        self.heart_rate = new_heart_rate
        
    def check_heart_rate(self):
        # code to check heart rate using a sensor or other device
        # for the purposes of this example, just setting a random value
        import random
        self.heart_rate = random.randint(60, 100)
        print(f"Heart rate for {self.patient_name}: {self.heart_rate}")
        
        
if __name__ == '__main__':
    patient = HeartRateMonitor('John')
    while True:
        patient.check_heart_rate()
        time.sleep(1)
