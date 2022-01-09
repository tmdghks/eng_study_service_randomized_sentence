import random
import time
import csv

#bringing sentence list from "영어 문장 리스트.txt"
f = open("C:/eng_studying_program/영어 문장 리스트.txt", 'r', encoding="utf8")
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다. 
f.close()

sentence_list = ""
for tmp in lines:
    sentence_list += tmp
sentence_list.replace('’', "'")
sentence_list = sentence_list.split('.')

def making_problem(sentence_str:str):
    sentence_list_shuffled = sentence_str.split()
    random.shuffle(sentence_list_shuffled)
    question = '('
    for sentence_tmp in sentence_list_shuffled:
        question = question + sentence_tmp + '/'
    print('문제: ' + question[:-1] + ')')   

while True:
    start_time = time.time()
    wrong_count = 0
    wrong_sentence_list = []
    sentence = random.choice(sentence_list).lstrip() + '.'
    sentence_list_correct = sentence.split()
    making_problem(sentence)
    answer_bool = False
    while answer_bool is False:
        input_tmp = input("정답을 입력하십시오.")
        answer = input_tmp.split()
        if answer == sentence_list_correct:
            print("정답입니다!")
            answer_bool = True
            end_time = time.time()
        else:
            print("오답입니다.")
            wrong_count += 1
            wrong_sentence_list.append(input_tmp)
    file_input_list = [sentence, wrong_sentence_list, input_tmp, wrong_count, end_time - start_time]
    print("걸린 시간: %.2f초" % str(end_time - start_time))
    f = open('C:/eng_studying_program/student data.csv', 'a', newline='', encoding="utf8")
    wr = csv.writer(f)
    wr.writerow(file_input_list)
    f.close()