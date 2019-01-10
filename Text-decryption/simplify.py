import sys
def main(argv):
    if len(sys.argv) < 2:
        print("Please use: xx.py filename")
        return
    
    filename=argv[1]#"data/Adam_input.txt"
    text = open(filename, 'r',encoding="utf-8-sig").readlines()
    writefile=open(filename[:-4]+"_simple.txt",'w',encoding="utf-8-sig")
    # print(text)
    chars=list(set(text))
    # print(chars)

    eradicate={'#','[',']','{','}','$','*','_','@','“','”','%','‘','’','/','�','&'}
    for line in text:
        writeline=line
        for i in range(len(line)):
            if line[i] in eradicate:
                writeline=writeline[:i]+' '+writeline[i+1:]
        # print(writeline)
        writefile.write(writeline)
            
    # text.close()
    writefile.close()

main(sys.argv)
