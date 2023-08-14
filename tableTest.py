import os


  
def main():
  print("| First | Second |")
  print("| --- | --- |")
  print("| 1 | 2 |")

  env_file = os.getenv('GITHUB_ENV')

  with open(env_file, "a") as myfile:
    myfile.write("TABLE_VAR=| First | Second |\n| --- | --- |\n| 1 | 2 |")
  
  return 0
if __name__ == "__main__":
    main()
