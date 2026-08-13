'''
#10 - Cugtas, Jairo Vincent M.
9 - Balingkilat
08/13/26
'''




validator = 0

# List of the Chinese Zodiacs
zodiacs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"
    ]

# loop to validate the input
while validator != 1: #While validator is not 1;
    user_yearofbirth = int(input("Enter your year of birth: ")) #User enters his/her year of birth
    if user_yearofbirth < 1900: #Checks if the year of birth is less than 1900. If true, the user is asked to input again (via while loop), but continues if false.
        print("\nInvalid year, it should not be earlier than 1900")
    else:
        validator = 1 #Sets validator to 1, ending the loop.
        
# This set of codes finds the Chinese Zodiac, then prints it.
remainder = (user_yearofbirth - 1900) % 12 #Finds the remainder of the amount of years after 1900.
user_ChineseZodiac = zodiacs[remainder] #Gets the Chinese Zodiac by using the remainder as the index in the list.
print(f"\nYour Chinese Zodiac Sign is: {user_ChineseZodiac}") #Prints the final result.