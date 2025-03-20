import streamlit as st

# Conversion dictionary
conversions = {
    "meter": {"kilometer": 0.001, "centimeter": 100, "inch": 39.37, "foot": 3.281},
    "kilometer": {"meter": 1000, "mile": 0.6214},
    "centimeter": {"meter": 0.01, "inch": 0.3937, "foot": 0.0328},
    "inch": {"centimeter": 2.54, "meter": 0.0254, "foot": 0.0833},
    "foot": {"meter": 0.3048, "inch": 12, "centimeter": 30.48},
    "kilogram": {"gram": 1000, "pound": 2.205},
    "gram": {"kilogram": 0.001},
    "pound": {"kilogram": 0.454},
    "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32},
    "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9},
}

# Function to convert units
def convert(value, from_unit, to_unit):
    if from_unit in conversions and to_unit in conversions[from_unit]:
        factor = conversions[from_unit][to_unit]
        return factor(value) if callable(factor) else value * factor
    return "Invalid conversion"

# Streamlit UI
st.title("Easy Unit Converter")

# Get user input
value = st.number_input("Enter value:", min_value=0.0)
from_unit = st.selectbox("From unit:", list(conversions.keys()))
to_unit = st.selectbox("To unit:", list(conversions[from_unit].keys()))

# Convert on button click
if st.button("Convert"):
    st.write(f"Converted value: {convert(value, from_unit, to_unit)}")
