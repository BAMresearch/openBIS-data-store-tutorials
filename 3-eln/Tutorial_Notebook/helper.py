

#this is for code generation for experiments
def auto_generated_code(prj = None):#it is imperative that you choose the right project for your experiment, otherwise the code will not be generated correctly
    if prj is None:
        raise ValueError("Project cannot be None")
    experiments_df = prj.get_experiments().df
    n = len(list(experiments_df['identifier']))#get current count of experiments in the project
    code = prj.code + "_EXP_" +str(n+1)
    return code



templates = {#this is just copy pasted data from the overview of synthesis from after choosing gui based material synthesis template.
            'Material Synthesis': 
                {'$name': 'Material Synthesis',#can also ask the usre to input this data and all other fields if needed..
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


def display_tree(space):#displays space>projects>collections>samples
    for project in space.get_projects():
        print(f'\t{project.code}')
        for experiment in project.get_experiments():
            print(f'\t\t{experiment.code}')
            for sample in experiment.get_samples():
                print(f'\t\t\t{sample.code}')
                for dataset in sample.get_datasets():
                    print(f'\t\t\t\t{dataset.code}')