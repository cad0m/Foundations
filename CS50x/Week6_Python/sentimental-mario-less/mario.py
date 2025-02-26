# TODO
while True:
    height = input("Give me the pyramid height (1-8): ")
    if height.isdigit():
        height = int(height)
        if 1 <= height <= 8:
            break


dots = height - 1
sharps = height - dots
for i in range(height):
    for j in range(dots):
        print(" ", end="")
    for k in range(sharps):
        print("#", end="")
    print()
    dots = dots - 1
    sharps = 1 + sharps
