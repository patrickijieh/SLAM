# SLAM
SLAM

## Feature detection ##
- Detect ORB features in each frame
- Use Lowe's ratio test to find corresponding features between frames
- Use RANSAC to remove false matches

##  Motion estimation ##
- Calculate essential matrix between consecutive frames (camera rotation and translation)
- Refine motion by using bundle adjustment to optimize camera poses

## Landmark management ##
- Create and track landmarks across frames
- Reconstruct 3D landmarks based on observations from multiple camera poses
- Use bundle adjustment to refine positions and handle occlusion

## Loop closure ##
- Identify previous locations seen
- Adjust past camera pose
- Use graph optimization 

## Visualization ##
- Plot camera trajectory and landmarks in 3D