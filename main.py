import random

answer = random.randint(1,1000)
user_input = 0
attempts = 0
            
while True:
    
    if attempts <= 20: #Up to 20 times
 
            user_input = input("Enter a number between 1 and 1000 : ")
            
            if user_input == int:
            
                attempts += 1 #Increasing the number of attempts
                
                if user_input == answer:
                    
                    print(f"correct answer! You guessed it in {attempts} attempts.")
                    break
                
                elif user_input > answer:
                    
                    if user_input > 1000:
                        
                        print(f"Out of range of numbers. Please re-enter. You guessed it in {attempts} attempts.")
                        
                    else:
                        
                        print(f"Down! Number of attempts : {attempts} attempts.")
                    
                elif user_input < answer:
                    
                    if user_input < 1:
                        
                        print(f"Out of range of numbers. Please re-enter. You guessed it in {attempts} attempts.")
                        
                    else:
                        
                        print(f"Up! Number of attempts : {attempts} attempts.")
            
            elif user_input == str:
                
                if user_input == "break":
                    
                    break
                
                else:
                    
                    print(f"It's not a number. Please re-enter. You guessed it in {attempts} attempts.")
                
            elif user_input == float:
                
                print(f"Please enter an integer. You guessed it in {attempts} attempts.")

    else:
        
        print("You've exceeded 20 attempts. Game over!")
        break