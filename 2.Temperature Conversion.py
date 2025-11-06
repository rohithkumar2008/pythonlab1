def fah_to_cel():
    print("Fahrenheit to Celsius Conversion")
    fahrenheit = float(input("Enter Fahrenheit value: "))
    celsius= (fahrenheit - 32) * 5 / 9
    print(celsius) 
def cel_to_fah():
    print("Celsius to Fahrenheit")
    celsius = float(input("Enter celsius value: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(fahrenheit)
print("Conversion Program") 
print("1.Fahrenheit to Celsius") 
print("2.Celsius to Fahrenheit") 
choice = int(input("Enter Your choice: ")) 
if (choice == 1):
    fah_to_cel()
elif (choice == 2):
    cel_to_fah()
else:
    print("Enter Valid Number")
