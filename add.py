import zlib
import hashlib


def add(file_paths):
    for file_path in file_paths:
        key = hashlib.sha1(file_path.encode("utf-8")).hexdigest()
        with open(file_path, "r") as f:
            content = f.read()
        with open(f'.ygit/objects/{key}', "wb") as f:
            compressed_content = zlib.compress(bytes(content, "utf-8"))
            f.write(compressed_content)
        with open(f'.ygit/index', "ab") as f:
            f.write(zlib.compress(bytes(f"{key} {file_path}", "utf-8")))

if __name__ == "__main__":
    add(['test.txt'])