# pythonCode
Repo of personal python code from courses and self projects.

Contents:
- RPG_Text_Game: contains files related to a RPG game created within the Stack Skills course
    "The Complete Python Course: Beginner to Advanced!" available at https://stackskills.com/courses/
    - Game covers python syntax, class creation and instantiation, and programming a dynamic game battle script
    - To play:
        - run the main.py script, the game exeutes in the terminal.
        - you decide the actions of a team: Mage, Rogue, and Steve the Cat.
        - you battle a monster Magmaximum and 2 Lava Imps
        - The battle script follows 2 phases
            1) Mage, Rogue, and Steve the Cat each get a turn to
                A) Do a quick attack against a target enemy
                B) Use a magic spell against a target enemy
                C) Use an item, choose an enemy if attack item
            2) Magmaximum and the 2 Lava Imps each take a turn to
                A) Do a quick attack against a player
                B) Attempt to use magic against a player
        - The battle continues until all players are dead, or all monsters are dead.
        - Only enter valid options, invalid options can cause the program to fail.
    - Game has some known limits and bugs: (which might be fixed if/when the game is expanded upon)
        - once magic or items has been chosen as the action, you cannot go back and change the action. Instead, you must
        choose a spell or item.
        - invalid option entries can cause the program to fail.
