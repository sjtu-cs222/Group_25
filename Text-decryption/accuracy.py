import sys
def main(argv):
    if len(sys.argv) < 2:
        print("Please use: xx.py filename")
        return
    filename=argv[1]#"data/Adam_input_simple.txt"
    solution=filename[:-4]+"_scrambled_result.txt"

    correctfile = open(filename, 'r',encoding="utf-8-sig").read()
    sol_file=open(solution,'r',encoding="utf-8-sig").read()

    cnt=0
    for i in range(len(correctfile)):
        if correctfile[i]!=sol_file[i]:
            cnt+=1
    print(cnt)
    print(1-float(cnt)/float(len(correctfile)))

main(sys.argv)