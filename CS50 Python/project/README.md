    # Alex's Turn Based Game
    #### Video Demo:  https://youtu.be/XD516znHQ_Q
    #### Description:

The python project I decided to go with is a text-based turn based game for CS50P,
it took me 2 hours to fully create this game and ensure that there are no bugs to
deal with. The game can be infinitely played and infinitely scaled up in difficulty
as the user progresses as this is the way its been coded and each enemy will have
their own unique archetypes, unique names and attributes making each fight slightly
different and interesting.

The player first begins with a welcome to the game message and this will allow them
to select whether or not they want to play the game then they will be greeted with a
character selection menu allowing them to decide what character they will like to
pick between 1-4 which comes as The Warrior, The Wizard, The Phantom and The Rogue,
they all have different ability distribution in terms of their stats and this allows
them to be more effective in different areas of the turn based combat such as having
more health, more strength, more mana allowing them to use more abilities, or more
speed to be able to dodge opponents attacks.

The game will require only a keyboard to play as the game is text input based and this
means that the user has to enter either a number or a word to continue on in the game,
once the user has done this then it will automatically go to the enemies turn and so on
until either you or the enemy wins.

Everytime you win a level, the level modifier gradually increases giving enemies a direct
increase to their health, mana and power levels making them stronger and stronger every
fight.

However if you lose a battle then the level will remain the same and you will have to face
a new enemy that belongs in that level.

Warning: if you quit the game you will lose all progress made as there is no save data coded
into the game.

The game itself makes use of object orientated programming to get the entities developed,
it also makes use of many loops to ensure continuous gameplay without the need of ridiculous
amounts of lines of code and it has timers throughout to make sure it flows smoothly like a
game rather than having everything happen instantaneously.