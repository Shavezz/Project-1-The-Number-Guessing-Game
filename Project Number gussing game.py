best_score = []
matching_numbers = []


def start_game():
   
   print('\nWelcome to the game!')
   count=0

   answer = int(input('\nGuess a number between 1 and 10: '))
  
   while True:
           
      if answer < 5:
         count += 1
         answer = int(input("It's higher. Try Again: "))
      if answer > 5:
         count += 1
         answer = int(input("It's lower. Try Again: "))
      if answer > 9:
         count += 1
         answer = int(input('The number is outside the range. The number should be between 1 and 10. Try Again: '))
      if answer == 5:
         print('\nYou got it!')
         count += 1
         print('\nIt took you {} attempts to get to the correct answer'.format(count))
         break
      
      best_score.append(count+1)
      matching_numbers.append(answer) #Why is this not getting appended to the list, matching_numbers?
      


def current_best_score():
   if len(matching_numbers) == 0:
      print("\nYou haven't gussed any numbers yet")
   else:   
      print('\nYou have guessed these numbers already:'.format(matching_numbers))
   
   if len(best_score) == 0:
      print('\nNo best score yet')
   else:
      print('\nThe best score so far is {} attempts'.format(min(best_score)))


   
while True:
   current_best_score()
   start_game()

   again = input('\nWould you like to play again? ')
   if again.lower() == 'yes':
      start_game()
         
   if again.lower() == 'no':
      print('\nThanks for playing')
      break
