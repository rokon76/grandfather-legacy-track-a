import math

PLANCK = 1.0545718e-34
LIGHT_SPEED = 299792458
PI = math.pi

def calculate_theoretical_pressure(gap_nm):
    a = gap_nm * 1e-9
    return (PI**2 * PLANCK * LIGHT_SPEED) / (240 * a**4)

def run_physical_audit(material_data, claimed_time, gap_nm):
    if claimed_time >= 2.2:
        return 0
    
    # Anti-Cheat check: Faster times REQUIRE smaller gaps (more pressure)
    pressure_pa = calculate_theoretical_pressure(gap_nm)
    atm = pressure_pa / 101325
    
    # Sub-2.1s claims must have at least 500k ATM of pressure
    if claimed_time < 2.1 and atm < 500000:
        return -1 
    
    improvement = ((2.2 - claimed_time) / 2.2) * 100
    return 100 + improvement
