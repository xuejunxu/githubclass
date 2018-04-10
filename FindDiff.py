"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    len1=len(line1)
    len2=len(line2)
    #print(len1)
    #print(len2)
    if (len1<len2):
        for string_num in range(len1):
            if (line1[string_num]!=line2[string_num]):
                first_diff=string_num
                return first_diff
                break
        return len1
    elif (len1>len2):
        for string_num in range(len2):
            if (line1[string_num]!=line2[string_num]):
                first_diff=string_num
                return first_diff
                break
        return len2
    else:
        for string_num in range(len1):
            if (line1[string_num]!=line2[string_num]):
                #print(line1[string_num])
                #print(line2[string_num])
                #print(string_num)
                return string_num
                break
        return IDENTICAL



def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    # if line1=='\n':
    #     return ""
    # elif line2=='\n':
    #     return ""
    # elif idx>=len(line1) or idx>=len(line2) or idx<0:
    #     return ""
    if idx>=len(line1) or idx>=len(line2) or idx<0:
        return""
    else:
        #print(line1)
        operator='='*idx+'^'
        #print(operator)
        #print(line2)
        return line1+'\n'+operator+'\n'+line2+'\n'


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    num_line=0
    if len(lines1)<len(lines2):
        line_ind=-1
        for lines in lines1:
            if singleline_diff(lines, lines2[num_line])<0:
                num_line=num_line+1
            else:
                line_ind=num_line
                str_ind=singleline_diff(lines, lines2[num_line])
                break
        if line_ind>=0:
            return (line_ind,str_ind)
        else:
            return (len(lines1),0)
    elif len(lines2)<len(lines1):
        line_ind=-1
        for lines in lines2:
            if (singleline_diff(lines, lines1[num_line]))<0:
                num_line=num_line+1
            else:
                line_ind=num_line
                str_ind=singleline_diff(lines, lines1[num_line])
                break
        if line_ind>=0:
            return (line_ind,str_ind)
        else:
            return (len(lines2),0)
    else:
        line_ind=-1
        for lines in lines2:
            #print(type(singleline_diff(lines, lines1[num_line])))
            #print((singleline_diff(lines, lines1[num_line])))
            if (singleline_diff(lines, lines1[num_line]))<0:
                num_line=num_line+1
            else:
                line_ind=num_line
                str_ind=singleline_diff(lines, lines1[num_line])
                break
        if line_ind>=0:
            return (line_ind,str_ind)
        else:
            return (IDENTICAL,IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile=open(filename,"rt")
    input_file=openfile.read()
    input_file=input_file.rstrip()
    input_file=input_file.lstrip()
    list_of_lines=list(input_file.split("\n"))
    openfile.close()

    return list_of_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1=get_file_lines(filename1)
    lines2=get_file_lines(filename2)
    tup_ind=multiline_diff(lines1, lines2)
    line_in_lines_index=tup_ind[0]
    #print("Line "+str(line_in_lines_index)+":")
    str_in_line_index=tup_ind[1]
    singleline_diff_format(lines1[line_in_lines_index], \
      lines2[line_in_lines_index], str_in_line_index)
    return_str=singleline_diff_format(lines1[line_in_lines_index],\
     lines2[line_in_lines_index], str_in_line_index)

    if line_in_lines_index==-1:
        return "No differences\n"
    else:
        return "Line "+str(line_in_lines_index)+":"+"\n"+return_str

