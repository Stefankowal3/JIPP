import random

questions = ["Why is the sky blue?\n", "Why is the sun round?\n", "Where are all the dinosaurs?\n"]

question = random.choice(questions)
answer = input(question).strip().lower()

while answer != "to wszystko":
    question = random.choice(questions)
    answer = input(question).strip().lower()
    
print("Okay, that's enough questions for now!")

