print("What is your age?")
user_age = int(input())
if user_age <= 10:
    print("Are you old enough to be on here?")
if 10 < user_age <= 20:
    print("Fun fact, you can't legally drink because you're not 21; better put that beer down.")
if 21 < user_age <= 30:
    print("I wish I was young again.")
if 31 < user_age <= 100:
    print("Ya old...")
if 100 < user_age:
    print("Dayum ya real old.")
print("You've still got time. Life's short, don't waste it.")