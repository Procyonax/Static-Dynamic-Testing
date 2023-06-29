### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # operator here should be '==' instead of '=' to compare the value given, a single equals sign will simply set the value to 1 instead of comparing.
      return True
    else
      return False
   

  dif highest_card(self, card1 card2): # there needs to be a comma seperating all parameters in this function, between card1 and card2, and use 'def' instead on 'dif'
  if card1.value > card2.value:
    return card # card1 needs to be used instead of 'card' which is not defined
  else:
    return card2 #code block needs to be properly indented
  


def cards_total(self, cards):
  total # total needs to be assigned to a value such as 0
  for card in cards:
    total += card.value
    return "You have a total of" + str(total) # total needs to be converted to a string in order to return a full statement 
  
```
