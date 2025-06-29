import random

class Naval_battle:
    
    def __init__(self):       
        
        self.map =  []
        self.boat = [3]
        self.cont = 0
        self.subtracao = [3]
        self.boat_kill = [0]
        self.victory = False
        self.cont2 = 0   
        self.num = 0
        
       
        
    def create(self):
        
        for x in range(1,11):
            
            self.map.append([0]*10)
            
        for z in self.map:
            
                  
            self.width = random.randint(0, 9)
            self.height = random.randint(0, 9)
            self.amount = random.randint(1,10)
            
            
            
            if self.cont2 < self.amount:         
                self.map[self.width][self.height] = [3]
                self.cont += 1
                self.cont2 += 1
     

    
    def aim(self):
        while self.cont != 0:  
            
            for y in self.map:
                    self.num += 1
                    print(y, self.num)   
        
            
            self.position1 =  int(input("enter the boat position width:\n"))
            self.position2 =  int(input("enter the boat position heith:\n"))
            if self.position1 >= 0 and self.position1 <= 9 and self.position2 >= 0 and self.position2 : 

                if isinstance(self.map[self.position1][self.position2], list):

                     self.boat_right = self.map[self.position1][self.position2]               
                     self.result = [a - b for a, b in zip(self.boat_right, self.subtracao)]
                     self.map[self.position1][self.position2] = self.result
                     print("you hit a boat!\n")  
                     
                     if self.map[self.position1][self.position2] == self.boat_kill: 
                        print("you killed a boat\n")  
                        self.cont -= 1                  
                        self.map[self.position1][self.position2] = 0
                else:
                    print(f"you hit the water/ boat {self.cont}/{self.cont2}")        

                 
                    
            elif self.position1 > 9 or self.position1 < 0 or self.position2 > 9 or self.position2 < 0:
                print("This position does not exists")        

    def win(self):
        if self.cont == 0:
            print("victory")            
                
            
                     
                

    
play = Naval_battle()
play.create()  
play.aim() 
play.win()   