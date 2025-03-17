# 사용한 라이브러리
import random
import time
# from google.colab import output  # colab용 os 대신 사용
from os import system # console 전용(google colab 사용 시 위의 라이브러리 사용)
import base64

from rich.console import Console # 출력문 꾸밀 수 있게 해주는 모듈
console = Console() # Console() 함수를 사용하기 위한 객체 생성

money = 500  # 현재 돈
betting_money = 0  # 베팅 금액
end = ["이런 얌생이 녀석",] # 패배 문자 리스트

# 5ecreT c0De
c0o00o= "c2hvd19tZV90aGVfbW9uZXk="
cOoOOo=c0o00o. encode("ascii")
c0oO0o= base64 .b64decode(cOoOOo)
cOo0Oo =c0oO0o. decode("UTF-8")

# 베팅 금액을 설정하는 함수
def betting():
    # global : 지역변수를 전역변수로 전환
    global money
    global betting_money

    while True:
        use_money = input(f"베팅할 금액을 입력하세요. (올인 하시려면 'all'을 입력하세요.) 보유 자금 : {money}\n>>>")
        if use_money.isdigit(): # isdigit : 문자열이 숫자로 인식될 수 있는지 True 또는 False 반환
            use_money = int(use_money)
            if use_money > money:
                print("베팅금액이 보유한 자금보다 많습니다.")
            elif use_money == 0:
                print("베팅금액이 없습니다.")
            elif use_money <= money:
                money -= use_money
                print(
                    f"성사되었습니다. 보유 자금 : {money} | 베팅 금액 : {use_money}\n"
                )
                break
            else:
                print("에러")

        elif use_money in ['all', 'All','aLL','alL','AlL','ALL','ALl']:
            betting_money = money
            use_money = money
            money = 0

            break

        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
    betting_money = use_money


# 점수 계산 함수
def user_score(cards):
    score = 0 # 계산된 점수
    ace = 0 # ace 개수

    for card in cards:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            ace += 1
        else:
            score += card

    while score > 21 and ace > 0:
        score -= 10
        ace -= 1

    return score


# 게임 진행 함수
def game_start():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"] * 4
    random.shuffle(deck)

    global money
    global betting_money

    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    dealer_score = user_score(dealer_card)

    print(f"플레이어의 카드 : {player_card} | 점수 : {user_score(player_card)}")
    print(f"딜러의 카드 : [{dealer_card[0]}, ?]")

    # 플레이어 턴
    while True:
        hit = input("계속 하시겠습니까?(Y/N) > ")
        if hit in ["N", "n"]:
            # output.clear()
            system('cls')
            print(f"플레이어의 카드 : {player_card} | 점수 : {user_score(player_card)}")
            break
        elif hit in ["Y", "y"]:
            player_card.append(deck.pop())
            print(f"플레이어의 카드 : {player_card} | 점수 : {user_score(player_card)}")
            if user_score(player_card) > 21:
                break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

    # 연출
    print("\n턴 전환중", end="")
    for i in range(3):
        print(".", end="")
        time.sleep(0.3) # 0.3초 정지
    print("\n")

    print("---- 딜러의 턴입니다. ----")

    print(f"딜러의 카드 : {dealer_card} | 점수 : {user_score(dealer_card)}")

    # 딜러의 턴
    while dealer_score <= 16:
        time.sleep(2)
        dealer_card.append(deck.pop())
        print(f"딜러의 카드 : {dealer_card} | 점수 : {user_score(dealer_card)}")
        dealer_score = user_score(dealer_card)

    print()
    if user_score(player_card) > 21:
        console.print("패배했습니다. 플레이어의 점수가 21점을 초과했습니다.",style="bold red",end="\n")
    elif user_score(dealer_card) > 21:
        console.print("승리했습니다. 딜러의 점수가 21점을 초과했습니다.",style="bold green",end="\n")
        money += betting_money * 2
    elif user_score(player_card) > user_score(dealer_card):
        console.print("승리했습니다. 플레이어의 점수가 더 높습니다.",style="bold green",end="\n")
        money += betting_money * 2
    elif user_score(player_card) < user_score(dealer_card):
        console.print("패배했습니다. 딜러의 점수가 더 높습니다.",style="bold red",end="\n")
    else:
        console.print("무승부입니다. 플레이어와 딜러의 점수가 같습니다.",style="bold",end="\n")
        money += betting_money

    betting_money = 0
    print()

# 게임 실행 판단
while True:
    start = input(
        f"룰을 보시려면 help를 입력하시고, 게임을 시작하시려면 (Y,N)을 입력해주세요. 현재 자금 : ${money}\n>>>"
    )

    if start in ["Y", "y"]:
        if money == 0:
            #output.clear()
            system('cls')
            print(random.choice(end))
            break

        else:
            #output.clear()  # colab
            system('cls')
            betting()
            game_start()

    elif start == "help":
        print(
            """
1. J, Q, K는 10점입니다.
2. A는 플레이어의 점수에 따라 1점 또는 11점으로 계산됩니다.
3. 돈을 모두 잃으면 게임을 시작할 수 없습니다. 그러나, 돈을 얻을 방법은 있습니다.
    """
        )
    elif start in ["n", "N"]:
        print("게임을 종료합니다.")
        break
    elif start == cOo0Oo:
        console.print(f"Get ${0x12FD1}!",style="bold green", end="\n")
        money += int(0x12FD1)

    else:
        print("다시 입력하세요.")
