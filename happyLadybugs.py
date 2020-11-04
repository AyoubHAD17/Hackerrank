def happyLadybugs(string):
    string = list(string)
    count = 0
    if len(string) == 1:
        if string[0] == '_':
            return "YES"
        else:
            return "NO"
    if string[1] == '_':
        for l in range(2, len(string)):
            if string[l] == string[0]:
                string[1] = string[l]
                string[l] = '_'
                break
    for i in range(1, len(string)-1):
        if string[i] == '_':
            count+=1
            continue
        elif string[i-1] == string[i]:
            continue
        elif string[i+1] == string[i]:
            continue
        elif string[i-1] == '_':
            count+=1
            if string[0] == string[i]:
                if string[1] == string[0]:
                    for j in range(1, len(string)):
                        if string[j] == string[i]:
                            try:
                                if string[j-1] == string[j]:
                                    continue
                                elif string[j+1] == string[j]:
                                    continue
                                else:
                                    string[i+1] = string[j]
                                    string[j] = '_'
                                    break
                            except IndexError:
                                string[i+1] = string[j]
                                string[j] = '_'
                else:
                    pass
            else:
                for j in range(1, len(string)):
                    if string[j] == string[i]:
                        try:
                            if string[j-1] == string[j] or string[j-1] == '_':
                                continue
                            elif string[j+1] == string[j]:
                                continue
                            else:
                                string[i-1] = string[j]
                                string[j] = '_'
                                break
                        except IndexError:
                            string[i-1] = string[j]
                            string[j] = '_'           
        elif string[i+1] == '_':
            count+=1
            if string[0] == string[i]:
                if string[1] == string[0]:
                    for j in range(1, len(string)):
                        if string[j] == string[i]:
                            try:
                                if string[j-1] == string[j]:
                                    continue
                                elif string[j+1] == string[j]:
                                    continue
                                else:
                                    string[i+1] = string[j]
                                    string[j] = '_'
                                    break
                            except IndexError:
                                string[i+1] = string[j]
                                string[j] = '_'
                else:
                    pass
            else:
                for j in range(1, len(string)):
                    if string[j] == string[i]:
                        try:
                            if string[j-1] == string[j]:
                                continue
                            elif string[j+1] == string[j] or string[j+1] == '_':
                                continue
                            else:
                                string[i+1] = string[j]
                                string[j] = '_'
                                break
                        except IndexError:
                            string[i+1] = string[j]
                            string[j] = '_'    
        else:
            continue
    if string[-2] != string[-1]:
        for k in range(len(string)-1):
            if string[k] == string[-1]:
                if string[k+1] == '_':
                    string[k+1] = string[-1]
                    string[-1] = '_'
                    break 
    print("".join(string))
    print(count)




if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        n = int(input())
        happyLadybugs(input())