import idaapi
import idautils
import idc


output_path = 'E:/Works/Data/paper2/output/'

def extract_functions():

	filename = idc.AskFile(1, "*.*", "Save list of functions")
        exit = False
        if not filename:
            basename = idc.GetInputFile()
            filename = output_path + basename + ".fcn"
            idc.GenerateFile(idc.OFILE_ASM, output_path + basename + ".asm", 0, idc.BADADDR, 0)
            idc.GenerateFile(idc.OFILE_LST, output_path + basename + ".lst", 0, idc.BADADDR, 0)
            exit = True
	fp = open(filename,'w')
	funcs = idautils.Functions()
	for f in funcs:
		print >>fp, "%#010x %s" % (f, GetFunctionName(f))
        if exit:
            idc.Exit(100000000000)
			
q = None
f = None
idc.Wait()
extract_functions()