
def wrap(string, max_width):
    s=textwrap.wrap(string,max_width)
    s="\n".join(s)
    return s
    