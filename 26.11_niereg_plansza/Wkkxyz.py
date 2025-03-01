# def draw_line(tablica):
#     linia = ""
#     wewn = False
#     for i in tablica:
#         if wewn == True:
#             linia += "|"
#             for j in range(0,i):
#                 linia += "_|"
#             wewn = False
#             continue
#         if wewn == False:
#             for j in range(0,i):
#                 linia += "  "
#             wewn = True
#     print(linia)

# tab = [[5,1,4,2], [4,3,1,5], [2,8,1,4], [5,1,4,2]]

# for x in tab:
#     draw_line(x)



def generate_spaces(count):
    return "  " * count


def generate_bar_and_underscores(count):
    return "|" + "_|" * count


def draw_line(tablica):
    linia = ""
    wewn = False

    for i in tablica:
        if wewn:
            linia += generate_bar_and_underscores(i)
            wewn = False
        else:
            linia += generate_spaces(i)
            wewn = True

    print(linia)


def process_table(tab):
    for row in tab:
        draw_line(row)


tab = [[5, 1, 4, 2], [4, 3, 1, 5], [2, 8, 1, 4], [5, 1, 4, 2]]
process_table(tab)