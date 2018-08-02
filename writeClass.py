import writeField
def writeClass(filename,data):
    fwrite = open(filename, 'w')
    className = filename[filename.rfind('/')+1:filename.find('.java')]
    out = ['package org.cbioportal.genome_nexus.model;','import org.springframework.data.mongodb.core.mapping.Field;']
    out += ['public class % [']
    out += [writeField.initial(data)]
    out += [writeField.method(data)]
    out += [']']
    finalAns = '\n\n'.join(out)
    finalAns = finalAns.replace('%',className)
    finalAns = finalAns.replace('[','{').replace(']','}')
    fwrite.write(finalAns)
    fwrite.close()
writeClass('/Users/emilyzhang/genome-nexus/model/src/main/java/org/cbioportal/genome_nexus/model/Mutdb.java',"Mutdbdata.csv")
