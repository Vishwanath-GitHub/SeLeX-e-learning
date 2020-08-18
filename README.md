# SeLeX-e-learning

> This hackathon project is in accordance to topics choosen with HAB59. This specifically is made to run on Windows.

The purpose of this project is to build to an E-Learning platform that has two specific aims:
* Better suggestions of the videos demanded by the users. The categories of videos are: Basic, Advanced & Certification.
* Auto-generation of subtitles with the user having the option to just read the subtitles for basic notes of the video instead of watching the videos again and again in case if he/she forgets something.

### Aims explained:
1. A video suggestion system will be built which interprets what the user wants (using filters too). So, if someone wants to learn specifically about something, he/she would get results and suggestions just according to the needs. No more irrelevant stuff. If you want basic knowledge, get basic stuff. If you want advanced course, get advanced-centric course. If you want certification, get a pure-certification course.
2. The auto-generated subtitles/captions (of ‘.srt’ file format) will be stored locally and available with every video. So there will be no need of different attached notes with any video. Also, the users don’t need to scribble through entire videos to re-watch if they missed something or forgot about it.


### Prerequisites (installation needed):
* Python 3.8 or better ([download here](https://www.python.org/downloads/windows/))
* Jetbrains PyCharm 2020.2 or better ([download here](https://www.jetbrains.com/pycharm/download/#section=windows))
* FFMPEG Module for Windows ([download here](https://ffmpeg.zeranoe.com/builds/)) (extract this to the project folder)

### How to Run: 
(do this on Desktop)
* `git clone https://github.com/hackappbuilders/SeLeX-e-learning.git`
* Open cloned folder
* Run this file inside folder: [`sqlite3.exe`](https://github.com/hackappbuilders/SeLeX-e-learning/blob/master/sqlite3.exe)
* Run this command: `.open mydb.db`
* Run this command: `CREATE TABLE users ( uname VARCHAR(30) PRIMARY KEY, password VARCHAR(30) );`
* Open PyCharm and open this project inside it
* Open Settings and inside Python Interpreter, install these modules: ModTkinter, Pyglet, ffmpeg, ffpyplayer
* Inside `SeLeX.py` file, on line number 281, inside `show = find_files(search_results + ".mp4", "C:\\Users\ADMIN\Desktop")`, replace `ADMIN` with your computer's username. (exteremely necessary) 
* Run [`SeLeX.py`](https://github.com/hackappbuilders/SeLeX-e-learning/blob/master/SeLeX.py)

### Open Sources Modules and Projects used:
1. https://github.com/BingLingGroup/autosub (for generation of subtitles)
2. https://github.com/satwikkansal/subtitles_to_plaintext (for removal of time stamp from ".srt" file)

### Technologies & Languages Used:
* Python 3 (with GUI)
* SQLite

_Project is made accordingly to the guidelines given by HAB59!_
