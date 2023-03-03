"""ex_5_0.py"""


def line_count(infile):
    fi=open(infile)
    lines=fi.readlines()
    return len(lines)



if __name__ == "__main__":
   
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
