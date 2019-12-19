
def _compare_lists(a, b, order_matters =False):
    if len(a) != len(b):
        return False

    if order_matters:
        for i in range(len(a)):
            if not compare_items(a[i], b[i]):
                return False
    else:
        for i in range(len(a)):
            found = False
            for j in range(len(b)):
                if compare_items(a[i],b[j]):
                    found = True
                    break
            if not found:
                return False
    return True


def _compare_dict(a, b,order_matters =False):
    if len(a) != len(b):
        return False
    for k,v in a.items():
        if k not in b:
            return False
        if not compare_items(v,b[k],order_matters):
            return False
    return True


def compare_items(a, b, order_matters =False):
    if type(a) != type(b):
        return False

    if type(a) == list:
        return _compare_lists(a, b,order_matters)

    if type(a) == dict:
        return _compare_dict(a, b,order_matters)

    return a == b


obj1 = ['1',2,'3']
obj2 = ['1',2,'3']
assert compare_items(obj1,obj2)

obj1 = ['1',2,'3']
obj2 = ['3',2,'1']
assert compare_items(obj1,obj2)

obj1 = [['1',2],'3']
obj2 = ['3',[2,'1']]
assert compare_items(obj1,obj2)


obj1 = { 'a' : {'b':{'c':[1,2] ,'d': [{'e':['f','g']},{'h':8}] }}}
obj2 = {"a":{"b":{"d":[{"h":8},{"e":["g","f"]}],"c":[2,1]}}}
assert compare_items(obj1,obj2)

obj1 = { 'a' : {'b':{'c':[1,2] ,'d': [{'e':['f','g']},{'h':8}] }}}
obj2 = {"a":{"b":{"d":[{"h":8},{"e":["g","f"]}],"c":[2,1]}}}
assert not compare_items(obj1,obj2,order_matters=True)


obj1 = {'1':1,'2':'2','3':[{'1':1,'2':'2','3':[1,2]},{'1':1,'2':'2','3':[2,1]}]}
obj2 = {'1':1,'2':'2','3':[{'1':1,'2':'2','3':[1,2]},{'1':1,'2':'2','3':[1,2]}]}
assert compare_items(obj1,obj2)


