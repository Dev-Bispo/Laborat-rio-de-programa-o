
class Towerofhonoi:
    def __init__(self):
        self.tower1 = [1,2,3]
        self.tower2 = [0,0,0]
        self.tower3 = [0,0,0]
        self.confirmation = False
        
    def game(self):
        
        if input("Do you want to play?(s/n)") == "s":
            self.confirmation = True            
            while self.confirmation is True:
                self.disco = input("Choice a disc")
                self.tower =  input("Choice a tower")  
                
                
                for i in (0,2):
                   
                    self.location = self.tower3[i]
                    self.dicho = self.tower1.pop(self.disco)   

                    self.location = self.tower2[i]
                   
                    self.location = self.tower2[i]
                   
                        
                    if self.tower == 1:
                        self.tower1.append(int(self.dicho))                        
                    elif self.tower == 2: 
                        self.tower2.append(self.dicho)
                    elif self.tower == 3:
                        self.tower3.append(self.dicho)
                        
                print(self.tower1,self.tower2,self.tower3)        
                                      
       
        
    def win(self):
        if self.tower3 ==  [1,2,3]:
            print("You win") 
            
            
play = Towerofhonoi()
play.win()      
play.game()        