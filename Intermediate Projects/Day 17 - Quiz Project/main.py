from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# COMPILING QUESTIONS IN QUESTION BANK
question_bank = []
for quest in range(0, len(question_data)):
    new_q = Question(question_data[quest]["question"], question_data[quest]["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

# GAME START
while quiz.still_has_question():
    quiz.next_question()
