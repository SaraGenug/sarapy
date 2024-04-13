while True:
    while True:
        height = input('身長(m)は?:')
        try:
            len(height) != 0
            height = float(height) / 100
            break
        except:
            print('身長(m)を入力してください！')
            break

    while True:
        try:
            weight = float(input('体重(kg)は?:'))
            #組み込み関数powで累乗を計算します
            bmi = weight / pow(height,2)
            #小数点以下第1位までの出力にフォーマットします
            print('BMI値は{:.1f}です。'.format(bmi))
            if bmi < 18.5:
                print('少し痩せすぎです。')
            elif 18.5 <= bmi < 25.0:
                print('標準的な体型です。')
            elif 25.0 <= bmi < 30.0:
                print('少し太っています。')
            else:
                print('高度の肥満です。')
            break
        except:
            print("What the fuck")
            break
    break