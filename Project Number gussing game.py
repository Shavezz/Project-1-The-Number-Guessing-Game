import random
#best_score = []
matching_numbers = []


def start_game():

   correct_answer = random.randint(0,10)
   answer = 0
   try:
      answer = int(input('\nGuess a number between 1 and 10: '))
      if answer not in matching_numbers:
         matching_numbers.append(answer)

         
   except ValueError:
      print("\nThe input was not a valid number.")      


   count=0
               
   while True:

      try:
         
         if answer < correct_answer:
            count += 1         
            answer = int(input("It's higher. Try Again: "))

         if answer not in matching_numbers:
            matching_numbers.append(answer)          
               
         if answer > correct_answer:
            count += 1          
            answer = int(input("It's lower. Try Again: "))

         if answer not in matching_numbers:
            matching_numbers.append(answer)

         if answer > 10:
            count += 1         
            answer = int(input('The number is outside the range. The number should be between 1 and 10. Try Again: '))

         if answer not in matching_numbers:
            matching_numbers.append(answer)
                  
         if answer == correct_answer:
            print('\nYou got it!')
            count += 1            
            print('\nIt took you {} attempts to get to the correct answer'.format(count))

            break

         if answer not in matching_numbers:
            matching_numbers.append(answer)

           

      except ValueError:
         print("\nThe input was not a valid number.")
         continue




      
   #best_score.append(count)



def current_best_score():
   if len(matching_numbers) == 0:
      print("\nYou haven't guessed any numbers yet")
   else:   
      print('\nYou have guessed these numbers already: {}'.format(matching_numbers))
   
   if len(matching_numbers) == 0:
      print('\nNo best score yet')
   else:
      print('\nThe best score so far is {} attempts'.format(len(matching_numbers)))



   
while True:
   print('\nWelcome to the game!')
  
   again = input('\nWould you like to play? Yes/No? ')
   if again.lower() == 'yes':
      start_game()
      current_best_score()
         
   if again.lower() == 'no':
      print('\nThanks for playing!')
      break
