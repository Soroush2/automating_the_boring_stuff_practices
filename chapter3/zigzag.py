import sys,time
indentIncreasing = True
indent=0
while True:
    try:

        time.sleep(0.05)
        print(' '*indent, end='')
        print('********')
        if indentIncreasing:
            indent +=1
            if indent ==20: 
                indentIncreasing =False
        else:
            indent -=1
            if indent ==0:
                indentIncreasing=True
    except KeyboardInterrupt:
        sys.exit()
