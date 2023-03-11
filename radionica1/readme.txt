#Otvoriti Anaconda Prompt i unesi sljedece naredbe:
conda create -n <env_name> python=3.9.16
conda activate <env_name>
pip3 install librosa
pip3 install matplotlib
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=<env_name>

#Pozicionirati se u folder sound_processing 
jupyter notebook

#otvoriti sound_analysis_kk skriptu
# u alatnoj traci odabrati
   Kernel -> Change kernel -> <env_name>