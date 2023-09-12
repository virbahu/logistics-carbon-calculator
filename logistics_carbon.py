import numpy as np
def calculate_logistics_carbon(weight_kg, distance_km, mode, utilization=0.8):
    factors = {"truck": 0.062, "rail": 0.022, "ocean": 0.008, "air": 0.602}
    ef = factors.get(mode, 0.062)
    co2 = weight_kg / 1000 * distance_km * ef / utilization
    return {"co2_kg": round(co2, 2), "co2_per_kg": round(co2 / max(weight_kg, 1), 4), "mode": mode, "emission_factor": ef}
if __name__=="__main__":
    for m in ["truck", "rail", "ocean", "air"]:
        print(calculate_logistics_carbon(5000, 1000, m))
