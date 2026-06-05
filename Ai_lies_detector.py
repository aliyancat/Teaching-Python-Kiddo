'''🧠 1. AI HBonesty Detector

User types messages.

Program analyzes:

ALL CAPS
too many pauses (...)
suspicious words


At the end it gives truth score '''



message = input("Enter your message ")


truth_score = 100

suspicious_words = ["trust me","im not lying","free money","click here"]


if message.isupper():
    truth_score =  truth_score - 20


for word in suspicious_words:
    if word in message.lower():
        truth_score = truth_score - 20


if "..." in message:
    truth_score = truth_score - 10


if truth_score > 80:
    print("Wow you are so  honest") 
elif truth_score > 40 and truth_score < 80:
    print("Hmm something is suspicious")

elif truth_score < 40:
    print("CAUGHT YOU")