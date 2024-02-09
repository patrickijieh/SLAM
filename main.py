import cv2
import os
import numpy as np

# Load the video
frames_path = r'videos\2011_09_26_drive_0023_sync\2011_09_26\2011_09_26_drive_0023_sync\image_02\data'

# Create an ORB object
orb = cv2.ORB_create(nfeatures=1000)

# Initialize previous keypoints and descriptors
prev_keypoints = None
prev_descriptors = None

ratio_threshold = 0.7 # Adjust this value to make Lowe's ratio less strict

frame_files = [f for f in os.listdir(frames_path) if f.endswith('.png')]

def apply_lowes_ratio_test(matches, ratio=0.75):
    good_matches = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good_matches.append(m)
    return good_matches


for frame_file in frame_files:
    frame = cv2.imread(os.path.join(frames_path, frame_file))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect ORB features
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # Match features with previous frame using Lowe's ratio test
    if prev_descriptors is not None:
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches = matcher.knnMatch(prev_descriptors, descriptors, k=2)

        # Apply Lowe's ratio test
        good_matches = apply_lowes_ratio_test(matches, ratio_threshold)

        obj = []
        scene = []

        for match in good_matches:
            obj.append(prev_keypoints[match.queryIdx].pt)
            scene.append(keypoints[match.trainIdx].pt)

        H = cv2.findHomography(np.array(obj), np.array(scene), cv2.RANSAC, 5.0)[0]

        print(H.shape)
        #print(len(good_matches))
        # Draw matched keypoints on the frame
        frame_with_matches = cv2.drawMatches(prev_frame, prev_keypoints, frame, keypoints, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

        # Display the frame with matches
        cv2.imshow('Feature Matches', frame_with_matches)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    prev_frame = frame
    prev_keypoints = keypoints
    prev_descriptors = descriptors

cv2.destroyAllWindows()