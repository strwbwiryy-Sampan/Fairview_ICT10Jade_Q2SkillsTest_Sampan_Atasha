from pyscript import document, display

element = {
        "H": ("Hydrogen", 1, 1.008),
        "C": ("Carbon", 6, 12.011),
        "N": ("Nitrogen", 7, 14.007),
        "O": ("Oxygen", 8, 15.999),
        "F": ("Fluorine", 9, 18.998),
        "P": ("Phosphorus", 15, 30.974),
        "S": ("Sulfur", 16, 32.06),
        "CI": ("Chlorine", 17, 35.45),
        "Se": ("Selenium", 34, 78.96),
        "Br": ("Bromine", 35, 79.90),
        "I": ("Iodine", 53, 126.90)
    }

def check_element(e):
    document.getElementById("output1").innerHTML = ""

elements = document.getElementById("elements").value

check1 = element.get(elements, ("Element not found", "Atomic Number not found", "Atomic Mass not found"))

document.getElementById("output1").innerHTML = f"""
     Symbol: {elements}
     Element: {check1[0]}
     Atomic Number: {check1[1]}
     Atomic Mass: {check1[2]}
 """

