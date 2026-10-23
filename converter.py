
def convert(value, from_unit, to_unit):
    # Convert common volume measurements to millilitres
    to_ml = {
        "ml": 1,
        "tsp": 4.92892,
        "tbsp": 14.7868,
        "cup": 236.588
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in to_ml or to_unit not in to_ml:
        raise ValueError("Supported units: ml, tsp, tbsp, cup")

    ml = value * to_ml[from_unit]
    return ml / to_ml[to_unit]


if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    source = input("Convert from (ml/tsp/tbsp/cup): ")
    target = input("Convert to (ml/tsp/tbsp/cup): ")

    try:
        result = convert(amount, source, target)
        print(f"{amount} {source} = {result:.2f} {target}")
    except ValueError as error:
        print("Error:", error)
