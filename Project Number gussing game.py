print('\nWelcome to the game!')
count=0

answer = int(input('\nGuess a number between 1 and 10: '))

while True:
   while True:
      if answer == 5:
         print('You got it!')
         count += 1
         print('It took you {} attempts to get to the correct answer'.format(count))
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
          

   again = input('\nWould you like to play again? ')
   if again.lower == 'yes':
      CONTINUE
      #HOW DO I START THE GAME OVER???
      
   if again.lower == 'no':
            break

         
