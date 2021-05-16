class infix_to_postfix:
    precedence = {'^': 5, '.': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}

    def __init__(self):
        self.items = []
        self.size = -1

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size -= 1
            return self.items.pop()

    def isempty(self):
        if(self.size == -1):
            return True
        else:
            return False

    def seek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.size]

    def isOperand(self, i):
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
        else:
            return False

    def infixtopostfix(self, expr):
        postfix = ""
        #   print('postfix expression after every iteration is:')
        for i in expr:
            if(len(expr) % 2 == 0):
                print("Incorrect infix expr")
                return False
            elif(self.isOperand(i)):
                postfix += i
            elif(i in '+-./^'):
                while(len(self.items) and self.precedence[i] <= self.precedence[self.seek()]):
                    postfix += self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o = self.pop()
                while o != '(':
                    postfix += o
                    o = self.pop()
            print(postfix)
            # end of for
        while len(self.items):
            if(self.seek() == '('):
                self.pop()
            else:
                postfix += self.pop()
        return postfix


s = infix_to_postfix()
expr = input('enter the expression ')
result = s.infixtopostfix(expr)
if (result != False):
    print("the postfix expr of :", expr, "is", result)
    postfix = result

print("Entered expression:", expr)
print("Postfix expression:", postfix)


pb = {}
pe = {}
nb = {}
ne = {}
stack = []
j = 0
n = 0

for v in postfix:
    if v >= 'A' and v <= 'Z':
        stack.append(v)
    elif v == '.':
        y = stack.pop()
        l2 = len(y)
        x = stack.pop()
        l1 = len(x)
        if bool(pb) is False:
            pb[x] = 'VDD'
            pb[y] = 'VDD'
            pe[x] = 'Y'+str(j)
            pe[y] = 'Y'+str(j)
            stack.append(x+y)
        else:
            if l1 > 1 and l2 > 1:
                s = ""
                d = ""
                if y[1] in '0123456789':
                    s = pb[y[0]+y[1]]
                    if x[1] in '0123456789':
                        pb[y[0]+y[1]] = pb[x[0]+x[1]]
                        d = pb[x[0]+x[1]]
                    else:
                        pb[y[0]+y[1]] = pb[x[0]]
                        d = pb[x[0]]
                else:
                    s = pb[y[0]]
                    if x[1] in '0123456789':
                        pb[y[0]] = pb[x[0]+x[1]]
                        d = pb[x[0]+x[1]]
                    else:
                        pb[y[0]] = pb[x[0]]
                        d = pb[x[0]]
                for u in pb:
                    if pb[u] == s:
                        pb[u] = d
                if y[l2-1] in '0123456789':
                    s = pe[y[l2-2]+y[l2-1]]
                    if x[l1-1] in '0123456789':
                        pe[y[l2-2]+y[l2-1]] = pe[x[l1-2]+x[l1-1]]
                        d = pe[x[l1-2]+x[l1-1]]
                    else:
                        pe[y[l2-2]+y[l2-1]] = pe[x[l1-1]]
                        d = pe[x[l1-1]]
                else:
                    s = pe[y[l2-1]]
                    if x[1] in '0123456789':
                        pe[y[l2-1]] = pe[x[l1-2]+x[l1-1]]
                        d = pe[x[l1-2]+x[l1-1]]
                    else:
                        pe[y[l2-1]] = pe[x[l1-1]]
                        d = pe[x[l1-1]]
                for u in pe:
                    if pe[u] == s:
                        pe[u] = d
                stack.append(x+y)
            elif l1 > 1:
                if y in pb:
                    y = y+str(n)
                    n = n+1
                if x[1] in '0123456789':
                    pb[y] = pb[x[0]+x[1]]
                else:
                    pb[y] = pb[x[0]]
                if x[l1-1] in '0123456789':
                    pe[y] = pe[x[l1-2]+x[l1-1]]
                else:
                    pe[y] = pe[x[l1-1]]
                stack.append(x+y)
            elif l2 > 1:
                if x in pb:
                    x = x+str(n)
                    n = n+1
                if y[1] in '0123456789':
                    pb[x] = pb[y[0]+y[1]]
                else:
                    pb[x] = pb[y[0]]
                if y[l2-1] in '0123456789':
                    pe[x] = pe[y[l2-2]+y[l2-1]]
                else:
                    pe[x] = pe[y[l2-1]]
                stack.append(y+x)
            else:
                if x in pb:
                    x = x+str(n)
                    n = n+1
                if y in pb:
                    y = y+str(n)
                    n = n+1
                j = j+1
                pb[x] = 'Y'+str(j)
                pb[y] = 'Y'+str(j)
                j = j+1
                pe[x] = 'Y'+str(j)
                pe[y] = 'Y'+str(j)
                stack.append(x+y)
    elif v == '+':
        y = stack.pop()
        l2 = len(y)
        x = stack.pop()
        l1 = len(x)
        if bool(pb) is False:
            pb[x] = 'VDD'
            pe[x] = 'Y'+str(j)
            pb[y] = pe[x]
            j = j+1
            pe[y] = 'Y'+str(j)
            stack.append(x+y)
        else:
            if l1 > 1 and l2 > 1:
                if y[1] in '0123456789':
                    s = pb[y[0]+y[1]]
                else:
                    s = pb[y[0]]
                k = 0
                while k < l2:
                    if k != l2-1 and y[k+1] in '0123456789':
                        b = y[k]+y[k+1]
                        k = k+1
                    else:
                        b = y[k]
                    if pb[b] == s:
                        if x[l1-1] in '0123456789':
                            pb[b] = pe[x[l1-2]+x[l1-1]]
                        else:
                            pb[b] = pe[x[l1-1]]
                    k = k+1
                stack.append(x+y)
            elif l1 > 1:
                if y in pb:
                    y = y+str(n)
                    n = n+1
                if x[l1-1] in '0123456789':
                    pb[y] = pe[x[l1-2]+x[l1-1]]
                else:
                    pb[y] = pe[x[l1-1]]
                j = j+1
                pe[y] = 'Y'+str(j)
                stack.append(x+y)
            elif l2 > 1:
                if x in pb:
                    x = x+str(n)
                    n = n+1
                if y[l2-1] in '0123456789':
                    pb[x] = pe[y[l2-2]+y[l2-1]]
                else:
                    pb[x] = pe[y[l2-1]]
                j = j+1
                pe[x] = 'Y'+str(j)
                stack.append(y+x)
            else:
                if x in pb:
                    x = x+str(n)
                    n = n+1
                if y in pb:
                    y = y+str(n)
                    n = n+1
                j = j+1
                pb[x] = 'Y'+str(j)
                j = j+1
                pe[x] = 'Y'+str(j)
                pb[y] = pe[x]
                j = j+1
                pe[y] = 'Y'+str(j)
                stack.append(x+y)


j = 0
n = 0
u = stack.pop()
if u[len(u)-1] in '0123456789':
    a = u[len(u)-2]+u[len(u)-1]
else:
    a = u[len(u)-1]
s = pe[a]


for v in pe:
    if pe[v] == s:
        pe[v] = 'O'


for v in postfix:
    if v >= 'A' and v <= 'Z':
        stack.append(v)
    elif v == '+':
        y = stack.pop()
        l2 = len(y)
        x = stack.pop()
        l1 = len(x)
        if bool(nb) is False:
            nb[x] = 'GND'
            nb[y] = 'GND'
            ne[x] = 'X'+str(j)
            ne[y] = 'X'+str(j)
            stack.append(x+y)
        else:
            if l1 > 1 and l2 > 1:
                s = ""
                d = ""
                if y[1] in '0123456789':
                    s = nb[y[0]+y[1]]
                    if x[1] in '0123456789':
                        nb[y[0]+y[1]] = nb[x[0]+x[1]]
                        d = nb[x[0]+x[1]]
                    else:
                        nb[y[0]+y[1]] = nb[x[0]]
                        d = nb[x[0]]
                else:
                    s = nb[y[0]]
                    if x[1] in '0123456789':
                        nb[y[0]] = nb[x[0]+x[1]]
                        d = nb[x[0]+x[1]]
                    else:
                        nb[y[0]] = nb[x[0]]
                        d = nb[x[0]]
                for u in nb:
                    if nb[u] == s:
                        nb[u] = d
                if y[l2-1] in '0123456789':
                    s = ne[y[l2-2]+y[l2-1]]
                    if x[l1-1] in '0123456789':
                        ne[y[l2-2]+y[l2-1]] = ne[x[l1-2]+x[l1-1]]
                        d = ne[x[l1-2]+x[l1-1]]
                    else:
                        ne[y[l2-2]+y[l2-1]] = ne[x[l1-1]]
                        d = ne[x[l1-1]]
                else:
                    s = ne[y[l2-1]]
                    if x[1] in '0123456789':
                        ne[y[l2-1]] = ne[x[l1-2]+x[l1-1]]
                        d = ne[x[l1-2]+x[l1-1]]
                    else:
                        ne[y[l2-1]] = ne[x[l1-1]]
                        d = ne[x[l1-1]]
                for u in ne:
                    if ne[u] == s:
                        ne[u] = d
                stack.append(x+y)
            elif l1 > 1:
                if y in nb:
                    y = y+str(n)
                    n = n+1
                if x[1] in '0123456789':
                    nb[y] = nb[x[0]+x[1]]
                else:
                    nb[y] = nb[x[0]]
                if x[l1-1] in '0123456789':
                    ne[y] = ne[x[l1-2]+x[l1-1]]
                else:
                    ne[y] = ne[x[l1-1]]
                stack.append(x+y)
            elif l2 > 1:
                if x in nb:
                    x = x+str(n)
                    n = n+1
                if y[1] in '0123456789':
                    nb[x] = nb[y[0]+y[1]]
                else:
                    nb[x] = nb[y[0]]
                if y[l2-1] in '0123456789':
                    ne[x] = ne[y[l2-2]+y[l2-1]]
                else:
                    ne[x] = ne[y[l2-1]]
                stack.append(y+x)
            else:
                if x in nb:
                    x = x+str(n)
                    n = n+1
                if y in nb:
                    y = y+str(n)
                    n = n+1
                j = j+1
                nb[x] = 'X'+str(j)
                nb[y] = 'X'+str(j)
                j = j+1
                ne[x] = 'X'+str(j)
                ne[y] = 'X'+str(j)
                stack.append(x+y)
    elif v == '.':
        y = stack.pop()
        l2 = len(y)
        x = stack.pop()
        l1 = len(x)
        if bool(nb) is False:
            nb[x] = 'GND'
            ne[x] = 'X'+str(j)
            nb[y] = ne[x]
            j = j+1
            ne[y] = 'X'+str(j)
            stack.append(x+y)
        else:
            if l1 > 1 and l2 > 1:
                if y[1] in '0123456789':
                    s = nb[y[0:1]]
                else:
                    s = nb[y[0]]
                k = 0
                while k < l2-1:
                    if y[k+1] in '0123456789':
                        b = y[k]+y[k+1]
                        k = k+1
                    else:
                        b = y[k]
                    if nb[b] == s:
                        if x[l1-1] in '0123456789':
                            nb[b] = ne[x[l1-2:l1-1]]
                        else:
                            nb[b] = ne[x[l1-1]]
                    k = k+1
                stack.append(x+y)
            elif l1 > 1:
                if y in nb:
                    y = y+str(n)
                    n = n+1
                if x[l1-1] in '0123456789':
                    nb[y] = ne[x[l1-2]+x[l1-1]]
                else:
                    nb[y] = ne[x[l1-1]]
                j = j+1
                ne[y] = 'X'+str(j)
                stack.append(x+y)
            elif l2 > 1:
                if x in nb:
                    x = x+str(n)
                    n = n+1
                if y[l2-1] in '0123456789':
                    nb[x] = ne[y[l2-1]+y[l2-1]]
                else:
                    nb[x] = ne[y[l2-1]]
                j = j+1
                ne[x] = 'X'+str(j)
                stack.append(y+x)
            else:
                if x in nb:
                    x = x+str(n)
                    n = n+1
                if y in nb:
                    y = y+str(n)
                    n = n+1
                j = j+1
                nb[x] = 'X'+str(j)
                j = j+1
                ne[x] = 'X'+str(j)
                nb[y] = ne[x]
                j = j+1
                ne[y] = 'X'+str(j)
                stack.append(x+y)


s = ne[a]
for v in ne:
    if ne[v] == s:
        ne[v] = 'O'


# print("\n", pb, "\n", pe)
# print("\n", nb, "\n", ne)


f = open("out.sim", 'w')

for v in pb:
    l = 'p'+' '+v[0]+' '+pb[v]+' '+pe[v]+' 2 4\n'
    f.write(l)
    l = 'n'+' '+v[0]+' '+nb[v]+' '+ne[v]+' 2 4\n'
    f.write(l)

print("file out.sim created successfully")
f.close()
