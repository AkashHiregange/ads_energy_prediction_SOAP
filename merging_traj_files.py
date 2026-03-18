from ase.io.aims import read_aims_output
from ase.io import read
import os
from ase.io.trajectory import Trajectory

all_images = []

# Iterate over all files in the source directory
for filename in os.listdir():
    if filename.endswith('.traj'):
        try:
            print(filename)
            # traj_path = os.path.join(source_dir, filename)
            # Read the trajectory file
            traj = Trajectory(filename)
            #atoms = read(f'{filename}@-1')
            #traj = Trajectory('final_images.traj', 'a', atoms)
            #traj.write(atoms)
            # Append images from the trajectory to the all_images list
            all_images.extend(traj)
            #print(len(all_images))
        except Exception as e:
            print(e)

# Write all images to the output trajectory file
with Trajectory('all_images.traj', 'a') as traj_out:
    for image in all_images:
        traj_out.write(image)

print(f'Concatenated {len(all_images)} images into all_images.traj')

#for file in os.listdir():
#    if file.endswith('.out'):
#        atoms = read(f'{file}')
#        traj = Trajectory('all_images.traj', 'a', atoms)
#        traj.write(atoms)
        
#print(f'Concatenated all aims.out into all_images.traj')
