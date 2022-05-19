questions = ["A.-> expend energy, enjoy groups  B.-> conserve energy, enjoy one-on-one ",
             "A.-> interpret literally B.-> look ",
             "A.-> logical, thinking, questioning B.-> empathetic, feeling, accommodating ",
             "A.-> organised, orderly B.-> flexible, adaptable ",
             "A.-> more outgoing, think out loud B.-> more reserved, think to yourself ",
             "A.-> practical, realistic, experimental B.-> imaginative, innovative, theoretical ",
             "A.-> candid, straight forward, frank B.-> tactful, kind, encouraging ",
             "A.-> plan, schedule B.-> unplanned, spontaneous ",
             "A.-> seek many tasks, public activities, interaction with others B.-> seek private, solitary "
             "activities "
             "with quiet to concentrate ",
             "A.-> standard, usual, conventional B.-> different, novel, unique ",
             "A.-> firm, tend to criticize, hold the line B.-> gentle, tend to appreciate, conciliate ",
             "A.-> regulated,structured B.-> easygoing, live and let live ",
             "A.-> external, communicative, express yourself B.-> internal, reticent,keep to yourself ",
             "A.-> focus on here-and-now B.-> look to the future, global perspective, big-picture ",
             "A.-> tough-minded,just B.-> tender-hearted, merciful ",
             "A.-> preparation, plan ahead B.-> go with the flow, adapt as you go ",
             "A.-> active, initiate  B.-> reflective, deliberate ",
             "A.-> facts, things, what-is B.-> ideas, dreams, what-could-be, philosophical ",
             "A.-> matter of fact, issue-oriented B.-> sensitive, people-oriented, compassionate ",
             "A.-> control,govern B.-> latitude, freedom "]

results = []
questions_lst = []


def welcome_note():
    print("WELCOME TO MYERS BRIGGS QUESTIONNAIRE")
    print("There are 20 questions in this questionnaire")
    print("Kindly pick either A or B for each question")
    print()


def collect_responses():
    for response in questions:
        print(response)
        questions_lst.append(input())


def analyse_responses(start, count_a, count_b):
    for response in questions_lst[start:21:4]:
        if response.lower() == "a":
            count_a += 1
        elif response.lower() == "b":
            count_b += 1
    if count_a > count_b:
        if start == 0:
            results.append("Extrovert")
        if start == 1:
            results.append("Sensor")
        if start == 2:
            results.append("Thinker")
        if start == 3:
            results.append("Judger")
    elif count_b > count_a:
        if start == 0:
            results.append("Introvert")
        if start == 1:
            results.append("Intuitive")
        if start == 2:
            results.append("Feeler")
        if start == 3:
            results.append("Perceiver")


def print_result():
    print("Here is the result:")
    for each in results:
        print(each)


welcome_note()
collect_responses()
analyse_responses(0, 0, 0)
analyse_responses(1, 0, 0)
analyse_responses(2, 0, 0)
analyse_responses(3, 0, 0)
print_result()
