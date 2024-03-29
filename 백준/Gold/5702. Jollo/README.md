# [Gold V] Jollo - 5702 

[문제 링크](https://www.acmicpc.net/problem/5702) 

### 성능 요약

메모리: 115172 KB, 시간: 388 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Jollo is a simple card game which the children from Logonia love to play. It is played between two players with a normal deck of 52 cards. In the game, cards are ordered according to their rank and suit, forming a sequence of 52 distinct values.</p>

<p>The game is composed of three rounds, played in a best-of-three series (a player must win two rounds to win the game). At the beginning of the game the deck is shuffled and each player is given a hand of three cards. In each round the players show one card to each other and the player with the highest card wins the round. The cards shown in a round are discarded (i.e., they cannot be shown again).</p>

<p>The King’s son loves to play the game. But he is not very smart, losing frequently to his little sister. And when he loses, he cries so loud no one can stand it. The servant who deals the cards to the Prince and his sister is afraid he will be sent to prison if the Prince continues to lose. The servant is allowed to see every card he deals, and after dealing five cards (three to the Princess and two to the Prince) he wants to know which is the lowest card he should deal to the Prince so that there is no chance he will lose the game, no matter how badly he plays.</p>

### 입력 

 <p>Each test case is given in a single line that contains five distinct integers A, B, C, X and Y , describing the cards dealt to the players. The first three cards are given to the Princess (1 ≤ A, B, C ≤ 52) and the last two cards are given to the Prince (1 ≤ X, Y ≤ 52).</p>

<p>The last test case is followed by a line containing five zeros.</p>

### 출력 

 <p>For each test case output a single line. If there exists a card that will make the Prince win the game no matter how badly he plays, you must print the lowest such a card. Otherwise, print -1.</p>

