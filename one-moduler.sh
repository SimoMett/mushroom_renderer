# put every source code in one python script
echo "" > mycology_fungi_tool.py
cat src/*.py >> mycology_fungi_tool.py
cat mycology_fungi_builder.py >> mycology_fungi_tool.py