# BlackJack - Python
A console-based Blackjack game written in Python. Players can bet virtual money, play against a dealer, and experience basic Blackjack mechanics in the terminal.
## Features
- Console-based Blackjack game
- Supports betting, including “all-in”
- Calculates Ace values dynamically (1 or 11)
- Dealer follows standard Blackjack rules (hits until reaching 17)
- Win, loss, or tie outcomes are reflected in player’s money
- Secret cheat code for bonus money
## Requirements
- Python 3.6 or higher
[Rich](https://pypi.org/project/rich/) library for styled console output
Install dependencies:
```
pip install rich
```
## How to Run
Run the Python script in a terminal or console:
```
python blackjack.py
```
## How to Play
1. The game starts by asking if you want to view rules or start playing.
2. Set your betting amount. You can enter a number or type `all` to bet all your money.
3. Player receives two cards and decides whether to “hit” (draw another card) or “stand” (keep current hand).
4. Dealer draws cards automatically according to Blackjack rules.
5. The outcome is determined:
    - Player wins, loses, or ties.
    - Player’s money is updated accordingly.
### Rules
- J, Q, K count as 10 points
- Ace (A) counts as 1 or 11 points, depending on hand
- If player money reaches 0, the game ends

### Cheat Code
- Enter a hidden code (base64-encoded) during input to receive a money bonus.

## Example
```
    Current money: $500
    Enter your bet (or type 'all' to bet all): 100
    Player cards: ['K', 7] | Score: 17
    Dealer cards: ['9', ?]
    Hit or Stand? (Y/N) > Y
    ...
```
## License
This project is open source and available under the MIT License.
