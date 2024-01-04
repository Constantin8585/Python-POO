def pluralize(total, singular,plural=None):
    assert isinstance (total, int) and total >=0
    # assert permet de verifier une condition
    # isinstance permet de verifier un tyoe de donnée
    
    if not plural:
        plural = singular +'s';
        string = singular if total <= 1 else plural
        return '{} {}'.format(total, string)
    
def get_basketball_team_stats(team_name, wins, losses):
    return '[BASKETBALL] STATS: {}: {}-{}.'.format (team_name, pluralize(wins, 'victoire'), pluralize(losses,'defaite'))

def  get_football_team_stats(team_name, wins, losses):
    return '[FOOTBALL] STATS: {}: {}-{}.'.format (team_name, pluralize(wins, 'victoire'), pluralize(losses,'defaite'))

if __name__ == '__main__':
    # Basketball teams
    print(get_basketball_team_stats('Golden State Warriors', 12, 39))
    print(get_basketball_team_stats('Los Angeles Lakers', 37, 11))
    
    raptors_stats = 'Toronto Raptors-36-14'
    data = raptors_stats.split('-')      
    print(get_basketball_team_stats(data[0],int(data[1]),int(data[2])))     
    
    with open('milwaukee.txt') as file :
        data = file.readline().strip().split('-') 
        print(get_basketball_team_stats(data[0],int(data[1]),int(data[2])))    
    
    # football teams
    print(get_football_team_stats('FC barcelona', 12, 39))
    print(get_football_team_stats('Real Madrid', 37, 11))
    
    madrid_stats = 'Athletico madrid-36-14'
    data = madrid_stats.split('-')      
    print(get_football_team_stats(data[0],int(data[1]),int(data[2])))
    
    with open('city') as file :
        data = file.readline().strip().split('-') 
        print(get_football_team_stats(data[0],int(data[1]),int(data[2]))) 
    

    