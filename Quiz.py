" Created a dict variable quest for storing questions and answwers"
quests = {
    1: {
        "question": "1. Who developed Python Programming Language?a) Wick van Rossum b) Rasmus Lerdorf c) Guido van Rossum d) Niene Stom",
        "answer": "c"
    },
    2: {
        "question": "2. Which type of Programming does Python support? a) object-oriented programming b) structured programming c) functional programming d) all of the mentioned",
        "answer": "d"
    },
    3: {
        "question": "3. Which of the following is the correct extension of the Python file? a) .python b) .pl c) .py d) .p",
        "answer": "c"
    }
}

"checks whether the question is right of wrong"
def check_ans(question, ans, score):
    if quests[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour current score is {score + 1}!\n")
        return True
    else:
        print(f"Wrong Answer. The correct answer is {quests[question]['answer']!r}\n")
        return False

score = 0#calculates score

for question in quests:#question will be printed
    print(quests[question]['question'])
    answer = input("Enter Answer (a, b, c, or d): ").lower()

    while answer not in ['a', 'b', 'c', 'd']:
        print("Invalid input. Please enter a valid option (a, b, c, or d).")
        answer = input("Enter Answer: ").lower()

    check = check_ans(question, answer, score)#checks for answer
    if check:
        score += 1

print(f"Your final score is {score}/{len(quests)}.")
