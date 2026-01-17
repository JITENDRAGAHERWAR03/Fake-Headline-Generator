actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "discovers",
    "builds",
    "investigates",
    "orders"
]

places_or_things = [
    "a new product",
    "a mysterious island",
    "an ancient artifact",
    "a secret recipe",
    "a hidden treasure",
    "a futuristic city",
    "a legendary creature",
    "a groundbreaking technology"
]

# 3 start the headline generation loop
while True:
    # 4 get user input for subject
    subject = input("Enter a subject for the headline (or type 'exit' to quit): ")
    if subject.lower() == 'exit':
        break

    # 5 randomly select an action and a place or thing
    import random
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    # 6 construct and display the headline
    headline = f"{subject} {action} {place_or_thing}!"
    print("Generated Headline:", headline)# fake_headline_generater.py
