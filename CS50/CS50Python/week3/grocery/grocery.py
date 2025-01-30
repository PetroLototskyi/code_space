def main():
    entry={}
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        if item not in entry:
            entry[item] = 1
        else:
            entry[item] +=1

    new_entry=sort(entry)
    for i in new_entry:
        print(f"{new_entry[i]} {i}")


def sort(entry):
    return dict(sorted(entry.items()))
main()
