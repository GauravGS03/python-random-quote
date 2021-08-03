import random
def primary():
  print("Hello World.")
  
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.rndint(0,last)
  print(quotes[rnd])

if __name__== "__primary__":
  primary()
