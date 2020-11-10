


import math



def millify(n):
    '''From StackOverFlow :-
                        https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers'''
    millnames = ['', ' K', ' M ', 'B ', ' T']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return str('{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx]))

def humanbytes(B):
        """
        From StackOverFlow
        """

        B = float(B)
        KB = float(1024)
        MB = float(KB ** 2)  # 1,048,576
        GB = float(KB ** 3)  # 1,073,741,824
        TB = float(KB ** 4)  # 1,099,511,627,776

        if B < KB:
            return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B / GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B / TB)

