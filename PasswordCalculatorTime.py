#_[N_F]_
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '!', '@',
            '#', '$', '%', '*', '(', ')', '_', '+', '-', '=', '§', ':', '?',
            ';', '/', 'ª', 'º', '°', '>', '<', '.', ',', '|']

password = input("enter the password : ")

length = len(password)
poss = len(alphabet) ** length
time = poss / (2500*length)

print("the max time to unlock this pass word is [ {}h or {}m or {}s ] \nhave {} possibilities"
      .format(int(time / 3600), int(time / 60), int(time), poss))
