def main():
    true_answer_real = ["A", "C", "A", "A", "D", "B", "C", "A",
                        "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    get_answer_of_user()
    # check_answer_of_user(list_answers=true_answer_real)
    # check_mark(list_ans=true_answer_real)
    checkout(list=true_answer_real)


def check_answer_of_user(list_answers):

    # list_answers = [0] * 20

    total_for_mark = 0
    true_answer = 0
    false_answer = 0
    answers = []
    answers_fl = []

    file_with_answer_user = open("answer_user.txt", "r")

    # answers = file_with_answer_user.readlines()

    answers_fl = file_with_answer_user.readline()
    # answers_fl.rstrip("\n")
    index_fl = 0
    index_list = 0
    while index_fl < 20:
        answers += answers_fl
        # answers_fl.rstrip("\n")
        answers.append(answers_fl)
        if answers[index_list] == list_answers[index_list]:
            total_for_mark += 1
            true_answer += 1
        else:
            false_answer += 1
        index_fl += 1
        index_list += 1

        # if answers[index_list] == list_answers[index_list]:
        #     false_answer += 1
        # else:
        #     false_answer += 1
        #     total_for_mark += 1
        #     true_answer += 1

        # index_fl += 1
        # index_list += 1

        answers_fl = file_with_answer_user.readline()
        # if answers[index_list] == list_answers[index_list]:
        #     total_for_mark += 1
        #     true_answer += 1
        # else:
        #     false_answer += 1
        # index_fl += 1
        # index_list += 1

    file_with_answer_user.close()

    # index = 0
    # while index < len(answers):
    #     answers[index] = answers[index].rstrip("\n")
    #     index += 1

    # total_for_mark = 0
    # true_answer = 0
    # false_answer = 0

    #####
    # if answers[0] == list_answers[0]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[1] == list_answers[1]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[2] == list_answers[2]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[3] == list_answers[3]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[4] == list_answers[4]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[5] == list_answers[5]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[6] == list_answers[6]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[7] == list_answers[7]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[8] == list_answers[8]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[9] == list_answers[9]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[10] == list_answers[10]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[11] == list_answers[11]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[12] == list_answers[12]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[13] == list_answers[13]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[14] == list_answers[14]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[15] == list_answers[15]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[16] == list_answers[16]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[17] == list_answers[17]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[18] == list_answers[18]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    # if answers[19] == list_answers[19]:
    #     total_for_mark += 1
    #     true_answer += 1
    # else:
    #     false_answer += 1
    ####

    print(f"Правильных ответов: {true_answer}")
    print(f"Неправильных ответов: {false_answer}")

    if true_answer >= 15:
        print("Вы прошли экзамен!")
    else:
        print("Вы провалили экзамен!")


def get_answer_of_user():
    answer_list = []

    try:
        for line in range(20):
            answersss = input("A or B or C or D: ")
            answer_list.append(answersss)

    except TypeError:
        print("Введи буквенный ответ")

    file_with_user_answer = open("answer_user.txt", "w")

    # file_with_user_answer.writelines(answer_list)
    # file_with_user_answer.write(f"[{answer_list}]")

    for item in answer_list:
        file_with_user_answer.write(str(item) + "\n")

    file_with_user_answer.close()


def check_mark(list_ans):

    total_for_mark = 0
    true_answer = 0
    false_answer = 0
    answers = []
    answers_fl = []
    index = 0
    index_list = 0

    file_with_answer_user = open("answer_user.txt", "r")

    full_mark = file_with_answer_user.readlines()

    while index < 20:

        a = full_mark[index_list]
        b = list_ans[index_list]

        if a == b:
            total_for_mark += 1
            true_answer += 1
        else:
            false_answer += 1
        index_list += 1
        index += 1

    print(f"Правильных ответов: {true_answer}")
    print(f"Неправильных ответов: {false_answer}")

    if true_answer >= 15:
        print("Вы прошли экзамен!")
    else:
        print("Вы провалили экзамен!")


def checkout(list):
    true_answer = 0
    false_answer = 0
    index = 0
    index_list = 0

    file_with_answer_user = open("answer_user.txt", "r")

    full_mark = file_with_answer_user.readline()

    while full_mark != "":
        if full_mark == list[index_list]:
            total_for_mark += 1
            true_answer += 1
            index_list += 1
            full_mark = file_with_answer_user.readline()
        else:
            false_answer += 1

    file_with_answer_user.close()

    print(f"Правильных ответов: {true_answer}")
    print(f"Неправильных ответов: {false_answer}")

    if true_answer >= 15:
        print("Вы прошли экзамен!")
    else:
        print("Вы провалили экзамен!")


main()
