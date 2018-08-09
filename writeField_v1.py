firstUp = lambda x: x[0].upper()+x[1:]
def method(data):
    f_in = open(data, "r")
    f = map(lambda x: x.split(','), f_in.readlines())
    finalAns = []
    for i in f:
        _input = i[0].strip("\"").strip()
        type = i[1].strip()
        field = i[2].strip()
        is_list = i[3].strip()
        ans = "\tpublic {3} get{4}()\n\t[\n\t\treturn {0};\n\t]\n\n\tpublic void set{4}({3} {0})\n\t[\n\t\tthis.{0} = {0};\n\t]"
        if is_list.upper() == "Y":
            l = "List<" + firstUp(_input)+'>'
            ans = ans.format(_input,l,field,type,firstUp(_input))
        else:
            ans = ans.format(_input,_input.capitalize() ,field,type,firstUp(_input))
        ans = ans.replace("[","{").replace(']','}')

        finalAns += [ans]
    return "\n".join(finalAns)

def initial(data):
    '''initializes objects contained in csv'''
    f_in = open(data, "r")
    f = map(lambda x: x.strip().split(','), f_in.readlines())
    finalAns = []
    for i in f:
        _input = i[0].strip("\"")
        type = i[1]
        field = i[2]
        is_list = i[3]
        if is_list.upper() == "Y":
            is_list = 'List'
            ans = "\t@Field(value = \"{2}\")\n\tprivate {1} {0};\n".format(_input,type,field,is_list)
        else:
            is_list = ''
            ans = "\t@Field(value = \"{2}\")\n\tprivate {1} {0};\n".format(_input,type,field,is_list)
        finalAns += [ans]
    return "\n".join(finalAns)
