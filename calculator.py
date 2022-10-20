import pygame
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod
}

pygame.init()

WIDTH = 280
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
GREY = (67, 84, 90)
WHITE = (255, 255, 255)
ORANGE = (245, 153, 7)
BLUE = (5, 80, 195)

x_offset = 0
y_offset = 0

font = pygame.font.SysFont(None, 40)
largefont = pygame.font.SysFont(None, 70)
def number_image():
    display_num = font.render(str(num_value), True, WHITE)
    screen.blit(display_num, (x_offset, y_offset))
display_num0 = font.render("0", True, WHITE)
display_val_plus = font.render("+", True, WHITE)
display_val_minus = font.render("-", True, WHITE)
display_val_multiply = font.render("*", True, WHITE)
display_val_divide = font.render("/", True, WHITE)
display_val_equals = font.render("=", True, WHITE)
equation = ""
values = []
op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
num_of_operation = [op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11]
def total():
    i = 0
    op_number = 0
    for i in len(values):
        if values[i] == "+":
            num_of_operation[op_number] = ops["+"]
            op_number += 1
def equation_comp():
    i = 0
    equation = ""
    for i  in len(values):
        equation += values[i]
        i += 1
    print(equation)

def eval_equation():
    print(total(values))
number = ""


click = False
running = True
while running:
    mx, my = pygame.mouse.get_pos()

    screen.fill(WHITE)

    for x_offset in range(0, 210, 70):
        for y_offset in range(240, 480, 60):
            pygame.draw.rect(screen, GREY, [x_offset, y_offset, 70, 60])
            pygame.draw.rect(screen, WHITE, [x_offset, y_offset, 70, 60], 2)
    for x_offset in range(0, 210, 140):
        pygame.draw.rect(screen, BLUE, [x_offset, 420, 70, 60])
        pygame.draw.rect(screen, WHITE, [x_offset, 420, 70, 60], 2)
    for x_offset in range(0, 280, 70):
        pygame.draw.rect(screen, BLUE, [x_offset, 180, 70, 60])
        pygame.draw.rect(screen, WHITE, [x_offset, 180, 70, 60], 2)
    for y_offset in range(240, 480, 60):
        pygame.draw.rect(screen, ORANGE, [210, y_offset, 70, 60])
        pygame.draw.rect(screen, WHITE, [210, y_offset, 70, 60], 2)
    for x_offset in range(27, 220, 70):
        for y_offset in range(257, 430, 60):
            num_value = int(x_offset/70 + (y_offset-257)/20 + 1)
            number_image()
    screen.blit(display_num0, (97, 437))
    screen.blit(display_val_plus, (display_val_plus.get_rect(center = screen.get_rect().center)[0]+105, 252))
    screen.blit(display_val_minus, (display_val_plus.get_rect(center = screen.get_rect().center)[0]+107, 316))
    screen.blit(display_val_multiply, (display_val_plus.get_rect(center = screen.get_rect().center)[0]+107, 382))
    screen.blit(display_val_divide, (display_val_plus.get_rect(center = screen.get_rect().center)[0]+108, 437))
    screen.blit(display_val_equals, (display_val_equals.get_rect(center = screen.get_rect().center)[0]+105, 192))
    
    number1 = pygame.Rect(0, 240, 70, 60)
    number2 = pygame.Rect(70, 240, 70, 60)
    number3 = pygame.Rect(140, 240, 70, 60)
    number4 = pygame.Rect(0, 300, 70, 60)
    number5 = pygame.Rect(70, 300, 70, 60)
    number6 = pygame.Rect(140, 300, 70, 60)
    number7 = pygame.Rect(0, 360, 70, 60)
    number8 = pygame.Rect(70, 360, 70, 60)
    number9 = pygame.Rect(140, 360, 70, 60)
    number0 = pygame.Rect(70, 420, 70, 60)
    val_plus = pygame.Rect(210, 240, 70, 60)
    val_minus = pygame.Rect(210, 300, 70, 60)
    val_multiply = pygame.Rect(210, 360, 70, 60)
    val_divide = pygame.Rect(210, 420, 70, 60)
    val_equals = pygame.Rect(210, 180, 70, 60)

    if number1.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(1)
                number += "1"
    elif number2.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(2)
                number += "2"
    elif number3.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(3)
                number += "3"
    elif number4.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(4)
                number += "4"
    elif number5.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(5)
                number += "5"
    elif number6.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(6)
                number += "6"
    elif number7.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(7)
                number += "7"
    elif number8.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(8)
                number += "8"
    elif number9.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(9)
                number += "9"
    elif number0.collidepoint((mx, my)):
        if click:
            if input_number_rect.left > 20:
                print(0)
                number += "0"
    elif val_plus.collidepoint((mx, my)):
        if click:
            print("+")
            values.append(number)
            # values.append(operator.add)
            # eval_equation()
    elif val_minus.collidepoint((mx, my)):
        if click:
            print("-")
            values.append(number)
    elif val_multiply.collidepoint((mx, my)):
        if click:
            print("*")
            values.append(number)
    elif val_divide.collidepoint((mx, my)):
        if click:
            print("/")
            values.append(number)
    elif val_equals.collidepoint((mx, my)):
        if click:
            print("=")
            print(values)
            equation_comp()
    input_number = largefont.render(number, True, BLUE)
    input_number_rect = input_number.get_rect()
    input_number_rect.right = 275
    input_number_rect.bottom = 100
    screen.blit(input_number, (input_number_rect))


    click = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

"""
make the function check for open brackets and corresponding close brackets
((3+2)/5)+(2+2)*2
12   2  1 3   3
"""
