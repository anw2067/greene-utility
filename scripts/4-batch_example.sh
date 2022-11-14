# Run this from the base directory /green-utility

cd src

# sweep / batch experiment example
./.python-greene submitit_hydra.py exp=example_exp name=sweep_example compute/greene=cpu iters=3,6
