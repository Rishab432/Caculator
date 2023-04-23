import pygame
import operator as op
pygame.init()


class Calculator:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((360, 580))
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False
        self.mx, self.my = pygame.mouse.get_pos()

        self.equation = []
        self.current_char = ''
        self.solution = ''
        self.ops = {
            '^': op.pow,
            '/': op.truediv,
            '*': op.mul,
            '-': op.sub,
            '+': op.add
        }

        self.BLACK = (0, 0, 0)
        self.GREY = (67, 84, 90)
        self.WHITE = (255, 255, 255)
        self.GOLD = (255, 215, 0)
        self.CYAN = (0, 185, 185)

        self.char_list = [
            ['C', '[', ']', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['^', '0', '.', '='],
        ]
        self.button_list = [
            [pygame.Rect(0, 130, 90, 90), pygame.Rect(90, 130, 90, 90), pygame.Rect(180, 130, 90, 90),
             pygame.Rect(270, 130, 90, 90)],
            [pygame.Rect(0, 220, 90, 90), pygame.Rect(90, 220, 90, 90), pygame.Rect(180, 220, 90, 90),
             pygame.Rect(270, 220, 90, 90)],
            [pygame.Rect(0, 310, 90, 90), pygame.Rect(90, 310, 90, 90), pygame.Rect(180, 310, 90, 90),
             pygame.Rect(270, 310, 90, 90)],
            [pygame.Rect(0, 400, 90, 90), pygame.Rect(90, 400, 90, 90), pygame.Rect(180, 400, 90, 90),
             pygame.Rect(270, 400, 90, 90)],
            [pygame.Rect(0, 490, 90, 90), pygame.Rect(90, 490, 90, 90), pygame.Rect(180, 490, 90, 90),
             pygame.Rect(270, 490, 90, 90)]
        ]

        self.x_offset = 0
        self.y_offset = 0

        self.font = pygame.font.Font("digital-7.ttf", 65)
        self.mini_font = pygame.font.Font("digital-7.ttf", 20)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def solver(self, equation_segment):
        equation_segment = [character for character in equation_segment if character != '']
        print(equation_segment)
        for operator_type in self.ops:
            for index, value in enumerate(equation_segment):
                if value == operator_type:
                    equation_segment[index - 1] = str(
                        self.ops[operator_type](float(equation_segment[index - 1]), float(equation_segment[index + 1])))
                    del equation_segment[index:index + 2]
            print(equation_segment)
        equation_segment = ''.join(equation_segment)
        return equation_segment

    def parser(self):
        mirror = []

        if "[" in self.equation:
            open_list = []
            current_open = 0
            open_count = self.equation.count('[')
            close_count = self.equation.count(']')
            if open_count != close_count:
                print('error, unmatched parenthesis')
                return 'Error'
            else:
                for x in range(open_count):
                    for y in range(len(self.equation)):
                        if self.equation[y] == "[":
                            open_list.append(y)
                        elif self.equation[y] == "]":
                            mirror.append([open_list[-1], y, Calculator.solver(self, self.equation[open_list[-1]+1:y])])
                            self.equation[y] = Calculator.solver(self, self.equation[open_list[-1]+1:y])
                            self.equation[open_list[-1]:y] = ['']*len(self.equation[open_list[-1]:y])
                            del open_list[-1]
                    # for replacer in mirror:
                    #     if replacer[1] == -1:
                    #         self.equation[replacer[0]] = replacer[2]
                    #         del self.equation[replacer[0] + 1:]
                    #     else:
                    #         self.equation[replacer[0]] = replacer[2]
                    #         del self.equation[replacer[0] + 1:replacer[1] + 1]
                    #     mirror.remove(replacer)
        self.current_char = Calculator.solver(self, self.equation)
        return self.current_char

    def interface(self):
        while self.running:
            self.mx, self.my = pygame.mouse.get_pos()
            Calculator.event_handler(self)
            self.screen.fill(self.WHITE)

            string_equation = ''.join(self.equation)
            disp_rect = pygame.draw.rect(self.screen, self.GOLD, (0, 0, 360, 130), 4, 8)
            disp_chars = self.font.render(f"{self.current_char}", True, self.CYAN)
            self.screen.blit(disp_chars, disp_chars.get_rect(centery=disp_rect.centery, right=disp_rect.right - 10))

            for i in range(4):
                for j in range(5):
                    pygame.draw.rect(self.screen, self.CYAN, self.button_list[j][i], 0, 8)
                    rectangle = pygame.draw.rect(self.screen, self.GOLD, self.button_list[j][i], 4, 8)
                    character = self.font.render(f"{self.char_list[j][i]}", True, self.WHITE)
                    self.screen.blit(character, character.get_rect(center=rectangle.center))
                    if self.click and rectangle.collidepoint((self.mx, self.my)):
                        if disp_chars.get_width() < 340 or self.char_list[j][i] in "^+-*/%C=":
                            if self.char_list[j][i] == 'C':
                                self.current_char = ''
                                if len(self.equation) == 0:
                                    print('error, no values in equation to clear')
                                else:
                                    self.equation = []
                            elif self.char_list[j][i] == '=':
                                if len(self.equation) == 0:
                                    print('error, no values in equation to solve')
                                else:
                                    if self.current_char != '':
                                        self.equation.append(self.current_char)
                                    string_equation = ''.join(self.equation)
                                    print(string_equation)
                                    self.current_char = Calculator.parser(self)
                                    print(self.current_char)
                                    self.equation = []
                            elif self.char_list[j][i] in "^+-*/%[]":
                                if len(self.current_char) <= 0 and self.char_list[j][i] not in "[]":
                                    print('error, no values to use operator on')
                                else:
                                    if self.current_char != '':
                                        self.equation.append(self.current_char)
                                    self.equation.append(self.char_list[j][i])
                                    self.current_char = ''
                            else:
                                self.current_char += self.char_list[j][i]
                        else:
                            print("character limit reached")

            disp_equation = self.mini_font.render(f"{string_equation}", True, self.CYAN)
            self.screen.blit(disp_equation, disp_equation.get_rect(centery=20, right=disp_rect.right - 10))

            self.click = False
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    run = Calculator()
    run.interface()
