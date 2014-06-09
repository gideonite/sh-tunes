#!/usr/bin/python

import pandas

# column keys
firstline = "Melody Incipit first line"
secondline = "Melody Incipit second line"
tunename = "Tune Name"
cleaned_1st_incipit = "cleaned-first-incipit"

def remove_Us_and_Ds(incipit):
    '''
    string -> list.
    '''
    if type(incipit) != str:
        print type(incipit)
        raise Error
    U = 0
    D = 0
    ret = []
    for ch in incipit:
        if 'U' == ch.upper():
            U += 1
            continue
        elif 'D' == ch.upper():
            D += 1
            continue
        elif '(' == ch or ')' == ch:
            pass
        elif ch in '0123456789':
            ch = int(ch) + 7*U - 7*D
        else:
            ch = ''
        ret.append(ch)
    return ret

assert remove_Us_and_Ds("12") == [1,2]
assert remove_Us_and_Ds("1u8") == [1,15]
assert remove_Us_and_Ds("1u1") == [1,8]
assert remove_Us_and_Ds("5u123d6543(21)") == [5,8,9,10,6,5,4,3,'(',2,1,')']

def remove_parens(incipit):
    '''
    list -> list.
    Removes everything in parens.
    '''
    iswithin = False
    ret = []
    for x in incipit:
        if '(' == x:
            iswithin = True
        elif ')' == x:
            iswithin = False
        elif not iswithin:
            ret.append(x)
    return ret

assert [1,2,3] == remove_parens([1,2,3,'(',4,5,')'])
assert [1,2,3] == remove_parens(['(',4,5,')',1,2,3])
assert [2] == remove_parens(['(',1,')',2,'(',3,')','(',4,')'])

def clean_incipit(incipit):
    if pandas.isnull(incipit):
        return incipit
    return remove_parens(remove_Us_and_Ds(incipit))

assert [1, 5, 19, 15] == clean_incipit("15(u1)u51(d5d6)")  # Rachel's example from email.

## If '' somehow made it's way into an incipit, remove it.
## TODO figure this out. What happened to these incipits??
#bad_row_nums = []
#for i,incipit in enumerate(cleaned_data[cleaned_1st_incipit]):
#    for note in incipit:
#        if type(note) != int:
#            bad_row_nums.append(i)
#            break
#
#cleaned_data = cleaned_data.drop(cleaned_data.index[bad_row_nums])
#
#bad_row_nums
