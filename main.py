def main():
    get_answer_user()
    check_answer()


def check_answer():
    index = 0

    true_answer = 0
    false_answer = 0

    list_with_wrong_answer = []

    true_answer_real = ["A", "C", "A", "A", "D", "B", "C", "A",
                        "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

    file_with_answer_user = open("answerr_user.txt", "r")

    info = file_with_answer_user.readline()
    info = info.rstrip("\n")
    while info != "":
        if info == true_answer_real[index]:
            true_answer += 1
        else:
            false_answer += 1
            list_with_wrong_answer.append(index)
        index += 1
        info = file_with_answer_user.readline()
        info = info.rstrip("\n")

    print(f"Правильных ответов: {true_answer}")
    print(f"Неправильных ответов: {false_answer}")

    file_with_answer_user.close()


def get_answer_user():
    answer_list = []
    for i in range(20):
        answer_list.append(input("A or B or C or D: "))

    file_answer_user = open("answerr_user.txt", "w")

    for line in answer_list:
        file_answer_user.write(line + "\n")


main()
