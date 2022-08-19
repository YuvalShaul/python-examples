
def show_par(a, b, c):
    print('a:', a, 'b:', b, 'c:')

    

def show_par(a, b, /, c, d, *, e, f):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'e:', e, 'f:', f )

#     Try these:
#    
# show_par(c=5, b=6, a=7)
#  
# show_par(5, 6,  c=7)
#
# show_par(5, b=6,  c=7)
#  
# show_par(4, 5, 6, d=7, e=8, f=9)
# 
# show_par(4, 5, c=6, d=7, e=8, f=9)
#
# show_par(4, 5, 6, 7, e=8, f=9)
# 
# show_par(4, 5, 6, 7, 8, f=9)
# 
# show_par(4, 5, 6, 7, f=8, e=9)
# 
# show_par(4, 5, f=6, e=7, d=8, c=9)
# 