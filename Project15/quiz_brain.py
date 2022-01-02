class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Asks the user a question from a question list and returns the user's answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}:  {current_question.text} (True/False)?:  ").lower()
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, question_answer):
        if answer == "t" or answer == "true":
            answer = "true"
        elif answer == "f" or answer == "false":
            answer = "false"

        if answer == question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}")
        print(f"Your score is {self.score}/{self.question_number}\n")

    def end_of_quiz(self):
        if not self.still_has_questions():
            print("You've completed the quiz.")
            print(f"Your final score was:{self.score}/{self.question_number}")


