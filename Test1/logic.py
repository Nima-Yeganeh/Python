temp = int(input("What is the temp outside? "))
print(temp)
if temp >= 0 and temp <= 37:
    print("Very good!")
elif temp < 0 or temp > 37:
    print("Very bad!")
