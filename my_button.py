import my_calc as cl

display_num = 0
res = 0
pre_ope = ""
tex_num = 0

def calculation():
  global display_num
  global res
  global pre_ope

  if pre_ope == "+" or pre_ope == "":
    res += display_num
  elif pre_ope == "-":
    res -= display_num
  elif pre_ope == "*":
    res *= display_num
  elif pre_ope == "/":
    res /= display_num
    res = int(res)

def set_pre_ope(operator):
  global pre_ope

  if operator == "+":
    pre_ope = "+"
  elif operator == "-":
    pre_ope = "-"
  elif operator == "*":
    pre_ope = "*"
  elif operator == "/":
    pre_ope = "/"

def num_btn(num):
  global display_num

  display_num = display_num * 10 + num
  cl.label["text"] = str(display_num)

def on_ope(operator):
  global display_num
  global res
  global pre_ope
  global tax_num

  calculation()

  if operator != "=":
    set_pre_ope(operator)

  display_num = 0
  cl.label["text"] = str(res)

  if operator == "=":
    tax_num = res
    res = 0
    pre_ope = ""

def on_ac():
  global display_num
  global res
  global pre_ope
  global tax_num

  display_num = 0
  res = 0
  tax_num = 0
  pre_ope = ""

  cl.label["text"] = "0000"

def on_clear():
  global display_num

  display_num = 0
  cl.label["text"] = str(display_num)

def on_tax(rate):
  global tax_num

  if pre_ope == "":
    if rate == 10:
      tax_num *= 1.1       
    elif rate == 8:
      tax_num *= 1.08

    cl.label["text"] = str(int(tax_num))
    tax_num = 0

