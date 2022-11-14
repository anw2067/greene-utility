# Greene Utility


### Step 1. Setup singularity
Follow the instructions [here](https://sites.google.com/nyu.edu/nyu-hpc/hpc-systems/greene/software/singularity-with-miniconda?authuser=0).<br>
**NOTE**: there is an error when creating `/ext3/env.sh`. 
The provided snippet has the line <br>
```export PYTHONPATH=/ext3/miniconda3/bin:$PATH```<br>
However, it should instead be <br>
```export PYTHONPATH=/ext3/miniconda3/bin:$PYTHONPATH```

### Setup 2. Setup the configs here.
1. Set `base_output_dir` in `configs/conf.yaml` as desired.
2. Setup the variables in `src/.python-greene`.

