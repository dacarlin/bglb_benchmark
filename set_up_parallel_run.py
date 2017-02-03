import shutil 

fmt = dict( zip( 'ANDRCQEGHILKMPFSTWYV', 
  [ 'ALA','ASN','ASP','ARG','CYS','GLN','GLU','GLY','HIS','ILE',
    'LEU','LYS','MET','PRO','PHE','SER','THR','TRP','TYR','VAL' ] ) )

with open( 'mutant_list.txt' ) as fn:
  mutant_list = fn.read().split()

for i, mutant in enumerate( mutant_list ):
  fmt_str = '-parser:script_vars t={} n={}\n-suffix=_{}\n' 
  mutant_path = 'output_files/{}'.format( i+1 )
  shutil.copytree( 'input_pkg', mutant_path )
  with open( mutant_path + '/mutant_flags', 'w' ) as fn:
    fn.write( fmt_str.format( mutant[1:-1], fmt[mutant[-1]], mutant ) )

