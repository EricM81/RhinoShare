import rhinoscriptsyntax as rs
import scriptcontext as sc
import eLib as e

def SelAllParents():
    objs = rs.GetObjects("Select objects to find all their parents", preselect=True)
    if objs: 
        count = len(objs)
        lastcount = 0
        while lastcount < count:
            lastcount = count
            rs.Command("_SelParents", False)
            count = len(rs.SelectedObjects(False, False))

        rs.Command("Isolate", True)




if (__name__ == "__main__"):
    SelAllParents()
