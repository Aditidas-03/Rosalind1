#k=homozygous dominant
#m=heterozygous
#n=homozygous recessive

def p_dom(k,m,n):
    
    tot_pop   = k+m+n
    homo_rec  = (n/tot_pop)* ((n-1)/(tot_pop-1))
    hetero    =(m/tot_pop) * ((m-1)/(tot_pop-1))
    hetro_rec =(m/tot_pop) * (n/(tot_pop-1)) + (n/tot_pop) * (m/(tot_pop-1))

    tot_rec =homo_rec + hetero*(1/4) + hetro_rec*(1/2)
    dom=1-tot_rec
    return dom

print(p_dom(24 ,17, 22))



    
