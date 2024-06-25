from Data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain
question_bank = []
for i in range(len(question_data) - 1):
    question_bank.append(QuestionModel(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("-"*12)
print("\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")