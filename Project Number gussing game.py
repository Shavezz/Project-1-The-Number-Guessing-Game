best_score = []
def start_game():
   
   print('\nWelcome to the game!')
   count=0

   answer = int(input('\nGuess a number between 1 and 10: '))
  
   while True:
      if answer == 5:
         print('\nYou got it!')
         count += 1
         print('\nIt took you {} attempts to get to the correct answer'.format(count))
         break
           
      if answer < 5:
         count += 1
         answer = int(input("It's higher. Try Again: "))
      if answer > 5:
         count += 1
         answer = int(input("It's lower. Try Again: "))
      if answer > 9:
         count += 1
         answer = int(input('The number is outside the range. The number should be between 1 and 10. Try Again: '))

      best_score.append(count+1)

      
   #return count #HERE I AM RETURNING COUNT AS YOU SAID
   #best_score = start_game()



def current_best_score():
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

   current_best_score()
