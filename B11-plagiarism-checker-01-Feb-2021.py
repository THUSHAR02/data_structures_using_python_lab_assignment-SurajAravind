# Python Script to test for program plagiarism


##1.  Download the repositories using GitHub classroom assistant
##2.  Rename the folders to identify the student based on registration number and name instead of github username
##    -- > rename_folders()
##3. All the repositories contain same file names.  Compare each file of a repository with the rest of the other repository files.

import os
import pandas as pd
#directory_list = os.listdir()
#print(directory_list)
directory_list = ['121910311001-KATIGARI NAGA MEGHANATHA REDDY','121910311002-AKKALA ARSHIL', '121910311003-VEDULA LAKSHMI SPANDANA',
                  '121910311005-DESAI VENKATA SAI NIRANJAN', '121910311006-A SUJITH REDDY', '121910311007-VEGESNA BHARGAVI',
                  '121910311009-SAI VISHNU MANTHINA', '121910311010-VADDI SAI SUSMITA', '121910311011-VADDI VAMSI KRISHNA',
                  '121910311012-KATIKIREDDY LAKSHMI PRANATHI','121910311013-AKSHAY SANKINENI', '121910311014-POTHU NAGA SAMPATH',
                  '121910311015-JATLA OM PRUDHVI RAJ', '121910311016-KOMPELLA DIVYA SREE', '121910311017-NARASUPALLI NIKHIL',
                  '121910311018-SIRUVURI VENKATA SAI LAHARI', '121910311019-RENUKA LAHARI VNS UPPULURI', '121910311020-ADAPA THANMAI SWATHI',
                  '121910311021-NARNI NIKHIL GUNA TARUN', '121910311022-PAPPALA SAKETH NAIDU', '121910311023-POTNURU SRRIDHAR',
                  '121910311024-ABBIREDDY JAGADEESH REDDY', '121910311025-GUDURU ALEKHYA', '121910311026-RUDRI VENKATA RATNA SAMANVITHA',
                  '121910311027-VEMANAMANDA BALARAMA MURTHY RAJU', '121910311028-KAKARLA SAI PRIYANKA', '121910311029-UPPALAPATI VARUN SAI',
                  '121910311030-G BHARAT CHANDRA', '121910311031-GANAGAM SAI ANISH', '121910311032-PAMPANABOYINA RITESH',
                  '121910311033-SANJAY NAIR', '121910311034-T VENKATA SAI MANJUSHA', '121910311035-RAYALA VENKATA SRAVANTH',
                  '121910311036-GAJAWADA ARIHANT', '121910311037-GUDIMETLA ESWAR SAI CHANDRA REDDY', '121910311038-SUNDARAPU VENKATA LAKSHMI PRASANNA',
                  '121910311039-JITHIN AMBALA', '121910311040-BUDUMURU  BALA PRIYANKA', '121910311041-AKHANDAM SATYADITYA',
                  '121910311042-S D ADITHYA KALYAN VEMULA', '121910311043-KARUMANCHI TARUN SAI', '121910311044-NAREDLA HARISH REDDY',
                  '121910311045-MOHAMMED MUSAIYAB AHAMED', '121910311046-PALISETTI  MONISHSAI', '121910311047-PAPPU DEEPAK',
                  '121910311048-DEEKONDA DHARANI', '121910311049-Y LAKSHMI VARSHITHA', '121910311050-GORRELA SATYA SAI KEERTHI SUBHA',
                  '121910311051-B NITHIN KUMAR GOUD', '121910311052-L ADHILAKSHMI SANTHOSH ANUPAMA', '121910311053-UPPERLA VINAY',
                  '121910311055-BALUSU LOKESH', '121910311056-BORRA VISHAL', '121910311057-JOGA ROHIT ABHINAV',
                  '121910311058-SOBANAPURAM YASHWANT SAI', '121910311059-VANAPARTHI SUSHMANTH', '121910311060-SALADI MOHAN SRI KRISHNA TEJA',
                  '121910311061-POLAROUTHU MADAN VENKAT SAI', '121910311063-YELURI SAI SHREYAS', '121910311064-SAMALA SAI TEJA',
                  '121910311065-YELLAMANCHILI VIVEK DARSHAN']

# Find out the file names of the repository

##os.chdir(directory_list[0])
##print(os.getcwd())
##print(os.listdir())
##['01_1_min_3_numbers.py', '01_2_gcd_lcm_2_numbers.py', '01_2_gcd_lcm_3_numbers.py', '01_3_perfect_number.py', '01_4_twin_primes.py', '01_5_prime_numbers.py', '01_6_sum_of_digits.py', '01_7_armstrong_number.py', '01_8_swap_2_numbers.py', '01_9_all_5_arithmetic_operations.py', '02_linear_list.py', '03_sparse_matrix.py', '04_1_linear_search.py', '04_2_binary_search.py', '05_singly_linked_list.py', '06_doubly_linked_list.py', '07_circular_singly_linked_list.py', '08_stack.py', '09_infix_postfix.py', '10_queue.py', '11_binary_tree_traversals.py', '12_binary_search_tree.py', '13_dfs_bfs_traversals.py', '14_Dijkstra_shortest_path.py', '15_sorting_techniques.py']

file_list = ['01_1_min_3_numbers.py', '01_2_gcd_lcm_2_numbers.py', '01_2_gcd_lcm_3_numbers.py',
             '01_3_perfect_number.py', '01_4_twin_primes.py', '01_5_prime_numbers.py',
             '01_6_sum_of_digits.py', '01_7_armstrong_number.py', '01_8_swap_2_numbers.py',
             '01_9_all_5_arithmetic_operations.py', '02_linear_list.py', '03_sparse_matrix.py',
             '04_1_linear_search.py', '04_2_binary_search.py', '05_singly_linked_list.py',
             '06_doubly_linked_list.py', '07_circular_singly_linked_list.py', '08_stack.py',
             '09_infix_postfix.py', '10_queue.py', '11_binary_tree_traversals.py',
             '12_binary_search_tree.py', '13_dfs_bfs_traversals.py', '14_Dijkstra_shortest_path.py',
             '15_sorting_techniques.py']




import filecmp

## Attempt-1
for directory in directory_list:
    directory_list_1 = directory_list[:]
    directory_list_1.remove(directory)
    for directory_1 in directory_list_1:
        for file in file_list:
            file1 = ".\\" + directory + "\\" + file
            file2 = ".\\" + directory_1 + "\\" + file
            if (filecmp.cmp(file1, file2, shallow=True) == True):
                print(directory, " - ", directory_1, " - ", file, "-similar")


##def rename_folders():
##    my_dataframe = pd.read_excel('2B11-classroom_roster.xlsx')
##    count = 1
##    
##    for directory_name in directory_list:
##        result = my_dataframe.isin([directory_name])
##        seriesObj = result.any()
##        columnNames = list(seriesObj[seriesObj == True].index)
##        for col in columnNames:
##            rows = list(result[col][result[col] == True].index)
##            for row in rows:
##                print("Count: " , count , " Student Registration Number and name: " , my_dataframe['identifier'][row], " Github user name : " , my_dataframe['github_username'][row])
##                count = count + 1
##                os.rename(directory_name, my_dataframe['identifier'][row])
##
##
##
##rename_folders()



##for directory_name in directory_list:
##    print(directory_name)


# Python program to check whether 
# the directory empty or not 

# Identify empty repositories
##
##for directory_name in directory_list:
##    director_contents = os.listdir(directory_name) 
##    if len(director_contents) == 0:
##        #print(directory_name ," - Empty directory")
##        os.rmdir(directory_name)
