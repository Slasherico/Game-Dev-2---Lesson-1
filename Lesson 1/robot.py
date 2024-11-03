class robot:
    color = ''
    name = ''
    
    def hello(self):
        print('hello i am', self.name, 'and my color is', self.color)
        
robot1 = robot()
robot1.name = 'Bolts'
robot1.color = 'Gray'

robot2 = robot()
robot2.name = 'Screws'
robot2.color = 'Brown'

robot1.hello()
robot2.hello()