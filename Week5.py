

import numpy as np

def DeNormalize():

    # Load the dataset into a NumPy array 
    
    # In practice, you can use np.loadtxt() or np.genfromtxt() to load data from a CSV.
    data = np.genfromtxt('bikeSharing.csv', delimiter=',', skip_header=1)
    
        # Column indices for the normalized columns
    temp_index = 9      
    atemp_index = 10    
    hum_index = 11       
    windspeed_index = 12 
    
    # Create a copy of the original data to preserve the original values
    denormalized_data = data.copy()
    
    # De-normalize the columns by multiplying them by their maximum values
    denormalized_data[:, temp_index] *= 41
    denormalized_data[:, atemp_index] *= 50
    denormalized_data[:, hum_index] *= 100
    denormalized_data[:, windspeed_index] *= 67
    
    # Print the resulting NumPy array with real values
    print(denormalized_data)
    np.savetxt("deNormalized.csv", denormalized_data, fmt='%.2f', delimiter=',')

#DeNormalize()


def extractFromFile():
    # Step 1: Load the bikeshare dataset
    # Replace 'bikeshare.csv' with the actual path to your dataset
    data = np.loadtxt('bikeSharing.csv', delimiter=',', skiprows=1)

    # Step 2: Get total number of rows
    total_rows = data.shape[0]

    # Calculate size of each section
    section_size = total_rows // 3  # Integer division

    # Step 3: Slice the data into three sections
    section1 = data[:section_size]                         # First third
    section2 = data[section_size:2 * section_size]         # Second third
    section3 = data[2 * section_size:]                     # Final third

    # Step 4: Combine Section 1 and Section 3
    newArray = np.vstack((section1, section3))

    # Step 5: Save the new array to a new CSV file
    np.savetxt("newBike.csv", newArray, fmt='%.2f', delimiter=',')

    print("New CSV file 'newBike.csv' created successfully!")

#extractFromFile()




import numpy as np

def analyze_bikeshare(file_path):
    """
    Analyzes a bikeshare dataset by splitting it into three equal sections,
    then calculates and interprets the average temperature and casual users
    for each section.

   
    """
    temp_col_index = 9  # Index of temperature
    casual_col_index = 13  # Index of casual users
    # Step 1: Load the dataset
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    
    # Step 2: Get total rows and determine section size
    total_rows = data.shape[0]
    section_size = total_rows // 3  # integer division for three equal sections
    
    # Step 3: Split data into three sections
    section1 = data[:section_size]
    section2 = data[section_size:2 * section_size]
    section3 = data[2 * section_size:]
    
    # Step 4: Calculate averages
    averages = {
        "temperature": {
            "section1": np.mean(section1[:, temp_col_index]),
            "section2": np.mean(section2[:, temp_col_index]),
            "section3": np.mean(section3[:, temp_col_index]),
        },
        "casual_users": {
            "section1": np.mean(section1[:, casual_col_index]),
            "section2": np.mean(section2[:, casual_col_index]),
            "section3": np.mean(section3[:, casual_col_index]),
        }
    }
    
    # Step 5: Print results
    print("\n--- Average Temperature per Section ---")
    for sec, val in averages["temperature"].items():
        print(f"{sec.capitalize()}: {val:.2f}")
    
    print("\n--- Average Casual Users per Section ---")
    for sec, val in averages["casual_users"].items():
        print(f"{sec.capitalize()}: {val:.2f}")
    
    # Step 6: Interpret results
    casual_users = list(averages["casual_users"].values())
    if casual_users[0] < casual_users[1] < casual_users[2]:
        interpretation = "Casual users increase over time, possibly due to warmer weather or growing popularity."
    elif casual_users[0] > casual_users[1] > casual_users[2]:
        interpretation = "Casual users decrease over time, which might indicate seasonal decline or reduced demand."
    else:
        interpretation = "The pattern of casual users does not follow a simple increasing or decreasing trend."
    
    print("\n--- Interpretation ---")
    print(interpretation)
    
    # Step 7: Return results
    return {
        "averages": averages,
        "interpretation": interpretation
    }

# Example usage:
# result = analyze_bikeshare('bikeshare.csv', temp_col_index=1, casual_col_index=2)


#analyze_bikeshare("bikeSharing.csv")

import numpy as np

def analyze_bikeshare_in_chunks(file_path, chunk_size=1000):
    """
    Reads a bikeshare dataset and splits it into chunks of specified size.
    For each chunk, calculates the average feeling temperature and
    average number of casual users.

    Parameters:
        file_path (str): Path to the bikeshare CSV file.
        feel_temp_col_index (int): Column index for feeling temperature.
        casual_col_index (int): Column index for casual users.
        chunk_size (int): Number of rows per section (default is 1000).

    Returns:
        list: A list of dictionaries containing averages for each chunk.
    """
    feel_temp_col_index=10
    casual_col_index=13
    # Step 1: Load data (skip header row if CSV has one)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)

    # Step 2: Split data into chunks
    sections = []
    for i in range(0, len(data), chunk_size):
        sections.append(data[i:i + chunk_size])
    
    print(f"Total sections created: {len(sections)}")
    
    # Step 3: Calculate averages for each section
    results = []
    for idx, section in enumerate(sections, start=1):
        avg_feel_temp = np.mean(section[:, feel_temp_col_index])
        avg_casual_users = np.mean(section[:, casual_col_index])
        
        results.append({
            "section": idx,
            "avg_feeling_temp": avg_feel_temp,
            "avg_casual_users": avg_casual_users
        })
        
        print(f"\nSection {idx}:")
        print(f"  Average Feeling Temperature: {avg_feel_temp:.2f}")
        print(f"  Average Casual Users: {avg_casual_users:.2f}")
    
    # Step 4: Interpretation (basic trend check for casual users)
    casual_values = [res["avg_casual_users"] for res in results]
    if casual_values == sorted(casual_values):
        print("\nPattern Observed: Casual users tend to increase over time.")
    elif casual_values == sorted(casual_values, reverse=True):
        print("\nPattern Observed: Casual users tend to decrease over time.")
    else:
        print("\nPattern Observed: Casual users show mixed or seasonal variation.")

    return results

# Example usage:
# results = analyze_bikeshare_in_chunks('bikeshare.csv', feel_temp_col_index=1, casual_col_index=2, chunk_size=1000)

#analyze_bikeshare_in_chunks('bikeSharing.csv')






import numpy as np

def add_difference_column(file_path, output_file='newBike.csv'):
    """
    Reads the bikeshare dataset, computes the difference between registered and casual users,
    appends this as a new column, and writes the updated array to a new CSV file.

    Parameters:
        file_path (str): Path to the original bikeshare CSV file.
        output_file (str): Name of the new CSV file to save the updated data.
        casual_col_index (int): Index of the casual users column.
        registered_col_index (int): Index of the registered users column.

    Returns:
        numpy.ndarray: The updated NumPy array with the new difference column included.
    """
    casual_col_index = 13  # Index for casual users
    registered_col_index = 14  # Index for registered users
    # Step 1: Load dataset (skip the header row if present)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    
    # Step 2: Compute the difference (registered - casual) for each record
    difference = data[:, registered_col_index] - data[:, casual_col_index]
    
    # Step 3: Reshape difference into a column vector
    difference = difference.reshape(-1, 1)
    
    # Step 4: Append the new column to the original data
    updated_data = np.hstack((data, difference))
    
    # Step 5: Save the updated data into a new CSV file
    np.savetxt(output_file, updated_data, delimiter=',', fmt='%.2f')
    
    print(f"Updated data saved successfully to '{output_file}'")
    return updated_data

# Example usage:
# updated_array = add_difference_column('bikeshare.csv', output_file='newBike.csv', casual_col_index=2, registered_col_index=3)
#add_difference_column('bikeSharing.csv')


import numpy as np

def remove_first_column(file_path, output_file='newBike.csv'):
    """
    Reads a bikeshare dataset, removes the first column, 
    and saves the remaining data to a new CSV file.

    Parameters:
        file_path (str): Path to the original bikeshare CSV file.
        output_file (str): Name of the new CSV file to save the result.

    Returns:
        numpy.ndarray: The NumPy array with the first column removed.
    """
    
    # Step 1: Load dataset (skip the header row if present)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    
    # Step 2: Remove the first column using slicing
    updated_data = data[:, 1:]  # keep all rows, columns from index 1 onward
    
    # Step 3: Save the updated data into a new CSV file
    np.savetxt(output_file, updated_data, delimiter=',', fmt='%.2f')
    
    print(f"Updated data saved successfully to '{output_file}'")
    return updated_data

# Example usage:
# result = remove_first_column('bikeshare.csv', output_file='newBike.csv')

#remove_first_column('bikeSharing.csv')



import numpy as np
import string

# Function to check if a string is a valid number (int or float)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def analyze_text_file(input_file, output_csv):
    # Define punctuation characters
    punctuation_set = set(string.punctuation)

    # Store results for all lines
    results = []

    # Read the file line by line
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            
            # Convert line into a numpy array of characters for vectorized operations
            char_array = np.array(list(line))
            
            # 1. Count words
            words = line.split()
            num_words = len(words)

            # 2. Count punctuations
            num_punctuations = np.isin(char_array, list(punctuation_set)).sum()

            # 3. Count spaces
            num_spaces = line.replace(' ', '')
            num_spaces = len(line)-len(num_spaces)

           
            # 4. Count numerical components (tokens that are numbers)
            num_numerical_components = sum(is_number(word) for word in words)

            # Append the results for this line
            results.append([
                num_words,
                num_punctuations,
                num_spaces,
                
                num_numerical_components
            ])

    # Convert results to numpy array
    results_array = np.array(results, dtype=int)
    np.savetxt(output_csv, results_array, delimiter=',', fmt='%.2f')

    
    print(f"Analysis complete. Results saved to {output_csv}")

# Example usage
analyze_text_file('SherlockHolmes.txt', 'output.csv')


