class Sol:
    def backspace_compare(self,S,T):

        pos = S.find('#')
        while (pos>-1):
            if pos>0:
                S=S[0:pos-1]+S[pos+1:]
            else:
                S=S[pos+1:]
            pos = S.find('#')

        pos = T.find('#')
        while (pos > -1):
            if pos>0:
                T = T[0:pos - 1] + T[pos + 1:]
            else:
                T=T[pos+1:]
            pos = T.find('#')

        if S==T:
            return True
        return False

if __name__ == '__main__':
    p = Sol()
    print(p.backspace_compare(S = "a##c", T= "#a#c"))
