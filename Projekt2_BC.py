"""
projekt2_BC.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Oupic Svoboda
email: tomas.svoboda@ideastatica.com
discord: Tomáš#7986
"""
import random
import time

def vypsani_hlavicky():
    print('Hi there!')
    cara = '-' * 40
    print(cara)
    print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    print(cara)
    print('Enter a number:')
    print(cara)


def vyhodnot_BC(input_numb: str, rnd_numb: int) -> list:
    bulls, cows, i = 0, 0, 0
    for n in input_numb:
        i += 1
        if n in str(rnd_numb):
            if n == (str(rnd_numb))[i - 1]:
                bulls += 1
            else:
                cows += 1
    return [bulls, cows]

def input_seq() -> str:
    incorrect_input = True
    while incorrect_input:
        in_n = input('>>>')
        if in_n == 'q':
            break
        print('Vstup musí být číslo.') if not in_n.isnumeric() else None
        print('Číslo musí mýt 4 znaky dlouhé.') if len(in_n) != 4 else None
        print('Číslo nesmí zažínat nulou.') if in_n[0] == "0" else None
        print('Kazdý znak musí být unikátní.') if len(list(in_n)) != len(set(in_n)) else None
        incorrect_input = False if in_n.isnumeric() and len(in_n) == 4 and in_n[0] != "0" and len(list(in_n)) == len(set(in_n)) else True
    return in_n

def ulozeni_do_txt(file_name: str, guesses: int, el_time: float) -> None:
    first_open = True
    try:
        txt_file = open(file_name, mode="r", encoding='utf-8')
        content = txt_file.read()
        txt_file.close()
        first_open = False
    except FileNotFoundError:
        content = str(guesses) + ' ' + str(el_time)
    content = content if first_open else content + '\n' + str(guesses) + ' ' + str(el_time)
    txt_file = open(file_name, mode="w", encoding='utf-8')
    txt_file.write(content)
    txt_file.close()

def read_and_eval(file_name: str)->list:
    with open (file_name, mode='r', encoding='utf-8') as txt_file:
        content = txt_file.read()
    content = content.split()
    content = [int(x) if x.isnumeric() else float(x) for x in content]
    sum_attempts, avr_attempts, num_attempts, sum_time, avr_time, num_time = 0, 0, 0, 0, 0, 0
    for x in range(0, len(content), 2):
        sum_attempts += content[x]
        num_attempts += 1
        avr_attempts = round(sum_attempts / num_attempts, 1)
    for x in range(1, len(content), 2):
        sum_time += content[x]
        num_time += 1
        avr_time = round(sum_time / num_time, 1)
    return [avr_attempts, avr_time]

def hra():
    hra_bezi, incorrect_rnd, random_numb = True, True, 1111
    while incorrect_rnd:
        if len(list(str(random_numb))) != len(set(str(random_numb))):
            random_numb = random.randint(1000, 9999)
        else: incorrect_rnd = False
    vypsani_hlavicky()
    nGuess = 0
    while hra_bezi:
        nGuess += 1
        start_time = time.time() if nGuess == 1 else start_time
        numb = input_seq()
        if numb == 'q':
            print('Hra byla přerušena uživatelem.')
            break
        BaC = vyhodnot_BC(numb, random_numb)
        bull_text = 'bull' if BaC[0]==1 else 'bulls'
        cow_text = 'cow' if BaC[1]==1 else 'cows'
        print(BaC[0], bull_text, ',', BaC[1], cow_text)
        print('-'*40)
        if BaC[0] == 4:
            hra_bezi = False
            end_time = time.time()
    else:
        final_time = round((end_time - start_time), 1)
        print("Correct, you've guessed the right number")
        print(f"in {nGuess} guesses! And it took only {final_time} seconds.")
        print('-'*40)
        file = 'Bulls and Cows results.txt'
        ulozeni_do_txt(file, nGuess, final_time)
        average = read_and_eval(file)
        print(f"Average number of attempts is {average[0]}.")
        print(f"Average time is {average[1]} seconds.")

if __name__ == '__main__':
    hra()
