import webbrowser

def RunCode():
    updates = input("[ WHAT'S NEW IN TUMC? ]\nBiggest update to TUMC so far...\n\n[ Pong Minigame by Norb ]\nPlay Pong on the Command Prompt. Yes, you heard this right!!!\nNote that this only runs on Windows.\nCheck README.md for more info.\n\n[ This Section ]\nYeah, that's right! Now, this app comes with a ''What's new?'' section!\n\n[ AT GITHUB ]\nFor more info, check https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection.\n\nThanks for downloading this project.\n\nMade by MF366.\n\n< Press ENTER to go to the repo. >\n< Type 'quit' and hit ENTER to quit the app. >\n\nYour choice: ")
    if updates == 'quit':
        quit()
    else:
        webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection')
    