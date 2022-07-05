import os


def find_files(search_path: str, search_query: str) -> None:
  found_files = 0

  for root, _directory, files in os.walk(search_path):
    for file in files:
      if search_query in file:
        try:
          found_files += 1
          print_file_details(root, file)
        except PermissionError:
          print('Arquivo não permitido!!')
        except FileNotFoundError:
          print('Aquivo não encontrado :(')
        except Exception as error:
          print(f'Error desconhecido: {error}')

  print(f'{found_files} arquivo(s) encontrado(s).')

def print_file_details(root: str, file: str) -> None:
  full_path, file_name, file_ext, size = file_info(root, file)

  print(f'Arquivo encontrado: {file}')
  print(f'Caminho: {full_path}')
  print(f'Nome: {file_name}')
  print(f'Extensão: {file_ext}')
  print(f'Tamanho: {format_file_size(size)}')

def file_info(root: str, file: str) -> tuple:
  full_path = os.path.join(root, file)
  file_name, file_ext = os.path.splitext(file)
  size = os.path.getsize(full_path)

  return (full_path, file_name, file_ext, size)

def format_file_size(size: int) -> str:
  BASE = 1024
  kilo = BASE
  mega = BASE ** 2
  giga = BASE ** 3
  tera = BASE ** 4
  peta = BASE ** 5

  if size < kilo:
    notation = 'B'
  elif size < mega:
    size = new_file_size(size, kilo)
    notation = 'K'
  elif size < giga:
    size = new_file_size(size, mega)
    notation = 'M'
  elif size < tera:
    size = new_file_size(size, giga)
    notation = 'G'
  elif size < peta:
    size = new_file_size(size, tera)
    notation = 'T'
  else:
    size = new_file_size(size, peta)
    notation = 'P'

  return f'{size}{notation}'

def new_file_size(size: int, bytes: int) -> float:
  return round(size / bytes, 2)