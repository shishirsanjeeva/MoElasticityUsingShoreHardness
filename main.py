import math

def youngs_modulus_from_shore(shore_hardness, scale="D", method="Ruess"):
    """
    Calculate Young's modulus (MPa) from Shore hardness using empirical equations from ASTM D2240 (Reuss).

    :param shore_hardness: Shore hardness value (typically between 0 and 100)
    :param scale: "A" for Shore A or "D" for Shore D (default)
    :param method: "Ruess" for Ruess' empirical equation, "Gent" for A. N. Gent's equation (Shore A only)
    :return: Estimated Young's modulus in MPa
    """
    if not (0 <= shore_hardness <= 100):
        raise ValueError("Shore hardness should be in the range 0 to 100.")

    if method == "Ruess":
        if scale.upper() == "D":
            return 10 **(0.0235 * (shore_hardness + 50) - 0.6403)
        elif scale.upper() == "A":
            return 10 **(0.0235 * shore_hardness - 0.6403)
        else:
            raise ValueError("Unsupported Shore hardness scale. Use 'A' or 'D'.")
    elif method == "Gent" and scale.upper() == "A":
        # A. N. Gent's 1958 equation for Shore A hardness
        return (0.0981 * (56 + 7.62336 * shore_hardness)) / (0.137505 * (254 - 2.54 * shore_hardness))
    else:
        raise ValueError("Unsupported method. Use 'Ruess' or 'Gent' (Gent applies only to Shore A).")

# Example usage
shore_a_value = 50  # Change to desired Shore A hardness
shore_d_value = 60  # Change to desired Shore D hardness

youngs_modulus_ruess_a = youngs_modulus_from_shore(shore_a_value, scale="A", method="Ruess")
youngs_modulus_ruess_d = youngs_modulus_from_shore(shore_d_value, scale="D", method="Ruess")
youngs_modulus_gent_a = youngs_modulus_from_shore(shore_a_value, scale="A", method="Gent")

print(f"Estimated Young's modulus (Ruess) for Shore A hardness {shore_a_value}: {youngs_modulus_ruess_a:.2f} MPa")
print(f"Estimated Young's modulus (Ruess) for Shore D hardness {shore_d_value}: {youngs_modulus_ruess_d:.2f} MPa")
print(f"Estimated Young's modulus (Gent) for Shore A hardness {shore_a_value}: {youngs_modulus_gent_a:.2f} MPa")