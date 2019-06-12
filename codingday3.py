cadbury1 ="milk chocolate"
cadbury2 = "dark chocolate"
cadbury3 = "white chocolate"

cadburymilk = 5
cadburydark = 3
cadburywhite = 8

chocolate1 = {"milk:5"}
chocolate2 = {"dark:3"}
chocolate3 = {"white:8"}

print(chocolate1, chocolate2, chocolate3)
print(chocolate1) 

chocolate = {"milk":5, "dark":8, "white":3}
print(chocolate)

#practice
name1 = "steve"
name2 = "lia"
name3 = "vin"
name4 = "katie"

Steve = 32
Lia = 28
Katie = 38

name = {"steve":32, "Lia":28, "Vin":45, "Katie": 38}
print(name)

female1 = "lia"
female2 = "katie"

male1 = "vin"
male2 = "steve"

female = {"lia":28, "katie":38}
male = {"steve":32, "vin":45}
print(female)
print(male)

import pandas
dir(pandas)

name = pandas.Series(name)
print(name)

gender = pandas.Series(male)
print(male)

gender = pandas.Series(female)
print(female)

