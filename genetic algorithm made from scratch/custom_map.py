def range_map(var,xi,xf,Xi,Xf):

	percent=(var-xi)/(xf-xi)

	new_var=Xi+(Xf-Xi)*percent

	return new_var


new_v=range_map(0.2,0,1,15,3)
print(new_v)