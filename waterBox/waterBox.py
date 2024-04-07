import openmm as mm
from openmm import app
from openmm import unit
from openmmtools import testsystems
from sys import stdout

# Initializing parameters
# We are doing a LOT of steps and a fairly big box
# Simulation will take a LONG time
# Reduce if needed
temperature = 0
steps = 10000
skipSteps = 10
equilSteps = 100
Box_edge=3.0*unit.nanometers
step_size = 10

# Built-in water box system with periodic boundary conditions
test_sys = testsystems.WaterBox(box_edge=Box_edge, cutoff=Box_edge/2)
(system, positions) = test_sys.system, test_sys.positions

for i in range(101):

    # We want to iterate through a large range of temperatures to get our data
    temperature = i * step_size
    print('Temperature = {}K'.format(temperature))

    integrator = mm.LangevinIntegrator(temperature*unit.kelvin, 1.0/unit.picoseconds,1.0*unit.femtoseconds)
    platform = mm.Platform.getPlatformByName('Reference')
    platform = mm.Platform.getPlatformByName('CPU')
    simulation = app.Simulation(test_sys.topology, system, integrator, platform)
    simulation.context.setPositions(test_sys.positions)

    # Minimizing energy
    simulation.minimizeEnergy()

    # Initializing velocities
    simulation.context.setVelocitiesToTemperature(temperature*unit.kelvin)

    # Equilibrating
    simulation.step(equilSteps*skipSteps)

    # Appending results to report
    simulation.reporters.append(app.StateDataReporter(stdout, skipSteps, step=True,
        potentialEnergy=True, temperature=True, progress=True, remainingTime=True,
        speed=True, totalSteps=steps, separator='\t'))

    simulation.reporters.append(app.PDBReporter('{}k_water_traj.pdb'.format(temperature), skipSteps))

    # Advance simulation by (steps*skipSteps) steps
    simulation.step(steps*skipSteps)
