from src.bot.Bot import Bot


class MyBot2(Bot):

    def __init__(self):
        super().__init__()

    def get_name(self):
        # Find a name for your bot
        return 'MyBot2Brah'

    def turn(self, game_state, character_state, other_bots):
        # Your bot logic goes here
        super().turn(game_state, character_state, other_bots)
        #return self.commands.idle()

        #goal = (self.character_state[])

        print(game_state.get_object_at_location)

        playerX = self.location[0]
        playerY = self.location[1]
        for bot in other_bots:
          evilBotX = bot.location[0]
          evilBotY = bot.location[1]

          # if evil bot is left of player.
          goal = (1,1)
          if abs(evilBotX - playerX) < 4:
            if evilBotX < playerX: #if evilbot left of player.
              goal = (self.character_state['location'][0] + 1, self.character_state['location'][1]) #goal move right.
            else:
              goal = (self.character_state['location'][0] - 1, self.character_state['location'][1])


        direction = self.pathfinder.get_next_direction(self.character_state['location'], goal)

          #if (self.hea)


        if direction:
          return self.commands.move(direction)
        else:
          return self.commands.idle()


