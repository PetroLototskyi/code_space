def main():
    file = input("File name: ").strip().lower()
    print(evaluate(file))

def evaluate(file):
    extention = file.rfind(".")
    copy=file[extention:len(file)]
    match copy:
        case ".gif":
            return "image/gif"
        case ".jpg":
            return "image/jpeg"
        case ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


main()
