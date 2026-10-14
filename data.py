# Data storage for Screen Time Tracker
# Sessions are stored in parallel lists: the same index in every list
# belongs to the same session (e.g. app_names[0], minutes[0],
# categories[0] and notes[0] describe the first session).
# Always append to all four lists together so they keep the same length.

# Name of the app or website used (e.g. "YouTube")
app_names = []

# Minutes spent in the session (positive integer)
minutes = []

# Category of the session: Social, School, Entertainment or Other
categories = []

# Optional notes about the session (empty string if none)
notes = []
