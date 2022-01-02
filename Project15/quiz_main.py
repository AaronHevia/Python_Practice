from quiz_question_model import Question
from quiz_brain import QuizBrain
from quiz_data import question_data as data

question_bank = []
for dictionary in data:
    question = Question(dictionary["text"], dictionary["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.end_of_quiz()

