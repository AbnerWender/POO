import random 
def embaralhar(algo):
    naosei= "".join(random.sample(algo,len(algo)))
    return print(naosei)


embaralhar(algo='python')