class DiffTriangle:

    def __init__(self):
        self.v = [None] * 15

    def copy(self):
        new = DiffTriangle()
        new.v = self.v.copy()
        return new

    def isValid(self):
        [a1,
         b1, b2,
         c1, c2, c3,
         d1, d2, d3, d4,
         e1, e2, e3, e4, e5] = self.v

        items = [i for i in self.v if i]
        reused = set(i for i in items if items.count(i) > 1)
        if len(reused) > 0:
            print(f'Reused items: {reused}')
            return False

        outOfBounds = [i for i in items if i < 1 or 15 < i]
        if len(outOfBounds) > 0:
            print(f'Out of bounds: {outOfBounds}')
            return False

        return (diffTest(a1, b1, b2) and
                diffTest(b1, c1, c2) and diffTest(b2, c2, c3) and
                diffTest(c1, d1, d2) and diffTest(c2, d2, d3) and diffTest(c3, d3, d4) and
                diffTest(d1, e1, e2) and diffTest(d2, e2, e3) and diffTest(d3, e3, e4) and
                diffTest(d4, e4, e5))

    def __repr__(self):
        return """DiffTriangle ({0}):
           {1:<2}
         {2:<2}  {3:2}
       {4:<2}  {5:2}  {6:2}
     {7:<2}  {8:<2}  {9:2}  {10:2}
   {11:<2}  {12:2}  {13:2}  {14:2}  {15:2}\n""".format(
            'valid' if self.isValid() else 'invalid',
            *['__' if i is None else i for i in self.v])


def diffTest(a, b, c):
    if b is not None and c is not None:
        if a == abs(b - c):
            return True

        print(a, '≠', b, '±', c)
        return False

    if b is None and c is None:
        return True

    print(a, '≠', b, '±', c)
    return False


def fillTriangle(dt, pos, options):
    dt = dt.copy()
    results = []

    if pos == 0:
        for opt in options:
            dt.v[pos] = opt
            new_options = [o for o in options if o != opt]
            results += fillTriangle(dt, pos + 1, new_options)

    if pos == 1:
        for opt in options:
            plus = opt + dt.v[0]
            minus = opt - dt.v[0]
            for after in [plus, minus]:
                if after in options:
                    dt.v[pos:pos + 2] = [opt, after]
                    new_options = [o for o in options if o not in [opt, after]]

                    results += fillTriangle(dt, pos + 2, new_options)

    if pos == 3:
        for opt in options:
            plus = opt + dt.v[1]
            minus = opt - dt.v[1]
            for after in [plus, minus]:
                if after in options:
                    dt.v[pos:pos + 2] = [opt, after]
                    new_options = [o for o in options if o not in [opt, after]]

                    results += fillTriangle(dt, pos + 2, new_options)

    if pos == 5:
        plus = dt.v[pos - 1] + dt.v[pos - 3]
        minus = dt.v[pos - 1] - dt.v[pos - 3]
        for after in [plus, minus]:
            if after in options:
                dt.v[pos] = after
                new_options = [o for o in options if o != after]
                results += fillTriangle(dt, pos + 1, new_options)

    if pos == 6:
        for opt in options:
            plus = opt + dt.v[3]
            minus = opt - dt.v[3]
            for after in [plus, minus]:
                if after in options:
                    dt.v[pos:pos + 2] = [opt, after]
                    new_options = [o for o in options if o not in [opt, after]]

                    results += fillTriangle(dt, pos + 2, new_options)

    if pos in [8, 9]:
        plus = dt.v[pos - 1] + dt.v[pos - 4]
        minus = dt.v[pos - 1] - dt.v[pos - 4]
        for after in [plus, minus]:
            if after in options:
                dt.v[pos] = after
                new_options = [o for o in options if o != after]
                results += fillTriangle(dt, pos + 1, new_options)

    if pos == 10:
        for opt in options:
            plus = opt + dt.v[6]
            minus = opt - dt.v[6]
            for after in [plus, minus]:
                if after in options:
                    dt.v[pos:pos + 2] = [opt, after]
                    new_options = [o for o in options if o not in [opt, after]]

                    results += fillTriangle(dt, pos + 2, new_options)

    if pos in [12, 13]:
        plus = dt.v[pos - 1] + dt.v[pos - 5]
        minus = dt.v[pos - 1] - dt.v[pos - 5]
        for after in [plus, minus]:
            if after in options:
                dt.v[pos] = after
                new_options = [o for o in options if o != after]
                results += fillTriangle(dt, pos + 1, new_options)

    if pos == 14:
        plus = dt.v[pos - 1] + dt.v[pos - 5]
        minus = dt.v[pos - 1] - dt.v[pos - 5]
        for after in [plus, minus]:
            if after in options:
                dt.v[pos] = after
                new_options = [o for o in options if o != after]

                if new_options:
                    print('WARN: Too many options for positions. Left over: ', new_options)
                print('Completed triangle!')
                results += [dt.copy()]

    return results

if __name__ == '__main__':
    # dt1 = DiffTriangle()
    # dt1.v[0:10] = [5, 4, 9, 6, 10, 1, 7, 13, 3, 4]
    # print(dt1)

    dt2 = DiffTriangle()
    dt2.v[0:3] = [5, 4, 9]
    results = fillTriangle(dt2, pos=3, options=[i for i in range(1, 16) if i not in dt2.v])
    print(results)

    dt3 = DiffTriangle()
    results = fillTriangle(dt3, pos=0, options=[i for i in range(1, 16) if i not in dt3.v])
    print(results)
