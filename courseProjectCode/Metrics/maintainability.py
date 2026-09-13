"""
This file is used to calculate the maintainability of the pandas core code. It calculates:
- Lines of Code per file
- Comment density per file
- Total Lines of Code
- Total Comment Density

Run calculations by running the main function of this file.
"""

import os
from pygount import SourceAnalysis

def main():

    # prep for totals
    print("Filepath\t\tLines of Code\tComment Density")
    
    total_loc = 0
    total_comments = 0

    # walk through core files
    for root, _, files in os.walk("pandas/core"):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                # analyze file
                analysis = SourceAnalysis.from_file(file_path, group="core")

                density = 0 if analysis.documentation_count + analysis.code_count == 0 else analysis.documentation_count/(analysis.code_count + analysis.documentation_count)
                density_percent = int(density * 100)
                print(f"{file_path}\t\t{analysis.code_count}\t\t{density_percent}%")
        
                total_loc += analysis.code_count + analysis.documentation_count
                total_comments += analysis.documentation_count

            except Exception as e:
                # print(e)
                continue # this is for skipping unexpected files 


    total_density = 0 if total_loc == 0 else total_comments/total_loc
    total_density_percent = int(total_density*100)
    print(f"Total\t\t\t{total_loc}\t\t{total_density_percent}%")


if __name__ == "__main__":
    main()