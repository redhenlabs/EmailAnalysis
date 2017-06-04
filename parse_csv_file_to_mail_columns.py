# -*- coding: utf-8 -*-


from time import time
import pandas as pd  # DataFrame structure and operations
import numpy as np  # arrays and numerical processing
import email

def add_columns():
    pd.options.mode.chained_assignment = None  # default='warn'
    
    email_filename = "emails_clean.csv"
    
    ## Set your Project Directory
    #proj_dir = '/app/hadoop/project/data/test/'
    proj_dir = 'C:/Training/udacity/ProjectEmail/'
    input_dir = 'inputs/'
    output_dir = 'outputs/'
    
    
    t1 = time()
    
    emails = pd.read_csv(proj_dir+input_dir+email_filename)
#    emails = pd.read_csv(proj_dir+input_dir+email_filename,nrows=500)
                      
    poi_email_address = pd.read_csv(proj_dir+input_dir+'poi_email_list.csv', header=None)
    poi_email_address.columns = ["poi_email"]
    
    
    
    
    # Parse the emails into a list email objects
    msg_body = get_messages(emails)
    
    
    emails["Message_Body"] = msg_body
    
    messages = list(map(email.message_from_string, emails['message']))
    emails.drop('message', axis=1, inplace=True)
    
    
    # Get fields from parsed email objects
    keys = messages[0].keys()
    for key in keys:
        emails[key] = [doc[key] for doc in messages]
    
    
    emails["Message_Body"] = msg_body
    
    """ Remove Extra Columns that are not required  """
    
    emails.drop('Mime-Version', axis=1, inplace=True)

    emails.drop('Content-Type', axis=1, inplace=True)
    emails.drop('Content-Transfer-Encoding', axis=1, inplace=True)
    emails.drop('X-FileName', axis=1, inplace=True)
    
    
    # Extract the root of file as Inbox Owner
    emails['Inbox_Owner'] = emails['file'].map(lambda x:x.split('/')[0])
    
    # Identify the POI - if matchining email from POI Email Address exists
    emails['POI'] = emails['From'].isin(poi_email_address['poi_email'])

    del messages
    emails.head()
    
    
    
    emails['Date'] = pd.to_datetime(emails['Date'], infer_datetime_format=True)
    emails.dtypes
    
#    emails["Message_word_split"] = emails["Message_Body"].str.split()
    
    """
    Add additional required fields for future use
    """
    emails["Bad_Words"] =np.nan
    emails["Bad_Words_count"] = np.nan
    emails["Total_Words_count"]= np.nan
    emails["Percentage_Bad_Words_count"]= np.nan
    emails["Lit_Words"] =np.nan
    emails["Lit_Words_count"] = np.nan
    emails["Percentage_Lit_Words_count"]= np.nan
    emails.to_csv(proj_dir+output_dir+'cleansed_emails_Parsed.csv',index=False)
    
    t2 = time()
    print(t1,t2,"Time Taken in mins :",t2-t1)

def get_messages(df):
    messages = []
    for item in df["message"]:
        # Return a message object structure from a string
        e = email.message_from_string(item)    
        # get message body  
        message_body = e.get_payload()
        message_body = message_body.lower()
        messages.append(message_body)
                       
    return messages
 
if __name__ == "__main__":
    add_columns()     