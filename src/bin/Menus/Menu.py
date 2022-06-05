from getpass import getpass
import sys


class Menu:

    def get_exit_choice_number(choices):
        last_number_value = int(choices[len(choices)-1])
        return str(last_number_value+1)

    @staticmethod
    def display_choices(choices):

        for (i, q) in choices.items():
            print(f"{i}-{q}")
        exit_choice_number = Menu.get_exit_choice_number(list(choices.keys()))
        print(f"{exit_choice_number}-exit")

    @staticmethod
    def get_choice(choices):
        exit_choice_number = Menu.get_exit_choice_number(choices)
        choices.append(exit_choice_number)
        res = input("Choose an option")

        for c in choices:
            if str(res) == exit_choice_number:
                sys.exit()
            if str(c) == str(res):
                return str(c)
        print("please enter a valid choice")
        return False

    @staticmethod
    def promt(text, hidden=False):
        if hidden == True:
            res = getpass(text)
            return res
        res = input(text)
        return res
