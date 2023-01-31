

def Transformation(all_names):
    top_5_per_week = [name[item] for item in range(5) for name in all_names]
    uniqe_top_fives = list(set(top_5_per_week))
    top_fives_sorted = sorted(uniqe_top_fives)
    return top_fives_sorted 

