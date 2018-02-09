import webbrowser

lst1 = ["Codechef", "HackerEarth", "hackerrank"]
lst2 = ["https://www.codechef.com/users/","https://www.hackerearth.com/@","https://www.hackerrank.com/","?hr_r=1"]

for i in range(3):
    print("Enter "+lst1[i]+" handle: ", end="")
    handle = input()
    try:
        if i == 2:
            webbrowser.open(lst2[i]+handle+lst2[i+1])
        else:
            webbrowser.open(lst2[i]+handle)
    except Exception as ex:
        print("Some Error occured: "+str(ex))
