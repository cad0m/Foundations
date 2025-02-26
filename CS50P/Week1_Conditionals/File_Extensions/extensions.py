def main():
    #taking file_name
    file_name = input("File name: ").lower().strip()

    #trim lasat 3 letter
    file_name = file_name[-3:]

    #finding  right format
    match file_name:
        case "gif" :
            print("image/gif")
        case  "jpg" | "peg":
            print("image/jpeg")
        case "png" :
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt" :
            print("text/plain")
        case "zip" :
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
