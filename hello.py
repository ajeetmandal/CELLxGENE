import os
os.system("echo Hello from the other side!")
os.system("pip install cellxgene")
os.system("pip install cellxgene[prepare]")
os.system("pip install scanpy>=1.3.7 python-igraph louvain>=0.6")
os.system("pip install cellxgene --upgrade")
os.system("cellxgene launch https://github.com/chanzuckerberg/cellxgene/raw/main/example-dataset/pbmc3k.h5ad")
