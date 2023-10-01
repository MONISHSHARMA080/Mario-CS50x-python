def print_pyramid(n):
    m=height
    if n<=0:
        return
    print(" "*(n-1),end="")
    print("#"*(m-(n-1)),end="  ")
    print("#"*(m-(n-1)))
    print_pyramid(n-1)

def main():
    while True:
        try:
            n=int(input("HEIGHT OF PYRAMID: "))
            if n > 0 and n < 9:
                return n
        except ValueError:
              print("PLEASE ENTER AN INTEGER")

height =main()

print_pyramid(height)
