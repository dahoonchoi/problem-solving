import sys
n = int(sys.stdin.readline())
answer = n
count = 0

while True:
    answer = ((answer//10) + (answer%10))%10 + (answer%10)*10 
    count += 1
    if n == answer :
        break 
print(count)
