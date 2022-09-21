import random as ran
list1=['rock','paper','scissors']
sc =0
su =0
while True:
  if sc<3 and su<3:
    print("<><><><><><><><><><><><><>\nyour turn")
    user = input("Enter a choice: ")
    if user in list1:
      comp = ran.choice(list1)
      if comp == user:
        print(f'Draw, you-{user} and computer {comp}')
      elif user=='rock' and comp=='paper':
        print(f'computer won, you-{user} and computer-{comp}')
        sc+=1
      elif user=='rock' and comp=='scissors':
        print(f'you won, you-{user} and computer-{comp}')
        su+=1
      elif user=='paper' and comp=='rock':
        print(f'you won, you-{user} and computer-{comp}')
        su+=1
      elif user=='paper' and comp=='scissors':
        print(f'computer won, you-{user} and computer-{comp}')
        sc+=1
      elif user=='scissors' and comp=='rock':
        print(f'computer won, you-{user} and computer-{comp}')
        sc+=1
      elif user=='scissors' and comp=='paper':
        print(f'you won, you-{user} and computer-{comp}')
        su+=1
    else:
      print("Enter a valid choice")
  elif sc==3:
    print(f'computer won by {sc}-{su}')
    break
  else:
    print(f'user won by {su}-{sc}')
    break
