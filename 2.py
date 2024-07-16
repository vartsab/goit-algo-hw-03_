import turtle

def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
        return
    length /= 3.0
    koch_snowflake(length, level-1)
    turtle.left(60)
    koch_snowflake(length, level-1)
    turtle.right(120)
    koch_snowflake(length, level-1)
    turtle.left(60)
    koch_snowflake(length, level-1)

def draw_koch_snowflake(length, level):
    for _ in range(3):
        koch_snowflake(length, level)
        turtle.right(120)

def main():
    # Отримати рівень рекурсії від користувача
    level = int(input("Enter the level of recursion (1-5 is recommended): "))
    
    # Налаштування черепашки
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    
    # Малювати сніжинку Коха
    draw_koch_snowflake(300, level)
    
    # Завершити малювання
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
