import MarksheetBean
from MarksheetBean import *
import MarksheetDao
from MarksheetDao import *

def testAdd():
    mb = MarksheetBean()
    mb.setId(9)
    mb.setName("sandee")
    #mb.setRollNumber(119)
    mb.setPhysics(64)
    mb.setChemistry(48)
    mb.setMaths(95)
    
    md = MarksheetDao()
    md.add(mb)
    
def testUpdate():
    mb = MarksheetBean()
    mb.setPhysics(99)
    
    md = MarksheetDao()
    md.update(mb)
    
def testDelete():
    mb = MarksheetBean()
    mb.setId(9)
    
    md = MarksheetDao()
    md.delete(mb)
    
def testSearch():
    mb = MarksheetBean()
    
    md = MarksheetDao()
    md.search(mb)
    
def testGetRollNumber():
    mb = MarksheetBean()
    mb.setRollNumber(114)
    
    md = MarksheetDao()
    md.getRollNum(mb)
    
def testGetMeritList():
    mb = MarksheetBean()
    
    md = MarksheetDao()
    md.getMeritList(mb)
    
def testNextPK():
    mb = MarksheetBean()
    
    md = MarksheetDao()
    md.nextPk(mb)

    
#testSearch()
#testNextPK()
#testAdd()

    