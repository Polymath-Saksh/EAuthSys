class SecurityQuestions:
    def __init__(self):
        self.questions = {}
    
    def set_security_questions(self, questions_and_answers):
        self.questions = questions_and_answers
    
    def verify_answers(self, answers):
        for question, answer in answers.items():
            if question not in self.questions or self.questions[question] != answer:
                return False
        return True
