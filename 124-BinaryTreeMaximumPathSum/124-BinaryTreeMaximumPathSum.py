left_gain = max(gain_from_left_subtree, 0)
right_gain = max(gain_from_right_subtree, 0)
gain_from_subtree = max(left_gain, right_gain) + root.val