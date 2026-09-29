import math

# Work with file

def read(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

def write(file_name, content):
    with open(file_name, "a+") as file:
        return file.write(content + "\n")

def create(file_name):
    with open(file_name, "a+") as file:
        file.write("")

def delete(file_name, content):
    with open(file_name, "r") as file:
        text = file.read()
        rep = text.replace(content, "")
    with open(file_name, "w") as file:
        file.write(rep)

# ------------------------------------------------------------

# work with numbers

def number(num):

    num = int(num)

    if 999 > num >= 1:

        if int(str(num)[0:]) >= 500:
            num += 500
            num = str(num)
            print(f"Result : {num[0]}k")
        else:
            print(f"Result : {num}")

    elif 9999 > num >= 1000:

        if int(str(num)[1:]) >= 500:
            num =  int(num)
            num += 500
            num = str(num)
            print(f"Result : {num[0]}k")
        else:
            num = str(num)
            print(f"Result : {num[0]}k")

    elif 99_999 > int(num) >= 10_000:
        if int(str(num)[2:]) >= 500:
            num = int(num)
            num += 500
            num = str(num)
            print(f"Result : {str(num[0:2])}k")
        else:
            print(f"Result : {str(num)[0:2]}k")

    elif 999_999 > num >= 100_000:
        if int(str(num)[3:]) >=500:
            num = int(num)
            num += 500
            num = str(num)
            print(f"Result : {num[0:3]}k")
        else:
            num = str(num)
            print(f"Result : {num[0:3]}k")

    elif 9_999_999 > num >= 1_000_000:

        if int(str(num)[1:]) >= 500_000:
            num = int(num)
            num += 500_000
            num = str(num)
            print(f"Result ; {num[0]}M")
        else:
            num = str(num)
            print(f"Result : {num[0]}M")

    elif 99_999_999 > num >= 10_000_000:

        if int(str(num)[2:]) >= 500_000:
            num = int(num)
            num += 500_000
            num = str(num)
            print(f"Result : {str(num)[0:2]}M")
        else:
            print(f"Result : {str(num)[0:2]}M")

    elif 999_999_999 > num >= 100_000_000:

        if int(str(num)[3:]) >= 500_000:
            num = int(num)
            num += 500_000
            num = str(num)
            print(f"Reuslt : {num[0:3]}M")

    elif 9_999_999_999 > num >= 1_000_000_000:

        if int(str(num)[1:]) >= 500_000_000:
            num = int(num)
            num += 500_000_000
            num = str(num)
            print(f"Result : {num[0]}B")
        else:
            print(f"Result : {str(num)[0]}B")


# math

def Pythagoras(line_1, line_2, vatar):

    if vatar is None and line_1 is not None and line_2 is not None:
        calculation = (line_1 ** 2) + (line_2 ** 2)
        calculation = math.sqrt(calculation)

        if int(str(calculation)[-1]) == 0:
           
           calculation = int(calculation)
           print(calculation)
           print(f"This result number is type of {str(type(calculation))[8:11]}")

        elif type(calculation) is float:

            calculation = float(calculation)
            print(float(str(calculation)[0:5]))
            print(f"This result number is type of {str(type(calculation))[8:13]}")

    if line_1 is None and line_2 is not None and vatar is not None:
        calculation = (vatar ** 2) - (line_2 ** 2)
        calculation = math.sqrt(calculation)

        if int(str(calculation)[-1]) == 0:
           calculation = int(calculation)
           print(calculation)
           print(f"This result number is type of {str(type(calculation))[8:11]}")

        else:

            calculation = float(calculation)
            print(float(str(calculation)[0:5]))
            print(f"This result number is type of {str(type(calculation))[8:13]}")

    if line_1 is not None and line_2 is None and vatar is not None:
        calculation = (vatar ** 2) - (line_1 ** 2)
        calculation = math.sqrt(calculation)

        if int(str(calculation)[-1]) == 0:
           
           calculation = int(calculation)
           print(calculation)
           print(f"This result number is type of {str(type(calculation))[8:11]}")

        else:

            calculation = float(calculation)
            print(float(str(calculation)[0:5]))
            print(f"This result number is type of {str(type(calculation))[8:13]}")


def squared(get_number):
    return get_number ** 2

def cubed(get_number):
    return get_number ** 3


def radical(get_number):
    get_number = get_number ** 0.5

    if int(str(get_number)[-1]) == 0:
        return int(get_number)
    else:
        return float(str(get_number)[0:4])

