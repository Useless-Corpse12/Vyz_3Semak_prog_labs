def ChkSkobki(inputTxt):
    open=0
    for chars in inputTxt:
        if chars==')' :
            if  open<1:
                return False
            else:
                open-=1
        if chars=='(' :
            open+=1
    return (open == 0)

txt=input()
print(ChkSkobki(txt))