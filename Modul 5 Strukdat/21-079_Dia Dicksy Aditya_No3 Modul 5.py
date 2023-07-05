import turtle as t

def segitiga(length,level):
    if level==1:
        for i in range(3):
            t.fd(length)
            t.left(120)

    else:
        segitiga(length/2,level-1)
        t.fd(length/2)
        segitiga(length/2,level-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        segitiga(length/2,level-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

segitiga(100,3)