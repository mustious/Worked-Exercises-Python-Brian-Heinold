import string

lower_ascii = string.ascii_lowercase
digits = string.digits
brace = "("

alg_exp = input("Enter your algebraic expression: ")
len_alg_exp = len(alg_exp) - 1
new_alg_exp = ""

for i in range(len_alg_exp):
    if (alg_exp[i] in digits) and ((alg_exp[i+1] in lower_ascii) or (alg_exp[i+1] == brace)):
        new_alg_exp = new_alg_exp + alg_exp[i] + "*"
    else:
        new_alg_exp += alg_exp[i]
new_alg_exp += alg_exp[-1]
print(new_alg_exp)