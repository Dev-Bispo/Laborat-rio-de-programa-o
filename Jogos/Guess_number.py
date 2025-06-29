import random
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/Guess_Number')

class Guess_Number:
    def __init__(self):
        self.choice = int(random.randint(1,100))
        self.guess = int
        self.confirmation = False
        self.erro =  0
        
        
        
    def game(self):
        if  (input("Ready to play? n/s ")).lower() == "s":
            self.confirmation = True
            print("you will have 10 attempts to guess a number from 1 to 100")
            
            while self.confirmation:
                if self.erro < 10 :
                    self.guess = int(input("Guess Number:"))

                    if self.guess > self.choice:
                        print("your guess was high")
                        self.erro += 1
                        print("Erros", self.erro , "/10")

                    elif self.guess < self.choice:
                        print("your guess was low")
                        self.erro += 1
                        print("Erros",self.erro,"/10")

                    elif self.guess == self.choice:
                        print("Congratulations, you guess!!!")
                        self.confirmation = False
                else:
                    print("You Lose")  
                    break      
                    
                        
gam = Guess_Number()
gam.game()                    