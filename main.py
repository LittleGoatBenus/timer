import time

print("""
Hi, this is a smple timer using the time module

""")


length = int(input("how long will you be timing for in seconds "))


running = True
second = 0


while running:

    for i in range(length):

        time.sleep(1)
        length -= 1

        print(length)

        if length == 0:
            print("timer finished")
            break
