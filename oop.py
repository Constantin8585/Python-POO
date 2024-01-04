class EquipBasketball:
    number_of_teams = 0
    fine_amount = 50_000
    def __init__(self,name,wins,losses) :
        self.name = name
        self.wins = wins
        self.losses = losses
        self.total_fine = 0
        
        EquipBasketball.number_of_teams += 1
# team_1 = EquipBasketball('Golden State Warriors',12 ,39)
# team_1.name = 'Golden State Warriors'
# team_1.wins = 12
# team_1.losses = 39

# team_2 = EquipBasketball('Los Angeles Lakers',40 ,10)
# team_2.name = 'Los Angeles Lakers'
# team_2.wins = 40
# team_2.losses = 10

# print(team_1.name)
# print(team_2.name)
# print(team_1.wins)
# print(team_2.wins)
# print(team_1.losses)
# print(team_2.losses)
    
    @classmethod
    def from_string(cls, stats_as_string):  
        data = stats_as_string.split('-')      
        return cls(data[0],data[1],data[2])
     
    @classmethod
    def from_file(cls, stats_as_file):
        with open(stats_as_file) as file:
            name, wins, losses = file.readline().strip().split('-')
            return cls(name, wins, losses)
        
    def get_fined(self):
        self.total_fine += EquipBasketball.fine_amount
        
    def stats(self):
        return f'[FOOTBALL] STATS: {self.name}: {self.wins} victoires -{self.losses} defaites.'  

    @classmethod
    def set_amount(cls, amount):
        cls.fine_amount=amount
        
EquipBasketball.set_amount(10000)
    
team_1 = EquipBasketball('Golden State Warriors',12 ,39)
team_2 = EquipBasketball('Los Angeles Lakers',40 ,10)
team_3 = EquipBasketball.from_string('Golden State Warriors-12-39')
team_4 = EquipBasketball.from_file('milwaukee.txt')

# print(team_1.stats())
# print(team_2.stats())
# team_1.get_fined()
# team_1.get_fined()
# print(team_1.total_fine)
print(EquipBasketball.fine_amount)
print(team_1.fine_amount)
print(team_2.fine_amount)
print(team_3.stats())
print(team_4.stats())
