def sort_Roll(Roll_Number):
  #key for the insertion sort will stop at the element until the element previous to the key gets sorted
        
  for i in range(1,len(Roll_Number)): 
  #It will start from i=1,which is in our view first position where sorting reqd. between 1st and 2nd position
    k = Roll_Number[i]
    #created this variable because it is getting out of index when Roll_Number[m+1]=k i.e. we are inserting the unsorted element to it's correct position
    m = i-1
    #two conditions defined since loops breaks in both cases i.e. either comparison reaches to the first value reaches beginning or key becomes smaller than previous element
    while m>=0 and Roll_Number[m]>k:
      Roll_Number[m+1] = Roll_Number[m]
      m -= 1
    Roll_Number[m+1]= k       
  return clean(Roll_Number)

    #Since roll numbers of two candidates can't be same hence,we need to remove duplicate copies if created by us due to any mistake
B =[]
def clean(Sorted_Roll_Number):
  global B
  for i in range(0,len(Sorted_Roll_Number)):
    if Sorted_Roll_Number[i] != Sorted_Roll_Number[i-1]:
      B.append(Sorted_Roll_Number[i])
          
  return Sorted_Roll_Number