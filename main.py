import json


class MorseCodeTranslator:

    def __init__(self):
        self.morse_code_dict = self.get_morse_code()
        self.input_text: str = ""
        self.morse_text: str = ""
        self.exit: bool = False
        print("Welcome\nText to Morse Code Converter\n")

    @staticmethod
    def get_morse_code() -> dict:
        """Reads the morse code data from file morse_code.txt and returns the data as dictionary
        :param: None
        :returns: dictionary
        """
        with open('morse_code.txt', mode='r') as file:
            return json.load(file)

    def get_input(self) -> None:
        """Obtains the input from the user and stores the input as string in the variable input_text
        :param: None:
        :returns: None
        """
        self.morse_text = ""
        self.input_text = input("Please enter the text to be converted (or type '//e' to exit):\n").lower()

    def convert_text(self) -> None:
        """Converts the string in variable input_text in to morse code text and stores it in the variable morse_text
        :param: None
        :returns: None"""
        if self.input_text == "//e":
            self.exit = True
        elif self.input_text:
            self.morse_text = " ".join([self.morse_code_dict[s] for s in self.input_text])

    def print_result(self) -> None:
        """Prints the string stored in the variable morse_text to the user.
        :param:None
        :returns:None"""
        print(self.morse_text)


def main():
    translator = MorseCodeTranslator()
    while not translator.exit:
        translator.get_input()
        translator.convert_text()
        translator.print_result()


if __name__ == "__main__":
    main()
