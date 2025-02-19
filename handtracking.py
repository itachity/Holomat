import cv2
import mediapipe as mp

# Initialize Mediapipe Hand Solution
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.1,
                       min_tracking_confidence=0.1)

mp_drawing = mp.solutions.drawing_utils

# Open camera

cap = cv2.VideoCapture(0)
print("Camera done processing")

if not cap.isOpened():
    print("Error: Camera not opened.")
    exit()

# Main Loop
while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame color from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB frame with MP Hands
    results = hands.process(rgb_frame)

    # Draw the hand annotations on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Resize the frame to make it larger
    frame = cv2.resize(frame, (1920, 1080))  # Set to desired width and height

    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    cv2.waitKey(1)

# Release resources
cap.release()
cv2.destroyAllWindows()
