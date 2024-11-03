class student:
    def __init__(self, name, study):
        self.name = name
        self.study = study
    
    def hello(self):
        print('Hello my name is', self.name, 'and i am studying', self.study, "at this school.")
        
goodstudent = student('Jonny', 'Math')
badstudent = student('Nick', 'Bullying')

goodstudent.hello()
badstudent.hello()