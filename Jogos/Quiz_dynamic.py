import random

class Quiz:
    def __init__(self):
        self.question = ["Zeke and Eren are brothers.", "King Bradley is a homunculus.", " Ulquiorra is the only Espada with two stages in his resurrection.", "Ryomen Sukuna is a cursed spirit."]
        self.response = ["true", "true", "true", "false"]                       
        self.play = False
        self.hit = 0
        self.victory = 0
        self.cont = 0
        
    def game(self):
        self.confirmation = (input("Do you want to play?s/n")).lower()   
       
        print("let's go \n")    
            
                       
                       
        for x in range (0,4):  
              
            print(self.question[x])
             
            self.cont += 1           
                           
            self.write = (input("R (True or False):")).lower()
            if self.write == self.response[x]:
                    self.hit += 1
                    print(f"You Rigth/ ponts {self.hit}")                            
            elif self.write != self.response[x]:
                    self.hit -= 1
                    print(f"You made a mistake/ ponts {self.hit}"  )
                            
 
                
                         
    def end(self):
        if self.cont == 4:
            if self.hit < -1:
                print("you lose") 
                self.play = False 

            elif self.hit > 0 and self.hit< 4:
                print("Good")
                self.play = False  

            elif self.hit ==  4:
                print("Congratulations!!") 
                self.play = False       
                            
               
play = Quiz()
play.game()  
play.end()              
                
                
                    
                
                
         