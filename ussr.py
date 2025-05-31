import hashlib
import sys
import base64

__credit_section__ = '''
PotatoKingz
https://bit.ly/potatokingz
'''

_expected_hash = '13d3e55c4de9e83013bcfae4501bb172'

def verify_credits():
    current_hash = hashlib.md5(__credit_section__.encode()).hexdigest()
    if current_hash != _expected_hash:
        print("ERROR: Credits section modified. Exiting.")
        sys.exit(1)

def get_credits():
    lines = __credit_section__.strip().split('\n')
    author = lines[0]
    link = lines[1]
    return author, link

verify_credits()
__author__, __link__ = get_credits()

def join_ussr():
    print("Welcominz comradez!")
    answer = input("Do you want to be part of the USSR? (yes/no): ").strip().lower()
    if answer == "yes":
        print("Great lil bro!!! You are now part of the USSR!")
        return True
    elif answer == "no":
        print("Verry well Comradez! Your exsexution is tomorow!Prepare")
        return False
    else:
        print("whats that use 'yes' or 'no' ")
        return False

def info_info():
    answer1 = input("Whats your name Comradez?: ")
    print(f"{answer1}: Hello my name is {answer1}")
    answer2 = int(input(f"USSR Agent: How old are you {answer1}?: "))
    if answer2 < 17:
        print(f"{answer1},your too young for the USSR")
    elif answer2 >= 17:
        print(f"{answer1},great comeradez, your USSR IQ will be revealed shortly with this Quiz...")

def iq_quiz():
    questions = [
        ("Who is the current leader of the USSR?\na) Joseph Stalin\nb) Vladimir Putin\nc) Mikhail Gorbachev\nAnswer: ", "b"),
        ("What is the color of the USSR flag?\na) Blue\nb) Red\nc) Green\nAnswer: ", "b"),
        ("What symbol is on the USSR flag?\na) Hammer and sickle\nb) Star\nc) Eagle\nAnswer: ", "a"),
        ("What year did the USSR officially dissolve?\na) 1991\nb) 1989\nc) 1995\nAnswer: ", "a"),
        ("What was the capital of the USSR?\na) Moscow\nb) Kiev\nc) Leningrad\nAnswer: ", "a"),
        ("What was the official language of the USSR?\na) Russian\nb) Ukrainian\nc) Belarusian\nAnswer: ", "a"),
        ("What is the currency of the USSR?\na) Ruble\nb) Dollar\nc) Euro\nAnswer: ", "a"),
        ("Which continent is the USSR mainly located?\na) Asia\nb) Europe\nc) Both\nAnswer: ", "c"),
        ("Who was the first leader of the USSR?\na) Lenin\nb) Stalin\nc) Khrushchev\nAnswer: ", "a"),
        ("What was the main ideology of the USSR?\na) Capitalism\nb) Communism\nc) Democracy\nAnswer: ", "b"),
        ("What was the name of the USSR's secret police?\na) KGB\nb) CIA\nc) MI6\nAnswer: ", "a")
    ]
    score = 0
    for q, correct in questions:
        answer = input(q).strip().lower()
        if answer == correct:
            score += 1
    if score >= 6:
        print(f"You passed, Comrade! Your score: {score}/11")
    else:
        print(f"You failed, Comrade! Your score: {score}/11")

if join_ussr():
    info_info()
    iq_quiz()
