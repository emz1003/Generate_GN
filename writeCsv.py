import writeField
## if the file is already written this creates the csv to reformat it
def generate_csv(f, csv_name):
    ans = ''
    fIn = open(f,'r')
    csvIn = open(csv_name, 'w')
    fRead = map(str.strip, fIn.readlines())
    for line in fRead:
        if "private" in line:
            w = line.split()
            typ = w[1]
            name = '"'+ w[2].strip(';') +'"'
            is_list = lambda typ:'y' if 'List' in typ else 'n'
            lis = is_list(typ)
            ans += ','.join([name,typ,change_name(w[2].strip(';')),lis + '\n'])
    csvIn.write(ans)
    csvIn.close()
    fIn.close()

def change_name(name):
    ans = ''
    for i in name:
        if i.isupper():
            ans += '_' + i.lower()
        else:
            ans += i
    return ans

# generate_csv('/Users/emilyzhang/genome-nexus/model/src/main/java/org/cbioportal/genome_nexus/model/my_variant_info_model/Ann.java', 'Ann.csv')




        
            