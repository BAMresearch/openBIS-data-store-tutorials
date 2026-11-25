import re#needed for the search collection function
#this is for code generation for experiments
def auto_generated_code(prj = None):#it is imperative that you choose the right project for your experiment, otherwise the code will not be generated correctly
    if prj is None:
        raise ValueError("Project cannot be None")
    experiments_df = prj.get_experiments().df
    n = len(list(experiments_df['identifier']))#get current count of experiments in the project
    code = prj.code + "_EXP_" +str(n+1)
    return code


def search_projects(space = None, keyword = ""):
    if space == None:
        return "Error: Space cannot be None."
    if len(space.get_projects()) == 0:
        return "Error: There are no projects in the space."
    if keyword == "":
        return "Error: No keyword was provided for search."
    pattern = r'[^a-zA-Z0-9_ -]'
    if keyword != re.sub(pattern, "", keyword):
        return "Error: The keyword includes characters outside the allowed set of a-z, A-Z, _, space, and -."
    #now we are sure there are no errors, so we will now implement the searching
    proj_dict = {}#this is a python dictionary that stores indices and names of projects
    
    output = []
    keyword = keyword.lower()
    keyword = keyword.replace(" ","")
    keyword = keyword.replace("_","")
    for i,x in enumerate(space.get_projects()):#get all projects with indices
        proj_dict[i] = [x.attrs.all()['code'], x.attrs.all()['code']]
    for i,project in enumerate(proj_dict.values()):
        project[0] = project[0].lower()
        project[0] = project[0].replace(" ","")
        project[0] = project[0].replace("_","")
        project[0] = re.sub(pattern, "", project[0])
        if keyword == "all":
            output.append([i,project[1]])
        else:
            if keyword in project[0]:
                output.append([i,project[1]])

    if len(output) == 0:
        print("Could not find any projects with keyword:", keyword)
    else:
        print('Indices\t\tProjects')
        for x in output:
            print(str(x[0]) + '\t\t' + str(x[1]))

#function that takes in 2 parameters, project and a keyword.
#searches and bring indices + names of relevant collections in the project that match the keyword
def search_collections(project = None, keyword = ""):
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

def search_samples(collection = None, keyword = ""):
    if collection == None:
        return "Error: Collection cannot be None."
    if len(collection.get_samples()) == 0:
        return "Error: There are no samples in the collection."
    if keyword == "":
        return "Error: No keyword was provided for search."
    pattern = r'[^a-zA-Z0-9_ -]'
    if keyword != re.sub(pattern, "", keyword):
        return "Error: The keyword includes characters outside the allowed set of a-z, A-Z, _, space, and -."
    #now we are sure there are no errors, so we will now implement the searching
    sample_dict = {}#this is a python dictionary that stores indices and names of samples
    
    output = []
    keyword = keyword.lower()
    keyword = keyword.replace(" ","")
    for i,x in enumerate(collection.get_samples()):#get all samples with indices
        sample_dict[i] = [x.props.all()['$name'], x.props.all()['$name']]
    for i,sample in enumerate(sample_dict.values()):
        sample[0] = sample[0].lower()
        sample[0] = sample[0].replace(" ","")
        sample[0] = re.sub(pattern, "", sample[0])
        if keyword == "all":
            output.append([i,sample[1]])
        else:
            if keyword in sample[0]:
                output.append([i,sample[1]])

    if len(output) == 0:
        print("Could not find any samples with keyword:", keyword)
    else:
        print('Indices\t\tSamples')
        for x in output:
            print(str(x[0]) + '\t\t' + str(x[1]))


templates = {
            'Material Synthesis': 
                {'$name': 'Material Synthesis',
                '$show_in_project_overview': True,
                'finished_flag': False,
                'start_date': None,
                'end_date': None,
                'experimental_step.experimental_goals': '<p>To synthesize and process functional materials with controlled composition, structure, and properties using a reproducible and parameterized workflow suitable for a wide range of material classes (e.g., powders, thin films, composites, nanomaterials).</p>',
                'experimental_step.experimental_description': '<p>Template for documenting generic material synthesis procedures, including precursor preparation, reaction processing, post-treatment, and intermediate/ final material handling.</p><h4><strong>Safety Precautions</strong></h4><ul><li>Wear appropriate PPE (lab coat, gloves, safety goggles).</li><li>Handle chemicals according to MSDS guidelines.</li><li>Use fume hood for volatile, toxic, or reactive substances.</li><li>Ensure proper handling of high-temperature equipment and pressurized systems.</li><li>Dispose of waste according to institutional and regulatory requirements.</li></ul><h4><strong>Synthesis Workflow</strong></h4><h4><strong>1. Precursor Preparation</strong></h4><ol><li>Define target material composition and stoichiometry.</li><li>Select precursor materials (e.g., salts, powders, polymers, solvents).</li><li>Weigh and record all precursor masses.</li><li>Dissolve or disperse precursors in appropriate solvent(s).</li><li>Adjust concentration and pH if required.</li><li>Apply mixing method:<ul><li>Magnetic stirring / overhead stirring</li><li>Ultrasonication</li><li>Ball milling</li></ul></li></ol><h4><strong>2. Reaction / Synthesis Step</strong></h4><ol><li>Transfer precursor solution or mixture into reaction vessel.</li><li>Set synthesis conditions:<ul><li>Temperature: ___ °C</li><li>Pressure: ___ bar (if applicable)</li><li>Atmosphere: air / inert / reactive gas</li></ul></li><li>Initiate reaction using selected method:<ul><li>Thermal treatment</li><li>Hydrothermal / solvothermal synthesis</li><li>Chemical precipitation</li><li>Vapor deposition / coating</li></ul></li><li>Maintain reaction for defined duration: ___ min/h</li><li>Monitor process (optional):<ul><li>pH</li><li>Temperature profile</li><li>Gas evolution</li><li>Optical/visual changes</li></ul></li></ol><h4><strong>3. Material Recovery</strong></h4><ol><li>Separate product phase:<ul><li>Filtration / centrifugation / decantation</li></ul></li><li>Wash material using appropriate solvent(s).</li><li>Repeat washing cycles until impurities are minimized (record number of cycles).</li><li>Dry material under defined conditions:<ul><li>Air drying / vacuum drying / freeze drying</li><li>Temperature: ___ °C</li><li>Duration: ___ h</li></ul></li></ol><h4><strong>4. Post-Treatment / Processing</strong></h4><ol><li>Apply additional processing if required:<ul><li>Calcination / annealing</li><li>Sintering</li><li>Mechanical processing (grinding, milling, pressing)</li></ul></li><li>Define treatment conditions:<ul><li>Temperature profile</li><li>Heating rate</li><li>Atmosphere</li></ul></li><li>Cool material under controlled conditions.</li></ol><h4><strong>5. Functionalization / Modification (Optional)</strong></h4><ol><li>Introduce dopants, coatings, or surface modifications.</li><li>Repeat reaction and recovery steps if applicable.</li><li>Record concentrations and incorporation method.</li></ol><h4><strong>6. Sample Preparation for Characterization</strong></h4><ol><li>Prepare material for analysis:<ul><li>Pelletizing / coating / dispersion</li></ul></li><li>Assign sample identifiers.</li><li>Store samples under defined conditions.</li></ol><h4><strong>Experimental Parameters (Key Variables)</strong></h4><ul><li>Composition ratios</li><li>Precursor concentration</li><li>Solvent type</li><li>Reaction temperature and time</li><li>pH</li><li>Atmosphere</li><li>Post-treatment temperature and duration</li></ul><p>&nbsp;</p>',
                'experimental_step.experimental_results': '<figure class="table"><table><thead><tr><th>Sample ID</th><th>Composition</th><th>Process Conditions</th><th>Yield [%]</th><th>Notes</th></tr></thead><tbody><tr><td>Sample-1</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>Sample-2</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure>',
                'experimental_step.spreadsheet': None,
                'reference': '<ul><li>Literature references for synthesis routes</li><li>Internal protocols / SOPs</li></ul>',
                'publication': None,
                'notes': '<p>Free text for additional notes, optimization insights, or anomalies.</p>',
                '$xmlcomments': None}
            ,
            'Chemical Treatment' : 
                {'$name': 'Chemical Treatment',
                '$show_in_project_overview': True,
                'finished_flag': False,
                'start_date': None,
                'end_date': None,
                'experimental_step.experimental_goals': '<p>To apply controlled, non-destructive chemical treatments to synthesized materials in order to modify surface chemistry without altering bulk structure (non-destructive treatment).</p>',
                'experimental_step.experimental_description': '<h4><strong>Safety Precautions</strong></h4><ul><li>Wear appropriate PPE (gloves, goggles, lab coat).</li><li>Handle chemicals according to safety data sheets.</li><li>Work in a fume hood when using volatile or reactive substances.</li><li>Ensure compatibility of chemicals with sample material.</li><li>Dispose of chemical waste properly.</li></ul><h4><strong>Treatment Workflow</strong></h4><h4><strong>1. Sample Selection &amp; Pre-Inspection</strong></h4><ol><li>Document samples from synthesis batch.</li><li>Record initial condition:<ul><li>Visual appearance</li></ul></li><li>Verify absence of visible structural damage.</li><li>Assign sample identifier and link to parent synthesis step</li></ol><figure class="table"><table><tbody><tr><td>Sample Name&nbsp;</td><td>Initial condition (Visual appeareance)</td><td>Structure status checked</td><td>Sample openBIS permID</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><h4><strong>2. Treatment Design</strong></h4><ol><li>Define treatment objective:<ul><li>Surface conditioning</li></ul></li><li>Select treatment medium:<ul><li>Solvent(s)</li><li>Aqueous solutions</li><li>Reactive but mild agents</li></ul></li><li>Define parameters:<ul><li>Concentration</li><li>pH</li><li>Temperature</li><li>Exposure time</li></ul></li></ol><figure class="table"><table><tbody><tr><td>Treatment objective</td><td>Treatment medium</td><td>Parameteres</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><h4><strong>3. Chemical Treatment Application</strong></h4><ol><li>Immerse or expose sample to treatment medium:<ul><li>Static immersion</li><li>Flow-through system</li><li>Controlled atmosphere exposure</li></ul></li><li>Maintain defined conditions:<ul><li>Temperature: ___ °C</li><li>Duration: ___ min/h</li><li>Agitation (if applicable)</li></ul></li><li>Monitor process:<ul><li>pH changes</li><li>Color changes in solution</li><li>Gas evolution (if any)</li></ul></li></ol><figure class="table"><table><tbody><tr><td>Treatment type</td><td>Conditions</td><td>Monitored properties</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><h4><strong>Experimental Parameters (Key Variables)</strong></h4><ul><li>Treatment type (cleaning, conditioning, passivation)</li><li>Chemical composition of treatment medium</li><li>Concentration and pH</li><li>Exposure time</li><li>Temperature</li><li>Drying conditions</li></ul><p>&nbsp;</p>',
                'experimental_step.experimental_results': '<p>&nbsp;</p><figure class="table"><table><thead><tr><th>Sample ID</th><th>Treatment Type</th><th>Key Parameters</th><th>Mass Change [%]</th><th>Observations</th></tr></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><h4>Chemical Exposure&nbsp;</h4><figure class="table"><table><thead><tr><th>Chemical</th><th>Concentration</th><th>Exposure Time</th><th>Temperature</th><th>Notes</th></tr></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><h4>Quality &amp; Integrity Check</h4><figure class="table"><table><thead><tr><th>Parameter</th><th>Before Treatment</th><th>After Treatment</th><th>Difference</th><th>Unit</th></tr></thead><tbody><tr><td>Mass</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>g</td></tr><tr><td>Dimension</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>mm</td></tr></tbody></table></figure>',
                'experimental_step.spreadsheet': None,
                'reference': '<ul><li>Standard cleaning or conditioning protocols</li><li>Internal SOPs</li><li>Literature references</li></ul>',
                'publication': None,
                'notes': None,
                '$xmlcomments': None}
             ,
            'Macrostructure Characterization' : 
                {'$name': 'Macrostructure Characterization',
                '$show_in_project_overview': True,
                'finished_flag': False,
                'start_date': None,
                'end_date': None,
                'experimental_step.experimental_goals': '<p>To characterize the macrostructural properties of synthesized materials, including bulk morphology, mechanical integrity, and structural homogeneity, using standardized and reproducible measurement techniques.</p><p>&nbsp;</p>',
                'experimental_step.experimental_description': '<p>&nbsp;</p><h4><strong>Safety Precautions</strong></h4><ul><li>Wear appropriate PPE depending on technique (e.g., safety glasses, gloves).</li><li>Follow instrument-specific safety procedures.</li><li>Ensure proper handling of mechanical testing devices and imaging systems.</li><li>Avoid exposure to dust or particulates when handling samples.</li></ul><h4><strong>Characterization Workflow</strong></h4><h4><strong>1. Sample Preparation</strong></h4><ol><li>Select sample(s) from synthesis batch.</li><li>Prepare sample</li><li>Assign sample identifier and link to parent material.</li></ol><h4><strong>2. Measurement Setup</strong></h4><ol><li>Select characterization technique(s):<ul><li>Optical imaging (e.g., microscopy, visual inspection)</li><li>Surface/topography measurement</li><li>Mechanical testing (e.g., compression, tensile, hardness)</li><li>Density / porosity measurement</li></ul></li><li>Configure instrument parameters:<ul><li>Resolution / magnification</li><li>Load / force range</li><li>Scan area or measurement volume</li></ul></li><li>Calibrate instrument if required.</li></ol><h4><strong>3. Data Acquisition</strong></h4><ol><li>Perform measurements according to defined protocol.</li><li>Record environmental conditions:<ul><li>Temperature</li><li>Humidity</li></ul></li><li>Acquire raw data:<ul><li>Images</li><li>Force-displacement curves</li><li>Dimensional measurements</li></ul></li><li>Repeat measurements for statistical reliability (n ≥ ___).</li></ol><h4><strong>4. Data Storage &amp; Linking</strong></h4><ol><li>Store raw data files.</li><li>Link results to:<ul><li>Parent synthesis step</li><li>Sample identifiers</li></ul></li><li>Ensure traceability and versioning.</li></ol><h4><strong>Experimental Parameters (Key Variables)</strong></h4><ul><li>Measurement technique</li><li>Instrument model and configuration</li><li>Sample geometry and preparation method</li><li>Environmental conditions</li><li>Number of replicates</li><li>Data processing method</li></ul><p>&nbsp;</p>',
                'experimental_step.experimental_results': '<h4><strong>Macrostructure Metrics (Examples)</strong></h4><ul><li>Bulk density</li><li>Porosity (%)</li><li>Surface roughness</li><li>Crack density / defect distribution</li><li>Mechanical strength (e.g., compressive strength)</li><li>Elastic modulus</li></ul><h4>&nbsp;</h4><h4>Experimental Parameters (Key Variables)</h4><figure class="table"><table><thead><tr><th>Sample ID</th><th>Technique</th><th>Key Parameter</th><th>Value</th><th>Unit</th><th>Notes</th></tr></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure>',
                'experimental_step.spreadsheet': None,
                'reference': '<ul><li>Standard methods (e.g., ISO, ASTM)</li><li>Internal SOPs</li><li>Literature references</li></ul>',
                'publication': None,
                'notes': '<p>Free text for interpretation, anomalies, or correlations with synthesis parameters.</p>',
                '$xmlcomments': None}
             ,
             'Microstructure Characterization' : 
                {'$name': 'Microstructure Characterization',
                '$show_in_project_overview': True,
                'finished_flag': False,
                'start_date': None,
                'end_date': None,
                'experimental_step.experimental_goals': '<p>To characterize the microstructural features of materials (µm–sub-µm scale), including morphology, phase distribution, and defect structures, to support understanding of structure–property relationships.</p>',
                'experimental_step.experimental_description': '<h4><strong>Safety Precautions</strong></h4><ul><li>Wear appropriate PPE depending on technique.</li><li>Follow instrument-specific safety procedures.</li><li>Handle samples carefully to avoid contamination or damage.</li><li>Be aware of vacuum systems, electron beams, or laser sources (if applicable).</li></ul><h4><strong>Characterization Workflow</strong></h4><h4><strong>1. Sample Preparation</strong></h4><ol><li>Select sample(s) from prior step (e.g., synthesis or pre-treatment).</li><li>Prepare sample</li><li>Assign sample identifier and link to parent material.</li></ol><h4><strong>2. Measurement Setup</strong></h4><ol><li>Select characterization technique(s):<ul><li>Scanning electron microscopy (SEM)</li><li>Optical microscopy</li><li>Atomic force microscopy (AFM)</li><li>Profilometry</li></ul></li><li>Configure instrument parameters:<ul><li>Magnification / resolution</li><li>Beam or probe settings</li><li>Scan area</li></ul></li><li>Calibrate instrument if required.</li></ol><h4><strong>3. Data Acquisition</strong></h4><ol><li>Load sample and locate region(s) of interest.</li><li>Acquire images at multiple magnifications.</li><li>Capture additional signals (if applicable):<ul><li>Secondary electrons / backscattered electrons</li><li>Topography maps</li></ul></li><li>Record acquisition parameters for each dataset.</li><li>Perform replicate measurements (n ≥ ___).</li></ol><h4><strong>4. Data Processing</strong></h4><ol><li>Process images:<ul><li>Contrast and brightness adjustment</li><li>Noise filtering</li></ul></li><li>Analyze microstructural features:<ul><li>Grain size and distribution</li><li>Phase contrast / phase boundaries</li><li>Surface roughness</li><li>Defects (cracks, voids, inclusions)</li></ul></li><li>Quantify features using image analysis tools.</li></ol><h4><strong>5. Result Validation</strong></h4><ol><li>Compare results across different regions and samples.</li><li>Identify potential artifacts:<ul><li>Charging effects</li><li>Surface contamination</li><li>Preparation-induced damage</li></ul></li><li>Cross-check with complementary techniques if available.</li></ol><h4><strong>6. Data Storage &amp; Linking</strong></h4><ol><li>Store raw and processed images.</li><li>Link datasets to:<ul><li>Parent synthesis or treatment step</li><li>Related macrostructure and TEM data</li></ul></li><li>Ensure metadata completeness and traceability.</li></ol><h4><strong>Experimental Parameters (Key Variables)</strong></h4><ul><li>Characterization technique</li><li>Magnification range</li><li>Sample preparation method</li><li>Instrument configuration</li><li>Scan area / resolution</li><li>Number of replicates</li></ul>',
                'experimental_step.experimental_results': '<h4><strong>Macrostructure Metrics (Examples)</strong></h4><ul><li>Bulk density</li><li>Porosity (%)</li><li>Surface roughness</li><li>Crack density / defect distribution</li><li>Mechanical strength (e.g., compressive strength)</li><li>Elastic modulus</li></ul><h4>&nbsp;</h4><h4>Experimental Parameters (Key Variables)</h4><figure class="table"><table><thead><tr><th>Sample ID</th><th>Technique</th><th>Key Parameter</th><th>Value</th><th>Unit</th><th>Notes</th></tr></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure>',
                'experimental_step.spreadsheet': None,
                'reference': '<ul><li>Standard characterization methods (ISO, ASTM)</li><li>Instrument manuals</li><li>Internal SOPs</li><li>Literature references</li></ul>',
                'publication': None,
                'notes': '<p>Free text for interpretation, anomalies, or correlations with synthesis and treatment parameters.</p>',
                '$xmlcomments': None}
                ,
            'Microstructure data analysis' : 
                {'$name': 'Microstructure data analysis',
                '$show_in_project_overview': True,
                'finished_flag': False,
                'start_date': None,
                'end_date': None,
                'experimental_step.experimental_goals': '<p>To analyze and interpret data obtained from microstructure characterization in order to quantify relevant structural features, identify trends, compare samples, and support structure–property correlations.</p>',
                'experimental_step.experimental_description': '<p>Template for documenting workflows for the analysis of microstructural datasets derived from imaging and related measurements.</p><p>This template supports:</p><ul><li>Quantitative feature extraction</li><li>Statistical analysis of replicate data</li><li>Comparison across samples, treatments, and batches</li><li>Traceable linkage between raw data, processed data, and conclusions<br><br>Notes</li><li>Ensure secure handling of data and metadata.</li><li>Follow institutional policies for software use, data storage, and version control.</li></ul><h4><strong>Analysis Workflow</strong></h4><h4><strong>1. Input Data Selection</strong></h4><ol><li>Select dataset(s) from previous microstructure characterization step.</li><li>Record linked parent data:<ul><li>Raw image files</li><li>Processed image files</li><li>Measurement logs</li></ul></li><li>Verify dataset completeness and metadata integrity.</li><li>Assign analysis identifier and link to source characterization step.</li></ol><h4><strong>2. Data Pre-Processing</strong></h4><ol><li>Import raw or processed data into analysis environment.</li><li>Apply pre-processing as required:<ul><li>Cropping</li><li>Background correction</li><li>Noise reduction</li><li>Contrast normalization</li></ul></li><li>Record all pre-processing parameters.</li><li>Preserve original raw data unchanged.</li></ol><h4><strong>3. Feature Extraction</strong></h4><ol><li>Define target microstructural features for extraction:<ul><li>Grain size</li><li>Feature size distribution</li><li>Phase fraction</li><li>Porosity / void fraction</li><li>Crack density</li><li>Inclusion density</li><li>Interface characteristics</li></ul></li><li>Apply analysis method:<ul><li>Thresholding</li><li>Segmentation</li><li>Edge detection</li><li>Region labeling</li><li>Manual annotation</li></ul></li><li>Extract quantitative values for each region/sample.</li><li>Record software, algorithm, and parameter settings used.</li></ol><h4><strong>4. Statistical Analysis</strong></h4><ol><li>Aggregate measurements across replicates and regions of interest.</li><li>Calculate descriptive statistics:<ul><li>Mean</li><li>Median</li><li>Standard deviation</li><li>Minimum / maximum</li></ul></li><li>Identify outliers and document treatment of outliers.</li><li>Compare groups by sample, synthesis condition, or treatment condition.</li></ol><h4><strong>5. Interpretation and Correlation</strong></h4><ol><li>Interpret extracted microstructural metrics in the context of:<ul><li>Synthesis conditions</li><li>Chemical pre-treatment</li><li>Macrostructure characterization</li></ul></li><li>Identify observed trends and anomalies.</li><li>Document possible relationships between microstructure and expected material properties.</li><li>Record limitations of the analysis.</li></ol><h4><strong>6. Validation</strong></h4><ol><li>Verify reproducibility of extracted results across replicates.</li><li>Cross-check selected results with manual review or alternative method.</li><li>Document analysis uncertainty and possible sources of error:<ul><li>Image quality</li><li>Segmentation sensitivity</li><li>Region selection bias</li></ul></li><li>Confirm traceability to original datasets.</li></ol><h4><strong>7. Data Storage &amp; Linking</strong></h4><ol><li>Store analysis scripts, parameter sets, processed outputs, and summary tables.</li><li>Link analysis results to:<ul><li>Parent microstructure characterization step</li><li>Related macrostructure and TEM characterization steps</li><li>Parent synthesis and treatment steps</li></ul></li><li>Ensure metadata completeness and versioning.</li></ol>',
                'experimental_step.experimental_results': '<p>&nbsp;</p><p>Experimental results</p><figure class="table"><table><thead><tr><th>Sample ID</th><th>Feature</th><th>Mean Value</th><th>Std. Dev.</th><th>Unit</th><th>Notes</th></tr></thead><tbody><tr><td>Sample-1</td><td>Grain size</td><td>&nbsp;</td><td>&nbsp;</td><td>µm</td><td>&nbsp;</td></tr><tr><td>Sample-1</td><td>Porosity</td><td>&nbsp;</td><td>&nbsp;</td><td>%</td><td>&nbsp;</td></tr><tr><td>Sample-2</td><td>Crack density</td><td>&nbsp;</td><td>&nbsp;</td><td>1/mm²</td><td>&nbsp;</td></tr></tbody></table></figure><h4><strong>Analysis Metrics (Examples)</strong></h4><ul><li>Grain size distribution</li><li>Feature aspect ratio</li><li>Phase fraction (%)</li><li>Porosity / void fraction (%)</li><li>Inclusion count per area</li><li>Crack length density</li><li>Surface feature coverage</li><li>Interface density</li></ul><figure class="table"><table><thead><tr><th>Dataset ID</th><th>Processing Step</th><th>Method</th><th>Parameters</th><th>Notes</th></tr></thead><tbody><tr><td>Data-1</td><td>Noise reduction</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>Data-1</td><td>Segmentation</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><h4><strong>Statistical Summary Table</strong></h4><figure class="table"><table><thead><tr><th>Parameter</th><th>n</th><th>Mean</th><th>Median</th><th>Std. Dev.</th><th>Min</th><th>Max</th><th>Unit</th></tr></thead><tbody><tr><td>Grain size</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>µm</td></tr><tr><td>Porosity</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure><p>&nbsp;</p><h4><strong>Interpretation Notes</strong></h4><ul><li>Main trends observed:</li><li>Comparison between samples:</li><li>Correlation with prior synthesis or treatment parameters:</li><li>Uncertainty / confidence level:</li></ul><h4><strong>References</strong></h4><ul><li>Image analysis methods</li><li>Internal SOPs</li><li>Software documentation</li><li>Literature references</li></ul>',
                'experimental_step.spreadsheet': None,
                'reference': '<ul><li>Image analysis methods</li><li>Internal SOPs</li><li>Software documentation</li><li>Literature references</li><li><mark class="marker-yellow">Git repository link?</mark></li></ul>',
                'publication': None,
                'notes': '<p>Free text for interpretation, anomalies, or follow-up recommendations</p>',
                '$xmlcomments': None}
}

