from object.object02 import person


class student(person):
    def study(self):
        print("공부하다.")

lee = student()
print(lee.mouth)
print(lee.study())
print(lee.eat())


kim = student()
print(kim.study())
print(kim.legs)
