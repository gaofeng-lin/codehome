# with open('C:/Users/76585/Desktop/shell/cfdname2/cfd_para.353',"r") as f:
            line=f.readline()
            while line:
                # new_line=re.split(r'(;, ,\t,=,\n)\s',str(line))
                new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
                # new_line=re.split('\W|\n\s',str(line))
                # new_line.remove("''")
                # new_list=list(new_line)
                
                # 去掉列表里面的 ''
                for i in new_line:
                    if i=='':
                        new_line.remove(i)
                
                if len(new_line)==3:
                    # print new_line
                    dict[new_line[1]]=[new_line[0],new_line[2]]
               
                
                
                line=f.readline()
            
            print dict