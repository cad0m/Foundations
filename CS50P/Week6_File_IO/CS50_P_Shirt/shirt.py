import sys
from PIL import Image
from PIL import ImageOps


def main():

    valide_format = ["png", "jpeg", "jpg"]

    if len(sys.argv) != 3:

        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(tuple(valide_format)):
        sys.exit("Invalid input ")

    elif sys.argv[1][sys.argv[1].find(".") :] != sys.argv[2][sys.argv[2].find(".") :]:
        sys.exit("Input and output have different extensions ")

    else:
        try:
            apply_shirt(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            sys.exit("File Not Found")


def apply_shirt(apply_to_image, output_name):

    # open images
    prepared = Image.open(apply_to_image)
    shirt = Image.open("shirt.png")

    # extract image size from shirt.png and make input image with the same size
    prepared = ImageOps.fit(prepared, shirt.size)

    # apply overly
    prepared.paste(shirt, shirt)

    # save image
    prepared.save(output_name)


if __name__ == "__main__":
    main()
