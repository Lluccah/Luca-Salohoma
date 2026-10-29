# Import Python's built-in random module
# this allows us to randomly select jokes from a list
import random

# create a list containing some jokes
# each joke its punchline
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the coffee file a police report? It got mugged!",
    "Why did the cookie go to the doctor? Because it was feeling crumbly!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the chicken cross the playground? To get to the other slide!",
]
 # random.choice () randomly selects a joke from the list
 # the selected joke is stored in the variable called random_joke
random_joke = random.choice(jokes)

# print the randomly selected joke to the screen
print(random_joke)
