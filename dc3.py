#mapper_ch.py
import sys

for line in sys.stdin:
    line = line.strip()

    for ch in line:
        if ch != " ":
            print(f"{ch}\t1")



#reducer_ch.py
import sys

current_char = None
count = 0

for line in sys.stdin:

    char, val = line.strip().split("\t")
    val = int(val)

    if char == current_char:
        count += val

    else:

        if current_char:
            print(f"{current_char}\t{count}")

        current_char = char
        count = val

# Last character
if current_char:
    print(f"{current_char}\t{count}")


#---------------------------------------------------------------

#mapper_word.py
import sys

for line in sys.stdin:

    words = line.strip().split()

    for word in words:
        print(f"{word}\t1")


#reducer_word.py
import sys

current_word = None
count = 0

for line in sys.stdin:

    word, val = line.strip().split("\t")
    val = int(val)

    if word == current_word:
        count += val

    else:

        if current_word:
            print(f"{current_word}\t{count}")

        current_word = word
        count = val

# Last word
if current_word:
    print(f"{current_word}\t{count}")