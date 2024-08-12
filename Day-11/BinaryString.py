def generate_binary(n, s="", last_char=""):
    if len(s) == n:
        print(s)
        return
    generate_binary(n, s + "0", "0")
    if last_char != "1":
        generate_binary(n, s + "1", "1")
N = int(input("Enter length of binary number:"))
generate_binary(N)
