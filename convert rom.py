
from flask import Flask, json

api = Flask(__name__)



def convert_rom(a):
    b = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    c = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    x = []
    for i in range(len(b)):
        d = a//b[i]
        a = a%b[i]
        z= d*c[i]
        x.append(z)
    return("".join(x))
@api.route('/', methods=['POST'])
def con_num ():
    k = request.form.get('roman_num')
    return convert_rom(k)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80)