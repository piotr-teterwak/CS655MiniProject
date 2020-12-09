bash ~/CS655MiniProject/Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
eval "$(/users/$USER/miniconda/bin/conda shell.bash hook)"
conda init
conda install --file requirements.txt -y
source ~/.bashrc
