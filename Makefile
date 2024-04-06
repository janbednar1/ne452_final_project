all: sim

sim:
	cd waterBox; python waterBox.py
	cd histos; python genPairDistancesWater.py
	mkdir img
	cd gr_compute; python oo_gr_compute.py
	cd gr_compute; python oh_gr_compute.py

clean:
	cd waterBox; rm *.pdb
	cd histos; rm *_histo
	rm -rf ./img
