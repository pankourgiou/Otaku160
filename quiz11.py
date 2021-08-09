import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("Which is Joe Satriani's third album?", "Flyin' in a blue dream", ["The Extrimist", "Time Machine"]),
QA("Which is Joe Satriani's second album?", "Surfing with the Alien", ["Flyin' in a blue dream", "Is there love in space?", "Super Colossal"]),
QA("Which is Fates Warning's tenth album?", "X", ["Parallels", "Perfect Symmetry", "Inside out"]),
QA("Which is Fates Warning's ninth album?", "Disconnected", ["Parallels", "Inside out"]),
QA("Which is Fates Warning's eighth album?", "A Pleasant Shade of Gray", ["X", "XI", "VIII", "Parallels"])]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
