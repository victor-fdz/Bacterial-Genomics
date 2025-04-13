# Uses the COG terms for all the annotated genome of S. maltophilia K279a as a reference to search your DEGs. The output file will be ready to be plotted. 

# DISCLAIMER: some genes were not annotated (were not presented in the COG file) so there may be more relatd pathways that are not being considered. 

# - # - # - # - # - # - # - # - #

# Define the file's paths.
file_COGs = "Stenotrophomonas_maltophilia_K279a_ASM7248v1_genomic.g2d.COG" # Tab-separated
file_DEGs = "Locus_tag_filtered_results.txt" # Only 1 column with the DEGs' tags

# Open it, extract its lines and save them as a list where each element is a list with the row's fields. 
with open(file_COGs) as f: 
    lines_COG = f.readlines()
cogs = [line[:-1].split("\t") for line in lines_COG] # The last character of each line is a line break

# Open the file with the list of locus of your differentially expressed genes and save the tags. 
with open(file_DEGs) as f: 
    lines_DEG = f.readlines()
tags = [line[:-1] for line in lines_DEG[1:]] # The first line is the name of the column and the last character of each line is a linebreak

# Filter in only those annotated (COG terms) genes that are differentially expressed in the sample. 
def_genes = [] # Empty list to store the rows
for cog in cogs: # Iterative process for each row of the COG list
    if cog[0] in tags: # cog[0] is the locus tag
        def_genes.append(cog)

# Convert the results into a dataframe.
col_names = ["Old_Locus_Tag", "COG_ID", "COG_cathegory"] # Column names
df = pd.DataFrame(def_genes,
                  columns = col_names, 
                  index = range(1, len(def_genes) + 1)) # 1-indexed table

# Export as a csv.
df.to_csv('DEGs_with_COGs.csv',
         index = False) # So the numbers of the rows are not presented as a column. 

# In case you are using a visualization interface such as Jupyter Notebook, show the final dataframe. 
df
