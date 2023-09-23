'''Implement a class player that represents a cricket player.The player class should have a
method called play() which prints "the player is playing cricket".Derive two classes,Batsman and
Bowler, from the player class.Override the play() method in each derived class to print"the batsman is batting"and "the bowler is bowling",respectively.
write a program to create object of both the
Batsman and Bowler classes and call the play() method for each object.'''






# define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

# define the derived class batsman
class Batsman(player):
  def play(self):
    print("The Batsman is batting.")

# define the derived class bowler
class Bowler(player):
  def play(self):
    print("The Bowler is bowling.")

# create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()


