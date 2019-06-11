# VocabX

VocabX is a simple python tool that works like flash cards to help you build your vocabulary. It is free and opensourced.

## WINDOW USERS!

If you are using it on Windows, change all `os.system("clear")` into `os.system("cls")`!

## Usage

### Install dependencies

You need `numpy`, `pandas`, `readchar` to use VocabX. Install them using `pip`.

### Create your very own word list

Create your own word list by creating a file named `wordlist.csv`. Each line of the csv should be like "word,explanations". An example of `wordlist.csv` is included.

### Use it!

Run VocabX by typing `python3 learn.py`. Your word list will be shuffled and you will be prompted by each word.

Press `q` to exit VocabX. 

Press `y` to tell you know the word. You will be prompted with the meaning and will be asked if you are sure that you know it. 

Press `l` to tell that you know the word now but would like to see it later to double check. The meaning will have an arrow with it. 

Press any other key to tell you do not know the word. If you do not know the word, the meaning will have an "x" with it and you will see it 10 words later and will have to remember it twice. After that, it will show up once again at the end of the list. The word you do not know will have a star with it.

## Tips

Get a new terminal, set it fullscreen and make font super large to have an immersive learning environment.
