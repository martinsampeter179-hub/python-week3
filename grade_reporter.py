# Starting list of scores
scores = [72, 45, 90, 61, 38]

# Initialize trackers for pass/fail counts and total score
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score  # Add score to running total
    
    # Determine grade based on score threshold
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Track pass/fail outcomes (50 or higher passes)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1
        
    print(f"Score: {score} - Grade: {grade}")

# Calculate average score rounded to 1 decimal place
average_score = round(total_score / len(scores), 1)

# Print final statistics
print("-" * 30)
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average score: {average_score}")
