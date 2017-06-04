# -*- coding: utf-8 -*-


from time import time
import pandas as pd  # DataFrame structure and operations
import numpy as np  # arrays and numerical processing
import email


pd.options.mode.chained_assignment = None  # default='warn'

email_filename = "cleansed_emails_Parsed.csv"
FinNeg_filename = "LoughranMcDonald_Negative.csv"
FinLit_filename = "LoughranMcDonald_Litigious.csv"
## Set your Project Directory
#proj_dir = '/app/hadoop/project/data/test/'
proj_dir = 'C:/Training/udacity/ProjectEmail/'
input_dir = 'inputs/'
output_dir = 'outputs/'

neg_finance_words = 'FinNeg2.csv'
litigation_words = 'FinLit.csv'


t1 = time()



emails = pd.read_csv(proj_dir+output_dir+email_filename)
#emails = pd.read_csv(proj_dir+output_dir+email_filename, nrows=2000)
#emails.drop('Message_word_split', axis=1, inplace=True)
    
#headers = [header for header in emails.columns]
FinNeg = pd.read_csv(proj_dir+input_dir+FinNeg_filename, header=None)
FinNeg.columns = ["word","year"]
FinNeg.drop('year', axis=1, inplace=True)
FinNeg["word"] = FinNeg["word"].str.lower()



FinLit = pd.read_csv(proj_dir+input_dir+FinLit_filename, header=None)
FinLit.columns = ["word","year"]
#print(FinLit.columns)
FinLit.drop('year', axis=1, inplace=True)
#print(FinLit.columns)
FinLit["word"] = FinLit["word"].str.lower()

error_frame = pd.DataFrame({'Line_Number':[' error at row :1000000000']})
#print(error_frame)

#DataFrame.to_csv(path_or_buf=None, sep=', ', na_rep='', float_format=None, columns=None

Test_Bad_Words =[]
Result_Bad_Words =''
Result_bad_word_count = 0

Test_Lit_Words =[]
Result_Lit_Words =''
Result_lit_word_count = 0

error_frame.to_csv(proj_dir+output_dir+'error_email_csv_with_bad_words.csv',index=False)

#error_frame_words=[]

for msg_count in range(0,len(emails["file"])):
    try:
        k = emails['Message_Body'][msg_count].split()
        Test_Bad_Words=(FinNeg[FinNeg['word'].isin(k)])
        Test_Lit_Words=(FinLit[FinLit['word'].isin(k)])
        
        if len(Test_Bad_Words) >0 :
            Result_bad_word_count = len(Test_Bad_Words.values)
            Result_Bad_Words = Test_Bad_Words.values.ravel()
            Result_Bad_Words= ','.join(map(str,Result_Bad_Words))
    #        print(Result_bad_word_count,'---BAD---',Result_Bad_Words)
            
        if len(Test_Lit_Words) >0 :
            Result_lit_word_count = len(Test_Lit_Words.values)
            Result_Lit_Words = Test_Lit_Words.values.ravel()
            Result_Lit_Words= ','.join(map(str,Result_Lit_Words))
    #        print(Result_lit_word_count,'---LITI---',Result_Lit_Words)
            
            
    #    print('--------',msg_count,'-----------') 
        emails['Bad_Words'][msg_count] =Result_Bad_Words
        emails['Bad_Words_count'][msg_count] = Result_bad_word_count
        emails['Total_Words_count'][msg_count] = len(k)
        emails['Percentage_Bad_Words_count'][msg_count] = ((emails['Bad_Words_count'][msg_count])/(emails['Total_Words_count'][msg_count]))
        emails['Lit_Words'][msg_count] = Result_Lit_Words
        emails['Lit_Words_count'][msg_count] = Result_lit_word_count
        emails['Percentage_Lit_Words_count'][msg_count] = ((emails['Lit_Words_count'][msg_count])/(emails['Total_Words_count'][msg_count]))
    
    
    
        Test_Bad_Words=[]
        Result_Bad_Words =''
        Result_bad_word_count = 0
        
        Test_Lit_Words =[]
        Result_Lit_Words =''
        Result_lit_word_count = 0
    except:
#        error_frame_words.append("error at row :"+str(msg_count))
        error_frame['Line_Number']="error at row :"+str(msg_count)
        error_frame.to_csv(proj_dir+output_dir+'error_email_csv_with_bad_words.csv',mode='a', header=False,index=False)
#        print("error at row :",msg_count , error_frame_words )
#        error_frame_words=[]
emails.to_csv(proj_dir+output_dir+'email_csv_with_bad_words.csv',index=False)

t2 = time()
print(t1,t2,"Time Taken in mins :",t2-t1)