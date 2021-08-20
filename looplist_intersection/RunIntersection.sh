python -c 'import loops_to_loop_name; loops_to_loop_name.convert("<looplist1>","<looplist1>" + "_A1","<looplist1>" + "_A2","a")'

python -c 'import loops_to_loop_name; loops_to_loop_name.convert("<looplist2>","<looplist2>" + "_B1","<looplist2>" + "_B2","b")'

python -c 'import pybedtools_intersect; pybedtools_intersect.intersect("<looplist1>" + "_A1","<looplist2>" + "_B1" ,"A1B1")'

python -c 'import pybedtools_intersect; pybedtools_intersect.intersect("<looplist1>" + "_A2","<looplist2>" + "_B2" ,"A2B2")'


python -c 'import filter; filter.filter("A1B1","A2B2","Loopslist_Intersect")'

