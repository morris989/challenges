from pathlib import Path
import sys
import zipfile


def usage():
    print("python crackzip.py dictionary desfolder zipfile")


def extract(name, dest, password):
    try:
        zip_ref = zipfile.ZipFile(name, 'r')
        zip_ref.extractall(dest, pwd=password.strip())
        zip_ref.close()
        print("Zip succefull extracted with password: %s", password)
        sys.exit()
    except Exception as e:
        print e


def main():
    n = Path(sys.argv[3])
    d = Path(sys.argv[2])
    p = Path(sys.argv[1])
    if not n.is_file() or not d.is_dir() or not p.is_file():
        usage()
        return 1
    ft = open(p, "r")
    for pt in ft:
        extract(n, d, pt)
    ft.close()


if __name__ == "__main__":
    main()
