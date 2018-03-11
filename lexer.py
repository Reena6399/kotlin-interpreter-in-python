
def tokenize(a,Token):
    keywords=["abstract","actual","annotation","as","as?","break","by","catch","class","companion","const","constructor","continue","crossinline","data","delegate","do","dynamic","else","enum","expect","external","false","field","file","final","field","finally","for","fun","get","if","import","in","!in","infix","init","inline","interface","inner","internal","is","!is","it","lateinit","noinline","null","object","open","operator","out","override","package","param","private","property","protected","public","receiver","reified","return","sealed","set","setparam","super","suspend","tailrec","this","throw","true","try","typealias","val","var","vararg","when","where","while"]
    operators=["+","-","*","/","%","=","+=","-=","*=","/=","%=","++","--","&&","||","!","==","!=","===","!==","<",">","<=",">=","[","]"]
    data_types=["Double","Float","Long","Int","Short","Byte"]
    separator=[",","(",")","{","}",":",";","."]
    for j in a:
        if j in keywords:
            Token.append(j)
        elif j in data_types:
            Token.append(j)
        elif j in operators:
            Token.append(j)
        elif j in separator:
            Token.append(j)
        else:
            n=len(j)
            i=0
            while i<n:
                string=''
                if j[i].isalpha() or j[i].isdigit() or j[i]=="_":
                    while j[i].isalpha() or j[i].isdigit() or j[i]=="_":
                        string+=j[i]
                        i=i+1
                        if i==n:
                            break
                    if string in keywords:
                        Token.append(string)
                    elif string in data_types:
                        Token.append(string)
                    else:
                        Token.append(string)
                elif j[i] in operators:
                    op=''
                    while j[i] in operators:
                        op+=j[i]
                        i+=1
                        if i==n:
                            break
                    if op in operators:
                    	Token.append(op)
                    else:
                    	print("error")
                elif j[i] in separator:
                    Token.append(j[i])
                    i+=1
                elif j[i]==" " or j[i]=="\t":
                	i+=1
                else:
                    print("error")
                    break
	#print(Token)
