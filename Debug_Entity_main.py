from tkinter import *
from tkinter import ttk
from Debug_Entity_alphabet_sort import *
from Debug_Entity_rollnumber_sorting import *

#initializing the root window
root = Tk()
root.title("CS101 PROJECT")
root.geometry('1600x900')
bi = PhotoImage(file = "Debug_Entity_image.jpg")
my_label = Label(root, image = bi)
my_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)



#creating label for the heading
myLabel2 = Label(root, text = "***STUDENT CONTACT BOOK***").grid(row = 1,column = 4)


#initializing the string variables
first = StringVar()
last = StringVar()
batch = StringVar()
phone = StringVar()
roll = StringVar()
branch = StringVar()
search_value = StringVar()
update_name = StringVar()


#creating entry boxes
Entry(root,width =50, bg = "white", borderwidth = 5, textvariable = first).grid(row = 16,column = 1, columnspan = 1, padx = 10, pady = 10) # first name
Entry(root,width =50, bg = "white", borderwidth = 5, textvariable = last).grid(row = 17,column = 1, columnspan = 1, padx = 10, pady = 10) #last name
Entry(root,width =50, bg = "white", borderwidth = 5, textvariable = roll).grid(row = 19,column = 1, columnspan = 1, padx = 10, pady = 10) #roll number
Entry(root,width =50, bg = "white", borderwidth = 5, textvariable = phone).grid(row = 20,column = 1, columnspan = 1, padx = 10, pady = 10) #phone number
Entry(root,width =50, bg = "white", borderwidth = 5, textvariable = batch).grid(row = 21,column = 1, columnspan = 1, padx = 10, pady = 10) #batch
Entry(root,width =40, bg = "white", borderwidth = 5, textvariable = search_value).grid(row = 48,column = 1, columnspan = 1, padx = 10, pady = 10) #search (look for entry)
Entry(root,width =40, bg = "white", borderwidth = 5, textvariable = update_name).grid(row = 9,column = 4, columnspan = 1, padx = 10, pady = 10) #update an entry based on name


#creating labels for the entry boxes
f_name_label = Label(root, text = "First Name:")
f_name_label.grid(row = 16, column = 0)

l_name_label = Label(root, text = "Last Name:")
l_name_label.grid(row = 17, column = 0)

branch_label = Label(root, text = "Branch(CSE/EE/ME/MC):")
branch_label.grid(row = 18, column = 0)

roll_num_label = Label(root, text = "Roll Number:")
roll_num_label.grid(row = 19, column = 0)
phone_label = Label(root, text = "Phone Number:")
phone_label.grid(row = 20, column = 0)

batch_label = Label(root, text = "Batch:")
batch_label.grid(row = 21, column = 0)

space1_label = Label(root, text = " ")
space1_label.grid(row = 22, column = 0)

space1_label = Label(root, text = " ")
space1_label.grid(row = 24, column = 0)

space3_label = Label(root, text = " ")
space3_label.grid(row = 26, column = 0)

space4_label = Label(root, text = " ")
space4_label.grid(row = 28, column = 0)

new_entry_label = Label(root, text = "**NEW ENTRIES**")
new_entry_label.grid(row = 14, column = 1)

view_label = Label(root, text = "**STUDENT NAMES**")
view_label.grid(row = 11, column = 99)

contact1_label = Label(root, text = "**CONTACT UPDATION**")
contact1_label.grid(row = 8, column = 2)

#drop down for branch
list2 = ["CSE", "MC","EE", "ME"]
my_branch = ttk.Combobox(root, value = list2)
my_branch.current(0)
my_branch.grid(row = 18,column = 1)    

#creating list box (which will display names of students which we can select and do operations on them)
scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=15)
scroll_bar.config (command=select.yview)
select.place(x = 1000, y = 150)



#defining the dictionary add text to our database
d = { 'first_name' : " ", 'last_name' : " ", "batch" : " ", "phone": " ", 'roll' : " ", 'branch' : " "}

#defining functions for Clicking the Button

#POPUP WINDOW--------------------------------------------------------------------------------------

def popupmsg(msg, title):
    '''creates a popup window whenever called. It takes 2 arguments :title-title of popup window 
    msg - message to be printed on that window. '''
    popup = Tk()
    popup.geometry("+800+200")               #defines position of popup
    popup.geometry("550x350")                #defines size of popup window

    popup.wm_title(title)
    label = Label(popup, text = msg, justify = LEFT)
    label.pack()
    popup.mainloop()


#ADD ENTRY---------------------------------------------------------------------------------------------

def addClick():
    '''it takes values from entry boxes/drop down and add them to our Debug_Entity_database.txt file 
    also adds the names to the list box'''
    global d                  
    #  .get() is used to receive values written in the entry boxes       
    first_name = first.get()              
    last_name = last.get()
    batch_year = batch.get()
    phone_number = phone.get()
    roll_number = roll.get()
    branch_ = my_branch.get()
    
    f = open("Debug_Entity_database.txt", 'a+')
    name = first_name + last_name
    #adding the name to dictionary
    for i in name:
        #checking for ascii values of lower and uppercase alphbets
        try:
            if(ord(i) >= 97 and ord(i)<= 122) or ((ord(i)>= 65 and ord(i)<=90)):
                d['first_name'] = first_name
                d['last_name'] = last_name
        
            else:
                msg = "Please enter a valid name!"
                popupmsg(msg, "ERROR")               #calling the popup function
        except:
            continue
            

    d['batch'] = batch_year
    #adding the phone number to dictionary
    for j in phone_number:
        #checking whether the phone number entered is of 10 digits
        try:
            if ord(j) >= 48 and ord(j)<=57 and len(phone_number)==10:
                d['phone'] = phone_number
                    
            else:
                #error prompt
                msg = "Please enter a valid phone number!"
                popupmsg(msg, "ERROR")
        except:
            continue

    #adding the roll number to the dictionary
    for k in roll_number:
        #checking whether the enterned values are digits by matching with their ascii values i.e. 48 to 57 and should be of length 7
        try:
            if ord(k) >= 48 and ord(k)<=57 and len(roll_number)==7:
                d['roll'] = roll_number   
            else:
                #error prompt
                msg = "Please enter a valid roll number!"
                popupmsg(msg, "ERROR")
        except:
            continue
   #adding the branch
    if branch_ == 'CSE' or branch_ == 'EE' or branch_ == 'MC' or branch_ == 'ME':
        d['branch'] = branch_
    else:
        #error prompt
        msg = "Please enter a valid branch!"
        popupmsg(msg, "ERROR")
        
    #adding all the details of the stident to the Debug_Entity_database.txt
    f.write(str(d))
    f.write('\n')
    f.seek(0,0)
    a = f.read()
    b = f.readline()
    f.close()
    #storing name in name variable
    name = " "
    name = first.get() +" " + last.get()
    #adding names to the list box
    select.insert(0,name)

#----VIEWING DETAILS----------------------------------------------------------------------------------    
def viewClick():
    '''will display the details of the student selected from the list box'''

    #storing the selected value of the list box in the variable name
    name = select.get(select.curselection())
    f = open("Debug_Entity_database.txt", 'r')             #opening the Debug_Entity_database.txt file
    f.seek(0)                                 #to move the mouse pointer to the start of file
    lines = f.readlines()
    for i in lines:
        d = eval(i)                          #takes the input as string and evaluates it as python expression
        if d['first_name'] + " " + d['last_name'] == name:
            msg = " \n\n"
            msg +="NAME:   " + name + "\n\n" +"ROLL NUMBER :   " + d['roll'] + "\n\n"+"BRANCH :   " + d['branch'] + "\n\n"+"PHONE NUMBER :   " + d['phone'] + "\n\n"+"BATCH :   " + d['batch'] + "\n\n"
            popupmsg(msg, "STUDENT DETAILS")                   #to display popup window


#DELETE-------------------------------------------------------------------------------------------- 
def abc():
    '''removes the selected value from the list box'''
    sel = select.curselection()
    for index in sel[::-1]:
            select.delete(index)

def delClick():
    '''deletes the details of a student from Debug_Entity_database.txt file and also deletes the student name from the list box by
       calling the abc function in it''' 
    name = select.get(select.curselection())
    f = open("Debug_Entity_database.txt", 'a+')         #opening Debug_Entity_database.txt file in append+read mode
    f.seek(0,0)                            #moving the cursor to start of file
    f_new = open("temp.txt", "a+")
    lines = f.readlines()                  #reading the file content
    for i in lines:
        d = eval(i)
        #adding all the entries to the file called temp.txt except the one which we want to delete
        if d['first_name'] + " " + d['last_name'] != name:      
            f_new.write(i)
    f_new.close()                         #closing temp.txt
    f.close()                             #closing Debug_Entity_database.txt
    #replacing the contents of Debug_Entity_database.txt with temp.txt
    f_new = open("temp.txt", 'r') 
    lines = f_new.readlines()
    f = open("Debug_Entity_database.txt", "w")
    for i in lines:
        f.write(i)
    f.close()
    f_new.close()
    #making temp.tst empty
    f_new = open("temp.txt","w")
    f_new.close()
    abc()                               #calling abc to delete name from list box

    
def clearClick():
    '''to clear the entry boxes'''

    first.set('')
    last.set('')
    branch.set('')
    roll.set('')
    branch.set('')
    phone.set('')
    batch.set('')
    update_name.set('')


def exitClick():
    '''closing the program'''
    root.destroy()


#----SEARCH-----------------------------------------------------------------------------------------------
#creating drop down for searching
l = ["First Name", "Last Name", "Roll Number"]
my_combo = ttk.Combobox(root, value = l)
my_combo.current(0)
my_combo.grid(row = 48,column = 0)    

search_by = ['First Name', 'Last Name', 'Roll Number']               #parameters for searching in drop down
d_search = ['first_name', 'last_name', 'roll']                       #dictionary keys used in searching

def searchClick():
    '''will take the value selected from the dropdown and then take the corresponding value entered in entry box 
       ans will display the details of that student in a popup window'''
    g = my_combo.get()                             #stores value selected in the drop down
    search_criteria = search_value.get()           #stores value written in the search entry box
    found = False                                  #flag to check whether entry found or not
    msg = " \n\n"
    index = 0
    #stores the index of selected value in the dropdown in variable called index
    for i in range(3):
        if g == search_by[i]:
            index = i
            break
    #looking for entry in Debug_Entity_database.txt
    f = open("Debug_Entity_database.txt", "r")
    lines = f.readlines()
    for line in lines:
        d_line = eval(line)
        if search_criteria == d_line[d_search[index]]:
            found = True
            msg +="NAME:   " + d_line['first_name']+" "+d_line['last_name'] + "\n" +"ROLL NUMBER :   " + d_line['roll'] + "\n"+"BRANCH :   " + d_line['branch'] + "\n"+"PHONE NUMBER :   " + d_line['phone'] + "\n"+"BATCH :   " + d_line['batch'] + "\n"
    #generating popup
    popupmsg(msg, "SEARCH")
    f.close()             #closing txt file
    if found == False:
        #if no entry found the deplays no result found
        searchLabel = Label(root, text ="No results found!").grid(row = 15, column = 3)


#-----SORT-----------------------------------------------------------------------------------------------------------

#creating sort dropdown menu
l_sort = ["Alphabetically", "Roll Number", "Currently Enrolled", "Passed Out", "EE Students", "ME Students", "CSE Students", "MC Students"]
combo_sort = ttk.Combobox(root, value = l_sort)
combo_sort.current(0)
combo_sort.grid(row = 54, column = 1) 

def sortClick():
    '''will take the selected parameter from the dropdown and will generate a popup with sorted details'''

    l_sort = ["Alphabetically", "Roll Number", "Currently Enrolled", "Passed Out",
               "EE Students", "ME Students", "CSE Students", "MC Students"]
    #initializing lists to store sorted values
    EE_list = []
    CSE_list= []
    MC_list = []
    ME_list = []
    s = combo_sort.get()                        #sortes the selected value in the dropdown
    f = open("Debug_Entity_database.txt", 'r')
    lines = f.readlines()                       #reads the txt file
#---BRANCH WISE SORTING-------------------------------
    #prints the names of EE students in a popup window
    if s == "EE Students":
        for line in lines:
            d_line = eval(line)
            if d_line['branch'] == "EE":
                EE_list.append(d_line['first_name'] + " " + d_line['last_name'])
            else:
                continue
        msg = " "
        for i in EE_list:
            msg = msg + i + "\n"
        popupmsg(msg, "EE STUDENTS")
        

     #print the names of MC students in a popup window       
    elif s == "MC Students" :
        for line in lines:
            d_line = eval(line)
            if d_line['branch'] == "MC" :
                MC_list.append(d_line['first_name'] + " " + d_line['last_name'])
        msg = " "
        for i in MC_list:
            msg = msg + i + "\n"
        popupmsg(msg, "MnC STUDENTS")
        
    #prints the names of CSE students in a popup window
    elif s == "CSE Students" :
        for line in lines:
            d_line = eval(line)
            if d_line['branch'] == "CSE" :
                CSE_list.append(d_line['first_name'] + " " + d_line['last_name'])
        msg = " "
        for i in CSE_list:
            msg = msg + i + "\n"
        popupmsg(msg, "CSE STUDENTS")
        
    #prints the names of ME students in a popup window
    elif s == "ME Students" :
        for line in lines:
            d_line = eval(line)
            if d_line['branch'] == "ME" :
                ME_list.append(d_line['first_name'] + " " + d_line['last_name'])
        msg = " "
        for i in ME_list:
            msg = msg + i + "\n"
        popupmsg(msg, "ME STUDENTS")
    f.close()         


#ALPHABETICALLY SORTING-----------------------------
    
    stu_names = []                        #initializing a list to store the names of students
    f = open("Debug_Entity_database.txt", "r")
    lines = f.readlines()
    #if the selected parameter is Alphabetically then it will read the txt file and look for names and append them to stu_names
    if s == "Alphabetically": 
        for g in lines:
            dic = eval(g)
            stu_names.append(dic['first_name']+" "+dic['last_name'])

        #using the alphabetically_sort function present in alphabet_sort module
        sorted_names = alphabetically_sort(stu_names)       #stores a sorted list of student names
        #creating popup window and the content to display on it
        msg = " \n\nNAMES\n\n\n"
        for name in sorted_names:
            msg += name + " \n"
        popupmsg(msg,"SORTED LIST BY ALPHABETICAL ORDER")
        


#---BRANCH WISE SORTING------------------------------------
    #initializing lists to store student names
    l_passedout = []
    l_enrolled = []
    f = open("Debug_Entity_database.txt", 'r')
    f.seek(0)
    msg = " "
    lines = f.readlines()
    #if the selected parameter is passesOut then it looks for the batch year less than or equal to 2017
    if s == "Passed Out":
        for i in lines:
            d = eval(i)
            year = d['batch']
            if  int(year) <= 2017 :
                #creating popup message of student names
                msg +=(d['first_name'] + " " + d['last_name']) + "\n"
        popupmsg(msg, "PASSED OUT STUDENTS")

    #if the selected parameter is currently enrolled then it looks for batch year greater than 2017 
    elif s == "Currently Enrolled":
        for i in lines:
            d = eval(i)
            year = d['batch']
            if int(year) > 2017:
                #generating popup message of student names
                msg += d['first_name'] + " " + d['last_name'] + "\n"
        popupmsg(msg, "CURRENTLY ENROLLED STUDENTS")
    f.close()

#---ROLL NUMBER SORTING--------------------------------------

    s = combo_sort.get()                #storing the slected value from the dropdown
    if s == "Roll Number":
      #reading the data from the file
      f = open("Debug_Entity_database.txt", 'r')
      Roll_Number=[]                   #initializing a list to store roll numbers of students
      lines=f.readlines()
      for line in lines: 
          #searching for roll number of each student in the txt file and appending them to the list called Roll_Number
          start= line.find("'roll': '")+len("'roll': '")
          end= line.find("', 'branch'")
          substring=line[start:end]
          Roll_Number.append((substring))
          (line.rstrip())    
      f.close()

      #insertion sort based sorting of roll numbers
      sort_Roll(Roll_Number)
      #generating popup message containing name,roll_number,branch of students sorted on the basis of increasing roll number
      msg = "\n\nNAME                               ROLL NUMBER                         BRANCH\n\n"
      f = open("Debug_Entity_database.txt", "r")
      lines = f.readlines()
      for i in B:
          for line in lines:
            D = eval(line)
            if D['roll'] == i:
                msg += str(D['first_name']+" " + str(D['last_name']) + "."*(35-(len(D['first_name'])+len(D['last_name']))) + i + "."*(45-len(i)) + str(D['branch']) + "\n")
          
      popupmsg(msg, "SORTED BY ROLL NUMBER")
      

#---UPDATE-----------------------------------------------------------------------------------------------------

def openClick():
    '''this function is called when openList button is pressed.
       it displays the names of all the students whose details are stored in the Debug_Entity_database.txt file'''
    #adding existing names to the list box
    f = open("Debug_Entity_database.txt", 'r')
    lines = f.readlines()
    for i in lines:
        #iterates through each line of Debug_Entity_database.txt and takes firstname and last name and adds it to the listbox
        dictionary = eval(i[: -1])
        name = dictionary['first_name'] + " " + dictionary['last_name']
        select.insert(0,name)
        
def upClick():
    '''this function is called when update button is pressed
       it checks if the name entered in the entry box is present in the database or not .
       if it is present , then it generates a message'''
    new = update_name.get()                            #get the name of the student whose details you want to update
    f = open("Debug_Entity_database.txt", 'r')
    f.seek(0,0)
    for i in f:
        dy = eval(i)
        found = False
        #checking whether entered name exists or not
        if dy['first_name'] + " " + dy['last_name'] != new:
            continue
        #if name foound then popup message for the next step
        else:
            found = True
            popupmsg("Please enter the new details for this student and click the Save Changes Button!", "UPDATE")
    #generating msg if name not found  
    if found == False:
        popupmsg("This name is not present in our database", "INVALID NAME")
        

#SAVE CHANGES---------------------------------------------------------------------------------------------------
def saveClick():
    '''this function is called when the SAVE CHANGES button is pressed
        it modifies the entered details of the selected student.'''
    #getting the modified values from the entry boxes
    first_name = first.get()
    last_name = last.get()
    batch_year = batch.get()
    phone_number = phone.get()
    roll_number = roll.get()
    branch_ = my_branch.get()
    f = open("Debug_Entity_database.txt", 'r')
    f.seek(0,0)
    name = first_name + last_name
    lines = f.readlines()
    dd = {}                              #initializing dictionary to store the modified entries
    for i in lines:
        d = eval(i)
        if d['first_name'] + d['last_name'] == name:
        #adding the name to the dictionary called d
            for i in name:
                if(ord(i) >= 97 and ord(i)<= 122) or ((ord(i)>= 65 and ord(i)<=90)):
                    d['first_name'] = first_name
                    d['last_name'] = last_name
                else:
                    msg = "Please enter a valid name!"
                    popupmsg(msg, "ERROR")
                    
                    
            d['batch'] = batch_year
            #adding the phone number to d
            for j in phone_number:
                if ord(j) >= 48 and ord(j)<=57 and len(phone_number)==10:
                    d['phone'] = phone_number
                         
                else:
                    msg = "Please enter a valid phone number!"
                    popupmsg(msg, "ERROR")
                    

            #adding the roll number to d
            for k in roll_number:
                if ord(k) >= 48 and ord(k)<=57 and len(roll_number)==7:
                     d['roll'] = roll_number  
                else:
                    msg = "Please enter a valid roll number!"
                    popupmsg(msg, "ERROR")
                    
           #adding the branch to d
            if branch_ == 'CSE' or branch_ == 'EE' or branch_ == 'MC' or branch_ == 'ME':
                d['branch'] = branch_
            else:
                msg = "Please enter a valid branch!"
                popupmsg(msg, "ERROR")
            dd = d                                  #storing all the values of d in dd
    f.close()
    #creating a file temp.txt to store all the dictionaries apart from the one to be modified
    f = open("Debug_Entity_database.txt","r")
    f_new = open("temp.txt","w")
    f_new.seek(0,0)
    lines = f.readlines()
    for line in lines:
        d_new = eval(line)
        if name != d_new['first_name']+d_new['last_name']:
            f_new.write(line)
    f_new.close()
    f.close()

    f_new = open("temp.txt","r")
    #empting the Debug_Entity_database.txt file and appending contents of temp.txt
    f = open("Debug_Entity_database.txt", "w")
    lines = f_new.readlines()
    for line in lines:
        f.write(line)
    f.close()
    f_new.close()
    f = open("Debug_Entity_database.txt", "a+")
    #appending the modified dictionary
    f.write(str(dd))
    f.close()
    #empting the temp.txt file
    f_new = open("temp.txt" ,'w')
    f_new.close()
    #generating message
    msg = "Entries have been updated!"
    popupmsg(msg, "SAVED!")

            

#---BUTTONS---------------------------------------------------------------------------------------------------------
#creating buttons
add_Button = Button(root, text = "Add a new entry",command = addClick).grid(row = 9, column = 1)
update_Button = Button(root, text = "Update an entry",command = upClick).grid(row = 9,column = 3)
delete_Button = Button(root, text = "Delete an entry", command = delClick).grid(row=9,column = 2)
search_Button = Button(root, text = "           Search           ", command = searchClick).grid(row = 49, column = 1)
sort_Button = Button(root, text = "Sort the List by ->", command = sortClick).grid(row = 54, column = 0)
view_Button = Button(root, text = "View Details", command = viewClick).grid(row = 21, column = 110)
clear_Button = Button(root, text = "Clear the fields", command = clearClick).grid(row = 23, column = 1)
exit_Button = Button(root, text = "       EXIT        ", command = exitClick).grid(row = 50, column = 105)
open_Button = Button(root, text = "Open list", command = openClick). grid(row = 20, column = 110)
save_Button = Button(root, text = "Save Changes", command = saveClick).grid(row=10,column=4)



#main loop of the program
root.mainloop()
