def divideVars(vars_info):
    input_Variables = {}
    output_Variables = {}
    external_Variables = {}
    #If there are some external variables save it as well
    if "ext rd" in vars_info:
        externalPart = vars_info.rsplit("ext rd")[1]
        vars_info = vars_info.rsplit("ext rd")[0]
    elif "ext wr" in vars_info:
        externalPart = vars_info.rsplit("ext wr")[1]
        vars_info = vars_info.rsplit("ext wr")[0]
    linewithInputs = vars_info.rsplit('\n')[0]
    linewithOutputs = vars_info.rsplit('\n')[1]
    linewithOutputs = linewithOutputs.replace('\t','').replace('\n','')
    linewithInputs = linewithInputs[linewithInputs.index('(')+1:linewithInputs.index(')')]
    inputList = []
    outputList = []
    split = False
    j=0
    for i,char in enumerate(linewithInputs):
        if char == ':':
            split = True
        if (split and char == ','):
            inputList.append(linewithInputs[j:i].replace(' ',''))
            j=i+1
            split = False
        elif (split and i==len(linewithInputs)-1):
            inputList.append(linewithInputs[j:].replace(' ',''))
            j=0
            split = False
    for group in inputList:
        listwithInputs = group.rsplit(':')
        for i,element in enumerate(listwithInputs):
            if i%2!=0:
                input_Variables[element] = listwithInputs[i-1].rsplit(',')
    for i,char in enumerate(linewithOutputs):
        if char == ':':
            split = True
        if (split and char == ','):
            outputList.append(linewithOutputs[j:i].replace(' ',''))
            j=i+1
            split = False
        elif (split and i==len(linewithOutputs)-1):
            outputList.append(linewithOutputs[j:].replace(' ',''))
            j=0
            split = False
    for group in outputList:
        listwithOutputs = group.rsplit(':')
        for i,element in enumerate(listwithOutputs):
            if i%2!=0:
                output_Variables[element] = listwithOutputs[i-1].rsplit(',')
    for key in input_Variables.keys():
        for i,var in enumerate(input_Variables[key]):
            input_Variables[key][i] = var.replace(' ','')
    for key in output_Variables.keys():
        for i,var in enumerate(output_Variables[key]):
            output_Variables[key][i] = var.replace(' ','')
    #Input and output variables are lists, were the key is the type and inside there's an array with variables of that type
    return input_Variables, output_Variables 