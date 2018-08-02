def web(file,data):
    csvIn = open(data,'r')
    csv = csvIn.readlines()
    csv = map(lambda x: x.split(','), csv)
    fin = open(file,'w')
    className = file[file.rfind('/')+1:file.find('Mixin')]

    ans = ''
    imports = "package org.cbioportal.genome_nexus.web.mixin;\nimport java.util.List;\nimport org.cbioportal.genome_nexus.model.{classname};\nimport com.fasterxml.jackson.annotation.JsonInclude;\nimport com.fasterxml.jackson.annotation.JsonProperty;\nimport io.swagger.annotations.ApiModelProperty;\n"
    body = '\n\n@JsonInclude(JsonInclude.Include.NON_NULL)\npublic class {classname}Mixin\n[\n'
    fields = []
    for i in csv:
        name = i[0].strip('\"')
        type = i[1].strip()
        field = i[2].strip()
        is_list = i[3].lower()
        if is_list == 'Y':
            type = '<List>' + vartype
        fields += ['@ApiModelProperty(value = "{F}", required = false)\nprivate {T} {N};'.format(N = name, T = type, F = field)]
    close = ']'
    ans += imports + body + '\n\n'.join(fields) + close
    fin.write(ans.format(classname = className).replace(']','}').replace('[','{'))
    fin.close()
    csvIn.close()

def service(file,data):
    csvIn = open(data,'r')
    csv = csvIn.readlines()
    csv = map(lambda x: x.split(','), csv)
    fin = open(file,'w')
    className = file[file.rfind('/')+1:file.find('Mixin')]

    ans = ''
    imports = 'package org.cbioportal.genome_nexus.service.mixin;\nimport com.fasterxml.jackson.annotation.JsonIgnoreProperties;\nimport com.fasterxml.jackson.annotation.JsonProperty;'
    body = '\n\n@JsonIgnoreProperties(ignoreUnknown = true)\npublic class {classname}Mixin\n[\n'
    fields = []
    for i in csv:
        name = i[0].strip('\"')
        type = i[1].strip()
        field = i[2].strip()
        is_list = i[3].lower()
        if is_list == 'Y':
            type = '<List>' + vartype
        fields += ['@JsonProperty(value = "{F}", required = true)\nprivate {T} {N};'.format(N = name, T = type, F = field)]
    close = '\n]'
    ans += imports + body + '\n\n'.join(fields) + close
    fin.write(ans.format(classname = className).replace(']','}').replace('[','{'))
    fin.close()
    csvIn.close()






web('/Users/emilyzhang/genome-nexus/web/src/main/java/org/cbioportal/genome_nexus/web/mixin/MutdbMixin.java', 'Mutdbdata.csv')
service('/Users/emilyzhang/genome-nexus/service/src/main/java/org/cbioportal/genome_nexus/service/mixin/MutdbMixin.java','Mutdbdata.csv')
