#!/bin/bash
#
#SBATCH -o logs/slurm-%A_%a.out
#SBATCH -t 1-12:00
#SBATCH --array=1

# for run
cd output_files/${SLURM_ARRAY_TASK_ID}
pwd
/share/work/rosetta/source/bin/rosetta_scripts.default.linuxgccrelease @flags @mutant_flags

