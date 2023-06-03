import ctypes
import pygame
import operator as op
import math
from fractions import Fraction


class Calculator:
    def __init__(self) -> None:
        pygame.init()
        ctypes.windll.user32.SetProcessDPIAware()

        self.screen = pygame.display.set_mode((360, 580))
        self.clock = pygame.time.Clock()
        self.running = True
        self.click = False
        self.mx, self.my = pygame.mouse.get_pos()

        self.calc_mode = 'decimals'
        self.equation = []
        self.equation_length = len(self.equation)
        self.layer = 0
        self.current_char = ''
        self.solution = ''
        self.ops = {
            'sin': math.sin,
            'asin': math.asin,
            'cos': math.cos,
            'acos': math.acos,
            'tan': math.tan,
            'atan': math.atan,
            'log': math.log,
            '^': op.pow,
            'sqrt': math.sqrt,
            '!': math.factorial,
            '/': op.truediv,
            '//': op.floordiv,
            '%': op.mod,
            '*': op.mul,
            '-': op.sub,
            '+': op.add
        }

        self.BLACK = (0, 0, 0)
        self.GREY = (67, 84, 90)
        self.WHITE = (255, 255, 255)
        self.GOLD = (255, 215, 0)
        self.CYAN = (0, 185, 185)
        self.font = pygame.font.Font("digital-7.ttf", 65)
        self.mid_font = pygame.font.Font("digital-7.ttf", 40)
        self.mini_font = pygame.font.Font("digital-7.ttf", 20)

        self.char_list = [
            ['C', '[', ']', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['2nd', '0', '.', '=']
        ]
        self.char2_list = [
            ['del', 'sqrt', '1/x', '//'],
            ['sin', 'asin', 'log', '%'],
            ['cos', 'acos', 'e', '!'],
            ['tan', 'atan', 'pi', '^'],
            ['1st', 'mode', '+/-', '=']
            # Tends to? Variables?
        ]
        self.symbols_list = ['/', '*', '-', '+', '[', '//', '!', '%', '^', ']']
        self.inequalities = ['<', '<=', '>', '>=', '==', '!=']
        self.trig_functions = ['log', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan']

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

        self.disp_rect = pygame.draw.rect(self.screen, self.GOLD, (0, 0, 360, 130), 4, 8)
        self.disp_chars = self.font.render(f"{self.current_char}", True, self.CYAN)
        self.current_page = 1

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
        for operator_type in self.ops:
            equation_segment = [character for character in equation_segment if character != '']
            # print("segment:", equation_segment)
            for index, value in enumerate(equation_segment):
                if value == operator_type:
                    # print(operator_type, self.ops[operator_type])
                    if value == 'log':
                        equation_segment[index + 1] = str(
                            self.ops[operator_type](float(equation_segment[index + 1]), 2))
                        equation_segment[index] = ''
                    elif value in self.trig_functions[1:4]:
                        equation_segment[index + 1] = str(
                            self.ops[operator_type](math.radians(float(equation_segment[index + 1]) % 360)))
                        equation_segment[index] = ''
                    elif value in self.trig_functions[4:]:
                        equation_segment[index + 1] = str(
                            math.degrees(self.ops[operator_type]((float(equation_segment[index + 1])))))
                        equation_segment[index] = ''
                    elif value == 'sqrt':
                        equation_segment[index] = str(math.sqrt(float(equation_segment[index - 1])))
                        equation_segment[index - 1] = ''
                    elif value == '!':
                        equation_segment[index] = str(math.factorial(int(float(equation_segment[index - 1]))))
                        equation_segment[index - 1] = ''
                    elif value != '/':
                        equation_segment[index + 1] = str(
                            self.ops[operator_type](float(equation_segment[index - 1]),
                                                    float(equation_segment[index + 1])))
                        equation_segment[index - 1:index + 1] = [''] * 2
                    else:
                        if self.calc_mode == "fraction":
                            equation_segment[index + 1] = str(
                                Fraction(equation_segment[index - 1], equation_segment[index + 1]))
                            equation_segment[index - 1:index + 1] = [''] * 2
                        else:
                            equation_segment[index + 1] = str(
                                self.ops[operator_type](float(equation_segment[index - 1]),
                                                        float(equation_segment[index + 1])))
                            equation_segment[index - 1:index + 1] = [''] * 2
        equation_segment = ''.join(equation_segment)
        return equation_segment

    def parser(self):
        if "[" in self.equation:
            open_list = []
            open_count = self.equation.count('[')
            close_count = self.equation.count(']')
            if open_count != close_count:
                print('error, unmatched parenthesis')
                return 'Error'
            else:
                for y in range(self.equation_length):
                    if self.equation[y] == "[":
                        open_list.append(y)
                    elif self.equation[y] == "]":
                        self.equation[y] = Calculator.solver(self, self.equation[open_list[-1] + 1:y])
                        self.equation[open_list[-1]:y] = [''] * len(self.equation[open_list[-1]:y])
                        del open_list[-1]
        self.current_char = Calculator.solver(self, self.equation)
        print(self.current_char)
        return self.current_char

    def first_page(self):
        for i in range(4):
            for j in range(5):
                pygame.draw.rect(self.screen, self.CYAN, self.button_list[j][i], 0, 8)
                rectangle = pygame.draw.rect(self.screen, self.GOLD, self.button_list[j][i], 4, 8)
                character = self.mid_font.render(f"{self.char_list[j][i]}", True, self.WHITE)
                self.screen.blit(character, character.get_rect(center=rectangle.center))
                if self.click and rectangle.collidepoint((self.mx, self.my)):
                    if self.char_list[j][i] not in "0123456789." or len(self.current_char) < 11:
                        if self.char_list[j][i] == '2nd':
                            self.current_page = 2
                        elif self.char_list[j][i] == 'C':  # Clear current and equation
                            self.current_char = ''
                            self.equation = []
                        elif self.char_list[j][i] == '=':  # Start calculating
                            if self.equation_length > 0:  # Check for equation
                                if self.current_char != '':  # Add current if filled
                                    self.equation.append(self.current_char)
                                self.current_char = Calculator.parser(self)
                                if len(self.current_char) >= 11:
                                    self.current_char = "{:e}".format(float(self.current_char))
                                    self.current_char = self.current_char[0:4] + self.current_char[-4:]
                                self.equation = []
                        elif self.char_list[j][i] in self.symbols_list[:]:  # For operators and brackets
                            if self.char_list[j][i] == '[':  # Add layer for '['
                                if self.current_char == '':
                                    if self.equation_length > 0:
                                        if self.equation[-1] == ']' or self.equation[-1] == '!':
                                            continue
                                    self.layer += 1
                                else:
                                    continue
                            elif self.char_list[j][i] == ']':  # Remove layer for ']'
                                if self.layer > 0:
                                    if self.equation_length > 0:
                                        if self.equation[-1] in self.symbols_list[:-1] and self.current_char == '':
                                            continue
                                    self.layer -= 1
                                else:
                                    continue
                            elif self.char_list[j][i] == '!':
                                if self.current_char == '':
                                    continue
                            else:
                                if self.current_char == '':
                                    if self.equation_length > 0:
                                        if self.equation[-1] != ']' and self.equation[-1] != '!':
                                            continue
                            if self.current_char != '':  # Append current if filled
                                self.equation.append(self.current_char)
                            self.equation.append(self.char_list[j][i])
                            self.current_char = ''
                        else:  # Extend current number
                            self.current_char += self.char_list[j][i]
                    else:
                        print("character limit reached")

    def second_page(self):
        for i in range(4):
            for j in range(5):
                pygame.draw.rect(self.screen, self.CYAN, self.button_list[j][i], 0, 8)
                rectangle = pygame.draw.rect(self.screen, self.GOLD, self.button_list[j][i], 4, 8)
                character = self.mid_font.render(f"{self.char2_list[j][i]}", True, self.WHITE)
                self.screen.blit(character, character.get_rect(center=rectangle.center))
                if self.click and rectangle.collidepoint((self.mx, self.my)):
                    if self.char2_list[j][i] not in "0123456789." or len(self.current_char) < 11:
                        if self.char2_list[j][i] == '1st':
                            self.current_page = 1
                        elif self.char2_list[j][i] == 'del':
                            if len(self.current_char) > 0:
                                self.current_char = ''
                        elif self.char2_list[j][i] == 'mode':
                            if self.calc_mode == 'decimals':
                                self.calc_mode = 'fractions'
                            else:
                                self.calc_mode = 'decimals'
                        elif self.char2_list[j][i] == '=':  # Start calculating (go to parser)
                            if self.equation_length > 0:  # Check for equation
                                if self.current_char != '':  # Add current if filled
                                    self.equation.append(self.current_char)
                                self.current_char = Calculator.parser(self)
                                if len(self.current_char) >= 11:
                                    self.current_char = "{:e}".format(float(self.current_char))
                                    self.current_char = self.current_char[0:4] + self.current_char[-4:]
                                self.equation = []
                        elif self.char2_list[j][i] == '1/x':
                            if self.current_char != '':
                                if self.equation_length > 0:
                                    if self.equation[-1] == ']' or self.equation[-1] == '!':
                                        print(self.equation)
                                        continue
                            else:
                                continue
                            self.equation.append('[')
                            self.equation.append('1')
                            self.equation.append('/')
                            self.equation.append(self.current_char)
                            self.equation.append(']')
                            self.current_char = ''
                        elif self.char2_list[j][i] in self.symbols_list[:]:  # For operators and brackets
                            if self.current_char != '' or (
                                    self.equation_length > 0 and (
                                    self.equation[-1] == ']' or self.equation[-1] == '!')):
                                # Must fill conditions: there is a current or
                                # there is an equation with the final character being operable (a number)
                                if self.current_char != '':  # Append current if filled
                                    self.equation.append(self.current_char)

                                self.equation.append(self.char2_list[j][i])
                                self.current_char = ''
                        elif self.char2_list[j][i] == 'pi':
                            self.current_char = str(math.pi)[:11]
                        elif self.char2_list[j][i] == 'e':
                            self.current_char = str(math.e)[:11]
                        elif self.char2_list[j][i] == '+/-' and len(self.current_char) > 0:
                            if self.current_char[0] == '-':
                                self.current_char[0] = ''
                            else:
                                self.current_char = '-' + self.current_char
                        elif self.char2_list[j][i] in self.trig_functions:
                            if self.equation_length == 0 or (self.equation[-1] != ']' and self.equation[-1] != '!'):
                                self.equation.append(self.char2_list[j][i])
                                self.equation.append('[')
                                self.layer += 1
                        else:
                            if self.char2_list[j][i] == 'sqrt':
                                if self.equation_length == 0 or (self.equation[-1] != ']' and self.equation[-1] != '!'):
                                    self.equation.append(self.char2_list[j][i])
                                    self.equation.append('[')
                                    self.layer += 1

    def interface(self):
        while self.running:
            self.mx, self.my = pygame.mouse.get_pos()
            Calculator.event_handler(self)
            self.screen.fill(self.WHITE)

            self.disp_rect = pygame.draw.rect(self.screen, self.GOLD, (0, 0, 360, 130), 4, 8)
            self.disp_chars = self.font.render(f"{self.current_char}", True, self.CYAN)
            self.screen.blit(self.disp_chars,
                             self.disp_chars.get_rect(centery=self.disp_rect.centery, right=self.disp_rect.right - 10))

            self.equation_length = len(self.equation)
            if self.current_page == 1:
                Calculator.first_page(self)
            else:
                Calculator.second_page(self)

            string_equation = ''.join(self.equation)
            disp_equation = self.mini_font.render(f"{string_equation}", True, self.CYAN)
            self.screen.blit(disp_equation, disp_equation.get_rect(centery=20, right=self.disp_rect.right - 10))
            disp_layer = self.mini_font.render(f"Layer: {self.layer}", True, self.CYAN)
            self.screen.blit(disp_layer, disp_layer.get_rect(centery=110, left=self.disp_rect.left + 10))
            disp_mode = self.mini_font.render(self.calc_mode, True, self.CYAN)
            self.screen.blit(disp_mode, disp_mode.get_rect(centery=110, right=self.disp_rect.right - 10))

            self.click = False
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    run = Calculator()
    run.interface()
