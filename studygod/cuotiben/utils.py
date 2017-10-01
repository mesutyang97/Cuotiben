import math
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

'''
input: an input string and a list of strings

output: return the top k matching strings
'''

def filter_by_category(input_s, stringList, k):
    result = sorted(stringList, key = lambda s : edit_distance(input_s, s))[:k]
    return result


def check_intersection(l1, l2):
    return len(list(set(l1) & set(l2))) != 0
'''
input: 
problems -> list of dictionary of ID, Category, Popularity, owner, a list of studygroups 
output: top k problems recommended to the user
'''

def recommend (problems, userID, k):
    owned_problem = {}
    total = 0
    for problem in problems:
        #if the problem is not public, the problem will not be recommended to him 
        if problem['owner'] is not None:
            #if the user owns the problem
            if userID == problem['owner']:
                total += 1
                #count the number of problems the user owns in this category 
                if owned_problem.has_key(problem['category']):
                    owned_problem[problem['category']] += 1
                else:
                    owned_problem[problem['category']] = 1 
    
    ratio = {}

    sorted_key = sorted(owned_problem.keys(), key = lambda k: owned_problem[k], reverse = True)
    
    num_elem = 0
    if total > k:
        for key in sorted_key:
            count = owned_problem[key]
            new_count = int(math.ceil(count * 1.0 / total*1.0 * k*1.0))
            num_elem += new_count
            if num_elem > k:
                new_count = k - num_elem + new_count
                ratio[key] = new_count
                break
            ratio[key] = new_count
    else:
        ratio = owned_problem

    result = []
    for key in ratio:
        result += sorted([p for p in problems if p['owner'] is None and p['category'] == key], 
                key = lambda problem: problem['Popularity'], reverse = True)[:ratio[key]]
    return result


        


"""
user = {'ID': 101, 'study_group': [1, 2, 3]}
userID = 101
problems = [{'ID' : 101, 'category' : 'Markov Chain', 'owner' : 101, 'Popularity' : 10}, 
            {'ID' : 102, 'category' : 'SQL', 'owner' : 101, 'Popularity' : 10},
            {'ID' : 103, 'category' : 'Markov Chain', 'owner' : 100, 'Popularity' : 20},
            {'ID' : 104, 'category' : 'Graph Theory', 'owner' : 101, 'Popularity' : 10},
            {'ID' : 105, 'category' : 'Master Theorem', 'owner' : 100, 'Popularity' : 30},
            {'ID' : 106, 'category' : 'Markov Chain', 'owner' : 101, 'Popularity' : 10},
            {'ID' : 107, 'category' : 'Markov Chain', 'owner' : None, 'Popularity' : 10}, 
            {'ID' : 108, 'category' : 'SQL', 'owner' : None, 'Popularity' : 10},
            {'ID' : 109, 'category' : 'Markov Chain', 'owner' : None, 'Popularity' : 20},
            {'ID' : 110, 'category' : 'Graph Theory', 'owner' : None, 'Popularity' : 10},
            {'ID' : 111, 'category' : 'Master Theorem', 'owner' : None, 'Popularity' : 30},
            {'ID' : 112, 'category' : 'Markov Chain', 'owner' : None, 'Popularity' : 10}]

print(recommend(problems, userID, 4))


'''
#the problem 
        #else if len(problems['study_group']) == 0:
        #check_intersection(problems['study_group'], user['study_group']):
'''

"""

