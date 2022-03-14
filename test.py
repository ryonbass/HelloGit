
print ("Hello world")
name = input("あなた誰?>>")
your_age = True
while your_age:
    age = int(input("今何歳?>>"))
    if not(age >= 0 and age <=150):
        print("そんなわけねぇだろ")
    else:
        your_age = False
print("やぁ{},もう{}歳になったんだね.".format(name,age))

print()

your_number  = True  
while your_number:
    x = int(input("好きな自然数を教えて>>"))
    if x % 4 == 0:
        print("奇遇だね！僕も好きな数字だよ!")
        your_number = False
    elif x % 4 != 0:
        print("なるほどね。本当は…4？>>")

print()

print("自己評価を10点満点で教えてください")
scores = []
scores.append(int(input("外見")))
scores.append(int(input("性格")))
scores.append(int(input("経済力")))
if sum(scores) > 24:
    print("外見{}点、性格{}点、経済力{}点".format(scores[0],scores[1],scores[2]))
    print("自信満々やな自分")
elif 10 < sum(scores) <= 24:
    print("外見{}点、性格{}点、経済力{}点".format(scores[0],scores[1],scores[2]))
    print("謙虚やね")
else:
    print("外見{}点、性格{}点、経済力{}点".format(scores[0],scores[1],scores[2]))
    print("まぁ…いいことあるって！")   

print()

fruits_dict = {"りんご":100,"みかん":200,"もも":300}
f_fruits = input("りんご、みかん、もも、どれが好き？>>")
eat = int(input("何個食べれる？>>"))
print(f_fruits)
print(fruits_dict)
if f_fruits in fruits_dict:
    total = fruits_dict[f_fruits] * eat
    print("{}円になります。お買い上げありがとうございます。".format(total))
else:
    print(fruits_dict.get(f_fruits,"ちゃんんと選べ"))
