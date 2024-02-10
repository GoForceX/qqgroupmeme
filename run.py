import os

def d(f):
    if os.path.exists(f):
        os.remove(f)
        print(f"更新图片配置中")

def check_files(ff):
    files = []
    for fn in os.listdir(ff):
        if os.path.isfile(os.path.join(ff, fn)):
            files.append(fn)
    return files

def write_config(files, c_f):
    with open(c_f, 'a') as f:
        f.write('export default {\n')
        f.write('  items: [\n')
        for file in files:
            f.write(f'    "pic/{file}",\n')
        f.write('  ]\n')
        f.write('}\n')

def main():
    ff = 'pic'
    c_f = 'assets/scripts/config.js'
    d(c_f) 
    files = check_files(ff)
    if files:
        write_config(files, c_f)
        print("已更新 config.js")

if __name__ == "__main__":
    main()
