url = input("Enter website url: ")

print(url)

if url.startswith("http://") or url.startswith("https://"):
    if url.endswith(".com") or url.endswith(".in") or url.endswith(".co"):
        print("valid url")
    else:
        print("make sure your url end with specific domain ")
else:
    print("port not found !!! ")