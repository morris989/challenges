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
        sys.exit(0)
    except Exception as e:
        print e
        sys.exit(1)


def main(argv):
    n = Path(argv[3])
    d = Path(argv[2])
    p = Path(argv[1])
    if not n.is_file() or not d.is_dir() or not p.is_file():
        usage()
        return 1
    ft = open(p, "r")
    for pt in ft:
        extract(n, d, pt)
    ft.close()
    print("Password not in dictionary.")
    return 0


if __name__ == "__main__":
    main(sys.argv)
