import random

def hangman(word):
#wrong   :プレイヤー2が間違えた回数
#hit     :文字を当てた回数
#stages  :吊られた人の文字列を完成させるためのリスト
#rletters:回答の文字列長
#play    :入力回数
#board   :プレイヤー2に見せるヒント
#win     :ゲームの勝敗
    wrong = 0
    hit = 0
    play = 0
    stages = [" _________",
              "|    |    |",
              "|    |    |",
              "|    0    |",
              "|   /|\   |",
              "|   / \   |",
              "|_________|",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("\n")
    print("/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/|")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||")
    print("| Thank you for coming to play \"hangman!\"  ||")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")
    
#code
    while wrong < (len(stages)-1):
        play += 1
        print(" ＿＿＿＿＿＿＿＿")
        print("<   round{}   <".format(play))
        print(" ￣￣￣￣￣￣￣￣")
        
        answer = input("please {} word!".format(hit+1))
        if len(answer) != 1:
            print("\nplease one word only!\n")
            play -= 1
            continue
#正解時
        elif answer in rletters:
            num = rletters.index(answer)
            rletters[num] = "_"
            board[num] = answer
            hit += 1
            if hit != len(rletters):
                print("\" " + " ".join(board) + " \"", end="")
                print(" @ {} word!".format(len(rletters)-hit))
        
#不正解時
        elif answer not in rletters:
            print("\" " + " ".join(board) + " \"", end="")
            print(" @ {} word!".format(len(rletters)-hit))
            wrong += 1
            print("\nmiss count {}".format(wrong))
#ハングマンカウント
            print("\n\"hangman statas\"")
            for miss in range(0, wrong + 1):
                print(stages[miss])
        print("\n")
        
        if "_" not in board:
            print("- - - - - - - - - -")
            print("◆◇◆◇◆◇◆◇◆◇◆")
            print("◇　　　　　　　　　◇")
            print("◆　Ｓｕｃｃｅｓ！　◆")
            print("◇　　　　　　　　　◇")
            print("◆◇◆◇◆◇◆◇◆◇◆")
            print("\nanswer is \"", end = "")
            for ans in board:
                print(ans, end = "")
            print("\" \n")
            break

        elif wrong == (len(stages)-1):
            print("　／＼／＼／＼／＼／＼")
            print("　＞  GAME OVER  ＜")
            print("　＼／＼／＼／＼／＼／")
        
random_list = list()
random_list = ["apple", "grape", "banana", "suica", "melon",
               "peach", "lemon", "cherry", "orange"]

hangman(random.choice(random_list))
