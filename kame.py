import turtle #turtleモジュールを呼び出す

class Kame(turtle.Turtle):  #turtle.Turtleを親クラスとして継承したKameクラスを定義する
    def __init__(self): #Kameクラスとしての初期化メソッドを定義
        super().__init__()  #親クラスの初期化メソッドを呼び出す
        self.shape('turtle')
        self.shapesize(2,2)