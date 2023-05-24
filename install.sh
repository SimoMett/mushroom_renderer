sudo pyinstaller mycology_fungi_builder.spec --noconfirm --distpath /opt
sudo chmod +x /opt/mycology_fungi_builder/run.sh
sudo ln -s /opt/mycology_fungi_builder/run.sh /usr/local/bin/mycology_fungi_builder