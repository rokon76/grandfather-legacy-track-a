def calculate_tao_emission(score):
    """
    Translates the Validator Score into a simulated TAO emission weight.
    """
    base_weight = 0.10
    
    if score > 100:
        improvement_bonus = (score - 100) / 100
        # Scaling factor for breakthroughs
        final_weight = min(1.0, base_weight + (improvement_bonus * 5))
        print(f"💰 STATUS: Eligible for Reward Boost")
    else:
        # Standard reward for scores 100 or below
        final_weight = base_weight * (score / 100)
        print(f"⚖️ STATUS: Standard Performance")

    print(f"Calculated Weight: {final_weight:.4f}")
    return final_weight

if __name__ == "__main__":
    # Test default
    calculate_tao_emission(100)
