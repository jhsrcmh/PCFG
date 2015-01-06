#!/usr/bin/python
# Filename: train.py
# --written by twins in NCI
import types
class PCFGTrainer(object):
    """docstring for PCFGTrainer"""
    Symbol = str
    def __init__(self, model):
        super(PCFGTrainer, self).__init__()
        self.modelname = model

    def train(self, a=[]):
        '''
            train the model with given sentences with grammer
        '''
        has = {}
        for i in a:
            self.walk(self.parse(i), has)
        self.train_temp(has)

    def parse(self, s):
        return self.read_from(self.tokenize(s))

    def tokenize(self, s):
        return s.replace('(',' ( ').replace(')',' ) ').split()

    def read_from(self, tokens):
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF while reading')
        token = tokens.pop(0)
        if '(' == token:
            L = []
            while tokens[0] != ')':
                L.append(self.read_from(tokens))
            tokens.pop(0) 
            return L
        elif ')' == token:
            raise SyntaxError('unexpected )')
        else:
            return self.atom(token)
     
    def atom(self, token):
        return self.Symbol(token)

    #将概率结果用于插入hashmap
    def insert(self, key, hashmap):
        if key in hashmap.keys():
            hashmap[key] = (hashmap.get(key) + 1)
        else:
            hashmap[key] = 1.0

    def insertvalue(self, key, value, hashmap):
        if key in hashmap.keys():
            hashmap[key] = (hashmap.get(key) + value)
        else:
            hashmap[key] = value

    #walk the list and get the hash 
    def walk(self, s, hashmap):
        for i in range(len(s)):
            if type(s[1]) is not types.ListType:
                self.insert(s[0] + '#' + s[1], hashmap)
                break
            else:
                self.insert(s[0] + '#' + s[1][0] + ' ' + s[2][0], hashmap)
                self.walk(s[1], hashmap)
                self.walk(s[2], hashmap)
                break

    #train the PCFG
    def train_temp(self, maps={}):
        first = {} #存储统一规则出现的次数
        last = {}  #存储最后的概率值
        for a in maps.keys():
            tmp = a.split('#')
            self.insertvalue(tmp[0], maps.get(a),first)
        for a in maps.keys():
            tmp = a.split('#')
            self.insertvalue(a, maps.get(a)/first.get(tmp[0]), last)
        f = file(self.modelname, 'w')
        for b in last.keys():
            f.write(b + '#  %s \n' %last.get(b))
        f.close

if __name__ == '__main__':
    a = '(S(NP(DT the)(NN boy))(VP(VP(VBD saw)(NP(DT a)(NN girl)))(PP(IN with)(NP(DT a)(NN telescope)))))'
    b = '(S(NP(DT the)(NN girl))(VP(VBD saw)(NP(NP(DT a)(NN boy))(PP(IN with)(NP(DT a)(NN telescope))))))'
    material = [a, b]
    trainer = PCFGTrainer('model.bin')
    trainer.train(material)