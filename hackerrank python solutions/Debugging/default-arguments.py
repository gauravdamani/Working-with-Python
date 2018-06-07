def print_from_stream(n, stream=EvenStream()):
    if stream_name=="even":
        n1=EvenStream()
        EvenStream.__init__(n1)
        for _ in range(n):
            print n1.get_next()
    else:
        for _ in range(n):
            print stream.get_next()