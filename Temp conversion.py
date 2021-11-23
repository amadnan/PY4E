def temp_conversion(temp,current_unit,to_be_converted):

#Conversion from Celsius to Fahrenheit 
    if to_be_converted == "F" and current_unit == "C":
        new_temp = round(9 / 5 * temp + 32, 3)
        print("The converted temperature in Fahrenheit scale is " + str(new_temp) + " degrees")
        
#Conversion from Fahrenheit into Celsius    
    elif to_be_converted == "C" and current_unit == "F":
        new_temp = round(5 / 9 * (temp - 32), 3)
        print("The converted temperature in Celsius scale is " + str(new_temp) + " degrees")    
        
#Conversion from Celsius to Kelvin 
    elif to_be_converted == "K" and current_unit == "C":
        new_temp = round(temp + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")
        
#Conversion from Kelvin to Celsius  
    elif to_be_converted == "C" and current_unit == "K":
         new_temp = round(temp - 273.15, 3)
         print("The converted temperature in Celsius scale is " + str(new_temp) + " degrees")
         
#Conversion from Kelvin to Fahrenheit   
    elif to_be_converted == "F" and current_unit == "K":
        new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)
        print("The converted temperature in Fahrenheit scale is " + str(new_temp) + " degrees")
        
#Conversion from Fahrenheit to Kelvin ###    
    else:
        new_temp = round(5 / 9 * (temp - 32) + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")

t = float(input("Temperature :"))
s1 = input("Scale from:")
s2 = input("Convert to: ")
temp_conversion(t,s1,s2)
#Use "F" for Fahrenheit, "C" for Celsius and "K" for Kelvin