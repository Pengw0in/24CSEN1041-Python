import random
import time

runTime = int(input("Enter the amount of time the simulation should run (seconds): "))
fee = {"bike": 20, "car": 50, "truck": 100}
passed = {"bike": 0, "car": 0, "truck": 0}

def bootSimulation(runTime:int):
    total_fee = 0
    print("SIMULATING TOLL BOOTH...")
    time.sleep(0.5)

    for _ in range(runTime):
        random_key = random.choice(list(fee.keys()))
        passed.update({random_key: passed[random_key] + 1})
        time.sleep(1)
        print(f"Vehicle passed: {random_key}")

    print("Toll Booth Summary".center(50, "-"))
    time.sleep(0.5)
    print(f"""Bike : {passed['bike']}
Car  : {passed['car']}
Truck: {passed['truck']}
""")
    print(f"Total Vehicles passed: {runTime}")
    
    for key in fee.keys():
        total_fee += passed[key] * fee[key]
    print(f"Total toll collected: {total_fee}/-")
        
bootSimulation(runTime)

