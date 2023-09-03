import random
which_dice=int(input("enter the number of dice you want to use 0 for normal 1 for 1 biased 2 for 2 biased 3 for 3 biased 4 for 4 biased 5 for 5 biased 6 for 6 biased"))
dice=[1,2,3,4,5,6] 
dice_chance=random.choices(dice,weights=(10,10,10,10,10,10),k=1)#normal dice
dice_1=[1,2,3,4,5,6]   
biased_1=random.choices(dice,weights=(60,10,10,10,10,10),k=1)#higher chances of 1
dice_2=[1,2,3,4,5,6]   
biased_2=random.choices(dice,weights=(10,60,10,10,10,10),k=1)
dice_3=[1,2,3,4,5,6]   
biased_3=random.choices(dice,weights=(10,10,60,10,10,10),k=1)#higher chances of 3
dice_4=[1,2,3,4,5,6]   
biased_4=random.choices(dice,weights=(10,10,10,60,10,10),k=1)
dice_5=[1,2,3,4,5,6]   
biased_5=random.choices(dice,weights=(10,10,10,10,60,10),k=1)
dice_6=[1,2,3,4,5,6]   
biased_6=random.choices(dice,weights=(10,10,10,10,10,60),k=1)
if which_dice==0:
  print(dice_chance)
elif which_dice==1:
  print(biased_1)
elif which_dice==2:
  print(biased_2)
elif which_dice==3:
  print(biased_3)
elif which_dice==4:
  print(biased_4)
elif which_dice==5:
  print(biased_5)
elif which_dice==6:
  print(biased_6)
else:
  print("BRUH input a number between 0-6")