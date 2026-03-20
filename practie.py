def is_html(file_path):
    with open(file_path, "rb") as f:
        data = f.read(200).lower()  # read first part

    return b"<html" in data or b"<!doctype html" in data
x = is_html("/home/thatguyaman/Desktop/os/assigment_2/html.html")
print(x)