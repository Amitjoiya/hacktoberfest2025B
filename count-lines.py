import os,sys
def count_lines(root, ext):
    total=0
    for dirpath,_,filenames in os.walk(root):
        for f in filenames:
            if f.endswith(ext):
                with open(os.path.join(dirpath,f),'rb') as fh:
                    total += sum(1 for _ in fh)
    return total
if __name__=="__main__":
    root = sys.argv[1] if len(sys.argv)>1 else '.'
    print("PY lines:", count_lines(root, '.py'))
