class PatientInfos:

    #Analyze min, max and average age for focus
    def analyze_age(focus,ages):
        total_age = 0
        min_age=float("inf")
        max_age=0
        for age in ages:
            total_age+=int(age)
            min_age=min(min_age,int(age))
            max_age=max(max_age,int(age))
        return "{}=> average age: {}, youngest: {}, oldest:{}".format(focus,int(total_age/len(ages)),min_age,max_age)

    #Analyze percentage of males and females for focus
    def analyze_sex(focus,sexes):
        male_count=0
        female_count=0
        for sex in sexes:
            if sex=="male":
                male_count+=1
            else:
                female_count+=1
        male_percentage =round((male_count*100)/len(sexes),2)
        female_percentage =round((female_count*100)/len(sexes),2)
        return "{} => male: {}({}%), female: {}({}%)".format(focus,male_count,male_percentage,female_count,female_percentage)            
    
    #Analyze overweight and and obesity stats for given focus
    def analyze_bmi(focus,bmis):
        obese_count =0
        overweight_count =0
        for bmi in bmis:
            if float(bmi) > 30.0:
                obese_count+=1
            elif float(bmi)>=25.0 and float(bmi) < 30.0:
                overweight_count+=1 
        over_p = round((overweight_count*100)/len(bmis),2)  
        obese_p =round((obese_count*100)/len(bmis),2)        
        return "{}=> overweight:{}({}%), obese:{}({}%)".format(focus,overweight_count,over_p,obese_count,obese_p)

    #Analyze average insurance charge for given focus
    def analyze_charges(focus,charges):
        total_charges = 0
        for charge in charges:
            total_charges+=float(charge)
        average_charge = round(total_charges/len(charges),2)    
        return '{}=> average charge: ${}'.format(focus,average_charge)

    #Analyze average non-smoker and smoker percentages for given focus
    def analyze_smoker(focus,smokers):
        smoker_count=0
        non_smoker_count = 0
        for smoker in smokers:
            if smoker=='yes':
                smoker_count+=1
            else:
                non_smoker_count+=1   
        smoker_count_p = round((smoker_count*100)/len(smokers),2)   
        non_smoker_count_p = round((non_smoker_count*100)/len(smokers),2)      
        return '{} => smokers:{}({}%), non-smokers:{}({}%)'.format(focus,smoker_count, smoker_count_p,non_smoker_count, non_smoker_count_p)             