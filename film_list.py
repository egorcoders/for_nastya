import random

OPTIONS = {
    1: 'Купить билет на определенное место',
    2: 'Узнать общее кол-во купленных билетов',
    3: 'Продать "K" любых билетов',
    4: 'Получить свободные ряды',
    5: 'Освободить первый ряд',
    6: 'Разместить семью из "К" человек',
}


def create_list(n: int, m: int) -> list:
    a = list()
    for i in range(n):
        b = list()
        for j in range(m):
            b.append(0)
        a.append(b)
    return a


def print_list(a: list) -> None:
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
    print()


def buy_ticket(a: list, r: int, p: int) -> bool:
    if len(a) > r >= 0 and len(a[0]) > p >= 0 and not a[r][p]:
        a[r][p] = 1
        return True
    return False


def total_places(a, total=0):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0:
                total += 1
    return total


def free_rows(a):
    return sum(i for i in range(len(a)) if sum(a[i]) == 0)


def buy_tickets(a: list, n: int) -> None:
    while i := 0 < n:
        row = random.randint(0, len(a) - 1)
        place = random.randint(0, len(a[0]) - 1)
        if not a[row][place]:
            a[row][place] = 1
            i += 1


def find_free_place(a: list) -> tuple[int, int]:
    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                return i, j
    return -1, -1


def free_first_row(a: list) -> None:
    for j in range(len(a[0])):
        if a[0][j] == 1:
            row, place = find_free_place(a)
            a[row][place] = 1
            a[0][j] = 0


def find_free_place_for_f(a: list, k: int) -> list:
    c = []
    for i in range(len(a)):
        j = 0
        while j < len(a[0]):
            if a[i][j] == 0:
                count = 0
                while j < len(a[0]) and a[i][j] == 0:
                    count += 1
                    j += 1
                if count >= k:
                    c.append(i + 1)
                    break
            else:
                j += 1
    return c


def main():
    n = int(input("Введите количество рядов: "))
    m = int(input("Введите количество мест в ряду: "))
    a = create_list(n, m)
    print('\nВыбранная схема мест кинотеатра:')
    print_list(a)
    while True:
        print('Введите цифру в соответствии с желаемой операцией:')
        for i, v in OPTIONS.items(): 
            print(i, v)
        pos = int(input())
        if pos == 1:
            row = int(input("Укажите ряд\n"))
            place = int(input("Укажите место\n"))
            if buy_ticket(a, row - 1, place - 1):
                print(f"\nВы купили билет на {place} место в {row} ряду")
                print_list(a)
            else:
                print("Данное место занято, выберите другое\n")
        elif pos == 2:
            print(f"Кол-во купленных билетов равно {total_places(a)}")
        elif pos == 3:
            k = int(input("Введите кол-во билетов\n"))
            buy_tickets(a, k)
            print_list(a)
        elif pos == 4:
            print(f"Кол-во свободных рядов равно {free_rows(a)}")
        elif pos == 5:
            free_first_row(a)
            print_list(a)
        elif pos == 6:
            k = int(input("Введите кол-во человек в семье"))
            c = find_free_place_for_f(a, k)
            print(*c)


if __name__ == '__main__':
    main()
