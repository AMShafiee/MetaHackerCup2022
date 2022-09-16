def second_friend(case_number):
    R, C = map(int, input().split())

    canvas = [list(input()) for _ in range(R)]
    filled_with = "^"
    if min(R, C) == 1:
        if any(each_space == '^' for row in canvas for each_space in row):
            return "Impossible"
        filled_with = "."
    canvas = [[filled_with for _ in canvas[0]] for _ in canvas]
    return "Possible\n%s" % "\n".join(map(lambda row: "".join(row), canvas))


for case_number in range(int(input())):
    print('Case #%d: %s' % (case_number + 1, second_friend(case_number)))