import writeField_v1
import writeCsv
from os import listdir
from os.path import isfile, join
mypath = '/Users/emilyzhang/genome-nexus/model/src/main/java/org/cbioportal/genome_nexus/model/my_variant_info_model'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print onlyfiles
def writeClass(filename,data):
    fwrite = open(filename, 'w')
    className = filename[filename.rfind('/')+1:filename.find('.java')]
    out = ['package org.cbioportal.genome_nexus.model.my_variant_info_model;','import org.springframework.data.mongodb.core.mapping.Field;']
    out += ['public class %\n[']
    out += [writeField_v1.initial(data)]
    out += [writeField_v1.method(data)]
    out += [']']
    finalAns = '\n\n'.join(out)
    finalAns = finalAns.replace('%',className)
    finalAns = finalAns.replace('[','{').replace(']','}')
    fwrite.write(finalAns)
    fwrite.close()

for i in onlyfiles:
    filename = mypath + '/' + i
    csvname = i.strip(".java") + '.csv'
    writeCsv.generate_csv(filename, csvname)
    writeClass(filename, csvname)


