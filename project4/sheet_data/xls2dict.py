#-*- coding:utf-8 -*-
import xlrd
import sys , os
import pickle
# 이 파일에서는 엑셀을 dictionary 로 만드는 작업을 합니다

def show_dict_info(dict_):
    for key in dict_:
        sample=dict_[key]
        break;

    print 'Show dictionary Info'
    print '# ele : {}'.format(len(dict_))
    print 'smaple : {}'.format(sample)

if not os.path.exists('./sheet_dict.pkl'):
    cac_sheet_dict = {}
    wb = xlrd.open_workbook('./20869_180512_complete.xlsx')
    ws = wb.sheet_by_index(0)

    accNos_calcium = []  # accession Number
    patientCodes_calcium = []  # patient code
    dates_calcuium = []  # examination date
    calcs = []  # cacium score

    # patientCodes - [(accNos0 ,dates0 ,calcium scores0) ,(accNos1, dates1, calcium scores1) .. ] 형태로 저장 합니다
    for i in range(1,ws.nrows):
        sys.stdout.write('\r -Progess {} / {}'.format(i, ws.nrows))
        sys.stdout.flush()

        accNo_cac=ws.row_values(i)[1] # Accession Code
        patCode_cac=ws.row_values(i)[2] # patient Code
        date_cac = ws.row_values(i)[5] # examination date
        score_cac = ws.row_values(i)[7] # Calcium Score
        try:

            accNo_cac , patCode_cac =map(int , [accNo_cac , patCode_cac])
            score_cac=float(score_cac)
        except:
            print '\t',i, 'access num : {}'.format(accNo_cac) , 'patient code {}'.format(patCode_cac) ,\
                'calcium score {}'.format(score_cac)
            continue;

        if not patCode_cac in cac_sheet_dict.keys():
            cac_sheet_dict[patCode_cac]=[[accNo_cac , date_cac , score_cac]]

        else:
            cac_sheet_dict[patCode_cac].append([accNo_cac , date_cac , score_cac])

    f=open('sheet_dict.pkl','wb')
    pickle.dump(file=f , obj=cac_sheet_dict)
    f.close()

else:
    f=open('sheet_dict.pkl','rb')
    cac_sheet_dict=pickle.load(f)
    f.close()

show_dict_info(cac_sheet_dict)