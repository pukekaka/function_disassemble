from idautils import *
from idaapi import *
from idc import *
idc.Wait()
ea = BeginEA()
output_directory = 'E:/Works/Data/samples/output/'
filename = idc.AskFile(1, "*.*", "Save list of basic blocks")
basename = idc.GetInputFile()
filename = basename + ".asmb"
fp = open(output_directory + filename,'w')
for funcea in Functions(SegStart(ea), SegEnd(ea)):
    functionName = GetFunctionName(funcea)
    for (startea, endea) in Chunks(funcea):
        for head in Heads(startea, endea):
        	text = functionName + ":" +"0x%08x"%(head)+":"+GetDisasm(head)+"\n"
        	fp.write(text)
        	#fp.write(functionName, ":", "0x%08x"%(head), ":", GetDisasm(head))
        	#print >> fp, "ss"
            #print >>fp, "%s : 0x%08x : %s" % functionName, head, GetDisasm(head)
            #print >>fp, "%#010x %#010x %s" % (first, idc.NextHead(i, endEA+1)-1, curName)
            #idc.GenerateFile(idc.OFILE_ASM, idc.GetInputFile()+".asmf", 0, idc.BADADDR, 0)
fp.close()
idc.Exit(0)