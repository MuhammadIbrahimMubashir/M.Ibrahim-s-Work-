MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

# Example list and main function
def main():
    lst = ['a', 'b', 'c', 'd', 'e']
    shorten(lst)
    print("Final list:", lst)

main()
