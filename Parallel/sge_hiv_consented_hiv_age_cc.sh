#! /bin/csh
#$ -S /bin/csh
#$ -o .
#$ -e .
#$ -cwd
#$ -t 1-100
#$ -tc 100
hostname
date
./run_model.py /cellar/users/agross/Data/tmp/for_parallel.h5 /cellar/users/agross/Data/tmp hiv_consented/chunk_$SGE_TASK_ID hiv_age_cc age CD4T CD8T NK Bcell Mono
date