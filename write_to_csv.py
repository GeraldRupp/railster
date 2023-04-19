# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:12:15 2023

@author: ruppg
"""


def write_to_csv(data, max_rows_per_file, output_folder,live_type):
    """
    Writes the given data to multiple CSV files with the name "liveint".
    Each file will contain at most max_rows_per_file rows of data.
    The files will be written to the specified output folder.
    """
    import csv
    import os

    import datetime
    # Determine the number of files needed based on the length of data and the maximum rows per file
    num_files = (len(data) + max_rows_per_file - 1) // max_rows_per_file
    current_date = datetime.datetime.now().strftime("%m%d_%Y")
    # Write the data to each file
    for file_index in range(num_files):
        # Compute the file name
        file_name = f"{live_type}_{current_date}_{file_index + 1}.csv"



        # Compute the start and end indices for the current file
        start_index = file_index * max_rows_per_file
        end_index = min(start_index + max_rows_per_file, len(data))

        # Open the file in the specified output folder and write the data to it
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data[start_index:end_index])