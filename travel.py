import numpy as np

# ข้อมูลเวลาเดินทาง (สมมติ) ในหน่วยนาที
travel_times = [20, 25, 30, 35, 28, 22, 33] 

# เวลาที่ต้องถึงที่ทำงาน (สมมติ)
arrival_time = 9 * 60  # 9 โมงเช้า

# จำนวนรอบจำลอง
num_simulations = 100000

# เวลาออกจากบ้านตอนนี้ (สมมติ)
current_time = 8 * 60 + 30  # 8:30 น.

# จำลองสถานการณ์
num_on_time = 0
for i in range(num_simulations):
    simulated_travel_time = np.random.choice(travel_times)
    arrival_time_simulated = current_time + simulated_travel_time
    if arrival_time_simulated <= arrival_time:
        num_on_time += 1

# คำนวณความน่าจะเป็น
probability_on_time = num_on_time / num_simulations

print(f"มีโอกาส {probability_on_time:.1%} ที่คุณจะไปทำงานทัน")