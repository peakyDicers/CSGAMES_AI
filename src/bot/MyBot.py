from src.bot.Bot import Bot
import copy


class MyBot(Bot):

    def __init__(self):
        super().__init__()

    def get_name(self):
        # Find a name for your bot
        return 'My bot'

    def turn(self, game_state, character_state, other_bots):
        # Your bot logic goes here
        super().turn(game_state, character_state, other_bots)

        copy_game_state = [list(state) for state in copy.deepcopy(game_state).split('\n')]
        print(len(copy_game_state))

        
        #get old bot location. 
        old_evilbot_locations = []
        for bot in other_bots:
          print(bot)
          old_evilbot_locations.append(bot['location'])
        print(old_evilbot_locations)

        #check new bot location and current bot location. 
        def checkNearbyBot():
          for i in range other_bots:
            deltaX = other_bots[i]['location'][0] - self['location'][0]
            print deltaX

            #if other_bots[i]['location']
            

        
        return self.commands.idle()
        

        

