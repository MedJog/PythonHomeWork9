# Задача с собакой и друзьями.
# Два друга движутся навстречу с заданной скоростью. У них есть собака. 
# Когда друзья начинают свой путь, собака бежит от одного друга к другому, 
# добегает, разворачивается и тут же бежит обратно. 
# Сколько раз собака перебежит от одного друга к другому, пока они не встретятся?

#distance = 10000
#first_friend_speed = 5
#second_friend_speed = 2
#dog_speed = 10
class DogFriends:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def run(self):
        return f'{self.name} движется со скоростью {self.speed}'

first_friend = DogFriends('Пётр', 5)
second_friend = DogFriends('Павел', 2)
dog = DogFriends('Шарик', 10)


first_friend_speed = getattr(first_friend, 'speed')
second_friend_speed = getattr(second_friend, 'speed')
dog_speed = getattr(dog, 'speed')


def dog_run(distance: int, first_friend_speed: int, second_friend_speed: int, dog_speed: int):
    second_friend = True
    count = 0
    time = 0
    while distance > 10:
        if second_friend == True:
            time = distance / (second_friend_speed + dog_speed)
        else:
            time = distance / (first_friend_speed + dog_speed)
        distance = distance - (first_friend_speed + second_friend_speed) * time
        count += 1
    print(f'Шарик успеет пробежать между друзьями {count} раз.')


print(first_friend.run())
print(second_friend.run())
print(dog.run())

distance = int(input('Введите значение расстояния мужду друзьями: '))
dog_run(distance,first_friend_speed, second_friend_speed,dog_speed)