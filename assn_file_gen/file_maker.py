def new_file_maker(file_name,file_props):
    new_file = open("./assignment"+file_props[5].zfill(2)+'/'+file_name+'.cpp','w')
    new_file.write("/*"+'*'*76+'*/\n')
    new_file.write("/*"+" Programmer: "+file_props[4]+" "*(63-len(file_props[4]))+'*/\n')
    new_file.write("/*"+' '*76+'*/\n')
    new_file.write("/* Program "+file_name+": "+file_props[0]+" "*(50 - len(file_props[0]))+'*/\n')
    new_file.write("/*"+' '*76+'*/\n')
    new_file.write("/*"+" Approximate completion time: "+str(file_props[3])+" minutes"+" "*36+'*/\n')
    new_file.write("/*"+'*'*76+'*/\n')

    new_file.write('\n')
    new_file.write('/*\n')
    new_file.write('   '+"This program "+file_props[1]+"."+'\n')
    new_file.write('*/\n')
    new_file.write('\n')
    new_file.write('#include <iostream>\n')
    new_file.write('using namespace std;\n')
    new_file.write('int main()\n')
    new_file.write('{\n')
    new_file.write('\n')
    new_file.write('  '+'return 0;\n')
    new_file.write('}\n')
    for i in range(int(file_props[2])):
        new_file.write("\n")
        func_str = """/******************************************************************************/
/* Function: FunctionName                                                     */
/*                                                                            */
/* Description: Brief description of what the function does                   */
/*                                                                            */
/* Data in: Brief description of parameters if any, none otherwise            */
/*                                                                            */
/* Data out: Brief description of the returned data if any, void otherwise    */
/******************************************************************************/\n"""
        new_file.write(func_str)


    new_file.close()

