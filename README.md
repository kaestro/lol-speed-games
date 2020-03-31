# lol speed game

speed game is guessing game from given data to only one person who
describes what he/she has seen.

As a toy project I decided to make some speed games from data of lol.

## 4 types
1. prototype
2. skill-audio
3. champion-voice
4. partial image

### prototype

* Get a champion's name from https://www.op.gg/statistics/champion/
* Pop random champion's name up for 30 seconds.
* Has the button Correct. Hit this will make score += 10
* Scoreboard

- Todo: Decide which GUI to use.

### skill-audio

* https://www.op.gg/statistics/champion/ provides champion skill sound effects.
* pick random champion, play skill effects sequentially from passive
to ult for 10 seconds.
* Correct person gets the point differently by on which sound he/she
got it correctly.
* Needs button for each person

### champion-voice

* namu.wiki provides a page where it gathered link to youtube of
champion voices.
* little adjustment from skill-audio version.
* instead of passive to ult, give score differently by how long the
person got the champion correctly.

### partial image

* pick random image of a champion.
* reveal a part of that image.
* increment the revealed part of the image and decrement the scores

## Libraries
* requests
* BeautifulSoup