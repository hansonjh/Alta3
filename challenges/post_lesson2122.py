#!/usr/bin/env python3

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": html.unescape("&quot;Frankly, my dear, I don&#039;t give a damn.&quot;"),
         "incorrect_answers": [
             html.unescape("&quot;Here&#039;s lookin&#039; at you, kid.&quot;"),
             html.unescape("&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;"),
             html.unescape("&quot;Round up the usual suspects.&quot;")
            ]
        }
question = trivia["question"]
correct = html.unescape(trivia["correct_answer"])
incorrect1 = trivia["incorrect_answers"][0]
incorrect2 = trivia["incorrect_answers"][1]
incorrect3 = trivia["incorrect_answers"][2]

print(question)
print("A)",correct)
print("B)",incorrect1)
print("C)",incorrect2)
print("D)",incorrect3)

answer = input("Answer here: ").lower()

if answer == "a":
    print("You know your movies!")
elif answer != "a":
    print("Please try again...")

