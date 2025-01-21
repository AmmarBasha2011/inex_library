from time import sleep
from sys import stdout

class PrintStyle:
    """This is For Custom Print for Letter"""

    @staticmethod
    def print_one(text: str, second: float = 0.05):
        """This is For Custom Print for Letter

        Args:
            text (str): this is Sentence
            second (float, optional): this is Seconds For Letter. Defaults to 0.05.

        Raises:
            ZeroDivisionError
        """
        
        if len(text) == 0:
            raise ZeroDivisionError
        
        for line in text + '\n':
            stdout.write(line)
            stdout.flush()
            sleep(second)
        
    @staticmethod
    def print_all(text: str, total_time: float = 5):
        """This is For Custom Print for Sentence

        Args:
            text (str): This is Sentence
            total_time (float, optional): This is Seconds For Sentence. Defaults to 5.

        Raises:
            ZeroDivisionError
        """
        
        # حساب الوقت الفاصل بين كل حرف
        if len(text) == 0:
            raise ZeroDivisionError
        else:
            interval = total_time / len(text)
        
        # طباعة النص حرفًا بحرف
        for char in text:
            stdout.write(char)
            stdout.flush()
            sleep(interval)
        
        # طباعة سطر جديد بعد انتهاء النص
        stdout.write('\n')
        stdout.flush()
