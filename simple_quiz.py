print("==============================")
print("       SIMPLE QUIZ")
print("==============================")

score = 0

questions = [
    "What is the capital of the Philippines?",
    "What is 5 + 5?",
    "What language are we learning?"
]

answers = [
    "manila",
    "10",
    "python"
]

for i in range(3):
    print()
    print(questions[i])
    answer = input("Your answer: ")

    if answer.lower() == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong answer!")

print()
print("==============================")
print("Your Score:", score, "/ 3")
print("==============================")