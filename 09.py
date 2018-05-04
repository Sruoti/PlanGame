def test(*params):
    print(len(params))
    print(params[6])
    for i in params:
        print(i)

test(1,2,3,4,5,'嘟嘟','棒棒哒')
