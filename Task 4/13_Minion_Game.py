def minion_game(string):
    v = 'AEIOU'
    Stuart_sc, Kevin_sc = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in v:
            Kevin_sc += score
        else:
            Stuart_sc += score
    if Stuart_sc == Kevin_sc:
        print('Draw')
    if Stuart_sc > Kevin_sc:
        print('Stuart {}'.format(Stuart_sc))
    if Stuart_sc < Kevin_sc:
        print('Kevin {}'.format(Kevin_sc))

if __name__ == '__main__':
    s = input()
    minion_game(s)