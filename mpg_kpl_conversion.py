import re

def fuel_economy_conversion():
    input_str = input("Enter the fuel economy and unit (e.g. 15 mpg or 20 kpl): ")
    match = re.findall(r'(\d+\.\d+|\d+)\s*([a-zA-Z]+)', input_str.strip())
    try:
        fuel_economy, current_unit = match[0]
        fuel_economy = float(fuel_economy)
        if current_unit == "mpg":
            target_unit = "kpl"
            converted_fuel_economy = fuel_economy * 0.425143707
        elif current_unit == "kpl":
            target_unit = "mpg"
            converted_fuel_economy = fuel_economy * 2.352145833
        else:
            raise ValueError("Invalid unit entered.")
        print(f'Fuel economy {fuel_economy} {current_unit} is equal to {converted_fuel_economy} {target_unit}')
    except ValueError as e:
        print("Invalid input:", e)
    except IndexError as e:
        print("Invalid input format:", e)
        
fuel_economy_conversion()
