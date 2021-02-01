import re
s=input('Enter the string:')

#Checks the input string if it matches the regex
if re.match(r"['(']{1,2}([A-Z])=(\d|\d\d)\s(\|\||&&)\s([A-Z])=(\d|\d\d)[')']\s(\|\||&&)\s['(']([A-Z])=(\d|\d\d)\s(\|\||&&)\s([A-Z])=(\d|\d\d)[')']{1,2}", s):
    pattern = re.compile(r"['(']{1,2}([A-Z])=(\d|\d\d)\s(\|\||&&)\s([A-Z])=(\d|\d\d)[')']\s(\|\||&&)\s['(']([A-Z])=(\d|\d\d)\s(\|\||&&)\s([A-Z])=(\d|\d\d)[')']{1,2}")
    matches = pattern.finditer(s)
    #this block prints the output in json format
    for match in matches:
        print('{')
        print('    "query":{')
        if(match.group(6)=='||'):
            print('        "or":[')
        else:
            print('        "and":[')
        var1=1
        var2=2
        var3=3
        var4=4
        var5=5
        for i in range(0,2):
            print('        {')
            if(match.group(var3)=='&&'):
                print('            "and":{')
            else:
                print('            "or":{')
            print('             "%s":%s,'%(match.group(var1),match.group(var2)))
            print('             "%s":%s'%(match.group(var4),match.group(var5)))
            print('            }')
            if(i==1):
                print('        }')
            else:
                print('        },')
            var1+=6
            var2+=6
            var3+=6
            var4+=6
            var5+=6
        print('        ]')
        print('    }')
        print('}')

else:
    print('Syntax Invalid')
