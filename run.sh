# activate the virtual environment
source ./env/bin/activate

# run emotion classification script
python src/emoclf.py

# run visualization script
python src/vis.py

# turn the virtual environment "off"
deactivate