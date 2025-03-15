import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background-color: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>UNIT CONVERTOR Using Python and Streamlit!</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert:", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "inches", "feet"])
    with col2:
        to_unit = st.selectbox("To unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "inches", "feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    with col2:
        to_unit = st.selectbox("To unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From unit", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To unit", ["celsius", "fahrenheit", "kelvin"])

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'inches': 39.37,
        'feet': 3.28
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1000000,
        'pounds': 2.2046,
        'ounces': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "celsius":
        return (value * 9/5 + 32) if to_unit == "fahrenheit" else (value + 273.15) if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "fahrenheit" else value
    return value

# Conversion button
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_conversion(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"<div class='footer'>Created by SanoberShahid</div>", unsafe_allow_html=True)




#C:/Users/Pcw/AppData/Local/Microsoft/WindowsApps/python3.11.exe -m pip install streamlit
#C:/Users/Pcw/AppData/Local/Microsoft/WindowsApps/python3.11.exe -m streamlit run c:/python/unit-convertor.py




# # project 02: sirziakhan UNIT-CONVERTOR
# # build a google unit convertor using python and  Streamlit.

# import streamlit as st
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #1e1e2f;
#     color: white;
#     }
#     .stApp {
#         background-color: linear-gradient(135deg, #bcbcbc, #cfe2f3);
#         padding :30px;
#         border-radius: 15px;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3)
#     }
#     h1 {
#         text-align: center;
#         font-size: 36px;
#         color: white;

#     }
#     .stButton>button {
#         background: linear-gradient(45deg, #0b5394, #351c75);
#         color: white;
#         font-size: 18px;
#         padding: 10px 20px;
#         border-radius:10px;
#         transition: 0.3s;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
#     }
#     .stButton>button:hover {
#         transform: scale(1.0.5);
#         background: linear-gradient(45deg, #92fe9d, #00c9ff);
#         text-color: black;
#     }
#     .stresult-box {
#         font-size: 20px;
#         font-weight: bold;
#         text-align: center;
#         background: rgba(255, 255, 255, 0.1);
#         padding: 25px;
#         border-radius: 10px;
#         margin-top: 20px;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4 );
        
#     }
#     .footer {
#         text-align: center;
#         margin-top: 50px;
#         font-size: 14px;
#         color: black;

#     }
#      </style>
#     """,
#     unsafe_allow_html=True
# )
#    # tittle and description:
# st.markdown("<h1> UNIT CONVERTOR Using Python and Streamlit! </h1> ", unsafe_allow_html=True)
# st.write("Easily convertor between different units of length, weight, and temprature.")


# #side bar menu:
# conversion_type = st.sidebar.selectionbox("Choose Conversion type", ["Length", "Weight", "Temprature"])
# value - st.number_input("Enter the value to convert:", value = 0.0, min_value = 0.0, step = 0.1)
# col1, col2 = st.columns(2)

# if conversion_type == "Length":
#     with col1:
#         from_unit = st.selectbox("From unit", ["meters","kilogram","centimeters","millimeters","miles","yards","inches","feets"])
#     with col2: 
#         to_unit = st.selectbox("To unit", ["meters","kilogram","centimeters","millimeters","miles","yards","inches","feets"])

# elif conversion_type == "Weight":
#     with col1:
#         from_unit = st.selectbox("From unit", ["kilograms","grams","milligrams","pounds","ounces"])
#     with col2:
#         to_unit = st.selectbox("To unit", ["kilograms","grams","milligrams","pounds","ounces"])
        
# elif  conversion_type == "Temprature":
#     with col1:
#             from_unit = st.selectbox("From unit", ["celsius","fahrenheit","kelvin"])
#     with col2:
#             to_unit = st.selectbox("To unit", ["celsius","fahrenheit","kelvin"])
            
#  # converted function:def Length_conversion(value, from_unit, to_unit):
#     Length_units = {
#         'meters': 1,
#         'kilometers':0.001,
#         'centimeters':100,
#         'millimeters':1000,
#         'miles':0.000621371,
#         'yards':1.09361,
#         'inches': 39.37,
#         'feets':3.28
#     }
#     return (Value / Length_units[from_unit])* Length_units[to_unit]

# def Weight_conversion(value, from_unit, to_unit):
#     Weight_units = {
#         'kilograms':1,
#         'grams':1000,
#         'milligrams':1000000,
#         'pounds':2.2046,
#         'ounces':35.27
#     }
#     return (value / Weight_units[from_unit]) * Weight_units[to_unit]

# def Temprature_conversion(value, from_unit, to_unit):
#     if from_unit == "celsius":
#         return (value * 9/5 + 32) if to_unit == "fahrenheit" else (value + 273.15) if to_unit == "kelvin" else value
#     elif from_unit == "fahrenheit":
#         return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "kelvin" else value
#     elif from_unit == "kelvin":
#         return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "fahrenheit" else value
#     return value

# # button for conversion:
# if st.button("Convert"):
#     if conversion_type == "Lentgth":
#         result = Length_conversion(value, from_unit, to_unit)
#     elif conversion_type == "Weight":
#         result = Weight_conversion(value, from_unit, to_unit)
#     elif conversion_type == "Temprature":
#         result = Temprature_conversion(value, from_unit, to_unit)

#     st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# st.markdown(f"<div class='footer'>Created by SanoberShahid </div>", unsafe_allow_html=True)


