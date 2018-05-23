#-*- coding:utf-8 -*_
import pickle, os
import xlwt

def match_fundus2cac(limit , fundus_info_dict , cac_sheet_dict): # fundus 이미지와 cac 을 matching 시킵니다.
    count =0

    for pat_code in fundus_info_dict:
        try:
            fundus_exams= fundus_info_dict[pat_code]
            for fundus_exam in fundus_exams:
                fundus_date, target_dir = fundus_exam
                fundus_yy = int(fundus_date[:4])
                cac_sheet_exams = cac_sheet_dict[int(pat_code)]
                for cac_sheet_exam  in cac_sheet_exams:
                    _ , cac_date , cac_score = cac_sheet_exam
                    cac_yy=int(cac_date.split('-')[0])

                    if abs(cac_yy - fundus_yy) < limit :
                        count += 1
        except KeyError as ke:
            print 'Error patcode {} '.format(pat_code)
    print '# data {}'.format(count)
def show_dict_info(dict_):
    for key in dict_:
        sample = dict_[key]
        break;

    print 'Show dictionary Info'
    print '# ele : {}'.format(len(dict_))
    print 'smaple : {}'.format(sample)

f = open(os.path.join('new_seoul_fundus_pickles', 'patientCodes_dates_12000_13000.pkl'))
fundus_info_dict = pickle.load(f)
f.close()

f = open(os.path.join('sheet_data', 'sheet_dict.pkl'))
cac_sheet_dict = pickle.load(f)
f.close()

print '##### fundus info dict ######'
show_dict_info(fundus_info_dict);
print '##### cac_sheet_dict ######'
show_dict_info(cac_sheet_dict)
#print cac_sheet_dict[int('8209558')]
match_fundus2cac(10 , fundus_info_dict , cac_sheet_dict)



