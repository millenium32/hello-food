import random

# 음식리스트 출력 기능
def print_list(foodlist):
    for i, food in enumerate(foodlist):
        print(f"{1+i}. {food}")

# 음식리스트 추천 기능
def print_rand_list(foodlist):
    for i in range(5):
    food=random.choice(foodlist)
    print(f"{i+1}.{food}")

foodlist=["짜장면","짬뽕","탕수육","우동","돈까스"]


for i in range(5):
    food=random.choice(foodlist)
    print(f"{i+1}.{food}")

for i, food in enumerate(foodlist):
    print(f"{1+i}. {food}")

addfood=input("추가 음식 입력:")
print(f"당신이 입력한 내용: {addfood}")
foodlist.append(addfood)

for i, food in enumerate(foodlist):
    print(f"{1+i}. {food}")