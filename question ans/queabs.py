import random
questions ={
    "Im atring which function is used to fin length ?": "len" , 
    "funtion is defined by using which keywords?" : "def",
    "what is the output for 10//3 ?" : "3",
    "Which datatype is used to find true or fase value ?": "boolen",
    "Which keyword is used to import module in python?" : "import",
    "what is the output of 2*3?" : "6",
}
 
def game():
    question_list= list(questions.keys())
    total_question=5
    score = 0
     
    question_pick = random.sample(question_list, total_question)

    for i, question in enumerate(question_pick):
        print(f"{i+1}.{question}\n")
        user_ans= input(f"your answwer: ").lower().strip()
        correct = questions[question]

        if user_ans == correct:
            print("correct answer")
            score +=1
        
        else:
            print("Wrong answer the correct anwer is ",correct)

    print(f"game is over, your score is: {score}/{total_question} ")

game()  