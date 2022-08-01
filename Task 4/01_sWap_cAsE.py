def swap_case(s):
    final_str = ''
    for ch in s:
        if ch.isupper() == True:
            final_str = final_str + ch.lower()
        elif ch.islower() == True:
            final_str = final_str + ch.upper()
        else:
            final_str = final_str + ch
    return final_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)