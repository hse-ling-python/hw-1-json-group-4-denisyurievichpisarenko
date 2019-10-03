import json
from collections import Counter

def get_list():
    full = []
    for line in open('hw_3_twitter', 'r', encoding='utf-8'):
        full.append(json.loads(line))
    return full

def count_lines(lines):
    num = len(lines)
    return num

def count_del(lines):
    dellist = []
    for line in lines:
        for key, value in line.items():
            if key == "deleted":
                dellist.append(key)
                break
    num = len(dellist)
    return num

def find_lang(lines):
    langs = []
    for line in lines:
        for key, value in line.items():
            if key == "lang":
                langs.append(value)
                break
    mostpop = Counter(langs).most_common(3)
    return mostpop

def pop_user(lines):
    users = []
    pop_users = []
    for line in lines:
        for key, value in line.items():
            if key == "user":
                users.append(value)
                break
    c = Counter(users)
    for key, value in c.items():
        if value > 1:
            pop_users.append(key)
    numpop = len(pop_users)
    return numpop

def main():
    text = get_list()
    amount = count_lines(text)
    print(amount, 'tweets')
    dels = count_del(text)
    perc = dels/amount * 100
    print('deleted tweets: ', perc, '%')
    language = find_lang(text)
    print('most popular languages are: ')
    for lang in language:
        print(lang)
    users = pop_user(lines)
    print('users with more than one tweet: ', users)

if __name__ == '__main__':
    main()

                
