def linearSearchProdect(prodectlist,targetprodect):
    indices=[]
    for index,prodect in enumerate(prodectlist):
        if prodect == targetprodect:
            indices.append(index)
    return indices
prodect=['apple','banana','orange','apple','orange','apple','orange']
target='orange'
print(linearSearchProdect(prodect,target))
