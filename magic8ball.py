# https://www.geeksforgeeks.org/magic-8-ball-program-in-python/
# July 9, 2024

import random
import datetime

def get_magic_8_ball_responses():
    responses = [
        "Yes, definitely.",
        "No, certainly not.",
        "Ask again later.",
        "As I see it, yes.",
        "Reply hazy, try again.",
        "Cannot predict now.",
        "Don't count on it.",
        "Do not count on it.",
        "It is decidedly so.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook is good.",
        "Very doubtful."
    ]
    return random.choice(responses)

def log_question_and_answer(question, answer):
    with open("magic_8_ball_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Question: {question} - Answer: {answer}\n")

def main():
    print("Welcome to the Magic 8-Ball!")
    while True:
        question = input("Ask a question or type 'exit' to leave: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        if question.strip() == '':
            print("Please ask a real question.")
            continue
        answer = get_magic_8_ball_responses()
        log_question_and_answer(question, answer)
        print("Magic 8-Ball says: ", answer)
if __name__ == "__main__":
    main()