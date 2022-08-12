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