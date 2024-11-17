tmp_inp = input("Insert the tempeture you would like to convert: ")
tmp_sign = tmp_inp[-1:-2:-1].upper()  #  חיתוך הערך (c/f)
tmp_num = float(tmp_inp[0:-1:]) #חיתוך המחרוזת מהמקום הראשון עד האחרון
if tmp_sign =='F' or 'f' :
    con_tmp = (tmp_num * 5 - 160) / 9 #המרה לצלזיוס
    print(str(round(con_tmp, 3)) + 'C') #עיגול המספר
elif tmp_sign == 'C' or 'c':
    con_tmp = (tmp_num * 9 + 32 * 5) /5
    print(str(round(con_tmp, 3)) + 'F') #עיגול המספר
else:
    print('input error')
    