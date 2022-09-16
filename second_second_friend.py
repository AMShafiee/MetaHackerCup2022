def get_number_of_possible_tree_neighbors(canvas, x, y, R, C):
    is_neighbor_rock = [0 <= x + x_displacement < R and 0 <= y + y_displacement < C and
                        canvas[x + x_displacement][y + y_displacement] != "#" for x_displacement, y_displacement in NEIGHBORS]
    return sum(is_neighbor_rock)


def second_second_friend(case_number):
    R, C = map(int, input().split())
    canvas = [list(input()) for _ in range(R)]
    altered_canvas = [['#' if each_place ==
                       '#' else '^' for each_place in each_row] for each_row in canvas]
    number_of_possible_tree_neighbors = [
        [get_number_of_possible_tree_neighbors(canvas, x, y, R, C) for y in range(C)] for x in range(R)
    ]
    tree_list_to_be_removed = [
        (x, y) for y in range(C) for x in range(R)
        if number_of_possible_tree_neighbors[x][y] < 2 and altered_canvas[x][y] == "^"
    ]

    for each_tree_place_x, each_tree_place_y in tree_list_to_be_removed:
        if canvas[each_tree_place_x][each_tree_place_y] == "^":
            return "Impossible"
        if altered_canvas[each_tree_place_x][each_tree_place_y] == "^":
            altered_canvas[each_tree_place_x][each_tree_place_y] = "."
            for each_neighbor_x, each_neighbor_y in [
                    (each_tree_place_x + x_displacement,
                     each_tree_place_y + y_displacement)
                    for x_displacement, y_displacement in NEIGHBORS]:
                if 0 <= each_neighbor_x < R and 0 <= each_neighbor_y < C and \
                        canvas[each_neighbor_x][each_neighbor_y] != "#" and \
                        number_of_possible_tree_neighbors[each_neighbor_x][each_neighbor_y] > 1:
                    number_of_possible_tree_neighbors[each_neighbor_x][each_neighbor_y] -= 1
                    if number_of_possible_tree_neighbors[each_neighbor_x][each_neighbor_y] < 2:
                        tree_list_to_be_removed.append(
                            (each_neighbor_x, each_neighbor_y))
    return "Possible\n%s" % "\n".join(map(lambda row: "".join(row), altered_canvas))


NEIGHBORS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for case_number in range(int(input())):
    print('Case #%d: %s' % (case_number + 1, second_second_friend(case_number)))
