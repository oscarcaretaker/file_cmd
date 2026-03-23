
# File Type Identifier

##  Description

Python program to detect file type using:

* Magic numbers
* ASCII content
* HTML tags
* File properties (symlink, directory)

---

## ▶️ Usage

```bash
python file.py <filename>
MAKE SURE THE PROGRAM FILE IS IN THE cwd.
```

---

## 📂 Supports

* Binary / Executable
* PDF, ZIP
* PNG, JPEG, GIF
* HTML
* ASCII & Empty files
* Symlink
* Directory

---

## 🧪 Test Examples

```bash
echo "Hello" > test.txt         # ASCII
touch empty.txt                 # Empty
echo "<html>" > test.html       # HTML
zip test.zip test.txt           # ZIP
ln -s test.txt link.txt         # Symlink
mkdir testdir                   # Directory
```

Run:

```bash
python file.py <file>
```
