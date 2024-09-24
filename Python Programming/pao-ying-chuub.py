from random import choice

def pao_ying_chuub():

    print("Let's play game!")

    user_scores = 0
    a_scores = 0

    while True:
        hands = ["hammer", "scissor", "paper"]
        
        print("------------------------------------")
        print("Please choose your hand: [hammer, scissor, paper, or stop]")

        a_hand = choice(hands)
        user_hand = input("Your hand: ")

        print(a_hand, user_hand)
    
        if a_hand == user_hand:
            print("Draw")

        elif user_hand == "hammer":
            if a_hand == "scissor":
                user_scores = user_scores + 1
                print("You Win!")  
           
            else:
                a_scores = a_scores + 1   
                print("You Lost!") 
         
        elif user_hand == "scissor":
            if a_hand == "paper":
                user_scores = user_scores + 1
                print("You Win!")  

            else:
                a_scores = a_scores + 1
                print("You Lost!")
                
        elif user_hand == "paper": 
            if a_hand == "hammer":
                user_scores = user_scores + 1
                print("You Win!")
                             
            else:
                a_scores = a_scores + 1
                print("You Lost!") 
                    
        elif user_hand == "stop":
            print("------------------------------------")
            print(f"Your scores: {user_scores}, Bot scores: {a_scores}")
            if user_scores > a_scores:
                print("You are the Winner!!")
            elif user_scores < a_scores:
                print("You are the Loser!")
            else:
                print("Draw")
            break
        else:
            print("Invalid, please try again")
        
