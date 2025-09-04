import random


subjects = [
    "Shakib Al Hasan",
    "Virat Kohli",
    "A Dhaka Cat",
    "Prime Minister Sheikh Hasina",
    "NCP",
    "Auto Rickshaw Driver from Dhaka",
    "Tamim Iqbal",
    "PM MOdi",
    "Bladimir Putin",
]



actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "Orders",
    "celebrates"
]


place_or_things = [
    "at Lalbagh Fort",
    "in Dhaka Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Padma Ghat",
    "at Shahbagh",
    "at Dhaka University",
    "at Prime University",
    "BPL match",
    "Mirpur"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    
    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break
    

print("\nThanks for using the Fake News Headline Generator. Have a fun day")    
    