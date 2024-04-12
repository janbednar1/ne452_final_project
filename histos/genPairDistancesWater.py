import numpy as np
import mdtraj as md

# Initializing independent parameters
nbins=300
rmin=0.1
step_size = 10

for i in range(101):

    k = i * step_size
    print('Generating pair distances for T = {}K'.format(k))
    
    # Load data
    input_data = md.load('../waterBox/{}k_water_traj.pdb'.format(k))

    # Initialize dependent parameters
    rmax=input_data.unitcell_lengths[0,0]/2.
    dr=(rmax-rmin)/float(nbins)
    volume=input_data.unitcell_lengths[0,0]*input_data.unitcell_lengths[0,1]*input_data.unitcell_lengths[0,2]

    # Compute distances
    N = int(input_data.n_atoms/3)
    Nsteps = input_data.n_frames
    
    OO_pairs = []
    OH_pairs = []
    
    for i in range(N):
        for j in range(i+1,N):
            OO_pairs.append([i*3,j*3])
            OH_pairs.append([i*3,j*3+1])
            OH_pairs.append([i*3,j*3+2])
            OH_pairs.append([j*3,i*3+1])
            OH_pairs.append([j*3,i*3+2])

    OO_distances = md.compute_distances(input_data,OO_pairs)
    OH_distances = md.compute_distances(input_data,OH_pairs)

    # Initialize histograms
    OO_histo=np.zeros(nbins,float)
    OH_histo=np.zeros(nbins,float)
    
    # Populate histograms
    for OO in OO_distances:
            for d in OO:
                    index_OO=int(np.floor((d-rmin)/dr))
                    if index_OO < nbins:
                            OO_histo[index_OO]+=1.
                            
    for OH in OH_distances:
            for d in OH:
                    index_OH=int(np.floor((d-rmin)/dr))
                    if index_OH < nbins:
                            OH_histo[index_OH]+=1.

    # Normalize histograms and divide by jacobian
    for i in range(nbins):
            r=rmin+i*dr
            OO_histo[i]=OO_histo[i]/(2.*np.pi*r*r*dr*N*N/volume)/float(Nsteps)
            OH_histo[i]=OH_histo[i]//(2.*np.pi*r*r*dr*N*N*4./volume)/float(Nsteps)

    # Write output files to be plotted
    OO_file=open('{}k_OO_histo'.format(k),'w')
    for i in range(nbins):
            OO_file.write(str(rmin+i*dr)+' '+str(OO_histo[i])+'\n')
    OO_file.close()

    OH_file=open('{}k_OH_histo'.format(k),'w')
    for i in range(nbins):
            OH_file.write(str(rmin+i*dr)+' '+str(OH_histo[i])+'\n')

    # Close file and wipe any potentially stored data
    OH_file.close()
    input_data = []
    OO_pairs = []
    OH_pairs = []
    OO_distances = []
    OH_distances = []
    OO_histo= []
    OH_histo= []
