from find import find_files


if __name__ == "__main__":
  search_path = input('Digite um caminho: ')
  search_query = input('Digite um termo: ')

  find_files(search_path, search_query)