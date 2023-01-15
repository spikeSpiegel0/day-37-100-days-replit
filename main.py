blue = "\033[34m"
red = "\033[31m"
reset = "\033[0m"
print(f"🌟 {blue}STAR WARS NAME GENERATOR{reset} 🌟")
print()
firstN = input("Enter your first name: ").title()
lastN = input("Enter your last name: ").lower()
mum = input("Enter your Mum's maiden name: ").title()
born = input("Enter the city where you are born: ").lower()
print()
print(f"{red}Your Starwars name is {firstN[0:3]}{lastN[0:3]} {mum[0:2]}{born[0:3]}")