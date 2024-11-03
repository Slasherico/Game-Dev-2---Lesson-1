class robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def hello(self):
        print('hello i am', self.name, 'and my color is', self.color)
        
robot1 = robot('Bolts', 'Gray')
robot2 = robot('Screws', 'Brown')

robot1.hello()
robot2.hello()