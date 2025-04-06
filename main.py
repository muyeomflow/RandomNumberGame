import random

answer = random.randint(1,1000)

guess = 0
attempts = 0
            
while True:
    
    if attempts <= 20: #Up to 20 times
    
        try:
                
            guess = int(input("Enter a number between 1 and 1000 : "))
            attempts += 1 #Increasing the number of attempts
            
            if guess == answer:
                
                print(f"correct answer! You guessed it in {attempts} attempts.")
                break
            
            elif guess > answer:
                
                if guess > 1000:
                    
                    print("Out of range of numbers. Please re-enter")
                    
                else:
                    
                    print(f"Down! Number of attempts : {attempts} attempts.")
                
            elif guess < answer:
                
                if guess < 1:
                    
                    print("Out of range of numbers. Please re-enter")
                    
                else:
                    
                    print("Up! Number of attempts : {attempts} attempts.")

        except ValueError: 
            
            print("Invalid input, please enter a number") # Prevent incorrect input from increasing the number of attempts
            continue
            
    else:
        
        print("You've exceeded 20 attempts. Game over!")
        break