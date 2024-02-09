import cv2

# Load the video
video_path = r'D:\Projects\slam\videos\drive.mp4'
cap = cv2.VideoCapture(video_path)

# Create an ORB object
orb = cv2.ORB_create(nfeatures=1000)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize previous keypoints and descriptors
prev_keypoints = None
prev_descriptors = None

ratio_threshold = 1.8 # Adjust this value to make Lowe's ratio less strict

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect ORB features
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # Match features with previous frame using Lowe's ratio test
    if prev_descriptors is not None:
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(prev_descriptors, descriptors)
        matches = sorted(matches, key=lambda x: x.distance)
        good_matches = [m for m in matches if m.distance < ratio_threshold * matches[0].distance]

        print(len(good_matches))
        # Draw matched keypoints on the frame
        frame_with_matches = cv2.drawMatches(prev_frame, prev_keypoints, frame, keypoints, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

        # Display the frame with matches
        cv2.imshow('Feature Matches', frame_with_matches)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    prev_frame = frame
    prev_keypoints = keypoints
    prev_descriptors = descriptors

cap.release()
cv2.destroyAllWindows()