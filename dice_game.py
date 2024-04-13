import dice

num = input('4,6,8,12,20のどれで勝負しますか？:')#input関数で値(文字列)を受け取る
num = int(num)  #文字列を整数に変換
my_dice = dice.Dice(num)
cpu_dice = dice.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = cpu_dice.shoot()

#出目を画面に出力　数字はstr関数を使って文字列に変更
print('CPU:{}/あなた:{}'.format(cpu_pip,my_pip))
#状況によってメッセージを変える
if my_pip > cpu_pip:
        print('おめでとうございます。あなたの勝ちです！')
elif my_pip < cpu_pip:
        print('残念！あなたの負けです。')
else:
        print('引き分けです。')