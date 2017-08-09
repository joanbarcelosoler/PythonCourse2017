
def binarify(num):
    digits = []
    while num > 0:
        a = int(float(num % 2))
        digits.insert(0, a)
        num = (num - a)/ 2
    return digits

def int_to_base(num, base):
    digits = []
    while num > 0:
        a = int(float(num % base))
        digits.insert(0, a)
        num = (num - a)/ base
    digits = str(digits)
    return digits

def base_to_int(string, base):
    digits = []
    st_a = [a for a in string]
    while len(st_a) > 0:
        a = int(st_a.pop(0)) * base**((len(st_a)))
        digits.append(a)
    return sum(digits)

def flexibase_add(str1, str2, base1, base2):
    str1 = str(str1)
    str2 = str(str2)
    num1 = base_to_int(str1, base1)
    num2 = base_to_int(str2, base2)
    result = num1 + num2
    return result 

def flexibase_multiply(str1, str2, base1, base2):
    str1 = str(str1)
    str2 = str(str2)
    num1 = base_to_int(str1, base1)
    num2 = base_to_int(str2, base2)
    result = num1 * num2
    return result 

units = {"0" : "", "1" : "I", "2" : "II", "3" : "III", "4" : "IV", "5" : "V", "6" : "VI", "7" : "VII", "8" : "VIII", "9" : "IX"}
tens = {"0" : "", "1" : "X", "2" : "XX", "3" : "XXX", "4" : "IL", "5" : "L", "6" : "LX", "7" : "LXX", "8" : "LXXX", "9" :"XC"}
hundreds = {"0" : "", "1" : "C", "2" : "CC", "3" : "CCC", "4" : "CD", "5" : "D", "6" : "DC", "7" : "DCC", "8" :"DCCC", "9" :"CM"}
thousands = {"0" : "", "1" : "M", "2" : "MM", "3" : "MMM"}

def romanify(num):
    st_n = '{0:04d}'.format(num)
    st_n = [a for a in st_n]
    roman = thousands[st_n[0]] + hundreds[st_n[1]] + tens[st_n[2]] + units[st_n[3]]
    print roman
