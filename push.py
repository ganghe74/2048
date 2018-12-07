from model import Model

def up(lists) :
    for k in range(5) :
        for i in range(5) :
            for j in range(6) :
                n = lists[i][j]
                if n == 0 :
                    if lists[i+1][j] != 0 :
                        lists[i][j] = lists[i+1][j]
                        lists[i+1][j] = 0
                elif lists[i][j] == lists[i+1][j] :
                    lists[i][j] = n+n
                    lists[i+1][j] = 0
    return lists


def down(lists, size) :
    for k in range(5) :
        for i in range(5) :
            list = lists[i]
            for j in range(6) :
                n = list[j]
                if i >= size-1 :
                    continue
                if n == 0 :
                    continue
                if lists[i+1][j] == 0 :
                    lists[i+1][j] = n
                    lists[i][j] = 0
                elif lists[i+1][j] == n :
                    lists[i+1][j] += n
                    lists[i][j] = 0
                else :
                    continue
    return lists


def left(lists) :
    for i in lists :
        for k in range(5) :
            for j in range(6) :
                n = i[j]
                if n == 0 :
                    continue
                else :
                    if j-1 < 0 :
                        continue
                    if n == i[j-1] :
                        i[j-1] = n+n
                        i[j] = 0
                    elif i[j-1] == 0 :
                        i[j-1] = n
                        i[j] = 0
                    else :
                        continue
    return lists


def right(lists, size) :
    for i in lists :
        for k in range(size-1) :
            for j in range(size) :
                n = i[j]
                if j == size-1 :
                    continue
                if n == 0 :
                    continue
                if i[j+1] == 0 :
                    i[j+1] = n
                    i[j] = 0
                elif i[j+1] == n :
                    i[j+1] = n+n
                    i[j] = 0
    return lists

if __name__ == '__main__':
    model = Model()
    for i in range(10):
        model.generate(2)
    print("=====Before=====")
    for row in model.field:
        print(row)

    print("\n=====After=====")
    result = left(model.field)
    for row in result:
        print(row)