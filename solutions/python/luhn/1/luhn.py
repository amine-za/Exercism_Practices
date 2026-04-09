class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num

    def valid(self):
        self.card_number = self.card_number.replace(" ", "")
        if len(self.card_number) <= 1 or not self.card_number.isdigit():
            return False

        # Length of the Card number string 
        num_length = len(self.card_number) - 1 
        
        # Sum of the card_number digits
        sum = 0
        for index, digit in enumerate(reversed(self.card_number)):
            int_digit = int(digit)

            if index % 2 and int_digit != 0: # Check if its a second number AND if digit its not zero
                subtract = 0
                if int_digit > 4:
                    subtract = 9
                int_digit = (int_digit * 2) - subtract

            sum += int_digit
        
        if sum % 10 != 0:
            return False

        return True
