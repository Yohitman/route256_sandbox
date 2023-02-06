slovar = []
result = {}
for n in range(int(input())):
    slovar.append(input())
for q in range(int(input())):
    test = input()
    if test != slovar[0]:
        result[test] = (slovar[0], 0)
    else:
        result[test] = (slovar[1], 0)
    for word in slovar:
        if word == test:
            continue
        if len(test) > len(word):
            for i in range(len(word)):
                if test.endswith(word[i:]):
                    if max(len(word[i:]), result[test][1]) == len(word[i:]):
                        result[test] = (word, len(word[i:]))
                        break
                    else:
                        break
        else:
            for i in range(len(test)):
                if word.endswith(test[i:]):
                    if max(len(test[i:]), result[test][1]) == len(test[i:]):
                        result[test] = (word, len(test[i:]))
                        break
                    else:
                        break
    print(result[test][0])
