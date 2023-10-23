class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list = q_list
        self.score=0
        
        
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_ans=input(f"Q.{self.question_number} : {current_question.text} (True/False) ").lower()
        self.check_answer(user_ans,current_question.answer)

            
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    
    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it! ")
        else:
            print("That's Wrong")
        print(f"The correct answer is {correct_ans}")
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")
    