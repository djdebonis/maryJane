# a basic edible calculator

import streamlit as st

st.markdown("# Basic Edible Calculator") # prints a title using md



quantity = st.text_input("Please enter how much mj flower you have: ")
units = ["grams", "ounces", "pounds"]  # create the list for the user
unitSelect = st.selectbox("Enter the unit type you would like to use: ", units)


# assign  some variables
milligramsPerGram = 1000

# calculate milligrams per ounce
gramsPerOunce  = 28
milligramsPerOunce = milligramsPerGram  *  gramsPerOunce

# calculate milligrams per pound
ouncesPerLb = 16
milligramsPerPound = milligramsPerOunce * ouncesPerLb


# convert any unit type to milligrams:
# initialize variable outside of local scope of if/else
milligrams = 0

if (unitSelect == units[0]): # if it's in grams
    milligrams = quantity * milligramsPerGram
    
elif (unitSelect == units[1]): # if it's in ounces
    
    milligrams = quantity * milligramsPerOunce
    
elif (unitSelect == units[2]):
    milligrams = quantity * milligramsPerPound

numCannabs = [1, 2, 3, 4, 5, 6,  7,  8, 9, 10, 11, 12, 13]
cannaCount = st.selectbox("Enter the number of cannabinoids you would like to calculate for: ", numCannabs)
 
# initialize a dictionary to store cannabinoid percentages

cannaType = []
cannaPercent = []

for i in range(cannaCount):
    tipo = st.text_input("Enter the name of the cannabinoid: ")
    percentage = st.text_input("Enter the percentage of cannabinoid in the mj:  ")
    percentage =  int(percentage)
    cannaType.append(tipo)
    cannaPercent.append(percentage)
    

for i  in range(cannaCount):
    cannaPortion = cannaPercent[i]  / 100
    cannaMg =  cannaPortion * milligrams
    
    st.write("For cannabinoid %s, there are %d mgs in the batch"%(cannaType[i], cannaMg))
    
st.write("Would you like to split into servings?")
    
    
    
    