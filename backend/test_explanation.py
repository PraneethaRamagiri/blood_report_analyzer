from explanation import generate_explanation

values = {
    "HGB": 9,
    "MCV": 77,
    "MCH": 22,
    "MCHC": 29
}

print(
    generate_explanation(
        "anemia",
        values
    )
)