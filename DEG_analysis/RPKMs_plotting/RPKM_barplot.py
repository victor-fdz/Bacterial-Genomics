############ Predefinig important objects ############

# Define your file.
file_path = "gene_count_fpkm.txt"

# Define the FPKM ranges to classify the genes. 
rans = ("<1","1-10","10-100","100-1000",">1000")

# Define the names of the samples and their replicas.
samples = {
    "WildType":["mean","replica1","replica2","replica3"],
    "Mutant":["mean","replica1","replica2","replica3"]
}

############ Processing and modifying the file ############

# Open it and extract its lines.
with open (file_path) as f: 
    lines = f.readlines()

# Generate a dataframe by splitting its lines in fields and define the first line as the columns' names. 
vals = [i[:-1].split("\t") for i in lines]
cols_names = vals[0]
fpkm_df = pd.DataFrame(vals[1:], 
                       columns = cols_names,
                       index = np.arange(1,len(lines)) # To 1-based indexing the table.
                        )

# Transform all the columns that contain numbers into floats. If this step is ignored, numbers will remain as stirngs. 
for i in cols_names[1:]:
    fpkm_df[i] = fpkm_df[i].astype(float)

# Let's generate a mean column for each strain. 
for sample in ("Mutant","WildType"):
    mean_col = [] # Empty list to store the mean values. 
    for i in range(1, len(fpkm_df)+1): # The process is done for each gene.
        r1 = fpkm_df[f"{sample}_fpkm_replica1"][i] 
        r2 = fpkm_df[f"{sample}_fpkm_replica2"][i]
        r3 = fpkm_df[f"{sample}_fpkm_replica3"][i]
        mean_col.append((r1+r2+r3)/3) # Mean is appended to the list.
    fpkm_df[f"{sample}_fpkm_mean"] = mean_col # Mean column is finally generated.

# Define a function to inspectionate a column and assign a value to each gene depending on the range in which its RPKM is. 
def fpkm_rans(col):
    ranged_vals = [] # Empty list to store the range value. 
    for i in range(1,len(col)+1): # The process is done for each gene.
        rpkm = col[i] # Define the RPKM value
        # Assign its range. 
        if rpkm < 1:
            ran = rans[0]
        elif 1 <= rpkm < 10:
            ran = rans[1]
        elif 10 <= rpkm < 100:
            ran = rans[2]
        elif 100 <= rpkm < 1000:
            ran = rans[3]
        else: 
            ran = rans[4]
        ranged_vals.append(ran) # The range is appended to the list.
    return ranged_vals # Return the list. 

# Define 3 empty lists to store:
new_cols = [] # List sto store the new columns created to then add them to the dataframe.
counts_range = [] # List to store a dictionary with the range counts for each column processed. This list will be used to update the dataframe.
data = [] # List to store lists of counts for each column. This list will be used in the plottig. 

# For each sample and for each replica, generate its ranged column. 
for sample in samples:
    for num in samples[sample]:
        # Generate the new column applying the previously created function.
        ranged_vals = fpkm_rans(fpkm_df[f"{sample}_fpkm_{num}"]) 
        fpkm_df[f"{sample}_fpkm_{num}_distrib"] = ranged_vals
        # Add thi:s new column to the list.
        new_col = fpkm_df[f"{sample}_fpkm_{num}_distrib"]
        new_cols.append(new_col)
        # Generate a dictionary to store each range with the number of genes in the column that are in it. 
        counts4range = {}
        # For each range.
        for ran in rans:
            counts = list(new_col).count(ran) # Count the number of genes with this range value. 
            counts4range[ran] = int(counts) # Add the number to the dictionary.  
        # Append the dictionary to the list counts_range.
        counts_range.append(counts4range)
        # Append a list with the values of the dictionary (range counts) to the counts list. 
        data.append(counts4range.values())

# Define the value range values for each oclumn as tupples.
rpkms = {
    'WildType(Mean)': tuple(data[0]),
    'WildType1': tuple(data[1]),
    'WildType2': tuple(data[2]),
    'WildType3': tuple(data[3]),
    'Mutant(Mean)': tuple(data[4]),
    'Mutant1': tuple(data[5]),
    'Mutant2': tuple(data[6]),
    'Mutant3': tuple(data[7])
}

############ Plotting (Barplot) ############

# Define the label positions (x), width of the bars and a mutliplier to space the bars. 
x = np.arange(len(rans))
width = 0.1
multiplier = -2.5

# Start the pot.
fig, ax = plt.subplots()
# For each sample and for each range count.
for sample, count in rpkms.items():
    # If its a wildtype sample:
    if sample.startswith("WildType"):
        cc = "mediumaquamarine"  # Column color (cc) for the replicas.
        if sample[::-1].startswith(")"): # If it's the mean (mean title finishes with a ")"):
                cc = "forestgreen" # Change the column color. 
    # If its a mutant sample, perform the same process but changing the colors. 
    else:
        cc = "slateblue"
        if sample[::-1].startswith(")"):
                cc = "navy"
    # Define a bar for the column.
    rects = ax.bar(x + (width * multiplier), # To space the columns.
                   count, # Data (range count values). 
                   width, 
                   label = sample, # Tha name that will appear in the legend is the sample name. 
                   color = cc, 
                   edgecolor = "white") # Color of the edges of the columns.
                  
    multiplier += 1 

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_xlabel('FPKM ranges')
ax.set_title('FPKM distribution by range')
ax.set_xticks(x + width, rans)
ax.legend(loc ='upper left', 
          fontsize = 10)
# Background lines:
ax.grid(color = "black", 
        linewidth = 0.5,
        axis = "y",
        alpha = 0.5) 

# Show the plot.
plt.show()
