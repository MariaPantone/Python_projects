import requests
import json 
import pprint as p
import random
import html

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"

endGame = ""

while endGame != "quit":
    r = requests.get(url)
    if(r.status_code != 200):
        endGame = input("Sorry, there was a problem retreving the question. Press 'enter' to try again or 'quit' to quit the game: ").lower()
        
    else:
        valid_answer = False
        answer_number = 1
        
        """ conversione in testo del codice in json caricato da browser """
        
        data = json.loads(r.text)

        """ selezione i dati che ci servono per costruire la domanda """
        
        question = data['results'][0]['question']
        wrong_answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']

        """ Aggiunta della risposta corretta alle risposte errate (alla fine) """
        
        answers = wrong_answers
        answers.append(correct_answer)
        
        """ Mescolare le risposte in modo randomico """
        
        random.shuffle(answers)

        """ usare html.unescape per non avere errori di lettura nei caratteri speciali della domanda"""
        
        print(html.unescape(question + "\n"))

        """ Ulizzare il loop for per stampare una alla volta le risposte e incrementare di 1 la variabile answer_number """
        
        for answer in answers:    
            print(str(answer_number)+ ". " + html.unescape(answer))
            answer_number +=1
            
        while valid_answer == False:
            user_answer = input("\nType the  number of  correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <=0:
                
                    print("Invalid answer.")
   
                else:
                    valid_answer = True   
            except:         
                print("Invalid answer. Use only numbers.")

                
        """ dichiariamo la variabile che verrà utilizzata per la risposta dell'utente (viene messa all'interno di una lista ed essendo che sarà un numero intero la prima posizione(ovvero la prima risposta) non parte da 1 ma da 0 quindi (variabile-1) """

        user_answer = answers[int(user_answer)-1]
        
        if user_answer == correct_answer:
            
                print("\nCongratulations. This is the correct answer!\nThe correct answer was: " + html.unescape(correct_answer))
                score_correct += 100
        else:
                print("Sorry, " + html.unescape(user_answer) + "is incorrect. The correct answer is : " + html.unescape(correct_answer))
                score_incorrect += 50


        print("\n###################################################\n")
        print("Points for each correct questions: 100 points ")
        print("\n")
        print("Penality for each correct questions: 50 points ")
        print("\n")
        print("Total score:  ",int(score_correct - score_incorrect))
        print("\n###################################################\n")
        
        endGame = input("Press 'enter' to play again or 'quit' to quit the game: ").lower()

print("\nThanks for playing")
        
