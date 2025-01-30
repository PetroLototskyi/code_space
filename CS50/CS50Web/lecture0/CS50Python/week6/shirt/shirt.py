import sys

from PIL import Image, ImageOps


def main():
    inspect_argv()  # Checking the command-line arguments
    image = image_exist_open(
        sys.argv[1]
    )  # Try open image of mappet and assign to vareiable
    shirt = image_exist_open(
        "shirt.png"
    )  # Try open image of shirt and assign to vareiable

    size = shirt.size  # get the image size

    # resize image of the mappet to size of the shirt
    resized_image = ImageOps.fit(image, size)

    # pase shirt in resided image file
    resized_image.paste(shirt, shirt)

    # save modefied image
    resized_image.save(sys.argv[2])


def inspect_argv():
    # If there are too few or too many arguments, or the file is not a Python file, exit the program
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if both input and output files have valid extensions
    valid_extensions = {".jpeg", ".jpg", ".png"}
    input_extension = sys.argv[1].lower()[sys.argv[1].rfind(".") :]

    if input_extension not in valid_extensions:
        sys.exit("Invalid input")

    output_extension = sys.argv[2].lower()[sys.argv[2].rfind(".") :]

    if output_extension not in valid_extensions:
        sys.exit("Invalid output")

    # Check if input and output extensions are the same
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")
  
def image_exist_open(name):  # Function to check if the file exists and read its lines
    # If the file does not exist, exit the program

    try:
        image = Image.open(name)
        return image
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
