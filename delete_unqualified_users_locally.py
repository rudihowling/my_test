#modify local file version

import pandas as pd

def remove_rows_with_xuan(file_path, sheet_name=0, output_file="G:/Keelworks/Keelworks/scripts/GWS/today.xlsx"): #modify this path to desired excel file
    try:
        # Read Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")  # Explicitly use openpyxl for xlsx files
        
        # Validate that 'Email Address [Required]' exists in the columns
        if 'Email Address [Required]' in df.columns:
            emails_to_remove = [
                'github.admin@keelworks.org', 'admin@keelworks.org', 'newsletter@keelworks.org',
                'op.admin@keelworks.org', 'q4dummy4@keelworks.org', 'q2dummy2@keelworks.org', 
                'q3dummy3@keelworks.org', 'script.admin@keelworks.org', 'teamgantt-admin@keelworks.org',
                'unsubscribe@keelworks.org', 'volunteer.coordinator@keelworks.org', 'funding@keelworks.org',
                'info@keelworks.org'
            ]
            
            # Remove rows where 'Email Address [Required]' is in the list
            df = df[~df['Email Address [Required]'].isin(emails_to_remove)]
            
            # Save the cleaned data to the new Excel file
            df.to_excel(output_file, index=False, engine="openpyxl")
            print(f"Results have been saved to {output_file}")
        else:
            print("Failed: 'Email Address [Required]' column not found!")

    except Exception as e:
        print(f"Error: {e}")

# Test the function
remove_rows_with_xuan("G:/Keelworks/Keelworks/scripts/GWS/User_Download.xlsx") #modify this path to downloaded file
