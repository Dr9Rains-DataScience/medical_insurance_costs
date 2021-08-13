import csv
from patientinfo import PatientInfos as pi

def get_data(filename,column,constraint_column,constraint_value):
    data =[]
    with open(filename,newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row[constraint_column].isalpha() and row[constraint_column]==constraint_value:
                data.append(row[column])
            elif not row[constraint_column].isalpha() and float(row[constraint_column]) >= constraint_value:
                
                data.append(row[column])

    return data    

filename = 'insurance.csv'

smoker_ages =get_data(filename,'age','smoker','yes') 
smoker_sex = get_data(filename,'sex','smoker','yes')
smoker_bmi = get_data(filename,'bmi','smoker','yes')  
smoker_charges = get_data(filename,'charges','smoker','yes')

obese_ages = get_data(filename,'age','bmi',30.0)
obese_sex = get_data(filename,'sex','bmi',30.0)
obese_smoker = get_data(filename,'smoker','bmi',30.0)
obese_charges = get_data(filename,'charges','bmi',30.0)

print(pi.analyze_age("smoker",smoker_ages))       
print(pi.analyze_sex("smoker",smoker_sex))   
print(pi.analyze_bmi("smoker",smoker_bmi))   
print(pi.analyze_charges("smoker",smoker_charges))

print(pi.analyze_age('obese',obese_ages))
print(pi.analyze_sex('obese',obese_sex))
print(pi.analyze_smoker('obese',obese_smoker))
print(pi.analyze_charges('obese',obese_charges))
  

