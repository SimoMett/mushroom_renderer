sudo pyinstaller mycology_fungi_builder.spec --noconfirm --distpath /opt
sudo unlink /usr/local/bin/mycology_fungi_builder
sudo chmod +x /opt/mycology_fungi_builder/mycology_fungi_builder
sudo ln -s /opt/mycology_fungi_builder/mycology_fungi_builder /usr/local/bin/mycology_fungi_builder