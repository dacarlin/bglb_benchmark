import pandas 
import os 
from glob import glob 

with open( 'mutant_list.txt' ) as fn:
    mutant_list = fn.read().split()

# first, collect all the weighted score files, this should be easy 

dfs = []
for i, mutant in enumerate( mutant_list ):
    scorefile = 'output_files/{}/score_{}.sc'.format( i+1, mutant )
    if os.path.isfile( scorefile ):
        df = pandas.read_csv( scorefile, sep='\s+', skiprows=1 )
        df['description'] = df['description'].str.split('_', expand=True).get(1) 
        df = df.groupby( 'description' ).apply( lambda x: x.mean() )
        dfs.append( df ) 

df = pandas.concat( dfs ) 
df.to_csv( 'small_feature_set.csv' ) 

# next, try to get all the pose energies from the PDBs 

def header_line( pdb_path ):
    if os.path.isfile( pdb_path ):
        for n, line in enumerate( open( pdb_path ) ):
            if "BEGIN_POSE_ENERGIES" in line:
                return n+1 

dfs = [] 
for i, mutant in enumerate( mutant_list ): 
    pdbs = glob( 'output_files/{}/bglb_*pdb'.format( i+1 ) )  #, mutant ) for j in range( 1, 11 ) ] 
    pdb_dfs = []
    for pdb in pdbs:
        df = pandas.read_csv( pdb, header=header_line(pdb), nrows=448, sep='\s+' ) 
        my_vec = []
        for i, row in df.iterrows():
            if i != 0:
                for index, value in row.iteritems():
                    my_vec.append( ( '{}_{}'.format( row.label, index ), value ) ) 
        pdb_dfs.append( my_vec ) 
    df = pandas.DataFrame( pdb_dfs )  
    dfs.append( df ) 
df = pandas.concat( dfs )
df.to_csv( 'big_feature_set.csv' ) 
        
        # great, now we have a pandas DatFrame for each PDB, now what? 
        # row 0 is the weights
        # row 1 is the whole-pose energies 
        # rows 2-446 are the individual residue scores 
        # row 447 is the ligand score 

