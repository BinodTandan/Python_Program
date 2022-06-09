# this = "     hello world    "
# print(this)
# print(this.strip())

def remove_and_strip(string, word):
    newStr = string.replace(word, " ")
    return newStr

this = "     hello world    "
n = remove_and_strip(this, "hello")
print(n)