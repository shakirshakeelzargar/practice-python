def sendMail():
  print("Mail sent")

import sys
sys.path.append('/usr/sammy/')

#from = "weekly-news@sci.com"

class Octopus:
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def tell_me_about_the_octopus(self):
        print("This octopus is " + self.color + ".")
        print(self.name + " is the octopus's name.")
