# NE452 Final Project

## Introduction
This project conduts a molecular dynamics simulation of a box of water in order to calculate the g(r) functions for OO and OH bonds. The simulation iterates through a large range of temperatures and generates g(r) plots as .png files in the `img/` directory

### Prerequisites
- Python 3.11.5 (other versions not tested)
- GNU Make
- OpenMM
- MDTraj

## Before you begin
The default parameters for this simulation make it very computationally expensive due to a large range of temperatures and a fairly large number of particles being simulated. As such, it will take a LONG time to run on most machines (INSERT TIME ESTIMATE HERE).

If you wish to avoid this, consider the following changes:
- Reduce <number> in `range(<number>)` and increase `step_size` located in `waterBox/waterBox.py`, `histos/genPairDistancesWater.py`, `gr_compute/oo_gr_compute.py`, and `gr_compute/oh_gr_compute.py`
  - Make sure to adjust `temperature` in `waterBox/waterBox.py` to control your temperature range
- Reduce `Box_edge` in `waterBox/waterBox.py` to reduce the size of the box being simulated, which reduces the total number of molecules 
- Reduce `steps` in `waterBox/waterBox.py` to reduce the number of simulation steps

## Running the simulation
To run the simulation, execute `make` in the top level directory. This command will automatically go into each subdirectory and execute the necessary scripts.
```bash
make
```

To clean up the outputs of the simulation, execute `make clean`.
```bash
make clean
```

## Aknowledgements
The code for this project was based off code made for the class NE452 at the University of Waterloo.