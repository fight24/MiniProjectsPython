class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        question = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer.lower().strip()
        choice = input(f"Q.{self.question_number + 1} : "
                       f"{question} (True/False)?: ").lower().strip()
        if choice == answer:
            self.score += 1
            print(f"You got it right!\n")
        else:
            print("That's wrong.\n")
        print(f"The correct answer was: {answer}.\nYour current score is: {self.score}/{self.question_number+1}")
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

