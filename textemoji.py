# I LOVE SCLUXWARE !!!!!!!!!!!!!!!!!!!
# make a little banner thing for my website because why not !!

import random

# there are six "/ - \" (v) on each side, each v separated by a |, middle has a smiley or something
eyes = ['◑', 'ﾟ', '¯͒˵', 'ˇ', 'ˋ̠', '●', '✪', '꒦', '⟡', '0', 'o', "'", '"', '◐', '-', '◦', '☀', '◕', '⌐■', '■', 'ᕙ', '⇀', '↼', '‶', 'ᕗ', '೭', '੧', '❛', '〜', '✿', '੭', '೨', 'ω','Φ', '⁀','⁕', '⟲', '⟳', '⟴']
mouths = ['෴','˖','_','W','~','•','‿','‸', '●', '✪', '꒦', '⟡', '0', 'o', '-', '◦', '☀', '◕', 'ᕙ', '⇀', '↼', 'ᕗ', '೭', '〜', '✿', 'ω','Φ','⁔', '←', '↑', '→', '↓', '↔', '↕', '↖', '↗', '↘', '↙', '↚', '↛', '↜', '↝']
randomspace = ['', ' '] # this is for between the eyes, mouth, etc



for i in range(9):

    randomeye1 = random.choice(eyes)
    randommouth1 = random.choice(mouths)
    randomeye2 = random.choice(eyes)
    randomspace1 = random.choice(randomspace) # between eye 1 and mouth
    randomspace2 = random.choice(randomspace) # between mouth and eye 2
    randomspace3 = random.choice(randomspace) # between beginning bracket and eye1, eye2 and ending bracket
    # print the guy!!!
    print('(' + randomspace3 + randomeye1 + randomspace1 + randommouth1 + randomspace2 + randomeye2 + randomspace3 + ')') # since this develops a lot of interesting critters, we can also have matching eye sets option
    # print('(' + randomspace3 + randomeye1 + randomspace1 + randommouth1 + randomspace2 + randomeye1 + randomspace3 + ')') # this line has both eyes the same as the first

# print(" / - \ | / - \ | / - \ | / - \ | / - \ | / - \ ( ﾟ෴ﾟ ) / - \ | / - \ | / - \ | / - \ | / - \ | / - \ ")

