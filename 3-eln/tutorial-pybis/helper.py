import re#needed for the search collection function
#this is for code generation for experiments
def auto_generated_code(prj = None):#it is imperative that you choose the right project for your experiment, otherwise the code will not be generated correctly
    if prj is None:
        raise ValueError("Project cannot be None")
    experiments_df = prj.get_experiments().df
    n = len(list(experiments_df['identifier']))#get current count of experiments in the project
    code = prj.code + "_EXP_" +str(n+1)
    return code

#function that takes in 2 parameters, project and a keyword.
#searches and bring indices + names of relevant collections in the project that match the keyword
def search_collection(project = None, keyword = ""):
    if project == None:
        return "Error: Project cannot be None."
    if len(project.get_collections()) == 0:
        return "Error: There are no collections in the project."
    if keyword == "":
        return "Error: No keyword was provided for search."
    pattern = r'[^a-zA-Z0-9_ -]'
    if keyword != re.sub(pattern, "", keyword):
        return "Error: The keyword includes characters outside the allowed set of a-z, A-Z, _, space, and -."
    #now we are sure there are no errors, so we will now implement the searching
    col_dict = {}#this is a python dictionary that stores indices and names of collections
    
    output = []
    keyword = keyword.lower()
    keyword = keyword.replace(" ","")
    for i,x in enumerate(project.get_collections()):#get all collections with indices
        col_dict[i] = [x.props.all()['$name'], x.props.all()['$name']]
    for i,collection in enumerate(col_dict.values()):
        collection[0] = collection[0].lower()
        collection[0] = collection[0].replace(" ","")
        collection[0] = re.sub(pattern, "", collection[0])
        if keyword == "all":
            output.append([i,collection[1]])
        else:
            if keyword in collection[0]:
                output.append([i,collection[1]])

    if len(output) == 0:
        print("Could not find any collections with keyword:", keyword)
    else:
        print('Indices\t\tCollections')
        for x in output:
            print(str(x[0]) + '\t\t' + str(x[1]))


templates = {#this is just copy pasted data from the overview of synthesis from after choosing gui based material synthesis template.
            'Material Synthesis': 
                {'$name': 'Material Synthesis',#can also ask the user to input this data and all other fields if needed..
                '$show_in_project_overview': True,
                'finished_flag': False,
                'start_date': None,
                'end_date': None,
                'experimental_step.experimental_goals': 'To synthesize and process functional materials with controlled composition, structure, and properties using a reproducible and parameterized workflow suitable for a wide range of material classes (e.g., powders, thin films, composites, nanomaterials).',
                'experimental_step.experimental_description': 'Very long description, can fix it later',
                'experimental_step.experimental_results': None,
                'experimental_step.spreadsheet': None,
                'reference': 'Literature references for synthesis routes Internal protocols / SOPs',
                'publication': None,
                'notes': 'Free text for additional notes, optimization insights, or anomalies',
                '$xmlcomments': None}
            ,
            'Chemical Treatment' : 
                {'$name': 'Chemical Treatment',}
             ,
            'Macrostructure Characterization' : 
                {'$name': 'Macrostructure Characterization',}
             ,
            'Macrostructure Characterization TS' : #can change later to ask user for the TS or no TS version of this.
                {'$name': 'Macrostructure Characterization TS',}
             ,
             'Microstructure Characterization' : 
                {'$name': 'Microstructure Characterization',}
            ,
            'Microstructure data analysis' : 
                {'$name': '	Microstructure data analysis',}
}
