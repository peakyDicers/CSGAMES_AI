import utils.Pathfinder;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class MyBot2 extends Bot {
  ArrayList<Integer> oldLocation;

  public String get_name() {
    // Find a name for your bot
    return "Brinux";
  }

  public HashMap<String, String> turn(String game_state, HashMap<String, Object> character_state,
      ArrayList<HashMap<String, Object>> other_bots) {
    // Your bot logic goes here.
    super.turn(game_state, character_state, other_bots);

    ArrayList<Integer> goal = new ArrayList<>(Arrays.asList(1, 1));

    int playerX = player.getLocation().get(0);
    int playerY = player.getLocation().get(1);
    for (int i = 0; i < other_bots.size(); i++) {

      //get location of evilbot.
      int evilBotX = otherBots.get(i).getLocation().get(0);
      int evilBotY = otherBots.get(i).getLocation().get(1);

      //if evil bot is less than 4 horizontal blocks away. 
      if (Math.abs(evilBotX - playerX) < 4) {
        if (evilBotX < playerX) //if evilbot left of player.
          goal = new ArrayList<Integer>(Arrays.asList(goal.get(0) + 1, goal.get(1))); //set goal to move right
        else
          goal = new ArrayList<Integer>(Arrays.asList(goal.get(0) - 1, goal.get(1))); //set goal to move left.
      }

      //if evil bot is less than 4 vertical blocks away. 
      if (Math.abs(evilBotY - playerY) < 4) {
        if (evilBotY < playerY) //if evilbot north of player.
          goal = new ArrayList<Integer>(Arrays.asList(goal.get(0), goal.get(1) + 1)); //set goal to move south.
        else
          goal = new ArrayList<Integer>(Arrays.asList(goal.get(0), goal.get(1) - 1)); //set goal to move north.
      }
    }


    String direction = pathfinder.getNextDirection(game_state, player.getLocation(), goal);
    if (direction != null) {
      return command.move(direction);
    } else {
      return command.idle();
    }
  }
}