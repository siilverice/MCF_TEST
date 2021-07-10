def translate_code(code, i, n, result):
    if n<0:
        if result in context:
            imperfect_list.append(result)
        return
    elif i+n > len(code):
        if code[i:len(code)-1] in data:
            result += data[code[i:len(code)-1]]
            if result in context:
                perfect_list.append(result)
            return
        else:
            if result in context:
                imperfect_list.append(result)
            return
        return translate_code(code, i, len(code)-1, result)
    elif code[i:n] in data:
        result += data[code[i:n]]
        return translate_code(code, i+n, n+6, result)
    else:
        return translate_code(code, i, n-1, result)


f = open("progc.dat", "r")

data = {}
context = []
morse_codes = []

is_finish_create_dic = False
is_finish_create_context = False

# collect data
for line in f:
    if line.strip() == '*':
        if not is_finish_create_dic:
            is_finish_create_dic = True
            continue
        elif not is_finish_create_context:
            is_finish_create_context = True
            continue
        else:
            break

    if not is_finish_create_dic:
        # create dictionary
        result = map(lambda w: w.strip(), line.split(' '))
        data[result[len(result)-1]] = result[0]

    if is_finish_create_dic and not is_finish_create_context:
        # collect context
        context.append(line.strip())

    if is_finish_create_dic and is_finish_create_context:
        # collect morse code
        morse_codes += map(lambda w: w.strip(), line.split(' '))
        morse_codes = filter(lambda w: not w == '', morse_codes)


for morse_code in morse_codes:
    perfect_list = []
    imperfect_list = []
    translate_code(morse_code, 0, 6, '')

    if len(perfect_list)==1:
        # only 1 perfect match
        print(perfect_list[0])
    elif len(perfect_list)>1:
        sorted_perfect_list = sorted(perfect_list, key=len)
        if len(sorted_perfect_list[0])==len(sorted_perfect_list[1]):
            # ambiguous match
            print(sorted_perfect_list[0] + '!')
        else:
            # multiple perfect match
            print(sorted_perfect_list[0])
    elif len(imperfect_list)>0:
        # sort and reverse
        sorted_imperfect_list = sorted(imperfect_list, key=len)[::-1]
    else:
        print('INCORRECT')
