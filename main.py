"""
Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200
(tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
"""


def exercise_1():
    for i in range(2000, 3200+1):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')


"""
Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, 
phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

"""


def exercise_2(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


"""
Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n 
(bao gồm cả 1 và n) sau đó in ra dictionary này. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
"""


def exercise_3(n):
    square = {}
    for i in range(1, n+1):
        square[i] = i*i
    return square


"""
Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và 
một tuple chứa mọi số.

Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


def exercise_4(s):
    arr = s.split(',')
    tup = tuple(arr)
    print(arr)
    print(tup)


def exercise_4_2(s):
    n = len(s)
    split = [',']
    i = 0
    res = []
    while i < n:
        if s[i] not in split:
            start = i
            while i < n and s[i] not in split:
                i += 1
            end = i
            res.append(s[start:end])
        i += 1
    print(res)
    tup = tuple(res)
    print(tup)


"""
Định nghĩa một class có ít nhất 2 method:

getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

printString: in chuỗi vừa nhập sang chữ hoa.

Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM
"""


def exercise_5():
    class String:
        def __init__(self):
            self.s = ''

        def get_string(self):
            self.s = input('input s')

        def print_string(self):
            print(self.s.upper())

    abc = String()
    abc.get_string()
    abc.print_string()


"""
Viết một ham` tính giá trị bình phương của một số.
"""


def exercise_6(num):
    return num**2


"""
Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài 
cuốn sách. Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python. Yêu cầu của bài tập này là viết 
một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho 
hàm bạn tự định nghĩa.
"""


def exercise_7():
    print(abs.__doc__)
    print(int.__doc__)
    print(exercise_6.__doc__)


"""
Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của 
[(2 nhân C nhân D) chia H]. Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao 
diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
"""


def exercise_9(s):
    import math
    c = 50
    h = 30
    num = s.split(',')
    res = []
    for i in num:
        q = math.sqrt(2*c*int(i)/h)
        res.append(str(int(q)))
    return ','.join(res)


"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng
thứ i và cột thứ j của mảng phải là i*j.
Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def exercise_10(a, b):
    return [[i*j for j in range(b)] for i in range(a)]


"""
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành 
chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
"""


def exercise_11(s):
    arr = s.split(',')
    arr.sort()
    return ','.join(arr)


"""
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình.
Giả sử đầu vào là:
Hello world
Practice makes perfect

Thì đầu ra sẽ là:

HELLO WORLD
PRACTICE MAKES PERFECT
"""


def exercise_12():
    lines = []
    while True:
        line = input().upper()
        lines.append(line)
        if not line:
            break

    for i in lines:
        print(i)


"""
Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp,
sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
Giả sử đầu vào là: hello world and practice makes perfect and hello world again
Thì đầu ra là: again and hello makes perfect practice world
"""


def exercise_13(s):
    split = [' ']
    n = len(s)
    i = 0
    words = []
    while i < n:
        if s[i] not in split:
            start = i
            while i < n and s[i] not in split:
                i += 1
            end = i
            words.append(s[start:end])
        i += 1
    print(words)
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    unique.sort()
    return ' '.join(unique)


"""
Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số
đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
"""


def exercise_15(a, b):
    for i in range(a, b+1):
        digits = [int(num) for num in str(i)]
        if all([digit % 2 == 0 for digit in digits]):
            print(i, end=',')


"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp
cho chương trình: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
"""


def exercise_16(s):
    num = 0
    letter = 0
    special = [' ', '!']
    for i in s:
        if i not in special:
            try:
                int(i)
                num += 1
            except ValueError:
                letter += 1
    print(f"letter = {letter}")
    print(f"num = {num}")


def exercise_16_2():
    s = input("Nhập câu của bạn: ")
    # Bài tập Python 16, Code by Quantrimang.com
    d = {"DIGITS": 0, "LETTERS": 0}
    for c in s:
        if c.isdigit():
            d["DIGITS"] += 1
        elif c.isalpha():
            d["LETTERS"] += 1
        else:
            pass
    print("Số chữ cái là:", d["LETTERS"])
    print("Số chữ số là:", d["DIGITS"])


"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
Giả sử đầu vào là: Quản Trị Mạng
Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8
"""


def exercise_17(s):
    up = 0
    low = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    print(f"up = {up}")
    print(f"low = {low}")


"""
Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.
Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
"""


def exercise_18(a):
    # string
    s = a + int(str(a)*2) + int(str(a)*3) + int(str(a)*4)
    return s


def exercise_18_2(a):
    # math
    n1 = a
    n2 = a*10 + n1
    n3 = a*100 + n2
    n4 = a*100 + n3
    return n1+n2+n3+n4


"""
Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
"""


def exercise_19(s):
    value = s.split(',')
    odd = [i for i in value if int(i) % 2 != 0]
    return ','.join(odd)


"""
Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện 
điều khiển.
Định dạng nhật ký được hiển thị như sau:
D 100
W 200
(D là tiền gửi, W là tiền rút ra).
Giả sử đầu vào được cung cấp là:
D 300
D 300
W 200
D 100
Thì đầu ra sẽ là:
500
"""


def exercise_20():
    total = 0
    while True:
        action = input("input record: D or W: ")
        if action:
            if action[0] == 'D':
                total += int(action[2:])
            else:
                total -= int(action[2:])
        else:
            break
    return total


"""
Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương trình để kiểm tra tính hợp lệ
của mật khẩu mà người dùng nhập vào.

Các tiêu chí kiểm tra mật khẩu bao gồm:

1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 12

Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu
chí trên hay không. Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.

Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345

Thì đầu ra sẽ là: ABd1234@1

"""


def exercise_21(s):
    import string
    passwords = s.split(',')
    alphabet = string.ascii_lowercase
    up_alpha = string.ascii_uppercase
    num = [str(_) for _ in range(10)]
    special = ['$', '#', '@']
    valid = []
    for pas in passwords:
        check = [0 for _ in range(4)]
        for letter in pas:
            if letter in alphabet:
                check[0] += 1
            elif letter in up_alpha:
                check[1] += 1
            elif letter in num:
                check[2] += 1
            elif letter in special:
                check[3] += 1
        if sum(check) in range(6, 13) and all(check):
            valid.append(pas)

    return ','.join(valid)


def exercise_21_2():
    import re
    value = []
    items = [x for x in input("Nhập mật khẩu: ").split(',')]
    # Bài tập Python 21, Code by Quantrimang.com
    for p in items:
        if len(p) < 6 or len(p) > 12:
            continue
        else:
            pass
        if not re.search("[a-z]", p):
            continue
        elif not re.search("[0-9]", p):
            continue
        elif not re.search("[A-Z]", p):
            continue
        elif not re.search("[$#@]", p):
            continue
        elif re.search("\s", p):
            continue
        else:
            pass
        value.append(p)
    print(",".join(value))


"""
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. Tuple 
được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.
Nếu đầu vào là:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Thì đầu ra sẽ là:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""


def exercise_22():
    from operator import itemgetter
    student = []
    while True:
        line = input("")
        if line:
            tup = tuple(line.split(','))
            student.append(tup)
        else:
            break

    student.sort(key=itemgetter(0, 1, 2))
    return student


"""
Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.
"""


def exercise_23(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i


# for i in exercise_23(22):
#     print(i)


"""
Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.
Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Thì output phải là:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""


def exercise_25(s):
    words = s.split(' ')
    frequent = {}
    for i in words:
        if i not in frequent:
            frequent[i] = 1
        else:
            frequent[i] += 1

    for key, value in frequent.items():
        print(f"{key}: {value}")


