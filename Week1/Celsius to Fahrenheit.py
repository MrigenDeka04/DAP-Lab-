#  Convert Celsius to Fahrenheit.

# °F = (9/5) °C+32

def celToFahrenheit(cel):
        F = ((9/5)*cel)+32
        print(F)

cel = int(input("Enter Celcius in degree:"))
celToFahrenheit(cel)