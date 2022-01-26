import subprocess
import os
import time


# grab the epoch timestamp at run time and convert to human-readable for the artifact output document footer information
timeStamp = time.time()

# convert epoch timestamp to human-readable date time formatted
report_time = time.strftime('%c', time.localtime(timeStamp))

# create a custom string to be included at the end of the generated output
report_time_footer = str('Artifacts generated on: ') + report_time + str('\ncreated by Python Automated IOC Generator') + str('\n\n')

#/////////////  BEGIN -- Generate IOC artifacts
#///////////// File Name, MD5 hash, SHA-1 hash, File size in bytes

# create and open a file named 'output.txt' to write our data to
f = open("output.txt", "w")

def iocGrab(arg):

    # store a single entry value from direct user input, or from the directory_as_input() function
    target_file = arg

    # Grab the name of the file, create a custom string, print output to screen, as well as write to 'output.txt'
    fileName = "\nFile name: " + target_file + "\n\n"
    print(fileName)
    f.write(fileName)

    # use subprocess to call the md5 command in the os
    process = subprocess.Popen(['md5', target_file], 
                               stdout=subprocess.PIPE,
                               encoding='utf-8')
    data = process.communicate()
    # Store the MD5 hash value as md5Data, print output to screen, as well as write to 'output.txt'
    md5Data = data[0]
    print(md5Data)
    f.write(md5Data)

    # use subprocess to call the shasum command using the '-a' and '1' options in the os
    process = subprocess.Popen(['shasum', '-a', '1', target_file], 
                               stdout=subprocess.PIPE,
                               encoding='utf-8')
    data2 = process.communicate()
    # Store the SHA-1 hash value as sha1Data, print output to screen, as well as write to 'output.txt'
    sha1Data = str("SHA-1: ") + str(data2[0])
    print(sha1Data)
    f.write(sha1Data)

    # use stat module's os.stat results and st_size to grab the file size in bytes
    size = os.stat(target_file).st_size
    # Store the 'size' value as fileSizeBytes, create a custom string, print output to screen, as well as write to 'output.txt'
    fileSizeBytes = str("Size in bytes: ") + str(size) + str("\n\n")
    print(fileSizeBytes)
    f.write(fileSizeBytes)

    return

#/////////////  END -- Generate IOC artifacts
    
#/////////////  BEGIN -- Directory as input

def directory_as_input(arg):

    # store the directory_as_input value in the path_of_the_directory variable
    path_of_the_directory = arg

    # initialize list 'i'
    i = [ ]

    for i in os.listdir(path_of_the_directory):
            iocGrab(i)

    f.write(report_time_footer)
    f.close()

    print(report_time_footer)

#/////////////  END -- Directory as input

#/////////////  Begin -- MAIN 

def main():
    print("\nPython Automated IOC Generator \nGathers File Name, MD5 hash value, SHA-1 hash value, and File Size in Bytes")

    # Prompt user for input of a single entry, or to select a directory of files to submit as input
    single_or_multiple_entries = int(input("\nEnter: \n'1' for single entry, or \n'2' to select a directory of files as input: "))
    
    # Conditional statement to handle user input and select the appropriate function
    if single_or_multiple_entries == 1:
        iocGrab(input("\nEnter path to file: "))
        f.write(report_time_footer)
        f.close()
        print(report_time_footer)
    elif single_or_multiple_entries == 2:
        directory_as_input(input("\nEnter path to directory of files: "))
    else:
        print("\n Please enter a valid option! \n")

#/////////////  End -- MAIN

main()