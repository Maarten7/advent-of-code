
class Snafu():
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return self.number
    
    def __len__(self):
        return len(self.number)
    
    def __getitem__(self, item):
        return self.number[item]

    def __add__(self, other):
        result = ""
        add_list = [self, other]

        j = 0
        while j < max(map(len, add_list)):
            j += 1
            digits = [self.get_digit(num, -j) for num in add_list]

            i = 0
            while i + 1 < len(digits): 
                digit, leap_over = self.add_digit(digits[i], digits[i+1]) 
                digits.append(digit)
                i += 2
                if leap_over:
                    add_list.append(leap_over + j * '0')

            result += digits[-1] 
        return Snafu(result[::-1])

    def add_digit(self, a, b):
            match a,b:
                case '1','=':
                    return '-', ''
                case '1','-':
                    return '0', ''
                case '1', '1':
                    return '2', ''
                case '1', '2':
                    return '=', '1'
                case '2','=':
                    return '0', ''
                case '2','-':
                    return '1', ''
                case '2', '2':
                    return '-', '1'
                case '-', '-':
                    return '=', ''
                case '-', '=':
                    return '2', '-'
                case '=', '=':
                    return '1', '-'
                case '0', _:
                    return b, ''
                case default:
                    return self.add_digit(b, a)
    
    def get_digit(self, number, i):
        try:
            return number[i]
        except IndexError:
            return '0'


som = Snafu('0')
for line in open("advent25.txt"):
    line = line.strip()
    som += Snafu(line)

print(som)