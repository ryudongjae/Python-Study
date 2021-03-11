
class Fridge:
    def __init__(self):
        self.isOpened =False
        self.foods = []

    def open(self):
        self.isOpened = True
        print ('냉장고 문이 열렸습니다.')

    def put(self,thing):
        if self.isOpened:
            self.foods.append(thing)
            print("냉장고 속에 음식이 들어갔습니다.")
        else:
            print("냉장고 문이 닫혀서 넣기가 불가능합니다.")

    def close(self):
        self.isOpened =False
        print("냉장고 문을 닫았습니다.")

    class Food:
        pass

